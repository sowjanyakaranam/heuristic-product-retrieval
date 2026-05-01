# Heuristic Product Retrieval M2 Starter

This is a Colab-friendly starter project for **CS 57200 – Heuristic Problem Solving (Track B)**.

It includes:
- a **correct baseline A\*** solver for top-K product subset retrieval
- one **integrated enhancement**: a tighter admissible heuristic
- a **brute-force validator** for tiny cases
- starter experiment utilities and plotting code

## Structure

```text
heuristic_product_retrieval_m2_starter/
├── data/
│   └── sample_products.csv
├── notebooks/
│   └── m2_experiments.ipynb
├── results/
│   ├── figures/
│   └── tables/
├── src/
│   ├── data_utils.py
│   ├── scoring.py
│   ├── astar_baseline.py
│   ├── heuristics.py
│   ├── experiments.py
│   └── viz.py
├── requirements.txt
└── README.md
```

## Colab setup

Clone your repo in Colab, then run:

```python
!pip install -r requirements.txt
import os, sys
ROOT = '/content/heuristic_product_retrieval_m2_starter'
os.chdir(ROOT)
sys.path.append(os.path.join(ROOT, 'src'))
```

Open `notebooks/m2_experiments.ipynb` and run it top to bottom.

## Baseline and enhancement

### Baseline
Standard A* with heuristic:
h(S) = - (K - |S|) * max relevance among remaining products

### Enhancement 1
Tighter admissible heuristic:
h_tight(S) = - sum of top (K - |S|) remaining relevance scores

## M2 experiments scaffolded

1. Baseline correctness validation
2. Baseline vs enhancement
3. Scaling study

## Replace next
- `data/sample_products.csv` with your cleaned category data
- synthetic embeddings with Sentence-BERT embeddings
- starter categories with your real categories
