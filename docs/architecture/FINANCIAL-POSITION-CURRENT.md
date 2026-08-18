# Financial Position — Current State

**Planning case: 18 clients/day (Table 1).** This is the only operating plan. 12/day and 6/day appear ONLY in the sensitivity table below (§2), always clearly labelled, never as competing plans. Every figure below is current, live-verified against `data/models/master_financial_model.yml` and `data/canonical/cost_ramp.yml` — no historical or superseded figures appear in this document (see `docs/CURRENT-STATE.md` for the historical correction record).

**Terminology used precisely throughout:** "Revenue" = gross booking value. "Operating Costs" = payroll + non-wage overhead + relief/absence coverage allowance. "Operating Result" = Revenue − Operating Costs — this is NOT "profit" in an accounting sense (no depreciation, tax, interest, or startup-capital amortisation is included; see the explicit exclusions note in §4). "Cash Flow" = the accrual-basis monthly movement of Operating Result over time — NOT a true cash-basis forecast (no debtor/creditor timing, no weekly-payroll-timing granularity).

**Two open financial items resolved this round (Financial Finalisation, 2026-08-18):** (1) the insurance figure conflict, resolved by investigation — see `docs/architecture/FINANCIAL-ASSUMPTION-REGISTER.md`; (2) the relief/absence staffing cost, previously entirely unmodelled, now a real, quantified, propagated line. Both changes are reflected in every figure below.

---

## 1. Headline — 18-Client Planning Case

| Metric | Value | Label |
|---|---|---|
| AM clients/day | 18 | VERIFIED (solver-confirmed) |
| PM transaction capacity/day (weekday) | 12.8128 | CALCULATED, `docs/architecture/PM-CAPACITY-RECONCILIATION.md` |
| Total Revenue | **A$154,710.69/month** | CALCULATED |
| Total Operating Costs | **A$122,133.89/month** | CALCULATED |
| **Operating Result** | **A$32,576.80/month** | **CALCULATED** |
| Operating Margin | 21.1% (Operating Result ÷ Revenue) | CALCULATED |
| Annualised Operating Result | A$390,921.60 | CALCULATED (Monthly × 12) |
| Break-even revenue | A$122,133.90/month | CALCULATED |
| Break-even client volume | 13.051 clients/day | CALCULATED |
| Margin of safety | 4.949 clients/day (27.5% above break-even volume) | CALCULATED |
| 24-month cumulative Operating Result | A$598,232.91 | CALCULATED |
| Cash-flow trough | -A$76,532.52 at Month 2 | CALCULATED |
| Month cumulative position turns positive | Month 6 | CALCULATED |

## 2. Sensitivity Table — 6/12/18 Clients/Day, Real Figures Throughout

**18/day is the sole planning case. 6/day and 12/day are sensitivity/downside comparisons only — shown here to demonstrate what happens if actual volume falls short, never presented as alternative plans anywhere else in this venture's documents.**

