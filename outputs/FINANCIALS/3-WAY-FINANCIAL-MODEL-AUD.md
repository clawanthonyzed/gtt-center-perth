# GTT Center Perth: 3-Way Financial Model (AUD)

**Prepared by:** Theodore (CFO consultant) for Grace (GTT Center Perth manager). Rebuilt to v0.5 on 2026-10-16 by Grace (workstream M) to Anthony's instructions of 2026-10-16; updated to v0.6 on 2026-10-17 (workstream M2) for the adaptive phlebotomist roster and the 10% post-test discount.
**Version:** v0.6 (2026-10-17). 25-minute pair cadence only, adaptive rostering of phlebotomists and therapists, full capacity from Month 1 (no ramp-up). The steady state at 18 clients a morning is unchanged at +A$35,186.40; break-even is now 7.250.
**Date:** 2026-10-17
**Repo snapshot:** clawanthonyzed/gtt-center-perth; calculators re-run on 2026-10-16 (tools/am_volume_tier_staffing_solver.py, tools/cost_ramp_model.py, tools/am_demand_tier_financial_ladder.py) re-run on 2026-10-17 with the phlebotomist count taken from the solver's draw check; workings in docs/overhaul-2026-10-17/M-model/
**Currency:** every figure is in Australian dollars (A$). No foreign amounts are used.

> **Read this first**
> - 🆕 **What v0.6 changes (Anthony, 2026-10-17):** (1) phlebotomists are on the adaptive roster: 1 phlebotomist when 9 or fewer clients are booked, 2 when 10 to 18, none in the afternoon, with a named second collector on call on light mornings; (2) the 10% post-test discount is adopted for any expecting mother who completes a GTT test, on standalone treatments or packages, morning or afternoon (Section 8b item 20c). Break-even falls from 8.266 to **7.250**; steady state, Year 1, GST-stress, peak funding and payback at 18 a morning are unchanged because both chairs run.
> - 🆕 **What v0.5 changed (Anthony, 2026-10-16):** (1) the 25-minute pair cadence is the only cadence: first booking 07:00, pairs at 07:00, 07:25, 07:50 and so on, last first draw 10:20, 9 pairs, 18 clients a morning at most, booked 2 to 4 weeks ahead; (2) staff are called in to match the confirmed slots, AM and PM, and idle staff are never rostered; (3) there is no ramp-up: the plan opens at the full 18 clients a morning, filled through marketing and a pre-launch waitlist; (4) the afternoon is made of stand-alone pre-booked services, with walk-ins only if staff are free.
> - 📌 **Baseline kept:** 18 AM clients/day at capacity, 07:00 start (CURRENT-STATE §0 and §5). Prices, rent and overheads are unchanged. Month 5 onward net is still **+A$35,186.40** and the GST-stress case **+A$23,442.58**.
> - 🔁 **What the no-ramp decision does:** Year 1 is now 12 full months: net **A$422,236.80** (earlier ramped figure A$322,014.93), GST-stress **A$281,310.96** (earlier A$196,608.65). Peak funding falls to the pre-opening capital, **A$251,198** (earlier A$267,771), and payback is **Month 8 / Month 11** (earlier Month 11 / Month 15). All of this assumes the waitlist delivers 18 clients on day one.
> - ⚖️ **Break-even:** **7.250** AM clients a day (40.3% of 18; was 8.266 with 2 phlebotomists on every morning), planning case, 25-minute cadence. It rests on bookings landing one per slot; if every booking stacks in pairs from 07:00 both chairs run and it is 12.655 (Section 6).
> - 🏠 **Rent:** the headline still uses **A$8,000/month, per Anthony's instruction.** Rent-adjusted A$9,500 and A$10,500 columns sit beside it, plus the gross ceiling column (A$10,500 all-in per the site brief v0.3). Section 9 states the utilities / cleaning assumption.
> - ✅ **Decided (Anthony, 2026-10-17):** phlebotomists are rostered adaptively. Dependency still open: the pathology partner and the Medicare and lab-employment rules may require the lab to supply collectors, in which case the roster is the lab's decision (Decision Log 2026-10-17).
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
| S37 | 🆕 [docs/overhaul-2026-10-16/M-model/MODEL-WORKINGS.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/overhaul-2026-10-16/M-model/MODEL-WORKINGS.md) (2026-10-16 roster, break-even, Year 1 and GST workings, with the calculator runs) |
| **TM** | **This model's own assumption or arithmetic.** Always listed in Section 8. |
---

## 1. Key numbers card

v0.5 figures. The earlier ramped (v0.4) figure is shown in brackets where it changed.

| | Headline (A$8,000 rent) ✅ | Rent-adjusted A$9,500 | Rent-adjusted A$10,500 | Gross ceiling A$10,500 all-in | Status |
|---|---|---|---|---|---|
| 💰 **Total startup capital** | **A$336,198** | A$339,198 | A$341,198 | A$341,198 | 🟡 Unchanged (S1 §6, S6, S8) |
| 👥 **Payroll, Months 1 to 3** | **A$280,787** (v0.4 A$214,844) | same | same | same | Full roster from Month 1, no ramp |
| 📈 **Monthly net, every month from Month 1 (repo basis)** | **+A$35,186.40** | +A$33,686.40 | +A$32,686.40 | +A$33,936.40 | 🟢 Full roster needed at 18/day (Section 12) |
| 🧾 **GST-stress downside** | **+A$23,442.58** | +A$22,078.94 | +A$21,169.85 | +A$22,306.21 | 🟠 TM, accountant to confirm |
| ⚖️ **Break-even, AM clients/day (repo basis)** | **7.250** (was 8.266) | 7.478 | 7.630 | 7.440 | 🟢 Planning case, 25-minute cadence, adaptive phlebotomists (Section 6) |
| ⚖️ Break-even, AM clients/day (GST-stress, bookings spaced) | 8.138 (was 9.255) | 8.366 | 8.518 | 8.328 | 🟠 TM |
| 🏦 **Peak funding** (with GST timing) | **A$251,198** (v0.4 A$267,771) | A$254,198 (A$272,271) | A$256,198 (A$275,271) | A$256,198 (A$274,021) | Equals the pre-opening capital: no operating loss to fund |
| ⚠️ **Lowest cash point** | **A$85,000, at opening** (v0.4 A$68,427, Month 1) | A$85,000 | A$85,000 | A$85,000 | 🟢 The reserve is never drawn |
| 🛟 Runway if fill falls to 70% from Month 1 | **9 full months** | 7 | 7 | 7 | Months the A$85,000 reserve lasts (Section 4b) |
| ⏱️ **Payback** (repo basis / after GST) | **Month 8 / Month 11** (v0.4 M11 / M15) | M8 / M12 | M9 / M13 | M8 / M12 | 🟢 Sections 7 and 9 |
| 📅 Year 1 net (repo basis / after GST) | **A$422,236.80 / A$281,310.96** (v0.4 A$322,015 / A$196,609) | A$404,236.80 / A$264,947.28 | A$392,236.80 / A$254,038.20 | A$407,236.80 / A$267,674.52 | 🟢 12 full-capacity months |
| 🧪 Lab / courier fee to GTT | A$0 per client (repo assumption) | | | | 🟠 Tender fees TO CONFIRM. Each A$10/client costs about A$4,739/month at capacity (Section 10) |
| 🧾 GST-free value of the package | A$107.71 a month for each percentage point of the A$250 package that is GST-free (at 18/day) | | | | 🔴 Proposed only (Section 11) |

**Plain English:**
- Removing the ramp-up does not change what the business earns once full. It removes the slow first four months, so Year 1 is 12 times the steady-state month, the first month already makes a profit, and the money needed to open is just the pre-opening capital.
- That is only true if the pre-launch waitlist and marketing deliver a full morning on day one. At 85% fill the steady-state profit is about +A$17.4k a month; at 70% the venue roughly breaks even and does not repay the capital (Section 13).
- Rostering to bookings still matters: on a lighter morning the roster shrinks with the bookings (Section 1A) instead of paying for a full team.

---

## 1A. Adaptive rostering rule (v0.5)

### 1A-i. What can flex and what stays fixed

