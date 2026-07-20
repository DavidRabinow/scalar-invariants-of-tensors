"""Numerical helpers for invariant-theory experiments."""

from __future__ import annotations

from typing import Callable

import numpy as np


def numerical_rank(matrix: np.ndarray, tol: float | None = None) -> int:
    """Rank via SVD with a relative singular-value tolerance."""
    if matrix.size == 0:
        return 0
    s = np.linalg.svd(matrix, compute_uv=False)
    if tol is None:
        tol = max(matrix.shape) * np.finfo(float).eps * (s[0] if s.size else 0.0)
    return int(np.sum(s > tol))


def nullspace_basis(matrix: np.ndarray, tol: float | None = None) -> np.ndarray:
    """Return an orthonormal basis for the (approximate) right nullspace."""
    if matrix.size == 0:
        return np.zeros((0, 0))
    _, s, vh = np.linalg.svd(matrix, full_matrices=True)
    if tol is None:
        tol = max(matrix.shape) * np.finfo(float).eps * (s[0] if s.size else 0.0)
    rank = int(np.sum(s > tol))
    return vh[rank:].T


def evaluate_on_draws(
    compute_scalars: Callable[[np.ndarray], np.ndarray],
    draw_tensor: Callable[[np.random.Generator], np.ndarray],
    n_draws: int,
    seed: int = 0,
) -> np.ndarray:
    """Build an (n_draws × n_scalars) matrix from random tensors."""
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(n_draws):
        T = draw_tensor(rng)
        rows.append(np.asarray(compute_scalars(T), dtype=float))
    return np.vstack(rows)


def independent_column_indices(matrix: np.ndarray, tol: float | None = None) -> list[int]:
    """Greedy column pivot selection for a maximal linearly independent set."""
    if matrix.size == 0:
        return []
    selected: list[int] = []
    for j in range(matrix.shape[1]):
        trial = selected + [j]
        if numerical_rank(matrix[:, trial], tol=tol) == len(trial):
            selected = trial
    return selected
