"""Canonical paths for research state, logs, and checkpoints."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RESEARCH_STATE = REPO_ROOT / "research_state"
LIVE_PROGRESS = RESEARCH_STATE / "live_progress.json"
EVENTS_LOG = RESEARCH_STATE / "events.jsonl"
CHECKPOINT_DIR = RESEARCH_STATE / "checkpoints"
CONTROL_DIR = RESEARCH_STATE / "controls"
LOG_DIR = RESEARCH_STATE / "logs"
RUN_META = RESEARCH_STATE / "run_meta.json"
PID_FILE = RESEARCH_STATE / "autonomous.pid"
DASHBOARD_STATIC = Path(__file__).resolve().parent / "dashboard" / "static"

DEFAULT_DASHBOARD_HOST = "127.0.0.1"
DEFAULT_DASHBOARD_PORT = 8765
DASHBOARD_URL = f"http://{DEFAULT_DASHBOARD_HOST}:{DEFAULT_DASHBOARD_PORT}"

SCOPE_DEFAULT = "connected metric-contraction graphs only"


def ensure_state_dirs() -> None:
    for path in (RESEARCH_STATE, CHECKPOINT_DIR, CONTROL_DIR, LOG_DIR):
        path.mkdir(parents=True, exist_ok=True)
