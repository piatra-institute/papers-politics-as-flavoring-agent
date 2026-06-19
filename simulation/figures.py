"""Figures for *Politics as a Flavoring Agent*. Each reads the results dict and
writes one PNG. No new computation here; every plotted value is a results key.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_identification(results: dict, path: str) -> None:
    ident = results["identification"]
    phis = ident["phi_grid"]
    shares = ident["choice_share_R_by_phi"]
    swings = [r["mean_hedonic_swing_aligned"] for r in ident["rows"]]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.6))
    ax1.plot(phis, shares, "o-", color="#444")
    ax1.set_ylim(0, 1)
    ax1.set_xlabel("flavoring share $\\phi$")
    ax1.set_ylabel("market share of good R")
    ax1.set_title("Market is blind to $\\phi$")
    ax1.axhline(shares[0], ls=":", color="#aaa")

    ax2.plot(phis, swings, "o-", color="#b2182b")
    ax2.set_xlabel("flavoring share $\\phi$")
    ax2.set_ylabel("blind$-$labeled hedonic swing")
    ax2.set_title("Only the lab swing identifies $\\phi$")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_plateau(results: dict, path: str) -> None:
    pl = results["plateau"]
    xs = [s["dF"] for s in pl["sweep"]]
    ys = [s["share"] for s in pl["sweep"]]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(xs, ys, color="#2166ac")
    if pl["threshold_dF_quarter"] is not None:
        ax.axvline(pl["threshold_dF_quarter"], ls="--", color="#777",
                   label=f"threshold $\\Delta F^*$ = {pl['threshold_dF_quarter']:.3f}")
    for c in pl["categories"]:
        ax.scatter([c["dispersion_dF"]], [c["politics_determined_share"]],
                   color="#b2182b" if c["regime"] == "flavor-dominated" else "#1a9850",
                   zorder=5)
        ax.annotate(c["category"].replace("_", " "),
                    (c["dispersion_dF"], c["politics_determined_share"]),
                    fontsize=7, rotation=30, ha="left", va="bottom")
    ax.set_xlabel("functional dispersion $\\Delta F$ (fraction of $F_0$)")
    ax.set_ylabel("politics-determined choice share")
    ax.set_title("The good-enough plateau")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_asymmetry(results: dict, path: str) -> None:
    asy = results["asymmetry"]
    xs = [s["base_mean"] for s in asy["sweep"]]
    ys = [s["demand_change"] for s in asy["sweep"]]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(xs, ys, color="#444")
    ax.axhline(0, ls=":", color="#aaa")
    if asy["breakeven_base_mean"] is not None:
        ax.axvline(asy["breakeven_base_mean"], ls="--", color="#b2182b",
                   label=f"break-even base = {asy['breakeven_base_mean']:.2f}")
    ax.scatter([0.0], [asy["mass_brand_demand_change"]], color="#b2182b",
               zorder=5, label="mass (centered) brand")
    ax.set_xlabel("brand base mean position (adopted pole at $+1$)")
    ax.set_ylabel("change in demand on politicization")
    ax.set_title("The activism trap")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
