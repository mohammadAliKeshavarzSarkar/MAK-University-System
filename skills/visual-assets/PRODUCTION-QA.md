# FRAME / IMAGE — Production QA and pilot evidence

## Practical production defaults

- Preserve the best available original and editable source (diagram code, SVG, chart data, native shapes). Keep a separate production derivative; do not overwrite the only master.
- Use SVG for appropriate pure-vector geometry, PNG for screenshots and transparency, JPEG for appropriate photos, and native shapes/charts when component/data editing is required. SVG can contain raster content. WebP/TIFF compatibility and SVG conversion must be tested before promising support.
- Estimate pixel coverage for the actual placement. Given raster source W × H and target container w × h in display pixels, Fill scale is max(w/W,h/H); Fit scale is min(w/W,h/H). Values above 1 require upscaling; adequate dimensions alone do not guarantee sharpness. DPI metadata changes do not add detail.
- Embed assets locally in the PPTX. Validate actual file signatures/decoding, alpha, SVG masters and each fallback, not only extensions. Inspect transparency on intended backgrounds; preserve meaningful contrast.
- Keep a high-quality editable master; optionally produce a smaller distribution copy. Verify actual compression and rendering, rather than assuming a desktop setting applies to a generated deck.

## Minimal per-asset record

Use a local manifest (JSON/YAML or a simple table). Example fields, not a license determination:

```yaml
asset_id: IMG-001
role: conceptual
origin: ai-generated
title: null
creator_or_tool: null
source_url_or_generation_record: null
source_file: null
production_file: null
dimensions_px: null
sha256: null
prompt_or_edit_history: null
license_and_version: null
intended_distribution: classroom
rights_basis_and_review_date: null
modifications: []
evidential: false
alt_text: null
credit: null
used_on_slides: []
review_status: pending
```

Record actual origin, not a guessed author. For external works check individual license and terms (including NC/ND/SA when relevant), document attribution using title/author/source/license when applicable, and disclose edits as required. Educational use does not automatically authorize public redistribution. Check privacy, trademark and other rights where relevant. A checkbox alone is not permission. Include readable credits in a manner compatible with the license and a durable companion record. Generated visuals must be clearly distinguishable from documentary evidence. Provide meaningful text alternatives for informative assets and an equivalent explanation for complex diagrams; mark decorative assets as appropriate.

## Final review

| Gate | Inspect |
| --- | --- |
| Meaning | Accurate subject/relationships; appropriate role; synthetic/generated content disclosed; no invented evidence |
| Visual | Relevance, crop, focal point, typography, contrast, consistency, meaningful color/orientation |
| File | Actual formats, dimensions, alpha, correct aspect ratio, local embedded image relationships, valid fallback decoding |
| Editability | Native text/labels/shapes as required; native chart versus image distinction; source masters retained |
| Rights/accessibility | Specific asset provenance, intended use, attribution, modifications, alternative text, reading order |
| Rendering | Actual PPTX and requested PDF, slide/page counts, notes, boundaries, full-slide inspection, font substitutions |
| Delivery | Check the final saved files and target viewer where available; disclose missing checks and unresolved defects |

A structural check is not a full visual review. A LibreOffice render is not native Microsoft PowerPoint validation. Alternative text presence is not full accessibility certification. No renderer test establishes classroom projection readability.

## Evidence register — two completed pilots

On 2026-11-24 the local source archives were reopened; ZIP integrity passed, and the included README, QA report, asset manifests and Pilot 02 numerical/structural audit records were inspected. These are records of prior tests; this consolidation is not a new rendering or independent complete rerun.

### Pilot 01 — Designing Complex Systems

Local archive: `FRAME_IMAGE_Pilot_01_Source.zip` (under the original `frame_image_pilot/` delivery). Includes `build.py`, `original.png`, `synthetic_latency.csv`, manifest, README and QA report. Rebuild with Python/python-pptx/Pillow using retained pixels; install Inter separately; optional LibreOffice PDF export.

- QA reports 8 slides, 8 notes sections, 137 slide objects, 4 picture placements, 8 PDF pages and 0 out-of-bounds objects at 100 EMU tolerance. One unique embedded media file; all four pictures used unchanged source bytes and had descriptions.
- 1672 × 941 original conceptual image, native crops, roughly 1.15× upscale for Full HD cover. Editable native diagrams/bars, not native chart workbooks. Three fictional latency values.
- Exact generation prompt unavailable. No generative refinement or SVG/transparency tests in this pilot. External candidate CERN Data Centre.jpg, Mramoeba, source-stated CC0 1.0, file retrieval failed. No authentic logo included; text signature only.

### Pilot 02 — Scaling Without Losing Control

Local archive: `FRAME_IMAGE_Pilot_02_Source.zip` (under `frame_image_pilot_02/`). Includes `prepare.py`, `build.js`, `patch_svg_fallbacks.py`, source images, vector/raster assets, synthetic capacity CSV, manifest, edit and structural audit JSON, README and QA report. Follow its README for dependencies (Python/Pillow/NumPy/CairoSVG, Node/pptxgenjs 4.0.0, separately installed Inter). Rebuild from retained assets; do not regenerate artwork as a prerequisite.

