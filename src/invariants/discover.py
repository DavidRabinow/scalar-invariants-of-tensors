"""
Blind discovery engine — find independent polynomial ingredients from candidates.

No answer key is used during discovery. Optional answer keys are only for grading.
This is the "AlphaGo search" idea without a neural net yet:
  propose candidates → evaluate on random data → keep non-redundant ones.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from .utils import evaluate_on_draws, independent_column_indices, numerical_rank


@dataclass
class Candidate:
    name: str
    order: int
    fn: Callable[[np.ndarray], float]


@dataclass
class LevelResult:
    name: str
    discovered_names: list[str]
    discovered_count: int
    expected_count: int | None
    passed: bool | None  # None if no expected answer provided
    by_order: dict[int, int]


def discover_independent(
    candidates: list[Candidate],
    draw: Callable[[np.random.Generator], np.ndarray],
    max_order: int,
    n_draws: int = 80,
    seed: int = 0,
    tol: float = 1e-8,
) -> LevelResult:
    """
    Walk orders 1..max_order. At each order, keep candidates that are
    independent of products of already-accepted lower-order generators.
    """
    kept: list[Candidate] = []
    by_order: dict[int, int] = {}

    for order in range(1, max_order + 1):
        at_order = [c for c in candidates if c.order == order]
        if not at_order and not kept:
            by_order[order] = 0
            continue

        products = _product_fns(kept, order)

        def compute(T: np.ndarray, _at=at_order, _prod=products) -> np.ndarray:
            vals = [c.fn(T) for c in _at]
            vals.extend(fn(T) for fn in _prod)
            return np.asarray(vals, dtype=float)

        n_cols = len(at_order) + len(products)
        if n_cols == 0:
            by_order[order] = 0
            continue

        mat = evaluate_on_draws(
            compute, draw, max(n_draws, n_cols + 20), seed=seed + order
        )
        # Columns: [candidates at this order | products of lower]
        cand_mat = mat[:, : len(at_order)] if at_order else np.zeros((mat.shape[0], 0))
        prod_mat = mat[:, len(at_order) :] if products else np.zeros((mat.shape[0], 0))

        new_local: list[int] = []
        for j in range(cand_mat.shape[1]):
            trial_cols = []
            # already kept new ones at this order
            for k in new_local:
                trial_cols.append(cand_mat[:, k])
            trial_cols.append(cand_mat[:, j])
            for p in range(prod_mat.shape[1]):
                trial_cols.append(prod_mat[:, p])
            trial = np.column_stack(trial_cols) if trial_cols else np.zeros((mat.shape[0], 0))
            base_cols = []
            for k in new_local:
                base_cols.append(cand_mat[:, k])
            for p in range(prod_mat.shape[1]):
                base_cols.append(prod_mat[:, p])
            base = np.column_stack(base_cols) if base_cols else np.zeros((mat.shape[0], 0))
            if numerical_rank(trial, tol=tol) > numerical_rank(base, tol=tol):
                new_local.append(j)

        for j in new_local:
            kept.append(at_order[j])
        by_order[order] = len(new_local)

    return LevelResult(
        name="",
        discovered_names=[c.name for c in kept],
        discovered_count=len(kept),
        expected_count=None,
        passed=None,
        by_order=by_order,
    )


def _product_fns(
    gens: list[Candidate], target_order: int
) -> list[Callable[[np.ndarray], float]]:
    """All products of generators whose orders sum to target_order."""
    out: list[Callable[[np.ndarray], float]] = []
    n = len(gens)

    def rec(start: int, rem: int, idxs: list[int]) -> None:
        if rem == 0:
            chosen = list(idxs)

            def fn(T: np.ndarray, _idxs=chosen) -> float:
                p = 1.0
                for i in _idxs:
                    p *= gens[i].fn(T)
                return p

            out.append(fn)
            return
        for i in range(start, n):
            d = gens[i].order
            if d > rem:
                continue
            idxs.append(i)
            rec(i, rem - d, idxs)
            idxs.pop()

    if gens:
        rec(0, target_order, [])
    return out


def grade(result: LevelResult, expected_count: int, name: str) -> LevelResult:
    result.name = name
    result.expected_count = expected_count
    result.passed = result.discovered_count == expected_count
    return result
