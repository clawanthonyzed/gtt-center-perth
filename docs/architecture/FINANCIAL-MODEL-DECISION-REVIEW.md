# Financial Model Decision Review

**Phase:** Financial Model Decision Review — analytical review only. No canonical YAML, financial formula, revenue methodology, cost methodology, or scenario was modified in this phase. No new assumption was introduced. Neither Table 1 nor Table 2 is chosen as "correct." No open tracker item is resolved without new evidence.

**Date:** 2026-08-10
**Model/document version reviewed:** commit `fdf8e17` (Document Generation Phase output) on top of `8727317` (Master Financial Model, item 46/47 resolved)

**Source of truth used:** `outputs/GTT-Center-Perth-Financial-Model.xlsx`, `outputs/GTT-Center-Perth-Financial-Report.docx`, `outputs/GTT-Center-Perth-Financial-Report.pdf`, `docs/architecture/FINANCIAL-DOCUMENT-GENERATION-AUDIT.md`, `data/models/master_financial_model.yml`, `docs/VERIFICATION-TRACKER.md`.

---

## Executive Summary

The canonical financial model is internally consistent, fully tested (114/114 passing), and traceable to source for every headline figure. Both committed scenarios (Table 1: 18 clients/day, Table 2: 12 clients/day) reach a positive, post-superannuation steady-state Net Operating Result — A$56,581.70/month and A$21,056.64/month respectively — and remain positive over a flat 24-month projection. Table 1 strictly dominates Table 2 financially (2.7x the net result, at identical headcount) but demand for 18 clients/day has never been tested, and the founder decision on which scenario is the actual daily target remains open (item 1m).

The model's own sensitivity analysis is the single most important risk finding of this review: **both scenarios become loss-making at 50% of committed client volume** (Table 1: -A$2,660.80/month; Table 2: -A$18,438.36/month), and Table 2's margin of safety above break-even (≈27% of committed volume) is materially thinner than Table 1's (≈48%). This is a genuine, quantified demand-shortfall risk, not a hypothetical one.

The bounded funding requirement (A$357,390–A$577,180) is close to — but not identical to — Anthony's own previously adopted figure (A$292,335–A$594,900). Both are disclosed side by side; neither is an exact number ready for a bank or investor. The single largest lever on both the funding range and cost-base precision is a confirmed venue (item 3, BLOCKING) — nearly every HIGH-tier blocked decision in Section 3 below traces back to that one external dependency.

The three generated deliverables are usable now as an internal reference and a founder-facing financial story. They are not yet investor- or lender-ready — see Section 6.

---

## 1. What's Known With Confidence

### Verified / Canonical (highest confidence — sourced directly, cross-checked)
- Package pricing: A$250 / A$300 (only two tiers; the historical third tier was dropped).
- Staffing structure: 8 dual-qualified treatment staff (4 Massage+Beauty, 2 Nails, 2 Hair) + 2 phlebotomists, **identical at both 18 clients/day and 12 clients/day** — zero incremental weekday labour cost between scenarios.
- Superannuation: 12% of Ordinary Time Earnings, correctly applied to 6 of 8 payroll components (item 46, resolved). This raised the previously-reported (pre-2026-08-09) steady-state figures down from A$60,201.62 to A$56,581.70/month (Table 1) and A$24,257.56 to A$21,056.64/month (Table 2).

