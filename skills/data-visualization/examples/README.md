# Example 01 — One synthetic dataset, multiple visualization libraries

This is a **teaching example**, not the output of a real machine-learning experiment. The CSV contains twelve fixed rows: `epoch`, `train_loss`, `validation_loss`. The lowest validation loss is **0.49 at epoch 7**, while training loss continues to decrease.

## Run

```bash
python -m pip install pandas matplotlib plotly altair
# Optional for static Plotly / Altair export:
python -m pip install kaleido vl-convert-python
python compare-learning-curves.py
```

The script handles plotting libraries independently. With the packages available, it creates:

- **Matplotlib:** static PNG + SVG for slides, print or scientific reports.
- **Plotly:** self-contained interactive HTML + JSON figure specification; optional PNG requires Kaleido/Chrome.
- **Altair:** HTML + Vega-Lite JSON, optional SVG requires export capability.

Check actual output before promising a requested format. The same fixed source CSV and comparable axes are used. The visual styles and interaction modes differ; results are not claims of usability improvements.

## Learning tasks

1. Identify exactly what the graph is saying, then independently check the minimum validation value from the CSV.
2. Compare readability, hover/tooltips, legends, markers, annotation and the final rendering.
3. Explain why exporting as SVG or PNG is not the same as a native editable PowerPoint data chart.
4. Improve one design variable while holding **data and axis domains constant**.
5. If a module is missing, document the limitation rather than fabricating the missing image.

## Context and accessibility

The palette uses MAK Paper/Ink/Signal. Training loss is dark solid with circles; validation loss is red dashed with squares. Both axes are labeled; the caption identifies the data as synthetic. A mathematical minimum is shown but not treated as proof of real model performance.

The current session could execute the Matplotlib and Plotly HTML paths. It could not import Altair or Kaleido, and network-restricted package installation did not succeed. The complete local demonstration script is more detailed than this repository's compact example.
