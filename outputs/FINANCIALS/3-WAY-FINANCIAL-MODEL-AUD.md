# GTT Center Perth: 3-Way Financial Model (AUD)

**Prepared by:** Theodore (CFO consultant) for Grace (GTT Center Perth manager)
**Version:** v0.3 (2026-10-11, demand-responsive rostering)
**Date:** 2026-10-11
**Repo snapshot:** clawanthonyzed/gtt-center-perth, commit `14b747d` (v0.1), `d96215a` (v0.2), re-checked at `01f769d` for v0.3 (read-only)
**Currency:** every figure is in Australian dollars (A$). No foreign amounts are used.

> **Read this first**
> - 🆕 **What v0.3 changes:** Anthony's mandate (2026-10-11): *"Staff will be rostered depending on the amount of clients that morning. We want to have a waitlist and clients book weeks in advance."* v0.2 paid the full 8 treatment staff + 2 phlebotomists every morning from Month 1. v0.3 rosters the casual phlebotomists and therapists to each morning's confirmed bookings, using the repo's own solver-verified staffing tiers and wage rates (Section 1A).
> - 📌 **Baseline kept:** the v3.0 committed model, locked as the headline by Anthony on 2026-10-10: 18 AM clients/day at capacity, 07:00 start ([CURRENT-STATE.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/CURRENT-STATE.md) §0 and §5). Revenue, ramp, prices, rent and overheads are unchanged from v0.2. Only labour changes.
> - 🏠 **Rent:** the headline still uses **A$8,000/month, per Anthony's instruction.** Rent-adjusted A$9,500 and A$10,500 columns sit beside it, plus a new **gross ceiling** column (A$10,500 all-in per the [site brief v0.3](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/outputs/LEASING/COMMERCIAL-SITE-BRIEF.md)). Section 9 states the utilities / cleaning assumption.
> - ⚠️ **One decision is still needed:** the cheaper 4-therapist roster for mornings with 10 or fewer bookings needs a 45-minute pair cadence. The repo solver says it works inside the lab's 10:30am window, but it is **"presented, not adopted"** and needs Anthony's sign-off (S29 §3). Without it, see Section 14 for the fallback.
> - 🧮 Nothing here is real trading data. No venue is open yet. Every figure is a planning estimate.
> - 🧾 Tax, GST and award content is **general information only**. Verify tax with the accountant and award rules with Fair Work before acting.
> - 🏢 The business's legal entity and ownership structure are **not stated here**. The repo lists this as an open founder and accountant decision ([ENTITY-STRUCTURE-INVESTIGATION.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md)).

---

## Source key

Tables cite sources using these short codes. Each code links to the real file.

| Code | File |
|---|---|
| S1 | [docs/CURRENT-STATE.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/CURRENT-STATE.md) |
| S2 | [data/canonical/revenue_ramp.yml](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/data/canonical/revenue_ramp.yml) |
| S3 | [data/canonical/cost_ramp.yml](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/data/canonical/cost_ramp.yml) |
| S4 | [docs/profit-loss-tables.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/profit-loss-tables.md) (v3.0) |
| S5 | [docs/architecture/FINANCIAL-POSITION-CURRENT.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/FINANCIAL-POSITION-CURRENT.md) §4 (overhead line items only) |
| S6 | [data/canonical/startup_costs.yml](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/data/canonical/startup_costs.yml) |
| S7 | [docs/architecture/STARTUP-COST-OPTIMISATION.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/STARTUP-COST-OPTIMISATION.md) |
| S8 | [docs/architecture/MVP-OPENING-DECISION-REVIEW.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/MVP-OPENING-DECISION-REVIEW.md) |
| S9 | [docs/architecture/startup-cost-reconstruction.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/startup-cost-reconstruction.md) |
| S10 | [docs/equipment-costs.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/equipment-costs.md) |
| S11 | [docs/cash-flow.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/cash-flow.md) (GST section) |
| S12 | [docs/financial-setup.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/financial-setup.md) (BAS and GST coding) |
| S13 | [docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md) |
| S14 | [docs/research/RENT-ECONOMICS-FORENSICS.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/research/RENT-ECONOMICS-FORENSICS.md) |
| S15 | [docs/research/CAPEX-FITOUT-FORENSICS.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/research/CAPEX-FITOUT-FORENSICS.md) |
| S16 | [docs/DECISION-LOG.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/DECISION-LOG.md) |
| S17 | [docs/rent-budget-2026-07-28.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/rent-budget-2026-07-28.md) |
| S18 | [docs/architecture/REVENUE-RAMP-METHODOLOGY.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/REVENUE-RAMP-METHODOLOGY.md) |
| S19 | [data/models/master_financial_model.yml](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/data/models/master_financial_model.yml) |
| S20 | [outputs/FOUNDER-CFO-ANALYSIS.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/outputs/FOUNDER-CFO-ANALYSIS.md) |
| S21 | [outputs/GTT-Center-Perth-Financial-Model.xlsx](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/outputs/GTT-Center-Perth-Financial-Model.xlsx) |
| S22 | [outputs/master-dossier/index.html](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/outputs/master-dossier/index.html) and [outputs/master-dossier-v2/index.html](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/outputs/master-dossier-v2/index.html) |
| S23 | [docs/architecture/CONSTRUCTION-COST-BASIS-INVESTIGATION.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/CONSTRUCTION-COST-BASIS-INVESTIGATION.md) |
| S24 | [docs/services-pricing-locked.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/services-pricing-locked.md) |
| S25 | [docs/pricing-billing-strategy.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/pricing-billing-strategy.md) |
| S26 | [docs/research/PATHOLOGY-PARTNER-ECONOMICS.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/research/PATHOLOGY-PARTNER-ECONOMICS.md) |
| S27 | [docs/research/PATHOLOGY-OPERATIONS-DEEP-DIVE.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/research/PATHOLOGY-OPERATIONS-DEEP-DIVE.md) §4 |
| S28 | [docs/onboarding.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/onboarding.md) (payment, cancellation and no-show policy) |
| S29 | 🆕 [docs/architecture/AM-DEMAND-DRIVEN-STAFFING-TIERS-2026-09.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/AM-DEMAND-DRIVEN-STAFFING-TIERS-2026-09.md) (solver tiers, 2026-09-19, the current staffing source) |
| S30 | 🆕 [docs/architecture/AM-STAFFING-RAMP-OPTIMISATION.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/AM-STAFFING-RAMP-OPTIMISATION.md) (what is fixed vs what flexes) |
| S31 | 🆕 [tools/cost_ramp_model.py](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/tools/cost_ramp_model.py) (wage rates, `am_treatment_monthly_for_headcount`, 3-hour floor) |
| S32 | 🆕 [docs/pm-staffing-roster.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/pm-staffing-roster.md) (booking-driven rostering, waitlist targets, staffing decision point) |
| S33 | 🆕 [docs/financial-break-even-staff.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/financial-break-even-staff.md) (award casual rates, 1 July 2026) |
| S34 | 🆕 [docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md), [docs/am-staffing-by-volume.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/am-staffing-by-volume.md) (older, pre-tier work, context only) |
| S35 | 🆕 [docs/dual-role-staffing-model-2026-07-28.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/dual-role-staffing-model-2026-07-28.md) and [docs/staff-plan.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/staff-plan.md) (one flexible casual pool) |
| S36 | 🆕 [outputs/LEASING/COMMERCIAL-SITE-BRIEF.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/outputs/LEASING/COMMERCIAL-SITE-BRIEF.md) v0.3 (A$10,500 gross ceiling) |
| **TM** | **This model's own assumption or arithmetic.** Always listed in Section 8. |

---

## 1. Key numbers card

v0.3 figures first. The v0.2 figure (full roster from Month 1) is shown in brackets where it changed.

| | Headline (A$8,000 rent) ✅ | Rent-adjusted A$9,500 | Rent-adjusted A$10,500 | Gross ceiling A$10,500 all-in | Status |
|---|---|---|---|---|---|
| 💰 **Total startup capital** | **A$336,198** | A$339,198 | A$341,198 | A$341,198 | 🟡 Unchanged from v0.2 (S1 §6, S6, S8) |
| 👥 **Payroll, Months 1 to 3** | **A$214,844** (v0.2 A$280,787) | same | same | same | 🟢 Saves **A$65,943** (Section 3a) |
| 📈 **Monthly net, Month 5 onward (repo basis)** | **+A$35,186.40** (unchanged) | +A$33,686.40 | +A$32,686.40 | +A$33,936.40 | 🟢 Full roster needed at 18/day (Section 12) |
| 🧾 **GST-stress downside** | **+A$23,442.58** (unchanged) | +A$22,078.94 | +A$21,169.85 | +A$22,306.21 | 🟠 TM, accountant to confirm |
| ⚖️ **Break-even, AM clients/day (repo basis)** | **8.266** (v0.2 12.655) | 8.493 (12.882) | 8.645 (13.034) | 8.455 (12.844) | 🟢 Headline matches the repo's own LOW-segment figure (S1 §10) |
| ⚖️ Break-even, AM clients/day (GST-stress) | 9.255 (v0.2 14.083) | 9.482 (14.310) | 9.634 (14.462) | 9.444 (14.272) | 🟠 TM |
| 🏦 **Peak funding** (with GST timing) | **A$267,771** (v0.2 A$318,176) | A$272,271 (A$325,403) | A$275,271 (A$330,222) | A$274,021 (A$326,699) | 🟢 About A$50k to A$55k lower |
| ⚠️ **Lowest cash point** | **A$68,427, Month 1** (v0.2 A$18,022, Month 3) | A$66,927 (A$13,795) | A$65,927 (A$10,976) | A$67,177 (A$14,499) | 🟢 Headroom roughly 4 to 6 times larger |
| 🛟 Runway if bookings stall at Month 1 volume | **4 full months** (v0.2: 1) | 3 (1) | 3 (1) | 4 (1) | 🆕 Months the A$85,000 reserve lasts (Section 4b) |
| ⏱️ **Payback** (repo basis / after GST) | **Month 11 / Month 15** (v0.2 M13 / M18) | M11 / M16 (M14 / M19) | M12 / M17 (M14 / M20) | M11 / M16 (M13 / M19) | 🟢 Sections 7 and 9 |
| 📅 Year 1 net (repo basis / after GST) | **A$322,015 / A$196,609** (v0.2 A$251,522 / A$126,115) | A$304,015 / A$180,245 | A$292,015 / A$169,336 | A$307,015 / A$182,972 | 🟢 |
| 🧪 Lab / courier fee to GTT | A$0 per client (repo assumption) | | | | 🟠 Tender fees TO CONFIRM. Each A$10/client costs about A$4,739/month at capacity (Section 10) |
| 🧾 Two-tier GST (proposed) | +A$2,154/month vs GST-stress if A$50 of each A$250 package is GST-free | | | | 🔴 Proposed only (Section 11) |

