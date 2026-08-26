"""
Core value-investing screener logic.

Philosophy (Graham / Buffett): price is what you pay, value is what you get.
The Graham checklist and value score below come entirely from the company's
actual financial statements (via yfinance) -- never from chart patterns.
A separate, optional price-momentum indicator (has the stock's price risen
every year) is also computed on user request; it is kept out of the value
score / checklist so it never distorts the fundamentals-based verdict, and
is offered purely as an extra, clearly-labeled filter for users who want it.
"""

import datetime
import json
import math
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yfinance as yf

from tickers import SET_TICKERS

CACHE_PATH = Path(__file__).parent / "cache.json"
CACHE_TTL_SECONDS = 12 * 60 * 60  # 12 hours


def _safe(value):
    """Convert NaN / None into plain None, leave everything else untouched."""
    if value is None:
        return None
    try:
        if isinstance(value, float) and math.isnan(value):
            return None
    except TypeError:
        return value
    return value


def _earnings_growth_streak(ticker_obj) -> tuple[bool | None, int, int]:
    """Check whether annual net income rose every year (no down years) over
    whatever history Yahoo Finance exposes for free (typically ~4-5 fiscal
    years). Returns (is_consistent, up_years_in_a_row, years_of_data)."""
    try:
        income_stmt = ticker_obj.income_stmt
        if income_stmt is None or income_stmt.empty or "Net Income" not in income_stmt.index:
            return None, 0, 0
        row = income_stmt.loc["Net Income"].dropna().sort_index()
        values = [float(v) for v in row.values]
    except Exception:
        return None, 0, 0

    if len(values) < 3:
        return None, 0, len(values)

    streak = 0
    for i in range(len(values) - 1, 0, -1):
        if values[i] > values[i - 1]:
            streak += 1
        else:
            break
    is_consistent = streak == len(values) - 1
    return is_consistent, streak, len(values)


def _price_growth_streak(ticker_obj) -> tuple[bool | None, int, int]:
    """Momentum overlay (not part of the value score): has the stock's
    year-end closing price risen every completed calendar year, over
    whatever history Yahoo Finance exposes for free (~5-6 years)?
    Returns (is_consistent, up_years_in_a_row, years_of_data)."""
    try:
        hist = ticker_obj.history(period="6y", interval="1d")
        if hist is None or hist.empty or "Close" not in hist.columns:
            return None, 0, 0
        yearly = hist["Close"].resample("YE").last().dropna()
        current_year = datetime.datetime.now().year
        yearly = yearly[yearly.index.year < current_year]
        values = [float(v) for v in yearly.values]
    except Exception:
        return None, 0, 0

    if len(values) < 3:
        return None, 0, len(values)

    streak = 0
    for i in range(len(values) - 1, 0, -1):
        if values[i] > values[i - 1]:
            streak += 1
        else:
            break
    is_consistent = streak == len(values) - 1
    return is_consistent, streak, len(values)


def _fetch_one(symbol: str, retries: int = 3) -> dict | None:
    for attempt in range(retries):
        try:
            return _fetch_one_inner(symbol)
        except Exception as exc:  # noqa: BLE001
            if "Too Many Requests" in str(exc) or "Rate limited" in str(exc):
                time.sleep(1.5 * (attempt + 1))
                continue
            print(f"[screener] failed to fetch {symbol}: {exc}")
            return None
    print(f"[screener] gave up on {symbol} after {retries} rate-limit retries")
    return None


