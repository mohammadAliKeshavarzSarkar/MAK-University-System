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