**Plain English:**
- Rostering to bookings does not change what the business earns at full capacity. At 18 clients a morning every role is needed, so Month 5 onward is still about **A$35.2k a month**.
- What changes is the **ramp-up**. Months 1 to 3 cost about **A$66k less** in wages, Month 1's loss falls from about A$45k to about A$17k, and Month 2 turns positive.
- The cash low is now about A$68k (Month 1) instead of about A$18k (Month 3). Payback comes about 2 to 3 months sooner.
- Break-even drops from about 12.7 to about 8.3 clients a morning, **if** bookings are steered to fill mornings in the tiers shown in Section 1A, and **if** Anthony signs off the 45-minute cadence for quiet mornings.

---

## 1A. Demand-responsive rostering rule (🆕 v0.3)

### 1A-i. What can flex and what stays fixed

| Role / cost | v0.3 treatment | Why | Source |
|---|---|---|---|
| Phlebotomists (2, casual, employed in-house) | **Variable by morning.** Rostered only on mornings with at least 1 confirmed GTT booking | Both chairs run in synchronised pairs; the repo has never solved a single-chair mode, so the floor is 2 on any morning with a GTT client | S29 §2, S30 §1, S1 §4 (in-house decision 2026-09-19) |
| AM therapists (massage + beauty pool, nails, hair; casual) | **Variable by morning:** 4 on mornings with 6 to 10 bookings, 8 on mornings with 11 to 18 | Solver-verified tiers | S29 §2, S31 `AM_HEADCOUNT_LOW` / `AM_HEADCOUNT_HIGH` |
| PM therapists (4 roles, casual) | Kept as in v0.2: each role paid the 3-hour minimum engagement every weekday and Saturday | Already priced at the legal floor at every PM ramp month. A PM role with zero bookings could be stood down, but the repo has no per-role PM booking mix, so no saving is counted (upside) | S31 `compute_pm_weekday_daily_labor`, S4 §2 |
| Venue Manager (Mon to Fri, A$320/day) | **Fixed** A$7,040/month | Safety-critical, must be on site every operating day (first aid, fire warden, clinical escalation) | S30 §1, S1 §0 item 2 |
| Reception | **Fixed, no separate line.** AM reception is the Venue Manager's role; PM reception is covered by rostered PM staff (dedicated PM reception role removed 2026-08-21) | | S31 `compute_payroll` docstring, S1 §4 |
| Saturday Venue Manager cover | An experienced staff member already rostered that day. No loading costed | Pay loading still open | S1 §0 item 2 |
| Rent, insurance, software, accounting, laundry, utilities, cleaning, misc, marketing, supplies | **Fixed**, unchanged from v0.2 | | S3, S5 §4 |

**Wage rates (all from the repo, none invented):** massage / beauty A$37.50/hr, nails and hair A$36.81/hr, phlebotomist A$34.375/hr (SS Level 1-2 midpoint), Venue Manager A$40.00/hr. These are the award **casual** rates, so the 25% casual loading is already inside them (S33 "Casual Rate" column; S31 comments). Saturday = 1.5 times the casual rate (repo method, S31). Super 12% and workers comp 1.7% on every wage line (S31). Shifts are paid as the full 6-hour 07:00 to 13:00 AM window, the repo's conservative basis (S31). The 3-hour minimum engagement is the repo's verified figure (S31 `CASUAL_MINIMUM_ENGAGEMENT_HOURS`; S4 §2 cites MA000005 cl. 11.5 and MA000027 cl. 11.2).

> General information, verify with Fair Work: casual minimum engagement, Saturday penalty rates for casuals, notice for roster changes, and casual conversion rights. The repo's rates were researched from third-party calculators, not the primary award text (S33).

### 1A-ii. The rostering rule table (one morning)

Labour cost per morning, wages only for the AM clinical and treatment roster. "Incl. on-costs" adds super 12% and workers comp 1.7%. The Venue Manager is fixed and not in these figures.

| Confirmed bookings that morning | Phlebotomists | Therapists | Pair cadence | Weekday wages | **Weekday incl. on-costs** | Saturday incl. on-costs | Labour per client (weekday) | Rule |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | n/a | A$0.00 | **A$0.00** | A$0.00 | n/a | No AM clinical roster |
| 1 (clinical floor) | 2 | 1 (the booked service line) | n/a | A$637.50 | **A$724.84** | A$1,087.26 | A$724.84 | Floor: 2 phlebotomists must be on whenever any GTT client is booked |
| 2 to 5 | 2 | 1 to 4 (one per booked line, capped at the 6 to 10 roster) | 45 min | A$637.50 to A$1,304.22 | **A$724.84 to A$1,482.90** | up to A$2,224.35 | e.g. A$362.42 (2 clients, 1 therapist); A$296.58 (5 clients, 4 therapists) | 🟠 Repo has no solver result below 6 clients (S30 §3). Avoid: steer bookings to fill mornings |
| 6 to 10 | 2 | 4 (2 massage+beauty, 1 nails, 1 hair) | 45 min | A$1,304.22 | **A$1,482.90** | A$2,224.35 | A$247.15 to A$148.29 | ✅ Solver-verified at 6 and 9 (S29 §2). ⚠️ 45-min cadence needs Anthony's sign-off |
| 11 to 14 | 2 | 8 (4 massage+beauty, 2 nails, 2 hair) | 25 min | A$2,195.94 | **A$2,496.78** | A$3,745.18 | A$226.98 to A$178.34 | 🔴 Avoid: the costliest band per client. Hold the morning at 10 and offer the waitlisted client another morning inside her window |
| 15 to 18 | 2 | 8 | 25 min | A$2,195.94 | **A$2,496.78** | A$3,745.18 | A$166.45 to A$138.71 | ✅ Release slots 11 to 18 on a morning only when it can reach **15 firm bookings on a weekday or 17 on a Saturday** |

**How the triggers are worked out (TM):** moving a morning from 4 to 8 therapists costs A$891.72 in weekday wages, or A$1,013.89 with on-costs. At A$250 a client that needs 4.06 extra clients, so the 15th client. On a Saturday it is A$1,520.83, so 6.08 extra clients: the 17th.

**Clinical floor at 1 client:**
- Repo basis (6-hour shifts, 2 chairs): A$724.84 a weekday morning with on-costs. This is what any rostered morning costs at minimum.
- Legal minimum, for reference only: 2 phlebotomists plus 1 therapist at the 3-hour minimum = A$318.75 wages, A$362.42 with on-costs. One client needs about 07:00 to 09:15 (draw 3 is 120 minutes after draw 1, S29 §2), so 3 hours covers her. 🟡 Not used: early release is a separate repo upside (S1 §8), and a 1-phlebotomist morning is not solved in the repo.

**Why the waitlist and 2 to 4 week lead time make this work (TM, built on S32):**
- Clients pay in full when they book and the roster is published 1 to 2 weeks ahead from the confirmed Fresha calendar (S28, S32 "Staffing Decision Point").
- The referral is usually for 24 to 28 weeks of pregnancy, so each client has several mornings that suit her. That flexibility lets Grace fill one morning before opening the next band.
- The repo already plans the waitlist (100 signups by week 13, 300+ by week 18, S32) and service-interest checkboxes, so the therapist mix can follow what clients booked.

### 1A-iii. How the monthly model applies the rule (TM)

- Every trading morning opens with the 2 + 4 roster (6 to 10 clients).
- Demand above 10 a morning on average is steered into full 18-client mornings on the 2 + 8 roster. So the share of mornings on the full roster = (average clients/day less 10) / 8.
- Same rule for weekdays (22/month) and Saturdays (4.33/month), at the Saturday rate.
- Revenue uses the same fractional ramp volumes as v0.2. Staffing uses the band the morning falls in.

| Month | Average AM clients/morning | Mornings on the 2 + 4 roster | Mornings on the 2 + 8 roster |
|---|---|---|---|
| M1 (43%) | 7.74 | 100.0% | 0.0% |
| M2 (64%) | 11.52 | 81.0% | 19.0% |
| M3 (79%) | 14.22 | 47.3% | 52.8% |
| M4 (93%) | 16.74 | 15.8% | 84.3% |
| M5 onward | 18.00 | 0.0% | 100.0% |

Note: shares are rounded to 0.1%. Before rounding, M3 is 47.25% / 52.75% and M4 is 15.75% / 84.25%.

---

## 2. Startup CapEx and fit-out

### 2a. How low / base / high are chosen

| Tier | Total pre-opening | What it is | Source |
|---|---|---|---|
| Low | A$243,912 | "Minimum Viable Opening": every deferrable item deferred | S7 §2 |
| **Base** ✅ | **A$251,198** | **Founder-approved "Revised Recommended Opening Strategy" (2026-08-10).** MVP plus 5 restorations | S6, S8 |
| High | A$644,832 | "Full Build": high end of every range, 20% contingency | S7 §2 |

### 2b. Summary by group (pre-opening capital plus working capital)

| Group | Low | Base ✅ | High | Source |
|---|---|---|---|---|
| Equipment, non-clinical | A$12,950 | A$12,950 | A$34,980 | S7 §2 Cat E less clinical line (TM split) |
| Clinical / blood collection equipment | A$6,330 | A$6,330 | A$10,240 | S9 Cat E, S7 §3.2 ("protected, no reduction") |
| Furniture, fixtures, fittings, signage | A$14,160 | A$14,160 | A$51,800 | S7 §2 Cat D |
| Fit-out / construction | A$138,328 | A$139,678 | A$306,029 | S7 §2 Cat C; base +A$1,350 acoustic curtain fabric (S8) |
| IT / booking setup | A$820 | A$820 | A$7,550 | S7 §2 Cat G |
| Compliance, legal, design, approvals | A$7,639 | A$7,639 | A$28,239 | S7 Cat B + Cat J + legal fees from Cat A |
| Bond and lease | A$16,000 | A$16,000 | A$41,500 | S9 Cat A |
| Pre-opening staff, launch marketing, opening stock | A$21,552 | A$26,707 | A$57,022 | S7 Cat H+I+F; base per S8 restorations |
| Contingency | A$26,133 | A$26,914 | A$107,472 | S7, S8 (12% / 12% / 20%) |
| **Subtotal: pre-opening capital** | **A$243,912** | **A$251,198** | **A$644,832** | S6, S7, S8 |
| Opening working capital reserve | A$85,000 | A$85,000 | A$110,000 | S1 §7.3, S6 (flagged stale in repo, see Section 8) |
| **GRAND TOTAL startup capital** | **A$328,912** | **A$336,198** | **A$754,832** | Base matches S8 "A$336,198 to 361,198" bracket |

