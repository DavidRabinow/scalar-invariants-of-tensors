#!/usr/bin/env bash
# Durable 15-minute brain monitor (survives Cursor exit).
# Double-fork via Python; auto-heals dead runs and relaunches forever daemon.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/autonomous_common.sh
source "${SCRIPT_DIR}/lib/autonomous_common.sh"
cd "${REPO_ROOT}"
mkdir -p "${LOG_DIR}"
export PYTHONPATH="${REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"
PY="${REPO_ROOT}/.venv/bin/python"
[[ -x "$PY" ]] || PY=python3

if [[ -f "${STATE_DIR}/brain_loop.pid" ]]; then
  OLD="$(tr -d '[:space:]' <"${STATE_DIR}/brain_loop.pid" || true)"
  if [[ -n "${OLD}" ]] && kill -0 "${OLD}" 2>/dev/null; then
    echo "brain loop already running: ${OLD}"
    exit 0
  fi
  rm -f "${STATE_DIR}/brain_loop.pid"
fi

export REPO_ROOT
BRAIN_PID="$("${PY}" - <<'PY'
import os, sys, time, subprocess, json
from pathlib import Path

repo = Path(os.environ["REPO_ROOT"])
log = repo / "research_state" / "logs" / "brain_loop.log"
pid_path = repo / "research_state" / "brain_loop.pid"
log.parent.mkdir(parents=True, exist_ok=True)

if os.fork() > 0:
    for _ in range(80):
        if pid_path.exists() and pid_path.read_text().strip():
            print(pid_path.read_text().strip())
            sys.exit(0)
        time.sleep(0.05)
    print("0")
    sys.exit(1)

os.setsid()
if os.fork() > 0:
    sys.exit(0)

os.chdir(repo)
os.environ["PYTHONPATH"] = str(repo / "src")
lf = open(log, "a", buffering=1)
os.dup2(lf.fileno(), 1)
os.dup2(lf.fileno(), 2)
os.dup2(open(os.devnull, "r").fileno(), 0)
pid_path.write_text(str(os.getpid()) + "\n")
print(f"brain loop start pid={os.getpid()}", flush=True)

INTERVAL = int(os.environ.get("BRAIN_INTERVAL_SEC", "900"))

while True:
    time.sleep(INTERVAL)
    print("AGENT_LOOP_TICK_brain81", flush=True)
    try:
        sys.path.insert(0, str(repo / "src"))
        from invariant_engine.brain import decide
        from invariant_engine.heal import heal_stale_state

        d = decide()
        print(
            "decide",
            d.get("action"),
            "found",
            d.get("found"),
            d.get("reason"),
            flush=True,
        )
        stale = d.get("status") in {"RUNNING", "CHECKPOINTING", "PAUSED"} and not d.get(
            "alive"
        )
        if d.get("action") == "heal_restart" or stale:
            print("heal", heal_stale_state(reason="brain loop"), flush=True)
            sp = repo / "research_state" / "supervise.pid"
            need = True
            if sp.exists():
                try:
                    os.kill(int(sp.read_text().strip()), 0)
                    need = False
                except Exception:
                    need = True
            if need:
                subprocess.Popen(
                    [
                        "bash",
                        str(repo / "scripts" / "start_forever_daemon.sh"),
                        "--preset",
                        "overnight-10d",
                        "--offline",
                        "--allow-battery",
                    ],
                    cwd=str(repo),
                    start_new_session=True,
                )
                print("relaunched daemon", flush=True)
    except Exception as e:
        print("brain_loop error", e, flush=True)
PY
)"

echo "Brain monitor started (detached)."
echo "  pid: ${BRAIN_PID}"
echo "  log: ${LOG_DIR}/brain_loop.log"
echo "  interval: ${BRAIN_INTERVAL_SEC:-900}s"
