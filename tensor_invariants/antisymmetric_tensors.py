"""
Antisymmetric p-form tensors from independent components.

Components are generated only for strictly increasing index tuples
``i1 < i2 < ... < ip``. All other slots are filled using the permutation sign:

    T_{σ(i1)...σ(ip)} = sign(σ) T_{i1...ip}.
"""

from __future__ import annotations

from itertools import permutations
from typing import Literal

import numpy as np

from .tensor_spaces import independent_index_tuples, n_independent_components


def perm_sign(seq: list[int] | tuple[int, ...]) -> int:
    """Sign of the permutation that sorts ``seq`` into increasing order."""
    a = list(seq)
    sign = 1
    n = len(a)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                sign = -sign
    return sign


def from_independent_components(
    comps: np.ndarray, dim: int, p: int
) -> np.ndarray:
    """Expand an independent-component vector into a dense antisymmetric tensor."""
    combos = independent_index_tuples(dim, p)
    if comps.shape != (len(combos),):
        raise ValueError(f"expected shape ({len(combos)},), got {comps.shape}")
    T = np.zeros((dim,) * p, dtype=comps.dtype)
    for idx, I in enumerate(combos):
        val = comps[idx]
        for perm in permutations(I):
            T[perm] = perm_sign(perm) * val
    return T


def to_independent_components(T: np.ndarray, dim: int, p: int) -> np.ndarray:
    combos = independent_index_tuples(dim, p)
    return np.array([T[I] for I in combos], dtype=T.dtype)


def random_antisymmetric_form(
    dim: int,
    p: int,
    rng: np.random.Generator,
    *,
    mode: Literal["float", "int", "modp"] = "float",
    p_mod: int | None = None,
    int_bound: int = 20,
) -> np.ndarray:
    """
    Draw a random antisymmetric p-form from independent components only.

    Modes
    -----
    float : uniform[-1,1] real components
    int   : integers in [-int_bound, int_bound]
    modp  : uniform residues in F_{p_mod}
    """
    n = n_independent_components(dim, p)
    if mode == "float":
        comps = rng.uniform(-1.0, 1.0, size=n)
    elif mode == "int":
        comps = rng.integers(-int_bound, int_bound + 1, size=n).astype(object)
    elif mode == "modp":
        if p_mod is None:
            raise ValueError("p_mod required for mode='modp'")
        comps = rng.integers(0, p_mod, size=n).astype(object)
    else:
        raise ValueError(f"unknown mode {mode}")
    return from_independent_components(comps, dim, p)


def antisymmetry_error(T: np.ndarray, sample_limit: int | None = None) -> float:
    """Max |T_perm - sign(σ) T_sorted| over independent bases and their perms."""
    dim = T.shape[0]
    p = T.ndim
    combos = independent_index_tuples(dim, p)
    if sample_limit is not None:
        combos = combos[:sample_limit]
    err = 0.0
    for I in combos:
        base = T[I]
        for perm in permutations(I):
            expected = perm_sign(perm) * base
            err = max(err, abs(float(T[perm] - expected)))
    return float(err)


def assert_antisymmetry(T: np.ndarray, tol: float = 1e-10) -> None:
    e = antisymmetry_error(T)
    if e > tol:
        raise AssertionError(f"antisymmetry violated: max error {e} > {tol}")


def transform_orthogonal(H: np.ndarray, Q: np.ndarray) -> np.ndarray:
    """
    Orthogonal change of basis:

        H'_{a1...ap} = Q_{a1}^{i1} ... Q_{ap}^{ip} H_{i1...ip}

    Implemented via successive tensordots.
    """
    p = H.ndim
    out = H
    for ax in range(p):
        out = np.tensordot(Q, out, axes=([1], [ax]))
        # tensordot moves contracted axis; restore axis order
        # After tensordot(Q, out, ([1],[ax])): result axes = (Q0, out axes without ax)
        # We want new axis at position ax.
        axes_order = list(range(1, ax + 1)) + [0] + list(range(ax + 1, p))
        out = np.transpose(out, axes_order)
    return out
