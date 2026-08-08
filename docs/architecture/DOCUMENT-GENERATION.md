# GTT Center Perth — Document Generation Architecture

**Purpose:** define how the future system generates each output document from `data/canonical/*.yml` (Layer 2) and `models/*` outputs (Layer 3) — never from independently-maintained figures inside the document itself. **No generator is built this phase; no document is regenerated or rewritten.** This document specifies the target-state mapping for each output type: what it consumes, what output format(s) it should eventually be, and which existing hand-authored document is its prior art / current equivalent.

**The one rule every row below exists to enforce:** *"Documents consume canonical/model data only — no independently maintained financial assumptions inside a document."* This is the direct architectural fix for the failure `rules/CLAUDE.md` documents (business-plan.md, executive-summary.md, and others each independently restating the same figures, going stale at different rates). In the target end-state, a template references a `data/canonical/` field ID or a `models/` output ID — it does not contain a literal number that could drift from the source.

---

## 1. Output Format Framework

| Format | Used for | Why |
|---|---|---|
| **XLSX** | Anything with real calculation structure a reader might want to audit, re-sort, or extend (financial forecasts, cost breakdowns, rosters) | Preserves formulas, not just values — an investor or accountant can trace a figure back to its inputs inside the file itself |
| **DOCX** | Narrative documents mixing prose and data (business plan, memoranda, manuals) | Editable by non-technical stakeholders (Anthony, Imara, a solicitor) without needing this repo's tooling |
| **PDF** | Anything intended for external distribution in a final, non-editable form (investor packs, partnership packs, signed-off manuals) | Fixed formatting, safe to send externally |
| **HTML** | Anything meant to be viewed interactively or embedded (timetables, dashboards) | No install required, works in a browser, supports live chart rendering |
| **CSV** | Structured data meant to be re-imported elsewhere (rosters into a scheduling tool, KPI series into a dashboard) | Universal, no formatting to strip out |

Most document types below need **two formats**: one working/audit format (XLSX/HTML) and one distribution format (PDF/DOCX) generated from the same source data — never two independently maintained files.

---

## 2. Document-by-Document Mapping

