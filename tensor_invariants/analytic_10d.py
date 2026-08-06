"""
Analytic Lorentz-scalar invariants of a 10D chiral (self-dual) 5-form.

Conventions match Cederwall–Hutomo–Kuzenko–Lechner–Sorokin (arXiv:2509.14350)
and the project's Lorentzian foundations: η=diag(-1,+1×9), F=*F.

These are explicit closed-form contractions — not a complete generating set for
the full invariant ring (Krull dimension 81). Trace-sector invariants
I_{2n}=tr(M^n) for n=2..10 are nine algebraically independent members of that
ring; they do not generate it.
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable

import numpy as np

from .numerical_rank import svd_rank, zero_small_columns
from .self_duality import combo_to_dense, random_self_dual_5form_combo
from .tensor_spaces import metric_diagonal

logger = logging.getLogger(__name__)


def build_M(T: np.ndarray, metric_diag: np.ndarray) -> np.ndarray:
    """
    M_{μν} = F_{μ a b c d} F_ν{}^{a b c d}  (contracted indices raised).
    Returns a 10×10 lowered-index matrix.
    """
    Tr = np.array(T, dtype=float, copy=True)
    for ax in range(1, 5):
        factors = np.ones(Tr.shape, dtype=float)
        for i, s in enumerate(metric_diag):
            sl = [slice(None)] * Tr.ndim
            sl[ax] = i
            factors[tuple(sl)] = float(s)
        Tr *= factors
    return np.tensordot(T, Tr, axes=([1, 2, 3, 4], [1, 2, 3, 4]))


def M_mixed(T: np.ndarray, metric_diag: np.ndarray) -> np.ndarray:
    """M_μ^ν = M_{μσ} η^{σν}. For this signature η^{σσ}=η_{σσ}."""
    M = build_M(T, metric_diag)
    return M * metric_diag[None, :]


def tr_M_power(T: np.ndarray, metric_diag: np.ndarray, n: int) -> float:
    """I_{2n}^{(1)} = tr(M^n)."""
    if n < 1:
        raise ValueError("n>=1")
    Mm = M_mixed(T, metric_diag)
    X = np.eye(Mm.shape[0], dtype=float)
    for _ in range(n):
        X = X @ Mm
    return float(np.trace(X))


def i4(T: np.ndarray, metric_diag: np.ndarray | None = None) -> float:
    metric_diag = metric_diag if metric_diag is not None else metric_diagonal(10, "lorentzian")
    return tr_M_power(T, metric_diag, 2)


def i6_trace(T: np.ndarray, metric_diag: np.ndarray | None = None) -> float:
    metric_diag = metric_diag if metric_diag is not None else metric_diagonal(10, "lorentzian")
    return tr_M_power(T, metric_diag, 3)


def analytic_callables(
    metric_diag: np.ndarray | None = None,
) -> dict[str, Callable[[np.ndarray], float]]:
    """Named analytic scalars usable as discovery / validation oracles."""
    g = metric_diag if metric_diag is not None else metric_diagonal(10, "lorentzian")

    def _i4(T: np.ndarray, gg=g) -> float:
        return tr_M_power(T, gg, 2)

    def _i6t(T: np.ndarray, gg=g) -> float:
        return tr_M_power(T, gg, 3)

    def _i8t(T: np.ndarray, gg=g) -> float:
        return tr_M_power(T, gg, 4)

    def _i10t(T: np.ndarray, gg=g) -> float:
        return tr_M_power(T, gg, 5)

    def _i4sq(T: np.ndarray, gg=g) -> float:
        v = tr_M_power(T, gg, 2)
        return v * v

    def _i4_i6t(T: np.ndarray, gg=g) -> float:
        return tr_M_power(T, gg, 2) * tr_M_power(T, gg, 3)

    out = {
        "I4=tr(M^2)": _i4,
        "I6^(1)=tr(M^3)": _i6t,
        "I8^(1)=tr(M^4)": _i8t,
        "I10^(1)=tr(M^5)": _i10t,
        "I4^2": _i4sq,
        "I4*I6^(1)": _i4_i6t,
    }
    # Trace sector through degree 20: tr(M^n) for n=2..10
    for n in range(2, 11):
        out.setdefault(
            f"tr(M^{n})",
            (lambda T, gg=g, nn=n: tr_M_power(T, gg, nn)),
        )
    return out


def rank_analytic_span(
    *,
    n_samples: int = 48,
    seed: int = 0,
    out_path: Path | None = None,
) -> dict[str, Any]:
    """
    Numerical ranks of analytic families on self-dual samples.

    Reports:
      - dim span{tr M^n : n=2..10}  (expect 9; literature)
      - deg-4: {I4} rank 1
      - deg-6: {tr M^3} alone rank 1 (full deg-6 needs N1050; not in this module)
      - deg-8: {I4^2, tr M^4} rank ≤2 of the 7-dimensional space
      - deg-10: {I4 trM3, tr M^5} rank ≤2 of the 14-dimensional space
    """
    g = metric_diagonal(10, "lorentzian")
    rng = np.random.default_rng(seed)
    tensors = [combo_to_dense(random_self_dual_5form_combo(rng)) for _ in range(n_samples)]
    t0 = time.time()

    # Trace sector columns n=2..10  (NOT n=1: tr M vanishes / is dependent)
    Tcols = np.zeros((n_samples, 9), dtype=float)
    for i, T in enumerate(tensors):
        Mm = M_mixed(T, g)
        X = Mm @ Mm  # start at M^2
        for j in range(9):
            Tcols[i, j] = float(np.trace(X))
            X = X @ Mm

    # Column-normalize before SVD: dynamic range spans ~10^{20}.
    rms = np.sqrt(np.mean(Tcols * Tcols, axis=0))
    Tn = Tcols / np.maximum(rms, 1e-30)
    trace_rank = svd_rank(Tn, abs_tol=1e-6)

    def eval_list(fns: list[Callable[[np.ndarray], float]]) -> np.ndarray:
        C = np.zeros((n_samples, len(fns)), dtype=float)
        for i, T in enumerate(tensors):
            for j, fn in enumerate(fns):
                C[i, j] = float(fn(T))
        return C

    fns = analytic_callables(g)
    deg4 = eval_list([fns["I4=tr(M^2)"]])
    deg6 = eval_list([fns["I6^(1)=tr(M^3)"]])
    deg8 = eval_list([fns["I4^2"], fns["I8^(1)=tr(M^4)"]])
    deg10 = eval_list([fns["I4*I6^(1)"], fns["I10^(1)=tr(M^5)"]])

    results = {
        "n_samples": n_samples,
        "seed": seed,
        "trace_sector_rank_trM2_to_trM10": int(trace_rank),
        "literature_trace_sector_independent": 9,
        "degree4_rank_I4": int(svd_rank(zero_small_columns(deg4), abs_tol=1e-8)),
        "degree6_rank_trM3_alone": int(svd_rank(zero_small_columns(deg6), abs_tol=1e-8)),
        "degree8_rank_I4sq_and_trM4": int(svd_rank(zero_small_columns(deg8), abs_tol=1e-8)),
        "degree10_rank_I4trM3_and_trM5": int(svd_rank(zero_small_columns(deg10), abs_tol=1e-8)),
        "literature_singlet_dims": {"4": 1, "6": 2, "8": 7, "10": 14},
        "proof_status": "strong computational evidence",
        "limitations": [
            "N^{(1050)} cubic not yet ported; degree-6 analytic span here is 1-dimensional.",
            "Trace sector does not generate the full ring.",
            "Krull dimension 81 is a cited theorem, not re-proved here.",
        ],
        "elapsed_sec": time.time() - t0,
    }
    path = out_path or Path("outputs/10d/analytic_ranks.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    logger.info("analytic ranks written to %s", path)
    return results
