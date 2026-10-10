# GTT Center Perth: 3-Way Financial Model (AUD)

**Prepared by:** Theodore (CFO consultant) for Grace (GTT Center Perth manager)
**Version:** v0.2, 2026-10-10, dual-lab + rent update
**Date:** 2026-10-10
**Repo snapshot:** clawanthonyzed/gtt-center-perth, commit `14b747d` (v0.1), re-checked at `d96215a` for v0.2 (read-only)
**Currency:** every figure is in Australian dollars (A$). No foreign amounts are used.

> **Read this first**
> - 📌 **Baseline used:** the v3.0 committed model, locked as the headline by Anthony on 2026-10-10. That is Table 1: 18 AM clients/day, 07:00 start, founder decision round 2026-09-19 ([CURRENT-STATE.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/CURRENT-STATE.md) §0 and §5).
> - 🏠 **Rent:** the headline uses **A$8,000/month, per Anthony's instruction.** His real rent budget is **A$9,500 to A$10,500/month** for 257 to 290 sqm with 2 blood collection rooms. Rent-adjusted figures sit right beside the headline in the key numbers card and in full in Section 9.
> - 🧪 **New in v0.2:** rent-adjusted scenarios (Section 9), lab fee sensitivity for the PathWest / WDP tender (Section 10), proposed two-tier GST invoicing (Section 11).
> - 🗄️ The older v2.0 baseline (A$113,712.16 revenue / A$88,625.09 costs / +A$25,087.07 net, 10 clients/day, ancillary included) is **superseded**. It is listed in Section 8 only.
> - 🧮 Nothing here is real trading data. No venue is open yet. Every figure is a planning estimate.
> - 🧾 Tax and GST content is **general information only**. Verify with the accountant before acting.
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
| S28 | [docs/onboarding.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/onboarding.md) |
| **TM** | **This model's own assumption or arithmetic.** Always listed in Section 8. |

---

## 1. Key numbers card

| | Headline (A$8,000 rent) ✅ | Rent-adjusted A$9,500 | Rent-adjusted A$10,500 | Status |
|---|---|---|---|---|
| 💰 **Total startup capital** | **A$336,198** | A$339,198 | A$341,198 | 🟡 Headline is the founder-approved "in principle" figure, not quotes (S1 §6, S6, S8). Rent columns scale bond + advance rent only (Section 9) |
| ↔️ Startup capital range (headline rent) | A$328,912 (lean) to A$754,832 (full build) | | | 🟡 S7, S8 |
| 📈 **Monthly net, Month 5 onward (repo basis, GST-inclusive)** | **+A$35,186.40** | +A$33,686.40 | +A$32,686.40 | 🟢 Headline S1 §5, locked by Anthony 2026-10-10 |
| 🧾 **GST-stress downside** (all AM sales taxable) | **+A$23,442.58** | +A$22,078.94 | +A$21,169.85 | 🟠 Conservative downside, TM estimate, accountant to confirm |
| ⚖️ **Break-even, AM clients/day (repo basis)** | **12.655** | 12.882 | 13.034 | 🟢 Headline reproduces S1 §10 exactly |
| ⚖️ Break-even, AM clients/day (GST-stress) | 14.083 | 14.310 | 14.462 | 🟠 TM |
| ⚖️ Break-even (two streams, current mix) | about **516 visits/month** (357 AM + 158 PM) | | | 🆕 Section 6 |
| 🏦 **Peak funding** (with GST timing) | **A$318,176** | A$325,403 | A$330,222 | 🟢 All fit inside their startup capital |
| 🏦 Peak funding (repo basis, no GST) | A$312,281 | A$318,281 | A$322,281 | 🟢 |
| ⚠️ Lowest cash point (Month 3) | **A$18,022** | A$13,795 | A$10,976 | 🟠 Thin in every case |
| ⏱️ **Payback** (repo basis / after GST) | **Month 13 / Month 18** | Month 14 / Month 19 | Month 14 / Month 20 | 🆕 Sections 7 and 9 |
| 🧪 Lab / courier fee to GTT | A$0 per client (repo assumption) | | | 🟠 Tender fees TO CONFIRM. Each A$10/client costs about A$4,739/month (Section 10) |
| 🧾 Two-tier GST (proposed) | +A$2,154/month vs GST-stress if A$50 of each A$250 package is GST-free | | | 🔴 Proposed only. Needs accountant advice and possibly an ATO private ruling (Section 11) |

**Plain English:** the plan needs about A$336k at A$8,000 rent, or up to about A$341k at A$10,500 rent. Cash is tightest in Month 3. Payback is roughly 13 to 20 months depending on rent and GST, if 18 clients/day is reached by Month 5. A lab fee is the biggest unknown left: at A$20+ per client the cash buffer is close to gone.

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

## 3. 12-month P&L by month (Table 1, committed model)