**Base group notes (S8):** fit-out includes acoustic-rated curtain fabric (+A$1,350). Pre-opening staff = A$22,872 (receptionist 3 weeks, Venue Manager 7 weeks, treatment trial 1 week). Marketing = A$1,250 (includes A$1,000 contingency reserve). Opening stock = A$2,585.

**TM split note:** the repo gives equipment only as one total (A$19,280) at base. The clinical line (A$6,330) is the repo's full-scope lean figure, kept whole because S7 §3.2 says pathology equipment is "protected, no reduction". Non-clinical equipment is the remainder.

### 2c. Item detail (full-scope scenarios A / B / C from S9)

The repo itemises lines only for its full-scope scenarios. These are shown so every line has a source. The adopted base above sits **below** Scenario A because it defers items (S7 §5).

**Equipment, non-clinical (S9 Cat E, from S10 room lists)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Nail (4 tables, dust collection, LEV, lamps, trolleys) | A$4,500 | A$6,850 | A$9,200 |
| Hair (dryers, straighteners, backwash hardware, mirror, trolleys) | A$4,400 | A$7,150 | A$9,900 |
| Beauty / brows | A$750 | A$1,145 | A$1,540 |
| Massage room | A$700 | A$1,000 | A$1,300 |
| Technology hardware (iPads, POS, printers, router, computer) | A$3,240 | A$5,580 | A$7,920 |
| Emergency / safety (first aid, AED, panic buttons, extinguisher) | A$2,360 | A$3,340 | A$4,320 |
| General cleaning equipment | A$300 | A$550 | A$800 |
| **Subtotal** | **A$16,250** | **A$25,615** | **A$34,980** |

⚠️ Not in any total: **cafe equipment A$5,000 to 12,650**, made day-one on 2026-08-23 (S10 Summary Budget). See Section 8.

**Clinical / blood collection equipment (S9 Cat E, from S10 §1)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| 2 phlebotomy chairs, vasovagal recovery chair, centrifuge, sharps / spill kit, specimen transport, documentation | A$6,330 | A$8,285 | A$10,240 |
| **Subtotal** | **A$6,330** | **A$8,285** | **A$10,240** |

⚠️ The 2nd Blood Collection Room (founder decision 2026-08-27, S16) may need a 2nd centrifuge, specimen fridge or recovery chair. This is open in the repo and not costed.

**Furniture, fixtures, fittings (S9 Cat D)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Lounge and common-area furniture | A$5,000 | A$10,000 | A$15,000 |
| Reception furniture (not the built counter) | A$800 | A$1,400 | A$2,000 |
| Treatment beds (2 massage + 2 facial / beauty) | A$2,400 | A$4,600 | A$6,800 |
| Styling, manicure and pedicure chairs (4 each) | A$6,000 | A$10,200 | A$14,400 |
| Staff room furniture | A$1,500 | A$2,500 | A$3,500 |
| Signage (shopfront + wayfinding) | A$3,000 | A$5,500 | A$8,000 |
| Decorations / branding | A$500 | A$1,250 | A$2,000 |
| Storage hampers (2) | A$60 | A$80 | A$100 |
| **Subtotal** | **A$19,260** | **A$35,530** | **A$51,800** |

**Fit-out / construction, 239 sqm (S9 Cat C, anchored to the floor-plan concept build)**

| Trade | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Demolition / strip-out | A$6,498 | A$9,370 | A$12,241 |
| Walls / partitions (collection room only) | A$12,996 | A$18,739 | A$24,482 |
| Doors | A$3,249 | A$4,685 | A$6,121 |
| Electrical | A$29,241 | A$42,163 | A$55,085 |
| Plumbing (Code-required wet areas, WCs, kitchenette) | A$24,368 | A$35,136 | A$45,904 |
| Lighting fixtures | A$12,996 | A$18,739 | A$24,482 |
| Flooring | A$16,245 | A$23,424 | A$30,603 |
| Painting / wall finishes | A$8,123 | A$11,712 | A$15,301 |
| Cabinetry / joinery | A$16,245 | A$23,424 | A$30,603 |
| HVAC | A$16,245 | A$23,424 | A$30,603 |
| Reception build | A$4,874 | A$7,027 | A$9,181 |
| Staff area fit-out | A$4,874 | A$7,027 | A$9,181 |
| Acoustic treatment for curtain bays | A$4,874 | A$7,027 | A$9,181 |
| Privacy curtain systems (4 bays) | A$1,625 | A$2,342 | A$3,060 |
| Rounding difference in repo's % split | -A$1 | A$2 | A$1 |
| **Subtotal** | **A$162,452** | **A$234,241** | **A$306,029** |

Note: S9 splits the construction total by trade percentages and rounds each line. Its lines add to A$1 to A$2 off its own subtotals. The subtotal is the source figure.

⚠️ Not costed: the extra ~18 to 20 sqm from the 2nd collection room (S16). The repo's own construction rate is not externally benchmarked (S23), and S15 finds clinical-grade space may cost A$39,000 to 60,450 more. See Section 8.

**IT / booking setup (S9 Cat G)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Website build | A$1,500 | A$3,000 | A$6,000 |
| Domain | A$20 | A$35 | A$50 |
| IT install (network, WiFi, POS setup labour) | A$500 | A$900 | A$1,500 |
| Fresha booking system setup (no setup fee; A$14.95/user/month is opex) | A$0 | A$0 | A$0 |
| Xero setup (bundled with accountant) | A$0 | A$0 | A$0 |
| **Subtotal** | **A$2,020** | **A$3,935** | **A$7,550** |

**Compliance, legal, design and approvals (S9 Cat A legal line, Cat B, Cat J)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Architect / designer drawings | A$5,000 | A$9,000 | A$15,000 |
| Skin Penetration Code / pathology-standards consulting | A$0 | A$1,500 | A$3,000 |
| Council planning / building permit fees | A$500 | A$1,000 | A$2,000 |
| Food Safety Supervisor certificate | A$100 | A$150 | A$200 |
| WorkSafe WA nail extraction pre-application | A$0 | A$0 | A$500 |
| Pathology partner room review (no fee found) | A$0 | A$0 | A$0 |
| Legal fees (lease review + setup paperwork) | A$3,000 | A$4,500 | A$6,000 |
| Accountant (initial brief + structure advice) | A$500 | A$1,000 | A$1,500 |
| ASIC business name | A$39 | A$39 | A$39 |
| **Subtotal** | **A$9,139** | **A$17,189** | **A$28,239** |

Insurance has no setup fee. The premium is an operating cost (A$708.34/month, modelled, not a quote: S5, S3).

