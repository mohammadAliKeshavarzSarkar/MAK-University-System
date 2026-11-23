#!/usr/bin/env python3
"""FRAME sample: same *synthetic* data in Matplotlib, Plotly and Altair."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "generated"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / "synthetic-learning-curves.csv")
assert df.columns.tolist() == ["epoch", "train_loss", "validation_loss"]
assert df.epoch.tolist() == list(range(1, 13))
assert not df.isna().any().any()
assert df[["train_loss", "validation_loss"]].ge(0).all().all()
assert df[["train_loss", "validation_loss"]].le(1.1).all().all()
minimum = int(df.loc[df.validation_loss.idxmin(), "epoch"])
assert minimum == 7
PAPER, INK, SIGNAL = "#F5F3EE", "#161616", "#E64B3C"
print("Fixed SYNTHETIC data: validation minimum =", df.validation_loss.min(),
      "at epoch", minimum)

# Matplotlib: static lecture/research graphic.
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.plot(df.epoch, df.train_loss, color=INK, marker="o", label="Training")
    ax.plot(df.epoch, df.validation_loss, color=SIGNAL, marker="s",
            linestyle="--", label="Validation")
    ax.axvline(minimum, color="#777777", linestyle=":")
    ax.set(xlim=(1, 12), ylim=(0, 1.1), xlabel="Epoch",
           ylabel="Loss (illustrative units)",
           title="Training and validation loss — synthetic example")
    ax.grid(axis="y", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "matplotlib.png", dpi=200)
    fig.savefig(OUT / "matplotlib.svg")
    plt.close(fig)
    print("Matplotlib: PNG/SVG created")
except ImportError as exc:
    print("Matplotlib unavailable:", exc)

# Plotly: interactive standalone HTML.
try:
    import plotly.graph_objects as go
    fig = go.Figure()
    for column, name, color, dash, marker in [
        ("train_loss", "Training", INK, "solid", "circle"),
        ("validation_loss", "Validation", SIGNAL, "dash", "square")
    ]:
        fig.add_trace(go.Scatter(x=df.epoch, y=df[column],
            mode="lines+markers", name=name,
            line=dict(color=color, dash=dash, width=3),
            marker=dict(symbol=marker, size=9)))
    fig.update_layout(title="Training and validation loss — synthetic example",
        paper_bgcolor=PAPER, plot_bgcolor=PAPER,
        xaxis=dict(title="Epoch", range=[1, 12], dtick=1),
        yaxis=dict(title="Loss (illustrative units)", range=[0, 1.1]))
    fig.write_html(str(OUT / "plotly.html"), include_plotlyjs=True)
    (OUT / "plotly.json").write_text(fig.to_json(), encoding="utf-8")
    try:
        import kaleido  # optional static image support
        fig.write_image(str(OUT / "plotly.png"))
    except (ImportError, ValueError, RuntimeError) as exc:
        print("Plotly PNG export unavailable:", str(exc)[:100])
    print("Plotly: interactive HTML/JSON created")
except ImportError as exc:
    print("Plotly unavailable:", exc)

# Vega-Altair: declarative representation; requires Altair installed.
try:
    import altair as alt
    long = df.melt("epoch", var_name="series", value_name="loss")
    long["series"] = long.series.replace({
        "train_loss": "Training", "validation_loss": "Validation"})
    chart = (alt.Chart(long).mark_line(point=True)
        .encode(
            x=alt.X("epoch:Q", title="Epoch", scale=alt.Scale(domain=[1, 12])),
            y=alt.Y("loss:Q", title="Loss (illustrative units)",
                scale=alt.Scale(domain=[0, 1.1])),
            color=alt.Color("series:N", scale=alt.Scale(
                domain=["Training", "Validation"], range=[INK, SIGNAL])),
            strokeDash="series:N", tooltip=["epoch:Q", "series:N", "loss:Q"])
        .properties(title="Training and validation loss — synthetic example",
                    width=800, height=460))
    chart.save(str(OUT / "altair.html"))
    chart.save(str(OUT / "altair.json"))
    print("Altair: HTML/JSON created")
except ImportError as exc:
    print("Altair unavailable (install separately):", exc)
