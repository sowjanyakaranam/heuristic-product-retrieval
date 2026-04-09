from __future__ import annotations
import matplotlib.pyplot as plt

def plot_algorithm_comparison(labels, baseline_vals, tight_vals, ylabel, title, output_path=None):
    x = range(len(labels))
    width = 0.35
    plt.figure(figsize=(8, 4.5))
    plt.bar([i - width / 2 for i in x], baseline_vals, width=width, label="Baseline A*")
    plt.bar([i + width / 2 for i in x], tight_vals, width=width, label="A* + Tight Heuristic")
    plt.xticks(list(x), labels)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.show()

def plot_scaling(ns, baseline_vals, tight_vals, ylabel, title, output_path=None):
    plt.figure(figsize=(8, 4.5))
    plt.plot(ns, baseline_vals, marker="o", label="Baseline A*")
    plt.plot(ns, tight_vals, marker="o", label="A* + Tight Heuristic")
    plt.xlabel("Candidate pool size N")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.show()
