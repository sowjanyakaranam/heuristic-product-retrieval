from __future__ import annotations
from typing import List, Dict, Any
from astar_baseline import astar_search, brute_force_search
from heuristics import baseline_heuristic, tight_heuristic

def run_correctness_test(products, query_embedding, k: int, lam: float = 0.30) -> Dict[str, Any]:
    astar_result = astar_search(products, query_embedding, k, baseline_heuristic, lam=lam)
    brute_result = brute_force_search(products, query_embedding, k, lam=lam)
    return {
        "k": k,
        "astar_objective": astar_result["objective"],
        "bruteforce_objective": brute_result["objective"],
        "objective_match": abs(astar_result["objective"] - brute_result["objective"]) < 1e-9,
        "astar_nodes": astar_result["nodes_expanded"],
        "astar_runtime_sec": astar_result["runtime_sec"],
        "bruteforce_runtime_sec": brute_result["runtime_sec"],
    }

def run_baseline_vs_tight(products, query_embedding, k: int, lam: float = 0.30) -> Dict[str, Any]:
    baseline = astar_search(products, query_embedding, k, baseline_heuristic, lam=lam)
    tight = astar_search(products, query_embedding, k, tight_heuristic, lam=lam)
    return {
        "k": k,
        "baseline_objective": baseline["objective"],
        "tight_objective": tight["objective"],
        "baseline_nodes": baseline["nodes_expanded"],
        "tight_nodes": tight["nodes_expanded"],
        "baseline_runtime_sec": baseline["runtime_sec"],
        "tight_runtime_sec": tight["runtime_sec"],
    }

def run_scaling_experiment(products, query_embedding, sizes: List[int], k: int, lam: float = 0.30) -> List[Dict[str, Any]]:
    out = []
    for n in sizes:
        subset = products[:n]
        baseline = astar_search(subset, query_embedding, k, baseline_heuristic, lam=lam)
        tight = astar_search(subset, query_embedding, k, tight_heuristic, lam=lam)
        out.append({
            "n": n,
            "k": k,
            "baseline_nodes": baseline["nodes_expanded"],
            "tight_nodes": tight["nodes_expanded"],
            "baseline_runtime_sec": baseline["runtime_sec"],
            "tight_runtime_sec": tight["runtime_sec"],
        })
    return out
