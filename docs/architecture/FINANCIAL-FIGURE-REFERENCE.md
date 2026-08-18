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

**IMPORTANT — what this payroll figure does and does NOT include (Step 8 audit finding this round):** the figure above prices ONLY the committed simultaneous headcount (8 treatment + 2 phlebotomists + 1 VM + 1 PM Reception) working their full rostered shift, every trading day, with no absence. It does **NOT** include any cost for the recommended relief/backup EMPLOYMENT POOL (12 treatment / 4 phlebotomists on the books, `docs/architecture/STAFFING-COVERAGE-VALIDATION.md`) actually being called in to cover an absence. See §5 below for the quantified gap this represents.

## 4. Non-Wage Overhead — 13-Line Breakdown

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
| Insurance (public liability + PI) | A$400.00 (the figure actually embedded in the A$13,980.00 total below) | `docs/profit-loss-tables.md` §4 | PLACEHOLDER — never an actual quote |
| Accounting/bookkeeping | A$500.00 | Same source | MODELLED |
| Consumables (wax, nail products, skincare) | A$800.00 | Same source | MODELLED |
| Miscellaneous/contingency | A$500.00 | Same source | MODELLED |
| **TOTAL NON-WAGE OVERHEAD** | **A$13,980.00/month** | Sum of the above | CALCULATED |

**Discrepancy, disclosed not resolved:** `data/canonical/opex.yml#opex_insurance_modelled` was separately revised 2026-08-16 to A$1,279.00/month, but this revision was never propagated into the A$13,980.00 total that actually flows through every P&L/payroll figure in the canonical model — that total still uses A$400.00. If propagated, non-wage overhead would rise to A$14,859.00/month (+A$879.00). See `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §4 for the full disclosure and financial impact — not corrected this round, requires Anthony's decision on which insurance figure is current.

## 5. The Un-Modelled Relief/Absence Cost Gap — Quantified, Not Silently Fixed

**Finding (Step 8 audit, this round):** the payroll figure in §3 prices only the committed simultaneous headcount. The recommended relief/backup EMPLOYMENT POOL (`docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §1-2) is genuinely a DIFFERENT concept from the daily roster — relief staff are only paid when an absence actually occurs and they are called in to cover it. **This means the steady-state payroll figure above (A$101,717.02/month) implicitly assumes ZERO absences, ever** — which is not realistic over any extended trading period.

**Ballpark quantification, using the same 8% per-person absence-rate planning assumption from `STAFFING-COVERAGE-VALIDATION.md` §1a:**

| Line | Expected relief shifts/month | Assumed relief engagement | Ballpark cost/month |
|---|---|---|---|
| Treatment (8 committed × 8% × 26.33 trading days) | ~16.85 shifts | 3-hour casual minimum engagement × blended A$37.155/hr rate | ~A$1,878/month |
| Phlebotomists (2 committed × 8% × 26.33 trading days) | ~4.21 shifts | 3-hour minimum × A$34.375/hr | ~A$434/month |
| **TOTAL, before on-costs** | | | **~A$2,313/month** |
| **TOTAL, with super + workers comp** | | | **~A$2,630/month** |

**Status: BALLPARK-ESTIMATE. NOT propagated into the canonical payroll model this round.** This figure depends on an undecided operational policy question (exactly how long a relief engagement actually runs when called in — the 3-hour casual-minimum-engagement floor is used here as the most defensible lower bound, but a real relief call-in might run longer, e.g. the rest of the affected person's shift) and the underlying 8% absence-rate assumption is itself a disclosed planning estimate, not verified data for this specific venture. Per Anthony's explicit instruction this round ("if a change is genuinely required: show current model → proposed model → financial impact → reason, THEN update the canonical model, in that order") — this section shows the current model (no relief cost) and the financial impact of a proposed change (~A$2,313-2,630/month), and stops there, pending Anthony's decision on the relief-engagement-length policy before propagating any change to `data/canonical/cost_ramp.yml`.

## 6. Break-Even — Full Calculation

See `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §3 for the full break-even table and plain-English explanation. Summary derivation: Total Costs (A$115,697.02/month) − PM Revenue (A$36,225.69/month, held fixed, capacity-constrained not AM-volume-linear) = AM revenue needed (A$79,471.33/month) → solved against the AM revenue formula (§1 above) for the client-volume figure that produces exactly that AM revenue, weighted across weekday and Saturday operating days = **12.073 clients/day**, equivalently **A$115,696.21/month** total revenue.

## 7. Cash Flow and Funding — Full Chain

See `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §5 for the full 24-month table and chart. Key derivation: Monthly Net Operating Cash Movement = Total Revenue − Total Operating Costs (an accrual-basis proxy, `assumption_cashflow_accrual_proxy` in `master_financial_model.yml` — NOT a true cash-basis forecast with real debtor/creditor timing, and does NOT reflect real weekly-granularity payroll timing, see `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §1). Cumulative Cash Position = running sum of Monthly Net Operating Cash Movement from Month 1. **This is operating cash flow only — it does NOT include startup expenditure (a separate, one-off capital outlay, `docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`) or the working capital reserve (a separate buffer figure) — these three concepts are not interchangeable, see the explicit distinction in §5 of the companion document.**

---

## Changelog

**2026-08-18** — Created per Anthony's explicit instruction (Priority 4/Step 6) to build a single calculation dictionary every other financial figure traces back to. Re-audited the full PM revenue chain (Step 10) and confirmed it reconciles, with one disclosed remaining uncertainty (individual-service average duration). Quantified, for the first time, the previously-unexamined relief/absence cost gap (Step 8) as a labelled ballpark estimate, not silently fixed or propagated.