### Modelled / Calculated (high confidence — deterministic, reproducible, but built on disclosed simplifications)
| Metric | Table 1 (18/day) | Table 2 (12/day) |
|---|---|---|
| Steady-state revenue | A$155,215.80 | A$115,720.80 |
| Steady-state payroll (incl. super) | A$84,654.10 | A$80,684.16 |
| Steady-state operating expenses | A$13,980.00 | A$13,980.00 |
| Steady-state total operating costs | A$98,634.10 | A$94,664.16 |
| Steady-state Net Operating Result | A$56,581.70 | A$21,056.64 |
| Gross Contribution margin (Revenue − Payroll) | 45.5% | 30.3% |
| Break-even AM client volume/day | 9.404 | 8.801 |
| Margin of safety above break-even | 8.596 clients/day (≈48% of committed) | 3.199 clients/day (≈27% of committed) |
| 24-month cumulative Net Operating Result | A$1,172,971.91 | A$368,159.42 |
| Operating cash trough (accrual-basis proxy) | -A$30,885.75 (Month 1) | -A$66,335.12 (Month 3) |

- **Revenue ramp:** Months 1–4 ramp at 43/64/79/93% of steady state, reaching 100% at Month 5; Months 6–24 held flat (no growth invented past Month 5 — no document in this repo states a post-Month-5 growth curve, so none was assumed).
- **Bounded funding requirement:** A$357,390–A$577,180 (Pre-Opening Capital A$272,390–A$467,180 + historical Working Capital Reserve A$85,000–A$110,000) — a defensible range, not an exact figure.

### Unresolved (explicitly not known — do not treat as settled)
- Which scenario (Table 1 or Table 2) is the venture's actual daily target (item 1m).
- The exact funding requirement (item 47 — bounded, not exact; underlying 6–9-range historical startup-capital reconciliation, items 25/26, unresolved).
- Real market/referral-demand evidence for the committed client volumes, or for the 43/64/79/93/100% ramp curve shape itself (items 41, 42).
- Current Fair Work award wage rates and Saturday/Sunday/Public Holiday penalty percentages (items 16, 17, 18) — every payroll figure in this model rests on a wage table dated "Effective 1 July 2025," 13+ months stale.
- WDP's commercial rental/staffing terms (items 1c, 1d) — could restructure the ~A$48,000–106,000/year AM Direct Labor cost entirely.
- A confirmed physical venue (item 3, BLOCKING) — gates real construction quotes, real rent, and a genuinely precise funding figure.

---

## 2. What Decisions Can Be Made Now

The evidence below is presented as available support for a decision — none of these decisions is made on Anthony's behalf.

**Is the model viable at all?** The evidence supports "yes, provisionally" — both scenarios are profitable at steady state, profitable cumulatively over 24 months, and the cost structure (payroll being 55–70% of total costs) is the dominant, well-understood driver. The provisional qualifier exists because committed client volume has never been demand-tested (see Section 4).

**Does Table 1 or Table 2 have sufficient margin?** The evidence favours Table 1 on pure financial grounds: same headcount, 2.7x the Net Operating Result, and a materially wider margin of safety (48% vs 27% of committed volume above break-even). Table 2's margin of safety (3.2 clients/day) is thin enough that a modest demand shortfall could push it into loss — the sensitivity table shows Table 2 is only marginally profitable at 75% of committed volume (+A$1,309.14/month). This is a financial-model-only comparison; it does not weigh the non-financial reasons a founder might still prefer the lower-volume scenario (service quality, staff workload, ramp risk) — those are outside this model's scope.

**Do pricing assumptions support profitability?** Yes, on the figures modelled: Gross Contribution margin is 45.5% (Table 1) / 30.3% (Table 2), and both scenarios clear their AM-volume break-even with room to spare at committed volume. This is not evidence that the A$250/A$300 price points are optimal, only that they are sufficient to be profitable at the currently modelled cost base.

**Does staffing structure create risk?** Mixed evidence. Upside: identical headcount at both scenarios means there is no headcount-inflation risk in choosing Table 1 over Table 2. Downside: the AM labour ramp is not modelled (item 43) — full 8-person weekday payroll is assumed from Month 1, which is disclosed as conservative, but only remains conservative if a genuine reduced-headcount (7-staff) roster is actually hireable during the ramp period, which item 12 flags as untested in the real world.