**Bond and lease (S9 Cat A, rent A$8,000/month from S17)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Lease bond (1 / 2 / 3 months' rent) | A$8,000 | A$16,000 | A$24,000 |
| Advance rent (1 / 1 / 2 months) | A$8,000 | A$8,000 | A$16,000 |
| Tenant agent / application fee | A$0 | A$0 | A$1,500 |
| **Subtotal** | **A$16,000** | **A$24,000** | **A$41,500** |

**Pre-opening staff, launch marketing, opening stock (S9 Cat H, I, F)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Recruitment ads | A$2,000 | A$2,900 | A$3,750 |
| Venue Manager pre-opening salary (8 / 11 / 14 weeks) | A$12,496 | A$17,182 | A$21,868 |
| Phlebotomist credentialing (2 staff) | A$1,225 | A$1,838 | A$2,450 |
| Receptionist training | A$1,602 | A$2,403 | A$3,204 |
| Treatment staff trial / induction | A$3,480 | A$7,830 | A$13,920 |
| First Aid / Fire Warden course | A$150 | A$220 | A$300 |
| Professional photography | A$800 | A$1,400 | A$2,000 |
| Pre-launch marketing push | A$600 | A$1,500 | A$3,000 |
| Referral outreach materials | A$200 | A$350 | A$500 |
| Opening consumables stock (all rooms) | A$3,380 | A$4,706 | A$6,030 |
| **Subtotal** | **A$25,933** | **A$40,329** | **A$57,022** |

Note: S7 §0 corrects Scenario B's treatment trial to 8 staff (+A$2,610). The table shows S9 as published.

**Contingency (S9 Cat K)**

| Item | A (lean) | B (expected) | C (high) |
|---|---|---|---|
| Contingency (10% / 15% / 20%) | A$25,738 | A$58,369 | A$107,472 |
| **Subtotal** | **A$25,738** | **A$58,369** | **A$107,472** |

**Full-scope totals (S9):** A A$283,122 / B A$447,493 / C A$644,832.

### 2d. Spend deferred to after opening (S7 §5, not in base)

| Item | Amount | Timing used in cashflow |
|---|---|---|
| Nail stations 3 and 4 | A$3,000 | Month 4 (S8 §4.3 trigger) |
| Hair chairs 3 and 4 | A$2,600 | Month 4 (S8 §4.3 trigger) |
| Acoustic treatment for curtain bays | A$4,874 | Month 6 (TM) |
| Full website build | A$1,200 | Month 6 (TM) |
| Professional photography | A$1,000 | Month 6 (TM) |
| 3rd iPad + colour printer | A$700 | Month 6 (TM) |
| **Total deferred** | **A$13,374** | |

---

## 3. 12-month P&L by month (Table 1, committed model, demand-responsive rostering)

**Ramp:** unchanged, the repo's own curve. Revenue is 43% / 64% / 79% / 93% of steady state in Months 1 to 4, then 100% (S2, S18). 🟡 The repo flags that this curve's origin is undocumented (S2 `conflict_ramp_curve_origin_unknown`).

**Costs:** 🆕 AM phlebotomist and therapist wages now follow the rostering rule in Section 1A. PM labour, the Venue Manager and every non-wage line are as in v0.2. Marketing still ramps A$600 / 800 / 1,000 / 1,200, then A$1,500 (S3, S4).

**Line definitions:**
- AM GTT = average AM clients/day x A$250 x 26.33 trading days (S1 §5, S2).
- PM standalone = 10 sessions/day at steady state, about 210 transactions/month at A$117 average, ramped like v0.2 (S13).
- Ancillary (cafe / retail) = A$0, excluded by founder decision (S1, S4).
- Direct costs = GTT supplies A$400 + consumables A$800 (S5 §4, S3).
- Payroll = AM rostered wages (Section 1A) + PM wages A$12,704.74 + Venue Manager A$7,040.00 + super 12% + workers comp 1.7% (S31).
- Rent = A$8,000 (founder decision 2026-10-03, S16).
- Other overhead = utilities, insurance, laundry, marketing, software, cleaning, accounting, misc (S5 §4, S3).

| Month | Ramp | AM clients/day | AM GTT | PM standalone | **Total revenue** | Direct costs | Payroll | Rent | Other overhead | **Total costs** | **Net** | Cumulative net | v0.2 net |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 43% | 7.74 | A$50,948.55 | A$10,571.71 | A$61,520.26 | A$1,200.00 | A$64,704.95 | A$8,000.00 | A$4,188.34 | A$78,093.29 | 🔴 -A$16,573.03 | -A$16,573.03 | -A$45,463.71 |
| M2 | 64% | 11.52 | A$75,830.40 | A$15,734.64 | A$91,565.04 | A$1,200.00 | A$70,194.19 | A$8,000.00 | A$4,388.34 | A$83,782.53 | 🟢 A$7,782.51 | -A$8,790.52 | -A$15,618.93 |
| M3 | 79% | 14.22 | A$93,603.15 | A$19,422.44 | A$113,025.59 | A$1,200.00 | A$79,944.77 | A$8,000.00 | A$4,588.34 | A$93,733.11 | 🟢 A$19,292.48 | A$10,501.96 | A$5,641.62 |
| M4 | 93% | 16.74 | A$110,191.05 | A$22,864.39 | A$133,055.44 | A$1,200.00 | A$89,045.33 | A$8,000.00 | A$4,788.34 | A$103,033.67 | 🟢 A$30,021.77 | A$40,523.73 | A$25,471.47 |
| M5 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$75,710.13 | A$35,186.40 |
| M6 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$110,896.53 | A$35,186.40 |
| M7 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$146,082.93 | A$35,186.40 |
| M8 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$181,269.33 | A$35,186.40 |
| M9 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$216,455.73 | A$35,186.40 |
| M10 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$251,642.13 | A$35,186.40 |
| M11 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$286,828.53 | A$35,186.40 |
| M12 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$322,014.93 | A$35,186.40 |
| **Year 1** | | | **A$1,278,453.15** | **A$265,276.14** | **A$1,543,729.29** | **A$14,400.00** | **A$1,052,654.28** | **A$96,000.00** | **A$58,660.08** | **A$1,221,714.36** | **A$322,014.93** | | **A$251,521.65** |

### 3a. Labour build: v0.3 vs v0.2 (🆕)

| Month | AM clients/day | Mornings on 2 + 8 roster | AM rostered wages (v0.3) | AM wages (v0.2, full roster) | PM + Venue Manager wages (fixed) | Super 12% + workers comp 1.7% (v0.3) | **Payroll v0.3** | **Payroll v0.2** | **Saving** |
|---|---|---|---|---|---|---|---|---|---|
| M1 | 7.74 | 0.0% | A$37,163.75 | A$62,573.31 | A$19,744.74 | A$7,796.46 | A$64,704.95 | A$93,595.63 | A$28,890.68 |
| M2 | 11.52 | 19.0% | A$41,991.57 | A$62,573.31 | A$19,744.74 | A$8,457.88 | A$70,194.19 | A$93,595.63 | A$23,401.44 |
| M3 | 14.22 | 52.8% | A$50,567.29 | A$62,573.31 | A$19,744.74 | A$9,632.74 | A$79,944.77 | A$93,595.63 | A$13,650.86 |
| M4 | 16.74 | 84.3% | A$58,571.30 | A$62,573.31 | A$19,744.74 | A$10,729.29 | A$89,045.33 | A$93,595.63 | A$4,550.30 |
| M5 to M12 (each) | 18.00 | 100.0% | A$62,573.31 | A$62,573.31 | A$19,744.74 | A$11,277.58 | A$93,595.63 | A$93,595.63 | A$0.00 |
| **Year 1** | | | **A$688,880.39** | **A$750,879.72** | **A$236,936.88** | **A$126,837.01** | **A$1,052,654.28** | **A$1,123,147.56** | **A$70,493.28** |
| **Months 1 to 3** | | | **A$129,722.61** | **A$187,719.93** | **A$59,234.22** | **A$25,887.08** | **A$214,843.91** | **A$280,786.89** | **A$65,942.98** |

Year 1 rows add the M5 to M12 line 8 times. PM + Venue Manager wages = PM weekday A$9,808.92 + PM Saturday A$2,895.82 + Venue Manager A$7,040.00 (S3).

**Plain English:** the saving is biggest in Month 1 (about A$28.9k), shrinks as mornings fill, and is zero from Month 5 when every morning needs the full team.

### 3b. Steady-state payroll breakdown (Month 5 onward, unchanged from v0.2, S3 `cost_table1_m5plus`)

| Payroll line | Monthly |
|---|---|
| AM weekday treatment staff (8) | A$39,235.68 |
| AM weekday phlebotomists (2) | A$9,075.00 |
| AM Saturday direct labour | A$14,262.63 |
| PM weekday direct labour (3-hour casual minimum floor) | A$9,808.92 |
| PM Saturday direct labour | A$2,895.82 |
| Opening-time increment (Venue Manager, Mon to Fri) | A$7,040.00 |
| Superannuation (12%) | A$9,878.17 |
| Workers compensation (1.7%, placeholder rate) | A$1,399.41 |
| **Total payroll** | **A$93,595.63** |

### 3c. Steady-state other overhead breakdown (unchanged, S5 §4, total matches S3 A$14,288.34)

| Line | Monthly |
|---|---|
| Utilities | A$650.00 |
| Insurance (modelled, not a quote) | A$708.34 |
| Laundry | A$350.00 |
| Marketing (Month 5 onward) | A$1,500.00 |
| Software (Fresha, email, internet / phone) | A$280.00 |
| Cleaning | A$600.00 |
| Accounting / bookkeeping | A$500.00 |
| Miscellaneous / contingency | A$500.00 |
| **Total other overhead** | **A$5,088.34** |

Check: other overhead A$5,088.34 + rent A$8,000 + direct costs A$1,200 = A$14,288.34 non-wage overhead (S3).

### 3d. GST estimate per month (general information only, TM)

The repo's P&L figures are **GST-inclusive** and have **no line for GST paid to the ATO** (S11). Same method as v0.2: all revenue taxable at 10%; credits on rent, consumables and other overhead; GTT supplies GST-free (S12); wages and super carry no GST. GST on sales and credits are unchanged from v0.2, because revenue and non-wage costs are unchanged.

| Month | GST on sales (rev ÷ 11) | GST credits | **Net GST owed** | **Net after GST** | v0.2 net after GST |
|---|---|---|---|---|---|
| M1 | A$5,592.75 | A$1,180.76 | A$4,411.99 | -A$20,985.02 | -A$49,875.70 |
| M2 | A$8,324.09 | A$1,198.94 | A$7,125.15 | A$657.36 | -A$22,744.08 |
| M3 | A$10,275.05 | A$1,217.12 | A$9,057.93 | A$10,234.55 | -A$3,416.31 |
| M4 | A$12,095.95 | A$1,235.30 | A$10,860.65 | A$19,161.12 | A$14,610.82 |
| M5 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M6 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M7 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M8 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M9 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M10 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M11 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| M12 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 | A$23,442.58 |
| **Year 1** | **A$140,339.04** | **A$14,932.76** | **A$125,406.28** | **A$196,608.65** | **A$126,115.37** |

🟠 If the A$250 package price includes GST, about A$22.73 of each package belongs to the ATO. That cuts steady-state net from A$35,186 to about A$23,443, exactly as in v0.2.

Not modelled: income tax (entity undecided), depreciation (the repo P&L has none), interest (no debt assumed).

---

## 4. Cashflow by month

**Rules used (unchanged from v0.2):**
- Opening funding = base startup capital A$336,198 (Section 2), all received before opening (TM, no debt assumed).
- Pre-opening capital A$251,198 is spent in Month 0, including the full contingency (TM, conservative).
- Operating cash = monthly P&L net. No debtor or creditor timing (S11, S21). Clients prepay at booking (S28), so this is if anything slightly conservative.
- GST: monthly BAS, paid the month after (S12).
- Deferred capex per Section 2d (Month 4 A$5,600, Month 6 A$7,774).

| Month | Opening cash | Funding in | CapEx out | Operating cash | GST paid (BAS) | **Closing cash** | v0.2 closing |
|---|---|---|---|---|---|---|---|
| M0 (pre-opening) | A$0.00 | A$336,198.00 | -A$251,198.00 | A$0.00 | A$0.00 | **A$85,000.00** | A$85,000.00 |
| M1 | A$85,000.00 | A$0.00 | A$0.00 | -A$16,573.03 | A$0.00 | ⚠️ **A$68,426.97** (lowest) | A$39,536.29 |
| M2 | A$68,426.97 | A$0.00 | A$0.00 | A$7,782.51 | -A$4,411.99 | **A$71,797.49** | A$19,505.37 |
| M3 | A$71,797.49 | A$0.00 | A$0.00 | A$19,292.48 | -A$7,125.15 | **A$83,964.82** | A$18,021.84 |
| M4 | A$83,964.82 | A$0.00 | -A$5,600.00 | A$30,021.77 | -A$9,057.93 | **A$99,328.66** | A$28,835.38 |
| M5 | A$99,328.66 | A$0.00 | A$0.00 | A$35,186.40 | -A$10,860.65 | **A$123,654.41** | A$53,161.13 |
| M6 | A$123,654.41 | A$0.00 | -A$7,774.00 | A$35,186.40 | -A$11,743.82 | **A$139,322.99** | A$68,829.71 |
| M7 | A$139,322.99 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$162,765.57** | A$92,272.29 |
| M8 | A$162,765.57 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$186,208.15** | A$115,714.87 |
| M9 | A$186,208.15 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$209,650.73** | A$139,157.45 |
| M10 | A$209,650.73 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$233,093.31** | A$162,600.03 |
| M11 | A$233,093.31 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$256,535.89** | A$186,042.61 |
| M12 | A$256,535.89 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$279,978.47** | A$209,485.19 |

### 4a. Peak funding requirement

| Measure | v0.3 | v0.2 | Note |
|---|---|---|---|
| Pre-opening capital spent (Month 0) | A$251,198.00 | A$251,198.00 | S8 |
| Deepest drop after opening, with GST | A$16,573.03 (Month 1) | A$66,978.16 (Month 3) | Reserve A$85,000 less lowest cash |
| **Peak funding requirement (with GST timing)** | **A$267,771.03** | A$318,176.16 | Capital less lowest cash |
| Peak funding requirement (repo basis, no GST) | A$267,771.03 | A$312,280.64 | v0.3 low is Month 1, before the first BAS, so both bases match |
| **Headroom inside A$336,198 base** | **A$68,426.97** | A$18,021.84 | 🟢 Now covers a large part of the uncosted floor-area fit-out (item 12b, up to A$63,750) |

🟢 v0.3 does **not** cut the startup capital. The extra headroom is needed for the open fit-out items in Section 8 and for the stall risk below.
🟢 Unspent contingency (up to A$26,914) and GST credits on fit-out would add further headroom (not counted, TM).
🔴 Rent during the fit-out period is still not in the base budget (item 28).

### 4b. Runway if bookings stall (🆕 TM)

Test: bookings stay at Month 1 volume (7.74 clients/day) forever, GST paid the month after. How many full months does the A$85,000 reserve last?

| | Monthly cash burn (after first BAS) | Full months covered | Cash runs out in |
|---|---|---|---|
| **v0.3 headline** | A$20,985.02 (A$16,573.03 loss + A$4,411.99 GST) | **4** | Month 5 |
| v0.2 headline | A$49,875.70 (A$45,463.71 loss + A$4,411.99 GST) | 1 | Month 2 |
| v0.3 at A$9,500 / A$10,500 / gross ceiling | | 3 / 3 / 4 | Month 4 / 4 / 5 |

**Plain English:** under v0.2 a slow start would empty the reserve in the second month. Under v0.3 there are about 4 months to fix marketing or referral flow before more money is needed.

---

## 5. Balance sheet snapshots (simple)

**Method (TM, unchanged):** fit-out, design and approvals, contingency, furniture and equipment are capitalised. Advance rent, legal fees, IT setup, pre-opening wages, launch marketing and professional fees (A$36,481 total) are expensed before opening. Assets at cost, no depreciation. Retained earnings use **net after GST** (Section 3d).

| Line | Opening day (end M0) | Month 6 | Month 12 |
|---|---|---|---|
| Cash | A$85,000.00 | A$139,322.99 | A$279,978.47 |
| Fit-out, furniture, equipment (at cost) | A$204,132.00 | A$217,506.00 | A$217,506.00 |
| Opening stock | A$2,585.00 | A$2,585.00 | A$2,585.00 |
| Lease bond | A$8,000.00 | A$8,000.00 | A$8,000.00 |
| **Total assets** | **A$299,717.00** | **A$367,413.99** | **A$508,069.47** |
| GST payable to ATO | A$0.00 | A$11,743.82 | A$11,743.82 |
| **Total liabilities** | **A$0.00** | **A$11,743.82** | **A$11,743.82** |
| Capital contributed | A$336,198.00 | A$336,198.00 | A$336,198.00 |
| Retained earnings | -A$36,481.00 | A$19,472.17 | A$160,127.65 |
| **Total equity** | **A$299,717.00** | **A$355,670.17** | **A$496,325.65** |
| **Check: assets less liabilities less equity** | ✅ A$0.00 | ✅ A$0.00 | ✅ A$0.00 |

How the 3 statements link:
- Retained earnings M6 = -A$36,481.00 + sum of M1 to M6 net after GST (A$55,953.17) = A$19,472.17.
- Retained earnings M12 = -A$36,481.00 + Year 1 net after GST (A$196,608.65) = A$160,127.65.
- Cash M12 ties to Section 4 closing cash.

---

## 6. Break-even

### 6a. AM clients/day, fixed vs variable labour

Repo method (S1 §10): PM held at its full A$24,585.37, solve for AM clients/day at the Month 5 cost base.

| Labour basis | Formula | **Break-even AM/day (repo)** | Break-even (GST-stress) | % of 18/day |
|---|---|---|---|---|
| v0.2: full roster every morning (all costs fixed) | (A$107,883.97 - A$24,585.37) ÷ A$6,582.50 | 12.655 | 14.083 | 70.3% |
| **v0.3: rostered to bookings (Section 1A)** | (A$78,993.29 - A$24,585.37) ÷ A$6,582.50 | **8.266** | **9.255** | **45.9%** |

- A$78,993.29 = fixed costs A$36,738.11 (rent, overhead, direct costs, PM labour and Venue Manager with on-costs) + one 2 + 4 roster every morning A$42,255.18 incl. on-costs. It is the repo's own LOW-segment total, and 8.266 is the repo's own LOW-segment break-even (S1 §10, S29 §5). ✅ Exact match.
- Margin of safety at 18/day: 9.734 clients/day (54.1%), up from 5.345 (29.7%).
- **Why the repo's "valley" goes away:** the repo shows 11.29 clients/day losing A$8,982/month because every morning steps up to 8 therapists (S1 §10). Under the v0.3 rule, a morning never runs at 11 to 14 on the full roster; extra clients fill whole 18-client mornings. Each extra client above 10 then adds A$250 of revenue for about A$137 of labour, so profit rises steadily from 8.266 upward.
- ⚠️ This depends on the 45-minute cadence sign-off (Section 1A) and on Grace steering bookings. Without the cadence, see Section 14.

### 6b. Two-stream break-even in visits/month (TM)

Both streams scaled together at the current capacity mix (474 AM : 210 PM per month).

| Labour basis | **Break-even visits / month** | AM / PM split | AM clients/day | % of 684 visits capacity |
|---|---|---|---|---|
| v0.2 (all costs fixed) | 515.8 | 357.4 AM + 158.5 PM | 13.57 | 75.4% |
| **v0.3 (rostered to bookings)** | **377.7** | 261.7 AM + 116.0 PM | 9.94 | 55.2% |

The 220:350 mix from the superseded v2.0 model is retired (PM capacity is now about 210/month).

### 6c. Sensitivity (steady-state cost base, headline rent)

| Scenario | Monthly net v0.3 (repo / GST-stress) | Monthly net v0.2 (repo / GST-stress) | Break-even AM/day v0.3 | v0.2 | Status |
|---|---|---|---|---|---|
| Base: 18/day, A$8k rent | A$35,186.40 / A$23,442.58 | A$35,186.40 / A$23,442.58 | 8.266 | 12.655 | 🟢 |
| Volume -20% (14.4 AM/day, PM -20%) | A$19,573.14 / A$10,430.60 | A$6,572.33 / -A$2,570.21 | 8.266 | 12.655 | 🟢 v0.3 stays clearly profitable |
| Price -10% (AM A$225, PM -10%) | A$20,879.36 / A$10,436.18 | A$20,879.36 / A$10,436.18 | 9.599 | 14.476 | 🟡 |
| Rent A$7,000 | A$36,186.40 / A$24,351.67 | A$36,186.40 / A$24,351.67 | 8.114 | 12.503 | 🟢 |
| Rent A$9,000 | A$34,186.40 / A$22,533.49 | A$34,186.40 / A$22,533.49 | 8.417 | 12.806 | 🟢 |
| Rent A$9,500 / A$10,500 / gross ceiling | see Section 9 | | 8.493 / 8.645 / 8.455 | 12.882 / 13.034 / 12.844 | 🟢 |
| 12 AM/day, PM full (TM, Table 1 rules) | A$17,359.41 / A$9,206.05 | -A$4,308.60 / -A$12,461.96 | 8.266 | 12.655 | 🟢 v0.3 |

Note: the 12/day row is this model's own figure on Table 1 rules. The repo's Table 2 (+A$1,096.40) uses a different 08:00-start schedule and is not comparable (S1 §10).

---

## 7. Payback timeline

**Definition (TM, unchanged):** the month when cumulative cash from opening day gets back to zero (pre-opening spend + ramp losses + deferred capex earned back). Months 13 onward assume steady state continues.

| Month | v0.3 cumulative (repo basis) | v0.3 cumulative (after GST) | v0.2 (repo / after GST) |
|---|---|---|---|
| M0 | -A$251,198.00 | -A$251,198.00 | -A$251,198.00 / -A$251,198.00 |
| M1 | 🔴 -A$267,771.03 (lowest) | 🔴 -A$267,771.03 (lowest) | -A$296,661.71 / -A$296,661.71 |
| M3 | -A$240,696.04 | -A$252,233.18 | -A$306,639.02 / -A$318,176.16 |
| M6 | -A$153,675.47 | -A$196,875.01 | -A$224,168.75 / -A$267,368.29 |
| M9 | -A$48,116.27 | -A$126,547.27 | -A$118,609.55 / -A$197,040.55 |
| M10 | -A$12,929.87 | -A$103,104.69 | -A$83,423.15 / -A$173,597.97 |
| **M11** | ✅ **A$22,256.53** | -A$79,662.11 | -A$48,236.75 / -A$150,155.39 |
| M13 | A$92,629.33 | -A$32,776.95 | ✅ A$22,136.05 / -A$103,270.23 |
| M14 | A$127,815.73 | -A$9,334.37 | A$57,322.45 / -A$79,827.65 |
| **M15** | A$163,002.13 | ✅ **A$14,108.21** | A$92,508.85 / -A$56,385.07 |
| M18 | A$268,561.33 | A$84,435.95 | A$198,068.05 / ✅ A$13,942.67 |

| Basis | v0.3 payback | v0.2 payback |
|---|---|---|
| Repo basis (GST-inclusive P&L) | **Month 11** | Month 13 |
| After estimated GST | **Month 15** | Month 18 |

---

## 8. Conflicts and open items

### 8a. Superseded figures (do not use)

| # | Old figure | Where | Current figure | Status |
|---|---|---|---|---|
| 1 | Revenue A$113,712.16 / costs A$88,625.09 / net +A$25,087.07 (v2.0, 10 clients/day, ancillary A$8,580 included) | S4 history, S11, S20 | A$143,070.37 / A$107,883.97 / +A$35,186.40 | ✅ RESOLVED by Anthony 2026-10-10: baseline locked to v3.0. S20 still calls v2.0 "current authoritative", which is stale |
| 2 | 220 AM : 350 PM visits/month mix | S20, original brief | about 474 AM : 210 PM per month | 🗄️ Superseded |
| 3 | Net A$63,028.75 / A$56,581.70 / A$44,166.17 (and others) | S1 strike-throughs, S21 | +A$35,186.40 | 🗄️ Superseded |
| 4 | Revenue A$154,710.69, net A$32,576.80, break-even 13.051/day, trough -A$76,532.52 | S5 (titled "Current") | See Sections 3, 4, 6 | 🗄️ Stale (2026-08-18) |
| 5 | Workbook: revenue A$155,215.80, net A$56,581.70, break-even 9.404/day | S21 | See above | 🗄️ Stale (2026-08-09) |
| 6 | Break-even 9.4/day and 9.821/day; 11.290/day | S22 dossiers | 8.266/day (v0.3); 12.655/day (full-roster basis) | 🗄️ Stale |
| 7 | Break-even "12 AM visits/day, capacity 8", Year 1 loss -A$513,540 | S20 | 8.266/day, Year 1 +A$322,015 (repo basis) | 🗄️ Not real |
| 8 | Cash trough -A$53,353.76 (Month 2) | S19 | -A$16,573.03 (Month 1, v0.3) | 🗄️ Not recomputed in repo |
| 9 | Inherited revenue A$157,792.16 | S1 §5 | A$143,070.37 canonical | 🗄️ Historical only |
| 9a | 🆕 v0.2 of this model: break-even 12.655, peak funding A$318,176, lowest cash A$18,022, payback M13 / M18, Year 1 A$251,522 | This file v0.2 | v0.3 figures in Section 1 | 🗄️ Superseded by v0.3 (2026-10-11) |
| 9b | 🆕 7-staff AM option (massage+beauty pool of 3) and 3 to 10/day tables | S30, S34, `am-staffing-by-volume.md` | 4 / 8 therapist tiers (S29) | 🗄️ Older cadences (23 and 40 minutes); S29 (2026-09-19) is current. Not used here |

### 8b. Live conflicts between documents

| # | Conflict | Figures | Impact | Owner |
|---|---|---|---|---|
| 10 | S1 §5 cost table lines do not add to its own total | 82,318.05 + 1,399.41 + 14,288.34 = A$98,005.80, but total says A$107,883.97 | Missing super line A$9,878.17 (present in S3) | Grace: add super row to S1 |
| 11 | Rent budget vs footprint | Headline keeps A$8,000 (S16). Budget A$9,500 to 10,500/month for 257 to 290 sqm | Section 9 | ✅ RESOLVED by Anthony 2026-10-10 |
| 12a | Floor area | 257 to 290 sqm with 2 blood collection rooms | Sets the search brief | ✅ RESOLVED by Anthony 2026-10-10 |
| 12b | Fit-out for the larger floor area not costed | 18 to 51 sqm extra at the repo's A$800 to 1,250/sqm = A$14,400 to 63,750 (TM, indicative). Not in any capital figure | v0.3 headroom (A$65,927 to A$68,427) now covers most of it, but that leaves little for anything else | 🔴 Still open: needs venue + builder quote |
| 13 | Construction rate vs market | Repo A$800 to 1,250/sqm not benchmarked (S23); S15 finds A$39,000 to 60,450 higher | Fit-out risk | 3 builder quotes |
| 14 | Cafe equipment not in base | A$5,000 to 12,650 (S10) | Base capex understated | Grace / founder |
| 15 | Clinical equipment two figures | A$8,300 to 14,100 vs A$6,330 to 10,240 (S10, S6) | Up to A$3,860 | Unreconciled |
| 16 | Lease cost overlap | Up to A$48,600 combined high end (S6) | Unclear | Unresolved |
| 17 | GST on the AM package | Mixed supply (S12) vs "likely fully taxable" (S11) | A$0 to about A$11,744/month | 🔴 Accountant |
| 18 | GST not in any repo P&L or cashflow | S11 | Payback M11 vs M15 (v0.3) | 🔴 Accountant |
| 19 | Working capital reserve basis | A$85,000 to 110,000 flagged stale (S19). v0.3 needs only about A$16,600 drop cover at plan, but A$85,000 buys 4 months of stall runway (Section 4b) | Keep A$85,000 | Founder |
| 20 | Startup capital: several ranges | A$251,198 base (S6) vs older ranges (S1 §7.4, S9) | Base used | After venue + quotes |
| 20a | 🆕 Phlebotomist floor | S29 says 2 phlebotomists are structural at every tier. S29's own odd-count rule lets the last pair use only Chair A, so a 1-client morning only uses one chair | Model keeps 2 on every rostered morning. A 1-phlebotomist floor on 1 to 2 client mornings would save A$234.51 a weekday morning (incl. on-costs) | 🟡 Clinical decision, not assumed |
| 20b | 🆕 Site brief says the A$10,500 ceiling is **excluding GST**; this model (like v0.2) treats the rent line as GST-inclusive and claims 1/11 back | If the landlord charges GST on top of A$10,500, cash rent is A$11,550: repo-basis net -A$1,050/month and GST-stress net -A$954.55/month vs Section 9 | Small, flagged | Grace at lease stage |

### 8c. Open items and this model's assumptions (TM)

| # | Item | Treatment here | Status |
|---|---|---|---|
| 21 | Ramp curve 43/64/79/93/100% | Used as the repo does; origin undocumented (S2) | 🟡 Assumption from repo |
| 22 | AM labour ramp | ✅ **Now modelled (v0.3):** rostered by morning to the S29 tiers. Replaces v0.2's full payroll from Month 1 (S3 `conflict_am_labor_ramp_unmodelled`) | 🟢 Closed in this model; repo YAML still flat |
| 23 | Contingency fully spent at Month 0 and capitalised | TM | 🟡 Conservative |
| 24 | Deferred capex timing (Month 4 and Month 6) | TM, from S7 §5 and S8 §4.3 | 🟡 |
| 25 | All funding is capital put in before opening, no loans | TM | 🟡 |
| 26 | GST: all sales taxable, monthly BAS paid next month | TM, from S11 and S12 | 🟠 Accountant |
| 27 | GST credits on fit-out and equipment | Not claimed | 🟢 Upside |
| 28 | Rent during fit-out (before trading) | Not in base. Each month costs A$8,000 / A$9,500 / A$10,500 | 🔴 Negotiate rent-free fit-out |
| 29 | No debtor / creditor timing | P&L net = operating cash. Clients prepay (S28) | 🟡 |
| 30 | No depreciation, income tax or interest | Entity undecided | 🟡 Accountant |
| 31 | Workers comp 1.7% | Repo placeholder rate | 🟡 |
| 32 | Saturday "experienced staff" cover | Pay loading unknown; no cost added (S1 §0) | 🟡 Founder |
| 33 | Insurance A$708.34/month | Modelled, not a quote | 🟡 |
| 34 | PM volume (10 sessions/day) and A$117 average | Founder-set planning input (S13) | 🟡 |
| 35 | Inventory held flat | Replenished via consumables line | 🟡 |
| 36 | Lab / courier fee to GTT | Repo assumes A$0. Sensitivity in Section 10 | 🔴 TO CONFIRM via tender |
| 37 | Two-tier GST invoicing (s38-10) | Proposed only (Section 11) | 🔴 Accountant |
| 38 | Contingency in rent-adjusted capital | Kept at A$26,914 | 🟡 TM |
| 39 | Rent-adjusted scenarios keep every other line at the headline | Only rent, bond and advance rent change (plus utilities / cleaning in the gross ceiling column) | 🟡 TM |
| 40 | 🆕 **45-minute pair cadence on mornings of 10 or fewer** | Used for the 2 + 4 roster. Solver-feasible inside the WDP 10:30am window but "presented, not adopted" (S29 §3) | 🔴 **Anthony sign-off needed.** Without it, Section 14 |
| 41 | 🆕 **Booking steering ("fill-to-tier")** | Grace fills each morning to 10, and opens slots 11 to 18 only when a morning can reach 15 (weekday) / 17 (Saturday). Assumes clients accept another morning inside their 24 to 28 week window | 🟠 Fresha slot-release setup + front-desk script. Fill-rate risk in Section 13 |
| 42 | 🆕 Fill rate 100% of rostered capacity in the base | Clients prepay; no-shows and late cancellations keep full payment (S28). Waitlist backfills earlier cancellations | 🟠 Sensitivity in Section 13 |
| 43 | 🆕 Casual pool availability | Phlebotomists and therapists accept variable mornings. Fewer early-month shifts may push good casuals to other work. The repo's one-pool, cross-trained hiring (S35) helps | 🟠 Recruitment risk, not costed |
| 44 | 🆕 Full 6-hour AM shifts paid on every rostered morning | Repo basis. Early release (start later / leave earlier, 3-hour floor) is a separate repo upside: A$14,167.19/month wages at 18/day (S1 §8, dated 2026-08-05, older rates), about A$16,108/month with on-costs (TM). Not in any figure here | 🟢 Upside |
| 45 | 🆕 Mornings of 1 to 5 clients | Monthly model never uses them (steering avoids them). If they happen, cost per client is high (Section 1A) | 🟡 |
| 46 | 🆕 Gross ceiling column | Assumes the A$10,500 all-in includes utilities (A$650) and cleaning (A$600). See Section 9 | 🟠 Verify against each listing's outgoings budget |

---

## 9. Rent-adjusted scenarios and gross ceiling

📌 **The headline uses A$8,000/month rent, per Anthony's instruction (2026-10-10).** The real budget is A$9,500 to A$10,500/month for 257 to 290 sqm with 2 blood collection rooms. The site brief v0.3 makes A$10,500 a **hard gross ceiling: base rent plus estimated outgoings plus car bays, excluding GST** (S36).

**Utilities / cleaning overlap: resolved assumption (TM, stated now):**
- **Gross ceiling column:** the A$10,500 all-in **includes** utilities (A$650) and cleaning (A$600), so those two lines are dropped from other overhead (A$1,250/month). Total occupancy = A$10,500.
- **Rent-adjusted A$10,500 column (kept from v0.2):** rent A$10,500 **plus** separate utilities and cleaning. Total occupancy = A$11,750. This is the prudent planning case.
- Why both are kept: in WA, landlord outgoings usually cover rates, building insurance and common-area costs. A tenant's own metered electricity and in-clinic cleaning are often **not** in outgoings (general information, verify against each listing's itemised outgoings budget). Grace should test every listing against both.

