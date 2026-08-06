"""Modular Gaussian elimination: rank and nullspace over prime fields."""

from __future__ import annotations

from typing import Sequence

import numpy as np

from .finite_field import mod_inv


def _as_int_mod(matrix: np.ndarray | Sequence[Sequence[int]], p: int) -> np.ndarray:
    A = np.asarray(matrix, dtype=object)
    if A.ndim != 2:
        raise ValueError("matrix must be 2-dimensional")
    out = np.empty(A.shape, dtype=object)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            out[i, j] = int(A[i, j]) % p
    return out


def rank_mod_p(matrix: np.ndarray | Sequence[Sequence[int]], p: int) -> int:
    """
    Exact rank of an integer matrix over the field F_p.

    Uses forward Gaussian elimination with partial pivoting.
    """
    A = _as_int_mod(matrix, p)
    m, n = A.shape
    rank = 0
    row = 0
    for col in range(n):
        pivot = None
        for i in range(row, m):
            if A[i, col] % p != 0:
                pivot = i
                break
        if pivot is None:
            continue
        if pivot != row:
            A[[row, pivot]] = A[[pivot, row]]
        inv = mod_inv(int(A[row, col]), p)
        for j in range(col, n):
            A[row, j] = (int(A[row, j]) * inv) % p
        for i in range(m):
            if i == row:
                continue
            factor = int(A[i, col]) % p
            if factor == 0:
                continue
            for j in range(col, n):
                A[i, j] = (int(A[i, j]) - factor * int(A[row, j])) % p
        rank += 1
        row += 1
        if row == m:
            break
    return rank


def nullspace_mod_p(
    matrix: np.ndarray | Sequence[Sequence[int]], p: int
) -> np.ndarray:
    """
    Right nullspace basis over F_p.

    Returns an integer array of shape ``(n_cols, nullity)`` with entries in
    ``{0,...,p-1}``. Columns form a basis for ``{ x | A x ≡ 0 (mod p) }``.
    """
    A = _as_int_mod(matrix, p)
    m, n = A.shape
    # Row-reduce to RREF-like form, tracking pivot columns
    pivots: list[int] = []
    row = 0
    R = A.copy()
    for col in range(n):
        pivot = None
        for i in range(row, m):
            if int(R[i, col]) % p != 0:
                pivot = i
                break
        if pivot is None:
            continue
        if pivot != row:
            R[[row, pivot]] = R[[pivot, row]]
        inv = mod_inv(int(R[row, col]), p)
        for j in range(n):
            R[row, j] = (int(R[row, j]) * inv) % p
        for i in range(m):
            if i == row:
                continue
            factor = int(R[i, col]) % p
            if factor == 0:
                continue
            for j in range(n):
                R[i, j] = (int(R[i, j]) - factor * int(R[row, j])) % p
        pivots.append(col)
        row += 1
        if row == m:
            break

    pivot_set = set(pivots)
    free = [j for j in range(n) if j not in pivot_set]
    if not free:
        return np.zeros((n, 0), dtype=object)

    # Map pivot column -> row index
    pivot_row = {pivots[i]: i for i in range(len(pivots))}
    basis = []
    for f in free:
        vec = [0] * n
        vec[f] = 1
        for pc in pivots:
            # R[pr, pc]=1 and R[pr, *] has entries; x_pc = -sum R[pr, free] x_free
            pr = pivot_row[pc]
            s = 0
            for j in free:
                s = (s + int(R[pr, j]) * vec[j]) % p
            vec[pc] = (-s) % p
        basis.append(vec)
    return np.array(basis, dtype=object).T


def ranks_agree_across_primes(
    matrix: np.ndarray | Sequence[Sequence[int]],
    primes: Sequence[int],
) -> dict:
    """Compute ranks over several primes and report agreement."""
    ranks = {int(p): rank_mod_p(matrix, int(p)) for p in primes}
    values = list(ranks.values())
    return {
        "ranks": ranks,
        "agree": len(set(values)) == 1,
        "rank": values[0] if values else 0,
    }
