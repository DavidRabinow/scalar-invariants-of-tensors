#!/usr/bin/env python3
"""
Full degree-8 metric-graph census for the 10D chiral 5-form.

Uses the 1753 canonical keys exported from Mathematica
(Degree8CanonicalGraphKeys.wl → outputs/10d/degree8_graph_keys.json).

Computes:
  connected_rank of all graphs
  rank_P of monomials in {I4, I6_a, I6_b} at degree 8  (= span{I4^2})
  n_new = rank([P|C]) - rank(P)

Does NOT invent completeness beyond matching the published singlet count 7.
"""

from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tensor_invariants.contraction_compiler import make_metric_evaluator  # noqa: E402
from tensor_invariants.graph_enumeration import ContractionGraph  # noqa: E402
from tensor_invariants.numerical_rank import svd_rank, zero_small_columns  # noqa: E402
from tensor_invariants.self_duality import combo_to_dense, random_self_dual_5form_combo  # noqa: E402
from tensor_invariants.tensor_spaces import metric_diagonal  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("degree8_census")


def key_to_mult(key: list[int], n: int = 8) -> tuple[tuple[int, ...], ...]:
    M = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j] = M[j][i] = int(key[k])
            k += 1
    if k != len(key):
        raise ValueError("key length mismatch")
    return tuple(tuple(row) for row in M)


def upper_key_from_mult(mult: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    n = len(mult)
    out: list[int] = []
    for i in range(n):
        for j in range(i + 1, n):
            out.append(int(mult[i][j]))
    return tuple(out)


def graph_from_canonical_id(cid: str, form_rank: int) -> ContractionGraph:
    # cid like M[0,1,4,4,1,0]
    inner = cid[cid.index("[") + 1 : cid.index("]")]
    vals = [int(x.strip()) for x in inner.split(",") if x.strip() != ""]
    n = int((1 + (1 + 8 * len(vals)) ** 0.5) / 2)  # solve C(n,2)=len
    # better: find n with n(n-1)/2 = len(vals)
    n = None
    for cand in range(2, 20):
        if cand * (cand - 1) // 2 == len(vals):
            n = cand
            break
    if n is None:
        raise ValueError(cid)
    return ContractionGraph(multiplicity=key_to_mult(vals, n=n), form_rank=form_rank)


def main() -> int:
    keys_path = ROOT / "outputs" / "10d" / "degree8_graph_keys.json"
    out_dir = ROOT / "outputs" / "10d"
    ckpt_dir = out_dir / "checkpoints"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    payload = json.loads(keys_path.read_text(encoding="utf-8"))
    keys: list[list[int]] = payload["keys"]
    log.info("Loaded %s degree-8 canonical keys", len(keys))

    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    gdiag = metric_diagonal(10, "lorentzian")
    rng = np.random.default_rng(seed)

    log.info("Sampling %s self-dual tensors (seed=%s)…", n_samples, seed)
    tensors = [combo_to_dense(random_self_dual_5form_combo(rng)) for _ in range(n_samples)]

    # Lower generators as graphs (blind discovery selection)
    g4 = graph_from_canonical_id("M[0,1,4,4,1,0]", 5)
    g6a = graph_from_canonical_id("M[0,0,0,1,4,0,1,3,1,4,1,0,0,0,0]", 5)  # ∝ tr M^3
    g6b = graph_from_canonical_id("M[0,0,1,2,2,2,1,0,2,1,1,1,2,0,0]", 5)  # independent
    _, e4 = make_metric_evaluator(g4, gdiag)
    _, e6a = make_metric_evaluator(g6a, gdiag)
    _, e6b = make_metric_evaluator(g6b, gdiag)

    # P_8 = span{I4^2} only (no other weighted monomials of {4,6,6} sum to 8)
    P = np.zeros((n_samples, 1), dtype=float)
    for i, T in enumerate(tensors):
        v = float(e4(T))
        P[i, 0] = v * v

    # Build C matrix: n_samples × 1753
    n_graphs = len(keys)
    C = np.zeros((n_samples, n_graphs), dtype=float)
    t0 = time.time()
    batch = 50
    for j, key in enumerate(keys):
        gr = ContractionGraph(multiplicity=key_to_mult(key), form_rank=5)
        _, ev = make_metric_evaluator(gr, gdiag)
        for i, T in enumerate(tensors):
            C[i, j] = float(ev(T))
        if (j + 1) % batch == 0 or j + 1 == n_graphs:
            elapsed = time.time() - t0
            rate = (j + 1) / max(elapsed, 1e-9)
            eta = (n_graphs - j - 1) / max(rate, 1e-9)
            prog = {
                "done": j + 1,
                "total": n_graphs,
                "elapsed_sec": elapsed,
                "eta_sec": eta,
                "n_samples": n_samples,
            }
            (ckpt_dir / "degree8_rank_progress.json").write_text(
                json.dumps(prog, indent=2), encoding="utf-8"
            )
            log.info(
                "graphs %s/%s (%.1f/s, ETA %.0fs)",
                j + 1,
                n_graphs,
                rate,
                eta,
            )

    Pz = zero_small_columns(P)
    Cz = zero_small_columns(C)
    rank_P = svd_rank(Pz, abs_tol=1e-8)
    connected_rank = svd_rank(Cz, abs_tol=1e-8)
    PC = np.column_stack([Pz, Cz]) if Pz.size else Cz
    rank_PC = svd_rank(zero_small_columns(PC), abs_tol=1e-8)
    n_new = rank_PC - rank_P

    # Greedy select 6 new columns beyond P (for explicit basis ids)
    selected: list[int] = []
    for j in range(n_graphs):
        if len(selected) >= max(n_new, 0):
            break
        cols = [C[:, k] for k in selected] + [C[:, j]]
        base_cols = [C[:, k] for k in selected]
        base = np.column_stack([P] + base_cols) if base_cols else P
        trial = np.column_stack([P] + cols)
        if svd_rank(zero_small_columns(trial), abs_tol=1e-8) > svd_rank(
            zero_small_columns(base), abs_tol=1e-8
        ):
            selected.append(j)

    result = {
        "n_graphs": n_graphs,
        "n_samples": n_samples,
        "seed": seed,
        "rank_P_I4_squared": int(rank_P),
        "connected_rank": int(connected_rank),
        "rank_PC": int(rank_PC),
        "n_new": int(n_new),
        "literature_singlet_dim": 7,
        "literature_new_balance": 6,
        "matches_literature_total": connected_rank == 7,
        "matches_literature_new": n_new == 6,
        "selected_new_key_indices": selected,
        "selected_new_keys": [keys[j] for j in selected],
        "proof_status": "strong computational evidence",
        "note": (
            "Full 1753-key metric-graph census on self-dual samples. "
            "Completeness at this degree uses the published SO(10) singlet count 7."
        ),
        "elapsed_sec": time.time() - t0,
    }
    out = out_dir / "degree8_full_rank.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    log.info("Wrote %s", out)
    log.info(
        "connected_rank=%s n_new=%s match_total=%s match_new=%s (%.1fs)",
        connected_rank,
        n_new,
        result["matches_literature_total"],
        result["matches_literature_new"],
        result["elapsed_sec"],
    )
    return 0 if result["matches_literature_total"] and result["matches_literature_new"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