| Role / cost | v0.5 treatment | Why | Source |
|---|---|---|---|
| Phlebotomists (casual, employed in-house; employer to be confirmed, see Decision Log 2026-10-17) | **Variable by morning (Anthony, 2026-10-17).** 1 phlebotomist when 1 to 9 clients are booked and no two share a slot; 2 phlebotomists when 10 to 18 are booked; none in the afternoon. A named second collector is on call on mornings of 9 or fewer, paid only if called in (assumed) | One chair carries up to 9 clients on the 25-minute cadence because the three draws of each client never overlap (solver draw check = 1); from the tenth booking two clients share a slot and two draws fall together (check = 2). The fixed minimum of 2 (2026-10-11) is retired | S29, tools/am_volume_tier_staffing_solver.py, gtt-clinical-protocol §Difficult Venepuncture |
| AM therapists (massage + beauty pool, nails, hair; casual) | **Variable by morning:** set by how many 45-minute services overlap at the busiest moment of the confirmed bookings (2 to 8 therapists, table below) | Repo solver run on the 25-minute cadence with the actual slot pattern | S29 §2, S31 |
| PM therapists (4 roles, casual) | Rostered to pre-booked stand-alone services only; each role is paid the 3-hour minimum engagement on a trading day. Walk-ins are accepted only if staff are free | Already priced at the legal floor at every PM level. A PM role with no bookings could be stood down, but there is no per-role PM booking mix, so no saving is counted (upside) | S31 `compute_pm_weekday_daily_labor`, S4 §2 |
| Venue Manager (Mon to Fri, A$320/day) | **Fixed** A$7,040/month | Safety-critical, must be on site every operating day (first aid, fire warden, clinical escalation) | S30 §1, S1 §0 item 2 |
| Reception | **Fixed, no separate line.** AM reception is the Venue Manager's role; PM reception is covered by rostered PM staff | | S31, S1 §4 |
| Saturday Venue Manager cover | An experienced staff member already rostered that day. No loading costed | Pay loading still open | S1 §0 item 2 |
| Rent, insurance, software, accounting, laundry, utilities, cleaning, misc, marketing, supplies | **Fixed** | | S3, S5 §4 |

**Wage rates (all from the repo, none invented):** massage / beauty A$37.50/hr, nails and hair A$36.81/hr, phlebotomist A$34.375/hr (SS Level 1-2 midpoint), Venue Manager A$40.00/hr. These are the award **casual** rates, so the 25% casual loading is already inside them. Saturday = 1.5 times the casual rate. Super 12% and workers comp 1.7% on every wage line. Shifts are paid as the full 6-hour 07:00 to 13:00 AM window, the repo's conservative basis. Early release (start later, leave earlier, 3-hour minimum) is a separate upside, not counted.

> General information, verify with Fair Work: casual minimum engagement, Saturday penalty rates for casuals, notice for roster changes, and casual conversion rights.

### 1A-ii. The rostering rule table (one morning, 25-minute cadence)

Labour cost per morning, wages only for the AM clinical and treatment roster, including super 12% and workers comp 1.7%. The Venue Manager is fixed and not in these figures. **Planning case:** bookings fill from the 07:00 slot onward, one client per slot first (Chair A), and a second client (Chair B) only after every slot has one. The real roster is set each week by running the confirmed slot list through the solver; the columns on the right show the best and worst possible patterns.

| Confirmed bookings that morning | Phlebotomists | Therapists (Massage and Beauty / Nails / Hair) | Last first draw | Weekday labour | Saturday labour | Labour per client (weekday) | Therapists if bookings are spaced (best) | Therapists if bookings stack in pairs (worst) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | n/a | A$0.00 | A$0.00 | n/a | 0 | 0 |
| 1 | 1 | 1 / 1 / 0 = 2 | 07:00 | A$741.45 | A$1,112.17 | A$741.45 | 2 | 2 |
| 2 | 1 | 2 / 2 / 0 = 4 | 07:25 | A$1,248.39 | A$1,872.59 | A$624.20 | 2 | 4 |
| 3 | 1 | 2 / 2 / 0 = 4 | 07:50 | A$1,248.39 | A$1,872.59 | A$416.13 | 2 | 6 |
| 4 | 1 | 2 / 2 / 0 = 4 | 08:15 | A$1,248.39 | A$1,872.59 | A$312.10 | 2 | 8 |
| 5 | 1 | 2 / 2 / 0 = 4 | 08:40 | A$1,248.39 | A$1,872.59 | A$249.68 | 2 | 8 |
| 6 | 1 | 2 / 2 / 0 = 4 | 09:05 | A$1,248.39 | A$1,872.59 | A$208.07 | 4 | 8 |
| 7 | 1 | 2 / 2 / 0 = 4 | 09:30 | A$1,248.39 | A$1,872.59 | A$178.34 | 4 | 8 |
| 8 | 1 | 2 / 2 / 0 = 4 | 09:55 | A$1,248.39 | A$1,872.59 | A$156.05 | 4 | 8 |
| 9 | 1 | 2 / 2 / 0 = 4 | 10:20 | A$1,248.39 | A$1,872.59 | A$138.71 | 4 | 8 |
| 10 | 2 | 3 / 2 / 1 = 6 | 10:20 | A$1,989.84 | A$2,984.76 | A$198.98 | 4 | 8 |
| 11 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$226.98 | 6 | 8 |
| 12 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$208.07 | 6 | 8 |
| 13 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$192.06 | 6 | 8 |
| 14 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$178.34 | 6 | 8 |
| 15 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$166.45 | 8 | 8 |
| 16 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$156.05 | 8 | 8 |
| 17 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$146.87 | 8 | 8 |
| 18 | 2 | 4 / 2 / 2 = 8 | 10:20 | A$2,496.78 | A$3,745.18 | A$138.71 | 8 | 8 |

**Why the roster is what it is (S10b).** The number of therapists is the number of 45-minute services that overlap at the busiest moment, not the number of clients. Pairs are 25 minutes apart, so two neighbouring slots overlap; with one client per slot at most two first services (massage or beauty) and two second services (nails or hair) run together, which is 4 therapists for any morning of 2 to 9 clients. Once a morning passes 10 clients the second chair is working in neighbouring slots, and 11 or more clients put four first services in the room at once, which is the full 4 + 2 + 2 = 8. So at about 12.6 booked clients (12 or 13 on a real morning) the roster is **8 therapists in the planning case and 2 phlebotomists** (1 phlebotomist up to 9 clients); if the second-chair bookings happen to sit in alternate slots it is 6. Eight is never a standard: a morning of 1 client rosters 1 phlebotomist and 2 therapists, 2 to 9 clients roster 1 phlebotomist and 4 therapists.

**Phlebotomist rule (decided by Anthony 2026-10-17; Section 8b item 20a).** With one chair in use (mornings of up to 9 clients, no two in a slot) the three draws per client never overlap, so one phlebotomist is rostered. Against the earlier fixed 2 this saves A$234.51 on a weekday morning, A$351.76 on a Saturday morning and **A$6,682.23 a month** whenever 9 or fewer are booked; break-even falls from 8.266 to 7.250. From 10 clients both chairs run and 2 are needed. A second collector is on call on light mornings (difficult draw, fainting) and is paid only if called in: one call-in at the 3-hour casual minimum costs A$117.25 on a weekday and A$175.88 on a Saturday; even one call-in every trading day adds only 0.463 to break-even. A paid standby allowance is not in the repo and is not modelled (TO CONFIRM). Options for a guaranteed second collector: a 3-hour second shift on every light morning (A$3,341.13 a month, break-even 7.758) or a second collector on Saturdays only (A$1,523.12 a month, break-even 7.482). Workings: `docs/overhaul-2026-10-17/M-model/R1-ADAPTIVE-PHLEBOTOMY.md`.

**How the roster is made.** Clients pay in full when they book; bookings open 2 to 4 weeks ahead; the roster is published 1 to 2 weeks ahead from the confirmed calendar (S28, S32 "Staffing Decision Point"). The waitlist (100 signups by week 13, 300+ by week 18, S32) and the service-interest checkboxes let the therapist mix follow what clients booked.

### 1A-iii. How the monthly model applies the rule

There is no ramp-up, so every month is a full-capacity month: 18 clients a morning, the full roster (2 phlebotomists + 8 therapists) every trading morning, weekdays (22 a month) and Saturdays (4.33 a month, at the Saturday rate). The adaptive rule matters on any morning that is not full (Sections 6 and 13).

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

## 3. 12-month P&L by month (Table 1, committed model, adaptive rostering, no ramp-up)

**No ramp-up.** The plan opens at the full 18 clients a morning, filled through marketing and a pre-launch waitlist. Every month is therefore a Month 5 month of the earlier model. Marketing is the steady A$1,500 from Month 1 (the earlier A$600 / 800 / 1,000 / 1,200 ramp is dropped). The pre-launch waitlist work is inside the launch marketing in the startup costs (Section 2).