**Is the funding range investable/plausible?** The bounded A$357,390–A$577,180 range is arithmetically clean (an exact decomposition of an already-canonical total, not a new invented figure) and lands close to Anthony's own previously adopted A$292,335–A$594,900 figure. That convergence across two independently-derived methods is a genuine, mild confidence signal. It is not yet precise enough to present to a lender or professional investor as a fundable amount (see Section 6).

---

## 3. What Decisions Remain Blocked

### HIGH — could materially change viability or the funding requirement

| # | Decision required | Why it matters | Current blocker | Impact if unresolved | Cheapest/highest-value path |
|---|---|---|---|---|---|
| Item 3 | Confirm physical venue | Gates fit-out quotes, real rent, council permits, staff hiring — the single dependency nearly every other HIGH item below cascades from | No location search reported closed | Every downstream cost figure (construction, rent, insurance-site-specific) stays a range, not a number | Anthony's own venue search + landlord negotiation — cannot be shortcut by more modelling |
| Items 25, 26 | Reconcile the 6–9 unreconciled historical startup-capital ranges, including the two competing fit-out construction estimates | Directly determines the true funding requirement's precision | No confirmed venue floor plate to quote against | Funding conversations must always be presented as a range, never a number | 3 real builder quotes once item 3 is resolved (per `docs/floor-plan-concept.md`'s own existing next step) |
| Items 1c, 1d | Confirm WDP's commercial rental/staffing terms and whether phlebotomy stays in-house or shifts to WDP | Could restructure ~A$48,000–106,600/year of AM Direct Labor cost either up or down | Awaiting WDP's State Business Manager (Carole actively chasing, per item 1c's 2026-08-08 update — genuine progress, not stalled) | Cost base for both scenarios' AM Direct Labor line stays uncertain until a real quote lands | Anthony follow-up with Carole once WDP's figure arrives; compare against the already-computed A$104,800–106,600/yr break-even threshold (item 1d-be) |
| Items 16, 17, 18 | Confirm current Fair Work MA000005/MA000027 award rates and Saturday/Sunday/PH penalty percentages | Every payroll figure in this model (≈55–70% of total costs) rests on a wage table 13+ months past its stated effective date, with a second, disagreeing "indicative" source in the same repo | No live Fair Work Commission fetch/payroll-advisor confirmation obtained yet | Direction of error unknown — payroll could be understated (raising apparent profitability) or the model could be conservative (understating it) | A single Fair Work Infoline call (13 13 94) or a direct FWC award-database lookup — cheap, no venue dependency, resolvable today |
| Item 1m | Which scenario (Table 1 or Table 2) is the actual committed daily target | Determines which single figure this venture communicates externally, and which ramp/staffing plan gets built for real | Genuinely a founder decision, not a modelling gap | Every external communication currently must present two figures side by side, which is accurate but harder to act on operationally | Anthony's own decision — zero cost, zero external dependency, resolvable today |

### MEDIUM — improves confidence but unlikely to change the overall viability conclusion

| # | Decision required | Why it matters | Current blocker | Impact if unresolved | Cheapest/highest-value path |
|---|---|---|---|---|---|
| Item 43 | Re-verify the 7-staff reduced-headcount option against the 25-min cadence for use during ramp-up | Could reduce, not increase, Months 1–4 payroll and therefore the operating cash trough | Requires a scheduling-solver re-run, not yet done against Table 1/Table 2 | Current cash-trough figures (A$30,885.75/A$66,335.12) may be a worst case, overstating the real working-capital need | A scheduling-solver task, moderate effort, no external dependency |
| Item 19 | Confirm real insurance cost via 3 broker quotes | Quantified this review: swings Table 1's net result by <1%, Table 2's by ≈2.5% — real but not viability-changing | No quotes obtained | Modest, quantifiable understatement of monthly opex persists | 3 quick BizCover quotes — cheap, no venue dependency |
| Item 22 | Update GTT supplies from the stale "200 tests/month" basis to Table 1/Table 2's real volumes (396/264) | Understates opex by ≈A$392/month (Table 1) or ≈A$128/month (Table 2) | Simple recalculation, not yet applied to the primary total | Small, real, currently-invisible cost understatement | A same-session arithmetic fix once someone is authorised to touch `opex.yml` — cheapest item on this entire list |
| Item 24 | Confirm whether the A$8,000/month rent figure includes outgoings | Could add A$1,200–2,000/month to fixed costs | Cannot be resolved before a real lease exists | Fixed-cost base could be understated by ~9–14% of the current rent line | Confirm once item 3 (venue) is resolved — same dependency, not independently actionable |
| Items 41, 42 | Reconcile the two disagreeing PM revenue ramps and document the 43/64/79/93/100% curve's origin | Affects Month 1–4 revenue/cash-flow precision (up to ≈A$6,020/month gap at Month 1), not steady-state viability | No external benchmark or client-acquisition model cited anywhere in this repo | Ramp-period cash-flow figures carry more uncertainty than the steady-state figures | Low-cost documentation review; would need real early-trading data to fully resolve |
| Item 39 | Determine what share of PM bookings are GTT-paired (pre-booking-discount eligible) | Current PM revenue may be a modest overstatement | Requires real booking-mix data | Revenue-side overstatement risk — the opposite direction to most other findings | Cannot be resolved pre-launch; track as a Day 1 KPI |

### LOW — documentation/completeness only

| # | Decision required | Why it matters | Cheapest path |
|---|---|---|---|
| Item 45 | Define a canonical "total visits" concept for consumables/laundry variable-cost modelling | Small dollar magnitude either way | Deferred until/unless a per-visit unit-economics model is ever wanted |
| Item 20 | Confirm real Fresha seat count/cost | Modelled figure may overstate (not understate) a small cost line | Confirm once a Fresha account exists |
| Item 21 | Add the missing A$50–100/month medical waste line to Non-Wage Overhead | Small, real, currently-invisible cost | Same-session fix once someone touches `opex.yml` |
| Items 30–35 | Various service-catalogue price/lifecycle conflicts (spray tan, hair colour, lash infill, GDM items) | Affect PM/ancillary service menu accuracy, not the core committed P&L | Resolve opportunistically next time each document is touched |

---

## 4. Model Risk Review (Investor/Operator Lens)

### Upside risks (not quantified further than the model already supports)
- **Ancillary revenue exclusion:** Currently A$0.00 by explicit instruction (2026-07-30). Historical placeholder estimates (spray tan, retail, café) totalled roughly A$98,000/year combined, but item 10/38 flags these as unreconciled and not modellable with confidence — genuine upside if a real bottom-up model is ever built, not a number to quote.
- **Utilisation above committed volume:** Item 1l's internal-planning-only Scenario B found a theoretical ceiling as high as 36 clients/day at the same relative labour efficiency, though the physical floor plan cannot currently support it — a real but currently unactionable upside.
- **PM attach-rate upside:** If the a-la-carte average (A$95/session) understates real upsell behaviour, PM revenue could exceed the model — no evidence either way currently exists.

### Downside risks (quantified where the model already supports it)
- **Demand shortfall is the largest quantified downside risk in this model.** Both scenarios are loss-making at 50% of committed volume (Table 1: -A$2,660.80/month; Table 2: -A$18,438.36/month). Table 2's thin margin of safety (only 3.2 clients/day above break-even) makes it materially more fragile to a shortfall than Table 1.
- **Wage-rate uncertainty (items 16–18)** is a systemic, direction-unknown risk across the entire payroll base — could move either scenario's net result meaningfully in either direction.
- **WDP commercial terms (items 1c, 1d)** could restructure a six-figure annual cost line depending on the eventual negotiated figure versus the computed A$104,800–106,600/yr break-even threshold.
- **Funding-range width:** the A$357,390–A$577,180 primary range spans roughly 62% between its low and high end — wide enough that raising toward the low end carries real execution risk if true costs land toward the high end.
- **Rent outgoings ambiguity (item 24)** could add A$1,200–2,000/month to fixed costs, currently unaccounted for.

### Unknown risks (not quantified — flagged, not invented)
- **The ramp curve's own origin is undocumented anywhere in this repo (item 42)** — no external benchmark, referral model, or comparable-venue data exists. This is arguably the single largest true unknown in the entire model: every other risk above is at least bounded by a range; the demand-ramp shape itself is not.
- **GST treatment (item 7)** and the **proposed 30% trust-distribution tax (items 9, 9c)** are structural/tax-position risks, not operating-model risks — they affect net proceeds to Anthony/Imara, not the venue's own P&L.
- **No market comparable is cited anywhere in this repo** for a first-of-its-kind Perth GTT wellness venue — the entire demand assumption rests on internal planning logic, not external validation.

---

## 5. Five Highest-Value Next Data Points

| # | Missing information | Why it matters | Expected impact | Ease of obtaining |
|---|---|---|---|---|
| 1 | Confirmed venue/lease | Unlocks real construction quotes, real rent, real site-specific insurance | Converts the funding range and the rent/construction cost lines from ranges to real numbers — the single highest-leverage item on this list | Difficult — a real property search/negotiation, not a data-gathering task |
| 2 | WDP's commercial rental/staffing figure | Determines whether AM Direct Labor stays in-house or shifts entirely | Could restructure a six-figure annual cost line either direction | Moderate — external party dependency, but already actively in motion (Carole chasing WDP's State Business Manager) |
| 3 | Current Fair Work MA000005/MA000027/MA000002 award rates and Saturday/Sunday/PH penalty percentages | Underpins the entire payroll base (55–70% of total costs) across both scenarios | Removes the largest unresolved systemic risk in the cost model | Easy — a single Fair Work Infoline call or FWC award-database lookup, no venue dependency |
| 4 | 3 real insurance quotes | Removes a disclosed placeholder line | Quantified this review as modest (<1% Table 1, ≈2.5% Table 2 of net result) — cheap to close regardless | Easy — BizCover, per `financial-setup.md`'s own existing instruction |
| 5 | Anthony's decision on item 1m (Table 1 vs Table 2 as the actual daily target) | Determines which single figure this venture uses externally and which real staffing/ramp plan gets built | No new number needed — an existing decision point, not a data-gathering task | Easiest — zero external dependency, resolvable today |

