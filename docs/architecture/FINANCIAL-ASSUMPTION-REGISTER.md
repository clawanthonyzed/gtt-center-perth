# Financial Assumption Register

**Purpose:** every material financial assumption in this venture's model, in one place, with a consistent certainty label. This is the register `docs/architecture/FINANCIAL-FIGURE-REFERENCE.md` and `docs/architecture/FINANCIAL-POSITION-CURRENT.md` both draw from — update this register first when an assumption changes, then propagate.

**Labels, used consistently across this entire project, never upgraded without genuine evidence:** VERIFIED (confirmed against a primary/authoritative source) · RESEARCHED-BEST-EVIDENCED (a defensible, sourced match, not yet professionally confirmed) · MODELLED (a reasoned planning figure, no direct primary-source citation) · BALLPARK-ESTIMATE (a rough, disclosed order-of-magnitude figure) · PLACEHOLDER (no reliable source found) · WAITING ON THIRD PARTY (depends on an external party's decision).

| Assumption | Current Value | Status | Source | Last Reviewed | Notes |
|---|---|---|---|---|---|
| AM client volume (planning case) | 18/day | VERIFIED | `scenario-c-sync-timetables.md` §0.6a, solver-confirmed zero collisions | 2026-08-18 | Sole planning case |
| AM price (revenue calc) | A$250.00 (Package 1) | MODELLED | `pricing.yml#am_price_used_for_revenue` | 2026-08-09 | Conservative convention — Package 2 (A$300) would be higher |
| Operating weekdays/month | 22 | MODELLED | `client_assumptions.yml#operating_days_per_month_weekday` | 2026-08-09 | Standard planning convention |
| Operating Saturdays/month | 4.33 | MODELLED | `client_assumptions.yml#operating_saturdays_per_month` | 2026-08-09 | 52/12 rounded |
| PM Refresh package price | A$185.00 | RESEARCHED-BEST-EVIDENCED | `PM-PACKAGES.md` §3 | 2026-08-17 | Real Perth comparable bundle pricing |
| PM Restore package price | A$135.00 | RESEARCHED-BEST-EVIDENCED | `PM-PACKAGES.md` §4 | 2026-08-17 | Real Perth comparable bundle pricing |
| Individual a-la-carte average price | A$84.11 | MODELLED | `PM-PACKAGES.md` §5 | 2026-08-17 | Average of 9 real catalogue midpoints |
| PM package/individual transaction mix | 60%/25%/15% | MODELLED | `PM-PACKAGES.md` §5 | 2026-08-17 | Disclosed planning assumption, no real booking data (pre-launch) |
| PM Refresh staffing model | 1 dual-qualified therapist | RESEARCHED-BEST-EVIDENCED | `PM-CAPACITY-RECONCILIATION.md` §2 | 2026-08-18 | Matches existing AM Massage+Beauty common-pool design |
| PM Restore staffing model | 2 specialists | RESEARCHED-BEST-EVIDENCED | `PM-CAPACITY-RECONCILIATION.md` §2 | 2026-08-18 | No confirmed Nails+Hair dual qualification anywhere in this repo |
| Individual PM service average duration | 46.15 min | MODELLED | `pm-staffing-roster.md`, inherited throughput assumption | 2026-08-18 | NOT independently re-verified against the actual 9 catalogue services' real durations — a disclosed, bounded remaining uncertainty |
| PM weekday transaction capacity | 12.8128/day | CALCULATED | `revenue_assumptions.yml#rev_pm_weekday_transactions` | 2026-08-18 | Derived from staff-minutes capacity ÷ weighted mix duration |
| PM Saturday transaction capacity | 6.4064/day | CALCULATED | `revenue_assumptions.yml#rev_pm_saturday_transactions` | 2026-08-18 | Weekday capacity × 50% (preserves original demand ratio) |
| Treatment — Massage+Beauty wage | A$37.50/hr casual | RESEARCHED-BEST-EVIDENCED | MA000005 Level 4, `wages.yml` | 2026-08-16 | Not reopened this round |
| Treatment — Nails/Hair wage | A$36.81/hr casual | RESEARCHED-BEST-EVIDENCED | MA000005 Level 3, `wages.yml` | 2026-08-16 | Not reopened this round |
| Phlebotomist wage | A$34.375/hr casual | RESEARCHED-BEST-EVIDENCED | MA000027 Support Services L1-2 midpoint, `wages.yml` | 2026-08-16 | Closest-match caveat disclosed — role does not map to an exact single classification |
| Phlebotomist employment arrangement | Direct employment assumed | **WAITING ON THIRD PARTY** | WDP/Carole Rivers | 2026-08-18 | Not actioned further — could materially change this cost line if WDP supplies phlebotomists instead |
| **Venue Manager wage** | **A$40.00/hr casual (MA000005 Level 6, "salon manager")** | **RESEARCHED-BEST-EVIDENCED, NOT VERIFIED** | `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §3c/§15 | 2026-08-18 | Corrected from a likely-misclassified Clerks Award L2 figure. Needs accountant/Fair Work confirmation before use in a real contract — status held, not upgraded |
| PM Reception wage | A$33.71/hr casual | RESEARCHED-BEST-EVIDENCED | MA000002 Level 1, `wages.yml` | 2026-08-16 | Not reopened this round |
| Superannuation rate | 12% of OTE, universal application | MODELLED | `wages.yml#wage_superannuation_rate` | 2026-08-09 | 12% SG rate itself well-known/current; universal-application methodology is a disclosed simplification |
| **Workers compensation rate** | **1.7% of direct labour** | **PLACEHOLDER, UNVERIFIED** | `wages.yml#wage_workers_comp_rate` | 2026-08-18 | Two genuine research attempts made this session (WorkCover WA 403 Forbidden, Safe Work Australia connection error) — neither succeeded. One secondary data point (Safe Work Australia's ~1.73% national all-industry average, beauty/personal-care typically lower-risk) suggests 1.7% may be a slight overestimate, not confirmed. Status held, not upgraded |
| Pay frequency | Weekly (pay Friday) | RESEARCHED-BEST-EVIDENCED | `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §1, cross-checked against `financial-setup.md` | 2026-08-17 | Cash-flow model uses a smooth monthly-average, not real weekly-granularity timing — a disclosed simplification |
| Rent/occupancy | A$8,000.00/month | MODELLED | `profit-loss-tables.md` §4 | Pre-2026-08-17 | Market-rate estimate, no signed lease yet |
| **Insurance (PL + PI + Property/Contents)** | **A$708.34/month** | **MODELLED/BALLPARK-ESTIMATE** | `opex.yml#opex_insurance_modelled`, corrected 2026-08-18 | 2026-08-18 | RESOLVED this round by investigation — neither A$400 (unexplained guess) nor A$1,279 (double-counted workers comp + an optional line) was defensible. Externally sanity-checked against real 2026 AU small-business PL/PI premium research. Real broker quotes in motion, `docs/insurance-broker-quote-request-draft.md`, will supersede once received |
| GTT supplies | A$400.00/month (P&L figure) vs A$792.00/month (`opex.yml`) | MODELLED | `profit-loss-tables.md` §4 vs `opex.yml#opex_gtt_supplies` | Pre-2026-08-17 | Pre-existing, disclosed cross-document discrepancy — NOT resolved this round (out of scope, lower materiality than insurance) |
| Consumables | A$800.00/month | MODELLED | `profit-loss-tables.md` §4 | Pre-2026-08-17 | Not reopened this round |
| Laundry | A$350.00/month | MODELLED | `profit-loss-tables.md` §4 | Pre-2026-08-17 | Not reopened this round |
| Marketing (steady state) | A$1,500.00/month | MODELLED | `opex.yml#opex_marketing_ads_steady_state` | Pre-2026-08-17 | Not reopened this round |
| Software (Fresha + email + internet/phone) | A$280.00/month | MODELLED | `profit-loss-tables.md` §4 | Pre-2026-08-17 | Not reopened this round |
| **Per-person casual absence rate (relief-cost planning input)** | **8% per shift** | **BALLPARK-ESTIMATE** | `STAFFING-COVERAGE-VALIDATION.md` §1a | 2026-08-18 | A commonly-cited casual-hospitality/beauty planning range, NOT independently verified against real data for this pre-opening venture. The single most consequential unverified assumption in the relief-cost model — if real absence rates differ materially, the A$6,128.53/month allowance below would need re-deriving |
| **Relief/absence coverage allowance** | **A$6,128.53/month** | **MODELLED/BALLPARK-ESTIMATE** | `FINANCIAL-FIGURE-REFERENCE.md` §5 | 2026-08-18 | NEW this round — full-shift replacement method (not the bare 3-hour casual-minimum floor), propagated into the canonical model as its own line, kept separate from Direct Labour |
| Treatment staff recommended employment pool | 12 (or 11 lower-reliability alternative) | MODELLED | `STAFFING-COVERAGE-VALIDATION.md` §1 | 2026-08-18 | Binomial reliability model, ≥95% target — an EMPLOYMENT POOL size for leave/sick coverage, NOT the simultaneous daily roster (8, VERIFIED, solver-driven) — see §6 below for this distinction made explicit |
| Phlebotomist recommended employment pool | 4 (or 3 lower-reliability alternative) | MODELLED | `STAFFING-COVERAGE-VALIDATION.md` §2 | 2026-08-18 | Binomial reliability model, 99.81% — deliberately above the 95% minimum given zero cross-training + WDP credentialing lead time |
| PM Reception relief pool | 1 small on-call backup (newly recommended) | MODELLED | `STAFFING-COVERAGE-VALIDATION.md` §4a | 2026-08-18 | No dollar cost until actually used, per the pool-vs-roster distinction |
| Venue Manager relief | None (disclosed single point of failure) | DECIDED | `STAFFING-COVERAGE-VALIDATION.md` §3 | 2026-08-18 | Permanent relief VM not recommended at launch scale — cost disproportionate |
| Startup capital (pre-opening) | A$251,198 | DECIDED | `startup_costs.yml#adopted_planning_scenarios` | Pre-2026-08-17 | Anthony's in-principle approval, not yet a locked final cost |
| Working capital reserve | A$85,000-110,000 | MODELLED | `CURRENT-STATE.md` §7.3 | Pre-2026-08-17 | Basis is a pre-rebase estimate, itself flagged stale elsewhere in this repo |
| Cash-flow trough (Table 1, current) | -A$76,532.52 at Month 2 | CALCULATED | `master_financial_model.yml#cash_flow_summary` | 2026-08-18 | Reflects the corrected, more realistic cost base |
| Break-even revenue (Table 1) | A$122,133.90/month | CALCULATED | `master_financial_model.yml#breakeven` | 2026-08-18 | |
| Break-even client volume (Table 1) | 13.051 clients/day | CALCULATED | `master_financial_model.yml#breakeven` | 2026-08-18 | Margin of safety 4.949 clients/day (27.5%) |

## Section 6 — Employment Pool vs. Simultaneous Roster, Made Explicit

**These are two genuinely different concepts, repeatedly conflated in earlier rounds — clarified structurally here, per Anthony's explicit instruction this round:**

| Concept | Treatment | Phlebotomy | What it means |
|---|---|---|---|
| **Simultaneous daily roster (priced in payroll)** | 8 | 2 | The number of people who must be physically present and working at the same time every trading day — this is what `data/canonical/cost_ramp.yml`'s `payroll_costs` field prices, in full, every month, with no absence assumed |
| **Recommended employment pool (NOT priced in payroll directly)** | 12 (or 11) | 4 (or 3) | The number of real people to actually HAVE ON THE BOOKS, so that when someone from the daily roster above is unavailable, a replacement exists — these extra people are only paid when they actually work a shift covering an absence |
| **Relief/absence coverage allowance (a separate, NEW payroll-adjacent line)** | Combined A$6,128.53/month across all committed roles | | The EXPECTED cost of the pool above actually being used, modelled as a recurring planning allowance (not a per-person cost), now included in Total Operating Costs as its own line, kept visibly separate from the committed-roster Direct Labour figure |

**Confirmed this round:** the payroll model was NOT double-counting or conflating these three concepts before this round's fix — it simply had zero cost for the third concept (relief actually being used). That gap is now closed with a real, quantified, propagated figure.

---

## Changelog

**2026-08-18** — Created per Anthony's explicit Step 7 instruction, consolidating every material financial assumption from across this repo's architecture documents into one register with consistent certainty labelling. Two assumptions materially corrected this round (insurance, relief/absence allowance) — both fully propagated through the canonical model and every current-facing financial document, not left as unactioned findings.
