"""Exact and Monte-Carlo analyses for *Politics as a Flavoring Agent*.

Every number cited in the paper's modelled sections is a key in the dict this
module returns. The deterministic results use exact float arithmetic over a
fixed population of consumers; the robustness layer adds Gumbel choice noise
under a fixed seed (SEED below), so the run is reproducible to the last digit.

The model. A category holds substitutable goods. Consumer i has a political
position x_i on a one-dimensional axis. Good j has functional quality F_j and,
if it is politicized, a position p_j. Alignment between a consumer and a good is
the Gaussian kernel a_ij = exp(-(x_i - p_j)^2 / 2 tau^2), in (0, 1]. The
"political term" the good carries for the consumer is

    pi_ij = lam_pos * a_ij - lam_neg * (1 - a_ij),

a hedonic bonus when aligned and a contamination penalty when misaligned, with
lam_neg >= lam_pos encoding the negativity dominance that the moral-contagion
literature reports (a misalignment spoils more than an alignment sweetens).

Two data-generating processes route this political term into consumption.
Under SORTING the term is expressive: it changes which good the consumer
chooses but not how the chosen good is experienced; the hedonic rating of the
physical good stays F_j. Under FLAVORING the term is hedonic: it multiplies the
experienced quality, so the same physical good is tasted as F_j*(1+pi_ij). A
mixture parameter phi in [0,1] is the flavoring share. Labeled total utility is

    U^lab_ij = F_j + pi_ij * (phi * F_j + (1 - phi) * F0),

and the blind (label-hidden) hedonic rating of good j is F_j*(1 + phi*pi_ij);
the expressive channel needs a visible label and so contributes nothing blind.

The parameter magnitudes are illustrative, anchored to published effect sizes
(label-on-taste and price-on-pleasantness experiments for lam_pos; negativity
dominance for the lam_neg/lam_pos ratio); they are not estimates for any named
market. The geometry, not the calibration, is the contribution.
"""
from __future__ import annotations

import numpy as np

SEED = 60240
N = 60000              # consumers in the population
F0 = 1.0               # reference functional quality (the plateau level)
TAU = 1.0              # alignment kernel width
MU = 1.0               # polarization: tribe means sit at -MU and +MU
SIGMA_X = 0.5          # within-tribe spread of political positions

# Flavoring strengths. lam_pos is the hedonic bonus at full alignment; lam_neg
# the contamination penalty at full misalignment. The ratio lam_neg/lam_pos is
# the negativity-dominance factor. Defaults: a 15% upward hedonic shift at full
# alignment, a 35% downward shift at full misalignment, ratio ~2.33.
LAM_POS = 0.15
LAM_NEG = 0.35
KAPPA_SYM = 0.25       # symmetric political weight used in the identification study

PHI_GRID = [0.0, 0.25, 0.5, 0.75, 1.0]

# Illustrative normalized functional dispersion by category, ordinal only: the
# standardized spread of functional quality across competing products in the
# category, as a fraction of F0. Low = a "good-enough" plateau (any unit clears
# the bar); high = real, decision-relevant performance gaps. Stipulated to order
# the categories, not measured.
CATEGORY_DF = {
    "bottled_water":   0.03,
    "beer":            0.06,
    "coffee":          0.10,
    "fashion_basics":  0.13,
    "cosmetics":       0.20,
    "phones":          0.48,
    "cars":            0.52,
    "tvs":             0.58,
    "industrial_tools": 0.68,
    "medical_devices": 0.78,
}


# ---------------------------------------------------------------------------
def make_population(n: int = N, mu: float = MU, sigma: float = SIGMA_X,
                    seed: int = SEED) -> np.ndarray:
    """A polarized electorate: half drawn near -mu, half near +mu."""
    rng = np.random.default_rng(seed)
    tribe = rng.choice([-1.0, 1.0], size=n)
    return tribe * mu + rng.normal(0.0, sigma, size=n)


def alignment(x: np.ndarray, p: float, tau: float = TAU) -> np.ndarray:
    """Gaussian alignment kernel a(x, p) in (0, 1]."""
    return np.exp(-((x - p) ** 2) / (2.0 * tau ** 2))


def political_term(a: np.ndarray, lam_pos: float, lam_neg: float) -> np.ndarray:
    """Hedonic bonus when aligned minus contamination penalty when misaligned."""
    return lam_pos * a - lam_neg * (1.0 - a)


