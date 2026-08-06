"""
Self-duality / Hodge star for p-forms with explicit signature conventions.

Default 10D Lorentzian conventions (matching literature gate docs):
- Indices 0..9; time = 0
- η = diag(-1, +1×9)
- ε_{0123456789} = +1
- (*F)_{μ1…μ5} = (1/5!) ε_{μ1…μ5 ν1…ν5} F^{ν1…ν5}
- On 5-forms in signature (1,9): ** = +Id, so real self-dual forms exist
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
from typing import Iterable

import numpy as np

from .antisymmetric_tensors import from_independent_components, perm_sign, to_independent_components
from .tensor_spaces import independent_index_tuples, metric_diagonal


DIM10 = 10
RANK5 = 5
FACT5 = factorial(RANK5)
COMBOS10 = list(combinations(range(DIM10), RANK5))
COMBO_INDEX10 = {c: i for i, c in enumerate(COMBOS10)}
N_COMPONENTS_5FORM = len(COMBOS10)  # 252
N_SELF_DUAL = N_COMPONENTS_5FORM // 2  # 126


def levi_civita_sign(indices: tuple[int, ...], dim: int | None = None) -> int:
    dim = dim or len(indices)
    if len(indices) != dim or len(set(indices)) != dim:
        return 0
    return perm_sign(list(indices))


@lru_cache(maxsize=None)
def _complement10(I: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(set(range(DIM10)) - set(I)))


def raise_dense(T: np.ndarray, metric_diag: np.ndarray) -> np.ndarray:
    """Raise all indices of a dense tensor with a diagonal metric."""
    out = T.copy()
    for ax in range(T.ndim):
        # Multiply by η^{ii} when index on axis ax equals i
        factors = np.ones(T.shape, dtype=float)
        for i, s in enumerate(metric_diag):
            sl = [slice(None)] * T.ndim
            sl[ax] = i
            factors[tuple(sl)] *= float(s)
        out = out * factors
    return out


def hodge_star_5form_lorentz10(F_combo: np.ndarray) -> np.ndarray:
    """
    Fast combo-basis Hodge star for 5-forms in 10D Lorentzian signature.

    (*F)_I = σ(I, I^c) * (product of η^{jj} for j in I^c) * F_{I^c}
    with the standard 1/5! absorbed into the combo ↔ dense conventions used here
    by working entirely in the increasing-tuple basis (matches existing hodge10).
    """
    if F_combo.shape != (N_COMPONENTS_5FORM,):
        raise ValueError(f"expected ({N_COMPONENTS_5FORM},)")
    metric = metric_diagonal(DIM10, "lorentzian")
    out = np.zeros_like(F_combo, dtype=float)
    for I in COMBOS10:
        Jc = _complement10(I)
        # ε_{I J} where J = complement in increasing order: sign of concat
        sign = levi_civita_sign(I + Jc)
        raise_s = 1.0
        for j in Jc:
            raise_s *= float(metric[j])
        # (*F)_I = sign * raise(F)_J   (combo stores lowered components)
        # F^J = raise_s * F_J
        out[COMBO_INDEX10[I]] = sign * raise_s * float(F_combo[COMBO_INDEX10[Jc]])
    return out


def project_self_dual_combo(F_combo: np.ndarray) -> np.ndarray:
    """Project to self-dual: (F + *F)/2."""
    star = hodge_star_5form_lorentz10(F_combo)
    return 0.5 * (F_combo + star)


def random_self_dual_5form_combo(rng: np.random.Generator) -> np.ndarray:
    raw = rng.uniform(-1.0, 1.0, size=N_COMPONENTS_5FORM)
    return project_self_dual_combo(raw)


def combo_to_dense(F_combo: np.ndarray) -> np.ndarray:
    return from_independent_components(F_combo, DIM10, RANK5)


def dense_to_combo(T: np.ndarray) -> np.ndarray:
    return to_independent_components(T, DIM10, RANK5)


@dataclass
class SelfDualityReport:
    max_double_star_error: float
    max_projection_star_error: float
    n_components: int
    n_self_dual_dof: int
    star_squared: int
    signature: str
    passed: bool
    message: str
    proof_status: str


def validate_self_duality(n_samples: int = 20, seed: int = 0) -> SelfDualityReport:
    """Validate **=+1 and self-dual projection in 10D Lorentzian 5-form conventions."""
    rng = np.random.default_rng(seed)
    max_ds = 0.0
    max_proj = 0.0
    for _ in range(n_samples):
        F = rng.uniform(-1.0, 1.0, size=N_COMPONENTS_5FORM)
        star = hodge_star_5form_lorentz10(F)
        star2 = hodge_star_5form_lorentz10(star)
        max_ds = max(max_ds, float(np.max(np.abs(star2 - F))))
        P = project_self_dual_combo(F)
        max_proj = max(max_proj, float(np.max(np.abs(P - hodge_star_5form_lorentz10(P)))))
    ok = max_ds < 1e-9 and max_proj < 1e-9
    return SelfDualityReport(
        max_double_star_error=max_ds,
        max_projection_star_error=max_proj,
        n_components=N_COMPONENTS_5FORM,
        n_self_dual_dof=N_SELF_DUAL,
        star_squared=1,
        signature="lorentzian η=diag(-1,+1×9)",
        passed=ok,
        message="OK" if ok else "self-duality validation failed",
        proof_status="exact finite-field computation"
        if False
        else "strong computational evidence",
    )