**Line definitions:**
- AM GTT = 18 clients/day x A$250 x 26.33 trading days (S1 §5).
- PM standalone = 10 sessions/day, about 210 transactions/month at A$117 average (S13).
- Ancillary (cafe / retail) = A$0, excluded by founder decision (S1, S4).
- Direct costs = GTT supplies A$400 + consumables A$800 (S5 §4, S3).
- Payroll = AM rostered wages (Section 1A) + PM wages A$12,704.74 + Venue Manager A$7,040.00 + super 12% + workers comp 1.7% (S31).
- Rent = A$8,000 (founder decision 2026-10-03, S16).
- Other overhead = utilities, insurance, laundry, marketing, software, cleaning, accounting, misc (S5 §4, S3).

| Month | Ramp | AM clients/day | AM GTT | PM standalone | **Total revenue** | Direct costs | Payroll | Rent | Other overhead | **Total costs** | **Net** | Cumulative net |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$35,186.40 |
| M2 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$70,372.80 |
| M3 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$105,559.20 |
| M4 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$140,745.60 |
| M5 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$175,932.00 |
| M6 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$211,118.40 |
| M7 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$246,304.80 |
| M8 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$281,491.20 |
| M9 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$316,677.60 |
| M10 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$351,864.00 |
| M11 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$387,050.40 |
| M12 | 100% | 18.00 | A$118,485.00 | A$24,585.37 | **A$143,070.37** | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | **A$107,883.97** | 🟢 A$35,186.40 | A$422,236.80 |
| **Year 1** | | | **A$1,421,820.00** | **A$295,024.44** | **A$1,716,844.44** | **A$14,400.00** | **A$1,123,147.56** | **A$96,000.00** | **A$61,060.08** | **A$1,294,607.64** | **A$422,236.80** | |

### 3a. Labour build: no ramp-up vs the earlier ramped model

| Month | AM clients/day | AM rostered wages | PM + Venue Manager wages (fixed) | Super 12% + workers comp 1.7% | **Payroll v0.5** | Payroll v0.4 (ramped) | Difference |
|---|---|---|---|---|---|---|---|
| M1 | 18.00 | A$62,573.31 | A$19,744.74 | A$11,277.58 | **A$93,595.63** | A$64,704.95 | +A$28,890.68 |
| M2 | 18.00 | A$62,573.31 | A$19,744.74 | A$11,277.58 | **A$93,595.63** | A$70,194.19 | +A$23,401.44 |
| M3 | 18.00 | A$62,573.31 | A$19,744.74 | A$11,277.58 | **A$93,595.63** | A$79,944.77 | +A$13,650.86 |
| M4 | 18.00 | A$62,573.31 | A$19,744.74 | A$11,277.58 | **A$93,595.63** | A$89,045.33 | +A$4,550.30 |
| M5 to M12 (each) | 18.00 | A$62,573.31 | A$19,744.74 | A$11,277.58 | **A$93,595.63** | A$93,595.63 | A$0.00 |
| **Year 1** | | A$750,879.72 | A$236,936.88 | A$135,330.96 | **A$1,123,147.56** | A$1,052,654.28 | +A$70,493.28 |

**Plain English:** with no ramp-up there are no light early months to save wages in, so payroll is the full A$93,595.63 from Month 1. That extra wage bill (A$70,493.28 over Year 1) is far smaller than the extra revenue from running full mornings straight away (A$173,115.15 more revenue over Year 1).

### 3b. Steady-state payroll breakdown (every month from Month 1, S3 `cost_table1_m5plus`)

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

The repo's P&L figures are **GST-inclusive** and have **no line for GST paid to the ATO** (S11). Method: all revenue taxable at 10%; credits on rent, consumables and other overhead; GTT supplies GST-free (S12); wages and super carry no GST. Revenue and non-wage costs are the same in every month.

| Month | GST on sales (rev ÷ 11) | GST credits | **Net GST owed** | **Net after GST** |
|---|---|---|---|---|
| M1 to M12 (each) | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| **Year 1** | **A$156,076.80** | **A$15,150.96** | **A$140,925.84** | **A$281,310.96** |

🟠 If the A$250 package price includes GST, about A$22.73 of each package belongs to the ATO. That cuts steady-state net from A$35,186 to about A$23,443. Year 1 on that basis is A$281,310.96. (The earlier ramped Year 1 on this basis was A$196,608.65.)

Not modelled: income tax (entity undecided), depreciation (the repo P&L has none), interest (no debt assumed).

---

## 4. Cashflow by month

**Rules used (unchanged):**
- Opening funding = base startup capital A$336,198 (Section 2), all received before opening (TM, no debt assumed).
- Pre-opening capital A$251,198 is spent in Month 0, including the full contingency (TM, conservative).
- Operating cash = monthly P&L net. No debtor or creditor timing (S11, S21). Clients prepay at booking (S28).
- GST: monthly BAS, paid the month after (S12).
- Deferred capex per Section 2d (Month 4 A$5,600, Month 6 A$7,774).

| Month | Opening cash | Funding in | CapEx out | Operating cash | GST paid (BAS) | **Closing cash** |
|---|---|---|---|---|---|---|
| M0 (pre-opening) | A$0.00 | A$336,198.00 | -A$251,198.00 | A$0.00 | A$0.00 | ⚠️ **A$85,000.00** (lowest) |
| M1 | A$85,000.00 | A$0.00 | A$0.00 | A$35,186.40 | A$0.00 | **A$120,186.40** |
| M2 | A$120,186.40 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$143,628.98** |
| M3 | A$143,628.98 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$167,071.56** |
| M4 | A$167,071.56 | A$0.00 | -A$5,600.00 | A$35,186.40 | -A$11,743.82 | **A$184,914.14** |
| M5 | A$184,914.14 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$208,356.72** |
| M6 | A$208,356.72 | A$0.00 | -A$7,774.00 | A$35,186.40 | -A$11,743.82 | **A$224,025.30** |
| M7 | A$224,025.30 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$247,467.88** |
| M8 | A$247,467.88 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$270,910.46** |
| M9 | A$270,910.46 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$294,353.04** |
| M10 | A$294,353.04 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$317,795.62** |
| M11 | A$317,795.62 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$341,238.20** |
| M12 | A$341,238.20 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$364,680.78** |

### 4a. Peak funding requirement

| Measure | v0.5 (no ramp-up) | v0.4 (ramped) | v0.2 | Note |
|---|---|---|---|---|
| Pre-opening capital spent (Month 0) | A$251,198.00 | A$251,198.00 | A$251,198.00 | S8 |
| Deepest drop after opening, with GST | A$0.00 (cash rises from Month 1) | A$16,573.03 (Month 1) | A$66,978.16 (Month 3) | Reserve A$85,000 less lowest cash |
| **Peak funding requirement (with GST timing)** | **A$251,198.00** | A$267,771.03 | A$318,176.16 | Capital less lowest cash |
| Peak funding requirement (repo basis, no GST) | A$251,198.00 | A$267,771.03 | A$312,280.64 | Both bases match: the low is at opening |
| **Headroom inside A$336,198 base** | **A$85,000.00** | A$68,426.97 | A$18,021.84 | 🟢 Covers the uncosted floor-area fit-out (item 12b, up to A$63,750) with room to spare |

🟢 v0.5 does **not** cut the startup capital. The extra headroom is needed for the open fit-out items in Section 8 and for the fill-rate risk below.
🟢 Unspent contingency (up to A$26,914) and GST credits on fit-out would add further headroom (not counted, TM).
🔴 Rent during the fit-out period is still not in the base budget (item 28).

### 4b. Runway if fill falls (TM)

Test: from Month 1 only 70% of the rostered slots fill (12.6 clients a morning, roster 2 + 8) and stay there. How many full months does the A$85,000 reserve last? GST paid the month after.

| | Net after GST per month | Full months covered | Cash goes negative in |
|---|---|---|---|
| **v0.5 headline** | -A$8,871.51 | **9** | Month 10 |
| v0.5 at A$9,500 / A$10,500 / gross ceiling | | 7 / 7 / 7 | Month 8 / 8 / 8 |

**Plain English:** with no ramp-up the reserve is untouched while the waitlist works. If fill is poor the reserve gives about 9 months to fix marketing and referral flow before more money is needed.

---

## 5. Balance sheet snapshots (simple)

**Method (TM, unchanged):** fit-out, design and approvals, contingency, furniture and equipment are capitalised. Advance rent, legal fees, IT setup, pre-opening wages, launch marketing and professional fees (A$36,481 total) are expensed before opening. Assets at cost, no depreciation. Retained earnings use **net after GST** (Section 3d).