**Ramp:** the repo's own curve. Revenue is 43% / 64% / 79% / 93% of steady state in Months 1 to 4, then 100% (S2, S18). 🟡 The repo flags that this curve's origin is undocumented (S2 `conflict_ramp_curve_origin_unknown`).

**Costs:** full payroll from Month 1 (repo method, conservative, S3). Only marketing ramps: A$600 / 800 / 1,000 / 1,200, then A$1,500 (S3, S4).

**Line definitions:**
- AM GTT = 18 clients/day x A$250 x 26.33 trading days at steady state (S1 §5, S2).
- PM standalone = 10 sessions/day, about 210 transactions/month at A$117 average (S13).
- Ancillary (cafe / retail) = A$0, excluded by founder decision (S1, S4).
- Direct costs = GTT supplies A$400 + consumables A$800 (S5 §4, S3).
- Payroll = A$93,595.63 (direct labour and opening A$82,318.05 + super A$9,878.17 + workers comp A$1,399.41) (S3).
- Rent = A$8,000 (founder decision 2026-10-03, S16).
- Other overhead = utilities, insurance, laundry, marketing, software, cleaning, accounting, misc (S5 §4, S3).

| Month | Ramp | AM GTT | PM standalone | **Total revenue** | Direct costs | Payroll | Rent | Other overhead | **Total costs** | **Net** | Cumulative net |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 | 43% | A$50,948.55 | A$10,571.71 | A$61,520.26 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$4,188.34 | A$106,983.97 | 🔴 -A$45,463.71 | -A$45,463.71 |
| M2 | 64% | A$75,830.40 | A$15,734.64 | A$91,565.04 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$4,388.34 | A$107,183.97 | 🔴 -A$15,618.93 | -A$61,082.64 |
| M3 | 79% | A$93,603.15 | A$19,422.44 | A$113,025.59 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$4,588.34 | A$107,383.97 | 🟢 A$5,641.62 | -A$55,441.02 |
| M4 | 93% | A$110,191.05 | A$22,864.39 | A$133,055.44 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$4,788.34 | A$107,583.97 | 🟢 A$25,471.47 | -A$29,969.55 |
| M5 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$5,216.85 |
| M6 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$40,403.25 |
| M7 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$75,589.65 |
| M8 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$110,776.05 |
| M9 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$145,962.45 |
| M10 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$181,148.85 |
| M11 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$216,335.25 |
| M12 | 100% | A$118,485.00 | A$24,585.37 | A$143,070.37 | A$1,200.00 | A$93,595.63 | A$8,000.00 | A$5,088.34 | A$107,883.97 | 🟢 A$35,186.40 | A$251,521.65 |
| **Year 1** | | **A$1,278,453.15** | **A$265,276.14** | **A$1,543,729.29** | **A$14,400.00** | **A$1,123,147.56** | **A$96,000.00** | **A$58,660.08** | **A$1,292,207.64** | **A$251,521.65** | |

### 3a. Steady-state payroll breakdown (Month 5 onward, S3 `cost_table1_m5plus`)

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

### 3b. Steady-state other overhead breakdown (S5 §4, total matches S3 A$14,288.34)

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

### 3c. GST estimate per month (general information only, TM)

The repo's P&L figures are **GST-inclusive** and have **no line for GST paid to the ATO** (S11). This table estimates it.

Assumptions (TM, accountant to confirm): all revenue is taxable at 10% (S11 says "likely fully taxable"). GST credits are claimed on rent, consumables and other overhead. GTT supplies are GST-free (S12). Wages and super carry no GST.

| Month | GST on sales (rev ÷ 11) | GST credits | **Net GST owed** | **Net after GST** |
|---|---|---|---|---|
| M1 | A$5,592.75 | A$1,180.76 | A$4,411.99 | -A$49,875.70 |
| M2 | A$8,324.09 | A$1,198.94 | A$7,125.15 | -A$22,744.08 |
| M3 | A$10,275.05 | A$1,217.12 | A$9,057.93 | -A$3,416.31 |
| M4 | A$12,095.95 | A$1,235.30 | A$10,860.65 | A$14,610.82 |
| M5 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M6 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M7 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M8 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M9 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M10 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M11 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| M12 | A$13,006.40 | A$1,262.58 | A$11,743.82 | A$23,442.58 |
| **Year 1** | **A$140,339.04** | **A$14,932.76** | **A$125,406.28** | **A$126,115.37** |

🟠 **Why this matters:** if the A$250 package price includes GST, about A$22.73 of each package belongs to the ATO. That cuts steady-state net from A$35,186 to about A$23,443. If part of the package is GST-free (the mixed-supply view in S12), the real figure sits between the two.

Not modelled: income tax (entity undecided), depreciation (the repo P&L has none), interest (no debt assumed).

---

## 4. Cashflow by month

