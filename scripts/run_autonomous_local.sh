#!/usr/bin/env bash
# Launch the autonomous invariant engine under macOS caffeinate (when available).
#
# Examples:
#   ./scripts/run_autonomous_local.sh --preset smoke
#   ./scripts/run_autonomous_local.sh --preset six-hour
#   ./scripts/run_autonomous_local.sh --preset overnight --offline
#   ./scripts/run_autonomous_local.sh --wall-hours 12 --max-degree 8
#
# Does not use sudo. Does not change permanent power settings.
# caffeinate stops automatically when the research process exits.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/autonomous_common.sh
source "${SCRIPT_DIR}/lib/autonomous_common.sh"

cd "${REPO_ROOT}"
mkdir -p "${STATE_DIR}" "${LOG_DIR}"

# Prefer project venv when present.
if [[ -z "${PYTHON:-}" && -x "${REPO_ROOT}/.venv/bin/python" ]]; then
  PYTHON="${REPO_ROOT}/.venv/bin/python"
fi
export PYTHONPATH="${REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"

ALLOW_BATTERY=0
WALL_HOURS=""
DETACH=0
ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --allow-battery)
      ALLOW_BATTERY=1
      ARGS+=("$1")
      shift
      ;;
    --detach)
      DETACH=1
      shift
      ;;
    --wall-hours)
      WALL_HOURS="$2"
      ARGS+=("$1" "$2")
      shift 2
      ;;
    --preset)
      ARGS+=("$1" "$2")
      # Infer wall hours from presets for battery gate when --wall-hours omitted.
      case "$2" in
        smoke) WALL_HOURS="${WALL_HOURS:-0.5}" ;;
        degree8) WALL_HOURS="${WALL_HOURS:-2}" ;;
        full) WALL_HOURS="${WALL_HOURS:-6}" ;;
        six-hour) WALL_HOURS="${WALL_HOURS:-6}" ;;
        overnight) WALL_HOURS="${WALL_HOURS:-12}" ;;
        ten-d) WALL_HOURS="${WALL_HOURS:-6}" ;;
        overnight-10d) WALL_HOURS="${WALL_HOURS:-12}" ;;
      esac
      shift 2
      ;;
    *)
      ARGS+=("$1")
      shift
      ;;
  esac
done

# Duplicate-run prevention
if [[ -f "${PID_FILE}" ]]; then
  OLD_PID="$(read_pid_file || true)"
  if [[ -n "${OLD_PID}" ]] && pid_is_running "${OLD_PID}"; then
    echo "ERROR: autonomous run already active (PID ${OLD_PID})." >&2
    echo "Use ./scripts/status_autonomous_local.sh or ./scripts/stop_autonomous_local.sh" >&2
    exit 1
  fi
  echo "Removing stale PID file ${PID_FILE}"
  rm -f "${PID_FILE}"
fi

# Battery gate (conservative: refuse long runs on battery unless --allow-battery)
ON_BATT="$(detect_on_battery)"
WALL_NUM="${WALL_HOURS:-0}"
if [[ "${ON_BATT}" == "yes" ]]; then
  if awk "BEGIN { exit !(${WALL_NUM} >= 1.0) }"; then
    if [[ "${ALLOW_BATTERY}" -ne 1 ]]; then
      echo "ERROR: Mac is on battery and this looks like a long run (wall_hours=${WALL_NUM})." >&2
      echo "Plug into AC power, or pass --allow-battery to override." >&2
      exit 1
    fi
  else
    echo "WARNING: Mac is on battery. Prefer AC power for research runs." >&2
  fi
fi

if is_macos; then
  if ! caffeinate_available; then
    echo "ERROR: macOS detected but ${CAFFEINATE_BIN} not found." >&2
    exit 2
  fi
  echo "Sleep prevention: ${CAFFEINATE_BIN} ${CAFFEINATE_FLAGS}"
  echo "  -d display  -i idle  -m disk  -s AC-system  -u user-activity"
else
  echo "Non-macOS ($(uname -s)): starting without caffeinate."
fi

