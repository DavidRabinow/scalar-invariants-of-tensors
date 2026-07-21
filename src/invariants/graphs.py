"""
Enumeration of connected loopless weighted multigraphs for p-form contractions.

Each vertex = one copy of an antisymmetric rank-``form_rank`` tensor.
Edge weight = number of contracted index pairs between two tensors.
Every vertex has total weighted degree exactly ``form_rank``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Any

import networkx as nx
import numpy as np


@dataclass(frozen=True)
class ContractionGraph:
    """Undirected multigraph encoded by a symmetric multiplicity matrix."""

    multiplicity: tuple[tuple[int, ...], ...]
    form_rank: int

    @property
    def n_vertices(self) -> int:
        return len(self.multiplicity)

    @property
    def canonical_id(self) -> str:
        return canonical_multiplicity_id(self.multiplicity)

    def to_networkx(self) -> nx.MultiGraph:
        n = self.n_vertices
        G = nx.MultiGraph()
        G.add_nodes_from(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                w = self.multiplicity[i][j]
                for _ in range(w):
                    G.add_edge(i, j)
        return G

    def edge_list(self) -> list[tuple[int, int, int]]:
        edges = []
        n = self.n_vertices
        for i in range(n):
            for j in range(i + 1, n):
                w = self.multiplicity[i][j]
                if w:
                    edges.append((i, j, w))
        return edges


def canonical_multiplicity_id(mult: tuple[tuple[int, ...], ...]) -> str:
    """
    Deterministic canonical labeling.

    For n<=6 use exact min-lex over permutations; for larger n use a stable
    Weisfeiler–Lehman hash of the multiplicity multigraph (exact Aut search
    is n!-expensive and was stalling N=8 overnight).
    """
    n = len(mult)
    if n <= 6:
        M = np.array(mult, dtype=int)
        best: tuple[int, ...] | None = None
        for p in permutations(range(n)):
            P = M[np.ix_(p, p)]
            tri = tuple(int(P[i, j]) for i in range(n) for j in range(i + 1, n))
            if best is None or tri < best:
                best = tri
        assert best is not None
        return "M[" + ",".join(str(x) for x in best) + "]"

    G = _as_nx([list(row) for row in mult])
    # Edge labels = multiplicity between pairs (already multi-edges in G).
    try:
        h = nx.weisfeiler_lehman_graph_hash(G)
    except Exception:
        # Fallback: sorted degree + sorted edge multiset
        degs = tuple(sorted(dict(G.degree()).values()))
        edges = tuple(sorted((min(u, v), max(u, v)) for u, v in G.edges()))
        h = f"{degs}|{edges}"
    return f"WL[{h}]"


def _fingerprint(mult: list[list[int]]) -> tuple:
    """Cheap isomorphism invariant for pre-filtering."""
    n = len(mult)
    degs = tuple(sorted(_degrees(mult)))
    # Sorted list of edge weights
    weights = tuple(
        sorted(mult[i][j] for i in range(n) for j in range(i + 1, n) if mult[i][j])
    )
    # Degree sequence of the line-ish: for each vertex, sorted incident weights
    local = []
    for i in range(n):
        local.append(tuple(sorted(mult[i][j] for j in range(n) if j != i and mult[i][j])))
    local_t = tuple(sorted(local))
    return degs, weights, local_t


def sample_contraction_graphs(
    n_vertices: int,
    form_rank: int,
    *,
    target: int = 120,
    seed: int = 0,
    max_attempts: int = 80_000,
    connected_only: bool = True,
    progress: Any = None,
) -> dict[str, Any]:
    """
    Random search for distinct form_rank-regular loopless multigraphs.

    Used when exact enumeration is too slow (e.g. 5-regular N=8). Not a
    complete census — a climb ladder to grow the candidate pool.
    """
    rng = np.random.default_rng(seed)
    n = n_vertices
    unique: list[ContractionGraph] = []
    unique_nx: list[nx.MultiGraph] = []
    attempts = 0

    while len(unique) < target and attempts < max_attempts:
        attempts += 1
        stubs: list[int] = []
        for v in range(n):
            stubs.extend([v] * form_rank)
        rng.shuffle(stubs)
        mult = [[0] * n for _ in range(n)]
        ok = True
        for a in range(0, len(stubs), 2):
            u, v = stubs[a], stubs[a + 1]
            if u == v:
                ok = False
                break
            i, j = (u, v) if u < v else (v, u)
            mult[i][j] += 1
            mult[j][i] += 1
            if mult[i][j] > form_rank:
                ok = False
                break
        if not ok:
            continue
        if any(d != form_rank for d in _degrees(mult)):
            continue
        Gnx = _as_nx(mult)
        if connected_only and n > 1 and not nx.is_connected(Gnx):
            continue
        dup = False
        for H in unique_nx:
            if nx.is_isomorphic(Gnx, H):
                dup = True
                break
        if dup:
            continue
        M = tuple(tuple(row) for row in mult)
        unique.append(ContractionGraph(multiplicity=M, form_rank=form_rank))
        unique_nx.append(Gnx)
        if progress and len(unique) % 10 == 0:
            progress(
                f"Sampled {len(unique)}/{target} N={n} graphs",
                {"stage": "sample_graphs", "completed": len(unique), "total": target},
            )

    return {
        "n_vertices": n,
        "form_rank": form_rank,
        "raw_assignments": attempts,
        "connected_count": len(unique),
        "nonisomorphic_count": len(unique),
        "graphs": unique,
        "canonical_ids": [g.canonical_id for g in unique],
        "sampled": True,
        "target": target,
        "attempts": attempts,
    }


def _degrees(mult: list[list[int]]) -> list[int]:
    n = len(mult)
    return [sum(mult[i][j] for j in range(n) if j != i) for i in range(n)]


def _as_nx(mult: list[list[int]]) -> nx.MultiGraph:
    n = len(mult)
    G = nx.MultiGraph()
    G.add_nodes_from(range(n))
    for i, j in combinations(range(n), 2):
        for _ in range(mult[i][j]):
            G.add_edge(i, j)
    return G


def enumerate_contraction_graphs(
    n_vertices: int,
    form_rank: int,
    *,
    connected_only: bool = True,
) -> dict[str, Any]:
    """
    Exact backtracking enumeration; dedupe online via NetworkX isomorphism.
    """
    empty = {
        "n_vertices": n_vertices,
        "form_rank": form_rank,
        "raw_assignments": 0,
        "connected_count": 0,
        "nonisomorphic_count": 0,
        "graphs": [],
        "canonical_ids": [],
    }
    if n_vertices < 1:
        return empty
    if (n_vertices * form_rank) % 2 != 0:
        empty["note"] = "impossible by handshaking lemma"
        return empty

    n = n_vertices
    mult = [[0] * n for _ in range(n)]
    raw = 0
    connected_count = 0
    unique: list[ContractionGraph] = []
    unique_nx: list[nx.MultiGraph] = []
    unique_fp: list[tuple] = []

    def consider() -> None:
        nonlocal connected_count
        degs = _degrees(mult)
        if any(d != form_rank for d in degs):
            return
        Gnx = _as_nx(mult)
        if connected_only and n > 1 and not nx.is_connected(Gnx):
            return
        connected_count += 1
        fp = _fingerprint(mult)
        for H, hfp in zip(unique_nx, unique_fp):
            if hfp != fp:
                continue
            if nx.is_isomorphic(Gnx, H):
                return
        M = tuple(tuple(row) for row in mult)
        g = ContractionGraph(multiplicity=M, form_rank=form_rank)
        unique.append(g)
        unique_nx.append(Gnx)
        unique_fp.append(fp)

    def rec(v: int) -> None:
        nonlocal raw
        if v == n:
            raw += 1
            consider()
            return

        need = form_rank - sum(mult[v][u] for u in range(v))
        if need < 0:
            return
        partners = list(range(v + 1, n))

        def assign(k: int, left: int) -> None:
            if left == 0:
                rec(v + 1)
                return
            if k == len(partners):
                return
            j = partners[k]
            used_j = sum(mult[j][u] for u in range(j))
            max_m = min(left, form_rank - used_j, form_rank)
            for m in range(max_m + 1):
                if m:
                    mult[v][j] = mult[j][v] = m
                assign(k + 1, left - m)
                if m:
                    mult[v][j] = mult[j][v] = 0

        if need == 0:
            rec(v + 1)
        elif not partners:
            return
        else:
            assign(0, need)

    rec(0)
    ids = [g.canonical_id for g in unique]
    return {
        "n_vertices": n_vertices,
        "form_rank": form_rank,
        "raw_assignments": raw,
        "connected_count": connected_count,
        "nonisomorphic_count": len(unique),
        "graphs": unique,
        "canonical_ids": ids,
    }


def summarize_orders(form_rank: int, max_order: int) -> list[dict]:
    rows = []
    for n in range(2, max_order + 1, 2):
        result = enumerate_contraction_graphs(n, form_rank)
        rows.append(
            {
                "N": n,
                "raw_assignments": result["raw_assignments"],
                "connected_count": result["connected_count"],
                "nonisomorphic_count": result["nonisomorphic_count"],
                "canonical_ids": result["canonical_ids"],
            }
        )
    return rows
