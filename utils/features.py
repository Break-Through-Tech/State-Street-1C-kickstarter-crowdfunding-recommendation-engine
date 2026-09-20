import pandas as pd
import numpy as np


def wilson(k, n, z=1.96):
    "95% Wilson score interval for k successes in n trials. Works on scalars or arrays."
    k, n = np.asarray(k, dtype=float), np.asarray(n, dtype=float)
    p = k / n
    d = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / d
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / d
    return centre - half, centre + half


def rate_table(data, by, target="target", min_n=50):
    "Success rate per group, with a Wilson CI and the gap from the overall rate."
    y = data[target]
    groups = data[by] if isinstance(by, str) else pd.Series(by, index=data.index)
    g = y.groupby(groups, observed=True).agg(n="size", successes="sum")
    g["rate"] = g["successes"] / g["n"]
    g["ci_lo"], g["ci_hi"] = wilson(g["successes"], g["n"])
    base = y.mean()
    g["vs_base"] = g["rate"] - base
    g = g[g["n"] >= min_n]
    g.attrs["base"] = base
    return g

def rate_plot(ax, table, title, labels=None, color="#2c6f52", rotate=0, base=None):
    "Bar chart of a rate_table: one bar per group, CI error bars, dashed overall-rate line."
    if base is None:
        base = table.attrs.get("base", (table["rate"] * table["n"]).sum() / table["n"].sum())
    x = np.arange(len(table))
    ax.bar(x, table["rate"], color=color, alpha=0.85)
    ax.errorbar(x, table["rate"],
                yerr=[table["rate"] - table["ci_lo"], table["ci_hi"] - table["rate"]],
                fmt="none", ecolor="k", capsize=3, lw=1)
    ax.axhline(base, color="#8a9590", ls="--", lw=1, label=f"overall {base:.1%}")
    ax.set_xticks(x)
    ax.set_xticklabels(labels if labels is not None else table.index,
                       rotation=rotate, ha="right" if rotate else "center", fontsize=8.5)
    for i, n in enumerate(table["n"]):
        ax.text(i, 0.015, f"n={n:,}", ha="center", fontsize=7, color="white", rotation=90)
    ax.set_ylim(0, 1); ax.set_ylabel("success rate"); ax.set_title(title)
    ax.legend(loc="upper right", fontsize=8)