| Line | Opening day (end M0) | Month 6 | Month 12 |
|---|---|---|---|
| Cash | A$85,000.00 | A$224,025.30 | A$364,680.78 |
| Fit-out, furniture, equipment (at cost) | A$204,132.00 | A$217,506.00 | A$217,506.00 |
| Opening stock | A$2,585.00 | A$2,585.00 | A$2,585.00 |
| Lease bond | A$8,000.00 | A$8,000.00 | A$8,000.00 |
| **Total assets** | **A$299,717.00** | **A$452,116.30** | **A$592,771.78** |
| GST payable to ATO | A$0.00 | A$11,743.82 | A$11,743.82 |
| **Total liabilities** | **A$0.00** | **A$11,743.82** | **A$11,743.82** |
| Capital contributed | A$336,198.00 | A$336,198.00 | A$336,198.00 |
| Retained earnings | -A$36,481.00 | A$104,174.48 | A$244,829.96 |
| **Total equity** | **A$299,717.00** | **A$440,372.48** | **A$581,027.96** |
| **Check: assets less liabilities less equity** | ✅ A$0.00 | ✅ A$0.00 | ✅ A$0.00 |

How the 3 statements link:
- Retained earnings M6 = -A$36,481.00 + sum of M1 to M6 net after GST (A$140,655.48) = A$104,174.48.
- Retained earnings M12 = -A$36,481.00 + Year 1 net after GST (A$281,310.96) = A$244,829.96.
- Cash M12 ties to Section 4 closing cash.

---

## 6. Break-even

### 6a. AM clients/day, adaptive rostering on the 25-minute cadence

Method (S1 §10): PM held at its full A$24,585.37, solve for AM clients/day at the cost base of the roster the bookings need.

| Step | Working | Result |
|---|---|---|
| 1. Fixed costs per month | Rent, other overhead, cost of goods, PM labour and Venue Manager with on-costs | A$36,738.11 |
| 2. AM roster for a morning of up to 9 clients booked one per slot | 1 phlebotomist + 4 therapists, with on-costs, 22 weekdays + 4.33 Saturdays (was 2 + 4 at A$42,255.18) | + A$35,572.95 |
| 3. Total costs at that roster | (was A$78,993.29) | **A$72,311.06** |
| 4. Less PM revenue | PM services at full steady state | - A$24,585.37 |
| 5. Costs AM GTT must cover | (was A$54,407.92) | **A$47,725.69** |
| 6. Revenue per daily AM client per month | A$250 x 26.33 trading days | **A$6,582.50** |
| 7. **Break-even** | A$47,725.69 ÷ A$6,582.50 | **7.250 AM clients/day** |

7.250 is 40.3% of the 18-client capacity, a margin of safety of 10.750 clients/day (59.7%). Before the adaptive phlebotomist rule it was 8.266 (45.9%, margin 9.734). The tier for 8 booked clients is the right one: the roster for 7 clients is the same 1 phlebotomist + 4 therapists, so the answer is stable inside the tier.

**Break-even depends on where bookings land in the slots**

| Booking pattern (roster that results) | Break-even AM/day (repo) | Break-even AM/day (GST-stress) | % of 18/day |
|---|---|---|---|
| Bookings spaced across the slots (1 phlebotomist + 4 therapists up to 9 clients) | **7.250** (was 8.266) | 8.138 (was 9.255) | 40.3% |
| **Planning case:** one client per slot from 07:00 (1 + 4 up to 9 clients, then 2 + 6, then 2 + 8) | **7.250** (was 8.266) | 8.138 (was 14.083) | 40.3% |
| Bookings stack in pairs from 07:00 (repo solver as published; 2 + 8 from 4 clients) | 12.655 | 14.083 | 70.3% |
| Planning case with a paid 3-hour second phlebotomist shift on every light morning | 7.758 | 8.696 | 43.1% |
| Planning case with a second collector every Saturday | 7.482 | 8.392 | 41.6% |

- **Headline: 7.250.** Bookings that stack in pairs put both chairs to work from the second booking, so the 2 + 8 roster and 12.655 return. The GST-stress figure of 8.138 holds as long as bookings stay one per slot.
- **Why the repo's "valley" is still there:** at 10 to 12 clients the planning-case roster steps up to 6 and then 8 therapists before the revenue catches up (net -A$3,028.26 at 10 clients, -A$10,891.10 at 11, -A$4,308.60 at 12, against +A$4,834.58 at 9). 9 booked earns +A$11,516.81 under the adaptive rule, more than any of 10 to 14 booked; a morning is again better than 9 from 15 clients upward (+A$15,438.90). With no ramp-up and a waitlist the aim is 18 every morning, so the valley is a risk to watch, not a plan.
- Fill is assumed 100% (Section 13).

### 6b. Two-stream break-even in visits/month (TM)

Both streams scaled together at the current capacity mix (474 AM : 210 PM per month), spaced-booking roster.

| Labour basis | **Break-even visits / month** | AM / PM split | AM clients/day | % of 684 visits capacity |
|---|---|---|---|---|
| Full roster every morning (all costs fixed) | 515.8 | 357.4 AM + 158.5 PM | 13.57 | 75.4% |
| **Adaptive rostering (1 phlebotomist + 4 therapists, spaced bookings; was 2 + 4: 377.7 visits, 9.94 AM/day, 55.2%)** | **345.7** | 239.6 AM + 106.1 PM | 9.10 | 50.5% |

### 6c. Sensitivity (steady-state cost base, headline rent)

| Scenario | Monthly net (repo / GST-stress) | Break-even AM/day (repo) | Status |
|---|---|---|---|
| Base: 18/day, A$8k rent | A$35,186.40 / A$23,442.58 | 7.250 | 🟢 |
| Volume -20% (14.4 AM/day, PM -20%) | A$6,572.33 / -A$2,570.22 | 7.997 | 🟡 still profitable |
| Price -10% (AM A$225, PM -10%) | A$20,879.36 / A$10,436.18 | 8.471 | 🟡 |
| Rent A$7,000 | A$36,186.40 / A$24,351.67 | 7.098 | 🟢 |
| Rent A$9,000 | A$34,186.40 / A$22,533.49 | 7.402 | 🟢 |
| 12 AM/day, PM full (TM, Table 1 rules) | -A$4,308.60 / -A$12,461.96 | 7.250 | 🔴 loss |
| Rent A$9,500 / A$10,500 / gross ceiling | see Section 9 | 7.478 / 7.630 / 7.440 | 🟢 |

Note: the 12/day row is this model's own figure on Table 1 rules. The repo's Table 2 (+A$1,096.40) uses a different 08:00-start schedule and is not comparable (S1 §10).

---

## 7. Payback timeline

**Definition (TM, unchanged):** the month when cumulative cash from opening day gets back to zero (pre-opening spend + deferred capex earned back). Steady state continues.

| Month | v0.5 cumulative (repo basis) | v0.5 cumulative (after GST) | v0.4 (repo / after GST) |
|---|---|---|---|
| M0 | -A$251,198.00 | -A$251,198.00 | -A$251,198.00 / -A$251,198.00 |
| M1 | -A$216,011.60 | -A$216,011.60 | -A$267,771.03 / -A$267,771.03 |
| M3 | -A$145,638.80 | -A$169,126.44 | -A$240,696.04 / -A$252,233.18 |
| M6 | -A$53,453.60 | -A$112,172.70 | -A$153,675.47 / -A$196,875.01 |
| M7 | -A$18,267.20 | -A$88,730.12 |  |
| M8 (payback, repo) | A$16,919.20 ✅ | -A$65,287.54 |  |
| M9 | A$52,105.60 | -A$41,844.96 | -A$48,116.27 / -A$126,547.27 |
| M10 | A$87,292.00 | -A$18,402.38 | -A$12,929.87 / -A$103,104.69 |
| M11 (payback, after GST) | A$122,478.40 | A$5,040.20 ✅ | A$22,256.53 / -A$79,662.11 |
| M12 | A$157,664.80 | A$28,482.78 | A$57,442.93 / -A$56,219.53 |