**Rules used:**
- Opening funding = base startup capital A$336,198 (Section 2), all received before opening (TM, no debt assumed).
- Pre-opening capital A$251,198 is spent in Month 0, including the full contingency (TM, conservative).
- Operating cash = monthly P&L net. The repo has no debtor or creditor timing (S11, S21), so none is used.
- GST: monthly BAS, lodged and paid by the 21st of the next month (S12 recommends monthly). So each month's GST is paid the month after.
- Deferred capex per Section 2d.

| Month | Opening cash | Funding in | CapEx out | Operating cash | GST paid (BAS) | **Closing cash** |
|---|---|---|---|---|---|---|
| M0 (pre-opening) | A$0.00 | A$336,198.00 | -A$251,198.00 | A$0.00 | A$0.00 | **A$85,000.00** |
| M1 | A$85,000.00 | A$0.00 | A$0.00 | -A$45,463.71 | A$0.00 | **A$39,536.29** |
| M2 | A$39,536.29 | A$0.00 | A$0.00 | -A$15,618.93 | -A$4,411.99 | **A$19,505.37** |
| M3 | A$19,505.37 | A$0.00 | A$0.00 | A$5,641.62 | -A$7,125.15 | ⚠️ **A$18,021.84** |
| M4 | A$18,021.84 | A$0.00 | -A$5,600.00 | A$25,471.47 | -A$9,057.93 | **A$28,835.38** |
| M5 | A$28,835.38 | A$0.00 | A$0.00 | A$35,186.40 | -A$10,860.65 | **A$53,161.13** |
| M6 | A$53,161.13 | A$0.00 | -A$7,774.00 | A$35,186.40 | -A$11,743.82 | **A$68,829.71** |
| M7 | A$68,829.71 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$92,272.29** |
| M8 | A$92,272.29 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$115,714.87** |
| M9 | A$115,714.87 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$139,157.45** |
| M10 | A$139,157.45 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$162,600.03** |
| M11 | A$162,600.03 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$186,042.61** |
| M12 | A$186,042.61 | A$0.00 | A$0.00 | A$35,186.40 | -A$11,743.82 | **A$209,485.19** |

### 4a. Peak funding requirement

| Measure | Figure | Note |
|---|---|---|
| Pre-opening capital spent (Month 0) | A$251,198.00 | S8 |
| Deepest drop after opening, with GST | A$66,978.16 | A$85,000 reserve falls to A$18,021.84 (Month 3) |
| **Peak funding requirement (with GST timing)** | **A$318,176.16** | A$336,198 less lowest cash A$18,021.84 |
| Peak funding requirement (repo basis, no GST) | A$312,280.64 | A$251,198 + cumulative low -A$61,082.64 at Month 2 |
| Headroom inside A$336,198 base | A$18,021.84 | 🟠 Thin. One bad month or a fit-out overrun uses it up |

🟢 Unspent contingency (up to A$26,914) would add to headroom.
🟢 GST credits on fit-out and equipment could come back on the first BAS. Not counted here (TM, conservative).
🔴 Pre-opening rent during the fit-out period is not in the base budget. Only 1 month of advance rent is included (Section 8).

---

## 5. Balance sheet snapshots (simple)

**Method (TM):** pre-opening costs that buy lasting assets are capitalised: fit-out, design and approvals, contingency (assumed spent on fit-out), furniture, equipment. Advance rent, legal fees, IT setup, pre-opening wages, launch marketing and professional fees (A$36,481 total) are expensed before opening. Assets are shown at cost with no depreciation, because the repo P&L has none. Retained earnings use **net after GST** (Section 3c). GST payable = the month's net GST, paid the next month.

| Line | Opening day (end M0) | Month 6 | Month 12 |
|---|---|---|---|
| Cash | A$85,000.00 | A$68,829.71 | A$209,485.19 |
| Fit-out, furniture, equipment (at cost) | A$204,132.00 | A$217,506.00 | A$217,506.00 |
| Opening stock | A$2,585.00 | A$2,585.00 | A$2,585.00 |
| Lease bond | A$8,000.00 | A$8,000.00 | A$8,000.00 |
| **Total assets** | **A$299,717.00** | **A$296,920.71** | **A$437,576.19** |
| GST payable to ATO | A$0.00 | A$11,743.82 | A$11,743.82 |
| **Total liabilities** | **A$0.00** | **A$11,743.82** | **A$11,743.82** |
| Capital contributed | A$336,198.00 | A$336,198.00 | A$336,198.00 |
| Retained earnings | -A$36,481.00 | -A$51,021.11 | A$89,634.37 |
| **Total equity** | **A$299,717.00** | **A$285,176.89** | **A$425,832.37** |
| **Check: assets less liabilities less equity** | ✅ A$0.00 | ✅ A$0.00 | ✅ A$0.00 |

How the 3 statements link:
- Retained earnings M6 = -A$36,481.00 + sum of M1 to M6 net after GST (-A$14,540.11) = -A$51,021.11.
- Retained earnings M12 = -A$36,481.00 + Year 1 net after GST (A$126,115.37) = A$89,634.37.
- Cash M12 ties to Section 4 closing cash.