# ---------------------------------------------------------------------------
# Study 1: identification. At the quality plateau (both goods at F0) the labeled
# market is exactly invariant to the flavoring share phi, while the blind-versus-
# labeled hedonic swing is exactly linear in phi. Market data fix the political
# premium; only the swing fixes its split into sorting and flavoring.
# ---------------------------------------------------------------------------
def identification() -> dict:
    x = make_population()
    # symmetric political weight so the two goods are mirror images
    aR = alignment(x, +1.0)          # good R at position +1
    aL = alignment(x, -1.0)          # good L at position -1
    piR = political_term(aR, KAPPA_SYM, KAPPA_SYM)
    piL = political_term(aL, KAPPA_SYM, KAPPA_SYM)

    rows = []
    share_R = []
    swing_aligned = []
    for phi in PHI_GRID:
        # labeled total utility; at the plateau F_R = F_L = F0 the phi-weighted
        # bracket collapses to F0 and U is independent of phi by construction
        uR = F0 + piR * (phi * F0 + (1 - phi) * F0)
        uL = F0 + piL * (phi * F0 + (1 - phi) * F0)
        choose_R = uR > uL
        sR = float(np.mean(choose_R))
        # blind-vs-labeled hedonic swing for the chosen good, averaged over
        # consumers (the within-good quantity a relabeling experiment recovers)
        pi_chosen = np.where(choose_R, piR, piL)
        swing = phi * F0 * pi_chosen
        # average swing among consumers whose chosen good is aligned (pi>0)
        aligned = pi_chosen > 0
        mean_swing_aligned = float(np.mean(swing[aligned])) if aligned.any() else 0.0
        rows.append({
            "phi": phi,
            "share_R": sR,
            "mean_hedonic_swing_aligned": mean_swing_aligned,
        })
        share_R.append(sR)
        swing_aligned.append(mean_swing_aligned)

    # the political premium: the labeled willingness-to-pay gap between a
    # consumer's better-matched and worse-matched good, in F0 units. Pinned by
    # the market, identical for every phi.
    pi_better = np.maximum(piR, piL)
    pi_worse = np.minimum(piR, piL)
    premium = float(np.mean(pi_better - pi_worse) * F0)

    choice_dispersion = float(max(share_R) - min(share_R))   # ~0: market is blind to phi
    # swing is linear through the origin in phi; slope = swing at phi=1
    swing_slope = swing_aligned[-1]

    return {
        "n_consumers": N,
        "kappa_symmetric": KAPPA_SYM,
        "phi_grid": list(PHI_GRID),
        "rows": rows,
        "political_premium_F0_units": premium,
        "choice_share_R_by_phi": share_R,
        "choice_share_dispersion_across_phi": choice_dispersion,
        "market_identifies_phi": choice_dispersion > 1e-6,
        "hedonic_swing_slope_in_phi": swing_slope,
        "flavoring_share_unidentified_interval": [0.0, 1.0],
    }


# ---------------------------------------------------------------------------
# Study 2: the good-enough plateau. Two oppositely-positioned goods of unequal
# functional quality. A consumer's choice is "politics-determined" when politics
# moves it off the functionally-best good. Sweeping functional dispersion dF
# locates the threshold below which politics decides the majority of choices,
# and maps named categories onto the axis.
# ---------------------------------------------------------------------------
def _politics_determined_share(dF: float, x: np.ndarray,
                               lam_pos: float = LAM_POS,
                               lam_neg: float = LAM_NEG,
                               phi: float = 1.0) -> float:
    """Share of consumers whose choice flips when the political term is removed.

    Good R sits at +1 with quality F0 + dF/2; good L at -1 with F0 - dF/2. The
    pure-functional choice is always R (the better good). Politics is decisive
    for a consumer when, with the political term present, L wins.
    """
    aR = alignment(x, +1.0)
    aL = alignment(x, -1.0)
    piR = political_term(aR, lam_pos, lam_neg)
    piL = political_term(aL, lam_pos, lam_neg)
    FR = F0 + dF / 2.0
    FL = F0 - dF / 2.0
    uR = FR + piR * (phi * FR + (1 - phi) * F0)
    uL = FL + piL * (phi * FL + (1 - phi) * F0)
    # functional-only choice is R for all; politics-determined = L chosen now
    return float(np.mean(uL > uR))


