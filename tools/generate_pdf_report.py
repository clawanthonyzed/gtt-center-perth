"""
GTT Center Perth -- PDF Report Generator (Deliverable 3).

Generates outputs/GTT-Center-Perth-Financial-Report.pdf, a presentation-
quality PDF readable without repo access. Uses reportlab for layout
(weasyprint is broken on this machine -- missing native libgobject-2.0-0,
a Windows system dependency, not fixable via pip) and matplotlib for
charts, all built from tools/document_data.py -- the same shared
data-assembly layer as the Excel and Word deliverables.

Charts are generated as PNGs from live canonical model outputs (never
manually recreated numbers), written to a scratch temp directory, then
embedded into the PDF -- the PNGs themselves are not committed to the repo.

SCOPE BOUNDARIES: same as generate_excel_model.py / generate_word_report.py
-- no primary scenario chosen, no invented opening cash/financing, funding
requirement always presented as a bounded range, no startup/capex leakage
into operating P&L, A$63,028.75 never labelled revenue.
"""

import os
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
import document_data as dd  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402

from reportlab.lib import colors  # noqa: E402
from reportlab.lib.pagesizes import A4  # noqa: E402
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # noqa: E402
from reportlab.lib.units import cm  # noqa: E402
from reportlab.lib.enums import TA_CENTER  # noqa: E402
from reportlab.platypus import (  # noqa: E402
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak,
    HRFlowable,
)

OUTPUT_PATH = REPO_ROOT / "outputs" / "GTT-Center-Perth-Financial-Report.pdf"

NAVY = colors.HexColor("#1F3864")
RED = colors.HexColor("#C00000")
AMBER = colors.HexColor("#FFF2CC")
LIGHT_BLUE = colors.HexColor("#DCE6F1")
GREY = colors.HexColor("#595959")

CHART_DIR = Path(tempfile.gettempdir()) / "gtt_pdf_charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

T1_COLOR = "#1F3864"
T2_COLOR = "#C00000"


