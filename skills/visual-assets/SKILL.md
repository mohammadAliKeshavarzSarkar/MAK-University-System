---
name: visual-assets
description: Research, select, generate, refine, construct, embed and audit presentation imagery for MAK/FRAME; use for editorial photography, conceptual images, technical illustrations, transparent assets, image composition, rights review and PowerPoint image QA.
---

# FRAME / IMAGE — Visual Asset Architecture

**Version:** 0.1 — pilot-informed working skill (2026-11-24)  
**Scope:** Presentation visuals, not a mandatory image style or a collection of stock assets.

This skill consolidates twelve guided IMAGE lessons and two production pilots. It complements [FRAME presentation production](../frame-presentations/SKILL.md), [the design guidebook](../../design/frame-guidebook.md), [academic quality](../../standards/academic-quality.md), [source integrity](../../standards/source-integrity.md), [iconography](../../design/iconography.md), and [scientific visualization](../data-visualization/SKILL.md). Follow current user directions and actual course or publication requirements first. Load this file explicitly; it does not install an image generator or automatically become active in ChatGPT.

## When to use

Use when a slide needs imagery, when selecting or editing an asset, when creating a technical diagram or conceptual metaphor, and when auditing presentation image quality or rights. For guided study, consult [the twelve-lesson path](LEARNING-PATH.md). For an informal concept, do not automatically generate images or build a deck.

## 1. Classify before choosing a medium

| Function | Preferred approach |
| --- | --- |
| Evidential | Authentic research figure, measured data or original documentary material; verify context and rights |
| Explanatory | Editable native shapes, verified vector illustration or reproducible diagram code |
| Contextual | Authentic photograph or clearly labeled non-evidential illustration, as appropriate |
| Conceptual | Original graphic abstraction, photographic-style illustration or generated metaphor |
| Decorative | Optional restrained imagery; omit when it distracts or adds no value |

A generated visual must not be passed off as an authentic observation, real screenshot, historical record, experimental result or actual physical device. For exact quantitative figures, use the [Data Visualization skill](../data-visualization/SKILL.md); for simple icons, use [Lucide-first iconography](../../design/iconography.md). Image generation is optional, not a default requirement.

## 2. Brief and source

Before searching or generating, define the slide's message, function, subject, medium, expected placement/aspect ratio, focal position, negative space, color semantics, technical detail and intended distribution. See [art direction](STYLE-GUIDE.md). Retrieve source-specific images from original file pages, official archives or research sources; use the [source catalog](SOURCES.md) as a starting point. Check the actual image, creator, license version, permitted context, adaptation restrictions and other relevant rights. Search previews are not cleared production assets. If retrieval or rights verification fails, omit the asset or use an explicitly labeled original alternative; do not pretend retrieval succeeded.

## 3. Create or refine

Use [image-generation and editing guidance](IMAGE-GENERATION.md) for conceptual art; use programmatic graphics, native shapes or verified source diagrams for exact relationships. Keep originals unchanged. Make one intentional revision at a time when evaluating an edit. Review actual outputs against the brief, including accidental objects, labels, crop, geometry and consistency. Record the actual prompt/tool/version if available; leave unknown values unknown. Do not claim pixel-exact preservation without verification.

## 4. Integrate into FRAME

Use the shared grid and established brand choices, not a fixed image quota. Keep titles, captions, equations and labels editable. Preserve aspect ratio; Fit when full content matters, Fill when cropping is justified. Keep meaningful color and orientation intact, including scientific images on RTL slides. Use sufficient raster pixels for the placed area, valid transparent PNG when needed, and SVG for appropriate vector content with tested raster fallback. Embed local image bytes in the PPTX instead of relying on remote URLs. Preserve source SVG/code and original images separately; vector artwork is not automatically an editable PowerPoint diagram.

## 5. Verify and deliver

Apply [production QA and provenance](PRODUCTION-QA.md) to the actual files. Inspect meaning, rights, attribution, accessibility, resolution, alpha, crop, image relationships, SVG and fallback file signatures, slide bounds and final rendered output. Distinguish visual inspection from package inspection and target-platform testing. For a deck, deliver the requested editable PPTX and any requested PDF or assets package; include source/credit records where needed. Never silently ship an invalid image fallback or fabricate an unavailable visual. If a capability cannot be tested, document it.

## Quality boundaries

The two pilots support a working workflow for conceptual artwork, native crops, editable text/diagrams, embedded raster images, reference-led refinement with limitations, transparent PNG, SVG and repaired raster fallbacks. They do not establish native Office interoperability, documentary-photo embedding, a stable independent AI image series, or public distribution clearance. See the exact [pilot evidence and open tests](PRODUCTION-QA.md). Keep pilot archives local; do not publish private artwork, font binaries, or assets with unreviewed rights.

## Learning and change control

Study → adapt → practice → inspect → record findings. Prefer a small meaningful experiment over another framework. The twelve guided lessons are complete as studies; not every technique has been tested. Promote changes only after review, retain the existing MAK identity, and do not convert provisional art directions into mandatory brand rules. The next priority is to apply this workflow in real university presentations and close the remaining tests when needed.
