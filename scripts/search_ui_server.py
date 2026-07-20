#!/usr/bin/env python3
"""
Local UI + 15-minute 10D invariant search.

  python3 scripts/search_ui_server.py

Then open http://127.0.0.1:5055
"""

from __future__ import annotations

import json
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from flask import Flask, jsonify, send_from_directory  # noqa: E402

from invariants.timed_search import (  # noqa: E402
    PROGRESS_DEFAULT,
    SearchProgress,
    run_timed_search,
    write_progress,
)

UI_DIR = ROOT / "ui"
PROGRESS_PATH = PROGRESS_DEFAULT
DURATION_SEC = 15 * 60

app = Flask(__name__, static_folder=str(UI_DIR), static_url_path="")
_lock = threading.Lock()
_worker: threading.Thread | None = None


def _ensure_progress_file() -> None:
    if not PROGRESS_PATH.exists():
        write_progress(
            PROGRESS_PATH,
            SearchProgress(
                status="idle",
                duration_sec=DURATION_SEC,
                message="Click “Start 15-minute search” to begin.",
            ),
        )


@app.get("/")
def index():
    return send_from_directory(UI_DIR, "index.html")


@app.get("/api/progress")
def progress():
    _ensure_progress_file()
    return jsonify(json.loads(PROGRESS_PATH.read_text()))


@app.post("/api/start")
def start():
    global _worker
    with _lock:
        if _worker is not None and _worker.is_alive():
            return jsonify({"ok": False, "error": "Search already running."}), 409

        def job():
            run_timed_search(
                duration_sec=DURATION_SEC,
                progress_path=PROGRESS_PATH,
                n_draws=64,
                seed=7,
            )

        write_progress(
            PROGRESS_PATH,
            SearchProgress(
                status="running",
                duration_sec=DURATION_SEC,
                message="Search thread starting…",
            ),
        )
        _worker = threading.Thread(target=job, daemon=True)
        _worker.start()
    return jsonify({"ok": True, "message": f"Started {DURATION_SEC // 60}-minute search."})


def main() -> None:
    _ensure_progress_file()
    print("UI:  http://127.0.0.1:5055")
    print("API: http://127.0.0.1:5055/api/progress")
    print("Click Start in the UI for a 15-minute search.")
    app.run(host="127.0.0.1", port=5055, debug=False, threaded=True)


if __name__ == "__main__":
    main()