---

## 6. Break-even

### 6a. Repo unit: AM clients/day (reproduced) ✅

Repo method (S1 §10): all costs are fixed. PM is held at its full A$24,585.37. Solve for AM clients/day.

**Formula:** (total costs - PM revenue) ÷ (A$250 x 26.33 trading days)

= (A$107,883.97 - A$24,585.37) ÷ A$6,582.50
= A$83,298.60 ÷ A$6,582.50
= **12.655 AM clients/day** ✅ exact match with S1 §10

- ≈ 333.2 AM visits/month, 70.3% of the 18/day target.
- Margin of safety: 5.345 clients/day (29.7%).

### 6b. Two-stream break-even in visits/month (🆕 new analysis)

The repo has no two-stream break-even. This section is new and is labelled TM.

**Formula:** fixed costs ÷ blended contribution per visit

- Fixed costs = A$107,883.97. The repo treats every cost as fixed, so contribution per visit = price (S3, S21).
- AM contribution = A$250.00 per visit (S1 §2).
- PM contribution = A$117.00 per transaction (A$24,585.37 ÷ 210.13 transactions, S13).
- If GTT supplies are treated as variable instead (A$2/test, S4), AM contribution falls to A$248 and break-even rises by less than 1%.

| Mix | Blended contribution / visit | **Break-even visits / month** | AM / PM split | Can it be done? |
|---|---|---|---|---|
| 220 : 350 (as briefed) | A$168.33 | **640.9** | 247.4 AM + 393.5 PM | 🔴 No. PM capacity is now about 210/month, so 393 PM visits is above the cap |
| Current capacity mix 474 : 210 | A$209.15 | **515.8** | 357.4 AM + 158.4 PM | 🟢 Yes. 75.4% of 684 visits/month capacity |

**Reconciling with the repo's 12.655:**
- Repo method: PM full (210 transactions) + 333 AM visits = 543 visits/month.
- Two-stream method: both streams scale down together, giving 357 AM (13.57 clients/day) + 158 PM = 516 visits.
- Both are right. They differ because PM is assumed full in one and scaled in the other. AM visits earn more each (A$250 vs A$117), so the repo method needs fewer AM clients.
- The 220:350 mix comes from the superseded v2.0 model (10 clients/day, 16 PM sessions/day). It no longer matches capacity.

### 6c. Sensitivity (steady state, repo basis, before GST)

