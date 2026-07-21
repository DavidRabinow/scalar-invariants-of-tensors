#!/bin/bash
set -euo pipefail
cd /Users/davidrabinow/Desktop/UPRS_pdf-highlighter/uprs/garments-for-good/research2
export PYTHONPATH=src
echo "AGENT_LOOP_TICK_brain81 $(date -u +%Y-%m-%dT%H:%M:%SZ)"
.venv/bin/python - <<'EOF'
from invariant_engine.brain import decide
from invariant_engine.heal import heal_stale_state
from pathlib import Path
import os, subprocess
d = decide()
print("decide", d.get("action"), d.get("found"), d.get("reason"), flush=True)
stale = d.get("status") in {"RUNNING","CHECKPOINTING","PAUSED"} and not d.get("alive")
if d.get("action")=="heal_restart" or stale:
    print("heal", heal_stale_state(reason="brain monitor"), flush=True)
    sp = Path("research_state/supervise.pid")
    need = True
    if sp.exists():
        try:
            os.kill(int(sp.read_text().strip()), 0)
            need = False
        except Exception:
            need = True
    if need:
        subprocess.Popen(["bash","scripts/start_forever_daemon.sh","--preset","overnight-10d","--offline","--allow-battery"], start_new_session=True)
        print("relaunched daemon", flush=True)
EOF
