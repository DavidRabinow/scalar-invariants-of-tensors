"""
10D chiral (self-dual) 5-form — storage and legacy helpers.

Hodge-star conventions and validation live in ``hodge10`` (Stage 1).
This module re-exports the audited combo-basis API for callers.
"""

from __future__ import annotations

from math import factorial

import numpy as np

from .discover import Candidate, discover_independent
from .hodge10 import (
    COMBOS,
    COMBO_INDEX,
    DIM,
    N_CHIRAL,
    N_COMPONENTS,
    RANK,
    combo_to_dense,
    hodge_star_combo_fast as hodge_star,
    project_self_dual_combo as project_self_dual,
    random_chiral_five_form_combo as random_chiral_five_form,
    random_five_form_combo as random_five_form,
    raise_dense as _raise_dense,
    validate_hodge,
)

# Back-compat aliases used by timed_search / run_10d
to_dense_tensor = combo_to_dense


def is_self_dual(F: np.ndarray, tol: float = 1e-10) -> bool:
    return float(np.max(np.abs(F - hodge_star(F)))) < tol


def quadratic_norm(F: np.ndarray) -> float:
    """
    Lorentzian contraction F_{μ1…μ5} F^{μ1…μ5} reconstructed from combo basis.

    Each increasing component appears 5! times in the fully antisymmetrized sum,
    so we multiply the combo sum by 5!.
    """
    total = 0.0
    for I in COMBOS:
        f = F[COMBO_INDEX[I]]
        raise_sign = (-1) ** (0 in I)
        total += f * (raise_sign * f)
    return float(total * factorial(RANK))


def make_order2_candidates() -> list[Candidate]:
    return [Candidate("F·F", 2, quadratic_norm)]


def make_order4_candidates() -> list[Candidate]:
    def q2(F: np.ndarray) -> float:
        q = quadratic_norm(F)
        return q * q

    def tr_T2(F: np.ndarray) -> float:
        Td = to_dense_tensor(F)
        Tu = _raise_dense(Td)
        T = np.tensordot(Td, Tu, axes=([1, 2, 3, 4], [1, 2, 3, 4]))
        eta = np.array([-1.0] + [1.0] * 9)
        Tup = eta[:, None] * T * eta[None, :]
        return float(np.tensordot(T, Tup, axes=([0, 1], [1, 0])))

    def G_norm(F: np.ndarray) -> float:
        Td = to_dense_tensor(F)
        Tu = _raise_dense(Td)
        G = np.tensordot(Td, Tu, axes=([2, 3, 4], [2, 3, 4]))
        Gu = _raise_dense(G)
        return float(np.tensordot(G, Gu, axes=([0, 1, 2, 3], [0, 1, 2, 3])))

    return [
        Candidate("(F·F)^2", 4, q2),
        Candidate("tr(T^2)", 4, tr_T2),
        Candidate("||G||^2", 4, G_norm),
    ]


def make_order6_candidates() -> list[Candidate]:
    def q3(F: np.ndarray) -> float:
        return quadratic_norm(F) ** 3

    def q_times_tr(F: np.ndarray) -> float:
        tr = make_order4_candidates()[1].fn(F)
        return quadratic_norm(F) * tr

    return [
        Candidate("(F·F)^3", 6, q3),
        Candidate("(F·F)*tr(T^2)", 6, q_times_tr),
    ]


def all_starter_candidates() -> list[Candidate]:
    return make_order2_candidates() + make_order4_candidates() + make_order6_candidates()


def sanity_checks(seed: int = 0) -> dict:
    report = validate_hodge(n_samples=20, seed=seed)
    return {
        "n_generic_components": N_COMPONENTS,
        "n_chiral_free_components": N_CHIRAL,
        "is_self_dual": report.max_projection_star_error < 1e-9,
        "max_|F-*F|_after_projection": report.max_projection_star_error,
        "max_|**F-F|": report.max_double_star_error,
        "max_fast_vs_reference": report.max_fast_vs_reference_error,
        "hodge_validation_passed": report.passed,
        "hodge_message": report.message,
        "literature_hypothesis_target": 81,
        "signature": "Lorentzian η=diag(-1,+1×9)",
        "note": "81 is an external literature hypothesis, not a computed progress denominator.",
    }


def run_low_order_discovery(seed: int = 0, n_draws: int = 16) -> dict:
    result = discover_independent(
        all_starter_candidates(),
        random_chiral_five_form,
        max_order=6,
        n_draws=n_draws,
        seed=seed,
        tol=1e-5,
    )
    return {
        "mode": "legacy-catalog-comparison-only",
        "discovered_count": result.discovered_count,
        "discovered_names": result.discovered_names,
        "by_order": {str(k): v for k, v in result.by_order.items()},
        "literature_hypothesis_target": 81,
        "note": (
            "Legacy hand catalog. Main discovery path will use automatic graphs "
            "(see IMPLEMENTATION_PLAN.md)."
        ),
    }
