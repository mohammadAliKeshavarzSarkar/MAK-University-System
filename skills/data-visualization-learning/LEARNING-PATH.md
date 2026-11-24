# FRAME Data Visualization — Learning Path (Studies 01–12)

**Scope:** Twelve completed hands-on lessons, with synthetic, self-contained teaching cases. **Not** twelve independent installed skills. Use [the Learning Lab facilitator](SKILL.md) and [source evidence](EVIDENCE.md) to guide work; use [data-visualization production](../data-visualization/SKILL.md) when making real deliverables.

These lessons progress from **chart craft → statistical evaluation → model explanation → intervention robustness and monitoring**. The source packages are held in the original conversation/project environment, **not** committed as binaries to this public repository. Exact numerical claims should be verified from their source package when needed.

## Phase A — Visualize data and communicate uncertainty

### 01 — Visualization libraries and learning curves

- **Question:** How can the same data be expressed as a static scientific figure and as an interactive chart?
- **Exercise:** Twelve synthetic training/validation loss epochs; Matplotlib PNG/SVG, Plotly interactive HTML/JSON, and an optional Altair declarative path. The illustrative validation minimum is 0.49 at epoch 7.
- **Skills:** Define the data and axis domains once; compare tooltip value, static rendering, editable output and source reproducibility.
- **Avoid:** Calling a Plotly browser screenshot a native vector export; asserting Altair or Kaleido ran when they were not installed; interpreting fabricated loss curves as evidence of real overfitting.
- **Check yourself:** Which file would you deliver for a static slide versus interactive browser demo? How would a lecturer modify the data?

### 02 — Choosing the chart by the question

- **Question:** Which chart communicates magnitude, raw variability, mean/SD, or error types?
- **Exercise:** Three fictional models, six latency values per model; bar, dot and mean±sample-SD views; a separate binary confusion matrix.
- **Skills:** Zero baseline for magnitude bars, individual observations for small samples, named error bars, accurate positive-class metric definitions.
- **Avoid:** Calling SD a CI or treating accuracy alone as a sufficient classifier summary.
- **Check yourself:** Why should the same six latency observations be shown differently for different analytic questions?

### 03 — Distributions, outliers and three uncertainty concepts

- **Question:** How can the mean hide unusual values and why are SD, CI and PI not interchangeable?
- **Exercise:** Sixteen synthetic latencies per model, including Model B's 151 ms flagged observation. Compare distributions; demonstrate 1.5×IQR flagging, sample SD, a t interval for the mean and a t prediction interval for one new observation.
- **Skills:** Outlier investigation without automatic deletion; distribution-first reporting; explicit independent, approximately normal sampling assumptions for intervals.
- **Avoid:** Treating an outlier flag as proof of bad data, or treating a 95% confidence interval as a 95% probability for a fixed parameter.
- **Check yourself:** Why is the new-observation prediction interval wider than the mean confidence interval?

### 04 — Matched comparisons and paired benchmarking

- **Question:** What do we learn by pairing each baseline result with the corresponding variant result?
- **Exercise:** Twelve synthetic matched workload batches, with differences `d=A−B`; paired lines, zero-centered difference plot and a t interval for mean paired improvement (7.58 ms; illustrative interval 4.99–10.17 ms).
- **Skills:** Define the experimental unit and subtraction direction; analyze within-pair differences; disclose independence/normality assumptions.
- **Avoid:** Treating paired observations as independent groups; offering a CI as an SLA prediction.
- **Check yourself:** Why can a paired plot reveal consistency that two aggregate bars conceal?

### 05 — Reliable benchmarking and practical importance

- **Question:** When is a statistically detectable effect too small to matter, and when is a larger effect too uncertain to claim?
- **Exercise:** Two synthetic matched-run scenarios: 20 pairs give a precise mean change of 1.32 ms; 10 noisy pairs give an estimated 6.90 ms with an interval crossing zero. The hypothetical engineering threshold is 5 ms.
- **Skills:** Report effect size, CI, p-value, repeated-run design and **predeclared practical threshold** together.
- **Avoid:** “p < 0.05 means useful,” “p > 0.05 means no effect,” dependent pseudo-repetitions, or retrofitting a requirement to the observed result.
- **Check yourself:** What can you conclude about a positive effect, and separately about a 5 ms improvement?

## Phase B — Evaluate model behavior and explain predictions

### 06 — Multiple datasets, subgroups and metrics

- **Question:** Why can a pooled leaderboard reverse when rare subsets or deployment mixtures matter?
- **Exercise:** A synthetic 1,000-case binary evaluation over Routine, Challenging and Rare-event slices: pooled accuracy 90.5% versus 90.4%, but rare-event accuracy 50% versus 80%. Compare equal-slice accuracy, precision/recall/F1 and a reweighted target mix.
- **Skills:** Report slice sizes and class supports; distinguish pooled accuracy, equal-slice averaging and *macro-F1*; specify a target mix and stable-within-slice assumptions.
- **Avoid:** Selecting a winner from pooled accuracy alone or describing a simulated reweighting as a validated deployment forecast.
- **Check yourself:** Which model is preferable when false negatives are more costly, and which further evidence is missing?

### 07 — Probability calibration and decisions