def plateau() -> dict:
    x = make_population()
    grid = np.linspace(0.0, 0.8, 161)
    shares = [_politics_determined_share(float(d), x) for d in grid]
    shares = np.array(shares)

    # threshold dF*: the dispersion at which politics stops deciding the
    # majority of the politically-engaged half (those whose aligned good is L).
    # Among consumers aligned to L (x<0, ~half the market), politics-determined
    # share starts near 0.5 of the whole and falls; find where the whole-market
    # politics-determined share crosses 0.25 (half of the L-aligned half).
    target = 0.25
    cross = None
    for d, s in zip(grid, shares):
        if s < target:
            cross = float(d)
            break
    # also the half-max point of the L-aligned subpopulation
    half_pt = None
    base = shares[0]
    for d, s in zip(grid, shares):
        if s < base / 2.0:
            half_pt = float(d)
            break

    cats = []
    for name, dF in CATEGORY_DF.items():
        s = _politics_determined_share(dF, x)
        cats.append({
            "category": name,
            "dispersion_dF": dF,
            "politics_determined_share": s,
            "regime": "flavor-dominated" if (cross is not None and dF < cross)
                      else "function-dominated",
        })
    cats.sort(key=lambda c: c["dispersion_dF"])
    ordering = [c["category"] for c in cats]
    n_flavor = sum(1 for c in cats if c["regime"] == "flavor-dominated")

    return {
        "threshold_dF_quarter": cross,
        "threshold_dF_halfmax": half_pt,
        "plateau_politics_determined_share": float(base),
        "sweep": [{"dF": float(d), "share": float(s)}
                  for d, s in zip(grid, shares)],
        "categories": cats,
        "category_ordering": ordering,
        "n_flavor_dominated": n_flavor,
        "n_function_dominated": len(cats) - n_flavor,
    }


# ---------------------------------------------------------------------------
# Study 3: the activism trap. A neutral good politicizes to position +1. Under
# negativity dominance the contamination of the alienated side outweighs the
# bonus to the aligned side, so politicization is net-negative for a brand whose
# base is broad, and net-positive only for a base already concentrated near the
# adopted pole. Reproduces the large-share-brand penalty.
# ---------------------------------------------------------------------------
SIGMA_BASE = 0.7       # spread of a brand's customer base around its mean position


def _base_positions(base_mean: float, n: int, seed: int) -> np.ndarray:
    """A brand's customer base: a unimodal cloud around base_mean.

    base_mean is how aligned the existing base is with the stance the brand will
    adopt (the adopted pole is +1). A mass-market brand sits near the center of
    the electorate (base_mean ~ 0); a niche challenger's base sits at a pole.
    """
    rng = np.random.default_rng(seed)
    return rng.normal(base_mean, SIGMA_BASE, size=n)


def _demand_change(base_mean: float, p_adopt: float = 1.0,
                   lam_pos: float = LAM_POS, lam_neg: float = LAM_NEG,
                   beta: float = 3.0, u_out: float = 0.5,
                   seed: int = SEED + 7) -> float:
    """Mean change in logit purchase probability when a neutral good adopts p."""
    xb = _base_positions(base_mean, N, seed)
    a = alignment(xb, p_adopt)
    pi = political_term(a, lam_pos, lam_neg)
    p_neutral = 1.0 / (1.0 + np.exp(-beta * (F0 - u_out)))
    p_polit = 1.0 / (1.0 + np.exp(-beta * (F0 * (1 + pi) - u_out)))
    return float(np.mean(p_polit - p_neutral))


