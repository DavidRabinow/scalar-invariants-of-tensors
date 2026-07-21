#!/usr/bin/env bash
# Fully detach the forever supervisor from Cursor/IDE/agent shells.
# Double-forks into its own session so parent exit cannot take it down.
#
#   ./scripts/start_forever_daemon.sh --preset overnight-10d --offline --allow-battery
#
# Stop research worker: ./scripts/stop_autonomous_local.sh
# Stop supervise loop:  kill "$(cat research_state/supervise.pid)"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/autonomous_common.sh
source "${SCRIPT_DIR}/lib/autonomous_common.sh"

cd "${REPO_ROOT}"
mkdir -p "${LOG_DIR}" "${STATE_DIR}"

if [[ -z "${PYTHON:-}" && -x "${REPO_ROOT}/.venv/bin/python" ]]; then
  PYTHON="${REPO_ROOT}/.venv/bin/python"
fi
export PYTHONPATH="${REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"
PY="${PYTHON:-python3}"

SUPERVISE_PID_FILE="${STATE_DIR}/supervise.pid"
DAEMON_LOG="${LOG_DIR}/supervise_daemon.log"
ARGS=("$@")

if [[ -f "${SUPERVISE_PID_FILE}" ]]; then
  OLD="$(tr -d '[:space:]' <"${SUPERVISE_PID_FILE}" || true)"
  if [[ -n "${OLD}" ]] && kill -0 "${OLD}" 2>/dev/null; then
    echo "ERROR: supervise already running (PID ${OLD})." >&2
    exit 1
  fi
  rm -f "${SUPERVISE_PID_FILE}"
fi

"${PY}" - <<'PY'
from invariant_engine.heal import heal_stale_state
print("heal:", heal_stale_state(reason="daemon pre-start"))
PY

export MAX_ATTEMPTS="${MAX_ATTEMPTS:-0}"
export BACKOFF_SEC="${BACKOFF_SEC:-8}"
export REPO_ROOT
export DAEMON_ARGS
DAEMON_ARGS="$(printf '%s\x1e' "${ARGS[@]+"${ARGS[@]}"}")"

DAEMON_PID="$("${PY}" - <<'PY'
import os
import sys
import time
from pathlib import Path

repo = Path(os.environ["REPO_ROOT"])
script = repo / "scripts" / "supervise_autonomous_local.sh"
log_path = repo / "research_state" / "logs" / "supervise_daemon.log"
pid_path = repo / "research_state" / "supervise.pid"
args = [a for a in os.environ.get("DAEMON_ARGS", "").split("\x1e") if a]

pid = os.fork()
if pid > 0:
    for _ in range(80):
        if pid_path.exists():
            text = pid_path.read_text(encoding="utf-8").strip()
            if text:
                print(text)
                sys.exit(0)
        time.sleep(0.05)
    print("0")
    sys.exit(1)

os.setsid()
if os.fork() > 0:
    sys.exit(0)

os.chdir(repo)
os.umask(0)
log_path.parent.mkdir(parents=True, exist_ok=True)
log_f = open(log_path, "a", buffering=1)
os.dup2(log_f.fileno(), 1)
os.dup2(log_f.fileno(), 2)
devnull = open(os.devnull, "r")
os.dup2(devnull.fileno(), 0)

pid_path.write_text(str(os.getpid()) + "\n", encoding="utf-8")
print(f"daemon supervise pid={os.getpid()} args={args}", flush=True)
os.execv("/bin/bash", ["bash", str(script), *args])
PY
)"

echo "Forever daemon started."
echo "  supervise PID: ${DAEMON_PID}"
echo "  pid file:      ${SUPERVISE_PID_FILE}"
echo "  daemon log:    ${DAEMON_LOG}"
echo "  dashboard:     ${DASHBOARD_URL}"
echo "  stop worker:   ./scripts/stop_autonomous_local.sh"
echo "  stop forever:  kill ${DAEMON_PID}"
sleep 2
tail -8 "${DAEMON_LOG}" 2>/dev/null || true