| Metric | 6 clients/day (SENSITIVITY) | 12 clients/day (SENSITIVITY) | **18 clients/day (PLANNING CASE)** |
|---|---|---|---|
| AM clients/day | 6 | 12 | **18** |
| PM transactions/day (weekday) | 12.8128 (unaffected by AM volume — capacity-constrained) | 12.8128 | **12.8128** |
| Monthly revenue | A$75,720.69 | A$115,215.69 | **A$154,710.69** |
| Annualised revenue | A$908,648.28 | A$1,382,588.28 | **A$1,856,528.28** |
| Direct labour | A$101,717.02 | A$101,717.02 | **A$101,717.02** |
| — of which superannuation (12%) | A$10,735.31 | A$10,735.31 | **A$10,735.31** |
| — of which workers comp (1.7%, PLACEHOLDER) | A$1,520.83 | A$1,520.83 | **A$1,520.83** |
| Non-wage overhead (insurance corrected) | A$14,288.34 | A$14,288.34 | **A$14,288.34** |
| Relief/Absence Coverage Allowance (NEW) | A$6,128.53 | A$6,128.53 | **A$6,128.53** |
| **Total opex** | **A$122,133.89** | **A$122,133.89** | **A$122,133.89** |
| **Monthly Operating Result** | **-A$46,413.20** | **-A$6,918.20** | **A$32,576.80** |
| Annualised Operating Result | -A$556,958.40 | -A$83,018.40 | **A$390,921.60** |
| Operating Margin | -61.3% | -6.0% | **21.1%** |
| Break-even revenue | A$122,133.90/month (same fixed cost base at every volume) | A$122,133.90/month | **A$122,133.90/month** |
| Break-even clients/day | 13.051/day | 13.051/day | **13.051/day** |
| Margin of safety (clients/day) | -7.051 (BELOW break-even) | -1.051 (BELOW break-even) | **+4.949 (ABOVE break-even)** |
| 24-month cumulative operating result | N/A — no ramp/24-month model exists for this sensitivity point (steady-state comparison only, never operated as a real ramping plan) | **-A$172,138.34** (Table 2's actual modelled 24-month result) | **A$598,232.91** |
| Cash-flow trough | N/A — same reason | **-A$172,138.34 at Month 24** (the cumulative position falls every month, never recovers) | **-A$76,532.52 at Month 2** |
| Month cumulative turns positive | N/A | **Never within 24 months — cumulative position deteriorates every month** | **Month 6** |

**Note on why labour/opex are identical across all three columns:** this reflects a disclosed, pre-existing modelling limitation (`conflict_am_labor_ramp_unmodelled` in `data/canonical/cost_ramp.yml`) — committed headcount is fixed at the 18-client design regardless of actual booking volume, since staff are rostered to the committed design, not flexed down. This makes the 6/12-client columns a genuine downside stress test (revenue drops, costs do not), not a lower-cost alternative plan.

**6 clients/day is genuinely loss-making** (-A$46,413.20/month). **12 clients/day (Table 2) is now loss-making at steady state too** (-A$6,918.20/month), under the more realistic cost base (corrected insurance + relief/absence allowance) — its 24-month cumulative position deteriorates every single month and never recovers. **Only 18 clients/day clears break-even, with a genuine but narrower margin of safety than every prior round showed.**

## 3. Break-Even — Both Forms, Plain English

**At approximately A$122,134/month of total revenue, the business covers its modelled operating costs (payroll + non-wage overhead + relief/absence coverage allowance) and neither makes nor loses money.**

| Form | Value | Calculation |
|---|---|---|
| Break-even revenue | **A$122,133.90/month** | Total Operating Costs (A$122,133.89) − PM Revenue (A$36,225.69, held fixed) = AM revenue needed (A$85,908.20) → converted back to a total-revenue figure |
| Break-even client volume | **13.051 clients/day** | AM revenue needed ÷ A$250/client, weighted across weekday and Saturday operating days |

**18-client target vs. break-even, both forms:**

| | Break-even | 18-client target | Buffer (dollar/client) | Buffer (%) |
|---|---|---|---|---|
| Revenue | A$122,133.90/month | A$154,710.69/month | +A$32,576.79/month | +26.7% |
| Client volume | 13.051/day | 18.000/day | +4.949/day | +37.9% |

**In plain terms: the 18-client planning case generates roughly A$32,600/month more revenue than the business needs just to break even, and could lose almost 5 clients/day of volume (about a quarter of the committed target) before falling below break-even.** This margin is genuinely narrower than every prior round showed (it was +49.1% client-volume buffer before this round's cost-realism corrections) — reported plainly, this is what happens when the model is made more accurate, not less.

## 4. Profit & Loss — 18-Client Planning Case, Monthly and Annualised

**Revenue**

| Line | Monthly | Annualised | Calculation trail |
|---|---|---|---|
| AM GTT (Package 1, weekday + Saturday) | A$118,485.00 | A$1,421,820.00 | `FINANCIAL-FIGURE-REFERENCE.md` §1 |
| AM gap-fill/standalone | A$0.00 (none — the AM window is fully occupied by the 18-client structure, no idle capacity exists to sell as gap-fill at full committed volume) | A$0.00 | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2 |
| PM packages + PM standalone (blended, see note) | A$36,225.69 | A$434,708.28 | `FINANCIAL-FIGURE-REFERENCE.md` §2 |
| Ancillary (cafe/retail) | A$0.00 (explicitly excluded from the baseline — treated as pure upside if it materialises, not forecast) | A$0.00 | `data/canonical/revenue_assumptions.yml#rev_ancillary_excluded_from_baseline` |
| **TOTAL REVENUE** | **A$154,710.69** | **A$1,856,528.28** | |

*(PM packages and PM standalone are not separately split in the canonical model — both are blended into the single A$117 average transaction value per the disclosed 60% individual / 25% PM Refresh / 15% PM Restore mix, `FINANCIAL-FIGURE-REFERENCE.md` §2 step 5. A future round could split this into two explicit lines once real booking data exists to support the split.)*

**Operating Costs**

| Line | Monthly | Annualised | Calculation trail |
|---|---|---|---|
| Treatment labour, AM (Massage+Beauty A$25,645.50 + Nails A$12,586.81 + Hair A$12,586.81) | A$50,819.12 | A$609,829.44 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| PM Treatment labour (session-throughput, 4 lines blended) | A$12,966.55 | A$155,598.60 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| Phlebotomy labour | A$11,754.19 | A$141,050.28 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| Venue Manager | A$9,118.40 | A$109,420.80 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| PM Reception | A$4,802.83 | A$57,633.96 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| Superannuation (12%, universal) | A$10,735.31 | A$128,823.72 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| Workers compensation (1.7%, **PLACEHOLDER**) | A$1,520.83 | A$18,249.96 | `FINANCIAL-FIGURE-REFERENCE.md` §3 |
| **Payroll subtotal** | **A$101,717.23** (A$0.21 rounding gap vs. the canonical A$101,717.02, disclosed floating-point artefact in the PM Treatment component, §3e of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` — immaterial, not force-reconciled) | A$1,220,606.76 | |
| Rent/occupancy | A$8,000.00 | A$96,000.00 | `FINANCIAL-FIGURE-REFERENCE.md` §4 |
| Utilities | A$650.00 | A$7,800.00 | §4 |
| **Insurance (Public Liability + Professional Indemnity + Property/Contents, CORRECTED)** | **A$708.34** | A$8,500.08 | §4 — `[MODELLED/BALLPARK-ESTIMATE — real broker quotes in motion]` |
| GTT supplies | A$400.00 | A$4,800.00 | §4 |
| Consumables | A$800.00 | A$9,600.00 | §4 |
| Laundry | A$350.00 | A$4,200.00 | §4 |
| Marketing | A$1,500.00 | A$18,000.00 | §4 |
| Software (Fresha + email + internet/phone) | A$280.00 | A$3,360.00 | §4 |
| Cleaning | A$600.00 | A$7,200.00 | §4 |
| Accounting/bookkeeping | A$500.00 | A$6,000.00 | §4 |
| Miscellaneous/contingency | A$500.00 | A$6,000.00 | §4 |
| **Non-wage overhead subtotal** | **A$14,288.34** | A$171,460.08 | Matches `cost_ramp.yml`'s canonical figure exactly |
| **Relief/Absence Coverage Allowance (NEW)** | **A$6,128.53** | A$73,542.36 | `FINANCIAL-FIGURE-REFERENCE.md` §5 — `[MODELLED/BALLPARK-ESTIMATE]` |
| **TOTAL OPERATING COSTS** | **A$122,133.89** (A$0.21 rounding gap embedded, per above) | **A$1,465,606.68** | |
| **OPERATING RESULT** | **A$32,576.80** | **A$390,921.60** | Total Revenue − Total Operating Costs |
| **Operating Margin** | **21.1%** | **21.1%** | Operating Result ÷ Total Revenue |

**Both open financial items from the prior round resolved this round, not left as unactioned discrepancies:** (1) insurance corrected to A$708.34/month, investigated rather than picked between the two prior figures — see `docs/architecture/FINANCIAL-ASSUMPTION-REGISTER.md` for the full derivation; (2) the relief/absence coverage gap is now a real, quantified, propagated line (A$6,128.53/month) rather than an unmodelled zero.

**Explicitly excluded from Operating Result (not a "profit" figure in the full accounting sense):** depreciation/amortisation of startup capex, income tax, interest on any financing, and any allocation of startup capital cost. None of these are modelled anywhere in this venture's canonical layer yet — flagged so the Operating Result figure above is not mistaken for a bottom-line net profit.

## 5. Cash Flow — 24 Months, Table 1 (Planning Case)

**Three distinct concepts, not to be conflated:**
1. **Startup expenditure** — A$251,198 (adopted planning figure), a one-off, pre-opening capital outlay. NOT part of any monthly figure below.
2. **Working capital reserve** — A$85,000-110,000, a separate buffer sized to fund the ramp period specifically.
3. **Cash required to survive the ramp** — what the table below actually measures: the depth of the cumulative OPERATING cash trough before the business becomes self-sustaining. This is NOT the same number as either of the above, though it is conceptually closest to the working capital reserve's own stated purpose.

| Month | Monthly Net Operating Cash Movement | Cumulative Position |
|---|---|---|
| 1 | -A$54,410.88 | -A$54,410.88 |
| 2 | -A$22,121.64 | **-A$76,532.52 (TROUGH)** |
| 3 | +A$884.97 | -A$75,647.55 |
| 4 | +A$22,344.46 | -A$53,303.09 |
| 5 | +A$32,576.80 | -A$20,726.29 |
| 6 | +A$32,576.80 | **+A$11,850.51 (first month cumulatively positive)** |
| 8 | +A$32,576.80 | +A$77,004.11 |
| 12 | +A$32,576.80 | +A$207,311.31 |
| 16 | +A$32,576.80 | +A$337,618.51 |
| 20 | +A$32,576.80 | +A$467,925.71 |
| 24 | +A$32,576.80 | **+A$598,232.91** |

*(Months 7, 9-11, 13-15, 17-19, 21-23 omitted from this table for readability — all at the same steady-state +A$32,576.80/month movement from Month 5 onward; the full 24-row series is reproducible via `tools/master_financial_model.py`.)*

**Chart — Cumulative Cash Position, Months 1-24:**

<svg viewBox="0 0 900 420" width="100%" height="420" role="img" aria-label="Line chart of cumulative operating cash position over 24 months, Table 1 planning case">
  <rect x="0" y="0" width="900" height="420" fill="#FCFBF7"/>
  <line x1="70" y1="313.3" x2="870" y2="313.3" stroke="#8A8B6E" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="75" y="308" font-size="11" fill="#5E5F45">A$0 (break-even cash line)</text>
  <polyline points="70.0,336.9 104.8,346.6 139.6,346.2 174.3,336.5 209.1,322.3 243.9,308.2 278.7,294.0 313.5,279.9 348.3,265.7 383.0,251.6 417.8,237.4 452.6,223.3 487.4,209.1 522.2,195.0 557.0,180.8 591.7,166.7 626.5,152.5 661.3,138.4 696.1,124.2 730.9,110.1 765.7,95.9 800.4,81.7 835.2,67.6 870.0,53.4" fill="none" stroke="#4C6444" stroke-width="2.5"/>
  <circle cx="104.8" cy="346.6" r="5" fill="#B3542A"/>
  <text x="108" y="365" font-size="11" fill="#B3542A">Trough: -A$76,533 (Month 2)</text>
  <circle cx="243.9" cy="308.2" r="5" fill="#4C6444"/>
  <text x="248" y="298" font-size="11" fill="#4C6444">Turns positive: Month 6</text>
  <circle cx="870.0" cy="53.4" r="5" fill="#4C6444"/>
  <text x="700" y="45" font-size="11" fill="#4C6444">Month 24: +A$598,233</text>
  <text x="70" y="405" font-size="11" fill="#5E5F45">Month 1</text>
  <text x="440" y="405" font-size="11" fill="#5E5F45">Month 12</text>
  <text x="820" y="405" font-size="11" fill="#5E5F45">Month 24</text>
  <text x="15" y="345" font-size="10" fill="#5E5F45" transform="rotate(-90 15,345)">-A$76,533</text>
  <text x="15" y="60" font-size="10" fill="#5E5F45" transform="rotate(-90 15,60)">+A$598,233</text>
</svg>

**Reading the chart: the business runs a genuine cash deficit for the first 5 months (deepest at Month 2, -A$76,532.52), funded from the working capital reserve/startup capital — not from operating revenue — before turning cumulatively cash-positive at Month 6 and growing steadily to +A$598,232.91 by Month 24. The negative startup-period cash flow is shown, not hidden behind the positive steady-state figure. The trough and recovery point are both slightly worse than the prior round's figures (was -A$63,658.78 at Month 2, positive from Month 5) — a genuine consequence of modelling the relief/absence cost and corrected insurance realistically, not an error.**

## 6. Startup Capital Requirement — Restated, Not Re-Derived

| Component | Range/Value | Status |
|---|---|---|
| Pre-opening capital (adopted planning figure) | A$251,198 | DECIDED — Anthony's in-principle approval, `data/canonical/startup_costs.yml#adopted_planning_scenarios` |
| Working capital reserve | A$85,000-110,000 | MODELLED |
| Combined bounded range (primary method) | A$357,390-577,180 | CALCULATED |
| Combined, using this venture's own operating-cash-trough as an illustrative cross-check instead of the historical reserve | A$348,922.78-543,712.78 (Table 1) | CALCULATED, `data/models/master_financial_model.yml#funding_requirement_investigation` |

**No single exact funding requirement is established** — the underlying startup-cost reconciliation itself remains genuinely unresolved (`docs/architecture/STARTUP-COST-RECONCILIATION.md`), a real, disclosed limitation, not glossed over.

---

## Changelog

**2026-08-18 (Financial Finalisation round)** — Recomputed every figure in this document against the resolved insurance figure (A$708.34/month, corrected from a flawed A$1,279 midpoint and an unexplained A$400 guess) and the newly-propagated relief/absence coverage allowance (A$6,128.53/month, previously entirely unmodelled). Operating Result fell from A$39,013.67 to A$32,576.80/month (Table 1) — a genuine cost-realism correction, reported plainly. **Table 2 (12/day sensitivity) is now loss-making at steady state** (-A$6,918.20/month), a real finding from this round's corrections. Cash-flow chart regenerated and re-verified via Playwright screenshot.

**2026-08-18 (earlier this date)** — Created per Anthony's explicit Priority 4 instruction: a single current-state financial position document, real dollar figures throughout, no historical clutter, every figure traceable to `docs/architecture/FINANCIAL-FIGURE-REFERENCE.md`. 18/day confirmed as the sole planning case throughout; 6/12 appear only in the explicitly labelled sensitivity table.