| Scenario | Monthly net | Break-even AM clients/day | Status |
|---|---|---|---|
| Base: 18/day, A$8k rent | A$35,186.40 | 12.655 | 🟢 |
| Volume -20% (14.4 AM/day, PM -20%) | A$6,572.33 | 12.655 | 🟠 Thin |
| Price -10% (AM A$225, PM average -10%) | A$20,879.36 | 14.476 | 🟡 |
| Rent A$7,000 | A$36,186.40 | 12.503 | 🟢 |
| Rent A$9,000 | A$34,186.40 | 12.806 | 🟢 |
| Rent A$9,500 (budget low end) | A$33,686.40 | 12.882 | 🟢 Section 9 |
| Rent A$10,500 (budget high end) | A$32,686.40 | 13.034 | 🟢 Section 9 |
| Repo downside: 12/day (Table 2) | A$1,096.40 | 11.833 (repo's own Table 2 figure) | 🔴 Near zero (S1 §10) |

Formulas (TM): net = revenue x factor - A$107,883.97. Break-even = (costs ± rent change - PM revenue x price factor) ÷ (A$6,582.50 x price factor).
Note: after estimated GST (Section 3c), the volume -20% case becomes a small loss, about -A$2,570/month (TM).

---

## 7. Payback timeline

**Definition (TM):** the month when cumulative cash from opening day gets back to zero. That means the A$251,198 pre-opening spend, plus ramp losses, plus deferred capex, has been earned back. The unused reserve is not counted, because it never left the bank.

| Month | Cumulative (repo basis) | Cumulative (after GST) |
|---|---|---|
| M0 | -A$251,198.00 | -A$251,198.00 |
| M2 | -A$312,280.64 | -A$316,692.63 |
| M3 | -A$306,639.02 | 🔴 -A$318,176.16 (lowest) |
| M6 | -A$224,168.75 | -A$267,368.29 |
| M9 | -A$118,609.55 | -A$197,040.55 |
| M12 | -A$13,050.35 | -A$126,712.81 |
| **M13** | ✅ **A$22,136.05** | -A$103,270.23 |
| M15 | A$92,508.85 | -A$56,385.07 |
| M17 | A$162,881.65 | -A$9,499.91 |
| **M18** | A$198,068.05 | ✅ **A$13,942.67** |

| Basis | Payback |
|---|---|
| Repo basis (GST-inclusive P&L) | **Month 13** after opening |
| After estimated GST | **Month 18** after opening |

Months 13 to 18 assume steady state continues, the same "no growth after Month 5" rule the repo uses (S2, S21).

---

## 8. Conflicts and open items

### 8a. Superseded figures (do not use)

| # | Old figure | Where | Current figure | Status |
|---|---|---|---|---|
| 1 | Revenue A$113,712.16 / costs A$88,625.09 / net +A$25,087.07 (v2.0, 10 clients/day, ancillary A$8,580 included) | S4 history, S11, S20 | A$143,070.37 / A$107,883.97 / +A$35,186.40 | ✅ RESOLVED by Anthony 2026-10-10: baseline choice locked to v3.0 (+A$35,186.40 headline, +A$23,443 GST-stress downside). S20 still calls v2.0 "current authoritative", which is stale |
| 2 | 220 AM : 350 PM visits/month mix | S20, original brief | about 474 AM : 210 PM per month | 🗄️ Superseded (18/day AM; PM capped at 10 sessions/day on 2026-09-19) |
| 3 | Net A$63,028.75 / A$56,581.70 / A$44,166.17 (and others) | S1 strike-throughs, S21 | +A$35,186.40 | 🗄️ Superseded |
| 4 | Revenue A$154,710.69, net A$32,576.80, break-even 13.051/day, trough -A$76,532.52 | S5 (titled "Current") | See Sections 3, 4, 6 | 🗄️ Stale (2026-08-18) despite the file name |
| 5 | Workbook: revenue A$155,215.80, net A$56,581.70, break-even 9.404/day | S21 | See above | 🗄️ Stale (2026-08-09) |
| 6 | Break-even 9.4/day and 9.821/day; 11.290/day | S22 dossiers | 12.655/day | 🗄️ Stale. S1 says 11.290 "is now STALE" |
| 7 | Break-even "12 AM visits/day, capacity 8", Year 1 loss -A$513,540 | S20 | 12.655/day, Year 1 +A$251,522 (repo basis) | 🗄️ Single-stream illustration on v2.0 inputs. Not real |
| 8 | Cash trough -A$53,353.76 (Month 2) | S19 (2026-08-21) | -A$61,082.64 (Month 2) on 2026-09-19 figures | 🗄️ Not recomputed after the PM 10-session decision |
| 9 | Inherited revenue A$157,792.16 | S1 §5 | A$143,070.37 canonical | 🗄️ Historical record only |

### 8b. Live conflicts between documents

| # | Conflict | Figures | Impact | Owner |
|---|---|---|---|---|
| 10 | S1 §5 cost table lines do not add to its own total | 82,318.05 + 1,399.41 + 14,288.34 = A$98,005.80, but total says A$107,883.97 | Missing super line A$9,878.17 (present in S3). Total is right; table is incomplete | Grace: add super row to S1 |
| 11 | Rent budget vs footprint | Headline keeps A$8,000 (S16). Anthony's budget is A$9,500 to 10,500/month for 257 to 290 sqm, about A$32.76 to 40.86 per sqm per month (TM arithmetic) | -A$1,500 to -A$2,500/month to net; full effect in Section 9 | ✅ RESOLVED by Anthony 2026-10-10 |
| 12a | Floor area | 257 to 290 sqm with 2 blood collection rooms | Sets the search brief | ✅ RESOLVED by Anthony 2026-10-10 |
| 12b | Fit-out for the larger floor area not costed | Base fit-out is for 239 sqm. 257 to 290 sqm adds 18 to 51 sqm. At the repo's A$800 to 1,250/sqm = A$14,400 to 63,750 extra fit-out (TM arithmetic, indicative only). Not added to any capital figure here | Base capex likely understated; would eat the A$10,976 to 18,022 cash headroom | 🔴 Still open: needs venue + builder quote |
| 13 | Construction rate vs market | Repo A$800 to 1,250/sqm is internal, not benchmarked (S23). Allied-health benchmark A$1,800 to 2,800/sqm; blended estimate is A$39,000 to 60,450 higher (S15) | Fit-out risk on the high side | 3 builder quotes (repo tracker item 49) |
| 14 | Cafe equipment not in base | A$5,000 to 12,650, made day-one 2026-08-23 (S10); base dated 2026-08-10 | Base capex understated | Grace / founder |
| 15 | Clinical equipment two figures | Summary A$8,300 to 14,100 vs itemised A$6,330 to 10,240 (S10, S6) | Up to A$3,860 | Unreconciled in repo |
| 16 | Lease cost overlap | Lease and legal lines may double up, up to A$48,600 combined high end (S6 `conflict_lease_cost_overlap`) | Unclear | Unresolved in repo |
| 17 | GST on the AM package | S12 codes the package as mixed (GST-free pathology part + taxable wellness part). S11 says "likely fully taxable", since the pathology partner bills Medicare directly | A$0 to about A$11,744/month cash difference. Proposed two-tier structure in Section 11 | 🔴 Accountant, possibly ATO private ruling |
| 18 | GST not in any repo P&L or cashflow | Figures are GST-inclusive with no GST-paid line (S11) | Payback Month 13 vs Month 18 | 🔴 Accountant |
| 19 | Working capital reserve basis | A$85,000 to 110,000 flagged stale in the repo (S19, repo tracker item 30). This model needs about A$67,000 drop cover with GST | Reserve looks adequate, but headroom is only A$18,022 | Founder |
| 20 | Startup capital: several ranges | Adopted A$251,198 (S6); older adopted range A$292,335 to 594,900 (S1 §7.4); reconstruction A$283,122 to 644,832 (S9) | This model uses A$251,198 as base | Locked only after venue + quotes |

### 8c. Open items and this model's assumptions (TM)

| # | Item | Treatment here | Status |
|---|---|---|---|
| 21 | Ramp curve 43/64/79/93/100% | Used as the repo does; origin undocumented (S2) | 🟡 Assumption from repo |
| 22 | AM labour does not ramp | Full payroll from Month 1, as the repo does (S3 `conflict_am_labor_ramp_unmodelled`) | 🟡 Conservative |
| 23 | Contingency fully spent at Month 0 and capitalised to fit-out | TM | 🟡 Conservative |
| 24 | Deferred capex timing (Month 4 and Month 6) | TM, from S7 §5 and S8 §4.3 | 🟡 |
| 25 | All funding is capital put in before opening, no loans | TM. Source of funds not stated in repo | 🟡 |
| 26 | GST: all sales taxable, monthly BAS paid next month, credits on non-wage overhead | TM, from S11 and S12 | 🟠 Accountant |
| 27 | GST credits on fit-out and equipment | Not claimed (could improve early cash) | 🟢 Upside |
| 28 | Rent during fit-out (before trading) | Not in base. Only 1 month advance rent included. Each month of fit-out rent costs A$8,000 / A$9,500 / A$10,500 at the three rent levels. A rent-free fit-out period would remove this | 🔴 Negotiate at lease stage |
| 29 | No debtor / creditor timing | P&L net = operating cash (repo has no timing data) | 🟡 |
| 30 | No depreciation, income tax or interest | Not modelled; entity undecided | 🟡 Accountant |
| 31 | Workers comp 1.7% | Repo placeholder rate | 🟡 |
| 32 | Saturday "experienced staff" cover | Pay loading unknown; no cost added (S1 §0) | 🟡 Founder |
| 33 | Insurance A$708.34/month | Modelled, not a broker quote | 🟡 Quotes in motion |
| 34 | PM volume (10 sessions/day) and A$117 average | Founder-set planning input (S13), no booking data | 🟡 |
| 35 | Inventory held flat | Assumed replenished via the monthly consumables line | 🟡 |
| 36 | Lab / courier fee charged to GTT by PathWest or WDP | Repo assumes A$0 (lab bills Medicare). Sensitivity only in Section 10 | 🔴 TO CONFIRM via tender |
| 37 | Two-tier GST invoicing (s38-10) | Proposed only. Clinical / lounge split is a TM assumption (Section 11) | 🔴 Accountant + possibly ATO private ruling |
| 38 | Contingency in rent-adjusted capital | Kept at A$26,914. Not re-scaled for the higher bond and advance rent (adds about A$360 to A$600 at 12%) | 🟡 TM |
| 39 | Rent-adjusted scenarios keep every other line at the headline | Only rent, bond and advance rent change. Floor-area fit-out uplift is item 12b | 🟡 TM |

---

## 9. Rent-adjusted scenarios (🆕 v0.2)

📌 **The headline uses A$8,000/month rent, per Anthony's instruction (2026-10-10).** His real rent budget is A$9,500 to A$10,500/month, to fit 257 to 290 sqm with 2 blood collection rooms. The two right-hand columns show what that budget does.

**What changes (TM):** rent every month, the lease bond (1 month's rent) and the advance rent (1 month's rent). Everything else stays at the headline. Same ramp, same GST method, same deferred capex.

| Measure | Headline A$8,000 ✅ | Rent-adjusted A$9,500 | Rent-adjusted A$10,500 |
|---|---|---|---|
| Rent per month | A$8,000.00 | A$9,500.00 | A$10,500.00 |
| Rent per sqm per month (257 to 290 sqm) | n/a (headline) | A$32.76 to A$36.96 | A$36.21 to A$40.86 |
| Lease bond (1 month, or bank guarantee) | A$8,000.00 | A$9,500.00 | A$10,500.00 |
| Advance rent (1 month) | A$8,000.00 | A$9,500.00 | A$10,500.00 |
| Pre-opening capital | A$251,198.00 | A$254,198.00 | A$256,198.00 |
| Working capital reserve | A$85,000.00 | A$85,000.00 | A$85,000.00 |
| **Total startup capital** | **A$336,198.00** | **A$339,198.00** | **A$341,198.00** |
| Each month of rent during fit-out (not in any total, item 28) | A$8,000.00 | A$9,500.00 | A$10,500.00 |
| **Net per month, Month 5 onward (repo basis)** | **A$35,186.40** | **A$33,686.40** | **A$32,686.40** |
| **Net per month, GST-stress downside** | **A$23,442.58** | **A$22,078.94** | **A$21,169.85** |
| Year 1 net (repo basis) | A$251,521.65 | A$233,521.65 | A$221,521.65 |
| Year 1 net (after estimated GST) | A$126,115.37 | A$109,751.71 | A$98,842.62 |
| **Break-even, AM clients/day (repo basis)** | **12.655** | **12.882** | **13.034** |
| Break-even, AM clients/day (GST-stress) | 14.083 | 14.310 | 14.462 |
| Peak funding (repo basis, no GST) | A$312,280.64 | A$318,280.64 | A$322,280.64 |
| **Peak funding (with GST timing)** | **A$318,176.16** | **A$325,403.44** | **A$330,221.62** |
| Lowest cash (Month 3) = headroom | A$18,021.84 | A$13,794.56 | A$10,976.38 |
| **Payback (repo basis)** | **Month 13** | **Month 14** | **Month 14** |
| **Payback (after GST)** | **Month 18** | **Month 19** | **Month 20** |

**Formulas (TM):**
- Net = headline net less (rent less A$8,000).
- GST-stress net also gets back 1/11 of the extra rent as a GST credit.
- Break-even = (A$107,883.97 + extra rent less PM A$24,585.37) ÷ A$6,582.50.
- Peak funding and payback are re-run month by month with the same cashflow rules as Sections 4 and 7.

**Plain English:**
- Each extra A$1,000 of rent costs A$1,000 a month (about A$909 after the GST credit).
- At A$10,500 the business still clears about A$32.7k a month on the repo basis, or about A$21.2k in the GST-stress case.
- Payback slips by 1 to 2 months.
- The real risk is the cash buffer: it shrinks to about A$11k, and the bigger floor area's fit-out (item 12b, up to about A$63.8k) is not in it yet.

---

## 10. Lab fee sensitivity: dual-lab tender (🆕 v0.2)

**Strategy:** PathWest and WDP compete on courier plus lab analysis through a tender. GTT employs its own 2 phlebotomists (already in payroll, Section 3a).

**What the repo assumes: A$0 lab fee to GTT (Medicare bulk-billing by the lab).**
- "GTT Center Perth earns zero revenue from pathology billing ... the pathology partner (WDP/PathWest) bills Medicare directly" (S11).
- "Your OGTT is bulk-billed by WDP at no charge to you" for Medicare card holders (S28).
- The partner's revenue per client is "the Medicare rebate value of the OGTT test itself ... not a fee GTT Center Perth pays the partner directly" (S26). Courier cost is not modelled anywhere in the repo (S26).
- So no lab or courier fee appears in any repo cost line. 🔴 **Actual tender fees are TO CONFIRM.**

**Fee basis (TM):** a flat fee per AM client, charged at the steady-state volume of 473.94 AM clients/month (18 x 26.33). It ramps with volume in Months 1 to 4. GST-stress column assumes the fee includes GST and GTT claims the credit.

**At headline rent A$8,000 (startup capital A$336,198):**

| Fee per client | Monthly cost | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST) | Peak funding (with GST) | Headroom in capital | Payback (repo / GST) |
|---|---|---|---|---|---|---|---|
| A$0 (repo) | A$0.00 | **A$35,186.40** | A$23,442.58 | 12.655 / 14.083 | A$318,176.16 | 🟢 A$18,021.84 | M13 / M18 |
| A$10 | A$4,739.40 | **A$30,447.00** | A$19,134.03 | 13.182 / 14.669 | A$326,530.43 | 🟠 A$9,667.57 | M15 / M22 |
| A$20 | A$9,478.80 | **A$25,707.60** | A$14,825.49 | 13.755 / 15.307 | A$334,884.70 | 🔴 A$1,313.30 | M17 / M27 |
| A$30 | A$14,218.20 | **A$20,968.20** | A$10,516.94 | 14.380 / 16.003 | A$344,627.24 | 🔴 short by A$8,429.24 | M20 / M38 |

