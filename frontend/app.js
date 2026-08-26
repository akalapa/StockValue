function initTheme() {
  const btn = document.getElementById("themeToggle");
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)");
  function currentTheme() {
    return document.documentElement.getAttribute("data-theme") || (systemDark.matches ? "dark" : "light");
  }
  function updateIcon() {
    btn.textContent = currentTheme() === "dark" ? "🌙" : "☀️";
  }
  btn.addEventListener("click", () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
    updateIcon();
  });
  updateIcon();
}
initTheme();

const state = {
  rows: [],
  sortKey: "margin_of_safety",
  sortDir: -1,
  fetchedAt: null,
};

const els = {
  status: document.getElementById("status"),
  tbody: document.getElementById("tableBody"),
  search: document.getElementById("search"),
  mosMin: document.getElementById("mosMin"),
  mosVal: document.getElementById("mosVal"),
  priceMin: document.getElementById("priceMin"),
  priceMax: document.getElementById("priceMax"),
  priceVal: document.getElementById("priceVal"),
  peMax: document.getElementById("peMax"),
  peVal: document.getElementById("peVal"),
  roeMin: document.getElementById("roeMin"),
  roeVal: document.getElementById("roeVal"),
  onlyProfitable: document.getElementById("onlyProfitable"),
  onlyGrowingProfit: document.getElementById("onlyGrowingProfit"),
  onlyRisingPrice: document.getElementById("onlyRisingPrice"),
  refreshBtn: document.getElementById("refreshBtn"),
  table: document.getElementById("stockTable"),
};

function fmtNum(v, digits = 2) {
  if (v === null || v === undefined || Number.isNaN(v)) return "-";
  return v.toLocaleString("en-US", { minimumFractionDigits: digits, maximumFractionDigits: digits });
}

function fmtPct(v, digits = 1) {
  if (v === null || v === undefined || Number.isNaN(v)) return "-";
  return v.toFixed(digits) + "%";
}

function profitGrowthLabel(r) {
  const dataYears = r.profit_growth_data_years;
  const streakYears = r.profit_growth_streak_years;
  if (dataYears === null || dataYears === undefined || dataYears < 3) return "N/A";
  if (r.consistent_profit_growth === true) return `✓ ${streakYears} ปี`;
  return `✗ (${streakYears ?? 0}/${dataYears - 1})`;
}

function priceGrowthLabel(r) {
  const dataYears = r.price_growth_data_years;
  const streakYears = r.price_growth_streak_years;
  if (dataYears === null || dataYears === undefined || dataYears < 3) return "N/A";
  if (r.consistent_price_growth === true) return `✓ ${streakYears} ปี`;
  return `✗ (${streakYears ?? 0}/${dataYears - 1})`;
}

function verdictBadge(verdict) {
  const map = {
    "Deep Value": "badge-deep",
    "Undervalued": "badge-under",
    "Fair Value": "badge-fair",
    "Overvalued": "badge-over",
  };
  const cls = map[verdict] || "badge-na";
  const label = verdict === "ข้อมูลไม่พอ (N/A)" ? "N/A" : verdict;
  return `<span class="badge ${cls}">${label}</span>`;
}

async function loadData(forceRefresh = false) {
  els.status.textContent = forceRefresh ? "กำลังรีเฟรชข้อมูลจาก Yahoo Finance..." : "กำลังโหลดข้อมูล...";
  els.refreshBtn.disabled = true;
  try {
    const res = await fetch(`/api/screen${forceRefresh ? "?refresh=true" : ""}`);
    const data = await res.json();
    state.rows = data.rows || [];
    state.fetchedAt = data.fetched_at;
    render();
  } catch (err) {
    els.status.textContent = "โหลดข้อมูลไม่สำเร็จ: " + err;
  } finally {
    els.refreshBtn.disabled = false;
  }
}

function applyFilters(rows) {
  const q = els.search.value.trim().toLowerCase();
  const mosMin = Number(els.mosMin.value);
  const priceMin = Number(els.priceMin.value);
  const priceMax = Number(els.priceMax.value);
  const peMax = Number(els.peMax.value);
  const roeMin = Number(els.roeMin.value);
  const onlyProfitable = els.onlyProfitable.checked;
  const onlyGrowingProfit = els.onlyGrowingProfit.checked;
  const onlyRisingPrice = els.onlyRisingPrice.checked;

  return rows.filter((r) => {
    if (q && !(r.symbol.toLowerCase().includes(q) || (r.name || "").toLowerCase().includes(q))) return false;
    if (r.margin_of_safety !== null && r.margin_of_safety < mosMin) return false;
    if (mosMin > -50 && r.margin_of_safety === null) return false;
    if (priceMax < 400 && (r.price === null || r.price > priceMax)) return false;
    if (priceMin > 0 && (r.price === null || r.price < priceMin)) return false;
    if (peMax < 40 && (r.pe === null || r.pe > peMax)) return false;
    if (roeMin > 0 && (r.roe === null || r.roe * 100 < roeMin)) return false;
    if (onlyProfitable && (r.eps === null || r.eps <= 0)) return false;
    if (onlyGrowingProfit && r.consistent_profit_growth !== true) return false;
    if (onlyRisingPrice && r.consistent_price_growth !== true) return false;
    return true;
  });
}