- **Question:** Can two scores rank cases identically but have different probability quality? What threshold minimizes a declared decision cost?
- **Exercise:** 3,600 generated binary cases with reference/oracle probabilities and a monotone overconfident transform. ROC-AUC and 0.5 accuracy match; Brier scores differ. Compare reliability diagrams and a hypothetical false-positive cost 1 versus false-negative cost 4, validation-selected threshold 0.25 and cost-based 0.20.
- **Skills:** Distinguish discrimination, probability quality and downstream decisions; fit/tune on validation only; report test performance after threshold selection.
- **Avoid:** Describing Brier as pure calibration, using test labels to tune the policy, or assuming the theoretical threshold is reliable with miscalibrated scores.
- **Check yourself:** Why can accuracy decrease while the chosen total decision cost improves?

### 08 — Global importance, local SHAP and correlated inputs

- **Question:** Why can correlated features yield misleadingly small individual permutation effects?
- **Exercise:** A synthetic 950-row latency regression with a strongly correlated complexity/proxy pair (r≈0.987). Compare individual versus grouped held-out R² permutation decreases; compute local TreeSHAP feature contributions relative to a specified 100-row reference.
- **Skills:** Specify metric, data split, shuffle definition, SHAP output and background; check attribution additivity to the prediction.
- **Avoid:** Adding permutation decreases as if they were a decomposition; interpreting SHAP `interventional` as an observed causal intervention.
- **Check yourself:** What evidence does model attribution provide, and what causal claim does it not establish?

### 09 — Explanation stability across analytical choices

- **Question:** What remains constant, and what changes, when we vary only the model, SHAP background or evaluated population?
- **Exercise:** Reuse Study 08's 950 synthetic rows. For the same case and model, contrast representative, deliberately low-complexity and deliberately high-complexity backgrounds: baselines ~121.26, 90.92 and 149.50 ms, all reconstructing the same 97.16 ms prediction. Compare an alternative fitted forest and two selected case cohorts.
- **Skills:** One-factor-at-a-time sensitivity analysis; report background selection, model parameters, explained population and uncertainty about importance rankings.
- **Avoid:** Treating extreme sensitivity-test backgrounds as sensible deployment references or equating explanation stability with causality.
- **Check yourself:** Why might an explanation change when the model's prediction does not?

## Phase C — Counterfactuals, robustness and monitoring

### 10 — Counterfactual recourse and feasible actions

- **Question:** Can a simple feature edit flip a prediction while violating real constraints?
- **Exercise:** Toy service: replicas R, cache C, derived capacity proxy `K=30R+30C`, fixed traffic 145, model score `sigmoid((K−T)/10)`, target 0.60 and cost budget 7. Directly editing capacity is forbidden; R4/cache-on crosses at cost 6, but fails when assumed cache gain is reduced.
- **Skills:** Separate mutable, immutable and derived inputs; enforce feasibility and budget; test structural assumptions before claiming actionability.
- **Avoid:** Calling a synthetic score a calibrated SLA probability or assuming a feature-edit counterfactual would work as a real intervention.
- **Check yourself:** Which input changes are valid actions versus mathematical shortcuts?

### 11 — Robust counterfactuals under uncertainty

- **Question:** Does a nominally successful action still pass under a bounded model/environment scenario grid?
- **Exercise:** Extend Study 10 to `score=sigmoid((R*u+C*g−T)/k)` over 3×3×3×3=81 hypothetical parameter settings. Under seven-unit budget no configuration passes all 81; six replicas without cache passes all tested cases at invented cost 12.
- **Skills:** Distinguish nominal score, worst-case score, finite-scenario coverage, cost trade-off and real-world/probabilistic robustness.
- **Avoid:** Calling 81/81 synthetic scenario passes “100% reliable” or treating unspecified uncertainty bounds as validated field conditions.
- **Check yourself:** What would need to be validated before we can trust the uncertainty range?

### 12 — Validate assumptions and monitor post-intervention outcomes

- **Question:** How can monitoring challenge earlier robustness assumptions, and what does missing telemetry mean?
- **Exercise:** Revisit Study 11 and generate 96 synthetic monitoring windows across Baseline, Canary, Rollout and Stress phases. Keep an invented per-window p95 objective ≤120 ms; distinguish observed breaches, unavailable p95 values and traffic outside the earlier finite-grid range. Stress has 18/21 observed breaches and 3 missing p95 windows.
- **Skills:** Separate input-range coverage, outcome monitoring, telemetry completeness and alert policy. Disclose that p95-like values are **directly simulated summaries**, not computed from request-level latency.
- **Avoid:** Equating a toy model score with measured p95 latency, interpreting missing results as passes, or inferring a causal rollout effect from unrandomized before/after phases.
- **Check yourself:** Which alert requires investigation, what evidence is missing, and what would a stronger evaluation design collect?

## Suggested lesson structure

Use **understanding → prediction → reveal → method critique → one-variable practice → review**. Avoid memorizing exact synthetic numbers; use them to verify method. An effective assessment asks the learner to spot the invalid inference and redesign a more defensible chart or experiment.

## Current boundary / next step

**Completed: 01–12.** **Proposed next (not yet completed): 13 — Data Drift and Change Detection**, including covariate drift, label/concept shift, detection windows and noisy false alerts. Add it here only after source material, exercise results, and quality checks are available.

The exercises are original FRAME learning material. Preserve the evidence and precise limitations recorded in the [evidence register](EVIDENCE.md) rather than inventing research outcomes or silently adopting their provisional design choices as FRAME production standards.