- QA reports 10 slides, 10 nonempty notes sections, 187 slide objects, 8 picture placements with descriptions, 10 LibreOffice PDF pages and zero out-of-bounds objects at 100 EMU tolerance.
- Seven PNG parts decode correctly, two SVG parts match the supplied vector master exactly, zero external image relationships. Two intentional source hyperlinks are not image dependencies.
- Original and ivory variant: 1672 × 941 RGB. Outside rectangle x=[1320,1460), y=[295,495), mean absolute 8-bit RGB channel difference 2.0959/255, pixels with any channel difference >10: 1.1215%, exactly equal pixels: 0.6408%. This approximate region is not a semantic mask or perceptual measure. Requested visual change succeeded; exact preservation did not.
- Original programmatic modules SVG and 1800 × 1240 RGBA PNG, alpha extrema 0 and 255, rendered on light and Ink backgrounds. Dark edges have reduced contrast on Ink. Two library-created PNG fallback parts actually contained SVG bytes; replaced with valid raster exports of the same geometry, then re-rendered. Package-level validation is not universal Office compatibility.
- Native diagram and plot use editable shapes. Toy capacity min(40 × replicas, 150) requests/s is constructed, not measured. Independent second-generation attempt rejected; consistency shown across generated reference pair and authored vector, not independently generated scenes.

Photo candidates recorded in the manifests: [CERN Data Centre.jpg](https://commons.wikimedia.org/wiki/File:CERN_Data_Centre.jpg) (Mramoeba) and [Front of server racks at NERSC.jpg](https://commons.wikimedia.org/wiki/File:Front_of_server_racks_at_NERSC.jpg) (Derrick Coetzee). The reports say both file pages stated CC0 1.0; file retrieval failed and neither photo was embedded. Reopen actual pages before reuse. No blanket public redistribution rights clearance is asserted.

## Open tests and scope

Authentic external photograph retrieval/embedding; independent multi-scene generated-image consistency; native Office rendering on actual target platform; SVG-to-native-shape conversion and older-viewer fallback behavior; image compression; full accessibility checker and reading order; classroom projection; public distribution rights review; final user approval of permanent styles. Keep these open until tested, not automatically completed by merging a skill.

Both archives are local evidence, not public repository files or claimed public downloads. No binary assets, personal logo, generated art, copyrighted reference images, or fonts need to be committed to adopt this workflow.

## Follow-up test — lossless embedded-media deduplication (2026-11-24)

The existing Pilot 02 PowerPoint was copied and optimized at the OOXML package level. Only byte-identical media parts with matching file extensions were deduplicated using SHA-256. Six relationship targets were rewritten to retained parts, five duplicates were removed, and any associated content-type overrides were removed. No image pixels, resolution, transparency, original SVG bytes, native slide objects or slide XML were intentionally changed; the original PPTX was preserved. The new ZIP passed its integrity test, retained media bytes matched the original exactly, all ten internal image relationships resolved, and zero external image dependencies were found. Retained PNGs decoded successfully. Python-pptx inspection found 10 slides, 187 objects, 10 nonempty notes sections and zero out-of-bounds objects at 100 EMU tolerance. Original and optimized decks were newly rendered via the same LibreOffice workflow: all ten PDF pages rasterized at the same scale had identical dimensions and pixel bytes.

- Original: 6,098,787 bytes; optimized: 3,325,485 bytes (45.473% reduction).
- Local output: `FRAME_IMAGE_Pilot_02_Lossless_Optimized.pptx`; not a public repository asset.
- This is lossless package-level optimization of one deck, not PowerPoint's native compression feature or a promised saving for other decks. Native Office compatibility is still untested. Prefer a separate copy and verify references, content types, actual image bytes, structural integrity and render equivalence before accepting a similar transformation. Do not use blind file deletion or deduplication of merely visually similar assets.

The CERN Data Centre and NERSC server racks source pages were reopened; both state CC0 1.0. A further actual NERSC image download attempt failed. External photograph embedding remains open, and no source image has been added. Other unresolved production tests above remain unchanged.

## Follow-up test — composite fallback and semantic slide titles (2026-11-24)

Two attempts to generate standalone images for an independent multi-scene test instead produced multi-panel presentation boards. The first included unverified validation claims; reject those claims and the board as a production deliverable. The second was retained locally as a crop/layout source only. Three 518 × 280 crops from the same 1672 × 941 composite illustrate modularity, vertical scaling, and data flow; they are not independently generated or measured evidence. At 3.92 inches of a 13.333-inch slide, a 1920px display allocates roughly 565px per image (1.09× enlargement). Use such derivatives only at appropriate sizes and preserve source/crop provenance. Independent multi-scene generation remains open.

The local `FRAME_Stage02_Composite_Fallback.pptx` has one slide, 13 native objects including three embedded pictures with descriptions, a nonempty semantic title placeholder, nonempty speaker notes, zero out-of-bounds objects (100 EMU tolerance), and one rendered LibreOffice PDF page. Final rendering and object sequence (title, kicker, intro, each heading/image/interpretation, footer) were inspected. Source archive `FRAME_Stage02_Source.zip` passed ZIP integrity; it contains retained composite, crops, manifest with hashes and coordinates, build script and QA notes. No assets uploaded to GitHub; public distribution clearance not established.

Reinspection of the original ten-slide IMAGE Pilot 02 found zero semantic title placeholders despite visible title text boxes. Prefer actual title placeholders in new decks where feasible and verify intended reading order, while preserving visual quality and existing masters. XML object sequence and alt text presence are useful structural checks but do not establish native PowerPoint Accessibility Checker or screen-reader success. Full accessibility and target-platform checks remain open.
