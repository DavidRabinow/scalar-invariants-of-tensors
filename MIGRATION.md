# Migration note

## What changed (2026-08-06)

The research-grade package `tensor_invariants/` replaces the previous
answer-key-centric 6D verification path as the primary scientific interface.

| Before (`src/invariants`, `src/invariant_engine`) | After (`tensor_invariants`, `run_pipeline.py`) |
|--------------------------------------------------|-----------------------------------------------|
| `run_6d.py` verifies hardcoded paper formulas | Blind discovery from weighted graphs + \(P_N\mid C_N\) |
| Ladder reported connected linear rank only | Separates graph count, connected rank, and new generators |
| SVD-only ranks | SVD + rational + modular backends |
| No CRT / rational reconstruction | Syzygy pipeline with discovery/validation split |
| No `references/` PDF | Paper copied to `references/` |
| Fragmented CLIs | `python run_pipeline.py …` |

## Preserved legacy code

`src/invariants/` and `src/invariant_engine/` are **retained** (autonomous
overnight runner, dashboard, caffeinate launcher). They are not deleted until
equivalent operational tests pass for any workflows that still depend on them.

New scientific work should import `tensor_invariants` and use `run_pipeline.py`.

## Audit trail

See `reports/initial_audit.md` for the pre-fix failure-mode checklist and
root-cause analysis.
