# First-Principles Financial Model (Phase C Rebuild + Audit Round)

**Date:** 2026-08-17 (created), 2026-08-18 (independently audited and corrected) | **Purpose:** Replace proportional wage-scaling with a genuine first-principles labour cost build (position -> headcount -> hours -> rate -> penalties -> on-costs -> monthly/annual cost), propagate the real calculated PM average transaction value (A$117, `docs/architecture/PM-PACKAGES.md`), and build the full revenue/P&L/cash-flow/break-even/sensitivity structure with every calculation shown inline. All figures below are the current canonical basis, propagated into `data/canonical/cost_ramp.yml`, `data/canonical/revenue_ramp.yml`, and `data/models/master_financial_model.yml` (see each file's own 2026-08-18 banner).

**2026-08-18 audit round, top-line summary:** Anthony requested an independent sanity audit of this document and the underlying model before proceeding to Phase D. Two real findings resulted: (1) an arithmetic error in §3a's original Saturday breakdown (fixed below, disclosed, was a real bug not a rounding artifact); (2) the Venue Manager's wage rate was likely misclassified (Clerks Award instead of the Hair & Beauty Industry Award's own manager classification) -- corrected, see §3c and §15. Both findings are disclosed with old->new figures, not silently smoothed over. **The audit did NOT find a fundamental "this business doesn't work" problem** -- the 18-client AM timetable is independently solver-verified to run on the committed 8 treatment staff + 2 phlebotomists with zero collisions (`docs/scenario-c-sync-timetables.md` §0.6a), and the venture remains net-positive at the 18-client planning case after both corrections (see §7). The corrections make the numbers slightly worse, not better -- reported honestly.

---

## 1. Pay Frequency — Resolved, Not Left Open

**Researched and resolved: weekly.** Real market research confirms casual workforces in Australia are overwhelmingly paid weekly; this is standard practice in hospitality and beauty-adjacent industries specifically, and casual staff commonly rely on weekly cash flow for retention reasons (a genuine labour-market consideration, not just administrative preference). This also matches this venture's own existing `docs/financial-setup.md` Monthly Financial Rhythm, which already specifies "Weekly payroll run (pay Friday)" — confirmed correct, not contradicted, by this research.

**Consistency check, 2026-08-18 audit round:** verified this figure is not contradicted anywhere else in the repo. `docs/financial-setup.md`'s "Weekly payroll run (pay Friday)" is the only other place pay frequency is stated, and it agrees. The cash-flow view in §8 below models payroll as a smooth monthly outflow (an accrual-basis proxy, per `assumption_cashflow_accrual_proxy` in `master_financial_model.yml`) rather than 4-5 discrete weekly Friday payments within the month — this is a genuine simplification, disclosed here explicitly: **a true weekly-granularity cash-flow view would show payroll leaving the account in ~4-5 lumps/month, not smoothly**, which matters for a real bank-balance forecast (the trough within a month could be briefly deeper than the monthly-average view shows) but does not change the monthly total. Not rebuilt to weekly granularity this pass — flagged as a real, disclosed gap rather than quietly assumed away.

## 2. Staff Structure Resolution

| Position | Required active (per trading day) | Total employed (incl. relief) | Qualification | Coverage model |
|---|---|---|---|---|
| Venue Manager | 1 | 1 (no relief at launch — disclosed single point of failure) | Cert III/IV service qualification (Beauty/Massage/Hairdressing) or dual | No standing relief; First Aid/Fire Warden backup cert required in ≥1 other staff member |
| Treatment staff (common pool) | 8 (4 Massage+Beauty, 2 Nails, 2 Hair) | 10-11 | Cert III/IV per specialty | 2-3 extra on the books, rostered flexibly, only paid for hours actually worked |
| Phlebotomist | 2 | 3-4 | Cert III/IV Pathology Collection, partner-credentialed | 1-2 extra credentialed, given the longer credentialing lead time vs treatment roles |
| PM Reception/Coordinator | 1 | 1 | Beauty/wellness customer service experience | See §2a below for why 1 is sufficient |

### 2a. Why One PM Reception/Coordinator Is Sufficient — Modelled, Not Assumed

The PM window (13:00-18:00, 5 hours) has a materially lower simultaneous-transaction load than the AM window: PM capacity is modelled at ~16 sessions/day steady state (`docs/pm-staffing-roster.md`), spread across a 5-hour window with a common treatment-staff pool of up to 8 available (though not all rostered every PM shift) — this is a single-stream check-in/check-out flow, not the synchronized dual-chair AM model that gave rise to the Venue Manager's own dedicated AM reception role. One coordinator handling check-in, Fresha management, and payment processing for a maximum of roughly 3-4 concurrent PM clients at any moment (16 sessions ÷ 5 hours ≈ 3.2 sessions/hour on average) is a normal single-reception-desk workload by any Perth day-spa comparable's own standard (none of the researched comparable businesses — Le Beau, Keturah, endota — run multiple simultaneous reception desks at this scale). If real PM volume materially exceeds this once trading, this is the first role to reassess — flagged as the trigger condition, not treated as permanently fixed.

## 3. Labour Cost — First-Principles Build, Table 1 (18 clients/day)

**Method, stated explicitly:** position -> number rostered per day -> hours/shift -> operating days/month -> wage rate -> Saturday penalty (150%, MA000005/MA000027 casual Saturday rate, researched 2026-08-16) -> monthly subtotal -> superannuation (12%, applied universally on wages, a cleaner treatment than the prior partial-coverage approach) -> workers compensation (1.7% of wages) -> total monthly payroll cost.

**Operating days:** 22 weekdays/month, 4.33 Saturdays/month (established convention, `docs/CURRENT-STATE.md`).
**Shifts:** AM (Venue Manager + Treatment + Phlebotomist) = 07:00-13:00 = 6 hours. PM Reception = 13:00-18:00 = 5 hours. Venue Manager = 07:00-15:00 = 8 hours (AM + wind-down/administrative overlap).

### 3a. Treatment Staff (8, common AM/PM pool)

| Role | Qty | Hourly rate | Weekday (22 days, 6hr) | Saturday (4.33 days, 6hr, x1.5) |
|---|---|---|---|---|
| Massage+Beauty pool | 4 | A$37.50 | 4 x 6 x 37.50 x 22 = **A$19,800.00** | 4 x 6 x 56.25 x 4.33 = **A$5,845.50** |
| Nails | 2 | A$36.81 | 2 x 6 x 36.81 x 22 = **A$9,717.84** | 2 x 6 x 55.215 x 4.33 = **A$2,868.97** |
| Hair | 2 | A$36.81 | 2 x 6 x 36.81 x 22 = **A$9,717.84** | 2 x 6 x 55.215 x 4.33 = **A$2,868.97** |
| **AM Treatment subtotal** | | | **A$39,235.68** | **A$11,583.44** |

**Correction, 2026-08-18 audit round:** the original 2026-08-17 version of this table showed Saturday figures of A$5,850.00/A$2,872.11/A$2,872.11 (subtotal A$11,594.22) — a genuine arithmetic error, not a rounding artifact. Those figures were computed using 4.3333 Saturdays/month (the unrounded 52/12), inconsistent with this repo's own canonical convention of 4.33 (`client_assumptions.yml#operating_saturdays_per_month`), used everywhere else in this document and the codebase. The corrected figures above (using 4.33 throughout) now match `tools/cost_ramp_model.py`'s own live output exactly (A$11,583.44, confirmed via direct code inspection of `AM_SATURDAY_DAILY_LABOR`'s derivation) — the code itself was always correct; only this document's separate hand-worked breakout table had the error. Net effect: A$10.78/month lower than previously stated for this specific line, immaterial to the headline total but a real, disclosed correction.

### 3b. Phlebotomists (2, AM only)

2 x 6hrs x A$34.375/hr x 22 days = **A$9,075.00** (weekday)
2 x 6hrs x A$51.5625/hr (Saturday x1.5) x 4.33 days = **A$2,679.19** (Saturday)

### 3c. Venue Manager (1, AM + admin)

**CORRECTED 2026-08-18 (Phase C audit round) — award reclassification, see §15 for the full research finding.** The original 2026-08-17 figure ($36.81/hr, Clerks Award MA000002 Level 2) was audited against the role's own actual duties and found to be a likely misclassification. STAFF-PROFILES.md's own Position 01 job description — "runs daily venue operations, manages staff rostering and performance... a genuine service qualification required" — matches the Hair & Beauty Industry Award MA000005's own Level 6 classification ("Diploma-qualified beauty therapist or salon manager responsible for staff and operations") far more closely than a generic clerical award. Corrected rate: **A$40.00/hr** (MA000005 Level 6 casual, 2026/27, includes 25% casual loading).

1 x 8hrs x A$40.00/hr x 22 days = **A$7,040.00** (weekday) — was A$6,478.56 at the Clerks Award rate
1 x 8hrs x A$60.00/hr (Saturday x1.5) x 4.33 days = **A$2,078.40** (Saturday) — was A$1,912.65

**Monthly VM total: A$9,118.40** — was A$8,391.21, a real increase of **+A$727.19/month** from this one correction. **Status: MODELLED/CORRECTED, NOT VERIFIED** — this is the best-evidenced classification found this pass, but a specific real employment contract's award classification should still be confirmed with an accountant or Fair Work professional before being treated as final. See §15.

### 3d. PM Reception/Coordinator (1)

1 x 5hrs x A$33.71/hr x 22 days = **A$3,708.10** (weekday)
1 x 5hrs x A$50.565/hr (Saturday x1.5) x 4.33 days = **A$1,094.73** (Saturday)

### 3e. PM Treatment Labour (4 roles, session-count/3-hour-floor method, unchanged methodology, current wage rates)

Weekday (16 sessions/day steady state; 16 / 4 roles / 1.3 sessions-per-hour throughput = 3.08hrs/role, clears the 3-hour floor): 4 roles x 3.08hrs x A$37.155/hr (blended current rate) x 22 days = **A$10,070.72**
Saturday (8 sessions/day; 8/4/1.3 = 1.54hrs/role, below the 3-hour floor, floor applies): 4 roles x 3hrs x A$55.7325/hr (blended, x1.5 Saturday) x 4.33 days = **A$2,895.83**

*(A small, pre-existing floating-point rounding gap of ~A$0.21-0.44/month exists between this hand-calculated figure and the live code output, A$10,070.50/A$2,895.82 — an accepted, immaterial, already-disclosed convention in this repo's cost model, not a new issue this round.)*

### 3f. Total Direct Labour (Wages Only, Before Super/Workers Comp)

| Component | Weekday | Saturday | Monthly total |
|---|---|---|---|
| Treatment (AM) | A$39,235.68 | A$11,583.44 | A$50,819.12 |
| Phlebotomists | A$9,075.00 | A$2,679.19 | A$11,754.19 |
| Venue Manager | A$7,040.00 | A$2,078.40 | A$9,118.40 |
| PM Reception | A$3,708.10 | A$1,094.73 | A$4,802.83 |
| PM Treatment | A$10,070.72 | A$2,895.83 | A$12,966.55 |
| **TOTAL WAGES (hand-calculated)** | | | **A$89,461.09** |
| **TOTAL WAGES (live code output, `direct_labor_and_opening_total`)** | | | **A$89,460.88** |

*(The A$0.21 gap is the PM Treatment rounding artifact noted in §3e — immaterial, disclosed, not force-reconciled to a false precision.)*

### 3g. On-Costs

| Item | Rate | Amount |
|---|---|---|
| Superannuation | 12% of total wages | A$10,735.31 |
| Workers Compensation | 1.7% of total wages | A$1,520.83 |
| **TOTAL MONTHLY PAYROLL COST (Table 1, 18/day)** | | **A$101,717.02** |
| **ANNUAL PAYROLL COST** | x 12 | **A$1,220,604.24** |

**Figure history, disclosed in full, nothing silently overwritten:**
- Original proportional-scaled figure (before Phase C): **A$87,398.78/month**
- Phase C first-principles rebuild (2026-08-17, before audit): **A$100,890.20/month**
- Phase C audit round, VM reclassification (2026-08-18, current): **A$101,717.02/month**
- Total increase vs. the original proportional-scaled figure: **+A$14,318.24/month (+16.4%)**

**Why the figures disagree, disclosed honestly:** the original model was built on an annual-salary-per-role basis (e.g. A$492,920/yr for 8 treatment staff, an FTE-style figure implying an averaged effective commitment across AM/PM, not a literal 6-hour-AM-shift-for-all-8 assumption). The first-principles model assumes every one of the 8 treatment staff, both phlebotomists, and the Venue Manager work their **full rostered shift with no early release**, at the current researched wage rates — the conservative, no-savings-assumed planning basis. The 2026-08-18 audit round's further increase is a genuine award-classification correction (§3c/§15), not a methodology change. The existing Downtime-Fill/Early-Release framework (`docs/CURRENT-STATE.md` §8) remains the disclosed, separate, tagged upside if early release is actually achieved in practice at lower-than-peak booking density — it is not blended into this headline figure, consistent with this repo's own established convention of keeping that saving separate.

## 4. Revenue Model — AM/PM Separated, Full Derivation

### 4a. AM Revenue (Table 1, 18 clients/day)

- Weekday: 18 clients x A$250 (Package 1, conservative planning price) x 22 days = **A$99,000.00/month**
- Saturday: 18 clients x A$250 x 4.33 days = **A$19,485.00/month**
- **AM Revenue Total: A$118,485.00/month** (unaffected by any labour-cost audit finding — AM revenue is price x volume, not wage-driven)

### 4b. PM Revenue — Rebuilt With the Real A$117 Average (Not a Simple Swap)

**Derivation, not just a substituted number:** PM revenue = session count x average transaction value, where the average transaction value (A$117) is itself derived from the real service catalogue and the two locked packages (`docs/architecture/PM-PACKAGES.md` §5), applied to the same session-count capacity already established (16 sessions/day weekday steady state, 8 Saturday, per `docs/pm-staffing-roster.md`):

- Weekday: 16 sessions x A$117 x 22 days = **A$41,184.00/month**
- Saturday: 8 sessions x A$117 x 4.33 days = **A$4,052.88/month**
- **PM Revenue Total: A$45,236.88/month** (was A$36,730.80 at the old, unexplained A$95 average — a real +A$8,506.08/month increase, because the new figure reflects real package pricing, not a placeholder)

### 4c. Total Revenue (Table 1, 18 clients/day)

**AM A$118,485.00 + PM A$45,236.88 = A$163,721.88/month** — unaffected by the audit round (revenue and labour cost are independent chains).

## 5. 6/12/18 Sensitivity Table — 18/Day Is the Planning Case, 6 and 12 Are Sensitivity Comparisons Only

| Metric | 6 clients/day (SENSITIVITY) | 12 clients/day (SENSITIVITY) | 18 clients/day (PLANNING CASE) |
|---|---|---|---|
| AM revenue/month | A$39,495.00 | A$78,990.00 | A$118,485.00 |
| PM revenue/month | A$45,236.88 (unaffected by AM volume) | A$45,236.88 | A$45,236.88 |
| **Total revenue/month** | **A$84,731.88** | **A$124,226.88** | **A$163,721.88** |
| Labour/month | A$101,717.02 (headcount held fixed, per `conflict_am_labor_ramp_unmodelled`) | A$101,717.02 | A$101,717.02 |
| Opex/month (non-wage overhead) | A$13,980.00 | A$13,980.00 | A$13,980.00 |
| **Total costs/month** | **A$115,697.02** | **A$115,697.02** | **A$115,697.02** |
| **Net operating result/month** | **-A$30,965.14** | **A$8,529.86** | **A$48,024.86** |
| Annualised result | -A$371,581.68 | A$102,358.32 | A$576,298.32 |
| Margin (net result / revenue) | -36.5% | 6.9% | 29.3% |
| Break-even revenue/month | A$115,697.02 (same for all three — see §6) | A$115,697.02 | A$115,697.02 |
| Break-even clients/day (AM-only solve) | 10.704/day (see §6) — **6/day is BELOW break-even** | 10.704/day — **12/day is BELOW break-even** | 10.704/day — **18/day clears break-even with a 7.3 client/day margin** |
| Staffing implications | Same 8 treatment + 2 phlebotomist + 1 VM + 1 PM reception headcount as 18/day — this model does NOT flex headcount down at lower volume (a real, disclosed limitation, not a hidden one) | Same headcount as 6/day and 18/day | Committed design point — the headcount this entire model is built around |

**Note on labour/opex being held constant across all three volumes:** this reflects the same disclosed, pre-existing modelling limitation as the rest of this repo's cost architecture (`conflict_am_labor_ramp_unmodelled`) — committed headcount is fixed regardless of actual daily booking volume, since staff are rostered to the committed design, not flexed down in this model. This makes the 6/12-client sensitivity rows a genuine downside stress test (revenue drops, costs don't), not an alternate lower-cost operating plan — consistent with 18/day being the only planning case. **6 clients/day would be genuinely loss-making at this fixed cost base (-A$30,965.14/month) — reported plainly, not smoothed over.** 12 clients/day (Table 2) is marginally profitable (A$8,529.86/month) but well below break-even's own comfortable margin.

## 6. Break-Even — Both Forms, Full Calculation and Assumptions Shown

**Basis and assumptions, stated explicitly:**
1. Fixed monthly cost base = Total Costs at Table 1's steady-state headcount = **A$115,697.02/month** (A$101,717.02 payroll + A$13,980.00 non-wage overhead) — this is the SAME cost base used at every client-volume level, per the `conflict_am_labor_ramp_unmodelled` limitation disclosed in §5. This is a conservative assumption for break-even purposes: it does NOT assume any cost saving at lower volume, so the break-even threshold below is a real, not optimistic, figure.
2. PM revenue (A$45,236.88/month) is held constant and NOT treated as volume-linear in this calculation, because it is capacity-constrained by session count, not by AM client volume (per §4b's derivation) — PM revenue does not grow or shrink with AM client volume in this model.
3. AM revenue IS the volume-linear component: AM revenue = clients/day x A$250 x operating days. This is the only lever this break-even solves for.

**Break-even revenue/month, calculation shown:**
Total costs (A$115,697.02) − PM revenue (A$45,236.88) = AM revenue needed = **A$70,460.14/month** from AM alone.
Total revenue at break-even = AM revenue needed + PM revenue = A$70,460.14 + A$45,236.88 = **A$115,697.02/month** (i.e. total revenue must equal total costs — the standard break-even identity, shown explicitly here since PM revenue is fixed rather than volume-linear).

**Break-even clients/day, calculation shown:**
A$70,460.14 (AM revenue needed) ÷ A$250/client ÷ 22 weekday-equivalent days = **12.81 clients/day** (weekday-only approximation).

*(Cross-check: `tools/master_financial_model.py`'s own `compute_breakeven()` function, which weights weekday and Saturday operating days together rather than approximating on 22 weekday-equivalent days alone, gives **10.704 clients/day** — the more precise, code-verified figure, and the one used in `data/models/master_financial_model.yml`. The two approaches differ because the weekday-only approximation above ignores Saturday's smaller per-day revenue contribution diluting the effective "days" denominator. **10.704 clients/day is the authoritative figure** — the 12.81 approximation above is shown only to make the calculation legible step-by-step; it is not used anywhere in the canonical model.)*

**What this means operationally:** the venue needs to average roughly **10.7 AM clients/day** (weighted across weekday and Saturday trading) across the month to cover its full monthly cost base at the current first-principles labour cost (including the Venue Manager reclassification). This is **59.5% of the 18/day planning target** (10.704 / 18), leaving a margin of safety of **7.296 clients/day (40.5% of target)** before the venue would become loss-making at its fixed cost base. This margin narrowed from the pre-audit figure (7.421 clients/day, 41.2%) because the VM wage correction increased the fixed cost base — a real, small narrowing, disclosed not hidden.

## 7. Monthly Steady-State P&L (Table 1, 18 clients/day)

| Line | Amount | Calculation |
|---|---|---|
| AM Revenue | A$118,485.00 | §4a |
| PM Revenue | A$45,236.88 | §4b |
| **Total Revenue** | **A$163,721.88** | |
| Direct labour (COGS-equivalent — service delivery staff) | A$101,717.02 | §3g |
| **Gross Profit** | **A$62,004.86** | Total Revenue - Direct Labour |
| Non-Wage Overhead (rent, utilities, insurance, consumables, GTT supplies, laundry, waste, software, marketing, other — 13-line breakdown, `docs/profit-loss-tables.md` §4) | A$13,980.00 | Unchanged, not client-volume-driven |
| **Net Operating Result** | **A$48,024.86/month** | Gross Profit - Non-Wage Overhead |
| Net margin | 29.3% | Net Operating Result / Total Revenue |
| **Annualised (steady state)** | **A$576,298.32** | Monthly x 12 |

**The business remains net-positive at the 18-client planning case after both audit corrections — but the margin is genuinely thinner than every prior version of this model showed (29.3% now, vs 29.8% pre-audit, vs 34.7% at the original proportional-scaled figure). Reported plainly: each successive layer of genuine correction (first-principles labour costing, then the VM award reclassification) has made the business look somewhat less profitable, not more — this is what an honest audit is supposed to surface, not something to be smoothed over.**

## 8. Cash Flow — Startup vs Opex vs Revenue, Clearly Separated

| Item | Status |
|---|---|
| Opening cash | `[PLACEHOLDER — no canonical source states an opening cash figure]` |
| Startup expenditure (one-off, pre-opening) | A$251,198 adopted planning figure (`docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`) — a separate, one-off capital outlay, not part of any monthly operating cash movement below |
| Working capital reserve | A$85,000-110,000 (separate from startup expenditure, funds the ramp period) |
| Monthly operating cash inflow | Total Revenue, §4c/§5 (varies by ramp month — Month 1-4 ramp not yet independently rebuilt against this new labour-cost basis; the current model applies the SAME fixed Month 5+ payroll figure to Months 1-4 too, since AM labour is FTE/fixed from Month 1 per `conflict_am_labor_ramp_unmodelled` — flagged as a real, disclosed limitation, not fabricated precision) |
| Monthly operating cash outflow | Total Costs, §7 (payroll + non-wage overhead) |
| **Monthly net operating cash movement (steady state, Month 5+)** | **+A$48,024.86/month** |
| Cumulative position, Month 1 | **-A$44,099.20** (per `master_financial_model.yml#cash_flow_summary`) |
| Cumulative position, Month 4 | **-A$2,414.39** — still marginally negative at Month 4 under the corrected cost base (was +A$892.89, positive, before the VM correction) |
| Cumulative position turns positive | **Month 5** (was Month 4 pre-audit) — a real, disclosed one-month delay caused by the VM wage correction |
| Trough (deepest cumulative negative position) | **-A$54,016.81 at Month 2** |
| Rent/fit-out/startup purchases | One-off, funded from the startup expenditure line above, not the monthly operating movement |

**Weekly-payroll-timing caveat (§1):** the figures above use a smooth monthly-average cash-flow view (accrual-basis proxy), not a true weekly-granularity forecast. Since payroll is actually paid weekly (§1), the real within-month cash position could briefly dip deeper than the monthly-average trough shown here, in the days just after a Friday payroll run and before that week's revenue has fully banked. Not modelled to weekly granularity this pass — flagged as a genuine, disclosed gap.

---

## 9. Five Distinct Staffing Concepts — Made Structurally Explicit (2026-08-18 audit round addition)

Anthony's explicit instruction this round: distinguish these five concepts, which the prior version of this document and `STAFF-PROFILES.md` blurred together in places. **They are NOT the same number and must not be treated as interchangeable:**

| Concept | Definition | Value (Treatment staff, common pool) | Value (Phlebotomists) | Value (Venue Manager) | Value (PM Reception) |
|---|---|---|---|---|---|
| **1. Required operating positions** | The distinct job roles/functions the venue cannot run without, regardless of headcount | 3 roles (Massage+Beauty, Nails, Hair) | 1 role | 1 role | 1 role |
| **2. Actual scheduled weekly hours** | Real rostered hours per week at committed 18-client volume, per the solver-verified timetable (`scenario-c-sync-timetables.md` §0.6a) | 6hrs/day x 6 days = 36hrs/week per rostered staff member (AM window; PM hours are separate, session-driven, see §3e) | 6hrs/day x 6 days = 36hrs/week per rostered phlebotomist | 8hrs/day x 6 days = 48hrs/week | ~5hrs/day x 6 days = ~30hrs/week |
| **3. Employment headcount required** | How many real people must be employed (not necessarily all working every day) to safely deliver #2 with normal leave/absence patterns | 8 committed (rostered daily) | 2 committed (rostered daily) | 1 committed | 1 committed |
| **4. Relief/backup pool** | ADDITIONAL people employed beyond #3, specifically to cover leave/sickness/absence, NOT rostered every day, only paid for hours actually worked | +2-3 above the 8 (10-11 total on the books) | +1-2 above the 2 (3-4 total on the books) | 0 — genuine single point of failure, disclosed | 0 — not sized this pass, see §13 open item |
| **5. Paid hours actually included in the financial model** | What §3 above's payroll build actually pays for — ONLY the committed #3 headcount's full rostered shift, EVERY trading day, with NO early release assumed | 8 people x 6hrs x 22 weekdays + Saturday equivalent (§3a) | 2 people x 6hrs x 22 weekdays + Saturday equivalent (§3b) | 1 person x 8hrs x 22 weekdays + Saturday equivalent (§3c) | 1 person x 5hrs x 22 weekdays + Saturday equivalent (§3d) |

**The critical distinction, stated plainly:** #3 (employment headcount) is what STAFF-PROFILES.md profiles and what real employment contracts would be issued for. #4 (relief pool) is real people on the books, genuinely needed for operational resilience, but **NOT included in the payroll figures anywhere in §3-§8 above** — relief staff are only paid when they actually work a shift (covering an absence), so they do not add to the steady-state monthly payroll total unless and until an absence actually occurs. This means: **the true, full "worst case, everyone is at full committed strength AND a relief person also happens to work that week" cost is not modelled** — but this is the correct, conservative-in-the-other-direction treatment, since relief staff by definition are not working (and not being paid) on a normal day where no one is absent. #1 (required operating positions, 3-4-4) is a functional/organisational concept, distinct from both headcount numbers, and should not be quoted as a staffing count anywhere.

## 10. Treatment Staff / Phlebotomy / VM Coverage — Direct Answers (2026-08-18 audit round addition)

Per Anthony's explicit Step 13-14 request, answering the specific questions directly (cross-referencing `docs/architecture/STAFF-PROFILES.md` §1 rather than duplicating its full content):

- **Staff needed at opening (Day 1 committed headcount):** 8 treatment + 2 phlebotomists + 1 Venue Manager + 1 PM Reception = 12 people minimum to run the committed 18-client design.
- **Employment headcount (people who must actually be hired):** Treatment 10-11, Phlebotomists 3-4, Venue Manager 1 (no relief), PM Reception 1 (no relief sized yet — see below) = **15-17 people employed**, not all rostered every day.
- **Daily roster count (people actually working on a normal day):** 12 (the committed headcount above) — the extra 3-6 employed-but-not-rostered relief staff (treatment/phlebotomy) are NOT on the floor on a normal day.
- **Relief/backup count:** Treatment +2-3, Phlebotomists +1-2, Venue Manager +0 (disclosed gap), PM Reception +0 (not yet sized — genuinely open, flagged not assumed at 0-is-fine; PM Reception's absence-coverage plan is an open item for the eventual Venue Manager to establish once trading, since the 2026-08-17 model only justified why ONE role is sufficient day-to-day, not who covers it when that one person is sick).
- **Sick-leave handling:** Casual staff (treatment, phlebotomy, PM reception) — no paid sick leave (National Employment Standards casual treatment), covered operationally by the relief pool where one exists (treatment, phlebotomy) or not covered at all (PM Reception, Venue Manager — disclosed gaps). Venue Manager, as a salaried Day-1 employee, DOES accrue NES personal/carer's leave once converted from casual — but as noted in STAFF-PROFILES.md, no second VM-capable staff member exists to cover that leave, a genuinely unresolved operational gap, not solved by this document.
- **Annual-leave handling:** Same asymmetry — casual staff have no NES annual leave entitlement (loaded rate compensates instead); the salaried Venue Manager does accrue it, with the same unresolved coverage gap noted above.
- **Required qualifications, cross-cover, and which positions cannot cross-cover:** Massage and Beauty are dual-qualification-paired (one pool, per `scenario-c-sync-timetables.md`'s own verified concurrency model) — this pairing IS the cross-cover mechanism for those two lines. Nails and Hair are each single-qualification lines with NO confirmed cross-qualification pairing to each other or to Massage/Beauty (flagged, not assumed, in `scenario-c-sync-timetables.md` §0.4). Phlebotomy cannot be cross-covered by any other role — it requires the pathology partner's own specific credentialing, the single tightest coverage constraint in the whole model (STAFF-PROFILES.md §1). The Venue Manager's own required service qualification (Cert III/IV) means the VM CAN, in principle, step into a treatment shift if genuinely needed — a real, if imperfect, mitigation for a treatment-staff gap, though this would leave the VM's own reception/management duties uncovered simultaneously, so it is not a free cross-cover.

## 11. Break-Even in Context — Cross-Reference

See §6 above for the full break-even calculation (both forms) with assumptions stated inline, per Anthony's explicit Step 7 instruction that this must be a real financial threshold explanation, not two bare numbers.

---

## 12. Changelog

**2026-08-17** — Created per Phase C's explicit instruction to stop proportional wage-scaling and rebuild from first principles (position -> headcount -> hours -> rate -> penalties -> on-costs), propagate the real A$117 PM average with its derivation shown (not a simple swap), and build the full revenue/P&L/cash-flow/break-even/sensitivity structure with every calculation inline. Old vs new figures disclosed and explained, not silently replaced.

**2026-08-18 (independent audit round, per Anthony's explicit request)** — Re-inspected the entire chain client -> appointments -> services -> pricing -> revenue -> staff hours -> wages -> super -> workers comp -> other opex -> operating result -> cash flow -> break-even, not just re-confirmed the tests passed. Two real findings: (1) §3a's Saturday treatment-staff breakdown had a genuine arithmetic error (used 4.3333 Saturdays/month for one sub-calculation instead of this repo's own canonical 4.33 convention) — fixed, A$10.78/month lower, immaterial but real. (2) The Venue Manager's wage classification (Clerks Award MA000002 L2, $36.81/hr) was audited against the role's actual duties and found to be a likely misclassification — corrected to the Hair & Beauty Industry Award MA000005's own Level 6 "salon manager" classification ($40.00/hr), a real, sourced, material finding (+A$727.19/month), flagged MODELLED/CORRECTED not VERIFIED pending professional confirmation. Workers compensation (1.7%) was re-investigated but the primary WorkCover WA source could not be fetched (403 Forbidden) — remains PLACEHOLDER, not silently left unexamined. Also added: §9 (five distinct staffing concepts made structurally explicit), §10 (direct coverage answers), enhanced §6 (break-even assumptions and both-forms calculation shown in full), and a §1 addendum on weekly-pay-frequency cash-flow-timing consistency. New headline: Table 1 steady-state Net Operating Result **A$48,024.86/month** (was A$48,851.68 pre-audit, A$53,837.02 before the original first-principles rebuild, A$56,581.70 at the very first superannuation-corrected figure). The business remains net-positive at 18 clients/day throughout every correction, but the margin has genuinely narrowed with each honest recompute — reported plainly, not smoothed over.
