"""Local research dashboard — localhost only, file-backed, no CDN."""

from __future__ import annotations

import json
import os
import time

from flask import Flask, Response, jsonify, request, send_from_directory

from ..atomic_io import atomic_write_json
from ..controls import write_control
from ..paths import (
    DASHBOARD_STATIC,
    DEFAULT_DASHBOARD_HOST,
    DEFAULT_DASHBOARD_PORT,
    EVENTS_LOG,
    LIVE_PROGRESS,
    PID_FILE,
    RUN_META,
    ensure_state_dirs,
)
from ..progress import baseline_live_progress, load_live_progress, read_recent_events


def create_app() -> Flask:
    ensure_state_dirs()
    app = Flask(
        __name__,
        static_folder=str(DASHBOARD_STATIC),
        static_url_path="/static",
    )

    @app.after_request
    def _localhost_only(resp):  # type: ignore[no-untyped-def]
        resp.headers["X-Invariant-Engine"] = "local-only"
        return resp

    @app.get("/")
    def index():
        return send_from_directory(DASHBOARD_STATIC, "index.html")

    @app.get("/api/progress")
    def api_progress():
        return jsonify(load_live_progress(LIVE_PROGRESS))

    @app.get("/api/events")
    def api_events():
        limit = min(int(request.args.get("limit", 100)), 500)
        return jsonify({"events": read_recent_events(EVENTS_LOG, limit=limit)})

    @app.get("/api/meta")
    def api_meta():
        if RUN_META.exists():
            return jsonify(json.loads(RUN_META.read_text(encoding="utf-8")))
        return jsonify({})

    @app.get("/api/stream")
    def api_stream():
        def gen():
            last = ""
            while True:
                data = load_live_progress(LIVE_PROGRESS)
                payload = json.dumps(data, default=str)
                if payload != last:
                    yield f"event: progress\ndata: {payload}\n\n"
                    last = payload
                else:
                    yield f"event: heartbeat\ndata: {json.dumps({'t': time.time()})}\n\n"
                time.sleep(1.5)

        return Response(gen(), mimetype="text/event-stream")

    @app.post("/api/control")
    def api_control():
        if request.remote_addr not in {"127.0.0.1", "::1"}:
            return jsonify({"ok": False, "error": "controls restricted to localhost"}), 403
        body = request.get_json(force=True, silent=True) or {}
        action = body.get("action")
        try:
            req = write_control(str(action), source="dashboard", detail=str(body.get("detail", "")))
        except ValueError as exc:
            return jsonify({"ok": False, "error": str(exc)}), 400
        return jsonify({"ok": True, "request": req})

    @app.get("/api/health")
    def health():
        return jsonify({"ok": True, "host": DEFAULT_DASHBOARD_HOST, "port": DEFAULT_DASHBOARD_PORT})

    return app


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def run_dashboard(host: str = DEFAULT_DASHBOARD_HOST, port: int = DEFAULT_DASHBOARD_PORT) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise SystemExit("Dashboard must bind to localhost only (127.0.0.1).")
    ensure_state_dirs()

    need_baseline = True
    if LIVE_PROGRESS.exists():
        cur = load_live_progress(LIVE_PROGRESS)
        pid = cur.get("pid")
        live_proc = bool(pid) and _pid_alive(int(pid))
        autonomous = PID_FILE.exists()
        if live_proc or autonomous:
            need_baseline = False
        elif cur.get("status") in {"RUNNING", "PAUSED", "CHECKPOINTING"}:
            need_baseline = True
        else:
            # Refresh certified frontier even on idle files so UI stays honest.
            need_baseline = cur.get("certified_frontier", {}).get("largest_certified_degree", 0) < 8
    if need_baseline:
        atomic_write_json(LIVE_PROGRESS, baseline_live_progress())
    app = create_app()
    print(f"Dashboard: http://{host}:{port}")
    print("Local-only. No cloud. No telemetry.")
    app.run(host=host, port=port, debug=False, threaded=True)