def _fetch_one_inner(symbol: str) -> dict | None:
    t = yf.Ticker(symbol)
    info = t.info
    if not info or info.get("regularMarketPrice") is None and info.get("currentPrice") is None:
        return None

    price = _safe(info.get("currentPrice")) or _safe(info.get("regularMarketPrice"))
    eps = _safe(info.get("trailingEps"))
    bvps = _safe(info.get("bookValue"))
    pe = _safe(info.get("trailingPE"))
    pb = _safe(info.get("priceToBook"))
    roe = _safe(info.get("returnOnEquity"))
    de = _safe(info.get("debtToEquity"))  # percent, e.g. 45.2 == 0.45x
    current_ratio = _safe(info.get("currentRatio"))
    div_yield = _safe(info.get("dividendYield"))
    earnings_growth = _safe(info.get("earningsGrowth"))
    market_cap = _safe(info.get("marketCap"))
    name = info.get("longName") or info.get("shortName") or symbol
    sector = info.get("sector") or "N/A"

    # --- Intrinsic value: Graham Number = sqrt(22.5 * EPS * BVPS) ---
    graham_number = None
    margin_of_safety = None
    if eps is not None and bvps is not None and eps > 0 and bvps > 0:
        graham_number = math.sqrt(22.5 * eps * bvps)
        if price:
            margin_of_safety = (graham_number - price) / graham_number * 100

    # --- Consistent profit growth: net income up every year available ---
    consistent_growth, growth_streak_years, growth_data_years = _earnings_growth_streak(t)

    # --- Price momentum overlay (separate from the value checklist/score) ---
    consistent_price_growth, price_streak_years, price_data_years = _price_growth_streak(t)

    # --- Graham's 9-point defensive-investor checklist ---
    checklist = {
        "pe_reasonable": pe is not None and 0 < pe <= 15,
        "pb_reasonable": pb is not None and 0 < pb <= 1.5,
        "combined_pe_pb": (pe is not None and pb is not None and pe > 0 and pb > 0
                            and pe * pb <= 22.5),
        "current_ratio_ok": current_ratio is not None and current_ratio >= 2,
        "low_debt": de is not None and de <= 100,  # <=1.0x equity
        "profitable": eps is not None and eps > 0,
        "roe_ok": roe is not None and roe >= 0.15,
        "pays_dividend": div_yield is not None and div_yield > 0,
        "consistent_profit_growth": bool(consistent_growth),
    }
    checklist_score = sum(1 for v in checklist.values() if v)
    checklist_total = len(checklist)

    # --- Composite value score (0-100), MOS weighted heaviest ---
    mos_component = 0
    if margin_of_safety is not None:
        mos_component = max(-30, min(100, margin_of_safety)) * 0.5
    quality_component = (checklist_score / checklist_total) * 50

    value_score = round(max(0, mos_component + quality_component), 1)

    if margin_of_safety is None:
        verdict = "ข้อมูลไม่พอ (N/A)"
    elif margin_of_safety >= 30 and checklist_score >= 5:
        verdict = "Deep Value"
    elif margin_of_safety >= 10:
        verdict = "Undervalued"
    elif margin_of_safety > -10:
        verdict = "Fair Value"
    else:
        verdict = "Overvalued"

    return {
        "symbol": symbol,
        "name": name,
        "sector": sector,
        "price": price,
        "eps": eps,
        "bvps": bvps,
        "pe": pe,
        "pb": pb,
        "roe": roe,
        "debt_to_equity": de,
        "current_ratio": current_ratio,
        "dividend_yield": div_yield,
        "earnings_growth": earnings_growth,
        "market_cap": market_cap,
        "graham_number": graham_number,
        "margin_of_safety": margin_of_safety,
        "consistent_profit_growth": consistent_growth,
        "profit_growth_streak_years": growth_streak_years,
        "profit_growth_data_years": growth_data_years,
        "consistent_price_growth": consistent_price_growth,
        "price_growth_streak_years": price_streak_years,
        "price_growth_data_years": price_data_years,
        "checklist": checklist,
        "checklist_score": checklist_score,
        "checklist_total": checklist_total,
        "value_score": value_score,
        "verdict": verdict,
    }


def fetch_all(tickers: list[str] | None = None, max_workers: int = 8) -> list[dict]:
    tickers = tickers or SET_TICKERS
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_fetch_one, sym): sym for sym in tickers}
        for future in as_completed(futures):
            row = future.result()
            if row is not None:
                results.append(row)
    results.sort(key=lambda r: (r["margin_of_safety"] is None, -(r["margin_of_safety"] or -999)))
    return results


def load_cache() -> dict | None:
    if not CACHE_PATH.exists():
        return None
    try:
        data = json.loads(CACHE_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if time.time() - data.get("fetched_at", 0) > CACHE_TTL_SECONDS:
        return data  # stale but still usable; caller decides whether to refresh
    return data


def save_cache(rows: list[dict]) -> dict:
    data = {"fetched_at": time.time(), "rows": rows}
    CACHE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    return data


def get_screen(force_refresh: bool = False) -> dict:
    cache = load_cache()
    if force_refresh or cache is None:
        rows = fetch_all()
        if rows:
            cache = save_cache(rows)
        elif cache is None:
            cache = {"fetched_at": time.time(), "rows": []}
    return cache
