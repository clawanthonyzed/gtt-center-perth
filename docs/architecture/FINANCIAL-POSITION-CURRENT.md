# Financial Position — Current State

**Planning case: 18 clients/day (Table 1).** This is the only operating plan. 12/day and 6/day appear ONLY in the sensitivity table below (§2), always clearly labelled, never as competing plans. Every figure below is current, live-verified against `data/models/master_financial_model.yml` and `data/canonical/cost_ramp.yml` — no historical or superseded figures appear in this document (see `docs/CURRENT-STATE.md` for the historical correction record).

**Terminology used precisely throughout:** "Revenue" = gross booking value. "Operating Costs" = payroll + non-wage overhead. "Operating Result" = Revenue − Operating Costs — this is NOT "profit" in an accounting sense (no depreciation, tax, interest, or startup-capital amortisation is included; see the explicit exclusions note in §4). "Cash Flow" = the accrual-basis monthly movement of Operating Result over time — NOT a true cash-basis forecast (no debtor/creditor timing, no weekly-payroll-timing granularity).

---

## 1. Headline — 18-Client Planning Case

| Metric | Value | Label |
|---|---|---|
| AM clients/day | 18 | VERIFIED (solver-confirmed) |
| PM transaction capacity/day (weekday) | 12.8128 | CALCULATED, `docs/architecture/PM-CAPACITY-RECONCILIATION.md` |
| Total Revenue | **A$154,710.69/month** | CALCULATED |
| Total Operating Costs | **A$115,697.02/month** | CALCULATED |
| **Operating Result** | **A$39,013.67/month** | **CALCULATED** |
| Operating Margin | 25.2% (Operating Result ÷ Revenue) | CALCULATED |
| Annualised Operating Result | A$468,164.04 | CALCULATED (Monthly × 12) |
| Break-even revenue | A$115,696.21/month | CALCULATED |
| Break-even client volume | 12.073 clients/day | CALCULATED |
| Margin of safety | 5.927 clients/day (32.9% above break-even volume) | CALCULATED |
| 24-month cumulative Operating Result | A$752,717.79 | CALCULATED |
| Cash-flow trough | -A$63,658.78 at Month 2 | CALCULATED |
| Month cumulative position turns positive | Month 5 | CALCULATED |

## 2. Sensitivity Table — 6/12/18 Clients/Day, Real Figures Throughout

**18/day is the sole planning case. 6/day and 12/day are sensitivity/downside comparisons only — shown here to demonstrate what happens if actual volume falls short, never presented as alternative plans anywhere else in this venture's documents.**