function sortRows(rows) {
  const { sortKey, sortDir } = state;
  return [...rows].sort((a, b) => {
    let av = a[sortKey];
    let bv = b[sortKey];
    if (av === null || av === undefined) return 1;
    if (bv === null || bv === undefined) return -1;
    if (typeof av === "string") return sortDir * av.localeCompare(bv);
    return sortDir * (av - bv);
  });
}

function updateSortIndicators() {
  els.table.querySelectorAll("thead th").forEach((th) => {
    const arrow = th.querySelector(".sort-arrow");
    if (th.dataset.key === state.sortKey) {
      th.classList.add("sorted");
      arrow.textContent = state.sortDir === 1 ? "▲" : "▼";
    } else {
      th.classList.remove("sorted");
      arrow.textContent = "";
    }
  });
}

function render() {
  updateSortIndicators();
  const filtered = sortRows(applyFilters(state.rows));
  els.tbody.innerHTML = filtered
    .map((r) => {
      const mosClass = r.margin_of_safety === null ? "mos-na" : r.margin_of_safety >= 0 ? "mos-positive" : "mos-negative";
      const code = r.symbol.replace(".BK", "");
      const setUrl = `https://www.set.or.th/th/market/product/stock/quote/${code}/financial-statement/company-highlights`;
      return `<tr>
        <td class="symbol-cell"><a href="${setUrl}" target="_blank" rel="noopener noreferrer">${code}</a></td>
        <td class="name-cell" title="${r.name}">${r.name}</td>
        <td>${r.sector}</td>
        <td>${fmtNum(r.price)}</td>
        <td>${r.graham_number !== null ? fmtNum(r.graham_number) : "-"}</td>
        <td class="${mosClass}">${r.margin_of_safety !== null ? fmtPct(r.margin_of_safety) : "N/A"}</td>
        <td>${r.pe !== null ? fmtNum(r.pe) : "-"}</td>
        <td>${r.pb !== null ? fmtNum(r.pb) : "-"}</td>
        <td>${r.roe !== null ? fmtPct(r.roe * 100) : "-"}</td>
        <td>${r.debt_to_equity !== null ? fmtPct(r.debt_to_equity, 0) : "-"}</td>
        <td>${r.dividend_yield !== null ? fmtPct(r.dividend_yield) : "-"}</td>
        <td class="${r.consistent_profit_growth === true ? "mos-positive" : ""}">${profitGrowthLabel(r)}</td>
        <td class="${r.consistent_price_growth === true ? "mos-positive" : ""}">${priceGrowthLabel(r)}</td>
        <td class="checklist-score">${r.checklist_score}/${r.checklist_total}</td>
        <td>${fmtNum(r.value_score, 1)}</td>
        <td>${verdictBadge(r.verdict)}</td>
      </tr>`;
    })
    .join("");

  const ts = state.fetchedAt ? new Date(state.fetchedAt * 1000).toLocaleString("th-TH") : "-";
  els.status.textContent = `แสดง ${filtered.length} จาก ${state.rows.length} หุ้น | ข้อมูลล่าสุด: ${ts} (ที่มา: Yahoo Finance)`;
}

els.search.addEventListener("input", render);
els.mosMin.addEventListener("input", () => {
  els.mosVal.textContent = els.mosMin.value + "%";
  render();
});
function updatePriceLabel() {
  const min = Number(els.priceMin.value);
  const max = Number(els.priceMax.value);
  els.priceVal.textContent = `${min} - ${max >= 400 ? "ไม่กำหนด" : max}`;
}
els.priceMin.addEventListener("input", () => {
  if (Number(els.priceMin.value) > Number(els.priceMax.value)) {
    els.priceMin.value = els.priceMax.value;
  }
  updatePriceLabel();
  render();
});
els.priceMax.addEventListener("input", () => {
  if (Number(els.priceMax.value) < Number(els.priceMin.value)) {
    els.priceMax.value = els.priceMin.value;
  }
  updatePriceLabel();
  render();
});
els.peMax.addEventListener("input", () => {
  els.peVal.textContent = els.peMax.value == 40 ? "ไม่กำหนด" : els.peMax.value;
  render();
});
els.roeMin.addEventListener("input", () => {
  els.roeVal.textContent = els.roeMin.value + "%";
  render();
});
els.onlyProfitable.addEventListener("change", render);
els.onlyGrowingProfit.addEventListener("change", render);
els.onlyRisingPrice.addEventListener("change", render);
els.refreshBtn.addEventListener("click", () => loadData(true));

els.table.querySelectorAll("thead th").forEach((th) => {
  th.addEventListener("click", () => {
    const key = th.dataset.key;
    if (state.sortKey === key) {
      state.sortDir *= -1;
    } else {
      state.sortKey = key;
      state.sortDir = key === "symbol" || key === "name" || key === "sector" || key === "verdict" ? 1 : -1;
    }
    render();
  });
});

loadData(false);