---

## 6. External-Audience Readiness

**Investor readiness: NOT sufficient as-is.** What exists (a validated, tested, traceable two-scenario model with disclosed limitations) is a genuinely strong internal foundation, but a professional investor pitch is missing: a confirmed venue and real construction quotes, an exact (not bounded) funding figure, resolved wage-rate conflicts across the entire payroll base, real demand/market evidence for the ramp curve, and a decision on which scenario is primary. Presenting the current deliverables externally without the "IMPORTANT — READ FIRST" scope notice and bounded-range framing intact would risk overstating precision this model does not have.

**Lender readiness: NOT sufficient as-is.** A lender typically requires an exact loan amount, accountant-reviewed/audited financials, and security/collateral documentation — none of which exist yet (item 6 explicitly states accountant sign-off has not occurred). The bounded funding range and disclosed methodology could support a preliminary, informal conversation with a lender or broker, but not a formal application.

**Internal operator readiness: YES, materially ready.** Anthony/Grace can use the current model right now to compare Table 1 vs Table 2 trade-offs, understand the cash-trough magnitude and timing the ramp period requires, identify which cost lines dominate (payroll, overwhelmingly, at both scenarios), and track the specific real-world data points (Section 5) that would most improve confidence. One usability caveat: the Excel workbook is a point-in-time snapshot with values written from the canonical YAML at generation time — it is not a live-linked tool that re-syncs automatically if the underlying YAML changes; each future update requires re-running the generator.

