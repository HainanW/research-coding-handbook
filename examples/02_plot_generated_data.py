"""Regenerate docs/images/01-generated-data.png. Requires NumPy and Matplotlib."""

from pathlib import Path
import runpy

import matplotlib
matplotlib.use("Agg")  # Export directly to a file without opening a GUI window.
import matplotlib.pyplot as plt
import numpy as np


def main():
    # run_path loads the numbered example file without executing its main block.
    example_path = Path(__file__).with_name("01_spyder_function_inspection.py")
    functions = runpy.run_path(str(example_path))
    x_local, y_local = functions["generate_data_local"](10, 4 * 0.03)
    x_global, y_global = functions["generate_data_global"](10, 4 * 0.03)
    x_curve = np.linspace(0.0, 6.0, 300)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), sharex=True, sharey=True)
    panels = [
        ("Local Generator (PCG64)", x_local, y_local, "#2166AC"),
        ("Global RandomState (MT19937)", x_global, y_global, "#B35806"),
    ]
    for ax, (title, x, y, color) in zip(axes, panels):
        ax.plot(x_curve, np.exp(-x_curve / 2.0), color="#303030", lw=1.8,
                label="Noise-free exp(-x / 2)")
        ax.scatter(x[:, 0], y[:, 0], color=color, edgecolors="white",
                   linewidths=0.7, s=48, zorder=3, label="10 noisy observations")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("x")
        ax.set_xlim(-0.1, 6.1)
        ax.grid(alpha=0.2)
        ax.legend(loc="upper right", fontsize=8, frameon=False)
    axes[0].set_ylabel("y")
    fig.suptitle("Same seed = 5; different random streams", fontsize=14)
    fig.text(0.5, 0.01, "Noise standard deviation = 0.12; arrays x and y have shape (10, 1)",
             ha="center", fontsize=9, color="#444444")
    fig.tight_layout(rect=(0, 0.05, 1, 0.93))

    destination = Path(__file__).resolve().parents[1] / "docs" / "images" / "01-generated-data.png"
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, dpi=180, facecolor="white")
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    main()
