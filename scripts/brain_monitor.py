"""Detached 15-minute brain monitor for the 10D climb (PPID 1 / setsid)."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
STATE = REPO / "research_state"
LOG = STATE / "logs" / "brain_loop.log"
PID_FILE = STATE / "brain_loop.pid"
INTERVAL = int(os.environ.get("BRAIN_INTERVAL_SEC", "900"))


def _daemonize() -> None:
    if os.fork() > 0:
        time.sleep(0.3)
        sys.exit(0)
    os.setsid()
    if os.fork() > 0:
        sys.exit(0)
    os.chdir(REPO)
    os.umask(0)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", buffering=1) as lf:
        os.dup2(lf.fileno(), 1)
        os.dup2(lf.fileno(), 2)
    with open(os.devnull, "r") as dn:
        os.dup2(dn.fileno(), 0)
    PID_FILE.write_text(str(os.getpid()) + "\n", encoding="utf-8")


def main() -> None:
    _daemonize()
    sys.path.insert(0, str(REPO / "src"))
    print(f"brain monitor live pid={os.getpid()} interval={INTERVAL}s", flush=True)

    while True:
        time.sleep(INTERVAL)
        print("AGENT_LOOP_TICK_brain81", flush=True)
        try:
            from invariant_engine.brain import decide
            from invariant_engine.heal import heal_stale_state

            d = decide()
            print(
                f"decide action={d.get('action')} found={d.get('found')} "
                f"reason={d.get('reason')}",
                flush=True,
            )
            stale = d.get("status") in {"RUNNING", "CHECKPOINTING", "PAUSED"} and not d.get(
                "alive"
            )
            if d.get("action") == "heal_restart" or stale:
                print("heal", heal_stale_state(reason="brain monitor"), flush=True)
                sp = STATE / "supervise.pid"
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
                            str(REPO / "scripts" / "start_forever_daemon.sh"),
                            "--preset",
                            "overnight-10d",
                            "--offline",
                            "--allow-battery",
                        ],
                        cwd=str(REPO),
                        start_new_session=True,
                    )
                    print("relaunched forever daemon", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"brain monitor error: {exc}", flush=True)


if __name__ == "__main__":
    # Parent prints pid after child writes it
    if os.environ.get("BRAIN_DAEMON_CHILD") == "1":
        main()
    else:
        if PID_FILE.exists():
            try:
                old = int(PID_FILE.read_text().strip())
                os.kill(old, 0)
                print(f"already running: {old}")
                raise SystemExit(0)
            except Exception:
                PID_FILE.unlink(missing_ok=True)
        env = os.environ.copy()
        env["BRAIN_DAEMON_CHILD"] = "1"
        env["PYTHONPATH"] = str(REPO / "src") + (
            os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else ""
        )
        subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve())],
            cwd=str(REPO),
            env=env,
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(40):
            if PID_FILE.exists() and PID_FILE.read_text().strip():
                print(f"started brain monitor pid={PID_FILE.read_text().strip()}")
                raise SystemExit(0)
            time.sleep(0.05)
        print("failed to start brain monitor", file=sys.stderr)
        raise SystemExit(1)