---

## 7. Document Quality Review

Findings from direct inspection of the three generated files — reported, not fixed, per this phase's "review only" scope.

- **Excel note/warning blocks use a fixed 15pt row height with `wrap_text` enabled but not auto-fit.** Several warning lines exceed what fits visually in one wrapped line at the sheet's column widths — the text is fully present in the cell (no data loss), but a reader skimming quickly in Excel without manually resizing the row could miss part of a warning. Worth an auto-fit-height pass if this workbook is revised.
- **"Table 1" / "Table 2" terminology is heavily overloaded.** It refers to the two financial scenarios throughout, but every actual data table in all three documents is also generically "a table" — a first-time external reader (particularly of the PDF, which is meant to be readable without repo context) could momentarily confuse the scenario name with an ordinary table reference. This terminology is inherited from the whole repository, not introduced by this phase, but is a real readability risk for an external audience unfamiliar with the convention.
- **Word Section 8 (Break-Even Analysis) lacks the per-scenario H2 subheadings** used consistently in Sections 3, 4, 5, 7, and 12 — it presents both scenarios in one combined table instead. A minor structural inconsistency, not an error.
- **The PDF (the most "public-facing" of the three deliverables) does not include the client-volume sensitivity table.** This means a PDF-only reader never sees the finding that both scenarios are loss-making at 50% of committed volume — a genuinely important risk data point that is fully present in the Excel (Sheet 8) and Word (Section 12) versions but absent from the PDF as scoped. Worth considering for inclusion if the PDF is ever revised or if it becomes the primary document shown to a new audience.
- **The Excel workbook is values-only, not formula-linked back to the source YAML** (though within-sheet totals do use live Excel formulas, e.g. Sheet 4's `=SUM(...)` rows) — appropriate for a snapshot deliverable, but not a live recalculation tool. Already disclosed in the audit doc; restated here as a usability note.
- **No formatting/calculation errors found.** Currency/negative formatting is consistent and clearly marked (`-A$` prefix) throughout; no broken cross-references between "see Sheet X" / "see Section Y" pointers and actual content; no unit-confusion or truncation issues beyond the row-height item above.

---

## Recommended Next Phase

Two low-cost, high-value actions are available immediately, with no external dependency: (1) Anthony's own decision on item 1m (Table 1 vs Table 2), and (2) a single Fair Work Commission/payroll-advisor confirmation of current award rates (items 16–18), which underpins the single largest systemic risk in the cost model. Both could be closed in the same session at effectively zero cost.

Beyond those two, nearly every other HIGH-tier blocked decision (funding precision, real construction cost, real rent, WDP commercial terms) cascades from a single external dependency: a confirmed venue (item 3). This review's own recommendation is that further modelling work is not the highest-value next phase — the highest-value next phase is closing that one external dependency, after which a genuine, non-bounded funding requirement and cost base become achievable for the first time.

---

## Validation — Confirmed Nothing Was Modified

- `git status --short` at the start of this review: clean (no uncommitted changes from the prior phase).
- `git status --short` after this review's file changes: only this document and a targeted, evidence-based addendum to `docs/VERIFICATION-TRACKER.md` item 19 (materiality re-quantification, status unchanged, no existing text removed).
- Full pytest suite: **114 passed**, 0 failed (re-run, unchanged from the prior phase).
- `tools/validate_canonical_data.py`: **13 files checked, 0 errors, 27 warnings** (identical to the prior phase — no new errors, no new warnings).
- `tools/check_consistency.py`: **0 findings** (identical to the prior phase).
- No canonical YAML file, financial formula, revenue/cost methodology, or scenario definition was touched. No generated document (`outputs/*.xlsx`, `*.docx`, `*.pdf`) was altered.
