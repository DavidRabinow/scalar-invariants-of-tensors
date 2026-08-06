"""Compile weighted contraction graphs into einsum plans."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from string import ascii_letters
from typing import Callable

import numpy as np

from .graph_enumeration import ContractionGraph

ALPHABET = ascii_letters + "".join(chr(c) for c in range(0x00C0, 0x00C0 + 120))


@dataclass(frozen=True)
class CompiledContraction:
    graph_id: str
    n_vertices: int
    form_rank: int
    einsum_subscripts: str
    pairing: tuple[tuple[int, int], ...]

    def evaluate_dense(self, tensors: list[np.ndarray]) -> float:
        if len(tensors) != self.n_vertices:
            raise ValueError("tensor count mismatch")
        from opt_einsum import contract

        return float(contract(self.einsum_subscripts, *tensors, optimize="greedy"))


def compile_graph(graph: ContractionGraph, *, slot_policy: str = "pop") -> CompiledContraction:
    """
    Pair free index slots according to edge multiplicities.

    Vertex v owns slots [r*v, ..., r*v+r-1]. An edge of weight w between u and v
    identifies w slots of u with w slots of v.
    """
    n = graph.n_vertices
    r = graph.form_rank
    free = {v: list(range(r * v, r * v + r)) for v in range(n)}
    if slot_policy == "reverse":
        for v in free:
            free[v].reverse()
    pairs: list[tuple[int, int]] = []
    for i, j, w in graph.edge_list():
        for _ in range(w):
            if not free[i] or not free[j]:
                raise RuntimeError("degree mismatch while pairing slots")
            if slot_policy == "pop0":
                pairs.append((free[i].pop(0), free[j].pop(0)))
            else:
                pairs.append((free[i].pop(), free[j].pop()))
    if any(free[v] for v in range(n)):
        raise RuntimeError("unused slots — graph not regular of degree r")

    n_slots = r * n
    if n_slots > len(ALPHABET):
        raise ValueError(f"need {n_slots} letters, alphabet has {len(ALPHABET)}")

    letters = [""] * n_slots
    next_i = 0
    for a, b in pairs:
        ch = ALPHABET[next_i]
        next_i += 1
        letters[a] = ch
        letters[b] = ch

    subs = ["".join(letters[r * v : r * v + r]) for v in range(n)]
    einsum = ",".join(subs) + "->"
    return CompiledContraction(
        graph_id=f"raw[{graph.n_vertices}:{hash(graph.multiplicity) & 0xFFFFFFFF:x}]",
        n_vertices=n,
        form_rank=r,
        einsum_subscripts=einsum,
        pairing=tuple(pairs),
    )


@lru_cache(maxsize=256)
def _cached_compile(mult: tuple[tuple[int, ...], ...], form_rank: int, policy: str) -> CompiledContraction:
    g = ContractionGraph(multiplicity=mult, form_rank=form_rank)
    return compile_graph(g, slot_policy=policy)


def make_evaluator(graph: ContractionGraph) -> tuple[CompiledContraction, Callable[[np.ndarray], float]]:
    compiled = _cached_compile(graph.multiplicity, graph.form_rank, "pop")

    def eval_fn(T: np.ndarray) -> float:
        return compiled.evaluate_dense([T] * compiled.n_vertices)

    return compiled, eval_fn


def make_metric_evaluator(
    graph: ContractionGraph,
    metric_diag: np.ndarray,
) -> tuple[CompiledContraction, Callable[[np.ndarray], float]]:
    """
    Lorentz-invariant contraction: each identified index pair is contracted with η.

    For diagonal η this is equivalent to inserting one factor η^{kk} for every
    contracted index value k. Euclidean η=diag(1,…,1) recovers make_evaluator.
    """
    compiled = _cached_compile(graph.multiplicity, graph.form_rank, "pop")
    g = np.asarray(metric_diag, dtype=float)
    if g.ndim != 1:
        raise ValueError("metric_diag must be 1-D diagonal components")

    body = compiled.einsum_subscripts.split("->")[0]
    letters: list[str] = []
    seen: set[str] = set()
    for part in body.split(","):
        for ch in part:
            if ch not in seen:
                seen.add(ch)
                letters.append(ch)
    if not letters:
        raise RuntimeError("compiled graph has no contracted letters")
    einsum = body + "," + ",".join(letters) + "->"
    n = compiled.n_vertices
    n_letters = len(letters)

    def eval_fn(T: np.ndarray) -> float:
        from opt_einsum import contract

        ops: list[np.ndarray] = [T] * n + [g] * n_letters
        return float(contract(einsum, *ops, optimize="greedy"))

    return compiled, eval_fn
