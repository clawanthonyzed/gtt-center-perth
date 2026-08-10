# Financial Document Generation Audit

**Phase:** Document Generation (turns the validated canonical data layer + Master Financial Model into professional deliverables). Presentation work — no canonical assumption, methodology, or figure was recalculated, reinterpreted, or changed in this phase.

**Date:** 2026-08-10
**Model commit used as source of truth:** `8727317` (the commit current at the start of this phase — includes the Funding Requirement Investigation, item 47, and the superannuation fix, item 46)

---

## 1. Exact Source Files Used

All three deliverables are built from a single shared data-assembly layer, `tools/document_data.py`, which reads (and computes nothing new beyond what these already do):

- `data/canonical/pricing.yml`, `client_assumptions.yml`, `scenarios.yml`, `staffing.yml`, `wages.yml`, `opex.yml`, `startup_costs.yml`, `capex.yml`, `services.yml`, `revenue_assumptions.yml`, `revenue_ramp.yml`, `cost_ramp.yml`
- `data/models/master_financial_model.yml`
- `tools/master_financial_model.py` — every function called live (`compute_24_month_pnl`, `compute_24_month_totals`, `compute_cash_flow`, `compute_breakeven`, `compute_sensitivity_client_volume`, `compute_sensitivity_insurance`, `compute_scenario_comparison`), not re-implemented or approximated
- Methodology docs referenced by name in the deliverables: `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`, `REVENUE-RAMP-METHODOLOGY.md`, `COST-RAMP-METHODOLOGY.md`, `MASTER-FINANCIAL-MODEL-METHODOLOGY.md`, `FUNDING-REQUIREMENT-INVESTIGATION.md`
- `docs/VERIFICATION-TRACKER.md`, `docs/CURRENT-STATE.md`

No canonical YAML file was modified in this phase.

---

## 2. Generated Files

| File | Generator | Format |
|---|---|---|
| `outputs/GTT-Center-Perth-Financial-Model.xlsx` | `tools/generate_excel_model.py` | 10-sheet Excel workbook, live formulas |
| `outputs/GTT-Center-Perth-Financial-Report.docx` | `tools/generate_word_report.py` | 16-section Word report |
| `outputs/GTT-Center-Perth-Financial-Report.pdf` | `tools/generate_pdf_report.py` | 10-page presentation PDF with 6 matplotlib charts |
| `tools/document_data.py` | — | shared data-assembly layer, no independent figures |

Chart PNGs used inside the PDF are generated at build time to a system temp directory (`%TEMP%/gtt_pdf_charts/`) and are **not** committed to the repository — regenerable from `tools/generate_pdf_report.py` at any time.

---

## 3. Library Stack

- `openpyxl` 3.1.5 — Excel generation, formula strings written directly into cells (e.g. `=SUM(...)`, `=B{r}-C{r}`) so totals are Excel-computed, not duplicated hard-coded values.
- `python-docx` (`docx`) 1.2.0 — Word generation.
- `reportlab` 5.0.0 — PDF generation (platypus flowables).
- `matplotlib` 3.11.1 — chart generation, all 6 charts computed from live `document_data.py` outputs.

**Capability note (not a live blocker):** `weasyprint` is installed on this machine but fails to import (`OSError: cannot load library 'libgobject-2.0-0'`) — a missing native Windows system library (GObject/Pango), not fixable via `pip install`. `reportlab` was used instead, a pure-Python, fully adequate substitute with no native dependency. No further troubleshooting of `weasyprint` was attempted since a working alternative existed.

---

## 4. Critical Figures — Verified Against the Live Model (not copied blindly)

All values below were re-derived by directly calling `tools/master_financial_model.py` and reading `data/models/master_financial_model.yml`, then cross-checked against the generated deliverables. **Zero discrepancies found.**

| Figure | Table 1 (18/day) | Table 2 (12/day) |
|---|---|---|
| Steady-state revenue | A$155,215.80 | A$115,720.80 |
| Steady-state net operating result (post-super) | A$56,581.70 | A$21,056.64 |
| 24-month total net operating result | A$1,172,971.91 | A$368,159.42 |
| Break-even AM client volume/day | 9.404 | 8.801 |
| Operating cash trough | -A$30,885.75 (Month 1) | -A$66,335.12 (Month 3) |
| Bounded funding requirement (universal) | A$357,390.00 – A$577,180.00 | (same, non-scenario-specific) |

---

## 5. QC Checklist — Results

