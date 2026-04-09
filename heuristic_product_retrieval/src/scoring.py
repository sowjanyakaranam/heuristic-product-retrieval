from __future__ import annotations
from typing import Sequence

def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    num = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(y * y for y in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return num / (norm_a * norm_b)

def relevance(product_embedding, query_embedding) -> float:
    return cosine_similarity(product_embedding, query_embedding)

def redundancy(selected_products) -> float:
    total = 0.0
    for i in range(len(selected_products)):
        for j in range(i + 1, len(selected_products)):
            total += cosine_similarity(selected_products[i].embedding, selected_products[j].embedding)
    return total

def objective(selected_products, query_embedding, lam: float = 0.30) -> float:
    rel = sum(relevance(p.embedding, query_embedding) for p in selected_products)
    red = redundancy(selected_products)
    return rel - lam * red