**What changes (TM):** rent every month, the lease bond (1 month's rent) and advance rent (1 month's rent); in the gross ceiling column also utilities and cleaning. Everything else is the headline. Same rostering rule, ramp, GST method and deferred capex.

| Measure | Headline A$8,000 ✅ | Rent-adjusted A$9,500 | Rent-adjusted A$10,500 | Gross ceiling A$10,500 all-in |
|---|---|---|---|---|
| Rent per month | A$8,000.00 | A$9,500.00 | A$10,500.00 | A$10,500.00 |
| Utilities + cleaning (separate) | A$1,250.00 | A$1,250.00 | A$1,250.00 | A$0.00 (inside ceiling) |
| **Total occupancy per month** | **A$9,250.00** | **A$10,750.00** | **A$11,750.00** | **A$10,500.00** |
| Lease bond / advance rent (1 month each) | A$8,000.00 each | A$9,500.00 each | A$10,500.00 each | A$10,500.00 each |
| Pre-opening capital | A$251,198.00 | A$254,198.00 | A$256,198.00 | A$256,198.00 |
| **Total startup capital** | **A$336,198.00** | **A$339,198.00** | **A$341,198.00** | **A$341,198.00** |
| Payroll Months 1 to 3 (v0.3) | A$214,843.91 | A$214,843.91 | A$214,843.91 | A$214,843.91 |
| **Net per month, Month 5 onward (repo)** | **A$35,186.40** | **A$33,686.40** | **A$32,686.40** | **A$33,936.40** |
| **Net per month, GST-stress** | **A$23,442.58** | **A$22,078.94** | **A$21,169.85** | **A$22,306.21** |
| Year 1 net, repo basis: v0.3 (v0.2) | A$322,014.93 (A$251,521.65) | A$304,014.93 (A$233,521.65) | A$292,014.93 (A$221,521.65) | A$307,014.93 (A$236,521.65) |
| Year 1 net, after GST: v0.3 (v0.2) | A$196,608.65 (A$126,115.37) | A$180,244.99 (A$109,751.71) | A$169,335.90 (A$98,842.62) | A$182,972.24 (A$112,478.96) |
| **Break-even AM/day, repo: v0.3 (v0.2)** | **8.266** (12.655) | **8.493** (12.882) | **8.645** (13.034) | **8.455** (12.844) |
| Break-even AM/day, GST-stress: v0.3 (v0.2) | 9.255 (14.083) | 9.482 (14.310) | 9.634 (14.462) | 9.444 (14.272) |
| **Peak funding, with GST: v0.3 (v0.2)** | **A$267,771.03** (A$318,176.16) | **A$272,271.03** (A$325,403.44) | **A$275,271.03** (A$330,221.62) | **A$274,021.03** (A$326,698.89) |
| Peak funding, repo basis: v0.3 (v0.2) | A$267,771.03 (A$312,280.64) | A$272,271.03 (A$318,280.64) | A$275,271.03 (A$322,280.64) | A$274,021.03 (A$319,780.64) |
| **Lowest cash = headroom: v0.3 (v0.2)** | **A$68,426.97** M1 (A$18,021.84 M3) | **A$66,926.97** M1 (A$13,794.56 M3) | **A$65,926.97** M1 (A$10,976.38 M3) | **A$67,176.97** M1 (A$14,499.11 M3) |
| Stall runway, full months: v0.3 (v0.2) | 4 (1) | 3 (1) | 3 (1) | 4 (1) |
| **Payback repo / after GST: v0.3** | **M11 / M15** | **M11 / M16** | **M12 / M17** | **M11 / M16** |
| Payback repo / after GST: v0.2 | M13 / M18 | M14 / M19 | M14 / M20 | M13 / M19 |

