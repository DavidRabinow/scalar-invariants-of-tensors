#!/usr/bin/env bash
# Request a safe stop of the autonomous local run (SIGINT/SIGTERM → checkpoint).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/autonomous_common.sh
source "${SCRIPT_DIR}/lib/autonomous_common.sh"

cd "${REPO_ROOT}"
export PYTHONPATH="${REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"

if [[ ! -f "${PID_FILE}" ]]; then
  echo "No PID file at ${PID_FILE}. Nothing to stop."
  exit 0
fi

PID="$(read_pid_file || true)"
if [[ -z "${PID}" ]]; then
  echo "PID file malformed; removing."
  rm -f "${PID_FILE}"
  exit 0
fi

if ! pid_is_running "${PID}"; then
  echo "Process ${PID} not running; removing stale PID file."
  rm -f "${PID_FILE}"
  exit 0
fi

# Prefer control-file stop so the controller checkpoints at an atomic boundary.
"${PYTHON:-python3}" - <<'PY'
from invariant_engine.controls import write_control
write_control("stop", source="stop_autonomous_local.sh")
print("Wrote safe-stop control request.")
PY

echo "Sent safe-stop request to PID ${PID} (also signaling TERM as backup)."
kill -TERM "${PID}" 2>/dev/null || true

# Wait briefly for exit + checkpoint.
for _ in $(seq 1 30); do
  if ! pid_is_running "${PID}"; then
    rm -f "${PID_FILE}"
    echo "Stopped."
    exit 0
  fi
  sleep 0.5
done

echo "Process still running after 15s. It may be finishing an atomic unit / checkpoint."
echo "Re-run status, or kill -INT ${PID} if needed. Force-kill is not the default."
exit 0
