---
name: data-visualization-learning
description: Teach and revisit the 12 completed FRAME data-visualization lessons, from chart choice and uncertainty through evaluation, SHAP, counterfactual recourse, robustness, and monitoring. Use verified synthetic exercise sources, reflective questions, controlled experiments, and scientific communication checks.
---

# MAK / FRAME — Data Visualization Learning Lab

**Status:** Reusable learning facilitator, prepared from FRAME DataViz Studies 01–12 (through 2026-11-24).  
**Purpose:** Learn why a visualization or evaluation is valid before polishing its appearance.  
**Boundary:** This learning skill **complements**, rather than replaces, the [Data Visualization & Scientific Communication production skill](../data-visualization/SKILL.md), [FRAME presentation production](../frame-presentations/SKILL.md), [academic quality](../../standards/academic-quality.md) and [source integrity](../../standards/source-integrity.md).

## When to load

Use for requests such as *teach me data visualization*, *continue our FRAME data-visualization learning*, *revisit Study 07*, *quiz me on benchmarking*, *compare two explanations*, *what did we learn so far?*, *apply a chart/evaluation lesson*, and critiques of charts, AI performance reports, or evaluation methodologies.

Read [the twelve-lesson map](LEARNING-PATH.md) to select a lesson, then [the exercise evidence register](EVIDENCE.md) when specific figures, results, code or past artifacts are relevant. **Do not invent access to the original ZIP/PPTX:** reopen the actual archived README, CSV, script or QA notes in the current context before citing a lesson's exact method or calculation. Previous conversation summaries do not substitute for reading that source.

## Learning workflow

1. **Orient:** Identify the learner's question, prior lesson and the next useful difficulty. If the user says “continue,” resume the last stated next lesson rather than restarting the course. The recorded sequence ends at **Lesson 12: uncertainty validation and monitoring**. The *proposed*, not yet completed, Lesson 13 is **Data Drift and Change Detection**.
2. **Reopen sources:** Inspect the relevant exercise's actual README and scripts/data; if unavailable, teach the general principle and disclose that the earlier example could not be verified. For library capabilities use [the five-tool catalog](../data-visualization/SOURCES.md); for scientific methods reopen an appropriate technical reference and the exercise citation.
3. **State a testable question:** Define the audience's decision, quantities, units, denominators, class labels, evaluation population and whether the data are synthetic, observed or simulated.
4. **Teach one distinction:** For example SD vs CI vs PI; paired vs independent observations; statistical vs practical significance; ranking vs calibration; feature attribution vs causality; finite-grid robustness vs field reliability.
5. **Practice deliberately:** Prefer one controlled alteration while holding the underlying dataset fixed (change chart encoding, metric, weights, cost threshold, model, background, or uncertainty assumption). If studying intervention effects, distinguish counterfactual model scores from real measured outcomes.
6. **Verify and critique:** Recompute any stated numbers from source data, review chart fidelity, show competing interpretations and limitations; use accessibility checks and static artifacts. Treat uncertainty and missing observations explicitly.
7. **Reflect and record:** Ask for a prediction before the reveal when useful. Offer one explanation question or a short exercise; assess reasoning, not just formula recall. End with an evidence-qualified takeaway and optional next step.

**Do not automatically generate a PPTX or a full new project** for a casual idea or question. When the user asks to continue the established hands-on study series or explicitly requests a deck, it is appropriate to build a small editable lesson with reproducible code/data, notes, PDF and visual QA. Avoid turning every lesson into a new repository skill.

## Teaching principles proven useful in the source exercises

- **Source truth before aesthetics:** Verify input provenance, metric definitions, axes, denominators, split boundaries and assumptions before choosing a plot.
- **Keep evaluation levels separate:** Observation spread; sampling uncertainty; uncertainty about future cases; statistical evidence; operational consequences.
- **Match the analysis to the design:** Use paired plots only for truly matched units; label threshold-cost assumptions; show subgroup support when aggregating.
- **Respect conditional explanations:** SHAP values depend on model and background; permutation importance depends on model, metric and dataset. Neither identifies causal interventions by itself.
- **Model score is not measured service quality:** Synthetic scoring rules, calibration, operational telemetry and causal impact must be distinguished.
- **Reproducible output has layers:** CSV + script + verified calculations, static SVG/PNG, optional browser HTML, editable PowerPoint shapes, and a native PowerPoint chart with an embedded data workbook are different artifacts.
- **MAK styling supports evidence:** Paper `#F5F3EE`, Ink `#161616`, restrained Signal `#E64B3C`, confirmed Latin-script Inter. Preserve actual logo artwork and the unresolved Persian-font decision. No chart styling preference is a substitute for numerical honesty.

## Four study modes

- **Explain:** Concise concept, visual encoding, example and a misconception check.
- **Compare:** Same input data, two legitimate views, plus why the conclusion appears different.
- **Practice:** Provide a small data/code exercise, a predeclared hypothesis, expected calculations and checks; labels must say *synthetic* if applicable.
- **Audit:** Review a figure or model evaluation for source credibility, class/axis conventions, uncertainty, costs, reproducibility, accessibility and unsupported causal claims.

## Outcome/QA gate

Before saying “complete,” check: original source reopened; inputs and counts consistent; derived numbers recalculated; no test leakage; plots describe what the method actually measures; uncertainty has a definition and assumptions; synthetic results not mislabeled as real; no claim of guaranteed deployment impact; slide notes, editability and rendering checked when a deck exists. Report unchecked capabilities separately, including font portability on the university presentation computer.

## Versioning and scope discipline

A completed study is **learning evidence**, not a new binding design standard or measured gain in student comprehension. This skill is a curriculum route; the existing [Data Visualization skill](../data-visualization/SKILL.md) remains the production reference. Add future lessons to [LEARNING-PATH.md](LEARNING-PATH.md) after the exercise is actually created and inspected; never mark the proposed Lesson 13 as completed in advance.

This repository is public: do not commit the original personal MAK logo, private course materials, unpublished data, copyrighted textbook chapters, credentials or complete prior artifact ZIPs by default. GitHub-hosted Markdown must be explicitly read by an assistant; it does not automatically install a skill in ChatGPT.
