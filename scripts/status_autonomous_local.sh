#!/usr/bin/env bash
# Show autonomous local run status. Optional: --open opens the dashboard.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/autonomous_common.sh
source "${SCRIPT_DIR}/lib/autonomous_common.sh"

cd "${REPO_ROOT}"
OPEN_BROWSER=0
if [[ "${1:-}" == "--open" ]]; then
  OPEN_BROWSER=1
fi

echo "Autonomous local status"
echo "======================="
echo "Dashboard: ${DASHBOARD_URL}"

if [[ -f "${PID_FILE}" ]]; then
  # shellcheck disable=SC1090
  source "${PID_FILE}"
  echo "PID file:  ${PID_FILE}"
  echo "PID:       ${PID:-?}"
  echo "Started:   ${START_TIME:-?}"
  echo "Commit:    ${GIT_COMMIT:-?}"
  echo "Config:    ${CONFIGURATION:-?}"
  echo "Log:       ${LOG_PATH:-?}"
  echo "Checkpoint:${CHECKPOINT_PATH:-?}"
  if [[ -n "${PID:-}" ]] && pid_is_running "${PID}"; then
    echo "Process:   RUNNING"
  else
    echo "Process:   NOT RUNNING (stale PID file)"
  fi
else
  echo "PID file:  (none)"
  echo "Process:   STOPPED"
fi

if [[ -f "${STATE_DIR}/live_progress.json" ]]; then
  echo
  "${PYTHON:-python3}" - <<'PY'
import json
from pathlib import Path
p = Path("research_state/live_progress.json")
d = json.loads(p.read_text())
print(f"Status:    {d.get('status')}")
print(f"Task:      {d.get('current_task')}")
print(f"Elapsed:   {d.get('elapsed_sec')}")
print(f"Heartbeat: {d.get('heartbeat_at')}")
PY
fi

if [[ "${OPEN_BROWSER}" -eq 1 ]]; then
  if is_macos && command -v open >/dev/null 2>&1; then
    open "${DASHBOARD_URL}"
    echo "Opened ${DASHBOARD_URL}"
  else
    echo "Open ${DASHBOARD_URL} in your browser (open(1) not available)."
  fi
fi
