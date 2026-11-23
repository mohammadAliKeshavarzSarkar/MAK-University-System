# FRAME — Presentation Design Guidebook

**Version:** 0.3 — Lessons from two presentation pilots  
**Date:** 2026-11-23  
**Status:** Working guidebook; brand decisions are tracked as confirmed, provisional, optional, or open  
**Studio:** FRAME — Presentation Architecture | Design & Production  
**Evidence:** v0.2 brand sources plus rendered RAG Pilot 01 (8 slides) and Classification Metrics Pilot 02 (11 slides).

## 1. Purpose

FRAME produces editable, accurate, accessible and visually coherent university, research, technical and professional presentations. It inherits the personal brand's identity, not every layout in its Canva references.

**Principle:** Clarity before decoration; structure before styling; evidence before claims.

## 2. Evidence and authority

**Sources reviewed**

1. *MAK — Personal Brand Guidelines | V1.0* (16 pages), Canva design `DAHaUb9MilI` — primary stated palette, typography and general identity principles.
2. *MAK — Visual Asset Library | Production V1.0* (12 pages), Canva design `DAHaUSr1X14` — optional pattern and editorial motif library.
3. *MAK — Personal Resume A4 | Phase 04* (1 page), Canva design `DAHaWX09mZk` — illustration of brand application; **a draft, not an authoritative factual CV**.
4. Untitled identity exploration board, Canva design `DAHaUflN3-w` (1 page) — alternative font suggestions and identity explorations.
5. User-supplied exact logo assets: `logo.png`, `logoTypeMain.png`, `logoType (2).webp`.
6. Project's professional writing identity and academic/professional profile, for tone, accuracy, and factual positioning.

**Decision hierarchy (FRAME proposal):** the user's newest explicit confirmation > authentic supplied logo files > stated personal brand guideline > exploratory Canva boards > FRAME-specific adaptations. Conflicts are documented, not silently resolved.

## 3. Brand identity — required foundations

### 3.1 Logo [required; usage roles provisional]

The uploaded geometric MAK monogram/wordmark artwork is the brand asset to preserve. It uses strong diagonals, a red triangle, and, in the full horizontal variants, a red-dot-accented wordmark and full personal name.

- `logo.png`: standalone monogram candidate, suitable for compact logo positions.
- `logoTypeMain.png`: horizontal logo lock-up candidate, suitable for title and closing slides.
- `logoType (2).webp`: alternate horizontal export, potentially useful for lightweight digital use.
- Maintain original proportions, geometry, typography, colors, and clear space.
- Do not stretch, rotate, add gradients/shadows, or redraw the symbol casually.
- Light/inverse logo variants for dark backgrounds require an approved asset; do not auto-invert dark logos.
- The older Canva guideline describes a proposed typographic `MAK.` signature. It should **not** silently replace the newer supplied geometric logo.

### 3.2 Colors [brand family required; exact token reconciliation open]

**Declared in the Canva Personal Brand Guidelines:**

| Role | Token | Hex | Intended use |
|---|---|---|---|
| Paper | `color.paper` | `#F5F3EE` | Dominant warm light background |
| Ink | `color.ink` | `#161616` | Main headings and normal body text |
| Signal | `color.signal` | `#E64B3C` | Restrained emphasis, callouts, markers |

The source guideline offers an **80% Paper / 15% Ink / ≤5% Signal** application mix as a *guideline*, not a numerical constraint on charts and academic illustrations.

**Measured directly from uploaded image pixels:** near-black `#151415`, red `#E74B3B`. This is a small but real difference from the Canva design tokens. **Do not recolor the uploaded logos.** For new FRAME content, use the documented Canva tokens pending explicit final choice; preserve images as supplied.

Secondary grays, accessible chart series and approved dark-background colors are **not finalized**.

### 3.3 Fonts [Inter confirmed for English/Latin; Persian font open]