| # | Check | Result |
|---|---|---|
| 1 | Full pytest suite | **114 passed**, 0 failed |
| 2 | `tools/validate_canonical_data.py` | **13 files checked, 0 errors, 27 warnings** (all pre-existing, already-disclosed conflicts — no new errors introduced) |
| 3 | `tools/check_consistency.py` | **0 findings** across all `docs/*.md` |
| 4 | Programmatic Excel-vs-model cross-check | Spot-checked Sheet 1 (Executive Summary) cell values against `document_data.py`/`master_financial_model.py` live outputs — all 12+ scenario-comparison rows and the funding range matched exactly. Confirmed live Excel `=SUM(...)` formulas present in Sheet 4 (P&L). |
| 5 | No document presents stale historical revenue as canonical | Searched all three deliverables for `157,792.16` / `118,297.16` — every occurrence found is explicitly labelled `HISTORICAL`/`SUPERSEDED`, never presented as current canonical revenue |
| 6 | A$63,028.75 never labelled revenue | Searched all three deliverables — appears once each in Excel/PDF, twice in Word, always under a "Value/Status" or explicit "Monthly Net P&L — NOT revenue" framing, never in a Revenue column/context |
| 7 | A$357,390–A$577,180 never presented as an exact figure | Every occurrence in all three deliverables pairs both bounds together (e.g. "A$357,390.00 - A$577,180.00 — a RANGE, not an exact figure") — confirmed via text search across Excel/Word/PDF |
| 8 | No startup/capex costs leaked into operating P&L | Sheet 4 (P&L Operating Model) scanned for `capex`/`startup cost`/`pre-opening`/`construction`/`fit-out` terms — the only matches are the sheet's own disclaimer sentence ("Startup costs and capex are NOT included anywhere in this sheet"), not actual cost figures |
| 9 | Formulas/totals correctness | Excel formula strings verified present and syntactically valid (`=SUM(...)`, cell-reference arithmetic); workbook opens and recalculates cleanly in openpyxl round-trip |
| 10 | Visual inspection | Excel: 10 sheets, no title-length warnings after fix, frozen panes present. Word: 16 `Heading 1` sections, 19 tables, correct page breaks. PDF: 10 pages, 6 embedded charts, title page + warning box render correctly |

No discrepancies were found requiring a model fix. One implementation bug was found and fixed **in the document generator itself** (not the model): Sheet 1 originally called `wb.active` after the sheet had already been removed by `main()`, causing an `AttributeError` — fixed by having `main()` leave the workbook's default sheet in place for `build_executive_summary` to claim, rather than removing it upfront. A second, cosmetic fix: Sheet 10's original name ("10. Source & Methodology Register") exceeded Excel's 31-character worksheet-name limit, triggering an openpyxl warning — shortened to "10. Source & Methodology".

---

## 6. Presentation Limitations (disclosed, not hidden)

- The funding requirement is presented as a **bounded range**, not an exact figure — the underlying 6–9-range historical startup-capital reconciliation (`docs/architecture/STARTUP-COST-RECONCILIATION.md`) remains genuinely unresolved and is explicitly stated as such in all three deliverables.
- Neither Table 1 nor Table 2 is presented as the venture's primary scenario anywhere — VERIFICATION-TRACKER.md item 1m remains open.
- The Cash Flow sections are explicitly labelled operating-cash-basis only (an accrual-basis proxy), not a true cash-basis forecast or a complete funding schedule.
- No opening cash balance or financing/debt/equity structure is assumed anywhere in any deliverable.
- Break-Even sections explicitly state that a traditional contribution-margin break-even is NOT computed, and why.

## 7. Figures Intentionally Excluded

- No new sensitivity scenarios beyond the two already computed by `tools/master_financial_model.py` (client volume, insurance).
- No investor-facing framing, financing recommendation, or lender-application content — out of scope for this phase.
- No marketing-facing content.

## 8. Unresolved Issues Carried Into the Deliverables

All carried forward unresolved, not resolved by this phase, and disclosed in Sheet 9 / Section 13 / the PDF's risks section of the respective deliverables:

- Item 30 — working capital reserve basis is stale (pre-rebase Month 1–3 loss estimate)
- Item 36 — historical vs. canonical revenue gap (A$2,576.36/month), origin unresolved
- Item 39 — PM pre-booking discount not applied anywhere in the model
- Items 41–42 — revenue-ramp Month 1–4 percentage curve's original derivation unresolved
- Item 43 — AM labour ramp not modelled (payroll held fixed from Month 1)
- Item 45 — GTT supplies/consumables/laundry FIXED vs. VARIABLE classification conflict
- Item 46 — superannuation partially resolved (6 of 8 payroll components); Opening-Time Increment and Receptionist/Relief Pool remain super-uncertain
- Item 47 — funding requirement bounded, not exact
- Insurance modelled (A$400/month) vs. itemised (A$975–1,583/month) estimate conflict

---

## 9. Report-Back Summary

**Generated:** Excel workbook (10 sheets, live formulas), Word report (16 sections), PDF report (10 pages, 6 charts), plus this audit doc.

**Verification results:** All 6 coordinator-listed critical figures matched the live model exactly, to the cent. Full test suite (114 tests) passed. Canonical validator and consistency checker both passed with only pre-existing, already-disclosed warnings (0 new errors). All 8 substantive QC checks (items 4–8 above map to the coordinator's numbered checklist) passed with no discrepancies found.

**Discrepancies found:** None in the underlying financial figures. Two implementation-level bugs were found and fixed in the document generator code itself (not the model) — see §5 above.

**Capability gaps hit:** `weasyprint` is broken on this machine (missing native `libgobject-2.0-0`) — worked around with `reportlab`, a fully adequate pure-Python substitute. No other capability gap encountered.
