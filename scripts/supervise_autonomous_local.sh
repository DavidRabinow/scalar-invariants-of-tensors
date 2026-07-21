#!/usr/bin/env bash
# Forever supervisor: restart after ANY crash until COMPLETE (clean) or STOPPED.
# Use MAX_ATTEMPTS=0 for unlimited. Default is effectively unlimited.
#
#   ./scripts/supervise_autonomous_local.sh --preset overnight-10d --offline --allow-battery
#
# Prefer launching via ./scripts/start_forever_daemon.sh so Cursor/IDE exit
# cannot kill the research loop.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/autonomous_common.sh
source "${SCRIPT_DIR}/lib/autonomous_common.sh"

cd "${REPO_ROOT}"
export PYTHONPATH="${REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"
if [[ -z "${PYTHON:-}" && -x "${REPO_ROOT}/.venv/bin/python" ]]; then
  PYTHON="${REPO_ROOT}/.venv/bin/python"
fi
PY="${PYTHON:-python3}"

# 0 = unlimited
MAX_ATTEMPTS="${MAX_ATTEMPTS:-0}"
BACKOFF_SEC="${BACKOFF_SEC:-8}"
ARGS=("$@")

FILTERED=()
for a in "${ARGS[@]+"${ARGS[@]}"}"; do
  [[ "$a" == "--detach" ]] && continue
  FILTERED+=("$a")
done
ARGS=("${FILTERED[@]+"${FILTERED[@]}"}")

echo "Supervisor: max_attempts=${MAX_ATTEMPTS:-unlimited} backoff=${BACKOFF_SEC}s"
echo "Dashboard: ${DASHBOARD_URL}"
echo "Args: ${ARGS[*]:-(defaults)}"
echo

attempt=1
while true; do
  if [[ "${MAX_ATTEMPTS}" -gt 0 && "${attempt}" -gt "${MAX_ATTEMPTS}" ]]; then
    echo "Supervisor: giving up after ${MAX_ATTEMPTS} attempts."
    exit 1
  fi

  LIMIT_LABEL="${MAX_ATTEMPTS}"
  [[ "${MAX_ATTEMPTS}" -eq 0 ]] && LIMIT_LABEL="∞"
  echo "======== attempt ${attempt}/${LIMIT_LABEL} $(date -u +%Y-%m-%dT%H:%M:%SZ) ========"

  "${PY}" - <<'PY'
from invariant_engine.heal import heal_stale_state
r = heal_stale_state(reason="supervisor pre-attempt")
print("heal:", r)
PY

  set +e
  "${SCRIPT_DIR}/run_autonomous_local.sh" "${ARGS[@]+"${ARGS[@]}"}"
  RC=$?
  set -e

  echo "Attempt ${attempt} exited with code ${RC}"

  STATUS="$("${PY}" - <<'PY'
import json
from pathlib import Path
p = Path("research_state/live_progress.json")
if not p.exists():
    print("MISSING")
else:
    print(json.loads(p.read_text()).get("status", "UNKNOWN"))
PY
)"

  echo "live_progress status: ${STATUS}"

  if [[ "${RC}" -eq 0 && "${STATUS}" == "COMPLETE" ]]; then
    echo "Supervisor: SUCCESS — run COMPLETE."
    exit 0
  fi

  if [[ "${RC}" -eq 0 && "${STATUS}" == "STOPPED" ]]; then
    echo "Supervisor: clean STOPPED (user stop). Not restarting."
    exit 0
  fi

  # Anything else (SIGKILL, ERROR, stale COMPLETE, non-zero) → heal and retry forever
  "${PY}" - <<'PY'
from invariant_engine.heal import heal_stale_state
print(heal_stale_state(reason="supervisor post-crash"))
PY

  echo "Supervisor: auto-heal restart in ${BACKOFF_SEC}s…"
  sleep "${BACKOFF_SEC}"
  attempt=$((attempt + 1))
done