**Formulas (TM):**
- Net = headline net less (total occupancy less A$9,250).
- GST-stress net also gets back 1/11 of the occupancy change as a GST credit (see item 20b on GST and the ceiling).
- Break-even = (A$78,993.29 + occupancy change less PM A$24,585.37) ÷ A$6,582.50.
- Peak funding, payback and runway are re-run month by month with the Section 4 and 7 rules.

**Plain English:**
- At the ceiling, if utilities and cleaning really are inside the A$10,500, the business clears about A$33.9k a month (about A$22.3k GST-stress). If they are not, about A$32.7k (A$21.2k).
- Payback slips by about 1 month at most against the headline.
- The cash low stays above A$65k in every rent case.

---

## 10. Lab fee sensitivity: dual-lab tender

**Strategy (unchanged):** PathWest and WDP compete on courier plus lab analysis through a tender. GTT employs its own 2 phlebotomists.

**What the repo assumes: A$0 lab fee to GTT (Medicare bulk-billing by the lab)** (S11, S26, S28). Courier cost is not modelled anywhere in the repo (S26). 🔴 **Actual tender fees are TO CONFIRM.**

**Fee basis (TM):** a flat fee per AM client, A$4,739.40/month per A$10 at 473.94 clients/month, ramping with volume in Months 1 to 4. GST-stress column assumes the fee includes GST and GTT claims the credit. v0.3 rostering applies.