| # | Document | Consumes (Layer 2/3) | Output format(s) | Current prior-art document | Notes |
|---|---|---|---|---|---|
| 1 | **Executive Summary** | `business.yml`, headline P&L/capacity figures from `models/financial/`, `models/operations/` | DOCX + PDF | `docs/executive-summary.md` | Must pull the *same* headline P&L figure the Financial Forecast Pack (#6) shows — no independent restatement |
| 2 | **Business Plan** | `business.yml`, `services.yml`, `pricing.yml`, `client_assumptions.yml`, full model outputs, plus authored narrative (vision, competitive positioning — not derivable from data) | DOCX + PDF | `docs/business-plan.md` | The document with the most narrative content relative to data — template needs a clear split between data-bound sections and freely-authored prose sections |
| 3 | **Feasibility Study** | `client_assumptions.yml` (addressable market), `models/financial/` break-even output, `risks.yml` | DOCX + PDF | `docs/feasibility.md` | Go/no-go framing — must present `SCENARIO`-tagged upside cases separately from the `MODELLED`/`CALCULATED` base case, per `DATA-GOVERNANCE.md` §4 |
| 4 | **Investor Information Memorandum** | Full financial model output, `startup_costs.yml`/`capex.yml`, `risks.yml` | DOCX + PDF | `docs/investor-memorandum.md` | Highest-stakes document for the "generated doc must never itself become a source of truth" rule — `rules/CLAUDE.md`'s own "Why This Rule Exists" section cites this exact document type showing a loss in its body table while a banner above claimed profitability; a template pulling one field, once, from `models/financial/` structurally prevents that class of internal contradiction |
| 5 | **Funding Proposal** | `startup_costs.yml`/`capex.yml`, cash-flow trough from `models/financial/`, `revenue_assumptions.yml` | DOCX + PDF | No direct prior art — closest existing content is `docs/CURRENT-STATE.md` §6/§7's startup-capital reconciliation and `docs/revenue-extraction-options.md` | New document type; needs the startup-capital range question (§6/§7's still-unreconciled ranges) resolved upstream in the data layer before this can be generated meaningfully |
| 6 | **Financial Forecast Pack** | Full `models/financial/` output (P&L, cash flow, break-even, unit economics, sensitivity) | **XLSX** (primary, with formulas) + PDF (summary extract) | `docs/profit-loss-tables.md`, `docs/cash-flow.md`, `docs/break-even-sensitivity-analysis.md`, `docs/unit-economics.md` | The clearest "should be a workbook, not prose" candidate in the whole repo — see `MODEL-ARCHITECTURE.md` §1 |
| 7 | **Startup Cost Report** | `startup_costs.yml`, `capex.yml`, `facilities.yml` | XLSX + PDF | `docs/equipment-costs.md`, `docs/floor-plan-concept.md`'s Fit-Out Cost Estimate, `docs/CURRENT-STATE.md` §6/§7 | Must render the low/mid/high range structure already established in §7, not collapse it to a single misleadingly-precise number |
| 8 | **Operations Manual** | `operating_hours.yml`, `scheduling_assumptions.yml`, `clinical_timing.yml`, combined-timetable output from `models/operations/` | DOCX + PDF | `docs/operations-manual.md` | The document CONFLICT-03 already flagged as a real staff-training risk when its scheduling section went stale — a generated version sourced live from `models/operations/` structurally cannot go stale the way a hand-maintained section did |
| 9 | **Staffing Plan** | `staffing.yml`, `wages.yml`, roster-requirement output from `models/staffing/` | DOCX + XLSX roster appendix | `docs/staff-plan.md`, `docs/hr-framework.md` | |
| 10 | **Client Timetable** | Client-timetable output from `models/operations/` | PDF/HTML for display + CSV data export | `docs/scenario-c-sync-timetables.md` | CSV export lets this feed a real booking system later without re-transcription |
| 11 | **Staff Roster** | Roster output from `models/staffing/` | XLSX/CSV (working) + PDF (for physical posting) | `docs/pm-staffing-roster.md`, `docs/am-staffing-by-volume.md` | |
| 12 | **Combined Timetable** | Client timetable + roster, merged | HTML (interactive) + PDF | `docs/scenario-c-sync-timeline.html` — currently hand-built, the clearest existing example of a visual that should be generated from data rather than authored | |
| 13 | **Capacity Report** | Capacity + utilisation + bottleneck-analysis output from `models/operations/` | PDF/HTML | `docs/am-capacity-weekend.md`, `docs/scenario-d-investigation.md` | |
| 14 | **Risk Report** | `risks.yml` | DOCX + PDF | `docs/risk-register.md`, `docs/02_issues_and_risks.md` | Two existing documents (a ranked table and a narrative gap analysis) that currently serve overlapping purposes — target state is one `risks.yml` feeding both a tabular and a narrative rendering, rather than two independently maintained files |
| 15 | **Marketing Plan** | `business.yml`, `client_assumptions.yml` (addressable market), largely authored narrative content | DOCX + PDF | `docs/poppy-marketing.md`, `docs/afternoon-marketing-plan.md`, `docs/referral-partnership-plan.md` | Lowest data-dependency document on this list — mostly stays hand-authored, with only the market-size figures pulled from canonical data |
| 16 | **Partnership Pack** | `business.yml`, `scheduling_assumptions.yml`, `clinical_timing.yml`, correspondence references from `data/sources/manifest.yml` | DOCX + PDF | `docs/pathology-partnership-brief.md`, `docs/reed-partnerships.md` | Must never restate a WDP-sourced figure (e.g. the 10:30am guidance) without the same `VERIFIED` tag and source citation the canonical layer carries |
| 17 | **KPI Report** | Selected `models/financial/` and `models/operations/` outputs (revenue/visit, margin %, break-even distance, utilisation) | HTML dashboard (primary) + CSV export | No direct prior art — new document type, ties directly to `dashboards/` (Layer 6, `TARGET-ARCHITECTURE.md`) | Only meaningful once real trading data exists; pre-launch this would show modelled/projected KPIs only, each still carrying its `MODELLED`/`SCENARIO` tag |

---

## 3. Template Structure (applies to every document above)

Each future `documents/templates/<doc-name>.yml` (or equivalent) is proposed to define:

```yaml
document_id: <e.g. investor-memorandum>
output_formats: [docx, pdf]
sections:
  - id: financial_snapshot
    source: models.financial.pnl_summary        # a model output ID, not a literal number
    render_as: table
    status_disclosure: required                  # any MODELLED/SCENARIO field must show its tag inline
  - id: market_positioning
    source: authored                              # explicitly not data-driven — prose content lives in the template itself
  - id: risk_summary
    source: data.canonical.risks
    filter: {status: [VERIFIED, DECIDED, MODELLED]}   # SCENARIO/PLACEHOLDER/SUPERSEDED excluded unless explicitly labelled
```

**The `status_disclosure: required` field is the mechanism that enforces `DATA-GOVERNANCE.md` §4's table** — a generator that ignores it is a validation failure, not a silent pass (see `VALIDATION-ARCHITECTURE.md` §3).

---

## 4. What Stays Authored, Not Generated

Not every word in every document above comes from data. Vision statements, competitive-positioning language, risk narrative framing, and marketing copy are genuinely authored content with no canonical-data equivalent — and should stay that way. The architectural point is narrower and more specific: **the numbers embedded inside that authored prose must be references, not restatements.** A future `business-plan.md` template can and should still say *"GTT Center Perth transforms the mandatory wait into a restorative experience"* as authored prose — it should not also independently type out *"+A$63,028.75/month"* as a literal string that could silently diverge from `models/financial/`'s actual output the next time the model is rebased.

---

## 5. What This Document Does Not Do

It does not generate any document, XLSX, DOCX, PDF, HTML, or CSV file. It does not build a template engine or choose an implementation library (e.g. `docxtpl`, `openpyxl`, Jinja2 for HTML) — that is an implementation-phase decision. It does not rewrite any of the 17 existing prior-art documents listed above.
