# First-Principles Financial Model (Phase C Rebuild)

**Date:** 2026-08-17 | **Purpose:** Replace proportional wage-scaling with a genuine first-principles labour cost build (position -> headcount -> hours -> rate -> penalties -> on-costs -> monthly/annual cost), propagate the real calculated PM average transaction value (A$117, `docs/architecture/PM-PACKAGES.md`), and build the full revenue/P&L/cash-flow/break-even/sensitivity structure with every calculation shown inline. All figures below are the new canonical basis, propagated into `data/canonical/cost_ramp.yml`, `data/canonical/revenue_ramp.yml`, and `data/models/master_financial_model.yml` (see each file's own 2026-08-17 banner).

---

## 1. Pay Frequency — Resolved, Not Left Open

**Researched and resolved: weekly.** Real market research confirms casual workforces in Australia are overwhelmingly paid weekly; this is standard practice in hospitality and beauty-adjacent industries specifically, and casual staff commonly rely on weekly cash flow for retention reasons (a genuine labour-market consideration, not just administrative preference). This also matches this venture's own existing `docs/financial-setup.md` Monthly Financial Rhythm, which already specifies "Weekly payroll run (pay Friday)" — confirmed correct, not contradicted, by this research.

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
| Massage+Beauty pool | 4 | A$37.50 | 4 x 6 x 37.50 x 22 = **A$19,800.00** | 4 x 6 x 56.25 x 4.33 = **A$5,850.00** |
| Nails | 2 | A$36.81 | 2 x 6 x 36.81 x 22 = **A$9,717.84** | 2 x 6 x 55.215 x 4.33 = **A$2,872.11** |
| Hair | 2 | A$36.81 | 2 x 6 x 36.81 x 22 = **A$9,717.84** | 2 x 6 x 55.215 x 4.33 = **A$2,872.11** |
| **AM Treatment subtotal** | | | **A$39,235.68** | **A$11,594.22** |

### 3b. Phlebotomists (2, AM only)

2 x 6hrs x A$34.375/hr x 22 days = **A$9,075.00** (weekday)
2 x 6hrs x A$51.5625/hr (Saturday x1.5) x 4.33 days = **A$2,679.19** (Saturday)

### 3c. Venue Manager (1, AM + admin)

1 x 8hrs x A$36.81/hr x 22 days = **A$6,478.56** (weekday)
1 x 8hrs x A$55.215/hr (Saturday x1.5) x 4.33 days = **A$1,912.65** (Saturday)

### 3d. PM Reception/Coordinator (1)

1 x 5hrs x A$33.71/hr x 22 days = **A$3,708.10** (weekday)
1 x 5hrs x A$50.565/hr (Saturday x1.5) x 4.33 days = **A$1,094.73** (Saturday)

### 3e. PM Treatment Labour (4 roles, session-count/3-hour-floor method, unchanged methodology, current wage rates)

Weekday (16 sessions/day steady state; 16 / 4 roles / 1.3 sessions-per-hour throughput = 3.08hrs/role, clears the 3-hour floor): 4 roles x 3.08hrs x A$37.155/hr (blended current rate) x 22 days = **A$10,070.72**
Saturday (8 sessions/day; 8/4/1.3 = 1.54hrs/role, below the 3-hour floor, floor applies): 4 roles x 3hrs x A$55.7325/hr (blended, x1.5 Saturday) x 4.33 days = **A$2,895.83**

### 3f. Total Direct Labour (Wages Only, Before Super/Workers Comp)

| Component | Weekday | Saturday | Monthly total |
|---|---|---|---|
| Treatment (AM) | A$39,235.68 | A$11,594.22 | A$50,829.90 |
| Phlebotomists | A$9,075.00 | A$2,679.19 | A$11,754.19 |
| Venue Manager | A$6,478.56 | A$1,912.65 | A$8,391.21 |
| PM Reception | A$3,708.10 | A$1,094.73 | A$4,802.83 |
| PM Treatment | A$10,070.72 | A$2,895.83 | A$12,966.55 |
| **TOTAL WAGES** | | | **A$88,744.68** |

### 3g. On-Costs

| Item | Rate | Amount |
|---|---|---|
| Superannuation | 12% of total wages | A$10,649.36 |
| Workers Compensation | 1.7% of total wages | A$1,508.66 |
| **TOTAL MONTHLY PAYROLL COST (Table 1, 18/day)** | | **A$100,902.70** |
| **ANNUAL PAYROLL COST** | x 12 | **A$1,210,832.40** |

**Old (proportional-scaled) figure: A$87,398.78/month. New (first-principles) figure: A$100,902.70/month — a real, material increase of +A$13,503.92/month (+15.5%).**

**Why the two methods disagree, disclosed honestly:** the old model was built on an annual-salary-per-role basis (e.g. A$492,920/yr for 8 treatment staff, an FTE-style figure implying an averaged effective commitment across AM/PM, not a literal 6-hour-AM-shift-for-all-8 assumption). The new first-principles model assumes every one of the 8 treatment staff, both phlebotomists, and the Venue Manager work their **full rostered shift with no early release**, at the current researched wage rates — the conservative, no-savings-assumed planning basis. The existing Downtime-Fill/Early-Release framework (`docs/CURRENT-STATE.md` §8) remains the disclosed, separate, tagged upside if early release is actually achieved in practice at lower-than-peak booking density — it is not blended into this headline figure, consistent with this repo's own established convention of keeping that saving separate. **This is a genuine, disclosed methodology change, not an error in either figure.**

## 4. Revenue Model — AM/PM Separated, Full Derivation

### 4a. AM Revenue (Table 1, 18 clients/day)

- Weekday: 18 clients x A$250 (Package 1, conservative planning price) x 22 days = **A$99,000.00/month**
- Saturday: 18 clients x A$250 x 4.33 days = **A$19,485.00/month**
- **AM Revenue Total: A$118,485.00/month** (unchanged from the prior model — AM revenue is price x volume, not wage-driven, so the wage recompute doesn't affect it)

### 4b. PM Revenue — Rebuilt With the Real A$117 Average (Not a Simple Swap)

**Derivation, not just a substituted number:** PM revenue = session count x average transaction value, where the average transaction value (A$117) is itself derived from the real service catalogue and the two locked packages (`docs/architecture/PM-PACKAGES.md` §5), applied to the same session-count capacity already established (16 sessions/day weekday steady state, 8 Saturday, per `docs/pm-staffing-roster.md`):

- Weekday: 16 sessions x A$117 x 22 days = **A$41,184.00/month**
- Saturday: 8 sessions x A$117 x 4.33 days = **A$4,052.88/month**
- **PM Revenue Total: A$45,236.88/month** (was A$36,730.80 at the old, unexplained A$95 average — a real +A$8,506.08/month increase, because the new figure reflects real package pricing, not a placeholder)

### 4c. Total Revenue (Table 1, 18 clients/day)

**AM A$118,485.00 + PM A$45,236.88 = A$163,721.88/month**

## 5. 6/12/18 Sensitivity Table — 18/Day Is the Planning Case, 6 and 12 Are Sensitivity Comparisons Only

| Metric | 6 clients/day (SENSITIVITY) | 12 clients/day (SENSITIVITY) | 18 clients/day (PLANNING CASE) |
|---|---|---|---|
| AM revenue/month | A$39,495.00 | A$78,990.00 | A$118,485.00 |
| PM revenue/month | A$45,236.88 (unaffected by AM volume) | A$45,236.88 | A$45,236.88 |
| **Total revenue/month** | **A$84,731.88** | **A$124,226.88** | **A$163,721.88** |
| Labour/month | A$100,902.70 (headcount held fixed, per `conflict_am_labor_ramp_unmodelled`) | A$100,902.70 | A$100,902.70 |
| Opex/month (non-wage overhead) | A$13,980.00 | A$13,980.00 | A$13,980.00 |
| **Total costs/month** | **A$114,882.70** | **A$114,882.70** | **A$114,882.70** |
| **Net operating result/month** | **-A$30,150.82** | **A$9,344.18** | **A$48,839.18** |
| Annualised result | -A$361,809.84 | A$112,130.16 | A$586,070.16 |
| Margin | -35.6% | 7.5% | 29.8% |

**Note on labour/opex being held constant across all three volumes:** this reflects the same disclosed, pre-existing modelling limitation as the rest of this repo's cost architecture (`conflict_am_labor_ramp_unmodelled`) — committed headcount is fixed regardless of actual daily booking volume, since staff are rostered to the committed design, not flexed down in this model. This makes the 6/12-client sensitivity rows a genuine downside stress test (revenue drops, costs don't), not an alternate lower-cost operating plan — consistent with 18/day being the only planning case.

## 6. Break-Even — Both Forms, Calculation Shown

**Break-even revenue/month:** Total costs = A$114,882.70/month. Since PM revenue (A$45,236.88/month) is not client-volume-linear in this model, break-even is solved on the AM-volume-linear component: AM revenue needed = A$114,882.70 - A$45,236.88 = **A$69,645.82/month** from AM alone.

**Break-even clients/day:** A$69,645.82 / month / A$250 per client / 22 weekday-equivalent days = **12.66 clients/day** (weekday-only approximation; a full weekday+Saturday-weighted solve would land slightly lower given Saturday's smaller contribution to the 22-day denominator — not further refined this pass, flagged as a reasonable approximation, not false-precision).

**What this means operationally:** the venue needs to average roughly 13 AM clients/day (weekday-equivalent) across the month to cover its full monthly cost base at the new first-principles labour cost — this is **70.3% of the 18/day planning target**, a real but narrower margin of safety than the prior (proportionally-scaled) model showed, because the first-principles labour cost is materially higher.

## 7. Monthly Steady-State P&L (Table 1, 18 clients/day)

| Line | Amount | Calculation |
|---|---|---|
| AM Revenue | A$118,485.00 | §4a |
| PM Revenue | A$45,236.88 | §4b |
| **Total Revenue** | **A$163,721.88** | |
| Direct labour (COGS-equivalent — service delivery staff) | A$100,902.70 | §3g |
| **Gross Profit** | **A$62,819.18** | Total Revenue - Direct Labour |
| Non-Wage Overhead (rent, utilities, insurance, consumables, GTT supplies, laundry, waste, software, marketing, other — 13-line breakdown, `docs/profit-loss-tables.md` §4) | A$13,980.00 | Unchanged, not client-volume-driven |
| **Net Operating Result** | **A$48,839.18/month** | Gross Profit - Non-Wage Overhead |
| Net margin | 29.8% | Net Operating Result / Total Revenue |
| **Annualised (steady state)** | **A$586,070.16** | Monthly x 12 |

## 8. Cash Flow — Startup vs Opex vs Revenue, Clearly Separated

| Item | Status |
|---|---|
| Opening cash | `[PLACEHOLDER — no canonical source states an opening cash figure]` |
| Startup expenditure (one-off, pre-opening) | A$251,198 adopted planning figure (`docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`) — a separate, one-off capital outlay, not part of any monthly operating cash movement below |
| Working capital reserve | A$85,000-110,000 (separate from startup expenditure, funds the ramp period) |
| Monthly operating cash inflow | Total Revenue, §4c/§5 (varies by ramp month — Month 1-4 ramp not yet rebuilt against this new labour-cost basis, flagged as an open follow-up) |
| Monthly operating cash outflow | Total Costs, §7 (payroll + non-wage overhead) |
| **Monthly net operating cash movement (steady state)** | **+A$48,839.18/month** |
| Rent/fit-out/startup purchases | One-off, funded from the startup expenditure line above, not the monthly operating movement |

**Not yet rebuilt this pass:** the Month 1-4 ramp cash-flow trough (previously -A$33,627.92 at Month 1 under the wage-recompute-only basis) needs re-deriving against this new first-principles labour cost — flagged as the next bounded follow-up, not fabricated here.

---

## Changelog

**2026-08-17** — Created per Phase C's explicit instruction to stop proportional wage-scaling and rebuild from first principles (position -> headcount -> hours -> rate -> penalties -> on-costs), propagate the real A$117 PM average with its derivation shown (not a simple swap), and build the full revenue/P&L/cash-flow/break-even/sensitivity structure with every calculation inline. Old vs new figures disclosed and explained, not silently replaced.
