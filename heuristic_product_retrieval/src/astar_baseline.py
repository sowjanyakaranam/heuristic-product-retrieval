from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Dict, Any
import heapq
import itertools
import time
from scoring import objective

@dataclass(order=True)
class PrioritizedState:
    priority: float
    counter: int
    selected: tuple = field(compare=False)
    remaining: tuple = field(compare=False)
    g_cost: float = field(compare=False, default=0.0)

def astar_search(products, query_embedding, k: int, heuristic_fn: Callable, lam: float = 0.30) -> Dict[str, Any]:
    start_time = time.perf_counter()
    counter = 0
    nodes_expanded = 0

    start_selected = tuple()
    start_remaining = tuple(products)
    start_h = heuristic_fn(start_selected, start_remaining, query_embedding, k)
    open_heap = [PrioritizedState(start_h, counter, start_selected, start_remaining, 0.0)]

    best_g = {(tuple(), tuple(p.pid for p in start_remaining)): 0.0}

    while open_heap:
        current = heapq.heappop(open_heap)
        nodes_expanded += 1

        if len(current.selected) == k:
            result = list(current.selected)
            return {
                "selected": result,
                "objective": objective(result, query_embedding, lam=lam),
                "nodes_expanded": nodes_expanded,
                "runtime_sec": time.perf_counter() - start_time,
            }

        for idx, p in enumerate(current.remaining):
            new_selected = current.selected + (p,)
            new_remaining = current.remaining[:idx] + current.remaining[idx + 1:]
            g_cost = -objective(list(new_selected), query_embedding, lam=lam)
            h_cost = heuristic_fn(new_selected, new_remaining, query_embedding, k)
            f_cost = g_cost + h_cost
            state_key = (tuple(prod.pid for prod in new_selected), tuple(prod.pid for prod in new_remaining))

            if state_key not in best_g or g_cost < best_g[state_key]:
                best_g[state_key] = g_cost
                counter += 1
                heapq.heappush(open_heap, PrioritizedState(f_cost, counter, new_selected, new_remaining, g_cost))
    raise RuntimeError("A* failed to find a solution.")

def brute_force_search(products, query_embedding, k: int, lam: float = 0.30) -> Dict[str, Any]:
    start_time = time.perf_counter()
    best_subset = None
    best_score = float("-inf")
    checked = 0
    for combo in itertools.combinations(products, k):
        checked += 1
        score = objective(list(combo), query_embedding, lam=lam)
        if score > best_score:
            best_score = score
            best_subset = list(combo)
    return {
        "selected": best_subset,
        "objective": best_score,
        "combinations_checked": checked,
        "runtime_sec": time.perf_counter() - start_time,
    }

"""m3"""

def weighted_astar_search(
    products,
    query_embedding,
    k: int,
    heuristic_fn,
    weight: float = 1.5,
    lam: float = 0.30,
):
    """
    Weighted A* search.

    Uses:
        f(S) = g(S) + weight * h(S)

    weight > 1 makes search greedier and usually faster,
    but may sacrifice optimality.
    """
    start_time = time.perf_counter()
    counter = 0
    nodes_expanded = 0

    start_selected = tuple()
    start_remaining = tuple(products)

    start_h = heuristic_fn(start_selected, start_remaining, query_embedding, k)
    open_heap = [
        PrioritizedState(
            weight * start_h,
            counter,
            start_selected,
            start_remaining,
            0.0,
        )
    ]

    best_g = {
        (tuple(), tuple(p.pid for p in start_remaining)): 0.0
    }

    while open_heap:
        current = heapq.heappop(open_heap)
        nodes_expanded += 1

        if len(current.selected) == k:
            result = list(current.selected)
            return {
                "selected": result,
                "objective": objective(result, query_embedding, lam=lam),
                "nodes_expanded": nodes_expanded,
                "runtime_sec": time.perf_counter() - start_time,
                "weight": weight,
            }

        for idx, p in enumerate(current.remaining):
            new_selected = current.selected + (p,)
            new_remaining = current.remaining[:idx] + current.remaining[idx + 1:]

            g_cost = -objective(list(new_selected), query_embedding, lam=lam)
            h_cost = heuristic_fn(new_selected, new_remaining, query_embedding, k)
            f_cost = g_cost + weight * h_cost

            state_key = (
                tuple(prod.pid for prod in new_selected),
                tuple(prod.pid for prod in new_remaining),
            )

            if state_key not in best_g or g_cost < best_g[state_key]:
                best_g[state_key] = g_cost
                counter += 1
                heapq.heappush(
                    open_heap,
                    PrioritizedState(
                        f_cost,
                        counter,
                        new_selected,
                        new_remaining,
                        g_cost,
                    ),
                )

    raise RuntimeError("Weighted A* failed to find a solution.")