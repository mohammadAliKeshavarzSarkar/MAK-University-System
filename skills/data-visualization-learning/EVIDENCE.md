# FRAME DataViz Studies 01–12 — Exercise Evidence and Boundaries

**Provenance checked:** 2026-11-24. This register was prepared by **reopening the `README.md` within each of the twelve user-supplied study source ZIPs**, and the Study 12 accompanying QA review. It preserves the exercises' stated limitations. It is a navigation document, **not** an independent rerun of all twelve experiments in this PR.

## Where to find the original evidence

The following filenames identify artifacts from the user's existing FRAME conversation/project files. **They are not stored in this public GitHub repository**, and the names do not imply GitHub or public download access. To inspect or rerun, retrieve the exact archive from the user/session or an approved storage location and inspect its README and scripts.

| Study | Source package filename | Core methodological artifact |
| ---: | --- | --- |
| 01 | `FRAME_DataViz_Study_01_Reproducible_Example.zip` | `synthetic-learning-curves.csv`; library comparison script; Matplotlib/Plotly outputs; Altair path untested in original runtime |
| 02 | `FRAME_DataViz_Study_02_Source_And_Charts.zip` | `synthetic_model_latency_runs.csv`, `synthetic_confusion_matrix.csv`; chart-selection comparison |
| 03 | `FRAME_DataViz_Study_03_Source_And_Charts.zip` | `synthetic_runtime_observations.csv`; distributions/SD/CI/PI formulas |
| 04 | `FRAME_DataViz_Study_04_Source_And_Charts.zip` | `synthetic_paired_benchmark.csv`; positive paired difference `A−B` |
| 05 | `FRAME_DataViz_Study_05_Source_And_Charts.zip` | `source/reproduce_benchmarks.py`; synthetic paired significance/practical threshold cases |
| 06 | `FRAME_DataViz_Study_06_Source_And_Charts.zip` | `synthetic_multidataset_predictions.csv`; pooled/subset confusion counts |
| 07 | `FRAME_DataViz_Study_07_Source_And_Charts.zip` | `synthetic_classifier_probabilities.csv`; validation vs test split; Brier/ROC-AUC/decision costs |
| 08 | `FRAME_DataViz_Study_08_Source_And_Charts.zip` | `synthetic_inference_latency.csv`; permutation and SHAP analysis with background selection |
| 09 | `FRAME_DataViz_Study_09_Source_And_Charts.zip` | Reused Study 08 synthetic latency data; SHAP/background/model/cohort sensitivity |
| 10 | `FRAME_DataViz_Study_10_Source_And_Charts.zip` | `synthetic_counterfactual_action_grid.csv`; toy structural equations and constrained action search |
| 11 | `FRAME_DataViz_Study_11_Source_And_Charts.zip` | `synthetic_uncertainty_scenarios.csv`, `synthetic_robust_recourse_grid.csv`; finite 81-case grid |
| 12 | `FRAME_DataViz_Study_12_Source_And_Charts.zip` | `synthetic_monitoring_windows.csv`, `synthetic_monitoring_summary.csv`; simulated monitoring phases |

Individual source ZIPs also include some combination of source scripts, verified JSON, chart exports, local README, and in many cases the source to rebuild a PPTX. The delivered `.pptx`, `.pdf`, contact sheet and QA review may exist separately. Archive folder structure and dependencies **differ** between studies: follow the specific README, rather than assuming one universal rebuild command.

**Privacy and rights:** Some private teaching archives include a reproduction copy of the user's original MAK brand logo. **Do not commit, republish or redistribute it in this public GitHub repository without approval.** Do not add course records, private research data, nonlicensed source assets or font binaries.

## Essential scientific qualification

Every numerical outcome in this set is **synthetic, simulated, or constructed for a lesson**. None establishes measured production AI performance, causal effectiveness of an intervention, educational benefit to students, or reliability of a real deployment. Details below are **reported by the exercise sources** and should be recalculated when reused in a new artifact.

### Core concept boundaries

