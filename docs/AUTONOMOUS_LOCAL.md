# Autonomous local overnight runs

Mandatory infrastructure before any unattended overnight run.

## What is local vs what needs internet

| Component | Needs Wi-Fi? |
|-----------|----------------|
| Cursor Agent (code generation / chat) | **Yes** |
| Cursor Background Agents (remote) | **Yes** — not a local Mac run |
| `invariant_engine` Python process | **No** (after `pip install`) |
| Local dashboard at `127.0.0.1:8765` | **No** |
| Reading checkpoints / reports on this Mac | **No** |

Once implementation is complete, the research process runs on this Mac without Cursor and without Wi-Fi.

## One-time setup (online)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verify offline readiness

```bash
PYTHONPATH=src python3 -m invariant_engine check-offline
```

## Start dashboard

```bash
PYTHONPATH=src python3 -m invariant_engine dashboard
# → http://127.0.0.1:8765
```

## Start a run (caffeinate is automatic on macOS)

```bash
./scripts/run_autonomous_local.sh --preset smoke
./scripts/run_autonomous_local.sh --preset six-hour
./scripts/run_autonomous_local.sh --preset overnight --offline
./scripts/run_autonomous_local.sh --wall-hours 12 --max-degree 8
```

On macOS the launcher wraps the Python process in:

```text
/usr/bin/caffeinate -dimsu -- <python …>
```

| Flag | Meaning |
|------|---------|
| `-d` | prevent display sleep |
| `-i` | prevent idle system sleep |
| `-m` | prevent disk idle sleep |
| `-s` | prevent system sleep while on AC power |
| `-u` | declare user activity |

No `sudo`. No permanent power-setting changes. `caffeinate` ends when the research process exits.

Long runs on battery are refused unless you pass `--allow-battery`.

## Status / stop

```bash
./scripts/status_autonomous_local.sh
./scripts/status_autonomous_local.sh --open
./scripts/stop_autonomous_local.sh
```

## Presets

| Preset | Wall | Notes |
|--------|------|-------|
| `smoke` | 30 min | Low workers; no progression beyond next uncertified phase; validation + checkpoint/resume test |
| `six-hour` | 6 h | Conservative RAM; degree-6 work or degree-8 planning |
| `overnight` | 12 h | AC power required by default; checkpoint every 10 min; certified transitions only |

## Structured progress (not terminal scraping)

- `research_state/live_progress.json` — atomic snapshot for the dashboard
- `research_state/events.jsonl` — append-only event log

## Acceptance gates (do not overnight until all pass)

1. `caffeinate` used automatically on macOS
2. Signal handling produces a valid checkpoint
3. Duplicate-run prevention works
4. Smoke run completes
5. Pause/resume works
6. Dashboard reflects structured progress
7. Dashboard survives engine restart (reads files)
8. Offline readiness passes
9. Offline smoke succeeds with Wi-Fi-independent project code
10. No external web assets in the dashboard
11. Existing 6D and 10D certified regressions still pass

```bash
PYTHONPATH=src python3 -m unittest \
  tests.test_hodge10 tests.test_graphs_6d \
  tests.test_runner_power tests.test_autonomous_infra \
  tests.test_offline_dashboard tests.test_autonomous_smoke -v
```

## Auto-heal / supervise (recommended in your own Terminal)

Runs die hard on heavy N=8 soaks (SIGKILL). The degree8 preset now skips that soak,
does real 6D discovery for N=2/4/6, and a **supervisor** restarts after crashes:

```bash
cd /path/to/research2
source .venv/bin/activate
./scripts/supervise_autonomous_local.sh --preset degree8 --offline --allow-battery
```

Or a single attempt:

```bash
./scripts/run_autonomous_local.sh --preset degree8 --offline --allow-battery
```

Heal stale RUNNING markers without starting:

```bash
PYTHONPATH=src python3 -c 'from invariant_engine.heal import heal_stale_state; print(heal_stale_state())'
```