GIT_COMMIT="$(git -C "${REPO_ROOT}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
START_TIME="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
STAMP="$(date +"%Y%m%dT%H%M%S")"
LOG_PATH="${LOG_DIR}/autonomous_${STAMP}.log"
CHECKPOINT_PATH="${STATE_DIR}/checkpoints"
CONFIG_STR="${ARGS[*]:-(defaults)}"

PY="${PYTHON:-python3}"
INNER=("${PY}" -m invariant_engine run "${ARGS[@]+"${ARGS[@]}"}")

echo "Dashboard: ${DASHBOARD_URL}"
echo "Log:       ${LOG_PATH}"
echo "Command:   ${INNER[*]}"
echo

# Launch under caffeinate on macOS. Forward signals to the python process.
# caffeinate is the parent; it exits when the child exits (no permanent settings).
if is_macos; then
  "${CAFFEINATE_BIN}" ${CAFFEINATE_FLAGS} -- "${INNER[@]}" >>"${LOG_PATH}" 2>&1 &
else
  "${INNER[@]}" >>"${LOG_PATH}" 2>&1 &
fi
WRAPPER_PID=$!

# Resolve PIDs: on macOS wrapper is caffeinate; python is its child.
sleep 0.4
PY_PID="${WRAPPER_PID}"
if is_macos && command -v pgrep >/dev/null 2>&1; then
  CHILD="$(pgrep -P "${WRAPPER_PID}" | head -n 1 || true)"
  if [[ -n "${CHILD}" ]]; then
    PY_PID="${CHILD}"
  fi
fi
# Only treat wrapper as python if the process *is* python (not caffeinate embedding python in argv).
WRAPPER_ARGS="$(ps -p "${WRAPPER_PID}" -o args= 2>/dev/null || true)"
if [[ "${WRAPPER_ARGS}" == *"/Python"* || "${WRAPPER_ARGS}" == *"python"* ]] \
  && [[ "${WRAPPER_ARGS}" != *"caffeinate"* ]]; then
  PY_PID="${WRAPPER_PID}"
fi

write_pid_file "${PY_PID}" "${START_TIME}" "${GIT_COMMIT}" "${CONFIG_STR}" "${LOG_PATH}" "${CHECKPOINT_PATH}" "${WRAPPER_PID}"

echo "Started autonomous run."
echo "  python PID: ${PY_PID}"
echo "  wrapper PID: ${WRAPPER_PID}"
echo "  git: ${GIT_COMMIT}"
echo "  dashboard: ${DASHBOARD_URL}"
echo "  (caffeinate ends automatically when the research process exits)"

if [[ "${DETACH}" -eq 1 ]]; then
  # Fully detach: do not wait, do not install EXIT traps that kill the child.
  echo "Detached mode: launcher exiting; research continues under caffeinate."
  echo "Stop with: ./scripts/stop_autonomous_local.sh"
  exit 0
fi

cleanup() {
  # Ensure checkpoint-friendly signal to python; then wait.
  if pid_is_running "${PY_PID}"; then
    kill -TERM "${PY_PID}" 2>/dev/null || true
  fi
  # Also terminate caffeinate wrapper if still up.
  if [[ "${WRAPPER_PID}" != "${PY_PID}" ]] && pid_is_running "${WRAPPER_PID}"; then
    kill -TERM "${WRAPPER_PID}" 2>/dev/null || true
  fi
}

forward_signal() {
  local sig="$1"
  echo "Forwarding ${sig} to python PID ${PY_PID}" >&2
  if pid_is_running "${PY_PID}"; then
    kill "-${sig}" "${PY_PID}" 2>/dev/null || true
  fi
}

trap 'forward_signal TERM' TERM
trap 'forward_signal INT' INT
trap cleanup EXIT

# Wait on wrapper (caffeinate or python). When it exits, caffeinate is gone.
set +e
wait "${WRAPPER_PID}"
RC=$?
set -e

# Clear traps before removing PID so EXIT cleanup doesn't double-signal.
trap - EXIT TERM INT
if [[ -f "${PID_FILE}" ]]; then
  CUR="$(read_pid_file || true)"
  if [[ "${CUR}" == "${PY_PID}" ]]; then
    rm -f "${PID_FILE}"
  fi
fi

echo "Autonomous run exited with code ${RC}"
exit "${RC}"