| Basis | v0.5 payback | v0.4 payback | v0.2 payback |
|---|---|---|---|
| Repo basis (GST-inclusive P&L) | **Month 8** | Month 11 | Month 13 |
| After estimated GST | **Month 11** | Month 15 | Month 18 |

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
| 6 | Break-even 9.4/day and 9.821/day; 11.290/day | S22 dossiers | 7.250/day; 12.655/day (full-roster basis) | 🗄️ Stale |
| 7 | Break-even "12 AM visits/day, capacity 8", Year 1 loss -A$513,540 | S20 | 7.250/day, Year 1 +A$422,237 (repo basis) | 🗄️ Not real |
| 8 | Cash trough -A$53,353.76 (Month 2) | S19 | no cash trough: lowest cash A$85,000 at opening | 🗄️ Not recomputed in repo |
| 9 | Inherited revenue A$157,792.16 | S1 §5 | A$143,070.37 canonical | 🗄️ Historical only |
| 9a | v0.2 of this model: break-even 12.655, peak funding A$318,176, lowest cash A$18,022, payback M13 / M18, Year 1 A$251,522 | This file v0.2 | current figures in Section 1 | 🗄️ Superseded |
| 9c | 🆕 v0.3 and v0.4 of this model: Year 1 A$322,015 / A$196,609, peak funding A$267,771, lowest cash A$68,427, payback M11 / M15, Months 1 to 4 ramped at 43 / 64 / 79 / 93% | This file v0.3, v0.4 | Year 1 A$422,236.80 / A$281,310.96, peak funding A$251,198, lowest cash A$85,000, payback M8 / M11 | 🗄️ Superseded 2026-10-16 (ramp-up removed by decision) |
| 9b | 7-staff AM option (massage+beauty pool of 3) and 3 to 10/day tables | S30, S34, `am-staffing-by-volume.md` | Roster table, Section 1A (25-minute cadence) | 🗄️ Older cadences (23 and 40 minutes). Not used here |

### 8b. Live conflicts between documents

| # | Conflict | Figures | Impact | Owner |
|---|---|---|---|---|
| 10 | S1 §5 cost table lines do not add to its own total | 82,318.05 + 1,399.41 + 14,288.34 = A$98,005.80, but total says A$107,883.97 | Missing super line A$9,878.17 (present in S3) | Grace: add super row to S1 |
| 11 | Rent budget vs footprint | Headline keeps A$8,000 (S16). Budget A$9,500 to 10,500/month for 257 to 290 sqm | Section 9 | ✅ RESOLVED by Anthony 2026-10-10 |
| 12a | Floor area | 257 to 290 sqm with 2 blood collection rooms | Sets the search brief | ✅ RESOLVED by Anthony 2026-10-10 |
| 12b | Fit-out for the larger floor area not costed | 18 to 51 sqm extra at the repo's A$800 to 1,250/sqm = A$14,400 to 63,750 (TM, indicative). Not in any capital figure | the A$85,000 headroom now covers most of it, but that leaves little for anything else | 🔴 Still open: needs venue + builder quote |
| 13 | Construction rate vs market | Repo A$800 to 1,250/sqm not benchmarked (S23); S15 finds A$39,000 to 60,450 higher | Fit-out risk | 3 builder quotes |
| 14 | Cafe equipment not in base | A$5,000 to 12,650 (S10) | Base capex understated | Grace / founder |
| 15 | Clinical equipment two figures | A$8,300 to 14,100 vs A$6,330 to 10,240 (S10, S6) | Up to A$3,860 | Unreconciled |
| 16 | Lease cost overlap | Up to A$48,600 combined high end (S6) | Unclear | Unresolved |
| 17 | GST on the AM package | Mixed supply (S12) vs "likely fully taxable" (S11) | A$0 to about A$11,744/month | 🔴 Accountant |
| 18 | GST not in any repo P&L or cashflow | S11 | Payback M8 vs M11 | 🔴 Accountant |
| 19 | Working capital reserve basis | A$85,000 to 110,000 flagged stale (S19). with no ramp-up the plan never draws the reserve, and A$85,000 buys about 9 months of runway if fill falls to 70% (Section 4b) | Keep A$85,000 | Founder |
| 20 | Startup capital: several ranges | A$251,198 base (S6) vs older ranges (S1 §7.4, S9) | Base used | After venue + quotes |
| 20a | ✅ Phlebotomist rule | **Decided by Anthony 2026-10-17: phlebotomists are on the adaptive roster.** 1 phlebotomist on mornings of 9 or fewer (no two clients in a slot), 2 from 10 booked, none in the afternoon; a named second collector is on call on light mornings. The earlier fixed minimum of 2 was GTT's own clinical standard (2026-10-11), not a regulation found in the repo. Saves A$6,682.23 a month on light mornings and lowers break-even to 7.250 | 🟡 Conditions: difficult-draw cover (maximum 2 attempts, then the on-call collector, otherwise reschedule or refer back), fainting protocol and a vasovagal recovery chair; Saturday has no Venue Manager, so a second collector every Saturday is recommended until first-aid cover is confirmed (A$1,523.12 a month, not in the headline). **The pathology partner and the Medicare and lab-employment rules may require the lab to supply collectors; if so the roster is the lab's decision** |
| 20c | 🆕 10% post-test discount | **Adopted by Anthony 2026-10-17.** Any expecting mother who completes a GTT test can redeem 10% off standalone wellness treatments or multi-service packages, morning or afternoon (valid immediately). Cost is not deducted from any figure in this model: at A$117 a booking, 25% take-up costs A$1,386.27 a month (3.9% of monthly profit; break-even 7.250 to 7.461), 10% take-up A$554.51. It pays for itself if 10% of redeemers are new bookings (idle therapist time) or 24.2% (extra hours must be paid). Terms (exclusions, stacking, one use per test, 14-day expiry) are proposals awaiting sign-off | 🟡 Take-up and new-booking share are assumptions. Workings: `docs/overhaul-2026-10-17/M-model/R2-POST-TEST-DISCOUNT.md` |
| 20b | 🆕 Site brief says the A$10,500 ceiling is **excluding GST**; this model (like v0.2) treats the rent line as GST-inclusive and claims 1/11 back | If the landlord charges GST on top of A$10,500, cash rent is A$11,550: repo-basis net -A$1,050/month and GST-stress net -A$954.55/month vs Section 9 | Small, flagged | Grace at lease stage |

### 8c. Open items and this model's assumptions (TM)

| # | Item | Treatment here | Status |
|---|---|---|---|
| 21 | Ramp curve 43/64/79/93/100% | **Removed by decision (2026-10-16).** The plan opens at 18 a morning via marketing and a pre-launch waitlist | ✅ Closed. Fill rate is now the central risk (Section 13) |
| 22 | AM labour ramp | Not needed: full roster from Month 1. Rostering to confirmed bookings (Section 1A) applies to any morning that is not full | 🟢 Closed |
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
| 40 | 🆕 **Cadence** | **25-minute pair cadence only** (first booking 07:00, last first draw 10:20, 18 clients a morning at most). Retired permanently by Anthony 2026-10-16: no other cadence is used anywhere | ✅ Decided |
| 41 | 🆕 **Slot offering** | All slots are offered; clients choose, booking 2 to 4 weeks ahead. The roster follows the confirmed pattern. The break-even of 7.250 assumes bookings fall one per slot; stacking in pairs from 07:00 raises it to 12.655 (Section 6) | 🟠 Watch the booking pattern in Fresha |
| 42 | 🆕 Fill rate 100% of rostered capacity from Month 1 | No ramp-up. Clients prepay; no-shows and late cancellations keep full payment (S28). The waitlist backfills cancellations | 🔴 Central risk, sensitivity in Section 13 |
| 43 | 🆕 Casual pool availability | Phlebotomists and therapists are called in to match the confirmed slots. The pool on the books is sized for the busiest morning plus absences (12 AM therapists, 4 phlebotomists, 4 PM therapists, 1 Venue Manager) | 🟠 Recruitment risk, not costed |
| 44 | 🆕 Full 6-hour AM shifts paid on every rostered morning | Repo basis. Early release (start later / leave earlier, 3-hour floor) is a separate repo upside: A$14,167.19/month wages at 18/day (S1 §8, dated 2026-08-05, older rates), about A$16,108/month with on-costs (TM). Not in any figure here | 🟢 Upside |
| 45 | 🆕 Mornings of 1 to 9 clients | If they happen, labour per client is high (Section 1A): for example 9 clients cost A$164.77 a client in labour on a weekday, against A$138.71 at 18 | 🟡 |
| 46 | 🆕 Gross ceiling column | Assumes the A$10,500 all-in includes utilities (A$650) and cleaning (A$600). See Section 9 | 🟠 Verify against each listing's outgoings budget |

---

## 9. Rent-adjusted scenarios and gross ceiling

📌 **The headline uses A$8,000/month rent, per Anthony's instruction (2026-10-10).** The real budget is A$9,500 to A$10,500/month for 257 to 290 sqm with 2 blood collection rooms. The site brief v0.3 makes A$10,500 a **hard gross ceiling: base rent plus estimated outgoings plus car bays, excluding GST** (S36).

