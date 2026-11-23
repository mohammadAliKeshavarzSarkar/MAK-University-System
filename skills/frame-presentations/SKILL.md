---
name: frame-presentations
description: Plan, build, revise, and quality-check university presentation decks, especially AI, software engineering, research, quantitative topics, and technical diagrams. Use MAK identity standards and deliver editable PowerPoint when requested.
---

# FRAME — Presentation Architecture | Design & Production

**Workflow version:** 0.2 — pilot-informed working standard (2026-11-23)  
**Scope:** University and technical presentations, including samples and existing-deck reviews.

This is a **repository workflow instruction**, not an automatically installed ChatGPT skill. An agent must load it and the referenced standards; it must not claim this file governs conversations where it has not been consulted.

## 1. Read and respect the sources

Read in this order when accessible:

1. [Academic quality standard](../../standards/academic-quality.md).
2. [Source integrity standard](../../standards/source-integrity.md).
3. [FRAME guidebook, v0.3 candidate](../../design/frame-guidebook.md).
4. Course brief, assessment rubric, user-supplied lectures/papers, and current user corrections.

Current user directions and actual university requirements take precedence over repository defaults. If an essential source is unavailable, explain the limitation; never imply it has been reviewed. Distinguish source facts, verified outside research, interpretations, examples, and assumptions.

## 2. Choose the production mode

- **Plan / outline:** Return a meaningful narrative, slide list, and source gaps; do not create a deck unless requested.
- **Build / revise:** Create or change the requested editable presentation and supporting outputs.
- **Audit:** Review existing slides for pedagogy, accuracy, accessibility, editability, branding and export quality.
- **Pilot / experiment:** Choose a clearly labeled sample topic when authorized, test one or more layouts, and record findings before promoting new rules.

Avoid turning an informal presentation idea into a full production workflow unless the user wants that deliverable.

## 3. Stage gates

### A — Brief and evidence

Determine from the available conversation and materials: subject, course, audience, presentation language, intended teaching goal, time limit, slide count if imposed, source constraints, required citation style, delivery medium and editability expectations.

**Exit condition:** Scope and any material uncertainty are explicit. Don't repeat questions already answered.

### B — Storyboard before styling

Create a slide-by-slide plan. Each slide should have one teaching job, a meaningful title, the key claim or question, and any visual or evidence needed. Useful patterns include:

- **Technical explanation:** problem → mechanism → worked example → limitations → takeaway.
- **Research:** motivation → question → method → evidence → limitations → discussion.
- **Quantitative lesson:** definitions → worked data → formula → result → interpretation and trade-offs.

Don't force an identical narrative on every assignment. Use speaker notes for useful explanation that would crowd the slide.

**Exit condition:** The story is technically defensible, sized to the time limit, and does not depend on unknown evidence.

### C — Apply FRAME visual architecture

Treat the [guidebook](../../design/frame-guidebook.md) as the single visual reference; do not duplicate all its specifications here.

- Use the documented **working content tokens** Paper #F5F3EE, Ink #161616 and Signal #E64B3C. Preserve supplied MAK logo artwork exactly; its image pixels differ slightly from these content tokens.
- Default to **Inter** for English text, pending user confirmation of alternative type. PT Mono or IBM Plex Mono may be used sparingly for labels.
- Use 16:9 slides, a coherent grid, generous whitespace and meaningful hierarchy.
- Favor light slides for dense content; a dark slide can omit the logo when no approved inverse asset exists.
- Use Canva pattern families selectively, never as mandatory decoration.
- For Persian/mixed Persian-English slides, verify RTL/LTR order and choose a suitable tested font rather than pretending Inter covers every script.
- When a Persian sentence is split across multiple **token boxes or timeline nodes**, verify the physical reading order is right-to-left; setting each text box to RTL is not enough. Number the positions explicitly when useful.
- Avoid treating résumé mockups as authoritative academic facts.

**Projection-first targets, subject to real context:** title 30–40 pt; key body 18–24 pt; display mathematics around 26 pt or larger where practical; chart legends/categories 14–16 pt or larger; small secondary ticks generally at least 12 pt. Split content before shrinking the central explanation. Footers of 8–9 pt from Pilot 01 are not reusable classroom defaults.

