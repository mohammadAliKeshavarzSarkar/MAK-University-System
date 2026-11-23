# MAK University System — Iconography Standard

**Status:** Lucide chosen by the user as the official **default icon source** (2026-11-23). This is an adaptable visual standard, not an exclusivity rule.  
**Applies to:** FRAME presentations and other university workflows when icons are useful.

## Choice order

1. **Lucide — first-choice library:** General educational topics, actions, navigation, documents, data, programming, diagrams' legend symbols, and small conceptual markers.
2. **Original custom-drawn icons — equally valid when justified:** Domain-specific concepts, mathematics, AI mechanisms, unusual diagrams, research topics, or visual storytelling that Lucide cannot express accurately.
3. **Complete technical diagrams — often better than icons:** Show relationships using labeled shapes, edges, equations, and data. Do not substitute decorative iconography for a truthful architecture.

**Priority is semantic precision, then consistency, then decoration.** A custom icon can replace a Lucide icon if it improves the explanation without introducing visual inconsistency. Do not require a Lucide icon on every slide.

## Visual direction (working defaults)

- Prefer Lucide's **outline** style. Upstream files typically use a `24 × 24` viewBox, `stroke-width="2"`, `fill="none"`, and rounded cap/join. Preserve the core geometry.
- Choose a size that reads in context. For projected slides, start around **24–40 px-equivalent** for ordinary conceptual markers; evaluate at full-slide viewing scale. For tiny labels or bigger hero icons, adjust case by case rather than enforcing one rigid pixel size.
- Use **Ink `#161616`** as the normal icon color on Paper `#F5F3EE`, and **Signal `#E64B3C`** sparingly when highlighting a genuine action, concept, or selected state. Respect contrast; avoid using a red thin-stroke icon as the only carrier of crucial meaning.
- Keep a consistent stroke weight and optical size on one slide. Avoid mixing outlined Lucide with filled multicolor glyphs without a clear reason.
- Maintain whitespace around icons; never distort, add unnecessary shadows, or crowd essential text.
- Icons supplement labels and accessible textual descriptions. Do not rely on icon shape or color alone to communicate essential information.
- For English/Persian bilingual layouts, test surrounding text order and reading direction independently of icon placement.
- Avoid using icons as research figures, evidence, or quantitative charts. Use labeled native diagrams/charts instead.
- Do not use Lucide symbols to redraw or modify the official MAK monogram or approved logo lock-ups.

## Current curated SVG starter set

| SVG filename | Typical use |
| --- | --- |
| `book-open.svg` | Lessons, knowledge, reference materials |
| `brain-circuit.svg` | AI-related section marker — **not** an algorithm diagram |
| `database.svg` | Data storage, data-driven components |
| `network.svg` | Connected systems and architecture section marker |
| `chart-no-axes-combined.svg` | Data analysis and analytics heading |
| `presentation.svg` | Slides, presenting and communication |

Files are sourced **unchanged** from the official Lucide GitHub repository and kept in [`assets/icons/lucide/`](../assets/icons/lucide/). The full package is *not vendored*, so this repository remains small. Browse additional icons at https://lucide.dev/icons/ and use the official `lucide-static` package if needed in a web project:

```bash
npm install lucide-static
```

For PowerPoint: insert an individual SVG when supported and inspect the rendered PPTX/PDF, because SVG import and export can vary by presentation software. Use a high-quality derived PNG fallback when necessary, but retain the SVG as the original vector reference.

## Custom icons

Original custom icons are **officially allowed**; they do not need to imitate Lucide exactly. When possible:

- Reuse the same overall stroke/spacing rhythm and simple geometric language.
- Give an icon a descriptive kebab-case name and a clear concept definition.
- Include source/author and permission details when incorporating third-party material.
- Store genuinely reusable approved icons under `assets/icons/custom/` when examples justify that folder; don't create placeholders in advance.
- Review custom icon legibility in both light and dark modes, on classroom projection, and with adjacent Persian and English labels.

## Source and licensing

- Official icon catalog: https://lucide.dev/icons/
- Official static package: https://lucide.dev/guide/static
- Official project repository: https://github.com/lucide-icons/lucide
- License information: https://lucide.dev/license
- The upstream Lucide repository states an **ISC** license, with an **MIT** notice applying to the identified Feather-derived icons. Preserve the applicable notices when storing or redistributing SVGs.
- The unmodified license text for the curated copy is retained at [`assets/icons/lucide/LICENSE-LUCIDE.txt`](../assets/icons/lucide/LICENSE-LUCIDE.txt).

## Governance

This source library is an approved **default**, not an automatic installation of Lucide into every app. Agents should use the repository's actual SVG assets or fetch an icon from the official source as the toolchain permits. Do not claim the entire Lucide package is stored locally. Add icons to this repo only when there is a demonstrated reusable need; otherwise link to the upstream source.
