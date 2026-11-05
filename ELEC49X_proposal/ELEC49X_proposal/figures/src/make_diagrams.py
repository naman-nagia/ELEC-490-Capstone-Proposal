"""Generate the blueprint's vector diagrams (PDF) into the figures/ folder.

Usage: python figures/src/make_diagrams.py
Requires matplotlib. Edit a box label or arrow here and re-run to update a figure.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent
INK, MUTED, NAVY, DATA, RED, GOLD = "#1f1f1e", "#5f5e58", "#0E2841", "#ecebe5", "#9d1939", "#fff2cc"
plt.rcParams.update({"font.family": ["Arial", "Helvetica", "DejaVu Sans"], "pdf.fonttype": 42})


class Canvas:
    def __init__(self, w, h, xmax=100, ymax=60):
        self.fig, self.ax = plt.subplots(figsize=(w, h))
        self.ax.set_xlim(0, xmax)
        self.ax.set_ylim(0, ymax)
        self.ax.axis("off")

    def box(self, x, y, text, w=13.5, h=8.0, edge=NAVY, fill="white", fs=6.8, color=INK, lw=1.0, ls="-", weight="normal"):
        self.ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.15,rounding_size=0.7",
                                         lw=lw, ec=edge, fc=fill, ls=ls))
        self.ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=color, linespacing=1.15, weight=weight)
        return dict(x=x, y=y, w=w, h=h)

    def arrow(self, p, q, label=None, lx=0.0, ly=0.9, color=MUTED, fs=6.2, ls="-", rad=0.0, lc=None, style=None):
        conn = style or f"arc3,rad={rad}"
        self.ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=7, lw=0.9, color=color, ls=ls,
                                          shrinkA=0, shrinkB=0, connectionstyle=conn))
        if label:
            self.ax.text((p[0] + q[0]) / 2 + lx, (p[1] + q[1]) / 2 + ly, label, ha="center", va="center",
                         fontsize=fs, color=lc or color, style="italic")

    def save(self, name):
        self.fig.tight_layout(pad=0.1)
        self.fig.savefig(OUT / f"{name}.pdf")
        plt.close(self.fig)


def R(b): return (b["x"] + b["w"] / 2 + 0.2, b["y"])
def L(b): return (b["x"] - b["w"] / 2 - 0.2, b["y"])
def T(b): return (b["x"], b["y"] + b["h"] / 2 + 0.2)
def B(b): return (b["x"], b["y"] - b["h"] / 2 - 0.2)


def pipeline():
    c = Canvas(7.0, 2.25, ymax=33)
    ys, yl = 22.5, 6
    xs = [23, 40, 57, 74, 91]
    e1 = c.box(6.5, ys, "GitSkills\nsnapshot (E1)", w=11, h=7, edge=MUTED, fill=DATA)
    fs = [c.box(x, ys, t, w=13, h=7.5) for x, t in zip(xs, [
        "F1\nIngest tables", "F2\nPrepare records", "F3\nCalculate metrics\n(F3.1 to F3.5)",
        "F4\nIntegrate results", "F5\nAnalyze, plot"])]
    ls = [c.box(x, yl, t, w=13, h=6.5, edge=MUTED, fill=DATA) for x, t in zip(xs, [
        "Data loader", "Preprocessor", "Metric modules", "Output joiner", "Analysis, plots"])]
    c.arrow(R(e1), L(fs[0]), "I1", ly=1.2)
    for a, b, lab in zip(fs, fs[1:], ["I2", "I3", "I4", "I5"]):
        c.arrow(R(a), L(b), lab, ly=1.2)
    for a, b, lab in zip(ls, ls[1:], ["passes rows to", "passes skills to", "writes tables for", "supplies file to"]):
        c.arrow(R(a), L(b), lab, ly=5.0, fs=5.6)
    for a, b in zip(fs, ls):
        c.arrow(B(a), T(b), color=NAVY, ls=(0, (2, 2)))
    c.ax.text(6.5, 7.5, "Top row: functions.\nBottom row: logical\nelements. Dashed:\nallocated to.", fontsize=5.8, style="italic", color=NAVY, ha="center", va="center")
    c.box(57, 30.6, "Cloned repositories (E2, token churn)", w=27, h=3.4, edge=MUTED, fill=DATA, fs=5.8)
    c.arrow((57, 28.7), T(fs[2]), "I6", lx=2, ly=0)
    c.ax.text(91, 29.6, "I7: tables, figures", fontsize=5.8, style="italic", color=MUTED, ha="center")
    c.arrow(T(fs[4]), (91, 28.8))
    c.save("pipeline-decomposition")


def readability_functional():
    c = Canvas(7.0, 3.15, ymax=62)
    col = [7.5, 22, 36.5, 51.5, 66.5, 81, 95]
    e1 = c.box(col[0], 55, "GitSkills\nsnapshot (E1)", w=12, h=7.5, edge=MUTED, fill=DATA)
    f1 = c.box(col[0], 38, "F1.1\nQuery artifacts\nand siblings", w=12.5, h=9)
    f2 = c.box(col[0], 20, "F2.1\nFilter eligible\nskills", w=12.5, h=8.5)
    f351 = c.box(col[1], 29.5, "F2.2\nSplit front\nmatter from body", w=13)
    f352 = c.box(col[2], 42, "F2.3\nSeparate code\nfrom prose", w=13)
    f353 = c.box(col[3], 54, "F3.5.1\nConvert Markdown\nto sentences", w=13.5)
    f354 = c.box(col[4], 54, "F3.5.2\nIdentify\nlanguage", w=11)
    f355 = c.box(col[5], 54, "F3.5.3\nCompute\nprose grades", w=11)
    f356 = c.box(col[3], 29.5, "F3.5.4\nCompute\ndescription grade", w=13.5)
    f357 = c.box(col[3], 11, "F3.5.5\nCut code into\n10-line windows", w=13.5)
    f358 = c.box(col[4], 11, "F3.5.6\nCompute linear\ncode score", w=11.5)
    f359 = c.box(col[5], 29.5, "F3.5.7\nAssemble\nreadability table", w=10.5)
    f4 = c.box(col[6] - 0.5, 29.5, "F4\nJoin\nmetrics", w=8)
    f51 = c.box(col[6] - 0.5, 46, "F5.1\nCompute\nstatistics", w=9)
    f52 = c.box(col[6] - 0.5, 11, "F5.2\nPlot\ndistributions", w=9.5)
    c.box(col[6] - 0.5, 58, "O1: median,\nIQR, Cliff's δ", w=11, h=5.6, edge=MUTED, fill=DATA, fs=6)
    c.box(col[6] - 0.5, 2.5, "O2: ECDF and\nbox plots", w=11, h=4.8, edge=MUTED, fill=DATA, fs=6)

    c.arrow(B(e1), T(f1), "I1", lx=2.2, ly=0)
    c.arrow(B(f1), T(f2), "I2", lx=2.2, ly=0)
    c.arrow(R(f2), (col[1] - 6.7, 26.5), "I3", ly=-1.9, lx=0.8)
    c.arrow((col[1] + 6.7, 32.0), (col[2] - 6.7, 40), "R1", ly=1.5, lx=-1.0)
    c.arrow(R(f351), L(f356), "R2", lx=0)
    c.arrow((col[2] + 6.7, 44.0), (col[3] - 7, 52), "R3", ly=1.4, lx=-1.0)
    c.arrow((col[2] + 6.7, 40.0), (col[3] - 7, 13), "R4", lx=-2.0, ly=0)
    c.arrow(R(f353), L(f354), "R5")
    c.arrow(R(f354), L(f355), "R6")
    c.arrow(R(f357), L(f358), "R7")
    c.arrow((col[0] + 6.5, 16.5), L(f357), "R8", ly=-1.2, lx=-3)
    c.arrow(B(f355), T(f359), "R9", lx=1.8, ly=0)
    c.arrow(R(f356), L(f359), "R10", lx=0)
    c.arrow((col[4] + 3, 15.2), (col[5] - 3, 25.2), "R11", lx=-1.8, ly=0.6)
    c.arrow(R(f359), L(f4), "I4", ly=1.4)
    c.arrow(T(f4), B(f51), "I5", lx=1.7, ly=0)
    c.arrow(B(f4), T(f52), "I5", lx=1.7, ly=0)
    c.arrow(T(f51), (f51["x"], 55.0), None)
    c.arrow(B(f52), (f52["x"], 5.1), None)
    c.save("readability-functional")


def readability_logical():
    c = Canvas(7.0, 2.45, ymax=47)
    top, mid, bot = 37, 22, 7
    a = c.box(7, mid, "Data loader\n(F1.1)", w=12, h=10, edge=MUTED, fill=DATA)
    b = c.box(25, mid, "Eligibility filter\n(F2.1)", w=13, h=10)
    d = c.box(44, mid, "Skill parser\n(F2.2, F2.3)", w=14.5, h=10)
    e = c.box(44, top, "Markdown normalizer\n(F3.5.1)", w=16, h=8.5)
    f = c.box(63, top, "Language identifier\n(F3.5.2)", w=15, h=8.5)
    g = c.box(84, top, "Prose scorer\n(F3.5.3, F3.5.4)", w=14.5, h=9.5)
    h = c.box(44, bot, "Code windower\n(F3.5.5)", w=14.5, h=8.5)
    i = c.box(63, bot, "Code scorer\n(F3.5.6)", w=14.5, h=8.5)
    j = c.box(84, mid, "Results writer\n(F3.5.7)", w=14.5, h=10)
    k = c.box(84, bot, "Output joiner (F4),\nanalysis and plots\n(F5.1, F5.2)", w=15.5, h=9.5, edge=MUTED, fill=DATA)
    c.arrow(R(a), L(b), "supplies rows to", ly=7.3, fs=5.7)
    c.arrow(R(b), L(d), "passes skills to", lx=-1.0, ly=7.3, fs=5.7)
    c.arrow(T(d), B(e), "sends prose to", lx=6.5, ly=0, fs=5.7)
    c.arrow(B(d), T(h), "sends code to", lx=-6.5, ly=0, fs=5.7)
    c.arrow(R(e), L(f), "sends sentences to", ly=6.0, fs=5.7)
    c.arrow(R(f), L(g), "admits English to", ly=6.0, fs=5.7)
    c.arrow(R(d), (g["x"] - 7.5, top - 4.8), "hands description to", lx=4.0, ly=-3.6, fs=5.7)
    c.arrow(R(h), L(i), "feeds windows to", ly=-6.0, fs=5.7)
    c.arrow((b["x"] + 3, mid - 5.2), (h["x"] - 7.5, bot + 1.5), "supplies scripts to", lx=-6.5, ly=-1.5, fs=5.7)
    c.arrow(B(g), T(j), "reports grades to", lx=7.5, ly=0, fs=5.7)
    c.arrow((i["x"] + 7.5, bot + 2.0), (j["x"] - 7.5, mid - 4.0), "reports scores to", lx=-7.5, ly=2.0, fs=5.7)
    c.arrow(B(j), T(k), "writes table for", lx=7.0, ly=0, fs=5.7)
    c.save("readability-logical")


def hierarchy():
    c = Canvas(7.0, 2.05, ymax=33)
    sn = c.box(9, 24, "SN-1 Which metrics\nhave meaning?", w=16, h=6, fill=GOLD, edge=MUTED)
    s4 = c.box(9, 11, "SN-4 What are each\nmetric's limits?", w=16, h=6, fill=GOLD, edge=MUTED)
    sys1 = c.box(31, 24, "SYS-1\nCompute all five metrics", w=19, h=6, edge=RED, lw=1.5)
    sys2 = c.box(31, 11, "SYS-2\nGive every row a status", w=19, h=6, edge=RED, lw=1.5)
    r1 = c.box(55, 30, "RD-1 Score each part", w=17, h=4.4, edge=RED, lw=1.5)
    r2 = c.box(55, 24, "RD-2 Prose to sentences", w=17, h=4.4, edge=RED, lw=1.5)
    v = c.box(55, 18, "RD-10 Review export", w=17, h=4.4)
    br = c.box(55, 12, "Size, churn, age, clone", w=17, h=4.4, edge=MUTED, fill=DATA)
    n = c.box(55, 6, "RD-4, RD-6 Shall nots", w=17, h=4.4, edge=RED, lw=1.5)
    r11 = c.box(83, 30, "RD-1.1 to RD-1.4 Scores\nRD-3 Language label", w=30, h=5, fs=6)
    r21 = c.box(83, 24, "RD-2.1 One stream per line", w=30, h=4.4, fs=6)
    tv = c.box(83, 18, "T05.5 Hand review (validation)", w=30, h=4.4, fs=6, edge=MUTED, fill=DATA)
    tn = c.box(83, 6, "T05.6 Fault injection (verification)", w=30, h=4.4, fs=6, edge=MUTED, fill=DATA)
    c.arrow(R(sn), L(sys1))
    c.arrow(R(s4), L(sys2))
    for t in (r1, r2, br):
        c.arrow(R(sys1), L(t))
    c.arrow(R(sys2), L(n))
    c.arrow(R(sys2), L(v))
    for a, b in [(r1, r11), (r2, r21)]:
        c.arrow(R(a), L(b))
    for a, b in [(v, tv), (n, tn)]:
        c.arrow(R(a), L(b), color=RED)
    c.ax.text(83, 12, "Red outline: critical.\nRed arrow: verified or validated by.", fontsize=6, color=MUTED, ha="center", va="center")
    c.save("requirements-hierarchy")


def relationship(name, need, parent, req, rationale, functions, logical, physical, verification, derived):
    c = Canvas(7.0, 2.8, ymax=52)
    sn = c.box(15, 43.5, need, w=27, h=11, fill=GOLD, edge=MUTED, fs=6.6)
    pa = c.box(50, 43.5, parent, w=28, h=11, fs=6.6)
    ra = c.box(84, 42, rationale, w=30, h=15.5, edge=RED, fs=6.2)
    fu = c.box(16, 24.5, functions, w=29, h=12.5, fs=6.4)
    re_ = c.box(50, 24.5, req, w=28, h=12.5, fill=NAVY, edge=NAVY, color="white", fs=6.8)
    ve = c.box(84, 24.5, verification, w=30, h=10.5, fs=6.4)
    lo = c.box(16, 6.5, logical, w=29, h=11.5, edge=NAVY, fs=6.4, lw=1.3)
    de = c.box(84, 7, derived, w=30, h=11, fs=6.4)
    ph = c.box(50, 6.5, physical, w=26, h=11.5, edge=MUTED, fill=DATA, fs=6.4)
    c.arrow(L(pa), R(sn), "traced from", ly=1.3, fs=5.6)
    c.arrow(T(re_), B(pa), "traced from", lx=6.0, ly=0)
    c.arrow(L(ra), (re_["x"] + 14.2, 29.0), "justifies", lx=-3.0, ly=1.3, fs=5.8)
    c.arrow(R(fu), L(re_), "satisfies", ly=1.1)
    c.arrow(R(re_), L(ve), "verified\nby", color=RED, ly=2.4, fs=5.8)
    c.arrow((re_["x"] + 14.2, 20.0), (de["x"] - 15.2, 9.0), "flows down to", lx=7.5, ly=1.6, color=NAVY)
    c.arrow(B(fu), T(lo), "allocated to", lx=6.2, ly=0, color=NAVY)
    c.arrow(R(lo), L(ph), "built with", ly=1.2, fs=5.6, color=NAVY)
    c.save(name)


def relationships():
    relationship(
        "critical-rd2",
        "STAKEHOLDER NEED · SN-1\nA researcher should be able to tell\nwhich established metrics have\nmeaningful equivalents for skills.",
        "PARENT · SYS-1\nThe pipeline shall compute all five\nmetrics for every eligible skill.",
        "REQUIREMENT · RD-2 (critical)\nWhen prose contains a heading, list\nitem or table row, the normalizer\nshall output it as its own sentence.",
        "RATIONALE\nFormulas count words per sentence.\nPilot: raw Markdown lifts the median\ngrade from 9.1 to 12.2.\nRejected: raw text; line-by-line rules\n(split wrapped sentences); dropping lists.\nAssumes: skill bodies use Markdown.",
        "FUNCTIONS\nF3.5.1 Convert Markdown to sentences:\nR3 (prose Markdown) to R5 (sentence\ntext). Upstream: F2.3 supplies R3.",
        "LOGICAL ELEMENTS\nSkill parser sends prose to the\nMarkdown normalizer, which sends\nsentences to the language identifier.",
        "PHYSICAL ELEMENTS\nmarkdown-it parser\nin the normalizer script",
        "VERIFICATION · T05.1 (P2, M3)\n20 hand-marked files. Pass: every\nheading, list item and table row is its\nown sentence; every line has one stream.",
        "DERIVED · RD-2.1\nThe segmenter shall assign each line\nof a skill to exactly one stream.")
    relationship(
        "critical-rd6",
        "STAKEHOLDER NEED · SN-4\nA reader should be able to see the\nlimits of each metric before relying\non it.",
        "PARENT · SYS-2\nThe pipeline shall assign every row\none status with a logged reason.",
        "REQUIREMENT · RD-6 (critical)\nThe module shall not label a grade\nas a quality score.",
        "RATIONALE\nPrior work: such scores only weakly track\nhuman judgement on context files (ρ = 0.19).\nRejected: rating scale with rater\nagreement (work exceeds the decision it\nsupports); LLM labels (paid; $0 budget).",
        "FUNCTIONS\nF3.5.7 Assemble readability table:\nR9 to R11 to I4.\nF5.1 Compute statistics: I5 to O1.",
        "LOGICAL ELEMENTS\nResults writer labels each score, and\nthe analysis stage carries that label\ninto tables and figures.",
        "PHYSICAL ELEMENTS\nLabel column in the\nParquet readability table",
        "VERIFICATION · T05.6 (P2, M3, M4)\nFault injection on controlled inputs.\nPass: no grade is labelled\na quality score.",
        "DERIVED · RD-10\nThe module shall export the 40\nextreme-graded English skills\nfor hand review.")


def test_setup():
    c = Canvas(7.0, 1.95, ymax=32)
    inputs = [c.box(10, y, t, w=18, h=6.6, edge=MUTED, fill=DATA, fs=6.3) for y, t in [
        (26.5, "Controlled fixtures\n(known expected results)"),
        (16.5, "13,000-skill sample\n(fixed GitSkills release)"),
        (6.5, "Full snapshot\n(July 2026)")]]
    pipe = c.box(40, 16.5, "Pipeline under test\nP1, P2, P3\nPinned Python environment,\nfixed configuration file,\none team workstation", w=23, h=20)
    outs = c.box(63, 16.5, "Outputs\nmetric tables,\nlogs, plotted values", w=14, h=20, edge=MUTED, fill=DATA, fs=6.3)
    checks = [c.box(87, y, t, w=25, h=5.4, fs=6.0) for y, t in [
        (29, "Reference values: T01-T04, T05.1-T05.4"),
        (22.8, "Status, report and fault checks:\nT05.6, T06, T09, T10"),
        (16.5, "Repeat-run comparison: T07"),
        (10.2, "Timer, memory monitor: T08"),
        (4, "Manual review: T05.5 (validation)")]]
    for b in inputs:
        c.arrow(R(b), (pipe["x"] - 11.7, b["y"] * 0.45 + 9.0))
    c.arrow(R(pipe), L(outs))
    for b in checks:
        c.arrow((outs["x"] + 7.2, 16.5 + (b["y"] - 16.5) * 0.55), L(b))
    c.save("test-setup")


def logo():
    fig, ax = plt.subplots(figsize=(2.2, 2.2))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(FancyBboxPatch((24, 16), 44, 66, boxstyle="round,pad=0.5,rounding_size=4", lw=2.4, ec=NAVY, fc="white"))
    ax.text(46, 72, "SKILL.md", ha="center", va="center", fontsize=9, weight="bold", color=NAVY)
    for y, w, col in [(60, 32, NAVY), (51, 26, NAVY), (42, 30, NAVY), (33, 18, RED)]:
        ax.plot([30, 30 + w], [y, y], lw=3.2, color=col, solid_capstyle="round")
    ax.add_patch(plt.Circle((66, 34), 15, fill=True, fc="white", ec=RED, lw=3.2))
    for x, h in [(60, 6), (66, 12), (72, 18)]:
        ax.plot([x, x], [27, 27 + h], lw=3.2, color=NAVY, solid_capstyle="butt")
    ax.plot([77, 89], [23, 11], lw=4.5, color=RED, solid_capstyle="round")
    fig.savefig(OUT / "group34-logo.pdf", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


if __name__ == "__main__":
    pipeline(); readability_functional(); readability_logical(); hierarchy(); relationships(); test_setup(); logo()