**Exit condition:** Main points, diagrams, labels and annotations are distinguishable at full-slide viewing size.

### D — Build accurate, editable content

**Equations and worked examples**
- Define variables and classes before using abbreviations such as TP, FP, TN and FN.
- Independently recompute numerical examples, percentages, totals and rounded results.
- Prefer editable PowerPoint elements for formulas when they preserve mathematical clarity; align numerators, denominators, operators and fraction bars.
- Identify illustrative/synthetic counts and model outputs explicitly. Never present them as measurements.

**Charts**
- Choose a chart based on the comparison to be explained, not visual fashion.
- Prefer native editable PowerPoint charts when subsequent data modification matters; check embedded series/workbook data.
- Identify axes, units, categories, denominators, legend meanings and data source.
- Validate chart values against the explanatory text. Threshold illustrations must be coherent with their underlying data; do not invent a smooth empirical curve from a few synthetic points.
- Do not use color as the only way to distinguish series.

**Architecture and code**
- Favor editable native shapes and connectors. Name components, show meaningful boundaries and make flow direction unambiguous.
- Inspect arrowheads and labels at projected size; very short connectors may become unreadable.
- Keep code accurate and concise; prefer stepwise explanation over small full-screen code dumps.
- Check that illustrated causal relationships and system behaviors are supported by the actual material.
- **Check diagram edges for semantic type correctness.** Intermediate scores, normalized attention weights, value vectors, and final outputs are different quantities. In multi-head attention, arrows to the final concatenation must originate from the individual head **outputs**, not merely their attention-weight charts.

**Source attribution**
- Cite claims, charts and images appropriately; provide a reference slide or notes when needed.
- Never invent bibliography entries, model performance, experimental results, authorship, or professional credentials.

**Exit condition:** The presentation's technical content, chart numbers and citations can be checked independently.

### E — Render, inspect, deliver

Do not declare the deck complete solely because the PowerPoint file was saved.

1. Check slide count, overall structure and available speaker notes.
2. Programmatically inspect slide bounds and layout overflow where possible.
3. Render to a slide preview or PDF; visually inspect representative *and* dense slides at full-page scale.
4. Check font substitutions, cropped text/images, contrast, chart labels, connectors, equation alignment, and RTL/LTR behavior. In bilingual token diagrams verify the left/right *object order*, not only the direction of the text inside each object.
5. Verify the final requested files can open. If charts are meant to be editable, confirm they are real PowerPoint charts, not just screenshots.
6. Provide an editable PPTX by default for a deck request. Deliver a PDF additionally **when requested**; don't infer every request needs PDF.
7. Disclose any verification step you could not perform. Do not claim classroom projection or font installation was tested without doing so.

**Exit condition:** Delivered files render coherently, material claims are supported, and unresolved defects are disclosed.

## 4. Review and version control

After each pilot or genuine university task, summarize:

- Observed issue and exact slide/context;
- Root cause or plausible contributing factor;
- Proposed change to the skill or guidebook;
- How to test whether the change helps.

Improve only based on useful recurring evidence. Changes should be reviewable, ideally through a branch and pull request, and never silently redefine unresolved brand decisions. Keep source/binary assets and sensitive coursework out of this public repository without permission.

### Pilot evidence incorporated into v0.2

- **RAG Pilot 01:** 8 slides, including an editable architecture diagram and source references; smallest measured text 8.5 pt. Lesson: protect classroom readability and connector legibility.
- **Classification Metrics Pilot 02:** 11 slides; 2 native editable charts; editable mathematical constructions; speaker notes; smallest measured text 11.8 pt. Lesson: numerical coherence and full-slide chart checks are essential.

Both were synthetic/teaching pilots, not evidence for experimental claims. See the [guidebook](../../design/frame-guidebook.md) for the associated design decisions.

## 5. Hard stops

Do not distort or recolor the approved geometric logo; copy Canva explorations as fixed slide templates; fabricate evidence; present synthetic results as research findings; upload private materials; merge GitHub policy changes without user approval; or claim this workflow is universally enforced outside environments that actually load it.