**At rent A$10,500 (startup capital A$341,198):**

| Fee per client | **Net / month (repo)** | Net / month (GST-stress) | Break-even AM/day (repo / GST) | Peak funding (with GST) | Headroom in capital | Payback (repo / GST) |
|---|---|---|---|---|---|---|
| A$0 | **A$32,686.40** | A$21,169.85 | 13.034 / 14.462 | A$330,221.62 | 🟠 A$10,976.38 | M14 / M20 |
| A$10 | **A$27,947.00** | A$16,861.30 | 13.577 / 15.065 | A$338,575.89 | 🔴 A$2,622.11 | M16 / M25 |
| A$20 | **A$23,207.60** | A$12,552.76 | 14.168 / 15.720 | A$346,930.16 | 🔴 short by A$5,732.16 | M19 / M33 |
| A$30 | **A$18,468.20** | A$8,244.21 | 14.812 / 16.434 | A$358,945.43 | 🔴 short by A$17,747.43 | M23 / M49 |

**Plain English:**
- Every A$10 per client costs about A$4,739 a month, about the same as 0.7 extra AM clients/day.
- The business stays profitable even at A$30 per client. But from about A$20 per client, the startup capital no longer covers the Month 3 cash low.
- Tender goal: A$0 to GTT (lab earns from Medicare), or at most about A$10 per client. Get courier, consumables supply and any rental or fee terms in writing from both labs.

