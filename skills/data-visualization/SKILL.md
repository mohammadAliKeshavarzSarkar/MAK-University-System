---
name: data-visualization
description: Learn, select, produce, compare and audit scientific and interactive charts for MAK/FRAME using Matplotlib, Vega-Altair, Plotly, Apache ECharts and Observable Plot. Preserve numerical accuracy, provenance, accessibility and output editability.
---

# MAK / FRAME — Data Visualization & Scientific Communication

**Status:** Working learning/production skill (2026-11-23).  
**Scope:** Research plots, AI/model analysis, scientific explanations, technical lectures, dashboards and frontend visualizations.

A repository skill must be deliberately loaded by an agent; storing it on GitHub does **not** automatically install a runtime or enable every plotting library. Read the current [five-source catalog](SOURCES.md) when claiming any library capability.

## Source and authority

1. Follow [academic quality](../../standards/academic-quality.md) and [source integrity](../../standards/source-integrity.md), including user-provided datasets and course constraints.
2. Inspect the **actual data, metadata and column meanings** before plotting. Don't silently replace a missing dataset with made-up values.
3. Treat every illustration in [the example](examples/README.md) as **synthetic** unless verified otherwise.
4. For presentation output, use the [FRAME production skill](../frame-presentations/SKILL.md) and [guidebook](../../design/frame-guidebook.md).
5. Do not confuse a gallery example, library marketing page or illustrative chart with validated research evidence.

## Tool selection — choose by task, not popularity

| Library | First use case | Output caution |
| --- | --- | --- |
| **Matplotlib (Python)** | Controlled static scientific figures, research charts, classroom graphics, PDF/SVG/PNG export | Resulting SVG/PNG is artwork, not a native editable PowerPoint chart |
| **Vega-Altair (Python)** | Fast declarative encoding, exploratory comparisons, clear statistical relationships using Vega-Lite | PNG/SVG/PDF saving may need **vl-convert**; validate environment and output |
| **Plotly Python** | Browser-based interaction, tooltips, zooming, exploratory model explanations, dashboards | Interactive HTML does not stay interactive in a PowerPoint image; static export needs **Kaleido** and often Chrome/Chromium |
| **Apache ECharts (JavaScript)** | Web applications and sophisticated dashboard interactions; Canvas/SVG renderer | Browser/chart application, not a Python library or native PowerPoint chart |
| **Observable Plot (JavaScript)** | Concise exploratory plots, layered marks and small multiples in web reports | Browser-generated visualizations may require export or a screenshot for slide use |

**Working default:** Start with Matplotlib for reproducible static scientific figures in FRAME, **unless** another library better serves the deliverable. Use Altair/Plotly for exploration; ECharts/Observable Plot for web products. Do not require all five for one project.

## Seven-step workflow

1. **Define the question.** State what audience needs to compare or infer; identify variables, categories, units, denominator, time range and target medium.
2. **Audit the source.** Identify origin, collection dates (when relevant), units, missing values, filters, duplicates, distributions, and aggregation. Verify types and derived measures. Clearly label synthetic, simulated and measured data.
3. **Choose the visual encoding.** Line for ordered change; points for paired quantities; bars for category magnitudes; histogram/distribution for sample shape; confusion matrix/heatmap for structured values; uncertainty bands only with actual lower/upper inputs. Chart type must support the claim.
4. **Build reproducibly.** Keep original data, transformation steps, fixed seeds when randomness is used, relevant dependencies and meaningful figure labels separate from final exports.
5. **Apply MAK identity cautiously.** Paper `#F5F3EE`, Ink `#161616`, Signal `#E64B3C` are available visual defaults. Don't force red where it implies danger or classification without justification. Use Inter for Latin text; Persian typeface and direction remain open. Red/black series need markers, dashes or direct labels as well as color.
6. **Export to the actual target.** For university slides use a high-resolution PNG/SVG/PDF figure **or** a native PowerPoint chart if chart-data editability is required. For interactive teaching, deliver browser HTML separately. Inspect actual render, dimensions, typography and chart legends.
7. **Review meaning.** Independently recalculate highlights, percentages, class totals, axis ranges and annotations. Give source/assumptions; explain limitations and trade-offs. Never claim learning gains from a prettier chart.

## Safeguards against misleading plots

- Name both axes with **units**; explain denominator, normalization and any logarithmic scale. Never hide truncation or unequal scales.
- Start magnitude-comparison bars from an honest zero baseline unless there is a clearly stated reason not to; **line plots need not start at zero** when the scale is disclosed.
- Do not interpolate invented experimental data or imply confidence intervals without underlying sampling/uncertainty definitions.
- Explain whether observations are paired, independent, cumulative, averaged, filtered or smoothed.
- If a model's training loss declines while validation loss rises, describe the **illustrated pattern**, not a measured conclusion about a real model unless backed by actual experiment records.
- Make colorblind/accessibility distinctions with line style, symbols or labels; use meaningful textual alternatives.
- Check that small chart labels stay readable at projected size and on the final exported PDF or PPTX.
- Mark source and version of reused material, including copyright/license where relevant.

## A practical lesson

Run [Example 01 — Synthetic Learning Curves](examples/README.md). The same twelve rows are visualized in Matplotlib and Plotly; the Altair code path is included for an environment with its optional package. Training and validation losses are **invented exercise numbers**, not model results. The example has a validation minimum at epoch 7 of 0.49 illustrative units.

Hold data, x/y domains, and informational annotation constant. Compare (a) notebook implementation, (b) chart readability, (c) interaction, (d) offline export, (e) PowerPoint editability. Never confuse a browser screenshot with vector output.

## Skill outputs

For a one-off figure, return a usable chart and its source/data when asked, with a source note and short QA. For an audit, identify concrete issues and corrections. For a learning comparison, deliver a controlled experiment and an honest capabilities table. **Do not build unnecessary dashboards or create five competing artifacts when one plot suffices.**

## Promotion gate

Treat new chart styling and library preferences as working hypotheses. Promote only demonstrated, generalizable checks to FRAME standards after review. Avoid copying substantial proprietary examples from visualization galleries into this public repository.