def fmt_aud(v):
    if v is None:
        return "n/a"
    neg = v < 0
    s = f"A${abs(v):,.2f}"
    return f"-{s}" if neg else s


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
styles = getSampleStyleSheet()
styles.add(ParagraphStyle("GTTTitle", parent=styles["Title"], fontSize=28, textColor=NAVY, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle("GTTSubtitle", parent=styles["Normal"], fontSize=14, textColor=GREY, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle("GTTH1", parent=styles["Heading1"], textColor=NAVY, fontSize=16, spaceBefore=14, spaceAfter=8))
styles.add(ParagraphStyle("GTTH2", parent=styles["Heading2"], textColor=NAVY, fontSize=12.5, spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle("GTTBody", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=6))
styles.add(ParagraphStyle("GTTWarning", parent=styles["Normal"], fontSize=10, leading=14, textColor=RED, spaceAfter=6, spaceBefore=4))
styles.add(ParagraphStyle("GTTCaption", parent=styles["Normal"], fontSize=8.5, textColor=GREY, alignment=TA_CENTER, spaceBefore=2, spaceAfter=10))


def p(text, style="GTTBody"):
    return Paragraph(text, styles[style])


def data_table(headers, rows, col_widths=None):
    table_data = [headers] + [[str(c) for c in row] for row in rows]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_BLUE]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def warning_box(text):
    t = Table([[Paragraph(text, styles["GTTWarning"])]], colWidths=[16.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AMBER),
        ("BOX", (0, 0), (-1, -1), 0.75, RED),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


# ---------------------------------------------------------------------------
# Charts (matplotlib, from live model outputs)
# ---------------------------------------------------------------------------
def chart_revenue_ramp(data: dd.DocumentData):
    fig, ax = plt.subplots(figsize=(6.3, 3.6), dpi=150)
    months = [1, 2, 3, 4, 5]
    for sid, color in ((dd.SCENARIOS[0], T1_COLOR), (dd.SCENARIOS[1], T2_COLOR)):
        vals = [data.pnl_24mo[sid][m - 1]["revenue"]["total_revenue"] for m in months]
        ax.plot(months, vals, marker="o", color=color, linewidth=2, label=data.label(sid))
    ax.set_title("Revenue Ramp -- Month 1 to Month 5+ (Steady State)", fontsize=11, color="#1F3864")
    ax.set_xlabel("Month")
    ax.set_ylabel("Monthly Revenue (AUD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.set_xticks(months)
    ax.set_xticklabels(["M1", "M2", "M3", "M4", "M5+"])
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    path = CHART_DIR / "revenue_ramp.png"
    fig.savefig(path)
    plt.close(fig)
    return path


def chart_cost_vs_revenue(data: dd.DocumentData):
    fig, ax = plt.subplots(figsize=(6.3, 3.6), dpi=150)
    labels = [data.label(sid) for sid in dd.SCENARIOS]
    revenue = [data.steady_state[sid]["revenue"]["total_revenue"] for sid in dd.SCENARIOS]
    costs = [data.steady_state[sid]["total_operating_costs"] for sid in dd.SCENARIOS]
    net = [data.steady_state[sid]["net_operating_result"] for sid in dd.SCENARIOS]
    x = range(len(labels))
    width = 0.25
    ax.bar([i - width for i in x], revenue, width=width, label="Revenue", color=T1_COLOR)
    ax.bar([i for i in x], costs, width=width, label="Total Operating Costs", color="#8FAADC")
    ax.bar([i + width for i in x], net, width=width, label="Net Operating Result", color="#548235")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_title("Month 5+ Steady State -- Revenue vs. Costs vs. Net Result", fontsize=11, color="#1F3864")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    path = CHART_DIR / "cost_vs_revenue.png"
    fig.savefig(path)
    plt.close(fig)
    return path


def chart_24mo_cumulative(data: dd.DocumentData):
    fig, ax = plt.subplots(figsize=(6.3, 3.6), dpi=150)
    months = list(range(1, 25))
    for sid, color in ((dd.SCENARIOS[0], T1_COLOR), (dd.SCENARIOS[1], T2_COLOR)):
        cumulative, running = [], 0.0
        for pnl in data.pnl_24mo[sid]:
            running += pnl["net_operating_result"]
            cumulative.append(running)
        ax.plot(months, cumulative, color=color, linewidth=2, label=data.label(sid))
    ax.axhline(0, color="#888888", linewidth=1, linestyle="--")
    ax.set_title("24-Month Cumulative Net Operating Result", fontsize=11, color="#1F3864")
    ax.set_xlabel("Month")
    ax.set_ylabel("Cumulative Net Operating Result (AUD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    path = CHART_DIR / "cumulative_24mo.png"
    fig.savefig(path)
    plt.close(fig)
    return path


def chart_breakeven(data: dd.DocumentData):
    fig, ax = plt.subplots(figsize=(6.3, 3.6), dpi=150)
    labels = [data.label(sid) for sid in dd.SCENARIOS]
    breakeven = [data.breakeven[sid]["breakeven_am_client_volume_per_day"] for sid in dd.SCENARIOS]
    committed = [data.breakeven[sid]["committed_client_volume_per_day"] for sid in dd.SCENARIOS]
    x = range(len(labels))
    width = 0.32
    ax.bar([i - width / 2 for i in x], breakeven, width=width, label="Break-Even AM Volume/Day", color="#C00000")
    ax.bar([i + width / 2 for i in x], committed, width=width, label="Committed AM Volume/Day", color=T1_COLOR)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("AM Clients / Day")
    ax.set_title("Break-Even vs. Committed AM Client Volume", fontsize=11, color="#1F3864")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    path = CHART_DIR / "breakeven.png"
    fig.savefig(path)
    plt.close(fig)
    return path


def chart_cash_trough(data: dd.DocumentData):
    fig, ax = plt.subplots(figsize=(6.3, 3.6), dpi=150)
    for sid, color in ((dd.SCENARIOS[0], T1_COLOR), (dd.SCENARIOS[1], T2_COLOR)):
        cf = data.cash_flow[sid]
        months = [r["forecast_month"] for r in cf["rows"]]
        cumulative = [r["cumulative_position"] for r in cf["rows"]]
        ax.plot(months, cumulative, color=color, linewidth=2, label=data.label(sid))
        ax.scatter([cf["trough_month"]], [cf["trough_cumulative_position"]], color=color, zorder=5, s=40)
    ax.axhline(0, color="#888888", linewidth=1, linestyle="--")
    ax.set_title("Operating Cash Position -- Accrual-Basis Proxy (NOT a funding schedule)", fontsize=10.5, color="#1F3864")
    ax.set_xlabel("Month")
    ax.set_ylabel("Cumulative Operating Cash Position (AUD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    path = CHART_DIR / "cash_trough.png"
    fig.savefig(path)
    plt.close(fig)
    return path


def chart_funding_range(data: dd.DocumentData):
    fig, ax = plt.subplots(figsize=(6.3, 2.6), dpi=150)
    fr = data.funding["combined_funding_requirement_bounded"]["primary_method"]
    low, high = fr["range_low"], fr["range_high"]
    ax.barh(["Bounded Funding\nRequirement"], [high - low], left=[low], color="#FFC000", edgecolor="#C00000", height=0.5)
    ax.set_xlabel("AUD")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.set_title(f"Bounded Funding Requirement: {fmt_aud(low)} - {fmt_aud(high)} (RANGE, NOT EXACT)", fontsize=10, color="#C00000")
    ax.grid(alpha=0.3, axis="x")
    fig.tight_layout()
    path = CHART_DIR / "funding_range.png"
    fig.savefig(path)
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------
# PDF assembly
# ---------------------------------------------------------------------------
def build_story(data: dd.DocumentData):
    story = []

    # -- Title page --
    story.append(Spacer(1, 3 * cm))
    story.append(p("GTT Center Perth", "GTTTitle"))
    story.append(p("Financial Model &amp; Report", "GTTSubtitle"))
    story.append(Spacer(1, 0.4 * cm))
    story.append(p("Two-scenario canonical financial model (Table 1: 18 clients/day, Table 2: 12 clients/day)", "GTTBody"))
    story.append(Spacer(1, 1 * cm))
    story.append(warning_box(
        "<b>IMPORTANT -- READ FIRST</b><br/><br/>"
        "This report presents CANONICAL (validated), MODELLED (calculated from canonical inputs), "
        "HISTORICAL-SUPERSEDED (preserved for traceability, no longer live), and BOUNDED (range, not exact) "
        "figures, each explicitly labelled. Neither Table 1 nor Table 2 is presented as the venture's primary "
        "scenario -- see VERIFICATION-TRACKER.md item 1m, still open. The funding requirement is a bounded range, "
        "not a single point estimate. No opening cash balance or financing structure is assumed anywhere in this "
        "report."
    ))
    story.append(PageBreak())

    # -- Executive Summary --
    story.append(p("1. Executive Summary", "GTTH1"))
    story.append(p(
        "GTT Center Perth's canonical financial model supports two committed scenarios, presented side by side "
        "throughout this report. Neither is designated the venture's primary basis -- Table 1 (18 clients/day) "
        "generates materially higher revenue and net operating result at identical headcount, but the founder "
        "decision to formally adopt it over Table 2 (12 clients/day) has not been made."
    ))
    sc = data.scenario_comparison
    rows = [
        ["Client volume/day", sc["scenario_table_1"]["client_volume_per_day"], sc["scenario_table_2"]["client_volume_per_day"]],
        ["Monthly revenue (steady state)", fmt_aud(sc["scenario_table_1"]["steady_state_revenue"]), fmt_aud(sc["scenario_table_2"]["steady_state_revenue"])],
        ["Total operating costs (steady state)", fmt_aud(sc["scenario_table_1"]["steady_state_total_operating_costs"]), fmt_aud(sc["scenario_table_2"]["steady_state_total_operating_costs"])],
        ["Net operating result (steady state, post-super)", fmt_aud(sc["scenario_table_1"]["steady_state_net_operating_result"]), fmt_aud(sc["scenario_table_2"]["steady_state_net_operating_result"])],
        ["24-month net operating result", fmt_aud(data.totals_24mo["scenario_table_1"]["total_net_operating_result_24mo"]), fmt_aud(data.totals_24mo["scenario_table_2"]["total_net_operating_result_24mo"])],
        ["Break-even AM client volume/day", data.breakeven["scenario_table_1"]["breakeven_am_client_volume_per_day"], data.breakeven["scenario_table_2"]["breakeven_am_client_volume_per_day"]],
        ["Operating cash trough", fmt_aud(data.cash_flow["scenario_table_1"]["trough_cumulative_position"]), fmt_aud(data.cash_flow["scenario_table_2"]["trough_cumulative_position"])],
    ]
    story.append(data_table(["Metric", "Table 1 (18/day)", "Table 2 (12/day)"], rows, col_widths=[8 * cm, 4.25 * cm, 4.25 * cm]))
    story.append(Spacer(1, 0.3 * cm))
    fr = data.funding["combined_funding_requirement_bounded"]["primary_method"]
    story.append(warning_box(f"Bounded funding requirement (universal, both scenarios): {fmt_aud(fr['range_low'])} - {fmt_aud(fr['range_high'])} -- a RANGE, not an exact figure. See Section 9."))
    story.append(PageBreak())

    # -- Scenario Comparison --
    story.append(p("2. Scenario Comparison", "GTTH1"))
    story.append(Image(str(chart_cost_vs_revenue(data)), width=15.5 * cm, height=8.85 * cm))
    story.append(p("Figure 1: Month 5+ steady-state Revenue, Total Operating Costs, and Net Operating Result, both scenarios. Source: tools/master_financial_model.py#compute_month_pnl.", "GTTCaption"))
    rows = [
        ["Steady-state payroll", fmt_aud(sc["scenario_table_1"]["steady_state_payroll"]), fmt_aud(sc["scenario_table_2"]["steady_state_payroll"])],
        ["Steady-state opex", fmt_aud(sc["scenario_table_1"]["steady_state_opex"]), fmt_aud(sc["scenario_table_2"]["steady_state_opex"])],
        ["Annualised revenue", fmt_aud(sc["scenario_table_1"]["annualised_revenue"]), fmt_aud(sc["scenario_table_2"]["annualised_revenue"])],
        ["Annualised net operating result", fmt_aud(sc["scenario_table_1"]["annualised_net_operating_result"]), fmt_aud(sc["scenario_table_2"]["annualised_net_operating_result"])],
    ]
    story.append(data_table(["Metric", "Table 1 (18/day)", "Table 2 (12/day)"], rows, col_widths=[8 * cm, 4.25 * cm, 4.25 * cm]))
    story.append(PageBreak())

    # -- Revenue & Cost Ramp --
    story.append(p("3. Revenue Ramp", "GTTH1"))
    story.append(p("Months 6-24 are held flat at Month 5+ (steady state) -- no post-Month-5 growth curve exists in this repository's canonical data, so none is invented."))
    story.append(Image(str(chart_revenue_ramp(data)), width=15.5 * cm, height=8.85 * cm))
    story.append(p("Figure 2: Revenue ramp, Month 1 to Month 5+, both scenarios. Source: data/canonical/revenue_ramp.yml.", "GTTCaption"))
    story.append(PageBreak())

    # -- 24-Month Outlook --
    story.append(p("4. 24-Month Financial Outlook", "GTTH1"))
    story.append(Image(str(chart_24mo_cumulative(data)), width=15.5 * cm, height=8.85 * cm))
    story.append(p("Figure 3: 24-month cumulative Net Operating Result, both scenarios. Source: tools/master_financial_model.py#compute_24_month_pnl.", "GTTCaption"))
    rows = []
    for m in data.snapshot_months:
        r1 = data.pnl_24mo["scenario_table_1"][m - 1]
        r2 = data.pnl_24mo["scenario_table_2"][m - 1]
        rows.append([f"Month {m}", fmt_aud(r1["net_operating_result"]), fmt_aud(r2["net_operating_result"])])
    story.append(data_table(["Month", "Table 1 Net Result", "Table 2 Net Result"], rows, col_widths=[6 * cm, 5.25 * cm, 5.25 * cm]))
    story.append(PageBreak())

    # -- Break-Even --
    story.append(p("5. Break-Even Analysis", "GTTH1"))
    story.append(warning_box(
        "A traditional contribution-margin break-even is NOT computed -- nearly every cost in this model is "
        "classified FIXED, and the GTT-supplies/consumables/laundry classification remains unresolved. What is "
        "computed is an AM client-volume break-even, holding Month 5+ PM revenue/payroll/opex fixed."
    ))
    story.append(Image(str(chart_breakeven(data)), width=15.5 * cm, height=8.85 * cm))
    story.append(p("Figure 4: Break-even vs. committed AM client volume, both scenarios. Source: tools/master_financial_model.py#compute_breakeven.", "GTTCaption"))
    rows = [[data.label(sid), data.breakeven[sid]["breakeven_am_client_volume_per_day"], data.breakeven[sid]["margin_of_safety_clients_per_day"]] for sid in dd.SCENARIOS]
    story.append(data_table(["Scenario", "Break-Even Vol./Day", "Margin of Safety"], rows, col_widths=[8 * cm, 4.25 * cm, 4.25 * cm]))
    story.append(PageBreak())

    # -- Operating Cash Position --
    story.append(p("6. Operating Cash Position", "GTTH1"))
    story.append(warning_box(
        "OPERATING-CASH-basis view only (accrual-basis proxy, NOT a true cash-basis forecast). NOT a complete "
        "funding schedule -- excludes startup capital, capex, and any opening cash balance (none assumed)."
    ))
    story.append(Image(str(chart_cash_trough(data)), width=15.5 * cm, height=8.85 * cm))
    story.append(p("Figure 5: Cumulative operating cash position, both scenarios, trough marked. Source: tools/master_financial_model.py#compute_cash_flow.", "GTTCaption"))
    story.append(PageBreak())

    # -- Funding Requirement --
    story.append(p("7. Funding Requirement", "GTTH1"))
    story.append(warning_box(
        "BOUNDED (OUTCOME 2), NOT an exact figure. The underlying 6-9-range historical startup-cost reconciliation "
        "remains genuinely unresolved."
    ))
    poc = data.funding["pre_opening_capital"]
    hist = data.funding["opening_working_capital"]["historical_reserve_method"]
    rows = [
        ["(A) Pre-Opening Capital", f"{fmt_aud(poc['range_low'])} - {fmt_aud(poc['range_high'])}"],
        ["(B) Working Capital Reserve (historical basis)", f"{fmt_aud(hist['range_low'])} - {fmt_aud(hist['range_high'])}"],
        ["(A) + (B) Combined -- PRIMARY METHOD", f"{fmt_aud(fr['range_low'])} - {fmt_aud(fr['range_high'])}"],
    ]
    story.append(data_table(["Component", "Range (AUD)"], rows, col_widths=[10 * cm, 6.5 * cm]))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Image(str(chart_funding_range(data)), width=15.5 * cm, height=6.5 * cm))
    story.append(p("Figure 6: Bounded funding requirement range. Source: data/models/master_financial_model.yml#funding_requirement_investigation.", "GTTCaption"))
    story.append(p(
        "Not included anywhere in this section: an opening cash balance (none exists in this repository), a "
        "financing/debt/equity structure (none assumed), or the operating cash trough summed on top of the working "
        "capital reserve (would double-count the same 'survive the ramp' concept)."
    ))
    story.append(PageBreak())

    # -- Risks / Open Issues --
    story.append(p("8. Key Risks and Unresolved Assumptions", "GTTH1"))
    rows = [
        ["30", "Working capital reserve basis is a pre-rebase Month 1-3 loss estimate", "UNRESOLVED"],
        ["36", "Historical vs. canonical revenue gap (A$2,576.36/month)", "RESOLVED (nuanced)"],
        ["39", "PM pre-booking discount not applied", "UNRESOLVED"],
        ["43", "AM labour ramp not modelled (fixed from Month 1)", "UNRESOLVED (disclosed)"],
        ["45", "GTT supplies/consumables/laundry classification", "UNRESOLVED"],
        ["46", "Superannuation partial coverage (2 of 8 payroll components)", "PARTIALLY RESOLVED"],
        ["47", "Funding requirement bounded, not exact", "PARTIALLY RESOLVED"],
    ]
    story.append(data_table(["Item", "Description", "Status"], rows, col_widths=[2 * cm, 10.5 * cm, 4 * cm]))
    story.append(PageBreak())

    # -- Methodology --
    story.append(p("9. Methodology Notes", "GTTH1"))
    story.append(p(
        "This report is generated entirely from data/canonical/*.yml and data/models/master_financial_model.yml. "
        "Every figure carries a governance status: CANONICAL (validated source data), MODELLED (computed from "
        "canonical inputs), HISTORICAL-SUPERSEDED (preserved for traceability only), BOUNDED (a range, not a "
        "point estimate), or UNRESOLVED (no defensible figure exists yet)."
    ))
    story.append(p("Source methodology documents:"))
    for doc_name in [
        "docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md", "docs/architecture/REVENUE-RAMP-METHODOLOGY.md",
        "docs/architecture/COST-RAMP-METHODOLOGY.md", "docs/architecture/MASTER-FINANCIAL-MODEL-METHODOLOGY.md",
        "docs/architecture/FUNDING-REQUIREMENT-INVESTIGATION.md", "docs/VERIFICATION-TRACKER.md", "docs/CURRENT-STATE.md",
    ]:
        story.append(p(f"&bull; {doc_name}", "GTTBody"))
    story.append(Spacer(1, 0.3 * cm))
    story.append(warning_box(
        "The historical A$63,028.75 figure (Table 1, pre-2026-08-09-superannuation-fix) is a Monthly Net P&L "
        "figure -- NOT revenue. It must never be relabelled as revenue in any deliverable."
    ))

    return story


def main():
    data = dd.get_data()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PATH), pagesize=A4,
        leftMargin=1.6 * cm, rightMargin=1.6 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm,
        title="GTT Center Perth Financial Report",
    )
    story = build_story(data)
    doc.build(story)
    print(f"PDF report written: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