1. **Plotting vs data:** A library example or polished figure does not establish a finding; raw data and computation remain authoritative.
2. **Spread vs inference:** Sample SD, t confidence intervals for a mean, and prediction intervals for a new observation answer different questions under stated assumptions.
3. **Benchmarking:** Matched pairs and true experimental units matter; repeated observations can be dependent; statistical detectability is distinct from operational value.
4. **Aggregated model metrics:** Pooled, equal-slice and reweighted metrics encode different population and importance assumptions. Equal-slice accuracy is not macro-F1.
5. **Calibration:** ROC-AUC summarizes ranking; a reliability diagram evaluates frequency agreement; Brier is a proper probability score, **not a pure calibration metric**. Threshold selection belongs to validation/decision analysis, not test tuning.
6. **Interpretability:** Permutation importance is performance- and data-dependent; correlated inputs can hide importance. SHAP explanations vary with model, background and explained population, and do not alone justify interventions.
7. **Recourse:** A toy score flip is not a causal action, and a feasible action within an invented budget is not proof of real-world effect.
8. **Robustness:** The 81 stipulated scenarios were a **finite grid without a probability distribution**, so 81/81 is not 100% field reliability.
9. **Monitoring:** Study 11's uncalibrated score has no validated mapping to Study 12's directly simulated p95-like values. The 96 windows are *not* raw request-level percentile calculations, matched observations, or a causal rollout experiment. Missing measurements are not passes.

### Selected numerical audit anchors — synthetic only

- **01:** 12 epochs; validation-loss minimum `0.49` at epoch 7; Altair and Kaleido were unavailable in the original execution environment.
- **02:** six runs/model; latency means `142, 113, 94 ms`; separate confusion matrix `TN=65, FP=10, FN=7, TP=18`.
- **03:** 16 values/model; B's 151 ms observation is flagged by the selected 1.5×IQR rule; Model A's illustrative mean t CI `91.90–94.35 ms` and single-new-observation PI `88.06–98.19 ms`.
- **04:** 12 matched pairs; `d=A−B`, mean `7.5833 ms`, illustrative 95% paired t interval `4.9924–10.1743 ms`.
- **05:** two synthetic scenarios, S `n=20`, estimated improvement `1.32 ms`; N `n=10`, `6.90 ms` with CI including zero; illustrative practical threshold `5 ms`.
- **06:** 1,000 constructed classification cases; pooled accuracies `90.5%` vs `90.4%`, rare-event accuracies `50%` vs `80%`. The reweighted mix is a *thought experiment*.
- **07:** 3,600 generated cases; ranking-preserving score transformation keeps ROC-AUC, changes Brier. Invented FP:FN cost ratio `1:4`, theoretical cutoff 0.20, validation-selected cutoff 0.25.
- **08:** 950 synthetic regression rows; complexity/proxy correlation `r≈0.987`; grouped versus individual permutation importance and local SHAP additivity checked.
- **09:** Same model and case predicted `97.16 ms`; deliberately shifted SHAP reference backgrounds move baseline from `90.92` to `149.50 ms` relative to representative baseline `121.26 ms`.
- **10:** Derived capacity `K=30R+30C`, toy score target 0.60; `R4,C1` crosses nominally at invented cost 6 but fails under smaller assumed cache effect.
- **11:** `3×3×3×3=81` hypothetical parameter combinations; no action is finite-grid robust within seven cost units; `R6,C0` costs 12 and passes this finite grid.
- **12:** 96 synthetic monitoring windows; 93 have p95-like values, three missing in stress. Stress exceeds 120 ms in `18/21` observed windows; the SLO threshold is invented and percentile summaries are *directly simulated*.

## Reuse checklist

- Locate actual ZIP / README / generated source; record version, date, package origin, and whether dependencies can run in the **current** environment.
- Recompute any adopted example figures from CSV and code. Verify sign conventions, confusion-matrix orientation, intervals, thresholds, metric denominators and subgroup support.
- Cite the method's primary documentation **separately** from the invented exercise data. Use [five visualization library references](../data-visualization/SOURCES.md) for tool selection and each original study README's research links for method specifics.
- For an editable presentation, verify the actual shape/chart semantics, speaker notes, final PDF and font substitution. Native PPTX shapes are not automatically spreadsheet-backed native chart objects.
- If original files cannot be retrieved, do not invent missing methods, claim independent replay, fabricate results or label “verified.”
- Before adopting a lesson as a permanent FRAME standard, obtain user review and a separate small PR.

**Current curriculum state:** Completed Studies **01–12**. Suggested Study **13 (Data Drift and Change Detection)** remains **proposed**, not completed.