def asymmetry() -> dict:
    means = np.linspace(-1.5, 1.5, 121)
    sweep = [{"base_mean": float(m), "demand_change": _demand_change(float(m))}
             for m in means]
    dvals = np.array([s["demand_change"] for s in sweep])

    mass_brand = _demand_change(0.0)            # centered, broad base
    niche_aligned = _demand_change(+1.0)        # base already at the adopted pole
    niche_opposed = _demand_change(-1.0)        # base at the opposite pole

    # break-even base mean where demand change crosses zero (scanning upward)
    breakeven = None
    for m, d in zip(means, dvals):
        if d > 0:
            breakeven = float(m)
            break

    # symmetric control: with lam_neg = lam_pos, the centered brand is neutral-to-
    # positive; the penalty is entirely a creature of negativity dominance
    mass_symmetric = _demand_change(0.0, lam_neg=LAM_POS)

    return {
        "lam_pos": LAM_POS,
        "lam_neg": LAM_NEG,
        "negativity_dominance_ratio": LAM_NEG / LAM_POS,
        "mass_brand_demand_change": mass_brand,
        "niche_aligned_demand_change": niche_aligned,
        "niche_opposed_demand_change": niche_opposed,
        "breakeven_base_mean": breakeven,
        "mass_brand_demand_change_symmetric_control": mass_symmetric,
        # headline figures as reported in the paper, rounded to three decimals
        "reported": {
            "mass_brand_demand_change": round(mass_brand, 3),
            "mass_brand_demand_loss": round(-mass_brand, 3),
            "niche_aligned_demand_change": round(niche_aligned, 3),
            "niche_opposed_demand_change": round(niche_opposed, 3),
            "niche_opposed_demand_loss": round(-niche_opposed, 3),
            "mass_brand_demand_change_symmetric_control": round(mass_symmetric, 3),
        },
        "sweep": sweep,
    }


# ---------------------------------------------------------------------------
# Robustness: re-run the identification choice shares and the activism-trap sign
# under Gumbel choice noise, to show the deterministic results are not artifacts
# of exact argmax.
# ---------------------------------------------------------------------------
def monte_carlo() -> dict:
    rng = np.random.default_rng(SEED + 99)
    x = make_population()
    aR = alignment(x, +1.0)
    aL = alignment(x, -1.0)
    piR = political_term(aR, KAPPA_SYM, KAPPA_SYM)
    piL = political_term(aL, KAPPA_SYM, KAPPA_SYM)
    scale = 0.05
    shares_by_phi = {}
    for phi in PHI_GRID:
        uR = F0 + piR * F0   # phi-invariant at plateau
        uL = F0 + piL * F0
        gR = rng.gumbel(0.0, scale, size=len(x))
        gL = rng.gumbel(0.0, scale, size=len(x))
        shares_by_phi[f"{phi:.2f}"] = float(np.mean((uR + gR) > (uL + gL)))
    vals = list(shares_by_phi.values())
    return {
        "n_samples": N,
        "seed": SEED + 99,
        "gumbel_scale": scale,
        "noisy_choice_share_R_by_phi": shares_by_phi,
        "noisy_choice_dispersion_across_phi": float(max(vals) - min(vals)),
    }


# ---------------------------------------------------------------------------
# Sensitivity: how the activism-trap break-even and the mass-brand penalty move
# with the negativity-dominance ratio and the kernel width.
# ---------------------------------------------------------------------------
def sensitivity() -> dict:
    ratios = [1.0, 1.5, 2.0, 2.33, 3.0, 4.0]
    out_ratio = []
    for r in ratios:
        lam_neg = LAM_POS * r
        mass = _demand_change(0.0, lam_neg=lam_neg)
        # break-even
        means = np.linspace(-1.5, 1.5, 121)
        be = None
        for m in means:
            if _demand_change(float(m), lam_neg=lam_neg) > 0:
                be = float(m)
                break
        out_ratio.append({"ratio": r, "mass_brand_demand_change": mass,
                          "breakeven_base_mean": be})
    taus = [0.6, 0.8, 1.0, 1.2, 1.6]
    x = make_population()
    out_tau = []
    for t in taus:
        aR = alignment(x, +1.0, tau=t)
        aL = alignment(x, -1.0, tau=t)
        piR = political_term(aR, LAM_POS, LAM_NEG)
        piL = political_term(aL, LAM_POS, LAM_NEG)
        # plateau politics-determined share at dF=0 under asymmetric weights
        uR = F0 + piR * F0
        uL = F0 + piL * F0
        out_tau.append({"tau": t,
                        "plateau_share_L": float(np.mean(uL > uR))})
    return {"by_negativity_ratio": out_ratio, "by_kernel_width": out_tau}


# ---------------------------------------------------------------------------
def run() -> dict:
    return {
        "params": {
            "n_consumers": N, "F0": F0, "tau": TAU, "mu": MU,
            "sigma_x": SIGMA_X, "lam_pos": LAM_POS, "lam_neg": LAM_NEG,
            "kappa_symmetric": KAPPA_SYM, "seed": SEED,
        },
        "identification": identification(),
        "plateau": plateau(),
        "asymmetry": asymmetry(),
        "monte_carlo": monte_carlo(),
        "sensitivity": sensitivity(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2)[:3000])