**Utilities / cleaning overlap: resolved assumption (TM, stated now):**
- **Gross ceiling column:** the A$10,500 all-in **includes** utilities (A$650) and cleaning (A$600), so those two lines are dropped from other overhead (A$1,250/month). Total occupancy = A$10,500.
- **Rent-adjusted A$10,500 column:** rent A$10,500 **plus** separate utilities and cleaning. Total occupancy = A$11,750. This is the prudent planning case.
- Why both are kept: in WA, landlord outgoings usually cover rates, building insurance and common-area costs. A tenant's own metered electricity and in-clinic cleaning are often **not** in outgoings (general information, verify against each listing's itemised outgoings budget). Grace should test every listing against both.

**What changes (TM):** rent every month, the lease bond (1 month's rent) and advance rent (1 month's rent); in the gross ceiling column also utilities and cleaning. Everything else is the headline. Same adaptive rostering, no ramp-up, GST method and deferred capex.

| Measure | Headline A$8,000 ✅ | Rent-adjusted A$9,500 | Rent-adjusted A$10,500 | Gross ceiling A$10,500 all-in |
|---|---|---|---|---|
| Rent per month | A$8,000.00 | A$9,500.00 | A$10,500.00 | A$10,500.00 |
| Utilities + cleaning (separate) | A$1,250.00 | A$1,250.00 | A$1,250.00 | A$0.00 (inside ceiling) |
| **Total occupancy per month** | **A$9,250.00** | **A$10,750.00** | **A$11,750.00** | **A$10,500.00** |
| Lease bond / advance rent (1 month each) | A$8,000.00 each | A$9,500.00 each | A$10,500.00 each | A$10,500.00 each |
| Pre-opening capital | A$251,198.00 | A$254,198.00 | A$256,198.00 | A$256,198.00 |
| **Total startup capital** | **A$336,198.00** | **A$339,198.00** | **A$341,198.00** | **A$341,198.00** |
| Payroll Months 1 to 3 | A$280,786.89 | A$280,786.89 | A$280,786.89 | A$280,786.89 |
| **Net per month, every month (repo)** | **A$35,186.40** | **A$33,686.40** | **A$32,686.40** | **A$33,936.40** |
| **Net per month, GST-stress** | **A$23,442.58** | **A$22,078.94** | **A$21,169.85** | **A$22,306.21** |
| Year 1 net, repo basis: v0.5 (v0.4 ramped) | A$422,236.80 (A$322,014.93) | A$404,236.80 (A$304,014.93) | A$392,236.80 (A$292,014.93) | A$407,236.80 (A$307,014.93) |
| Year 1 net, after GST: v0.5 (v0.4 ramped) | A$281,310.96 (A$196,608.65) | A$264,947.28 (A$180,244.99) | A$254,038.20 (A$169,335.90) | A$267,674.52 (A$182,972.24) |
| **Break-even AM/day, repo (spaced bookings)** | **7.250** | **7.478** | **7.630** | **7.440** |
| Break-even AM/day, GST-stress (spaced bookings) | 8.138 | 8.366 | 8.518 | 8.328 |
| **Peak funding, with GST: v0.5 (v0.4)** | **A$251,198.00** (A$267,771.03) | **A$254,198.00** (A$272,271.03) | **A$256,198.00** (A$275,271.03) | **A$256,198.00** (A$274,021.03) |
| **Lowest cash = headroom** | **A$85,000.00** (opening) | **A$85,000.00** | **A$85,000.00** | **A$85,000.00** |
| Fill-down runway, full months (70% fill) | 9 | 7 | 7 | 7 |
| **Payback repo / after GST: v0.5** | **M8 / M11** | **M8 / M12** | **M9 / M13** | **M8 / M12** |
| Payback repo / after GST: v0.4 (ramped) | M11 / M15 | M11 / M16 | M12 / M17 | M11 / M16 |

**Formulas (TM):**
- Net = headline net less (total occupancy less A$9,250).
- GST-stress net also gets back 1/11 of the occupancy change as a GST credit (see item 20b on GST and the ceiling).
- Break-even = (A$72,311.06 + occupancy change less PM A$24,585.37) ÷ A$6,582.50.
- Peak funding, payback and runway are re-run month by month with the Section 4 and 7 rules.

**Plain English:**
- At the ceiling, if utilities and cleaning really are inside the A$10,500, the business clears about A$33.9k a month (about A$22.3k GST-stress). If they are not, about A$32.7k (A$21.2k).
- Payback slips by about 1 month at most against the headline.
- The A$85,000 reserve is untouched in every rent case.

---

## 10. Lab fee sensitivity: dual-lab tender

**Strategy (unchanged):** PathWest and WDP compete on courier plus lab analysis through a tender. GTT employs its own phlebotomists.

**What the repo assumes: A$0 lab fee to GTT (Medicare bulk-billing by the lab)** (S11, S26, S28). Courier cost is not modelled anywhere in the repo (S26). 🔴 **Actual tender fees are TO CONFIRM.**

**Fee basis (TM):** a flat fee per AM client, A$4,739.40/month per A$10 at 473.94 clients/month (18 a day, full from Month 1). GST-stress column assumes the fee includes GST and GTT claims the credit. Peak funding stays at the pre-opening capital and the reserve stays untouched in every fee case, because there is no ramp loss.

**At headline rent A$8,000 (startup capital A$336,198; peak funding A$251,198):**

| Fee per client | Monthly cost (at 18/day) | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST, spaced) | Year 1 net (repo) | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| A$0 (repo) | A$0.00 | **A$35,186.40** | A$23,442.58 | 7.250 / 8.138 | A$422,236.80 | M8 / M11 |
| A$10 | A$4,739.40 | **A$30,447.00** | A$19,134.03 | 7.552 / 8.477 | A$365,364.00 | M9 / M14 |
| A$20 | A$9,478.80 | **A$25,707.60** | A$14,825.49 | 7.881 / 8.846 | A$308,491.20 | M11 / M18 |
| A$30 | A$14,218.20 | **A$20,968.20** | A$10,516.94 | 8.239 / 13.260 | A$251,618.40 | M13 / M25 |

**At rent-adjusted A$10,500 (startup capital A$341,198; peak funding A$256,198):**

| Fee per client | Monthly cost (at 18/day) | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST, spaced) | Year 1 net (repo) | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| A$0 (repo) | A$0.00 | **A$32,686.40** | A$21,169.85 | 7.630 / 8.518 | A$392,236.80 | M9 / M13 |
| A$10 | A$4,739.40 | **A$27,947.00** | A$16,861.30 | 7.948 / 8.873 | A$335,364.00 | M10 / M16 |
| A$20 | A$9,478.80 | **A$23,207.60** | A$12,552.76 | 8.294 / 13.096 | A$278,491.20 | M12 / M21 |
| A$30 | A$14,218.20 | **A$18,468.20** | A$8,244.21 | 8.671 / 13.691 | A$221,618.40 | M15 / M32 |

**At gross ceiling A$10,500 all-in (startup capital A$341,198; peak funding A$256,198):**

| Fee per client | Monthly cost (at 18/day) | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST, spaced) | Year 1 net (repo) | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| A$0 (repo) | A$0.00 | **A$33,936.40** | A$22,306.21 | 7.440 / 8.328 | A$407,236.80 | M8 / M12 |
| A$10 | A$4,739.40 | **A$29,197.00** | A$17,997.67 | 7.750 / 8.675 | A$350,364.00 | M10 / M15 |
| A$20 | A$9,478.80 | **A$24,457.60** | A$13,689.12 | 8.087 / 12.890 | A$293,491.20 | M12 / M19 |
| A$30 | A$14,218.20 | **A$19,718.20** | A$9,380.58 | 8.455 / 13.476 | A$236,618.40 | M14 / M28 |

**Plain English:**
- Every A$10 per client still costs about A$4,739 a month at full volume.
- Break-even above 9 clients assumes the next bookings land in spaced slots; otherwise the roster steps up (Section 6).
- At A$30 the after-GST payback does not arrive inside 72 months, so the tender goal is unchanged: A$0 to GTT, or at most about A$10.

---

## 11. Two-tier GST invoicing (proposed, s38-10 GST Act)

> **This is general knowledge, not your personal documents. Verify before acting.**
> **Status: proposed; requires accountant advice and possibly an ATO private ruling.** Nothing here is settled tax treatment.

### 11a. What the base case assumes, and what the proposal changes

| Case | What it assumes about GST | Net / month at 18 a day |
|---|---|---|
| **Base case (repo basis)** | The P&L is GST-inclusive and has **no GST line**. In effect the whole package is treated as if no GST is paid out of it, and no GST credits on costs are claimed | +A$35,186.40 |
| **GST-stress** | The whole A$250 package (and PM services) is taxable at 10% and the price includes GST. GST on sales A$13,006.40, credits A$1,262.58 | +A$23,442.58 |
| **Proposed two-tier invoice** | A clinical phlebotomy component is GST-free under s38-10 (if every condition is met); the wellness lounge component stays taxable at 10% | Between the two, depending on the clinical share |

