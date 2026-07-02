# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-06-19 — Initial implementation from seed chats
Scope: full paper built from the three seed chats (chat-initial, chat, chat2) through the PIATRA pipeline.
Changes:
  - Extracted the sharp computable contribution from the seed's loose `Value = F + P + C + S + M + N - K` sketch: the sorting-versus-flavoring identification problem. Politics differentiates a converged market through two channels that are observationally equivalent on market data; only a blind-versus-labeled relabeling experiment separates them.
  - Built `simulation/` (numpy + matplotlib, uv): `analyses.py` (model + three studies + seeded robustness + sensitivity), `figures.py`, `run_all.py`. Deterministic results exact over a 60,000-consumer population; robustness layer seeded (SEED = 60240).
  - Three results, each reproducing a published empirical regularity as model output: (1) identification — at the plateau the labeled market is exactly invariant to the flavoring share phi (choice dispersion 0, premium pinned at 0.362), only the within-good hedonic swing (0 to 0.202, linear in phi) identifies it; (2) plateau threshold dF* = 0.445 partitioning ten categories 5/5 into the received susceptibility typology; (3) activism trap — negativity dominance (ratio 2.33) makes politicization net-negative for a centered mass base (-0.036) but a symmetric control gains (+0.008), break-even base mean 0.425, reproducing the large-share-brand penalty.
  - Wrote PAPER.md (8 sections, distinctive titles, limits folded into the closing section rather than a bolt-on), metadata.yaml (title, abstract, has_simulation, claims_target), brief/research/sources.
  - Bibliography of 42 entries, all engaged in-text (political consumerism, brand activism, expectation effects on taste, moral disgust/contamination, negativity dominance, identity/quality economics, distinction/status). Citations verified against memory of the real literature; 0 confabulated (refs MISSING = 0).
Verification:
  - voice: 0 errors, 7 review-candidate warns (negate-pivot / inline-contrastive, all genuine contrasts); advisories thinned (exactly 8 -> 2, pet-vocabulary removed, spelled-quantity removed).
  - refs: 0 missing, 0 unused (42 in-text keys, 42 bib entries).
  - claims: 25 prose decimals, 0 without a matching results.json value (added rounded headline keys so the reported 0.036 audits).
  - build: 14 pages, 0 missing-character warnings.
  - check => PASS

---

## 2026-07-02 — reform pass (de-template)

Corpus reform, structural (the identification result and the ordinal-stipulation caveats were already presented honestly; §4 deliberately derives the plateau bracket-collapse as the central result, §8 already concedes the dispersions are ordinal).

- paper/PAPER.md abstract: replaced the twin boilerplate closer "It does not certify that any named market is, and the closing section is precise about the difference" (shared with two other June papers) with a distinct ending stating the single discipline running through the three results.
- paper/PAPER.md §8: retitled "What the Construct Licenses, and What It Does Not" -> "The Cover That Vagueness Gave" and softened the "Three boundaries hold the rest in place" ledger opener; ends on the beer/phone callback. No number or citation changed.
- Verify: voice 0 errors; refs 42/42, 0 missing/0 unused; claims 25/0 unmatched; check => PASS; synced.
