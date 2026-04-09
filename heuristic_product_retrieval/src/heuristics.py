from __future__ import annotations
from scoring import relevance

def baseline_heuristic(selected, remaining, query_embedding, k: int) -> float:
    remaining_slots = k - len(selected)
    if remaining_slots <= 0 or not remaining:
        return 0.0
    best_rel = max(relevance(p.embedding, query_embedding) for p in remaining)
    return -remaining_slots * best_rel

def tight_heuristic(selected, remaining, query_embedding, k: int) -> float:
    remaining_slots = k - len(selected)
    if remaining_slots <= 0:
        return 0.0
    scores = sorted((relevance(p.embedding, query_embedding) for p in remaining), reverse=True)
    return -sum(scores[:remaining_slots])
