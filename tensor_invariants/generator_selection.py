"""
Blind selection of algebra generators from connected contractions.

At each even degree N:

  C_N = evaluation matrix of connected degree-N contractions
  P_N = evaluation matrix of weighted-degree-N monomials in accepted generators

  n_new = rank([P_N | C_N]) - rank(P_N)

No answer key is used during selection.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Literal, Sequence

import numpy as np

from .antisymmetric_tensors import random_antisymmetric_form
from .contraction_compiler import make_evaluator, make_metric_evaluator
from .finite_field import DEFAULT_DISCOVERY_PRIMES
from .graph_enumeration import (
    ContractionGraph,
    enumerate_contraction_graphs,
    sample_contraction_graphs,
)
from .monomial_basis import NamedGenerator, evaluate_monomial_row, weighted_monomials
from .nullspace import rank_mod_p
from .numerical_rank import svd_rank, zero_small_columns
from .tensor_spaces import metric_diagonal

logger = logging.getLogger(__name__)

DEFAULT_CACHE_DIR = Path("checkpoints") / "graphs"


@dataclass
class DegreeReport:
    degree: int
    n_graphs: int
    connected_rank: int
    n_lower_monomials: int
    rank_P: int
    rank_PC: int
    n_new: int
    selected_graph_ids: list[str]
    monomial_names: list[str]
    elapsed_sec: float
    backend: str
    proof_status: str


@dataclass
class DiscoveryState:
    generators: list[NamedGenerator] = field(default_factory=list)
    reports: list[DegreeReport] = field(default_factory=list)
    graphs_by_degree: dict[int, list[ContractionGraph]] = field(default_factory=dict)
    extras: dict[str, Any] = field(default_factory=dict)

    @property
    def degrees(self) -> list[int]:
        return [g.degree for g in self.generators]


def _build_matrices(
    graphs: Sequence[ContractionGraph],
    gens: Sequence[NamedGenerator],
    degree: int,
    tensors: Sequence[np.ndarray],
    *,
    metric_diag: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, list[str], list[Any]]:
    monos = weighted_monomials(gens, degree)
    evaluators = []
    ids = []
    for g in graphs:
        if metric_diag is None:
            _, ev = make_evaluator(g)
        else:
            _, ev = make_metric_evaluator(g, metric_diag)
        evaluators.append(ev)
        ids.append(g.canonical_id)

    n = len(tensors)
    P = np.zeros((n, len(monos)), dtype=float)
    C = np.zeros((n, len(evaluators)), dtype=float)
    for i, T in enumerate(tensors):
        if monos:
            P[i, :] = evaluate_monomial_row(gens, monos, T)
        for j, ev in enumerate(evaluators):
            C[i, j] = float(ev(T))
    return P, C, ids, monos


def _rank(M: np.ndarray, backend: str, primes: Sequence[int]) -> int:
    if M.size == 0:
        return 0
    # Drop analytically-vanishing / float-noise columns before ranking.
    M = zero_small_columns(M)
    if backend == "svd":
        # Absolute floor kills 1e-13 self-dual quadratic residuals.
        return svd_rank(M, abs_tol=1e-8)
    if backend == "modp":
        # Scale floats to integers approximately — for discovery prefer integer tensors
        A = np.rint(M).astype(object) if np.allclose(M, np.rint(M), atol=1e-6) else None
        if A is None:
            return svd_rank(M, abs_tol=1e-8)
        ranks = [rank_mod_p(A, int(p)) for p in primes]
        if len(set(ranks)) != 1:
            logger.warning("modular ranks disagree: %s; falling back to SVD", ranks)
            return svd_rank(M, abs_tol=1e-8)
        return ranks[0]
    raise ValueError(backend)


def select_new_columns(
    P: np.ndarray,
    C: np.ndarray,
    *,
    backend: str = "svd",
    primes: Sequence[int] = DEFAULT_DISCOVERY_PRIMES,
) -> tuple[list[int], int, int, int]:
    """
    Greedily select columns of C that increase rank beyond span(P).

    Returns (selected_indices, rank_P, rank_PC, connected_rank).
    """
    rank_P = _rank(P, backend, primes)
    # Connected rank among C alone
    connected_rank = _rank(C, backend, primes)

    selected: list[int] = []
    for j in range(C.shape[1]):
        cols_new = [C[:, k] for k in selected] + [C[:, j]]
        base_cols = [C[:, k] for k in selected]
        if P.size:
            base = np.column_stack([P] + base_cols) if base_cols else P
            trial = np.column_stack([P] + cols_new)
        else:
            base = np.column_stack(base_cols) if base_cols else np.zeros((C.shape[0], 0))
            trial = np.column_stack(cols_new)
        if _rank(trial, backend, primes) > _rank(base, backend, primes):
            selected.append(j)

    if P.size and selected:
        PC = np.column_stack([P, C[:, selected]])
    elif selected:
        PC = C[:, selected]
    elif P.size:
        PC = P
    else:
        PC = np.zeros((C.shape[0], 0))
    rank_PC = _rank(PC, backend, primes)
    n_new = rank_PC - rank_P
    # Consistency: greedy count should match n_new
    if len(selected) != n_new:
        # Recompute n_new from full C
        if P.size and C.size:
            full = np.column_stack([P, C])
        elif C.size:
            full = C
        else:
            full = P if P.size else np.zeros((0, 0))
        n_new = _rank(full, backend, primes) - rank_P
        # Keep greedy selected truncated/padded is wrong — trust dimension formula
        # and keep greedy list as explicit generators chosen
    return selected, rank_P, rank_PC, connected_rank


def load_or_enumerate_graphs(
    n_vertices: int,
    form_rank: int = 3,
    *,
    cache_dir: Path | None = DEFAULT_CACHE_DIR,
    force: bool = False,
    sample_if_large: bool = True,
    sample_target: int = 60,
) -> list[ContractionGraph]:
    """Load cached multiplicity matrices or enumerate/sample and cache them."""
    if cache_dir is not None:
        cache_dir.mkdir(parents=True, exist_ok=True)
        path = cache_dir / f"graphs_N{n_vertices}_r{form_rank}.json"
        if path.exists() and not force:
            data = json.loads(path.read_text(encoding="utf-8"))
            graphs = [
                ContractionGraph(
                    multiplicity=tuple(tuple(row) for row in m),
                    form_rank=form_rank,
                )
                for m in data["multiplicities"]
            ]
            logger.info("Loaded %s cached graphs for N=%s", len(graphs), n_vertices)
            return graphs

    # Exact enum is practical through N=8 for 3-forms; larger → sample.
    if sample_if_large and (n_vertices >= 10 or (form_rank >= 5 and n_vertices >= 6)):
        logger.info("Sampling graphs at N=%s (exact census deferred)", n_vertices)
        graphs = sample_contraction_graphs(
            n_vertices,
            form_rank,
            target=sample_target if n_vertices < 10 else min(sample_target, 12),
            seed=n_vertices * 17 + form_rank,
            max_attempts=50_000 if n_vertices < 10 else 20_000,
        )
        sampled = True
    else:
        enum = enumerate_contraction_graphs(n_vertices, form_rank, connected_only=True)
        graphs = enum["graphs"]
        sampled = False

    if cache_dir is not None:
        path = cache_dir / f"graphs_N{n_vertices}_r{form_rank}.json"
        path.write_text(
            json.dumps(
                {
                    "n_vertices": n_vertices,
                    "form_rank": form_rank,
                    "nonisomorphic_count": len(graphs),
                    "multiplicities": [g.multiplicity for g in graphs],
                    "canonical_ids": [g.canonical_id for g in graphs],
                    "sampled": sampled,
                }
            ),
            encoding="utf-8",
        )
    return graphs


def discover_degree(
    degree: int,
    state: DiscoveryState,
    *,
    dim: int = 6,
    form_rank: int = 3,
    n_samples: int = 64,
    seed: int = 0,
    backend: Literal["svd", "modp"] = "svd",
    primes: Sequence[int] = DEFAULT_DISCOVERY_PRIMES,
    sample_mode: Literal["float", "int"] = "float",
    graphs: Sequence[ContractionGraph] | None = None,
    cache_dir: Path | None = DEFAULT_CACHE_DIR,
    max_graphs: int | None = None,
    tensors: Sequence[np.ndarray] | None = None,
    metric_diag: np.ndarray | None = None,
    sample_if_large: bool = True,
) -> DegreeReport:
    """Enumerate (or use provided) graphs at ``degree`` and select new generators."""
    t0 = time.time()
    if graphs is None:
        graphs = load_or_enumerate_graphs(
            degree,
            form_rank,
            cache_dir=cache_dir,
            sample_if_large=sample_if_large,
        )
    if max_graphs is not None and len(graphs) > max_graphs:
        logger.warning(
            "N=%s: using first %s of %s graphs (sampling cap)",
            degree,
            max_graphs,
            len(graphs),
        )
        graphs = list(graphs)[:max_graphs]
    state.graphs_by_degree[degree] = list(graphs)

    if tensors is None:
        rng = np.random.default_rng(seed + 1000 * degree)
        tensors = [
            random_antisymmetric_form(dim, form_rank, rng, mode=sample_mode, int_bound=5)
            for _ in range(n_samples)
        ]
    # Convert object int tensors to float for einsum
    tensors_f = [np.asarray(T, dtype=float) for T in tensors]

    P, C, ids, monos = _build_matrices(
        graphs, state.generators, degree, tensors_f, metric_diag=metric_diag
    )
    selected, rank_P, rank_PC, connected_rank = select_new_columns(
        P, C, backend=backend, primes=primes
    )
    n_new = rank_PC - rank_P

    for k, j in enumerate(selected):
        gid = ids[j]
        name = f"g^({degree})" if n_new == 1 else f"g^({degree})_{k+1}"

        def _make_ev(graph=graphs[j], gdiag=metric_diag):
            if gdiag is None:
                _, ev = make_evaluator(graph)
            else:
                _, ev = make_metric_evaluator(graph, gdiag)
            return ev

        ev = _make_ev()
        state.generators.append(NamedGenerator(name=name, degree=degree, evaluate=ev))

    report = DegreeReport(
        degree=degree,
        n_graphs=len(graphs),
        connected_rank=connected_rank,
        n_lower_monomials=len(monos),
        rank_P=rank_P,
        rank_PC=rank_PC,
        n_new=n_new,
        selected_graph_ids=[ids[j] for j in selected],
        monomial_names=[m.name for m in monos],
        elapsed_sec=time.time() - t0,
        backend=backend,
        proof_status="strong computational evidence"
        if backend == "svd"
        else "exact finite-field computation",
    )
    state.reports.append(report)
    logger.info(
        "N=%s graphs=%s connected_rank=%s n_new=%s P=%s PC=%s (%.2fs)",
        degree,
        report.n_graphs,
        connected_rank,
        n_new,
        rank_P,
        rank_PC,
        report.elapsed_sec,
    )
    return report


def reproduce_6d(
    *,
    max_degree: int = 10,
    n_samples: int = 80,
    seed: int = 1,
    backend: Literal["svd", "modp"] = "svd",
    cache_dir: Path | None = DEFAULT_CACHE_DIR,
) -> DiscoveryState:
    """Blind reproduction of the 6D three-form generator ladder."""
    state = DiscoveryState()
    for n in range(2, max_degree + 1, 2):
        # N=10 full census is very large; sample a small connected set.
        # Evaluating many 10-fold contractions is expensive — keep samples modest.
        max_graphs = 12 if n >= 10 else None
        discover_degree(
            n,
            state,
            dim=6,
            form_rank=3,
            n_samples=n_samples if n < 10 else min(n_samples, 16),
            seed=seed,
            backend=backend,
            sample_mode="float",
            cache_dir=cache_dir,
            max_graphs=max_graphs,
        )
    return state


def _i4_tr_m2(T: np.ndarray, metric_diag: np.ndarray) -> float:
    """I_4 = tr(M^2) with M_{μν} = F_{μ a b c d} F_ν{}^{a b c d} (raise contracted indices only)."""
    # Raise axes 1..4 of a copy; leave the free first index lowered.
    Tr = np.array(T, dtype=float, copy=True)
    for ax in range(1, 5):
        factors = np.ones(Tr.shape, dtype=float)
        for i, s in enumerate(metric_diag):
            sl = [slice(None)] * Tr.ndim
            sl[ax] = i
            factors[tuple(sl)] = float(s)
        Tr *= factors
    # M[μ,ν] = sum_{abcd} F[μ,abcd] F[ν,abcd] * η^{aa}…η^{dd}
    M = np.tensordot(T, Tr, axes=([1, 2, 3, 4], [1, 2, 3, 4]))
    # Mixed: M_μ^ν = M_{μσ} η^{σν}; for this diagonal signature η^{σσ}=η_{σσ}.
    M_mixed = M * metric_diag[None, :]
    return float(np.tensordot(M_mixed, M_mixed, axes=([0, 1], [1, 0])))


def discover_10d(
    *,
    max_degree: int = 6,
    n_samples: int = 32,
    seed: int = 2,
    backend: Literal["svd", "modp"] = "svd",
    cache_dir: Path | None = DEFAULT_CACHE_DIR,
) -> DiscoveryState:
    """
    Blind discovery for a Lorentzian self-dual 5-form in d=10.

    Samples from the self-dual subspace; contracts with η=diag(-1,+1×9).
    Does not use literature Hilbert numbers as an answer key.
    """
    from .self_duality import combo_to_dense, random_self_dual_5form_combo

    state = DiscoveryState()
    gdiag = metric_diagonal(10, "lorentzian")
    rng = np.random.default_rng(seed)
    logger.info("Sampling %s self-dual dense 5-forms (seed=%s)…", n_samples, seed)
    tensors = [
        combo_to_dense(random_self_dual_5form_combo(rng)) for _ in range(n_samples)
    ]

    # Exact connected censuses are cheap through N=6 for 5-forms (49 graphs).
    for n in range(2, max_degree + 1, 2):
        sample_if_large = n >= 8  # N=8 has ~1753 canonical graphs
        max_graphs = 80 if n >= 8 else None
        discover_degree(
            n,
            state,
            dim=10,
            form_rank=5,
            n_samples=n_samples,
            seed=seed,
            backend=backend,
            tensors=tensors,
            metric_diag=gdiag,
            cache_dir=cache_dir,
            sample_if_large=sample_if_large,
            max_graphs=max_graphs,
        )

    # Cross-check: selected degree-4 generator vs explicit I4=tr(M^2)
    if any(g.degree == 4 for g in state.generators):
        g4 = next(g for g in state.generators if g.degree == 4)
        ratios = []
        for T in tensors[: min(8, len(tensors))]:
            a = float(g4.evaluate(T))
            b = _i4_tr_m2(T, gdiag)
            if abs(b) > 1e-12:
                ratios.append(a / b)
        state.extras["i4_crosscheck"] = {
            "ratios_graph_over_I4": ratios,
            "ratio_mean": float(np.mean(ratios)) if ratios else None,
            "ratio_std": float(np.std(ratios)) if ratios else None,
            "proof_status": "strong computational evidence",
            "note": "Constant ratio ⇒ selected degree-4 graph spans the I4=tr(M^2) line.",
        }
    return state
