"""
Timed search toward ~81 independent invariants of a 10D chiral 5-form.

Writes live progress to a JSON file the UI polls.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np

from .five_form_10d import (
    DIM,
    random_chiral_five_form,
    to_dense_tensor,
    quadratic_norm,
)
from .utils import numerical_rank

ETA = np.array([-1.0] + [1.0] * 9)
PROGRESS_DEFAULT = Path(__file__).resolve().parents[2] / "ui" / "progress.json"


@dataclass
class FoundInvariant:
    id: int
    name: str
    order: int
    found_at_sec: float


@dataclass
class SearchProgress:
    status: str = "idle"  # idle | running | done | error
    target: int = 81
    found_count: int = 0
    found: list[FoundInvariant] = field(default_factory=list)
    candidates_tested: int = 0
    draws_used: int = 0
    elapsed_sec: float = 0.0
    duration_sec: float = 900.0
    message: str = ""
    by_order: dict[str, int] = field(default_factory=dict)
    started_at: float | None = None

    def to_json(self) -> dict:
        d = asdict(self)
        return d


def _raise_all(T: np.ndarray) -> np.ndarray:
    idx = np.indices(T.shape)
    n0 = sum((idx[ax] == 0).astype(int) for ax in range(T.ndim))
    return T * np.where(n0 % 2 == 0, 1.0, -1.0)


def _build_T_and_G(F: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    Td = to_dense_tensor(F)
    Tu = _raise_all(Td)
    # T_μν = F_μabcd F_ν^abcd
    T = np.tensordot(Td, Tu, axes=([1, 2, 3, 4], [1, 2, 3, 4]))
    # G_abcd = F_abijk F_cd^ijk
    G = np.tensordot(Td, Tu, axes=([2, 3, 4], [2, 3, 4]))
    q = quadratic_norm(F)
    return T, G, q


def _lorentz_frobenius(A: np.ndarray) -> float:
    Au = _raise_all(A)
    return float(np.tensordot(A, Au, axes=[list(range(A.ndim))] * 2))


def _matrix_power_traces(T: np.ndarray, max_power: int) -> dict[int, float]:
    """tr(T^k) with Lorentz trace tr(A)=A^μ_μ = η^{μα} A_{αμ}."""
    # Raise first index: T^μ_ν = η^{μα} T_{αν}
    Tm = ETA[:, None] * T  # T^μ_ν
    out: dict[int, float] = {}
    Pk = np.eye(DIM)
    for k in range(1, max_power + 1):
        Pk = Pk @ Tm
        out[k] = float(np.trace(Pk))
    return out


def candidate_catalog() -> list[tuple[str, int, Callable]]:
    """
    Named candidates evaluated from precomputed (T, G, q).

    Each fn(T, G, q) -> float.
    """
    cats: list[tuple[str, int, Callable]] = []

    # Order 2
    cats.append(("F·F", 2, lambda T, G, q: q))

    # Order 4 from T and G
    def trT2(T, G, q):
        Tm = ETA[:, None] * T
        return float(np.trace(Tm @ Tm))

    def Gnorm(T, G, q):
        return _lorentz_frobenius(G)

    def q2(T, G, q):
        return q * q

    cats.append(("tr(T^2)", 4, trT2))
    cats.append(("||G||^2", 4, Gnorm))
    cats.append(("(F·F)^2", 4, q2))

    # More order-4 style: element contractions of G
    def G_trace_pairs(T, G, q):
        # G_{ab}^{ab} style: contract two pairs with metric
        Gu = _raise_all(G)
        return float(np.einsum("abcd,abcd->", G, Gu))  # same as frobenius

    # Order 6
    def trT3(T, G, q):
        Tm = ETA[:, None] * T
        return float(np.trace(Tm @ Tm @ Tm))

    def q_trT2(T, G, q):
        return q * trT2(T, G, q)

    def q_G(T, G, q):
        return q * Gnorm(T, G, q)

    cats.append(("tr(T^3)", 6, trT3))
    cats.append(("(F·F)*tr(T^2)", 6, q_trT2))
    cats.append(("(F·F)*||G||^2", 6, q_G))

    # Order 8
    def trT4(T, G, q):
        Tm = ETA[:, None] * T
        M = Tm @ Tm
        return float(np.trace(M @ M))

    def trT2_sq(T, G, q):
        t = trT2(T, G, q)
        return t * t

    def Gnorm_sq(T, G, q):
        g = Gnorm(T, G, q)
        return g * g

    def trT2_G(T, G, q):
        return trT2(T, G, q) * Gnorm(T, G, q)

    def q4(T, G, q):
        return q**4

    def q_trT3(T, G, q):
        return q * trT3(T, G, q)

    def q2_trT2(T, G, q):
        return (q * q) * trT2(T, G, q)

    cats.append(("tr(T^4)", 8, trT4))
    cats.append(("[tr(T^2)]^2", 8, trT2_sq))
    cats.append(("[||G||^2]^2", 8, Gnorm_sq))
    cats.append(("tr(T^2)*||G||^2", 8, trT2_G))
    cats.append(("(F·F)^4", 8, q4))
    cats.append(("(F·F)*tr(T^3)", 8, q_trT3))
    cats.append(("(F·F)^2*tr(T^2)", 8, q2_trT2))

    # Higher traces as extra candidates (may be dependent)
    def trT5(T, G, q):
        Tm = ETA[:, None] * T
        M = Tm @ Tm @ Tm @ Tm @ Tm
        return float(np.trace(M))

    def trT6(T, G, q):
        Tm = ETA[:, None] * T
        M = Tm @ Tm @ Tm
        return float(np.trace(M @ M))

    cats.append(("tr(T^5)", 10, trT5))
    cats.append(("tr(T^6)", 12, trT6))

    # Det-like
    def detT(T, G, q):
        Tm = ETA[:, None] * T
        return float(np.linalg.det(Tm))

    cats.append(("det(T)", 10, detT))

    # More G-derived: contract G to a matrix then traces
    def G_to_M_tr2(T, G, q):
        # M_μν = G_μabc G_ν^abc
        Gu = _raise_all(G)
        M = np.tensordot(G, Gu, axes=([1, 2, 3], [1, 2, 3]))
        Mm = ETA[:, None] * M
        return float(np.trace(Mm @ Mm))

    def G_to_M_tr3(T, G, q):
        Gu = _raise_all(G)
        M = np.tensordot(G, Gu, axes=([1, 2, 3], [1, 2, 3]))
        Mm = ETA[:, None] * M
        return float(np.trace(Mm @ Mm @ Mm))

    cats.append(("tr(M_G^2)", 8, G_to_M_tr2))
    cats.append(("tr(M_G^3)", 12, G_to_M_tr3))

    # Extra T/G family members to push past the original ~8 when possible.
    def trT7(T, G, q):
        Tm = ETA[:, None] * T
        M = Tm @ Tm @ Tm @ Tm
        return float(np.trace(M @ Tm @ Tm @ Tm))

    def trT8(T, G, q):
        Tm = ETA[:, None] * T
        M = Tm @ Tm
        M2 = M @ M
        return float(np.trace(M2 @ M2))

    def G_to_M_tr4(T, G, q):
        Gu = _raise_all(G)
        M = np.tensordot(G, Gu, axes=([1, 2, 3], [1, 2, 3]))
        Mm = ETA[:, None] * M
        A = Mm @ Mm
        return float(np.trace(A @ A))

    def trT2_trT3(T, G, q):
        return trT2(T, G, q) * trT3(T, G, q)

    def trT2_trT4(T, G, q):
        return trT2(T, G, q) * trT4(T, G, q)

    def Gnorm_trT2(T, G, q):
        return Gnorm(T, G, q) * trT2(T, G, q)

    def Gnorm_trT3(T, G, q):
        return Gnorm(T, G, q) * trT3(T, G, q)

    def frobenius_T(T, G, q):
        return _lorentz_frobenius(T)

    def frobenius_T_sq(T, G, q):
        f = _lorentz_frobenius(T)
        return f * f

    cats.append(("||T||^2", 4, frobenius_T))
    cats.append(("[||T||^2]^2", 8, frobenius_T_sq))
    cats.append(("tr(T^7)", 14, trT7))
    cats.append(("tr(T^8)", 16, trT8))
    cats.append(("tr(M_G^4)", 16, G_to_M_tr4))
    cats.append(("tr(T^2)*tr(T^3)", 10, trT2_trT3))
    cats.append(("tr(T^2)*tr(T^4)", 12, trT2_trT4))
    cats.append(("||G||^2*tr(T^2)", 8, Gnorm_trT2))
    cats.append(("||G||^2*tr(T^3)", 10, Gnorm_trT3))

    return cats


def write_progress(path: Path, progress: SearchProgress) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(progress.to_json(), indent=2))
    tmp.replace(path)


def run_timed_search(
    duration_sec: float = 900.0,
    progress_path: Path = PROGRESS_DEFAULT,
    n_draws: int = 48,
    seed: int = 0,
    tol: float = 1e-5,
) -> SearchProgress:
    """
    Keep testing candidates for `duration_sec`, growing an independent set.
    """
    progress = SearchProgress(
        status="running",
        duration_sec=duration_sec,
        message="Starting timed search…",
        started_at=time.time(),
    )
    write_progress(progress_path, progress)

    catalog = candidate_catalog()
    rng = np.random.default_rng(seed)

    # Precompute feature matrix: rows=draws, cols=candidates
    # Do draws in batches while time remains; expand independence greedily.
    names = [c[0] for c in catalog]
    orders = [c[1] for c in catalog]
    fns = [c[2] for c in catalog]
    n_cand = len(catalog)

    values = np.zeros((0, n_cand))
    kept_idx: list[int] = []
    t0 = time.time()

    def elapsed() -> float:
        return time.time() - t0

    try:
        while elapsed() < duration_sec:
            # one more random draw
            F = random_chiral_five_form(rng)
            T, G, q = _build_T_and_G(F)
            row = np.array([fn(T, G, q) for fn in fns], dtype=float)
            # kill near-zeros / nan
            row = np.nan_to_num(row, nan=0.0, posinf=0.0, neginf=0.0)
            values = np.vstack([values, row])
            progress.draws_used = values.shape[0]
            progress.candidates_tested = n_cand
            progress.elapsed_sec = elapsed()

            # Recompute greedy independent set by order (respect polynomial products lightly:
            # first take linear independence of all columns; then we'll filter by order ladder)
            # Ladder: process candidates sorted by order
            order_sorted = sorted(range(n_cand), key=lambda i: (orders[i], i))
            kept_idx = []
            # Also include monomials of kept as extra columns conceptually via
            # checking each candidate against span of kept + products of kept.
            # For speed in timed UI: linear independence among candidate columns only,
            # plus drop anything that matches a product of already kept by correlation.

            for j in order_sorted:
                if elapsed() >= duration_sec:
                    break
                col = values[:, j]
                if np.max(np.abs(col)) < tol:
                    continue  # identically ~0
                # build matrix of kept cols + products of pairs of kept with matching order
                cols = [values[:, k] for k in kept_idx]
                # products
                for a in range(len(kept_idx)):
                    for b in range(a, len(kept_idx)):
                        oa, ob = orders[kept_idx[a]], orders[kept_idx[b]]
                        if oa + ob == orders[j]:
                            cols.append(values[:, kept_idx[a]] * values[:, kept_idx[b]])
                # triple products for higher
                for a in range(len(kept_idx)):
                    for b in range(a, len(kept_idx)):
                        for c in range(b, len(kept_idx)):
                            oa = orders[kept_idx[a]] + orders[kept_idx[b]] + orders[kept_idx[c]]
                            if oa == orders[j]:
                                cols.append(
                                    values[:, kept_idx[a]]
                                    * values[:, kept_idx[b]]
                                    * values[:, kept_idx[c]]
                                )
                base = np.column_stack(cols) if cols else np.zeros((values.shape[0], 0))
                trial = np.column_stack([base, col]) if base.size else col.reshape(-1, 1)
                # Relative SVD tolerance (None) — absolute tol falsely "discovers" products
                # when column magnitudes are huge.
                if numerical_rank(trial, tol=None) > numerical_rank(base, tol=None):
                    kept_idx.append(j)

            # update found list
            new_found = []
            for n, j in enumerate(kept_idx, start=1):
                new_found.append(
                    FoundInvariant(
                        id=n,
                        name=names[j],
                        order=orders[j],
                        found_at_sec=round(elapsed(), 2),
                    )
                )
            progress.found = new_found
            progress.found_count = len(new_found)
            by: dict[str, int] = {}
            for inv in new_found:
                by[str(inv.order)] = by.get(str(inv.order), 0) + 1
            progress.by_order = by
            progress.message = (
                f"Found {progress.found_count} / ~{progress.target} · "
                f"{progress.draws_used} random tests · "
                f"{int(progress.elapsed_sec)}s / {int(duration_sec)}s"
            )
            write_progress(progress_path, progress)

            # small yield so UI can poll; also avoid burning CPU only on rank
            if values.shape[0] >= n_draws and elapsed() > 30:
                # keep adding draws but sleep briefly
                time.sleep(0.05)

        progress.status = "done"
        progress.elapsed_sec = elapsed()
        progress.message = (
            f"Time’s up. Found {progress.found_count} independent starter-family "
            f"invariants (target ~{progress.target}). More auto-graphs needed to climb higher."
        )
        write_progress(progress_path, progress)
    except Exception as e:
        progress.status = "error"
        progress.message = str(e)
        progress.elapsed_sec = elapsed()
        write_progress(progress_path, progress)
        raise

    return progress
