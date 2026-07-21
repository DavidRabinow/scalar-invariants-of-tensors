# Lorentz Invariants of Forms (6D → 10D)

Extension of Elamaran–Ferko–Scarlett, *Machine Learning Invariants of Tensors* (arXiv:2512.23750).

## Goal

Find the **functionally independent Lorentz scalars** built from a *p*-form field strength (no derivatives), and the **syzygies** (polynomial relations) among candidate contractions.

| Case | Object | Known / target |
|------|--------|----------------|
| Reproduce | Generic 3-form \(H_{\mu\nu\rho}\) in \(d=6\) | **5** independent invariants |
| Extend | Chiral (self-dual) 5-form \(F^+_{\mu_1\ldots\mu_5}\) in \(d=10\) | **81** primary invariants (analytical count); need explicit generators + relations |

Physics payoff: the most general Lagrangian depending on the form but not its derivatives is an arbitrary function of those independent scalars. In 10D this controls ModMax-type / \(T\bar T\)-like flows for chiral 4-form theories (Type IIB \(F_5\)).

## Method (data-driven)

1. Enumerate inequivalent index contractions as graphs / tensor networks.
2. Evaluate them on many random numerical tensors.
3. Use SVD nullspaces to find linear relations at fixed order, then polynomial relations against products of lower-order invariants.
4. Stop when no new independent scalars appear for several consecutive orders.

## Layout

```
src/invariants/          # mathematical core (graphs, Hodge, discovery)
src/invariant_engine/    # autonomous runner, dashboard, offline checks
scripts/                 # CLIs + caffeinate launcher
research_state/          # live_progress.json, events, checkpoints (local)
docs/AUTONOMOUS_LOCAL.md # overnight / offline / dashboard ops
```

## Autonomous local runs (mandatory before overnight)

Full operator guide: [docs/AUTONOMOUS_LOCAL.md](docs/AUTONOMOUS_LOCAL.md).

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python3 -m invariant_engine check-offline
PYTHONPATH=src python3 -m invariant_engine dashboard   # http://127.0.0.1:8765
./scripts/run_autonomous_local.sh --preset smoke
./scripts/status_autonomous_local.sh
./scripts/stop_autonomous_local.sh
```

Presets: `--preset smoke` (30m) · `--preset six-hour` · `--preset overnight --offline`

On macOS the launcher wraps the engine in `/usr/bin/caffeinate -dimsu` automatically. Computation is fully local after install; Cursor Agent still needs internet to generate code.
