# Financial Figure Reference — Calculation Dictionary

**Purpose:** every major financial figure in this venture's model, with its full derivation chain shown, source cited, and certainty labelled. This is the document every other financial figure (dossier, Dash, any summary) should trace back to. Current figures only — historical corrections and superseded rounds live in `docs/CURRENT-STATE.md` and `docs/architecture/*-RECONCILIATION*.md`, not here.

**Labels used throughout:** VERIFIED (confirmed against a primary/authoritative source) · RESEARCHED-BEST-EVIDENCE (a defensible, sourced match, not yet professionally confirmed) · MODELLED (a reasoned planning figure, no direct primary-source citation) · BALLPARK-ESTIMATE (a rough, disclosed order-of-magnitude figure, not precise) · PLACEHOLDER (no reliable source found) · WAITING ON THIRD PARTY (depends on an external party's decision).

**Planning case: 18 clients/day (Table 1) only.** 12/day (Table 2) and 6/day appear in this document ONLY inside the explicitly labelled sensitivity table (`docs/architecture/FINANCIAL-POSITION-CURRENT.md` §2) — nowhere else, never as a competing plan.

---

## 1. AM Revenue

**Derivation chain:** client volume/day → price per client → operating days/month → weekday revenue → Saturday revenue → total AM revenue/month.

| Step | Input | Value | Source | Label |
|---|---|---|---|---|
| 1 | Client volume/day (18-client planning case) | 18 | `data/canonical/scenarios.yml#scenario_table_1.client_volume` | VERIFIED — solver-confirmed, `scenario-c-sync-timetables.md` §0.6a |
| 2 | Price per client (Package 1, conservative planning price) | A$250.00 | `data/canonical/pricing.yml#am_price_used_for_revenue` | MODELLED — a deliberate conservative convention (Package 2 at A$300 would be higher; real booking mix unknown) |
| 3 | Weekday operating days/month | 22 | `data/canonical/client_assumptions.yml#operating_days_per_month_weekday` | MODELLED — standard planning convention |
| 4 | Saturday operating days/month | 4.33 | `data/canonical/client_assumptions.yml#operating_saturdays_per_month` | MODELLED — standard planning convention |
| 5 | Weekday AM revenue | 18 × A$250 × 22 = **A$99,000.00/month** | Calculated from steps 1-3 | CALCULATED |
| 6 | Saturday AM revenue | 18 × A$250 × 4.33 = **A$19,485.00/month** | Calculated from steps 1, 2, 4 | CALCULATED |
| **TOTAL AM REVENUE** | | **A$118,485.00/month** | Sum of steps 5-6 | **CALCULATED** |

## 2. PM Revenue — Full Chain, Re-Verified (Step 10 Audit This Round)

**Derivation chain:** package prices → service duration per package → staffing requirement per package → total available PM staff-minutes → transaction capacity → expected transaction mix (individual/package) → average transaction value → daily revenue → monthly revenue.

| Step | Input | Value | Source | Label |
|---|---|---|---|---|
| 1a | PM Refresh package price | A$185.00 (Massage 45min + Mini facial 30min, A$212 a-la-carte sum, 13% bundle discount) | `docs/architecture/PM-PACKAGES.md` §3 | RESEARCHED-BEST-EVIDENCE — real Perth comparable bundle pricing |
| 1b | PM Restore package price | A$135.00 (Gel manicure 45min + Blow-dry 30min, A$150 a-la-carte sum, 10% bundle discount) | `docs/architecture/PM-PACKAGES.md` §4 | RESEARCHED-BEST-EVIDENCE |
| 1c | Individual a-la-carte average price | A$84.11 (average of 9 real catalogue service midpoints) | `docs/architecture/PM-PACKAGES.md` §5 | MODELLED — real catalogue prices, but the specific 9-service selection and midpoint convention is a planning choice |
| 2a | PM Refresh staffing requirement | 1 dual-qualified Massage+Beauty therapist, 75 continuous minutes | Researched 2026-08-18 — matches the venue's existing AM Massage+Beauty common-pool design; real Perth comparables (Keturah, Hidden Valley, endota) bundle massage+facial with no evidence of mid-service handover | RESEARCHED-BEST-EVIDENCE — `docs/architecture/PM-CAPACITY-RECONCILIATION.md` §2 |
| 2b | PM Restore staffing requirement | 2 specialists (1 Nail Technician + 1 Hairdresser), 75 total staff-minutes | Researched 2026-08-18 — no confirmed dual Nails+Hair qualification anywhere in this repo (`scenario-c-sync-timetables.md` §0.4) | RESEARCHED-BEST-EVIDENCE — `docs/architecture/PM-CAPACITY-RECONCILIATION.md` §2 |
| 3 | Individual-service average duration | 46.15 min (60÷1.3 sessions/hr throughput) | `docs/pm-staffing-roster.md`'s existing throughput assumption | MODELLED — inherited, not independently re-verified against the actual weighted-average duration of the 9 specific catalogue services this round (a disclosed, bounded limitation) |
| 4 | Total available PM staff-minutes/day (weekday) | 4 treatment lines × 3.08hrs/role × 60 = **739.2 min/day** | `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §3e (the same labour-hours figure that drives PM payroll — unchanged by this revenue correction) | CALCULATED |
| 5 | Expected transaction mix | 60% individual / 25% PM Refresh / 15% PM Restore | `docs/architecture/PM-PACKAGES.md` §5 | MODELLED — a disclosed planning assumption, no real booking data exists (pre-launch venture) |
| 6 | Weighted minutes/transaction | 0.6×46.15 + 0.25×75 + 0.15×75 = **57.69 min/transaction** | Calculated from steps 1-5 | CALCULATED |
| 7 | Weekday transaction capacity | 739.2 ÷ 57.69 = **12.8128 transactions/day** | Calculated | CALCULATED — `data/canonical/revenue_assumptions.yml#rev_pm_weekday_transactions` |
| 8 | Saturday transaction capacity | 12.8128 × 0.5 (preserves the original weekday:Saturday demand ratio, NOT the floor-inflated paid capacity) = **6.4064 transactions/day** | Calculated | CALCULATED — `data/canonical/revenue_assumptions.yml#rev_pm_saturday_transactions` |
| 9 | Blended average transaction value | 0.6×A$84.11 + 0.25×A$185.00 + 0.15×A$135.00 = **A$116.97** (rounded to A$117.00 in pricing.yml) | `data/canonical/pricing.yml#pm_alacarte_average` | MODELLED |
| 10 | Weekday PM revenue | 12.8128 × A$117.00 × 22 days = **A$32,980.15/month** | Calculated | CALCULATED |
| 11 | Saturday PM revenue | 6.4064 × A$117.00 × 4.33 days = **A$3,245.55/month** | Calculated | CALCULATED |
| **TOTAL PM REVENUE** | | **A$36,225.69/month** | Sum of steps 10-11 | **CALCULATED, VERIFIED against a live run of `tools/revenue_ramp_model.py` — matches exactly, no drift** |

**Re-audit confirmation, this round (Step 10):** re-traced the full chain above from package prices through to monthly revenue and confirmed every intermediate figure reconciles — no further discrepancy found. The chain does NOT reconcile perfectly with zero disclosed uncertainty: step 3 (individual-service average duration) remains an inherited assumption, not independently re-verified against the 9 specific catalogue services' own real durations. If those real durations differ materially from 46.15 minutes, the transaction-capacity figures in steps 7-8 would shift somewhat — the direction of the original correction (PM revenue was overstated before Priority 1) would not change, only the precise magnitude might.

## 3. Labour Cost — Per Position, Full Chain

**Derivation chain (every position):** position → headcount (committed, simultaneous) → hours/shift → operating days/month → hourly wage rate → Saturday penalty (×1.5) → monthly wage subtotal → superannuation (12%, universal) → workers compensation (1.7%, PLACEHOLDER) → total monthly payroll cost.

| Position | Headcount | Hours/shift | Wage rate (ordinary) | Saturday rate (×1.5) | Weekday monthly | Saturday monthly | Monthly subtotal | Award/classification | **Label** |
|---|---|---|---|---|---|---|---|---|---|
| Treatment — Massage+Beauty | 4 | 6hr AM | A$37.50/hr | A$56.25/hr | A$19,800.00 | A$5,845.50 | A$25,645.50 | Hair & Beauty Industry Award MA000005 Level 4 | RESEARCHED-BEST-EVIDENCE |
| Treatment — Nails | 2 | 6hr AM | A$36.81/hr | A$55.215/hr | A$9,717.84 | A$2,868.97 | A$12,586.81 | MA000005 Level 3 | RESEARCHED-BEST-EVIDENCE |
| Treatment — Hair | 2 | 6hr AM | A$36.81/hr | A$55.215/hr | A$9,717.84 | A$2,868.97 | A$12,586.81 | MA000005 Level 3 | RESEARCHED-BEST-EVIDENCE |
| Phlebotomists | 2 | 6hr AM | A$34.375/hr | A$51.5625/hr | A$9,075.00 | A$2,679.19 | A$11,754.19 | Health Professionals and Support Services Award MA000027, Support Services Level 1-2 | RESEARCHED-BEST-EVIDENCE, closest-match caveat disclosed; **WAITING ON THIRD PARTY** for WDP employment-arrangement question |
| Venue Manager | 1 | 8hr AM+admin | A$40.00/hr | A$60.00/hr | A$7,040.00 | A$2,078.40 | A$9,118.40 | MA000005 Level 6 ("salon manager") | **RESEARCHED-BEST-EVIDENCE, NOT VERIFIED** — needs accountant/Fair Work confirmation |
| PM Reception | 1 | 5hr PM | A$33.71/hr | A$50.565/hr | A$3,708.10 | A$1,094.73 | A$4,802.83 | Clerks Award MA000002 Level 1 | RESEARCHED-BEST-EVIDENCE |
| PM Treatment (4 roles, session-throughput method) | shared with AM pool | ~3.08hr weekday / 3.0hr floor Saturday | A$37.155/hr blended | A$55.7325/hr blended | A$10,070.72 | A$2,895.83 | A$12,966.55 | Blended across the 4 PM treatment lines above | RESEARCHED-BEST-EVIDENCE |
| **TOTAL WAGES (before on-costs)** | | | | | | | **A$89,460.88** | | CALCULATED, live-verified |
| Superannuation | 12% of total wages | | | | | | **A$10,735.31** | Superannuation Guarantee | MODELLED — 12% rate itself well-known/current; this repo's universal-application methodology is a disclosed simplification |
| Workers compensation | 1.7% of total wages | | | | | | **A$1,520.83** | WorkCover WA, classification not confirmed | **PLACEHOLDER, UNVERIFIED** — two genuine research attempts made (WorkCover WA 403 Forbidden, Safe Work Australia connection error), neither succeeded |
| **TOTAL MONTHLY PAYROLL COST** | | | | | | | **A$101,717.02** | | **CALCULATED** |
| **ANNUAL PAYROLL COST** | | | | | | | **A$1,220,604.24** | Monthly × 12 | CALCULATED |

**IMPORTANT — what this payroll figure does and does NOT include:** the figure above prices ONLY the committed simultaneous headcount (8 treatment + 2 phlebotomists + 1 VM + 1 PM Reception) working their full rostered shift, every trading day, with no absence. It does **NOT** include the relief/absence cost — that is now a SEPARATE, quantified line (§5 below), not blended into payroll, so the committed-roster figure is never confused with the full realistic cost base.

## 4. Non-Wage Overhead — 13-Line Breakdown, Insurance Corrected

**Insurance resolved 2026-08-18 (Financial Finalisation round), investigated not chosen between two existing figures.** Both prior figures were traced and found flawed: A$400/month was an unexplained round guess; A$1,279/month (a "revised placeholder," 2026-08-16) was found this round to double-count workers compensation (already charged separately, §3 above) and include an optional business-interruption line as if committed. Corrected: Public Liability (A$2,500-4,500/yr) + Professional Indemnity (A$2,000-4,000/yr) + Property/Contents (A$1,500-2,500/yr) only = A$6,000-11,000/year = **A$500.00-916.67/month, midpoint A$708.34/month** — externally sanity-checked against real 2026 Australian small-business PL/PI premium research (this venture's higher-risk client profile, pregnant clients + health-adjacent services, justifies sitting above generic small-business averages). Full investigation: `docs/architecture/FINANCIAL-ASSUMPTION-REGISTER.md`.

| Component | Monthly | Source | Label |
|---|---|---|---|
| Rent (commercial lease, ~200sqm) | A$8,000.00 | `docs/profit-loss-tables.md` §4, `docs/cash-flow.md` §Cost Assumptions | MODELLED — market-rate estimate, no signed lease yet |
| Utilities (power/water, medical fridge + HVAC) | A$650.00 | Same source | MODELLED |
| Internet + phone | A$150.00 | Same source | MODELLED |
| Fresha booking system (Team plan) | A$100.00 | Same source | MODELLED |
| Resend email platform | A$30.00 | Same source | MODELLED |
| Marketing (Instagram/Meta ads, steady state) | A$1,500.00 | Same source | MODELLED |
| GTT supplies (glucose, tubes) | A$400.00 | Same source | MODELLED — NOTE: `data/canonical/opex.yml#opex_gtt_supplies` shows a different figure (A$792.00) for this same line — a pre-existing, disclosed cross-document discrepancy, not resolved this round |
| Laundry/linen service | A$350.00 | Same source | MODELLED |
| Cleaning service | A$600.00 | Same source | MODELLED |
| **Insurance (Public Liability + Professional Indemnity + Property/Contents)** | **A$708.34** (CORRECTED 2026-08-18 — was A$400.00) | `data/canonical/opex.yml#opex_insurance_modelled` | **MODELLED/BALLPARK-ESTIMATE** — real broker quotes already in motion, `docs/insurance-broker-quote-request-draft.md` |
| Accounting/bookkeeping | A$500.00 | Same source | MODELLED |
| Consumables (wax, nail products, skincare) | A$800.00 | Same source | MODELLED |
| Miscellaneous/contingency | A$500.00 | Same source | MODELLED |
| **TOTAL NON-WAGE OVERHEAD** | **A$14,288.34/month** (was A$13,980.00) | Sum of the above | CALCULATED |

## 5. Relief/Absence Coverage Allowance — Real Cost Model, Not a Ballpark

**Resolved 2026-08-18 (Financial Finalisation round), replacing the prior round's rough estimate with a real, methodologically-defensible cost model.** The payroll figure in §3 prices only the committed simultaneous headcount — the recommended relief/backup EMPLOYMENT POOL (12 treatment / 4 phlebotomists on the books, `docs/architecture/STAFFING-COVERAGE-VALIDATION.md`) is a genuinely different concept from the daily roster, and relief staff are only paid when an absence actually occurs and they are called in to cover it. Previously, this implicitly assumed ZERO absences, ever — unrealistic over any extended trading period.

**Method, full-shift replacement (not the bare 3-hour casual-minimum floor):** a relief person covering a colleague's absence realistically works that colleague's FULL rostered shift (6hr AM for treatment/phlebotomy, 5hr PM for reception), not the bare legal minimum engagement. Using the same 8% per-person per-shift unavailability planning assumption (`STAFFING-COVERAGE-VALIDATION.md` §1a, a commonly-cited casual-hospitality/beauty planning range, NOT independently verified against real data for this pre-opening venture):

| Line | Expected relief shifts/month (weekday + Saturday, 8% × 26.33 trading days) | Full-shift cost/month |
|---|---|---|
| Treatment (8 committed) | 16.85 shifts × 6hr × A$37.155/hr weekday blended (A$55.7325/hr Saturday) | A$4,065.53 |
| Phlebotomists (2 committed) | 4.21 shifts × 6hr × A$34.375/hr weekday (A$51.5625/hr Saturday) | A$940.34 |
| PM Reception (1 committed) | 2.11 shifts × 5hr × A$33.71/hr weekday (A$50.565/hr Saturday) | A$384.23 |
| **Subtotal, before on-costs** | | **A$5,390.09** |
| Superannuation (12%) | | A$646.81 |
| Workers compensation (1.7%) | | A$91.63 |
| **TOTAL RELIEF/ABSENCE COVERAGE ALLOWANCE** | | **A$6,128.53/month** |

**Decision on how this appears in the model, per Anthony's explicit Step 3 instruction:** modelled as its OWN recurring opex line (Option B — a distinct, separately-labelled allowance), not blended into Direct Labour (Option A) and not treated as a one-off contingency (Option C). Reasoning: real absences are individually stochastic (unpredictable which day, which person) but statistically real and recurring IN AGGREGATE over any extended trading period — the same defensible planning convention used for budgeting a maintenance/contingency reserve. Keeping it as its own line (not blended into Direct Labour) ensures the committed-roster payroll figure is never confused with the full realistic cost base, and Anthony can see exactly what this allowance represents and adjust the underlying 8% assumption independently if better data emerges. **Status: MODELLED/BALLPARK-ESTIMATE** — propagated into `data/canonical/cost_ramp.yml` as `relief_absence_allowance`, a new field distinct from `payroll_costs`.

**PROPAGATED this round** (unlike the prior round's un-actioned finding) — `data/canonical/cost_ramp.yml`'s `total_operating_costs` now includes this line for every scenario/month. Impact: Total Operating Costs A$115,697.02 → A$122,133.89/month (Table 1); A$110,292.03 → A$116,728.90/month (Table 2).

## 6. Break-Even — Full Calculation, Recomputed

See `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §3 for the full break-even table and plain-English explanation. Summary derivation: Total Costs (A$122,133.89/month, now including the corrected insurance figure and the relief/absence allowance) − PM Revenue (A$36,225.69/month, held fixed, capacity-constrained not AM-volume-linear) = AM revenue needed (A$85,908.20/month) → solved against the AM revenue formula (§1 above) for the client-volume figure that produces exactly that AM revenue, weighted across weekday and Saturday operating days = **13.051 clients/day**, equivalently **A$122,133.90/month** total revenue. **Table 2's own break-even (12.230 clients/day) now exceeds its own committed volume (12/day) — Table 2 no longer clears break-even at steady state, a real, disclosed finding.**

## 7. Cash Flow and Funding — Full Chain, Recomputed

See `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §5 for the full 24-month table and chart. Key derivation: Monthly Net Operating Cash Movement = Total Revenue − Total Operating Costs (now including the corrected insurance and relief-allowance lines) — an accrual-basis proxy, `assumption_cashflow_accrual_proxy` in `master_financial_model.yml` — NOT a true cash-basis forecast with real debtor/creditor timing, and does NOT reflect real weekly-granularity payroll timing, see `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §1. Cumulative Cash Position = running sum of Monthly Net Operating Cash Movement from Month 1. **This is operating cash flow only — it does NOT include startup expenditure (a separate, one-off capital outlay) or the working capital reserve (a separate buffer figure) — these three concepts are not interchangeable.** Table 1's trough deepened to -A$76,532.52 (Month 2, unchanged month); Table 2's cumulative position now falls every month with no recovery (trough at Month 24, -A$172,138.34), since its steady state is now loss-making.

---

## Changelog

**2026-08-18 (Financial Finalisation round)** — Resolved both open items from the prior round by investigation, not by asking Anthony to pick. Insurance corrected to A$708.34/month (was A$400 unexplained guess vs. a methodologically-flawed A$1,279 figure that double-counted workers comp and included an optional line) — propagated into §4's non-wage overhead total. Relief/absence coverage upgraded from a rough ballpark to a real, defensible cost model (full-shift replacement, not the bare 3-hour minimum) and PROPAGATED into the canonical model this round (§5), not left un-actioned. Break-even and cash-flow sections (§6-7) recomputed against the new total operating costs.

**2026-08-18 (earlier this date)** — Created per Anthony's explicit instruction (Priority 4/Step 6) to build a single calculation dictionary every other financial figure traces back to. Re-audited the full PM revenue chain (Step 10) and confirmed it reconciles, with one disclosed remaining uncertainty (individual-service average duration). Quantified, for the first time, the previously-unexamined relief/absence cost gap as a labelled ballpark estimate, not silently fixed or propagated.