| Invoice line | What it covers | Proposed GST |
|---|---|---|
| Clinical phlebotomy component | Blood collection by GTT's employed phlebotomist for the referred GTT test | GST-free under s38-10 **only if** every condition below is met. Unproven |
| Wellness lounge component | Treatments, lounge access, refreshments | Taxable, 10% GST |
| Pathology test itself | Lab analysis | Not GTT's supply. The lab bills Medicare (S11, S26) |

**What each percentage point is worth (the number the tax workstream can price its split with).** At 18 clients a morning there are 473.94 AM clients a month (18 x 26.33). GST saved = 473.94 x clinical amount ÷ 11.

| Unit | GST saved per month | Per year |
|---|---|---|
| Each A$1 of the A$250 package that is GST-free | A$43.09 | A$517.03 |
| **Each 1 percentage point (A$2.50) of the package that is GST-free** | **A$107.71** | **A$1,292.56** |
| 10 percentage points (A$25) | A$1,077.14 | A$12,925.64 |
| 20 percentage points (A$50) | A$2,154.27 | A$25,851.24 |
| 100% of the AM package GST-free (ceiling for this lever) | A$10,771.36 | A$129,256.32 |

The PM services (A$24,585.37 a month, GST A$2,235.04) are taxable stand-alone services and are not part of the split. If the whole AM package were GST-free, net would be about A$34,214 a month, still A$972 below the headline because the headline claims no GST at all.

### 11b. Why this is not settled

- 🔴 **Recognised professional test.** s38-10 only covers services by a recognised professional in the s38-10 table. To my knowledge, phlebotomy is not a listed profession. A collection by a registered nurse might arguably sit under nursing.
- 🔴 **"Generally accepted as necessary" test.** The service must be generally accepted in the profession as necessary for appropriate treatment.
- 🔴 **Pathology is normally the lab's Medicare service, not GTT's.** Whether a GTT-employed phlebotomist's collection is a separate supply by GTT is **not settled**.
- 🟠 **Repo conflict.** The repo says the A$250 package is 100% wellness and lounge (S24 via S11, S25). The older Xero coding (S12) assumed a mixed supply.
- 🟠 **Fair price.** Any clinical price must be a genuine, market-supportable value. Shifting price just to cut GST risks the anti-avoidance rules.
- 🟢 **GST credits are kept.** GST-free supplies do not stop GTT claiming GST credits on its costs.

### 11c. Effect on net profit

Every split is a **TM assumption**. The A$50 row is anchored to a competitor's A$50 "pathology only" price (S27, not GTT's price). Monthly net columns are the GST-stress figures plus the GST saved; break-even and payback are re-run under v0.5.

| Clinical part of each A$250 package (assumption) | Share | GST saved / month | **Net / month at A$8,000** | Net at A$9,500 | Net at A$10,500 | Net at gross ceiling | Break-even AM/day (GST, A$8,000, spaced) | Payback after GST (A$8,000) |
|---|---|---|---|---|---|---|---|---|
| A$0 (GST-stress downside) | 0% | A$0.00 | **A$23,442.58** | A$22,078.94 | A$21,169.85 | A$22,306.21 | 8.138 | M11 |
| A$25 | 10% | A$1,077.14 | **A$24,519.72** | A$23,156.08 | A$22,246.99 | A$23,383.35 | 8.057 | M11 |
| A$50 (market anchor) | 20% | A$2,154.27 | **A$25,596.85** | A$24,233.21 | A$23,324.12 | A$24,460.48 | 7.978 | M10 |
| A$75 | 30% | A$3,231.41 | **A$26,673.99** | A$25,310.35 | A$24,401.26 | A$25,537.62 | 7.901 | M10 |

Note: computing the A$50 row directly (not by adding) can give A$0.01 more in some columns, from rounding GST on sales to the cent.

**Plain English:** a two-tier invoice, if it works, adds about A$1.1k to A$3.2k a month over the GST-stress case. Worth asking the accountant. Not worth building the case on.

---

## 12. Steady state at 18 clients/day

**Month 1 onward stays at +A$35,186.40 (repo basis) and +A$23,442.58 (GST-stress).** Annual: A$422,236.80 (repo basis) and A$281,310.96 (GST-stress). Net margin: 35,186.40 ÷ 143,070.37 = 24.6%.

Why:
- At 18 clients a morning the repo solver needs **8 therapists whatever the booking pattern**, and 2 phlebotomists (both chairs run; S29 §2). Payroll is A$93,595.63 (Section 3b).
- Rostering to bookings, phlebotomists included, is a lever on any morning that is not full; at capacity every role is rostered, so the adaptive phlebotomist rule changes none of the steady-state figures.

Three things could still move the steady state, none counted in the headline:
- 🟢 **Early release** (staff start at their first booking and leave after their last, 3-hour floor): repo figure A$14,167.19/month wages at 18/day, about A$16,108 with on-costs (S1 §8, TM). Dated 2026-08-05, before the latest rates. Tagged upside.
- 🟢 **PM roles with no bookings stood down.** Not quantified (no PM service-mix data).
- 🔴 **Fill rate below 100%** at capacity lowers revenue, not labour (Section 13).

---

## 13. Waitlist value and fill-rate sensitivity

**Repo position:** the repo plans a waitlist (100 signups by week 13, 300+ by week 18) and a staffing decision from confirmed paid bookings (S32). It has **no fill-rate or conversion data**; it notes warm-waitlist conversion is "commonly 20 to 40%" but unverified for this category (S32). So the fill rates below are **explicit TM assumptions**. With no ramp-up this is the central risk of the plan.

**Definition (TM):** fill rate = clients actually served ÷ rostered slots, from Month 1. The roster follows the bookings (Section 1A); at 85% and 70% the morning is still a 16-slot and 13-slot roster of 2 + 8 (both chairs run, so the adaptive phlebotomist rule does not change those two rows; averages hide quiet days under 10, which do better under the rule).

- Prepaid bookings protect revenue: no-shows and cancellations under 24 hours keep the full fee; 24 to 48 hours keeps 50% (S28). The waitlist's job is to backfill released slots.

| Fill rate of rostered slots | Clients served a morning | **Monthly net (repo / GST-stress)** | Year 1 net (repo) | Peak funding (with GST) | Lowest cash | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| **100% (base)** | 18.0 | **A$35,186.40 / A$23,442.58** | A$422,236.80 | A$251,198.00 | 🟢 A$85,000.00 (opening) | M8 / M11 |
| 85% | 15.3 | **A$17,413.65 / A$7,285.54** | A$208,963.80 | A$251,198.00 | 🟢 A$85,000.00 (opening) | M16 / M35 |
| 70% | 12.6 | **-A$359.10 / -A$8,871.51** | -A$4,309.20 | A$468,975.83 at Month 24, still rising | 🔴 -A$132,777.83 (Month 24, still falling) | not reached |
| 50% (v0.6; 9 a morning, 1 phlebotomist) | 9.0 | **A$11,516.81 / A$5,158.67** (was A$4,834.58 / -A$1,523.56 with 2 phlebotomists) | A$138,201.72 (was A$58,014.96) | A$251,198.00 | 🟢 A$85,000.00 (opening) | M23 / M51 (was M55 / not reached) |

**Plain English:**
- At 100% fill (the base), the waitlist does what the plan needs.
- Each 1% of fill at capacity is worth 0.18 clients a morning, about **A$1,185 a month** in revenue.
- Moving from 85% to 100% fill is worth about **A$17,773 a month** at steady state. That is the waitlist's value in money terms.
- At 70% the venue cannot pay its way even when every morning is fully rostered. If real fill tracks below about 85%, Grace should lean on the waitlist and marketing before adding mornings.

---

## 14. (Removed in v0.5)

The earlier contingency for a slower cadence no longer applies. With the 25-minute cadence as the only cadence, every morning is offered at full capacity and rostered to the confirmed bookings (Section 1A).

---

## 15. What changed from v0.4 to v0.5 (2026-10-16)

