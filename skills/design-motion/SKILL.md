---
name: design-motion
description: Teach and test purposeful motion, timing/easing, focus continuity, object reveals, reduced-motion alternatives, and RTL semantics in FRAME technical presentations.
---

# Learn — Motion and Choreography

**Status:** Learning module. No automatic animation requirement for FRAME decks.

## Primary references and their actual scope

- [Material Design 1 — Choreography](https://m1.material.io/motion/choreography.html): continuity, shared focal elements, coordinated creation and avoiding distracting layout shifts.
- [Atlassian — Motion](https://atlassian.design/foundations/motion): purposeful UI motion, clarity/accessibility/performance, duration/easing/property and reduced-motion paths.
- [IBM Carbon — Motion](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview): productive and expressive UI motion and easing.
- [Adobe Spectrum 2 — Motion](https://spectrum.adobe.com/foundations/behavior/motion): purposeful directional meaning, linear/diagonal/clockwise motion and RTL consideration; guidance is **still under development**.
- Full limits: [source catalog](../design-learning/SOURCES.md).

**Critical boundary:** These are mostly **interface-design** systems. Their millisecond tokens and easing curves are not automatically PowerPoint settings or spoken-lecture timing requirements. Material's linked page is legacy Material Design 1.

## When motion is justified

Choose motion only if it helps someone understand a change, a sequence, a dependency or a comparison. Consider a static slide as the default when motion serves no specific teaching objective. Motion cannot repair a weak diagram or incorrect facts.

## The choreography exercise

1. Describe the technical relationship before choosing a visual effect: parallel, sequential, causal, comparative, or merely grouped.
2. Establish a stable anchor and define the focal point.
3. Make a four-frame storyboard: initial context → key relationship → relevant detail → full static result. Do not assume four frames are always required.
4. For truly parallel components (e.g. Q, K and V projections from a common input), reveal them **together** unless a separate narration explicitly clarifies that the reveal order is not computation order.
5. Favor restrained fades or anchored movements over unrelated fly-ins or position jumps.
6. Check direction in Persian/RTL contexts when movement represents forward progress or sequence; don't simply mirror a mathematical/causal arrow.
7. Preserve a final no-motion frame, complete notes and a readable PDF/static alternative.
8. Render/test in the target software. An exported MP4 made by a separate tool does **not** prove PowerPoint object animation works.

## Evaluating timing and easing

Compare a quick, restrained change with a more deliberate one when the learning goal justifies it. Atlassian distinguishes short UI microinteractions and longer UI transitions, and Carbon distinguishes productive from expressive movement. Use these as conceptual contrasts, **not normative slide-duration values**. The pace of explanation and readability of on-screen text take precedence.

## Accessibility and QA

- Does the meaning remain available when animations are off or reduced?
- Does any movement incorrectly imply a dependency?
- Does the focal object stay visually stable enough to track?
- Are transitions free of unnecessary flashing, fast direction changes or distractions?
- Are Persian reading direction and diagram arrows independently correct?
- Is the final explanation inspectable as a static slide?
- Have the PPTX, PDF and video each been tested independently if promised?

## Reference experiment

FRAME Motion Study 01 compared a static Q/K/V illustration with a coordinated reveal: a stable input, parallel Q/K/V branches appearing together, and definitions afterward. The **PowerPoint contained editable storyboard states and slide fades**, whereas a **separate 7.5-second MP4** demonstrated object-level fades. These implementations are not equivalent. No student-learning effect was measured.

## Reporting

State the instructional purpose, storyboard, actual animation technology, static fallback, inspected platforms and known limitations. Only propose a reusable design guideline after the result is reviewed in real presentation conditions.
