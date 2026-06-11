#!/usr/bin/env python3
"""
generate_timeline.py
--------------------
Renders a Gantt-style portfolio timeline from timeline.json.

Usage:
    python generate_timeline.py                  # reads timeline.json, writes timeline.png
    python generate_timeline.py --data foo.json --out bar.png

To change the timeline, edit timeline.json (add/remove/edit entries) and re-run.
You never need to touch this script to update the chart.

Each entry needs: name, start ("YYYY-MM"), end ("YYYY-MM"), category.
'org' is optional and shown in parentheses after the name.
Categories and their colors/labels are defined in the "categories" block of the JSON.

Requires: matplotlib  (pip install matplotlib)
"""

import argparse
import json
import sys
from datetime import date


def parse_ym(value):
    """Parse a 'YYYY-MM' string into a (year, month) -> fractional-year float.

    The end month is treated as the END of that month, so a project running
    04/2025 - 08/2025 spans the full width of April through August (5 months).
    """
    try:
        year, month = (int(p) for p in value.split("-"))
    except (ValueError, AttributeError):
        raise SystemExit(f"Bad date '{value}'. Expected format 'YYYY-MM'.")
    return year, month


def ym_to_float(year, month, end=False):
    """Convert (year, month) to a float on a continuous year axis.

    month 1 (Jan) starts at year + 0.0. With end=True we move to the end of the
    month so a single-month item still has visible width and durations read
    inclusively.
    """
    base = year + (month - 1) / 12.0
    return base + (1 / 12.0 if end else 0.0)


def months_between(start_ym, end_ym):
    """Inclusive month count between two (year, month) tuples."""
    (sy, sm), (ey, em) = start_ym, end_ym
    return (ey - sy) * 12 + (em - sm) + 1


def load_data(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise SystemExit(f"Data file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"timeline JSON is invalid: {exc}")


def render(data, out_path):
    # Import here so a missing matplotlib gives a clean message, not a stack trace.
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import Patch
    except ImportError:
        raise SystemExit("matplotlib is required. Install with: pip install matplotlib")

    categories = data.get("categories", {})
    entries = data.get("entries", [])
    if not entries:
        raise SystemExit("No entries found in the data file.")

    # Draw earliest-start at the top: reverse-sort so first row sits highest.
    entries = sorted(entries, key=lambda e: parse_ym(e["start"]))

    fig_height = max(3.5, 0.62 * len(entries) + 2.2)
    fig, ax = plt.subplots(figsize=(14, fig_height))

    bar_height = 0.58
    earliest = min(parse_ym(e["start"]) for e in entries)
    latest = max(parse_ym(e["end"]) for e in entries)
    span = ym_to_float(*latest, end=True) - ym_to_float(*earliest)
    # Reserve room on the left for project-name labels (~42% of the time span),
    # and a little on the right for the month-count annotations.
    label_pad = max(span * 0.42, 2.4)
    axis_min = ym_to_float(*earliest) - label_pad
    axis_max = ym_to_float(*latest, end=True) + span * 0.10 + 0.3

    used_categories = []
    for row, entry in enumerate(entries):
        y = len(entries) - 1 - row  # top-down
        start_ym = parse_ym(entry["start"])
        end_ym = parse_ym(entry["end"])
        x0 = ym_to_float(*start_ym)
        x1 = ym_to_float(*end_ym, end=True)
        width = x1 - x0

        cat_key = entry.get("category", "pmp")
        cat = categories.get(cat_key, {})
        color = cat.get("color", "#2563eb")
        if cat_key not in used_categories:
            used_categories.append(cat_key)

        ax.barh(
            y,
            width,
            left=x0,
            height=bar_height,
            color=color,
            edgecolor="white",
            linewidth=1.2,
            zorder=3,
        )

        months = months_between(start_ym, end_ym)
        ax.text(
            x1 + 0.06,
            y,
            f"{months} mo",
            va="center",
            ha="left",
            fontsize=8.5,
            color="#6b7280",
            zorder=4,
        )

        label = entry["name"]
        if entry.get("org"):
            label = f"{label}  ({entry['org']})"
        # Name sits in the reserved left margin, right-aligned up to the axis edge.
        ax.text(
            axis_min + label_pad - 0.12,
            y,
            label,
            va="center",
            ha="right",
            fontsize=9.5,
            color="#111827",
            fontweight="bold",
            zorder=4,
        )

    # Year gridlines, only across the bar area (not the label margin)
    plot_start = ym_to_float(*earliest)
    first_year = int(plot_start)
    if first_year < plot_start:
        first_year += 1
    last_year = int(axis_max) + 1
    for yr in range(first_year, last_year + 1):
        ax.axvline(yr, color="#e5e7eb", linewidth=1, zorder=1)

    ax.set_xlim(axis_min, axis_max)
    ax.set_ylim(-0.7, len(entries) - 0.3)
    ax.set_yticks([])
    year_ticks = list(range(first_year, last_year + 1))
    ax.set_xticks(year_ticks)
    ax.set_xticklabels([str(y) for y in year_ticks], fontsize=10)
    ax.tick_params(axis="x", length=0)

    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#d1d5db")

    title = data.get("title", "Portfolio Timeline")
    subtitle = data.get("subtitle")
    ax.set_title(title, fontsize=15, fontweight="bold", color="#111827", pad=18, loc="left")
    if subtitle:
        ax.text(
            0.0,
            1.02,
            subtitle,
            transform=ax.transAxes,
            fontsize=10,
            color="#6b7280",
            ha="left",
            va="bottom",
        )

    # Legend, only for categories actually used, in JSON order
    legend_handles = []
    for cat_key in categories:
        if cat_key in used_categories:
            cat = categories[cat_key]
            legend_handles.append(
                Patch(facecolor=cat.get("color", "#2563eb"), label=cat.get("label", cat_key))
            )
    if legend_handles:
        ax.legend(
            handles=legend_handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.08),
            ncol=1,
            frameon=False,
            fontsize=9,
        )

    footer = date.today().strftime("Generated %Y-%m-%d from timeline.json")
    fig.text(0.99, 0.01, footer, ha="right", va="bottom", fontsize=7.5, color="#9ca3af")

    fig.tight_layout(rect=[0, 0.02, 1, 1])
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"Wrote {out_path}  ({len(entries)} entries)")


def main():
    parser = argparse.ArgumentParser(description="Render a portfolio timeline from JSON.")
    parser.add_argument("--data", default="timeline.json", help="Path to the JSON data file.")
    parser.add_argument("--out", default="timeline.png", help="Output image path.")
    args = parser.parse_args()

    data = load_data(args.data)
    render(data, args.out)


if __name__ == "__main__":
    main()