| Item | v0.4 | v0.5 |
|---|---|---|
| Cadence | Two cadences, one for quiet mornings | **25-minute pair cadence only** (first booking 07:00, last first draw 10:20) |
| Rostering | Two fixed rosters by volume band | Roster follows the confirmed slot pattern (Section 1A) |
| Ramp-up | Months 1 to 4 at 43 / 64 / 79 / 93% | **None.** 18 clients a morning from Month 1 via marketing and a pre-launch waitlist |
| Year 1 net (repo / after GST) | A$322,014.93 / A$196,608.65 | **A$422,236.80 / A$281,310.96** |
| Break-even (repo) | 8.266 | **8.266** (re-derived on the 25-minute cadence; 12.655 if bookings stack in pairs) |
| Peak funding (with GST) | A$267,771.03 | **A$251,198.00** |
| Lowest cash | A$68,426.97 (Month 1) | **A$85,000.00 (opening)** |
| Payback (repo / GST) | M11 / M15 | **M8 / M11** |
| Payroll Months 1 to 3 | A$214,843.91 | A$280,786.89 |
| Monthly net M1 onward | +A$35,186.40 (from Month 5) | +A$35,186.40 |
| GST-stress M1 onward | +A$23,442.58 (from Month 5) | +A$23,442.58 |
| Section 14 (slower-cadence contingency) | Present | Removed |

### Numbers to sync into the deck and tracker

| Figure | New value | Replaces |
|---|---|---|
| Monthly net (headline) | +A$35,186.40 | no change |
| Annual steady state | A$422,236.80 | no change |
| Net margin | 24.6% | no change |
| GST-stress downside | +A$23,442.58 a month; A$281,310.96 a year | Year 1 A$196,609 |
| Break-even AM clients/day | **7.250** (v0.6: adaptive phlebotomists; was 8.266 in v0.5) | tied to the retired cadence |
| Year 1 net (repo / after GST) | **A$422,237 / A$281,311** | A$322,015 / A$196,609 |
| Peak funding (with GST) | **A$251,198** | A$267,771 |
| Payback (repo / after GST) | **Month 8 / Month 11** | Month 11 / Month 15 |
| Gross ceiling A$10,500 all-in: net / GST-stress / break-even / peak / payback | **+A$33,936 / +A$22,306 / 7.440 / A$256,198 / M8 and M12** | +A$33,936 / +A$22,306 / 8.455 / A$274,021 / M11 and M16 |
| Rent-adjusted A$10,500 (+ separate utilities and cleaning) | **+A$32,686 / 7.630 / A$256,198 / M9 and M13** | +A$32,686 / 8.645 / A$275,271 / M12 and M17 |
| Startup capital | A$336,198 (A$341,198 at A$10,500) | no change |
| Caveat to carry on every slide using these numbers | "Fill assumed 100% from Month 1 through marketing and a pre-launch waitlist: 85% is about +A$17.4k a month, 70% is a loss." | |

---

## 15b. What changed from v0.5 to v0.6 (2026-10-17)

| Item | v0.5 | v0.6 |
|---|---|---|
| Phlebotomists | 2 on every morning with a booking | **1 up to 9 booked, 2 from 10, none in the afternoon**; named second collector on call |
| Break-even (repo / GST-stress) | 8.266 / 9.255 | **7.250 / 8.138** |
| Margin of safety at 18 | 9.734 clients (54.1%) | **10.750 clients (59.7%)** |
| Morning labour per month, 1 to 9 booked | A$42,255.18 (4 therapists + 2 phlebotomists) | **A$35,572.95** |
| Net at 9 booked a morning | +A$4,834.58 a month | **+A$11,516.81** |
| Saturday contribution at 9 booked | +A$25.65 | **+A$377.41** |
| Saturday proof at 18 | +A$754.82 | +A$754.82 (unchanged) |
| Steady state, Year 1, GST-stress, peak funding, payback | A$35,186.40; A$422,236.80; A$281,310.96; A$251,198; M8 / M11 | unchanged |
| Headcount on the books | 21 (4 phlebotomists) | 21 (4 phlebotomists; peak need still 2) |
| 10% post-test discount | proposal, afternoon only | **adopted, morning or afternoon**; cost A$277 to A$2,218 a month at 5% to 40% take-up; not deducted from the headline |

---

## 16. Flags for Anthony

1. **Phlebotomists are adaptive (your decision, 2026-10-17).** The pathology partner and the Medicare and lab-employment rules may require the lab to supply collectors; if so the roster is the lab's decision. Ask the partner whether one collector per chair meets its collection-site conditions, and confirm Saturday first-aid cover (no Venue Manager on Saturdays).
2. **Break-even depends on booking pattern.** 7.250 assumes bookings fall one per slot. If every booking stacks in pairs from 07:00 it is 12.655.
3. **No ramp-up is a demand assumption.** Year 1 of A$422,237 requires 18 clients on day one. At 85% fill Year 1 is A$208,964; at 70% it is a loss.
4. **Marketing.** The model uses the steady A$1,500 a month from Month 1. The pre-launch waitlist build sits in the launch marketing already in the startup costs.
5. **Phlebotomist employment type.** The job posting offers permanent part-time 25 hours a week; an adaptive roster gives each of 4 phlebotomists about 9 to 18 hours a week. Casual or a guaranteed minimum roster: TO CONFIRM.
6. **10% post-test discount terms.** Adopted in principle; the exclusions, stacking (it replaces the 10% pre-booking discount), one use per test and 14-day expiry are proposals for your sign-off.

---

*Arithmetic: every table above was regenerated and re-summed with a script (row sums, column totals, cashflow roll-forward and balance sheet checks all tie to the cent). The roll-forward rules were first run on the earlier ramped inputs and reproduced the earlier peak funding (A$267,771.03), payback (M11 / M15) and Year 1 (A$322,014.93) exactly, and the steady-state month reproduces the repo's A$107,883.97 cost and A$35,186.40 net exactly. Repo source files were read only.*

---

## Founder Rules, 2026-10-25 (inputs decided, not yet modelled)

**Founder Rule, 2026-10-25 (Anthony's 24 founder interview answers).** Source: docs/overhaul-2026-10-19/L13-r18/FOUNDER-INTERVIEW-LOCKED.md. Tag: `[DECIDED, Anthony, 2026-10-25]`. Added on top. No existing calculator number, table figure or model output in this file was changed.

1. **Package contents.** Package 1 includes 2 services of 30 minutes each. Package 2 includes 2 services of up to 45 minutes each (1 x 30 + 1 x 45, 2 x 30, or 2 x 45). Services fit between draws and never interrupt a draw; draws happen at fixed times. Both packages include lounge access and approved beverages during the draw. _Note: Matches the repo's existing package shapes; the R17 conflict ('Package 1 = one service') is closed._
2. **Package prices.** Package 1 is A$300. Package 2 is A$350. _Note: The A$250 and A$300 figures in the repo (CURRENT-STATE section 2) are the OLD price set. Model outputs were NOT recomputed._
3. **GST.** GST is inside the price (A$300 and A$350 are GST-inclusive). _Note: Not in the repo before this lock as a package rule._
4. **Planning mix.** Plan on 100 percent of clients taking Package 1. _Note: Same idea as the repo's conservative Package 1 standing instruction, now at A$300._
6. **Lab payment split.** Lab payment is split online if possible. Backup: the client pays the lab directly through a link. _Note: Consistent with Option Y (lab money does not sit in GTT). Mechanism is a Theodore R18 design item; no fee figures invented._
7. **Interest on prepaid money.** GTT earns interest on prepaid package money. _Note: No interest rate or balance is in the repo, so no interest income is modelled. Only GTT's own package money; the lab portion must not be held (Option Y). Theodore and Catherine to confirm._
9. **Tax flags.** Keep tax flags only on the three big ones: tax consolidation, GST group, lab money. _Note: Other tax flags are dropped from the model's open-item lists._
12. **Midwives.** 2 permanent part-time midwives plus 1 casual for leave. They work a fortnightly block: one works Monday to Wednesday and the other Thursday to Saturday for the fortnight, then they swap (or swap Wednesday for Saturday). To be discussed with the staff when hiring. _Note: Supersedes the R17 alternating-day grid. Costing in ROSTER-R18.md. Casual cost: not in repo._
23. **Refund cap.** ANSWER PENDING Theodore R18. Anthony is unsure whether the cap applies to GTT refunds or to Medicare refunds. Not decided; no figure invented. _Note: Open._
24. **Payroll tax.** Payroll tax is a new cost and Anthony accepts it. _Note: Theodore's R17 approximation was about A$632.14 a month on the new wages; not in the repo net._

**Model status (read this):** the tables in this file still use Package 1 at A$250 and Package 2 at A$300 and the R17 steady-state figures. Answers 2, 3, 4, 12 and 24 change the inputs (A$300 GST-inclusive Package 1 at 100 percent, two part-time midwives, payroll tax). The repo calculators were not re-run in this lock-in. The re-run is a Theodore R18 task using the repo's own tools (tools/cost_ramp_model.py and the AM solvers). Until then, treat the figures above this section as the previous price set.
