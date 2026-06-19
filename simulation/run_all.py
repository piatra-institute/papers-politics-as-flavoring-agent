"""Orchestrator: reproduces every modelled number in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in
the modelled sections is a key in the JSON file. The deterministic results are
exact over the fixed population; the robustness layer is seeded (analyses.SEED),
so the run is reproducible to the last digit.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_identification, plot_plateau, plot_asymmetry

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_identification(results, str(OUT / "figures" / "identification.png"))
    plot_plateau(results, str(OUT / "figures" / "plateau.png"))
    plot_asymmetry(results, str(OUT / "figures" / "asymmetry.png"))

    ident = results["identification"]
    pl = results["plateau"]
    asy = results["asymmetry"]
    mc = results["monte_carlo"]
    print("IDENTIFICATION")
    print(f"  political premium (F0 units)        : {ident['political_premium_F0_units']:.4f}")
    print(f"  choice-share dispersion across phi  : {ident['choice_share_dispersion_across_phi']:.2e}")
    print(f"  market identifies phi               : {ident['market_identifies_phi']}")
    print(f"  hedonic swing slope in phi          : {ident['hedonic_swing_slope_in_phi']:.4f}")
    print(f"  noisy choice dispersion (control)   : {mc['noisy_choice_dispersion_across_phi']:.2e}")
    print("PLATEAU")
    print(f"  threshold dF* (quarter)             : {pl['threshold_dF_quarter']}")
    print(f"  flavor-dominated categories         : {pl['n_flavor_dominated']}/"
          f"{pl['n_flavor_dominated'] + pl['n_function_dominated']}")
    for c in pl["categories"]:
        print(f"    {c['category']:17s} dF={c['dispersion_dF']:.2f} "
              f"share={c['politics_determined_share']:.3f} {c['regime']}")
    print("ASYMMETRY")
    print(f"  negativity-dominance ratio          : {asy['negativity_dominance_ratio']:.2f}")
    print(f"  mass (centered) brand demand change : {asy['mass_brand_demand_change']:.4f}")
    print(f"  mass brand, symmetric control       : {asy['mass_brand_demand_change_symmetric_control']:.4f}")
    print(f"  niche aligned demand change         : {asy['niche_aligned_demand_change']:.4f}")
    print(f"  break-even base mean                : {asy['breakeven_base_mean']}")


if __name__ == "__main__":
    main()