| Metric | 6 clients/day (SENSITIVITY) | 12 clients/day (SENSITIVITY) | **18 clients/day (PLANNING CASE)** |
|---|---|---|---|
| AM clients/day | 6 | 12 | **18** |
| PM transactions/day (weekday) | 12.8128 (unaffected by AM volume — capacity-constrained) | 12.8128 | **12.8128** |
| AM revenue/day (weekday) | A$1,500.00 | A$3,000.00 | **A$4,500.00** |
| PM revenue/day (weekday) | A$1,499.04 | A$1,499.04 | **A$1,499.04** |
| Total daily revenue (weekday) | A$2,999.04 | A$4,499.04 | **A$5,999.04** |
| Monthly revenue | A$75,720.69 | A$115,215.69 | **A$154,710.69** |
| Annualised revenue | A$908,648.28 | A$1,382,588.28 | **A$1,856,528.28** |
| Direct labour | A$101,717.02 | A$101,717.02 | **A$101,717.02** |
| — of which superannuation (12%) | A$10,735.31 | A$10,735.31 | **A$10,735.31** |
| — of which workers comp (1.7%, PLACEHOLDER) | A$1,520.83 | A$1,520.83 | **A$1,520.83** |
| Other opex (non-wage overhead) | A$13,980.00 | A$13,980.00 | **A$13,980.00** |
| **Total opex** | **A$115,697.02** | **A$115,697.02** | **A$115,697.02** |
| **Monthly Operating Result** | **-A$39,976.33** | **-A$481.33** | **A$39,013.67** |
| Annualised Operating Result | -A$479,715.96 | -A$5,775.96 | **A$468,164.04** |
| Operating Margin | -52.8% | -0.4% | **25.2%** |
| Break-even revenue | A$115,696.21/month (same fixed cost base at every volume) | A$115,696.21/month | **A$115,696.21/month** |
| Break-even clients/day | 12.073/day | 12.073/day | **12.073/day** |
| Margin of safety (clients/day) | -6.073 (BELOW break-even) | -0.073 (BELOW break-even) | **+5.927 (ABOVE break-even)** |
| 24-month cumulative operating result | N/A — no ramp/ 24-month model exists for this sensitivity point (steady-state comparison only, never operated as a real ramping plan) | **-A$17,653.46** (Table 2's actual modelled 24-month result) | **A$752,717.79** |
| Cash-flow trough | N/A — same reason | **-A$116,126.66 at Month 4** | **-A$63,658.78 at Month 2** |
| Month cumulative turns positive | N/A | **Never within 24 months — remains cumulatively negative throughout** | **Month 5** |

**Note on why labour/opex are identical across all three columns:** this reflects a disclosed, pre-existing modelling limitation (`conflict_am_labor_ramp_unmodelled` in `data/canonical/cost_ramp.yml`) — committed headcount is fixed at the 18-client design regardless of actual booking volume, since staff are rostered to the committed design, not flexed down. This makes the 6/12-client columns a genuine downside stress test (revenue drops, costs do not), not a lower-cost alternative plan.

**6 clients/day is genuinely loss-making** (-A$39,976.33/month) at this fixed cost base. **12 clients/day (Table 2) is marginally loss-making at steady state under the corrected PM revenue basis** (-A$481.33/month) and never recovers its cumulative cash position within 24 months. **Only 18 clients/day clears break-even with a real margin of safety.**

## 3. Break-Even — Both Forms, Plain English

**At approximately A$115,696/month of total revenue, the business covers its modelled operating costs (payroll + non-wage overhead) and neither makes nor loses money.**

| Form | Value | Calculation |
|---|---|---|
| Break-even revenue | **A$115,696.21/month** | Total Operating Costs (A$115,697.02) − PM Revenue (A$36,225.69, held fixed) = AM revenue needed (A$79,471.33) → converted back to a total-revenue figure |
| Break-even client volume | **12.073 clients/day** | AM revenue needed ÷ A$250/client, weighted across weekday and Saturday operating days |

**18-client target vs. break-even, both forms:**

| | Break-even | 18-client target | Buffer (dollar/client) | Buffer (%) |
|---|---|---|---|---|
| Revenue | A$115,696.21/month | A$154,710.69/month | +A$39,014.48/month | +33.7% |
| Client volume | 12.073/day | 18.000/day | +5.927/day | +49.1% |

**In plain terms: the 18-client planning case generates roughly A$39,000/month more revenue than the business needs just to break even, and could lose nearly 6 clients/day of volume (about a third of the committed target) before falling below break-even.** This is a real, calculable margin of safety — not a vague reassurance.

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
| Insurance (**PLACEHOLDER**) | A$400.00 | A$4,800.00 | §4 — **see the discrepancy note directly below this table** |
| GTT supplies | A$400.00 | A$4,800.00 | §4 |
| Consumables | A$800.00 | A$9,600.00 | §4 |
| Laundry | A$350.00 | A$4,200.00 | §4 |
| Marketing | A$1,500.00 | A$18,000.00 | §4 |
| Software (Fresha + email + internet/phone) | A$280.00 | A$3,360.00 | §4 |
| Cleaning | A$600.00 | A$7,200.00 | §4 |
| Accounting/bookkeeping | A$500.00 | A$6,000.00 | §4 |
| Miscellaneous/contingency | A$500.00 | A$6,000.00 | §4 |
| **Non-wage overhead subtotal** | **A$13,980.00** | A$167,760.00 | Matches `cost_ramp.yml`'s canonical figure exactly |
| **TOTAL OPERATING COSTS** | **A$115,697.02** (A$0.21 rounding gap embedded, per above) | **A$1,388,364.24** | |
| **OPERATING RESULT** | **A$39,013.67** | **A$468,164.04** | Total Revenue − Total Operating Costs |
| **Operating Margin** | **25.2%** | **25.2%** | Operating Result ÷ Total Revenue |

**Discrepancy found and disclosed, not silently resolved:** `data/canonical/opex.yml`'s own insurance record (`opex_insurance_modelled`) was revised 2026-08-16 to A$1,279.00/month (a "revised provisional placeholder"), and the model's own sensitivity-insurance function treats A$1,279 as the "current, modelled" figure — **but the actual A$13,980.00 non-wage-overhead total that flows through every P&L figure in this venture's canonical model was never recomputed to include that revision** — it still uses the original A$400.00/month insurance figure (`docs/profit-loss-tables.md` §4's 13-line breakdown, cross-checked in `tools/cost_ramp_model.py`'s own source comment). If the A$1,279 figure were actually propagated into the A$13,980 total, non-wage overhead would rise to **A$14,859.00/month** (+A$879.00/month), reducing the Operating Result to **A$38,134.67/month**. **Not corrected in this document or the canonical model this round** — this is a newly-surfaced internal inconsistency requiring Anthony's decision on which insurance figure to treat as current before it is propagated, consistent with "show current model → proposed model → financial impact → reason, then update," not a silent patch.

**Explicitly excluded from Operating Result (not a "profit" figure in the full accounting sense):** depreciation/amortisation of startup capex, income tax, interest on any financing, and any allocation of startup capital cost. None of these are modelled anywhere in this venture's canonical layer yet — flagged so the Operating Result figure above is not mistaken for a bottom-line net profit.

## 5. Cash Flow — 24 Months, Table 1 (Planning Case)

**Three distinct concepts, not to be conflated:**
1. **Startup expenditure** — A$251,198 (adopted planning figure), a one-off, pre-opening capital outlay. NOT part of any monthly figure below.
2. **Working capital reserve** — A$85,000-110,000, a separate buffer sized to fund the ramp period specifically.
3. **Cash required to survive the ramp** — what the table below actually measures: the depth of the cumulative OPERATING cash trough before the business becomes self-sustaining. This is NOT the same number as either of the above, though it is conceptually closest to the working capital reserve's own stated purpose.

| Month | Monthly Net Operating Cash Movement | Cumulative Position |
|---|---|---|
| 1 | -A$47,974.01 | -A$47,974.01 |
| 2 | -A$15,684.77 | **-A$63,658.78 (TROUGH)** |
| 3 | +A$7,321.84 | -A$56,336.94 |
| 4 | +A$28,781.33 | -A$27,555.61 |
| 5 | +A$39,013.67 | **+A$11,458.06 (first month cumulatively positive)** |
| 6 | +A$39,013.67 | +A$50,471.73 |
| 8 | +A$39,013.67 | +A$128,499.07 |
| 12 | +A$39,013.67 | +A$284,553.75 |
| 16 | +A$39,013.67 | +A$440,608.43 |
| 20 | +A$39,013.67 | +A$596,663.11 |
| 24 | +A$39,013.67 | **+A$752,717.79** |

*(Months 7, 9-11, 13-15, 17-19, 21-23 omitted from this table for readability — all at the same steady-state +A$39,013.67/month movement from Month 5 onward; the full 24-row series is reproducible via `tools/master_financial_model.py`.)*

**Chart — Cumulative Cash Position, Months 1-24:**

<svg viewBox="0 0 900 420" width="100%" height="420" role="img" aria-label="Line chart of cumulative operating cash position over 24 months, Table 1 planning case">
  <rect x="0" y="0" width="900" height="420" fill="#FCFBF7"/>
  <line x1="70" y1="323.7" x2="870" y2="323.7" stroke="#8A8B6E" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="75" y="318" font-size="11" fill="#5E5F45">A$0 (break-even cash line)</text>
  <polyline points="70.0,340.9 104.8,346.6 139.6,343.9 174.3,333.6 209.1,319.6 243.9,305.6 278.7,291.6 313.5,277.6 348.3,263.6 383.0,249.5 417.8,235.5 452.6,221.5 487.4,207.5 522.2,193.5 557.0,179.5 591.7,165.5 626.5,151.5 661.3,137.5 696.1,123.5 730.9,109.5 765.7,95.5 800.4,81.5 835.2,67.5 870.0,53.4" fill="none" stroke="#4C6444" stroke-width="2.5"/>
  <circle cx="104.8" cy="346.6" r="5" fill="#B3542A"/>
  <text x="108" y="365" font-size="11" fill="#B3542A">Trough: -A$63,659 (Month 2)</text>
  <circle cx="209.1" cy="319.6" r="5" fill="#4C6444"/>
  <text x="213" y="312" font-size="11" fill="#4C6444">Turns positive: Month 5</text>
  <circle cx="870.0" cy="53.4" r="5" fill="#4C6444"/>
  <text x="700" y="45" font-size="11" fill="#4C6444">Month 24: +A$752,718</text>
  <text x="70" y="405" font-size="11" fill="#5E5F45">Month 1</text>
  <text x="440" y="405" font-size="11" fill="#5E5F45">Month 12</text>
  <text x="820" y="405" font-size="11" fill="#5E5F45">Month 24</text>
  <text x="15" y="345" font-size="10" fill="#5E5F45" transform="rotate(-90 15,345)">-A$63,659</text>
  <text x="15" y="60" font-size="10" fill="#5E5F45" transform="rotate(-90 15,60)">+A$752,718</text>
</svg>

**Reading the chart: the business runs a genuine cash deficit for the first 4 months (deepest at Month 2, -A$63,658.78), funded from the working capital reserve/startup capital — not from operating revenue — before turning cumulatively cash-positive at Month 5 and growing steadily to +A$752,717.79 by Month 24. The negative startup-period cash flow is shown, not hidden behind the positive steady-state figure.**

## 6. Startup Capital Requirement — Restated, Not Re-Derived

| Component | Range/Value | Status |
|---|---|---|
| Pre-opening capital (adopted planning figure) | A$251,198 | DECIDED — Anthony's in-principle approval, `data/canonical/startup_costs.yml#adopted_planning_scenarios` |
| Working capital reserve | A$85,000-110,000 | MODELLED |
| Combined bounded range (primary method) | A$357,390-577,180 | CALCULATED |
| Combined, using this venture's own operating-cash-trough as an illustrative cross-check instead of the historical reserve | A$336,048.78-530,838.78 (Table 1) | CALCULATED, `data/models/master_financial_model.yml#funding_requirement_investigation` |

**No single exact funding requirement is established** — the underlying startup-cost reconciliation itself remains genuinely unresolved (`docs/architecture/STARTUP-COST-RECONCILIATION.md`), a real, disclosed limitation, not glossed over.

---

## Changelog

**2026-08-18** — Created per Anthony's explicit Priority 4 instruction: a single current-state financial position document, real dollar figures throughout, no historical clutter, every figure traceable to `docs/architecture/FINANCIAL-FIGURE-REFERENCE.md`. 18/day confirmed as the sole planning case throughout; 6/12 appear only in the explicitly labelled sensitivity table.
