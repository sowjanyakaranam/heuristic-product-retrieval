# 🚀 Heuristic Product Retrieval — Final Project

This project implements a **heuristic search-based approach for query-based product retrieval in e-commerce**, developed for **CS 57200 – Heuristic Problem Solving (Track B)**.

Instead of ranking products independently, this system selects a **top-K subset of products** that is:

* **highly relevant** to a user query
* **diverse** (non-redundant)

---

# 🎯 Problem Overview

Traditional retrieval systems:

* rank items independently
* often return **redundant results**

This project reformulates retrieval as a **combinatorial subset selection problem**, optimizing:

* relevance to query
* diversity within results

---

# 🧠 Approach

We model the problem as a **search problem** and solve it using:

### ✅ Baseline

* A* search for **exact optimization**

### ⚡ Enhancements

1. **Tighter Heuristic**

   * Better estimate of remaining score
   * Reduces node expansions

2. **Weighted A***

   * Trades optimality for speed
   * Faster convergence in practice

3. **Top-M Filtering (Most impactful)**

   * Reduces candidate set before search
   * Dramatically improves scalability

---

# 📂 Project Structure

```text
heuristic_product_retrieval/
├── data/
│   ├── sample_products.csv
│   └── real_products.csv
├── notebooks/
│   └── m2_experiments.ipynb
├── results/
│   ├── figures/
│   │   ├── weighted_astar_tradeoff.png
│   │   ├── real_vs_synthetic_nodes.png
│   │   └── real_vs_synthetic_runtime.png
│   └── tables/
│       ├── exp5_topm.csv
│       ├── exp6_real_amazon_case_study.csv
│       └── exp6_selected_real_products.csv
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

---

# ⚙️ Setup (Colab / Local)

## Install dependencies

```python
!pip install -r requirements.txt
```

## Set working directory

```python
import os, sys
ROOT = '/content/heuristic-product-retrieval'
os.chdir(ROOT)
sys.path.append(os.path.join(ROOT, 'src'))
```

## Run experiments

Open:

```text
notebooks/m2_experiments.ipynb
```

Run all cells.

---

# 📊 Experiments Conducted

### Synthetic Experiments

1. ✅ Correctness validation (vs brute-force)
2. ✅ Baseline vs tighter heuristic
3. ✅ Scaling with candidate size
4. ✅ Sensitivity to K
5. ✅ Weighted A* tradeoff
6. ✅ Top-M filtering impact

---

### 🌍 Real Data Experiment

**Dataset:**

* Amazon Product Dataset (Kaggle)

**Pipeline:**

1. Product text → embeddings (Sentence-BERT)
2. Query embedding
3. Top-M filtering
4. A* subset selection

**Outputs:**

* selected product subset
* runtime
* nodes expanded

---

# 📈 Key Results

* **Tighter heuristic**

  * ↓ nodes expanded
  * faster search

* **Top-M filtering**

  * 🚀 largest speed improvement
  * preserves solution quality

* **Weighted A***

  * modest speed gains

* **Real data**

  * pipeline works end-to-end
  * produces meaningful results

---

# 🧪 Example Query

```text
"healthy protein snacks"
```

Output:

* diverse product subset
* avoids redundant items

---

# 📦 Data Notes

* `sample_products.csv` → synthetic data
* `real_products.csv` → processed Amazon dataset

⚠️ Full raw dataset not included due to size constraints.

---

# 📚 Dependencies

* Python 3.x
* numpy
* pandas
* matplotlib
* sentence-transformers

Install via:

```bash
pip install -r requirements.txt
```

---

# 🔍 Limitations

* A* is exponential in worst case
* real dataset scaled via Top-M filtering
* redundancy model is simplified

---

# 🚀 Future Work

* larger-scale real datasets
* advanced heuristics (redundancy-aware)
* approximate / real-time search
* personalization

---

# 👩‍💻 Author

Sowjanya Karanam
CS 57200 – Heuristic Problem Solving

---

# 🧾 Summary

This project demonstrates that:

✔ subset selection improves retrieval quality
✔ heuristic search enables exact optimization
✔ filtering makes the approach scalable
✔ system works on real-world data

---

# 🔥 Final Note

> This project bridges theoretical heuristic search with practical e-commerce retrieval by combining exact optimization with scalable approximations.

---

If you want one last improvement:
👉 I can add **badges, visuals, and demo GIFs** to make your GitHub stand out even more.
