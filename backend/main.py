from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from screener import get_screen

FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app = FastAPI(title="Value Screener (SET)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/screen")
def api_screen(refresh: bool = Query(False)):
    data = get_screen(force_refresh=refresh)
    return data


@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR)), name="frontend")
