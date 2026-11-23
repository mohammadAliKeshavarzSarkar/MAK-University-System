# MAK Data Visualization — Official Source Catalog

**Checked:** 2026-11-23. These are software documentation and examples; they do **not** provide evidence for user-specific research results.

| Tool | Official link | Documented strengths | Important production limits |
| --- | --- | --- | --- |
| **Vega-Altair** | https://altair-viz.github.io/ | Python declarative charts built on Vega-Lite; straightforward visual encodings and examples | Static export docs: https://altair-viz.github.io/user_guide/saving_charts.html ; PNG/SVG/PDF can need `vl-convert-python`. Do not imply installed by default. |
| **Matplotlib** | https://matplotlib.org/stable/gallery/index.html | Broad Python gallery of scientific/statistical plots and configurable static figures | `savefig` supports PNG, SVG and PDF: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html . Exporting SVG does **not** create a native PowerPoint chart. |
| **Plotly Python** | https://plotly.com/python/ | Interactive Python plots with hover, zoom and static/HTML output | https://plotly.com/python/static-image-export/ : PNG/SVG/PDF may need Kaleido v1 + installed Chrome/Chromium; HTML is an interactive browser artifact, not a PPTX animation. |
| **Apache ECharts** | https://echarts.apache.org/en/index.html | Open-source JavaScript browser charts, Canvas/SVG, dashboard components and datasets | Main site is JavaScript-rendered; avoid unsupported claims about detailed APIs without reopening reference docs. |
| **Observable Plot** | https://observablehq.github.io/plot/ | JavaScript exploratory charts using marks, scales, transforms, facets, projections | Browser-based; must explicitly export/verify standalone visualizations for slides. |

## FRAME guidance and review links

- [Data Visualization skill](SKILL.md)
- [Example 01: Synthetic Learning Curves](examples/README.md)
- [Existing FRAME presentation skill](../frame-presentations/SKILL.md)
- [Academic quality](../../standards/academic-quality.md)
- [Source integrity](../../standards/source-integrity.md)

## Execution evidence and limitations from the first exercise

In the current Python runtime for Example 01: **Matplotlib 3.10.8** generated PNG and SVG successfully; **Plotly 6.5.2** generated a standalone HTML and figure JSON, and its HTML rendered in Chromium. The **Kaleido** static-export package and **Altair** package were not available, and attempts to install additional Python packages failed due to network name resolution. Therefore, the Altair path has **not** been execution-tested here and a Plotly native image export was **not** verified. Browser screenshots are not a substitute for Kaleido or vector export.

The example dataset has twelve fixed illustrative epochs; it is **not real training data**. The minimum validation loss is 0.49 at epoch 7. The result is numerical inspection of a constructed example, not a claim about a trained model.

## Scope boundary

These sources are approved **learning/selection references**, not mandatory dependencies. Choose the correct library for each user task and verify the installed version before relying on current behavior. We link documentation instead of copying third-party galleries, copyrighted plots or large package distributions to our public repository.