---

## 11. Two-tier GST invoicing (proposed, s38-10 GST Act) (🆕 v0.2)

> **This is general knowledge, not your personal documents. Verify before acting.**
> **Status: proposed; requires accountant advice and possibly an ATO private ruling.** Nothing here is settled tax treatment.

### 11a. The proposed structure

| Invoice line | What it covers | Proposed GST |
|---|---|---|
| Clinical phlebotomy component | Blood collection by GTT's employed phlebotomist for the referred GTT test | GST-free under s38-10 **only if** every condition below is met. Unproven |
| Wellness lounge component | Treatments, lounge access, refreshments | Taxable, 10% GST |
| Pathology test itself | Lab analysis | Not GTT's supply. The lab bills Medicare (S11, S26) |

### 11b. Why this is not settled (read before relying on it)

- 🔴 **Recognised professional test.** s38-10 only covers services by a recognised professional in the s38-10 table (for example nursing, physiotherapy, pharmacy). To my knowledge, phlebotomy is not a listed profession. A collection by a registered nurse might arguably sit under nursing. A phlebotomist alone may not qualify.
- 🔴 **"Generally accepted as necessary" test.** The service must be generally accepted in the profession as necessary for appropriate treatment of the recipient.
- 🔴 **Pathology is normally the lab's Medicare service, not GTT's.** The collection is usually part of the lab's own Medicare-billed service. Whether a GTT-employed phlebotomist's collection is a separate supply by GTT is **not settled**.
- 🟠 **Repo conflict.** The repo currently says the A$250 package is 100% wellness and lounge, with the pathology billed separately to Medicare (S24 via S11, S25). That framing supports no GST-free part at all. The repo's older Xero coding (S12) assumed a mixed supply. A two-tier invoice changes this framing and must be decided on purpose.
- 🟠 **Fair price.** Any clinical price has to be a genuine, market-supportable value. Shifting price into the GST-free line just to cut GST risks the ATO's anti-avoidance rules.
- 🟢 **GST credits are kept.** GST-free supplies (unlike input-taxed ones) do not stop GTT claiming GST credits on its costs.