**At headline rent A$8,000 (startup capital A$336,198):**

| Fee per client | Monthly cost (at 18/day) | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST) | Peak funding (with GST) | Headroom in capital | Payback (repo / GST) |
|---|---|---|---|---|---|---|---|
| A$0 (repo) | A$0.00 | **A$35,186.40** | A$23,442.58 | 8.266 / 9.255 | A$267,771.03 | 🟢 A$68,426.97 | M11 / M15 |
| A$10 | A$4,739.40 | **A$30,447.00** | A$19,134.03 | 8.610 / 9.640 | A$269,808.97 | 🟢 A$66,389.03 | M12 / M18 |
| A$20 | A$9,478.80 | **A$25,707.60** | A$14,825.49 | 8.984 / 10.173 | A$274,172.29 | 🟢 A$62,025.71 | M14 / M23 |
| A$30 | A$14,218.20 | **A$20,968.20** | A$10,516.94 | 9.393 / 11.644 | A$279,058.19 | 🟢 A$57,139.81 | M17 / M31 |

**At rent-adjusted A$10,500 (startup capital A$341,198):**

| Fee per client | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST) | Peak funding (with GST) | Headroom in capital | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| A$0 | **A$32,686.40** | A$21,169.85 | 8.645 / 9.634 | A$275,271.03 | 🟢 A$65,926.97 | M12 / M17 |
| A$10 | **A$27,947.00** | A$16,861.30 | 9.006 / 10.096 | A$279,059.13 | 🟢 A$62,138.87 | M14 / M21 |
| A$20 | **A$23,207.60** | A$12,552.76 | 9.397 / 11.372 | A$283,945.01 | 🟢 A$57,252.99 | M16 / M27 |
| A$30 | **A$18,468.20** | A$8,244.21 | 9.824 / 13.018 | A$289,341.46 | 🟢 A$51,856.54 | M20 / M40 |

**At gross ceiling A$10,500 all-in (startup capital A$341,198):**

| Fee per client | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST) | Peak funding (with GST) | Headroom in capital | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| A$0 | **A$33,936.40** | A$22,306.21 | 8.455 / 9.444 | A$274,021.03 | 🟢 A$67,176.97 | M11 / M16 |
| A$10 | **A$29,197.00** | A$17,997.67 | 8.808 / 9.838 | A$276,672.77 | 🟢 A$64,525.23 | M13 / M19 |
| A$20 | **A$24,457.60** | A$13,689.12 | 9.191 / 10.772 | A$281,558.65 | 🟢 A$59,639.35 | M15 / M25 |
| A$30 | **A$19,718.20** | A$9,380.58 | 9.608 / 12.331 | A$286,444.55 | 🟢 A$54,753.45 | M18 / M35 |

**Plain English:**
- Every A$10 per client still costs about A$4,739 a month at full volume. Rostering does not change that.
- What changes: under v0.2, a fee of about A$20 or more meant the startup capital no longer covered the cash low. Under v0.3 the capital covers it even at A$30, with more than A$50k to spare.
- At A$30 the GST-stress payback stretches to 31 to 40 months, so the tender goal is unchanged: A$0 to GTT, or at most about A$10.

---

## 11. Two-tier GST invoicing (proposed, s38-10 GST Act)

> **This is general knowledge, not your personal documents. Verify before acting.**
> **Status: proposed; requires accountant advice and possibly an ATO private ruling.** Nothing here is settled tax treatment.

### 11a. The proposed structure (unchanged from v0.2)

| Invoice line | What it covers | Proposed GST |
|---|---|---|
| Clinical phlebotomy component | Blood collection by GTT's employed phlebotomist for the referred GTT test | GST-free under s38-10 **only if** every condition below is met. Unproven |
| Wellness lounge component | Treatments, lounge access, refreshments | Taxable, 10% GST |
| Pathology test itself | Lab analysis | Not GTT's supply. The lab bills Medicare (S11, S26) |

### 11b. Why this is not settled (unchanged from v0.2)

- 🔴 **Recognised professional test.** s38-10 only covers services by a recognised professional in the s38-10 table. To my knowledge, phlebotomy is not a listed profession. A collection by a registered nurse might arguably sit under nursing.
- 🔴 **"Generally accepted as necessary" test.** The service must be generally accepted in the profession as necessary for appropriate treatment.
- 🔴 **Pathology is normally the lab's Medicare service, not GTT's.** Whether a GTT-employed phlebotomist's collection is a separate supply by GTT is **not settled**.
- 🟠 **Repo conflict.** The repo says the A$250 package is 100% wellness and lounge (S24 via S11, S25). The older Xero coding (S12) assumed a mixed supply.
- 🟠 **Fair price.** Any clinical price must be a genuine, market-supportable value. Shifting price just to cut GST risks the anti-avoidance rules.
- 🟢 **GST credits are kept.** GST-free supplies do not stop GTT claiming GST credits on its costs.

### 11c. Effect on net profit

Every split is a **TM assumption**. The A$50 row is anchored to a competitor's A$50 "pathology only" price (S27, not GTT's price). GST saved = 473.94 AM clients/month x clinical amount ÷ 11. Monthly net columns are the GST-stress figures plus the GST saved (unchanged from v0.2 at steady state); break-even and payback are re-run under v0.3 rostering.