**Confirmed by the user on 2026-11-23:** [Inter](https://fonts.google.com/specimen/Inter) is the **official primary English/Latin-script typeface** for FRAME presentation titles, headings, body text and standard diagram/chart labels.

- Use **Inter Regular, Medium, SemiBold and Bold** where the hierarchy calls for them; choose weight by semantic importance instead of applying heavy type everywhere.
- **PT Mono** or **IBM Plex Mono** remain *optional/provisional* choices for technical/editorial labels and indices, not replacements for ordinary body text.
- The exploratory Canva board suggested **Neue Haas Grotesk or Helvetica** as earlier options. They are **not** the approved primary choice; don't silently substitute them.
- **Persian typography remains unconfirmed.** Inter does not provide the needed Persian/Arabic glyph coverage. Choose and test a separate Persian-capable companion font and mixed-direction layout before standardizing it.
- Source: [Google Fonts — Inter](https://fonts.google.com/specimen/Inter); [official Google Fonts Inter source](https://github.com/google/fonts/tree/main/ofl/inter); [SIL Open Font License 1.1](https://github.com/google/fonts/blob/main/ofl/inter/OFL.txt).
- For deck production, check that Inter is installed and discoverable in the actual presentation/rendering environment. It is installed in the current FRAME working environment, but **that does not mean it is installed on the user's university computer or every future runtime**. Check font substitution and PDF/PPTX rendering before delivery.
- Font binaries are **not committed** to this public guideline repository. Download an official copy when an environment needs it; retain licensing notices if redistributing fonts. Avoid giving users raw font files as presentation deliverables.

The brand guide's type sizes are designed for mixed media. For *projected 16:9 presentations*, start with:

- Display/cover: 44–60 pt
- Slide headings: 30–40 pt
- Body: 18–24 pt
- Charts and technical annotations: preferably 16–20 pt
- Labels, footnotes, and source details: 12–16 pt where feasible

These are testing ranges, not rules to compress content. Persian and mixed-language font fallbacks need separate selection.

**Pilot-based projection guidance — proposed for v0.3:**

- Target **18–24 pt** for main explanatory text and **30–40 pt** for slide titles. Split slides before reducing central explanations below 16 pt unless the assignment truly requires denser material.
- Key displayed math should be comfortable at a distance, ideally **26 pt or larger** where possible, with aligned fraction parts and variable definitions.
- Chart legends and category labels should generally be **14–16 pt or larger**; reserve a 12 pt floor for genuinely secondary tick labels.
- Source metadata can sometimes be smaller than the main body, but information essential to understanding must not hide in tiny footers. Prefer a dedicated references slide or speaker notes.
- Pilot 01 used 8.5 pt footers and some 14–15 pt body text. These are **not approved classroom defaults**. Pilot 02's smallest measured type was 11.8 pt, primarily peripheral text; core mathematical and chart explanations were larger.

These targets require visual testing at actual classroom scale, not merely a file-level font inspection.

## 4. Presentation-specific system [provisional]

- **Canvas:** widescreen 16:9 landscape; export both editable `.pptx` and PDF when requested.
- **Grid:** consistent margins and alignment; a flexible 12-column layout is available as a reference, not compulsory for every slide.
- **Hierarchy:** one primary message per slide; titles communicate a conclusion or question whenever useful.
- **Spacing:** prefer repeatable 8-based increments, adapted to slide dimensions.
- **Backgrounds:** Paper/light preferred for teaching, dense data, diagrams and readable research content; dark section or opening slides may use legible light text **without a logo**; if a logo appears, use only an approved inverse artwork. Never force a dark logo onto a dark background.
- **Brand placement:** full horizontal logo generally on cover/closing slides; compact monogram sparingly elsewhere. Never let logo compete with content.
- **Accent:** Signal red for emphasis, selected diagram elements and attention markers; not default red paragraphs or a background for every slide.

## 5. Optional visual vocabulary — not mandatory

The Canva Asset Library proposes four pattern families:

1. **Signature Slash** — expressive edge gesture for cover or section transitions.
2. **Technical Grid** — subtle engineering, AI, research and technical structure.
3. **Quarter Arc** — modular editorial rhythm.
4. **Monogram Field** — abstract letterform-derived background, not an exact copy of the logo.

It also proposes slash motifs, corner marks, editorial rules and registration marks. These are **optional tools**. The source recommends one strong visual gesture at a time, typography-first hierarchy and red as signal rather than ornament. Never use a pattern just to fill empty space.

### Iconography — adopted visual resource

Lucide is the **default general-purpose icon library** for FRAME and other MAK University workflows. Follow the shared [MAK iconography policy](iconography.md). Prefer one coherent 24×24 outline family, adapting size and Ink/Signal color to the slide. **Custom-drawn icons and complete diagrams remain allowed** whenever a stock icon is semantically inadequate, especially for AI/math/architecture. Do not misrepresent a complex algorithm with a generic icon, overdecorate slides, or alter the approved MAK logo. The curated SVG files live in [`assets/icons/lucide/`](../assets/icons/lucide/) and retain their upstream license.

## 6. Technical communication and factual discipline

- Establish narrative and slide outline before decoration.
- Use architecture diagrams for component relationships and clear directional data flows.
- Use charts only when they clarify a measured or explicitly illustrative relationship.
- Show labels, units, source attribution and important assumptions.
- Distinguish real data, estimates, demonstrations and hypothetical examples.
- Make editable native shapes, texts, charts and diagrams wherever practical.
- No fabricated citations, outcomes, impact metrics or professional titles.
- For code and mathematical slides, prioritize legibility over exhaustive detail.
- Provide notes when the live spoken explanation needs additional technical nuance.

## 7. Editable mathematics, diagrams and charts — proposed rules

### Equations and worked numerical examples

- Use **editable PowerPoint text and shapes** for formulas when this preserves correctness; align independently editable numerators, denominators, operators, and fraction bars.
- Define all variables and the positive class before calculating classification metrics.
- Recalculate derived results from displayed counts; check totals, percentages, and rounding.
- Label synthetic counts and illustrative scenarios as such. Never imply that they came from a trained model or empirical study.

### Native charts

- Prefer **native editable PowerPoint charts** when data should be adjustable after delivery. Check that series values and embedded chart data remain accessible.
- Name all chart axes, categories, units, source context and series. Use values or direct annotations when the audience needs exact comparisons.
- For precision/recall and threshold plots, maintain numerical coherence across operating points, and never present interpolated invented points as an empirical performance curve.
- The brand's Ink and Signal colors can help identify simple series, but add labels, markers, or other non-color signals. The wider accessible chart palette remains open.

### Software, AI and system architecture

- Make component roles, interface boundaries, directional flow, and relationships explicit.
- Treat connector arrows as claims about what passes between components. Do not draw a weight chart directly feeding a concatenation node when the algorithm concatenates **weighted value outputs**.
- When drawing sequence tokens in Persian, place their **physical objects in right-to-left order**, and show the reading direction or numbered positions where confusion is possible. Right-aligning text inside individually ordered boxes does not fix reversed sequence flow.
- Prefer native editable shapes and connectors. Inspect short arrows and label spacing at full-slide scale.
- Do not draw unsupported dependencies or causal claims simply to create a pleasing diagram.

## 8. Accessibility and QA

- Text contrast must be suitable for the role and projected environment.
- Red Signal on Paper is too low-contrast for ordinary small text; prefer dark Ink for body copy.
- Do not encode meaning by color alone; add labels, markers, patterns or legend.
- Use sensible slide density; split complex material across slides rather than reducing font size severely.
- Check English/Persian directionality if applicable. Separately verify ordered token boxes, mixed Latin/Persian vectors and formulas in the actual rendered slide; avoid assuming that underlying string order equals visual reading order.
- Before delivery verify text overflow, image cropping, slide consistency, font substitutions, chart scales, factual sources and exported PDF rendering.

## 9. Portfolio alignment and source caution

The linked resume Canva draft contains some placeholder language and a university branch label that conflicts with the uploaded academic profile. Treat it as a **visual reference only** until facts have been individually verified. FRAME's self-introduction and project descriptions must follow the latest confirmed academic/professional profile, never copy unverified résumé draft claims.

## 10. Decision register

| Topic | Status | Next test or decision |
|---|---|---|
| Personal geometric MAK logo | Required | Confirm preferred primary lock-up and approved inverse variant |
| Paper / Ink / Signal brand family | Required | Choose exact tokens: Canva guide vs slightly different uploaded logo pixels |
| Inter English/Latin typography | Confirmed | Verify font installation, weight mapping and rendering on the actual presentation machine |
| PT Mono or IBM Plex Mono | Provisional | Test as captions/labels, not extended slide body |
| 16:9 | Adopted | Standard for most decks |
| 12-column / 8-based structure | Provisional | Test on first technical presentation |
| Signature Slash, Grid, Arc, Monogram Field | Optional | Use only when informative |
| Dark presentation mode | Optional; inverse logo open | Dark slides may omit logo; approved inverse artwork still required for on-slide logo use |
| Persian typography | Open | Choose tested compatible font and mixed-language layout rules |
| Secondary chart palette | Open | Choose after realistic diagrams/charts are tested |

## 11. Evidence from two sample decks

| Pilot | Inspected outputs | Main lesson | Proposed action |
|---|---|---|---|
| RAG Pilot 01 | 8 slides; editable architecture diagram; rendered PDF; synthetic example; notes | Consistent MAK identity, but 8.5 pt footer and some 14–15 pt content are weak projection defaults | Raise font targets and verify arrows, references and diagram labels |
| Classification Metrics Pilot 02 | 11 slides; 2 native editable charts; editable fraction-style formulas; notes; 11-page PDF | Quantitative layouts became clearer with room for equations and chart labels; minimum font 11.8 pt | Preserve numerical, editability and rendering checks |

**Verified pilot structure:** Both source PowerPoint files were inspected: 8 and 11 slides respectively, with 0 and 2 native PowerPoint chart objects. Neither deck has native shapes outside the slide canvas. Both are teaching pilots, not records of real experiments.

**Pilot 02's clearly labeled synthetic case:** 1,000 cases, with 950 negatives and 50 positives. A screening-model example has TN=912, FP=38, FN=14, TP=36, yielding accuracy 94.8%, precision ≈48.6%, recall 72.0%, and F1 ≈58.1%. Three illustrative operating thresholds lower from 0.70 to 0.50 to 0.30; their associated true-positive and false-positive counts should be checked for monotonicity.

**Cross-pilot findings:** The minimal editorial direction transfers well to AI and statistics. Editable diagrams and equations are feasible, but charts need extra space, and mathematical examples need a repeatable calculation review. An unapproved inverse logo is not required for dark recap slides.

### Targeted bilingual diagram evidence (Pilots 03–04)

- **Pilot 03:** Rendering exposed a vector whose values appeared reversed inside an RTL Persian sentence; isolating mathematical expressions into editable LTR text objects corrected the display.
- **Pilot 04 refinement R1:** A four-token Persian sequence was physically reversed to honor RTL reading order. A multi-head architecture diagram was corrected to show that **head outputs**, rather than the attention-weight bars, feed the concatenation step.
- These are **technical QA lessons** grounded in the sample, not approval of every Pilot 04 visual choice. The Persian font, inverse logo, and other open identity choices remain provisional.

## 12. Pre-delivery checks — proposed standard

- [ ] Course requirements, intended audience, language and time limit are reflected in the deck.
- [ ] Every slide advances one clear teaching point; source claims are traceable.
- [ ] Equations, sample totals, percentages, chart values and rounding independently recalculated.
- [ ] Connectors, labels and equation parts checked at full-slide projection scale.
- [ ] Editable chart objects and their embedded data verified when editability is promised.
- [ ] Font size, contrast, labels, RTL/LTR layout and color-independent distinctions checked.
- [ ] No clipped content, out-of-bounds shapes, accidental font substitutions or distorted images.
- [ ] Exported PDF or slide-preview rendering visually inspected; page count consistent.
- [ ] Notes, reference context and requested delivery files complete and usable.
- [ ] No private or unauthorized files copied into this public repository.

## 13. Approval and iteration rule

This is a **living, reviewable guidebook**. Improve rules through evidence from actual presentations and review proposed changes through a GitHub pull request before merging. Preserve original Canva references and supplied logo assets unchanged.

**Still open:** primary logo lock-up and inverse variants, minor differences between color tokens and embedded logo pixels, the Persian companion typeface and bilingual font pairing, and a broader accessible chart palette. Future changes should be motivated by specific observed problems and tested on real material.