### 11c. Effect on net profit

**The repo's pricing supports no clinical / lounge split** (S24 says the package is 100% wellness and lounge). So every split below is a **TM assumption**. The A$50 row is anchored to one real market price: a competitor's A$50 "pathology only" offer (S27, Tier 3, not GTT's price).

Method (TM): GST saved per month = AM clients/month (473.94) x clinical amount ÷ 11. PM is unchanged (taxable). Compared with the GST-stress downside, where all AM sales are taxable.

| Clinical part of each A$250 package (assumption) | Share | GST saved / month | **Net / month at A$8,000** | Net at A$9,500 | Net at A$10,500 | Break-even AM/day (GST, A$8,000) | Payback after GST (A$8,000) |
|---|---|---|---|---|---|---|---|
| A$0 (GST-stress downside) | 0% | A$0.00 | **A$23,442.58** | A$22,078.94 | A$21,169.85 | 14.083 | M18 |
| A$25 | 10% | A$1,077.14 | **A$24,519.72** | A$23,156.08 | A$22,246.99 | 13.943 | M17 |
| A$50 (market anchor) | 20% | A$2,154.27 | **A$25,596.85** | A$24,233.21 | A$23,324.12 | 13.806 | M17 |
| A$75 | 30% | A$3,231.41 | **A$26,673.99** | A$25,310.35 | A$24,401.26 | 13.672 | M16 |

**Plain English:**
- If it works, a two-tier invoice adds about A$1.1k to A$3.2k a month over the GST-stress downside.
- It does not change the A$35,186.40 headline (that figure has no GST line at all).
- It closes only a small part of the roughly A$11.7k a month gap between headline and downside.
- Worth asking the accountant. Not worth building the business case on.

---

*Arithmetic: every table above was re-summed with a script before publishing. Repo source files were read only. Nothing on the server was edited.*
