"""Machine-readable and markdown reporting for invariant discovery runs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Sequence

from .generator_selection import DiscoveryState, DegreeReport
from .syzygies import SyzygyRelation


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")


def report_graphs(state: DiscoveryState) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for n, graphs in sorted(state.graphs_by_degree.items()):
        out[str(n)] = {
            "count": len(graphs),
            "canonical_ids": [g.canonical_id for g in graphs],
            "multiplicities": [g.multiplicity for g in graphs],
        }
    return out


def report_ranks(state: DiscoveryState) -> dict[str, Any]:
    return {
        str(r.degree): {
            "n_graphs": r.n_graphs,
            "connected_rank": r.connected_rank,
            "n_lower_monomials": r.n_lower_monomials,
            "rank_P": r.rank_P,
            "rank_PC": r.rank_PC,
            "n_new": r.n_new,
            "monomial_names": r.monomial_names,
            "backend": r.backend,
            "proof_status": r.proof_status,
            "elapsed_sec": r.elapsed_sec,
        }
        for r in state.reports
    }


def report_generators(state: DiscoveryState) -> dict[str, Any]:
    return {
        "degrees": state.degrees,
        "names": [g.name for g in state.generators],
        "selected_graph_ids": {
            str(r.degree): r.selected_graph_ids for r in state.reports if r.n_new
        },
    }


def write_6d_outputs(
    out_dir: Path,
    state: DiscoveryState,
    syzygies: Sequence[SyzygyRelation] | None = None,
    expected: dict[str, Any] | None = None,
) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    graphs = report_graphs(state)
    ranks = report_ranks(state)
    gens = report_generators(state)
    syz = [s.to_dict() for s in (syzygies or [])]
    write_json(out_dir / "graphs.json", graphs)
    write_json(out_dir / "ranks.json", ranks)
    write_json(out_dir / "generators.json", gens)
    write_json(out_dir / "syzygies.json", syz)

    comparison = compare_to_expected(state, expected or {})
    return {
        "graphs": graphs,
        "ranks": ranks,
        "generators": gens,
        "syzygies": syz,
        "comparison": comparison,
    }


def compare_to_expected(state: DiscoveryState, expected: dict[str, Any]) -> dict[str, Any]:
    graph_counts = {r.degree: r.n_graphs for r in state.reports}
    connected_ranks = {r.degree: r.connected_rank for r in state.reports}
    new_gens = {r.degree: r.n_new for r in state.reports}
    computed = set(graph_counts)

    exp_graphs = {
        int(k): v
        for k, v in (expected.get("graph_counts") or {}).items()
        if int(k) in computed
    }
    exp_ranks = {
        int(k): v
        for k, v in (expected.get("connected_ranks") or {}).items()
        if int(k) in computed
    }
    exp_new = {
        int(k): v
        for k, v in (expected.get("new_generators") or {}).items()
        if int(k) in computed
    }
    exp_degrees = expected.get("generator_degrees") or [2, 4, 4, 6, 8]
    # Only require generator degrees whose order was reached
    max_computed = max(computed) if computed else 0
    exp_degrees_trunc = [d for d in exp_degrees if d <= max_computed]

    def match(a: dict, b: dict) -> bool:
        return all(a.get(k) == b.get(k) for k in b)

    return {
        "graph_counts": {"got": graph_counts, "expected": exp_graphs, "ok": match(graph_counts, exp_graphs)},
        "connected_ranks": {
            "got": connected_ranks,
            "expected": exp_ranks,
            "ok": match(connected_ranks, exp_ranks),
        },
        "new_generators": {"got": new_gens, "expected": exp_new, "ok": match(new_gens, exp_new)},
        "generator_degrees": {
            "got": state.degrees,
            "expected": exp_degrees_trunc,
            "ok": list(state.degrees) == list(exp_degrees_trunc),
        },
    }


def write_6d_markdown(path: Path, bundle: dict[str, Any]) -> None:
    comp = bundle["comparison"]
    lines = [
        "# Six-dimensional reproduction report",
        "",
        "Blind discovery of polynomial invariants of a generic antisymmetric 3-form",
        "in six Euclidean dimensions, compared to Elamaran–Ferko–Scarlett",
        "(*Machine Learning Invariants of Tensors*, arXiv:2512.23750).",
        "",
        "## Generator degrees",
        "",
        f"- Obtained: `{comp['generator_degrees']['got']}`",
        f"- Expected: `{comp['generator_degrees']['expected']}`",
        f"- Match: **{comp['generator_degrees']['ok']}**",
        "",
        "## Graph counts / connected ranks / new generators",
        "",
        "| Degree | Graphs (got/exp) | Connected rank (got/exp) | New gens (got/exp) |",
        "|--------|------------------|---------------------------|---------------------|",
    ]
    degrees = sorted(
        set(comp["graph_counts"]["expected"])
        | set(comp["graph_counts"]["got"])
        | set(comp["new_generators"]["expected"])
    )
    for n in degrees:
        g = comp["graph_counts"]["got"].get(n)
        ge = comp["graph_counts"]["expected"].get(n)
        r = comp["connected_ranks"]["got"].get(n)
        re = comp["connected_ranks"]["expected"].get(n)
        ng = comp["new_generators"]["got"].get(n)
        ne = comp["new_generators"]["expected"].get(n)
        lines.append(f"| {n} | {g}/{ge} | {r}/{re} | {ng}/{ne} |")
    lines += [
        "",
        "## Proof-status labels",
        "",
        "- Graph enumeration counts: exact combinatorial enumeration.",
        "- Ranks / new generators: strong computational evidence (numerical SVD),",
        "  cross-checked with finite-field ranks in the test suite.",
        "- Syzygies: rationally reconstructed / finite-field identities on tested samples",
        "  — **not** claimed as symbolic proofs unless separately established.",
        "",
        "## Machine-readable outputs",
        "",
        "- `outputs/6d/graphs.json`",
        "- `outputs/6d/ranks.json`",
        "- `outputs/6d/generators.json`",
        "- `outputs/6d/syzygies.json`",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
