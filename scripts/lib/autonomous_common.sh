#!/usr/bin/env bash
# Shared helpers for autonomous local runner scripts.
# Sourced by run/stop/status scripts; also exercised by tests.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
STATE_DIR="${REPO_ROOT}/research_state"
PID_FILE="${STATE_DIR}/autonomous.pid"
RUN_META="${STATE_DIR}/run_meta.json"
LOG_DIR="${STATE_DIR}/logs"
DASHBOARD_URL="http://127.0.0.1:8765"
CAFFEINATE_BIN="/usr/bin/caffeinate"
# Flags documented for operators:
#   -d  prevent display sleep
#   -i  prevent idle system sleep
#   -m  prevent disk idle sleep
#   -s  prevent system sleep while on AC power (conservative plugged-in mode)
#   -u  declare user activity
CAFFEINATE_FLAGS="-dimsu"

is_macos() {
  [[ "$(uname -s)" == "Darwin" ]]
}

caffeinate_available() {
  [[ -x "${CAFFEINATE_BIN}" ]]
}

detect_on_battery() {
  # Echo "yes", "no", or "unknown"
  if ! is_macos; then
    echo "unknown"
    return 0
  fi
  if ! command -v pmset >/dev/null 2>&1; then
    echo "unknown"
    return 0
  fi
  local out
  out="$(pmset -g batt 2>/dev/null || true)"
  if echo "${out}" | grep -qi "Battery Power"; then
    echo "yes"
  elif echo "${out}" | grep -qi "AC Power"; then
    echo "no"
  else
    echo "unknown"
  fi
}

pid_is_running() {
  local pid="$1"
  if [[ -z "${pid}" ]]; then
    return 1
  fi
  if kill -0 "${pid}" 2>/dev/null; then
    return 0
  fi
  return 1
}

read_pid_file() {
  if [[ ! -f "${PID_FILE}" ]]; then
    return 1
  fi
  # shellcheck disable=SC1090
  # PID file is KEY=value lines
  # shellcheck source=/dev/null
  source "${PID_FILE}"
  echo "${PID:-}"
}

remove_stale_pid_file() {
  if [[ ! -f "${PID_FILE}" ]]; then
    return 0
  fi
  local pid
  pid="$(read_pid_file || true)"
  if [[ -n "${pid}" ]] && pid_is_running "${pid}"; then
    return 1
  fi
  rm -f "${PID_FILE}"
  return 0
}

write_pid_file() {
  local pid="$1"
  local start_time="$2"
  local git_commit="$3"
  local config="$4"
  local log_path="$5"
  local checkpoint_path="$6"
  local wrapper_pid="${7:-}"
  mkdir -p "${STATE_DIR}" "${LOG_DIR}"
  # Quote values so CONFIGURATION=--preset degree8 does not break `source`.
  cat > "${PID_FILE}" <<EOF
PID='${pid}'
PYTHON_PID='${pid}'
WRAPPER_PID='${wrapper_pid}'
START_TIME='${start_time}'
GIT_COMMIT='${git_commit}'
CONFIGURATION='${config}'
LOG_PATH='${log_path}'
CHECKPOINT_PATH='${checkpoint_path}'
EOF
}

build_python_command() {
  # Prints the python argv as a bash array via stdout (space-separated, carefully quoted by caller).
  # Caller should pass remaining CLI args.
  local py="${PYTHON:-python3}"
  echo "${py}" -m invariant_engine run "$@"
}

wrap_with_caffeinate() {
  # Usage: wrap_with_caffeinate cmd arg...
  # Prints final argv words.
  if is_macos; then
    if ! caffeinate_available; then
      echo "ERROR: macOS detected but ${CAFFEINATE_BIN} is missing." >&2
      echo "Install macOS command-line tools or run on a Mac with caffeinate." >&2
      return 2
    fi
    echo "${CAFFEINATE_BIN}" "${CAFFEINATE_FLAGS}" -- "$@"
  else
    echo "$@"
  fi
}
