"""
Reproduce §4.1 of Elamaran–Ferko–Scarlett: trace invariants of a 3-form in 6D.

A totally antisymmetric H_{abc} in d=6, contracted only with δ^{ab}.
Expected independent generators:
  x^(2), x^(4)_1, x^(4)_2, x^(6), x^(8)
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Callable

import numpy as np
from opt_einsum import contract

from .utils import evaluate_on_draws, numerical_rank


DIM = 6


def random_three_form(rng: np.random.Generator, dim: int = DIM) -> np.ndarray:
    """Draw a random real antisymmetric 3-form in Euclidean R^dim."""
    raw = rng.uniform(-1.0, 1.0, size=(dim, dim, dim))
    H = np.zeros_like(raw)
    for a, b, c in combinations(range(dim), 3):
        val = raw[a, b, c]
        for perm, sign in _signed_perms((a, b, c)):
            H[perm] = sign * val
    return H


def _signed_perms(idxs: tuple[int, int, int]):
    a, b, c = idxs
    yield (a, b, c), 1
    yield (b, c, a), 1
    yield (c, a, b), 1
    yield (a, c, b), -1
    yield (c, b, a), -1
    yield (b, a, c), -1


@dataclass(frozen=True)
class ExplicitInvariant:
    name: str
    order: int
    fn: Callable[[np.ndarray], float]


def paper_generators() -> list[ExplicitInvariant]:
    """The five HSOP elements of §4.1 (trace variables)."""

    def x2(H: np.ndarray) -> float:
        return float(contract("abc,abc->", H, H))

    def x4_1(H: np.ndarray) -> float:
        # H_abc H_ade H_def H_bcf
        return float(contract("abc,ade,def,bcf->", H, H, H, H))

    def x4_2(H: np.ndarray) -> float:
        # H_abc H_ade H_cef H_bdf
        return float(contract("abc,ade,cef,bdf->", H, H, H, H))

    def x6(H: np.ndarray) -> float:
        # H_abc H_chi H_ghi H_adg H_def H_bef
        return float(contract("abc,chi,ghi,adg,def,bef->", H, H, H, H, H, H))

    def x8(H: np.ndarray) -> float:
        # H_abc H_bci H_ghi H_gjk H_jkl H_fhl H_def H_ade
        return float(
            contract("abc,bci,ghi,gjk,jkl,fhl,def,ade->", H, H, H, H, H, H, H, H)
        )

    return [
        ExplicitInvariant("x^(2)", 2, x2),
        ExplicitInvariant("x^(4)_1", 4, x4_1),
        ExplicitInvariant("x^(4)_2", 4, x4_2),
        ExplicitInvariant("x^(6)", 6, x6),
        ExplicitInvariant("x^(8)", 8, x8),
    ]


# Dependent invariants from Appendix A (for syzygy checks)
def appendix_dependents() -> list[ExplicitInvariant]:
    def X6_1(H: np.ndarray) -> float:
        # H_abc H_bci H_ghi H_fgh H_def H_ade
        return float(contract("abc,bci,ghi,fgh,def,ade->", H, H, H, H, H, H))

    def X6_2(H: np.ndarray) -> float:
        # H_abc H_cfh H_def H_bei H_dgi H_agh
        return float(contract("abc,cfh,def,bei,dgi,agh->", H, H, H, H, H, H))

    return [
        ExplicitInvariant("X^(6)_1", 6, X6_1),
        ExplicitInvariant("X^(6)_2", 6, X6_2),
    ]


def _partitions_of_order(
    generators: list[ExplicitInvariant], order: int
) -> list[list[int]]:
    """Multisets of generator indices whose orders sum to `order`."""
    out: list[list[int]] = []
    n = len(generators)

    def rec(start: int, rem: int, acc: list[int]) -> None:
        if rem == 0:
            out.append(list(acc))
            return
        for i in range(start, n):
            d = generators[i].order
            if d > rem:
                continue
            acc.append(i)
            rec(i, rem - d, acc)
            acc.pop()

    rec(0, order, [])
    return out


def _product_values(
    H: np.ndarray, generators: list[ExplicitInvariant], order: int
) -> list[float]:
    parts = _partitions_of_order(generators, order)
    cache = {i: float(generators[i].fn(H)) for i in range(len(generators))}
    vals = []
    for part in parts:
        p = 1.0
        for i in part:
            p *= cache[i]
        vals.append(p)
    return vals


def verify_paper_generators_independent(
    n_draws: int = 40, seed: int = 1, tol: float = 1e-8
) -> dict:
    """
    Check that the five paper generators are numerically independent as an HSOP:
    at each generator order, the new gens are independent of products of lower ones.
    """
    gens = paper_generators()
    report: dict = {"generators": [g.name for g in gens], "orders": {}}

    def compute(H: np.ndarray) -> np.ndarray:
        return np.array([g.fn(H) for g in gens], dtype=float)

    mat = evaluate_on_draws(compute, random_three_form, n_draws, seed=seed)
    report["generator_matrix_rank"] = numerical_rank(mat, tol=tol)
    report["expected_rank"] = 5

    for order in (2, 4, 6, 8, 10, 12):
        strictly_lower = [g for g in gens if g.order < order]
        at_order = [g for g in gens if g.order == order]
        n_products = len(_partitions_of_order(strictly_lower, order))

        def compute_all(H: np.ndarray, _at=at_order, _low=strictly_lower, _ord=order):
            vals = [g.fn(H) for g in _at]
            vals.extend(_product_values(H, _low, _ord))
            return np.array(vals, dtype=float)

        n_cols = len(at_order) + n_products
        if n_cols == 0:
            continue
        M = evaluate_on_draws(
            compute_all,
            random_three_form,
            max(n_cols + 15, 30),
            seed=seed + order,
        )
        r = numerical_rank(M, tol=tol)
        report["orders"][order] = {
            "n_gens_at_order": len(at_order),
            "n_lower_products": n_products,
            "matrix_rank": r,
            "new_independent": r - n_products,
        }
    return report


def verify_appendix_syzygies(
    n_draws: int = 200, seed: int = 7, tol: float = 1e-6
) -> dict:
    """
    Check Appendix A relations (A.2):

      X6_1 - (1/2) x2 x4_1 + (1/18) x2^3 = 0
      X6_2 + (1/2) x6 + (1/12) x2 x4_2 - (1/6) x2 x4_1 + (1/72) x2^3 = 0
    """
    gens = {g.name: g for g in paper_generators()}
    deps = {g.name: g for g in appendix_dependents()}

    def residuals(H: np.ndarray) -> np.ndarray:
        x2 = gens["x^(2)"].fn(H)
        x41 = gens["x^(4)_1"].fn(H)
        x42 = gens["x^(4)_2"].fn(H)
        x6 = gens["x^(6)"].fn(H)
        X1 = deps["X^(6)_1"].fn(H)
        X2 = deps["X^(6)_2"].fn(H)
        r1 = X1 - 0.5 * x2 * x41 + (1.0 / 18.0) * x2**3
        r2 = (
            X2
            + 0.5 * x6
            + (1.0 / 12.0) * x2 * x42
            - (1.0 / 6.0) * x2 * x41
            + (1.0 / 72.0) * x2**3
        )
        return np.array([r1, r2], dtype=float)

    mat = evaluate_on_draws(residuals, random_three_form, n_draws, seed=seed)
    max_abs = np.max(np.abs(mat), axis=0)
    return {
        "max_abs_residual_X6_1": float(max_abs[0]),
        "max_abs_residual_X6_2": float(max_abs[1]),
        "pass": bool(np.all(max_abs < tol)),
        "tol": tol,
        "n_draws": n_draws,
    }


def smoke_evaluate_generators(seed: int = 0) -> dict[str, float]:
    """Single random draw — useful to confirm contractions run."""
    rng = np.random.default_rng(seed)
    H = random_three_form(rng)
    return {g.name: g.fn(H) for g in paper_generators()}
