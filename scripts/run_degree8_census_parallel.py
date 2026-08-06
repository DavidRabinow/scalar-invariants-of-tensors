#!/usr/bin/env python3
"""Parallel full degree-8 census (1753 keys) for 10D chiral 5-form."""

from __future__ import annotations

import json
import logging
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("degree8_parallel")

_GDIAG = None
_TENSORS = None


def _init_worker(tensors: list, gdiag: np.ndarray) -> None:
    global _GDIAG, _TENSORS
    _GDIAG = gdiag
    _TENSORS = tensors


def key_to_mult(key: list[int], n: int = 8) -> tuple[tuple[int, ...], ...]:
    M = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j] = M[j][i] = int(key[k])
            k += 1
    return tuple(tuple(row) for row in M)


def _eval_key(args: tuple[int, list[int]]) -> tuple[int, np.ndarray]:
    from tensor_invariants.contraction_compiler import make_metric_evaluator
    from tensor_invariants.graph_enumeration import ContractionGraph

    j, key = args
    gr = ContractionGraph(multiplicity=key_to_mult(key), form_rank=5)
    _, ev = make_metric_evaluator(gr, _GDIAG)
    col = np.array([float(ev(T)) for T in _TENSORS], dtype=float)
    return j, col


def graph_from_canonical_id(cid: str, form_rank: int):
    from tensor_invariants.graph_enumeration import ContractionGraph

    inner = cid[cid.index("[") + 1 : cid.index("]")]
    vals = [int(x.strip()) for x in inner.split(",") if x.strip() != ""]
    n = None
    for cand in range(2, 20):
        if cand * (cand - 1) // 2 == len(vals):
            n = cand
            break
    assert n is not None
    return ContractionGraph(multiplicity=key_to_mult(vals, n=n), form_rank=form_rank)


def main() -> int:
    from tensor_invariants.contraction_compiler import make_metric_evaluator
    from tensor_invariants.numerical_rank import svd_rank, zero_small_columns
    from tensor_invariants.self_duality import combo_to_dense, random_self_dual_5form_combo
    from tensor_invariants.tensor_spaces import metric_diagonal

    n_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8

    keys_path = ROOT / "outputs" / "10d" / "degree8_graph_keys.json"
    out_dir = ROOT / "outputs" / "10d"
    ckpt_dir = out_dir / "checkpoints"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    keys: list[list[int]] = json.loads(keys_path.read_text(encoding="utf-8"))["keys"]
    n_graphs = len(keys)
    log.info("keys=%s samples=%s workers=%s", n_graphs, n_samples, workers)

    gdiag = metric_diagonal(10, "lorentzian")
    rng = np.random.default_rng(seed)
    tensors = [combo_to_dense(random_self_dual_5form_combo(rng)) for _ in range(n_samples)]

    g4 = graph_from_canonical_id("M[0,1,4,4,1,0]", 5)
    _, e4 = make_metric_evaluator(g4, gdiag)
    P = np.zeros((n_samples, 1), dtype=float)
    for i, T in enumerate(tensors):
        v = float(e4(T))
        P[i, 0] = v * v

    C = np.zeros((n_samples, n_graphs), dtype=float)
    t0 = time.time()
    done = 0
    with ProcessPoolExecutor(
        max_workers=workers,
        initializer=_init_worker,
        initargs=(tensors, gdiag),
    ) as ex:
        futs = [ex.submit(_eval_key, (j, key)) for j, key in enumerate(keys)]
        for fut in as_completed(futs):
            j, col = fut.result()
            C[:, j] = col
            done += 1
            if done % 100 == 0 or done == n_graphs:
                elapsed = time.time() - t0
                rate = done / max(elapsed, 1e-9)
                eta = (n_graphs - done) / max(rate, 1e-9)
                (ckpt_dir / "degree8_rank_progress.json").write_text(
                    json.dumps(
                        {
                            "done": done,
                            "total": n_graphs,
                            "elapsed_sec": elapsed,
                            "eta_sec": eta,
                            "n_samples": n_samples,
                            "workers": workers,
                        },
                        indent=2,
                    ),
                    encoding="utf-8",
                )
                log.info("graphs %s/%s (%.1f/s ETA %.0fs)", done, n_graphs, rate, eta)

    Pz = zero_small_columns(P)
    Cz = zero_small_columns(C)
    # Column-normalize C for stable rank across huge dynamic range
    rms = np.sqrt(np.mean(Cz * Cz, axis=0))
    Cn = Cz / np.maximum(rms, 1e-30)
    rank_P = svd_rank(Pz, abs_tol=1e-8)
    connected_rank = svd_rank(Cn, abs_tol=1e-6)
    PC = np.column_stack([Pz / max(float(np.sqrt(np.mean(Pz * Pz))), 1e-30), Cn])
    rank_PC = svd_rank(zero_small_columns(PC), abs_tol=1e-6)
    n_new = rank_PC - rank_P

    selected: list[int] = []
    for j in range(n_graphs):
        if len(selected) >= max(n_new, 0):
            break
        cols = [Cn[:, k] for k in selected] + [Cn[:, j]]
        base_cols = [Cn[:, k] for k in selected]
        Pn = Pz / max(float(np.sqrt(np.mean(Pz * Pz))), 1e-30)
        base = np.column_stack([Pn] + base_cols) if base_cols else Pn
        trial = np.column_stack([Pn] + cols)
        if svd_rank(trial, abs_tol=1e-6) > svd_rank(base, abs_tol=1e-6):
            selected.append(j)

    result = {
        "n_graphs": n_graphs,
        "n_samples": n_samples,
        "seed": seed,
        "workers": workers,
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
            "Full 1753-key metric-graph census on self-dual samples with column-normalized SVD. "
            "Completeness uses published singlet count 7."
        ),
        "elapsed_sec": time.time() - t0,
    }
    out = out_dir / "degree8_full_rank.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    log.info("Wrote %s", out)
    log.info(
        "connected_rank=%s n_new=%s match=%s/%s (%.1fs)",
        connected_rank,
        n_new,
        result["matches_literature_total"],
        result["matches_literature_new"],
        result["elapsed_sec"],
    )
    return 0 if result["matches_literature_total"] and result["matches_literature_new"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