| Clinical part of each A$250 package (assumption) | Share | GST saved / month | **Net / month at A$8,000** | Net at A$9,500 | Net at A$10,500 | Net at gross ceiling | Break-even AM/day (GST, A$8,000) | Payback after GST (A$8,000) |
|---|---|---|---|---|---|---|---|---|
| A$0 (GST-stress downside) | 0% | A$0.00 | **A$23,442.58** | A$22,078.94 | A$21,169.85 | A$22,306.21 | 9.255 | M15 |
| A$25 | 10% | A$1,077.14 | **A$24,519.72** | A$23,156.08 | A$22,246.99 | A$23,383.35 | 9.163 | M14 |
| A$50 (market anchor) | 20% | A$2,154.27 | **A$25,596.85** | A$24,233.21 | A$23,324.12 | A$24,460.48 | 9.073 | M14 |
| A$75 | 30% | A$3,231.41 | **A$26,673.99** | A$25,310.35 | A$24,401.26 | A$25,537.62 | 8.985 | M13 |

Note: computing the A$50 row directly (not by adding) gives A$0.01 more in some columns, from rounding GST on sales to the cent.

**Plain English:** a two-tier invoice, if it works, adds about A$1.1k to A$3.2k a month over the GST-stress case. Worth asking the accountant. Not worth building the case on.

---

## 12. Steady state at 18 clients/day: does it change? (🆕)

**No. Month 5 onward stays at +A$35,186.40 (repo basis) and +A$23,442.58 (GST-stress).**

Why:
- At 18 clients a morning the repo solver needs **8 therapists at any cadence** inside the WDP 10:30am window, and 2 phlebotomists (S29 §2, §3). Only mornings of 10 or fewer can drop to 4 therapists.
- So when demand fills every morning, rostering to bookings rosters the full team every morning. Payroll is A$93,595.63 either way (Section 3b).
- Rostering to bookings is a **ramp-up and bad-month tool**, not a margin lever at capacity. Its value shows up in the cash low, payback, break-even and in how a weak month behaves (volume -20% now earns about A$19.6k instead of about A$6.6k, Section 6c).

Three things could still move the steady state, none counted in the headline:
- 🟢 **Early release** (staff start at their first booking and leave after their last, 3-hour floor): repo figure A$14,167.19/month wages at 18/day, about A$16,108 with on-costs (S1 §8, TM). Dated 2026-08-05, before the latest rates. Tagged upside, as in the repo.
- 🟢 **PM roles with no bookings stood down.** Not quantified (no PM service-mix data).
- 🔴 **Fill rate below 100%** at capacity lowers revenue, not labour (Section 13).

---

## 13. Waitlist value and fill-rate sensitivity (🆕)

**Repo position:** the repo plans a waitlist (100 signups by week 13, 300+ by week 18) and a 2-weeks-before-launch staffing decision from confirmed paid bookings (S32). It has **no fill-rate or conversion data**; it notes warm-waitlist conversion is "commonly 20 to 40%" but unverified for this category (S32). So the fill rates below are **explicit TM assumptions**.

**Definition (TM):** fill rate = clients actually served ÷ rostered slots. Below 100%, Grace has to roster more mornings / bigger bands to serve the same demand (labour up in the ramp), and at capacity an 18-slot morning only yields 18 x fill (revenue down).

- Prepaid bookings protect revenue: no-shows and cancellations under 24 hours keep the full fee; 24 to 48 hours keeps 50% (S28). Those slots are not lost revenue.
- The real fill risk is cancellations more than 48 hours out (credit, rebooked later) and released slots that never sell. **The waitlist's job is to backfill those slots.**

| Fill rate of rostered slots | Payroll Months 1 to 3 | Month 1 net | Max clients served at capacity | **Monthly net M5+ (repo / GST-stress)** | Year 1 net (repo) | Peak funding (with GST) | Lowest cash | Payback (repo / GST) | Break-even AM/day (repo / GST) |
|---|---|---|---|---|---|---|---|---|---|
| **100% (base)** | A$214,843.91 | -A$16,573.03 | 18.0 | **A$35,186.40 / A$23,442.58** | A$322,014.93 | A$267,771.03 | 🟢 A$68,426.97 (M1) | M11 / M15 | 8.266 / 9.255 |
| 85% | A$231,247.87 | -A$16,573.03 | 15.3 | **A$17,413.65 / A$7,285.54** | A$149,399.87 | A$271,742.13 | 🟢 A$64,455.87 (M2) | M19 / M42 | 8.266 / 11.102 |
| 70% | A$250,142.14 | -A$20,390.73 | 12.6 | **-A$359.10 / -A$8,871.51** | -A$40,112.80 | A$392,280.56 | 🔴 -A$56,082.56 (M12, still falling) | not reached | not reached within 12.6 |

**Plain English:**
- At 100% fill (the base), the waitlist does what the plan needs.
- Each 1% of fill at capacity is worth 0.18 clients a morning, about **A$1,185 a month** in revenue.
- Moving from 85% to 100% fill is worth about **A$17,773 a month** at steady state. That is the waitlist's value in money terms.
- At 70% the venue cannot pay its way even when every morning is fully rostered. If real fill tracks below about 85%, Grace should cut released slots and lean on the waitlist before adding mornings.
- Rostering to bookings does not create this risk; v0.2 at full capacity faces exactly the same revenue loss from empty slots.

---

## 14. Alternative: full mornings only (🆕, no cadence decision needed)

If Anthony does **not** sign off the 45-minute cadence, the 2 + 4 roster is not available. The fallback that keeps the committed 25-minute cadence is to run AM GTT **only on full 18-client mornings** with the 2 + 8 roster, and close AM GTT on other mornings (PM and the Venue Manager carry on).

| Measure (headline rent) | v0.3 base (fill-to-tier) | Full mornings only | v0.2 |
|---|---|---|---|
| AM GTT mornings per month, M1 / M2 / M3 / M4 | 26.33 every month | 11.32 / 16.85 / 20.80 / 24.49 | 26.33 |
| Payroll Months 1 to 3 | A$214,843.91 | A$199,680.60 | A$280,786.89 |
| Saving vs v0.2, Months 1 to 3 | A$65,942.98 | A$81,106.29 | |
| Month 1 net | -A$16,573.03 | -A$4,910.56 | -A$45,463.71 |
| Peak funding (with GST) | A$267,771.03 | A$256,108.56 | A$318,176.16 |
| Lowest cash | A$68,426.97 (M1) | A$80,089.44 (M1) | A$18,021.84 (M3) |
| Payback (repo / after GST) | M11 / M15 | M10 / M14 | M13 / M18 |
| Break-even AM/day (repo / GST) | 8.266 / 9.255 | 4.621 / 6.461 (average per trading day) | 12.655 / 14.083 |
| Monthly net M5+ | A$35,186.40 | A$35,186.40 | A$35,186.40 |

**Why it is cheaper on paper but not the base:**
- A full 18-client morning has the lowest labour per client (A$138.71 on a weekday).
- But in Month 1 AM GTT would run on only about 11 mornings a month (about 2 or 3 a week). Clients lose choice of day, and casual phlebotomists and therapists get few shifts, which risks losing them before volume arrives (item 43).
- An 18-client morning is also the most complex operation, run from opening week by a new team.
- Recommendation (TM): use the v0.3 base if the cadence is approved; use full mornings only as the fallback, or for the first 2 to 4 weeks only.

---

## 15. What changed from v0.2 (🆕)

| Item | v0.2 | v0.3 |
|---|---|---|
| AM labour | Full 8 + 2 roster every morning from Month 1 | Rostered to each morning's confirmed bookings (S29 tiers) |
| Payroll Months 1 to 3 | A$280,786.89 | A$214,843.91 (-A$65,942.98) |
| Year 1 net (repo) | A$251,521.65 | A$322,014.93 |
| Break-even (repo / GST-stress) | 12.655 / 14.083 | 8.266 / 9.255 |
| Peak funding (with GST) | A$318,176.16 | A$267,771.03 |
| Lowest cash | A$18,021.84 (M3) | A$68,426.97 (M1) |
| Payback (repo / GST) | M13 / M18 | M11 / M15 |
| Monthly net M5+ | +A$35,186.40 | +A$35,186.40 (unchanged) |
| GST-stress M5+ | +A$23,442.58 | +A$23,442.58 (unchanged) |
| Rent columns | A$8,000 / A$9,500 / A$10,500 | Same, plus gross ceiling A$10,500 all-in (utilities and cleaning inside) |
| New sections | | 1A rostering rule, 4b stall runway, 12 steady state, 13 fill rate, 14 full-mornings fallback |

### Numbers Grace must sync into the deck and tracker

| Figure | New value | Replaces |
|---|---|---|
| Monthly net, Month 5 onward (headline) | +A$35,186.40 | no change |
| GST-stress downside | +A$23,442.58 | no change |
| Break-even AM clients/day | **8.266** (GST-stress 9.255) | 12.655 (14.083) |
| Peak funding (with GST) | **A$267,771** | A$318,176 |
| Lowest cash point | **A$68,427 in Month 1** | A$18,022 in Month 3 |
| Payback (repo / after GST) | **Month 11 / Month 15** | Month 13 / Month 18 |
| Payroll Months 1 to 3 | **A$214,844** | A$280,787 |
| Year 1 net (repo / after GST) | **A$322,015 / A$196,609** | A$251,522 / A$126,115 |
| Gross ceiling A$10,500 all-in: net / GST-stress / break-even / peak / payback | **+A$33,936 / +A$22,306 / 8.455 / A$274,021 / M11 and M16** | new |
| Rent-adjusted A$10,500 (+ separate utilities and cleaning): net / break-even / peak / payback | **+A$32,686 / 8.645 / A$275,271 / M12 and M17** | +A$32,686 / 13.034 / A$330,222 / M14 and M20 |
| Startup capital | A$336,198 (A$341,198 at A$10,500) | no change |
| Caveat to carry on every slide using the new break-even | "Needs the 45-minute cadence for mornings of 10 or fewer and booking steering. Without the cadence: full-mornings fallback, Section 14." | new |

---

*Arithmetic: every table above was regenerated and re-summed with a script (row sums, column totals, cashflow roll-forward and balance sheet checks all tie to the cent; v0.2 figures reproduced exactly as a control). Repo source files were read only. Nothing on the server was edited.*
