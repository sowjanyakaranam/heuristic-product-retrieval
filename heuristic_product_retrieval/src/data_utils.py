from __future__ import annotations
from dataclasses import dataclass
from typing import List
import csv

@dataclass(frozen=True)
class Product:
    pid: str
    title: str
    category: str
    price: float
    embedding: tuple[float, ...]

def parse_embedding(text: str) -> tuple[float, ...]:
    return tuple(float(x) for x in text.split("|"))

def load_products_csv(path: str) -> List[Product]:
    products = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(Product(
                pid=row["product_id"],
                title=row["title"],
                category=row["category"],
                price=float(row["price"]),
                embedding=parse_embedding(row["embedding"]),
            ))
    return products

def filter_by_category(products: List[Product], category: str) -> List[Product]:
    return [p for p in products if p.category == category]

def top_m_by_relevance(products, query_embedding, m, scoring_fn):
    """
    Select top-M products based on relevance to the query.
    """
    scored = sorted(
        products,
        key=lambda p: scoring_fn(p.embedding, query_embedding),
        reverse=True,
    )
    return scored[:m]