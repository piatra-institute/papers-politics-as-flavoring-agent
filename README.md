# politics-as-flavoring-agent

When functional quality across competing products has converged, political meaning takes over the work of differentiation, and it does so through two channels an outside observer cannot tell apart: sorting (politics changes which good is chosen, leaving its experienced quality intact) and flavoring (politics changes the experienced quality itself, so the same physical good is tasted as better when its label aligns). This paper builds the smallest model that holds both, with a mixture parameter for how much of the political premium is flavoring, and shows that at the quality plateau the labeled market is exactly invariant to that parameter: revealed preference cannot recover it, and only a blind-versus-labeled relabeling experiment can. The same plateau condition yields a category-susceptibility threshold that reproduces the received typology, and the negativity-dominance of moral contamination yields the large-share-brand penalty of corporate activism. Ships a runnable simulation whose output carries every modelled number.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build politics-as-flavoring-agent`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
