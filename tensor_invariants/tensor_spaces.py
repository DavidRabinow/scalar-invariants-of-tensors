"""Index spaces and metrics for antisymmetric p-forms."""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Literal

import numpy as np

SignatureName = Literal["euclidean", "lorentzian"]


def n_independent_components(dim: int, p: int) -> int:
    """Number of independent components of a p-form in dimension ``dim``: C(dim,p)."""
    if p < 0 or p > dim:
        return 0
    return comb(dim, p)


def independent_index_tuples(dim: int, p: int) -> list[tuple[int, ...]]:
    """Strictly increasing index tuples ``i1 < i2 < ... < ip``."""
    return list(combinations(range(dim), p))


def metric_diagonal(dim: int, signature: SignatureName = "euclidean") -> np.ndarray:
    """Diagonal metric components η_{μν}."""
    if signature == "euclidean":
        return np.ones(dim, dtype=float)
    if signature == "lorentzian":
        g = np.ones(dim, dtype=float)
        g[0] = -1.0
        return g
    raise ValueError(f"unknown signature {signature}")


def raise_index_sign(indices: tuple[int, ...], metric_diag: np.ndarray) -> float:
    """Product of η^{i_k i_k} for raising all indices of a component."""
    s = 1.0
    for i in indices:
        s *= float(metric_diag[i])
    return s
