"""Numerical and exact rational matrix rank backends."""

from __future__ import annotations

from fractions import Fraction
from typing import Sequence

import numpy as np


def svd_rank(matrix: np.ndarray | Sequence[Sequence[float]], tol: float | None = None) -> int:
    """Rank via SVD with a relative singular-value tolerance."""
    A = np.asarray(matrix, dtype=float)
    if A.size == 0:
        return 0
    if A.ndim != 2:
        raise ValueError("matrix must be 2D")
    s = np.linalg.svd(A, compute_uv=False)
    if tol is None:
        tol = max(A.shape) * np.finfo(float).eps * (float(s[0]) if s.size else 0.0)
    return int(np.sum(s > tol))


def _to_fraction_matrix(matrix: np.ndarray | Sequence[Sequence[float | int | Fraction]]) -> list[list[Fraction]]:
    A = np.asarray(matrix, dtype=object)
    rows: list[list[Fraction]] = []
    for i in range(A.shape[0]):
        row = []
        for j in range(A.shape[1]):
            v = A[i, j]
            if isinstance(v, Fraction):
                row.append(v)
            else:
                row.append(Fraction(v).limit_denominator())
        rows.append(row)
    return rows


def rational_rank(matrix: np.ndarray | Sequence[Sequence[float | int | Fraction]]) -> int:
    """
    Exact rank over Q via fraction Gaussian elimination.

    For floating inputs, values are converted with ``Fraction(...).limit_denominator()``.
    Prefer integer/Fraction matrices for scientific claims.
    """
    A = np.asarray(matrix, dtype=object)
    if A.size == 0:
        return 0
    F = _to_fraction_matrix(A)
    m, n = len(F), len(F[0]) if F else 0
    rank = 0
    row = 0
    for col in range(n):
        pivot = None
        for i in range(row, m):
            if F[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        F[row], F[pivot] = F[pivot], F[row]
        piv = F[row][col]
        F[row] = [x / piv for x in F[row]]
        for i in range(m):
            if i == row:
                continue
            factor = F[i][col]
            if factor == 0:
                continue
            F[i] = [F[i][j] - factor * F[row][j] for j in range(n)]
        rank += 1
        row += 1
        if row == m:
            break
    return rank


def compare_rank_backends(
    matrix: np.ndarray,
    primes: Sequence[int],
    tol: float | None = None,
) -> dict:
    """Compare SVD, rational, and modular ranks (for small matrices)."""
    from .nullspace import rank_mod_p

    # Round float matrix to nearest int for modular/rational if nearly integral
    A = np.asarray(matrix, dtype=float)
    near_int = np.allclose(A, np.round(A), atol=1e-8)
    A_int = np.rint(A).astype(object) if near_int else None

    out: dict = {"svd_rank": svd_rank(A, tol=tol), "near_integer": near_int}
    if A_int is not None and A.size <= 400:
        out["rational_rank"] = rational_rank(A_int)
        out["mod_ranks"] = {int(p): rank_mod_p(A_int, int(p)) for p in primes}
    return out
