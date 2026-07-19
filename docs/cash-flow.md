> **2026-07-14 UPDATE (corrected) — PM MODEL RECALCULATED ON ACTUAL HOURS WORKED:** PM afternoon sessions are individual services (NOT Package 1/2/3), delivered by a 4-role dedicated PM roster (massage, hair, nail, beauty — see `pm-staffing-roster.md`), staffed on hours actually worked (casuals paid per session-hour, not a blanket shift). Full recalculated P&L: **profitable from Month 4 (+A$4,924/month), reaching +A$6,663/month at Month 5+ steady state.** All revenue/cost figures in the tables below are SUPERSEDED — see `pm-staffing-roster.md` "CORRECTION — Hours-Based Casual Cost Model" section for the current authoritative numbers.
>
> **FURTHER UPDATE (2026-07-19 — Phase 6 verification pass, found via cross-document check):** `pm-staffing-roster.md` (referenced immediately above as authoritative) is itself built on the 8-client Scenario B AM model and reports a Month 5+ steady-state figure of -A$4,384/month (a loss) under its own later correction — **not** the +A$4,924/Month-4 / +A$6,663/Month-5+ figures stated in the banner above. Neither of those matches `profit-loss-tables.md` v2.0 (2026-07-17, the most recent of the three documents), which reports **+A$25,087.07/month at Month 5+ steady state** under the current 10-client Scenario C model. **This entire file (`cash-flow.md`) is built on the superseded 8-client Scenario B model and 3-package (Package 1/2/3) structure — both since replaced.** Its month-by-month *ramp shape* (gradual build to full capacity by Month 5) remains a reasonable methodology reference, but none of its absolute dollar figures should be treated as current without re-verification against `profit-loss-tables.md` v2.0. See `docs/01_conflicts_log.md` for the full three-way discrepancy and `docs/business-plan.md`/`docs/executive-summary.md` for where this has been flagged in founder-facing summary documents.

# GTT Center Perth — 18-Month Cash Flow Projection
## YETI Holding Trust | GTT Center Perth trading entity
### Version 1.0 | June 2026

---

## ⚠ DAY 51 RECONCILIATION

This model has been reconciled to the Day-51 package-price model (`financial-break-even-staff.md` — Package 1/A$200, Package 2/A$250, Package 3/A$300, structure locked, prices negotiable). Three changes from the Day-50 version:

1. **No separate "Morning GTT" vs "Afternoon Wellness" revenue lines.** Every visit (AM GTT or PM Spa Package) sells one of Package 1/2/3. Initial blended avg = **A$250/visit** (30/40/30 mix).
2. **Subtenant income removed entirely** (Bloom Baby keepsake scan + dietitian — both out of scope for startup, no equipment/contracts). All subtenant rows/columns deleted from this model.
3. **3D scan operator replaced by 1 PM Service Therapist** (new hire — AM staff are fully committed to the GTT window and cannot double as PM staff). Fixed-cost base rises from A$71,236/month to **A$74,391/month** (A$892,694/yr — see `financial-break-even-staff.md` Total Annual Payroll, incl. new Casual Relief Pool for sick/holiday cover).

Net effect: the 12-staff/A$675,589 stable-month profit of A$5,646 (Day 50) becomes Months 1-3 ramp-up losses (**-A$30,685 / -A$16,270 / -A$7,901**), turning marginally positive (**+A$4,188/month**) at Month 4 once PM Spa Packages reach 5/day, then flat **+A$10,232/month** from Month 5 onward once PM hits its 6/day target (within the Month 3-6 window — see `financial-break-even-staff.md` Lever 2). Capital recovery against the A$149,500 pre-launch baseline moves from ~Month 22 to **~Month 24** — only 2 months later, because the PM ramp to 6/day fully offsets the loss of 3D-scan revenue and subtenant income. The PM Service Therapist's volume ramp (2 -> 3 -> 4 -> 5 -> 6 packages/day, M1-M5) is the single biggest assumption in this model — see `financial-break-even-staff.md` Sensitivity section for the pricing-based fallback lever if PM volume underperforms. Cross-ref: `review-audit.md` CF-01/CF-04/CF-05/CF-06, IC-01/IC-04/IC-06/IC-07.

---

## Model Assumptions

### Revenue Assumptions
| Parameter | Value | Basis |
|---|---|---|
| GTT package avg (AM) | A$250 | 30% Package 1 (A$200) / 40% Package 2 (A$250) / 30% Package 3 (A$300) mix = (0.30×200)+(0.40×250)+(0.30×300) = **A$250**. See `financial-break-even-staff.md` Package Pricing Model. Every visit = one package; venue/lounge bundled free, no separate fee. |
| PM Spa Package avg | A$250 | Same Package 1/2/3 menu, no testing — sold standalone in the afternoon by the PM Service Therapist |
| Morning GTT wave capacity | 8 patients/day (2 phlebotomists, 2 chairs, Day 1) | RESOLVED Day 49 — 2 phlebotomists/2 collection chairs from Day 1, corrected draw-timing pathway. See operations-manual.md for the verified timetable (review-audit.md CF-02 resolved) |
| PM Spa Package capacity | 2/day (Month 1) ramping to 6/day (Month 5+) | 1 PM Service Therapist (new hire), cross-trained massage+facial — see `financial-break-even-staff.md` Shift Structure (CF-01) |
| Operating days/month | 22 days (Mon–Fri, 4.4 weeks) | Closed Sat–Sun. Saturday requires penalty rates — not in current model. |
| Spray tan (ancillary) | A$58,000/yr | See `financial-break-even-staff.md` Revenue Model |
| Retail (ancillary) | A$25,000/yr | See `financial-break-even-staff.md` Revenue Model |
| Cafe (ancillary) | A$15,000/yr | See `financial-break-even-staff.md` Revenue Model |
| **Total ancillary revenue (stable)** | **A$8,167/month** | A$98,000/yr ÷ 12, available from Month 1, scales with total foot traffic (see 18-month table below) |

### Cost Assumptions — Fixed Monthly (Stable Operations)
| Line Item | Monthly | Basis |
|---|---|---|
| Payroll (12 staff incl. relief pool, 12% super) | A$59,422 | A$713,067/yr ÷ 12 — see `financial-break-even-staff.md` Total Annual Payroll (3D scan operator removed, +PM Service Therapist, +Casual Relief Pool) |
| Workers comp (WA, 1.7% of payroll) | A$989 | A$11,867/yr ÷ 12 |
| Rent (commercial lease) | A$8,000 | 200 sqm @ A$40/sqm/month, Subiaco/Nedlands estimate |
| Utilities (power/water) | A$650 | Medical fridge + HVAC |
| Internet + phone | A$150 | Business NBN + mobile |
| Fresha Team plan | A$100 | Booking system |
| Resend email platform | A$30 | Up to 50K emails/month |
| Instagram/Meta ads | A$1,500 | Ongoing digital marketing |
| GTT supplies (glucose, tubes, etc.) | A$400 | 200 tests × A$2/test |
| Laundry/linen service | A$350 | Towels, gowns, treatment linen |
| Cleaning service | A$600 | Daily turn, weekly deep clean |
| Insurance (public liability + PI) | A$400 | Annual A$4,800 ÷ 12 |
| Accounting/bookkeeping | A$500 | Monthly Xero + BAS prep |
| Consumables (wax, nail products, skincare) | A$800 | Service delivery materials |
| Miscellaneous / contingency | A$500 | |
| **TOTAL FIXED + SEMI-FIXED** | **A$74,391** | A$892,694/yr |

**Footnote:** Non-wage overhead (A$13,980/mo = A$167,760/yr — rent through misc, excluding payroll/workers comp) is unchanged from Day 50 and remains canonical, cross-referenced by `financial-break-even-staff.md`.

### Pre-Launch Period (Months -6 to 0)
| Phase | Duration | Monthly Burn |
|---|---|---|
| Legal/structure/entity setup | Weeks 1–2 | A$3,500 (one-off) |
| Venue search/lease negotiation | Weeks 3–8 | A$1,500 admin/legal |
| Fit-out + Instagram launch | Weeks 9–16 | A$12,000 fit-out draw + A$500 social |
| Equipment install + WDP setup | Weeks 17–18 | A$8,000 equipment |
| Staff hire + training | Weeks 19–20 | A$12,000 wages during training |
| Soft open (limited capacity) | Weeks 19–20 | Revenue offset begins |

### Ramp-Up Traffic Model (With Pre-Launch Marketing)
Pre-launch Instagram starts Week 9 of fit-out. Target 300+ waitlist names before soft open.

| Month | GTT visits/day | PM Spa Packages/day | Total visits/day | Operating days | Total visits |
|---|---|---|---|---|---|
| Month 1 (soft open) | 4 | 2 | 6 | 22 | 132 |
| Month 2 | 6 | 3 | 9 | 22 | 198 |
| Month 3 | 7 | 4 | 11 | 22 | 242 |
| Month 4 | 8 | 5 | 13 | 22 | 286 |
| Month 5+ (stable) | 8 | 6 | 14 | 22 | 308 |
| Year 2 (capacity ceiling) | 8 | 6 | 14 | 22 | 308 |

GTT capped at 8/day (2 phlebotomists/2 chairs, Scenario B verified timetable — Scenario A 10-client growth deferred, no verified timetable). PM Spa Packages capped at 6/day (1 PM Service Therapist, per `financial-break-even-staff.md` Lever 2). **Updated Day 51:** operational break-even (fixed costs covered) requires ~298 visits/month (13.5/day) at A$250 avg package price (A$74,391 ÷ A$250). Month 3 (242 visits) falls short; Month 4 (286 visits) clears it narrowly (+A$4,188); Month 5+ (308 visits, both AM and PM at capacity) is flat profitable at +A$10,232/month — see SUMMARY METRICS below.

---

## PRE-LAUNCH CAPITAL DEPLOYMENT (Weeks 1–20)

| Item | Low | Mid | High |
|---|---|---|---|
| Entity setup (trust + company) | A$3,000 | A$4,000 | A$5,000 |
| Lease bond (3 months rent) | A$18,000 | A$24,000 | A$30,000 |
| Fit-out (construction + design) | A$40,000 | A$65,000 | A$90,000 |
| ACSQHC collection room fit-out | A$8,000 | A$12,000 | A$18,000 |
| Medical equipment (fridge, chairs, etc.) | A$6,000 | A$9,000 | A$14,000 |
| Salon equipment (massage tables, nail stations) | A$15,000 | A$22,000 | A$30,000 |
| IT/POS/Fresha setup | A$2,000 | A$3,500 | A$5,000 |
| WDP accreditation/licensing fees | A$2,500 | A$4,000 | A$6,000 |
| Initial supplies (GTT + salon) | A$3,000 | A$5,000 | A$7,000 |
| Pre-launch marketing (social + print) | A$4,000 | A$7,000 | A$10,000 |
| Staff training wages (4 weeks) | A$12,000 | A$16,000 | A$20,000 |
| Pre-open operating costs (2 months) | A$20,000 | A$28,000 | A$35,000 |
| Contingency (15%) | A$20,000 | A$30,000 | A$41,000 |
| **TOTAL STARTUP CAPITAL** | **A$153,500** | **A$229,500** | **A$311,000** |

Working capital recommended (3 months operations): A$55,000–120,000  
**Total capital required (startup + working capital): A$209,000–A$431,000**

---

## 18-MONTH MONTH-BY-MONTH CASH FLOW

### Revenue Formula
- GTT package revenue = GTT visits × A$250 avg (Package 1/2/3, 30/40/30 mix — see `services-pricing-locked.md`)
- PM Spa Package revenue = PM visits × A$250 avg (same 3-package menu, sold standalone, no testing)
- Ancillary revenue = Total visits × ~A$24.75/visit (spray tan + retail + cafe, scales with combined AM+PM foot traffic)

### Cost Formula (Monthly)
- Fixed costs = A$74,391/month (stable from Month 3+; ramps at 90% Month 1 / 95% Month 2 — same ramp shape as before, applied to new base. No further step-increases — the new base already includes the PM Service Therapist and Casual Relief Pool as fixed annual costs regardless of PM volume)
- Ramp-up: Month 1–2 wages slightly reduced as casual hours lower; modelled at 90% Month 1, 95% Month 2

---

### PRE-LAUNCH: Month -2 to 0 (Fit-Out + Social Media Launch)

| Month | Description | Cash Out | Cash In | Net Cash Flow | Cumulative |
|---|---|---|---|---|---|
| Month -2 | Entity setup, lease signed, bond paid | A$(49,000) | A$0 | A$(49,000) | A$(49,000) |
| Month -1 | Fit-out construction, equipment order, social media live | A$(58,000) | A$0 | A$(58,000) | A$(107,000) |
| Month 0 | Staff hired, training, WDP setup, soft launch prep | A$(42,500) | A$0 | A$(42,500) | A$(149,500) |

*Total pre-revenue capital deployed (mid estimate): A$149,500*

---

### OPERATIONAL MONTHS 1–18

| Month | GTT Visits | PM Spa | Total Visits | GTT Rev | PM Rev | Ancillary | **Total Revenue** | Fixed Costs | **Net P&L** | Cumulative |
|---|---|---|---|---|---|---|---|---|---|---|
| **M1** | 88 | 44 | 132 | A$22,000 | A$11,000 | A$3,267 | **A$36,267** | A$66,952 | **A$(30,685)** | A$(180,185) |
| **M2** | 132 | 66 | 198 | A$33,000 | A$16,500 | A$4,901 | **A$54,401** | A$70,671 | **A$(16,270)** | A$(196,455) |
| **M3** | 154 | 88 | 242 | A$38,500 | A$22,000 | A$5,990 | **A$66,490** | A$74,391 | **A$(7,901)** | A$(204,356) |
| **M4** | 176 | 110 | 286 | A$44,000 | A$27,500 | A$7,079 | **A$78,579** | A$74,391 | **A$4,188** | A$(200,168) |
| **M5** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(189,936) |
| **M6** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(179,704) |
| **M7** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(169,472) |
| **M8** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(159,240) |
| **M9** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(149,008) |
| **M10** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(138,776) |
| **M11** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(128,544) |
| **M12** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(118,312) |
| | | | | | | | | | | |
| **M13** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(108,080) |
| **M14** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(97,848) |
| **M15** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(87,616) |
| **M16** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(77,384) |
| **M17** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(67,152) |
| **M18** | 176 | 132 | 308 | A$44,000 | A$33,000 | A$7,623 | **A$84,623** | A$74,391 | **A$10,232** | A$(56,920) |

GTT and PM both reach their capacity ceilings (8/day, 6/day) at Month 5 and stay flat through M18 — both AM (2 phlebotomists/2 chairs) and PM (1 PM Service Therapist) are fully booked at this point, so further revenue growth requires either price increases (see `financial-break-even-staff.md` Sensitivity) or the deferred Scenario A 10-client expansion (operations-manual.md, no verified timetable).

---

## SUMMARY METRICS

### Payback Period
| Scenario | Startup Capital | Month Breakeven Ops | Month Capital Recovered |
|---|---|---|---|
| Low (A$209K) | A$209,000 | Month 4 | ~Month 30 |
| Mid (A$305K) | A$305,000 | Month 4 | ~Month 39 |
| High (A$431K) | A$431,000 | Month 4 | ~Month 52 |

**Operational break-even (monthly costs covered): Month 4** (marginally, +A$4,188/month — full break-even at +A$10,232/month from Month 5, once PM Spa Packages reach their 6/day capacity ceiling)  
**Capital recovery (against Month-0 baseline of A$149,500): ~Month 24** (cumulative crosses zero between M23 ≈ A$(5,760) and M24 ≈ +A$4,472, continuing at the Month-5+ run-rate of +A$10,232/month). For full startup capital (incl. working capital), see Payback Period table above.

### Annual P&L Summary
| Period | Revenue | Costs | Net Profit |
|---|---|---|---|
| Year 1 (M1–M12) | A$918,765 | A$881,533 | **A$37,232** |
| Year 2 (M13–M18 annualised ×2) | A$1,015,476 | A$892,692 | **A$122,784** |

### Key Milestones
| Milestone | Target |
|---|---|
| Pre-launch Instagram live | Week 9 (fit-out start) |
| 100 waitlist signups | Week 13 |
| 300 waitlist signups | Week 18 |
| Soft open (reduced capacity) | Week 20 |
| Full open (all services live) | Month 1 + 2 weeks |
| Break-even operations | Month 4, marginal (+A$4,188/month) — see Day 51 Reconciliation note above |
| Full capacity (14 visits/day: 8 AM GTT + 6 PM Spa) | Month 5 |
| Capital recovery (mid estimate) | ~Month 39 (mid estimate, post-Day-51 reconciliation) |
| Second phlebotomist | RESOLVED Day 49 — both phlebotomists hired pre-launch (Day 1), not a Month 6 trigger. See financial-break-even-staff.md |
| Property purchase evaluation | Month 18 (Year 2–3 if rent+proof of model) |

---

## SENSITIVITY ANALYSIS

### Revenue Sensitivity (Stable Month — 308 visits at A$250 avg = 176 GTT + 132 PM, plus A$7,623 ancillary)

| Scenario | Monthly Revenue | Monthly Costs | Monthly Profit | Annual Profit |
|---|---|---|---|---|
| Bear (70% capacity, no PM/ancillary) | A$30,800 | A$74,391 | A$(43,591) | A$(523,092) |
| Base (Month 5+, as modelled) | A$84,623 | A$74,391 | A$10,232 | A$122,784 |
| Bull (premium package mix + extended PM hours) | A$101,548 | A$75,891 | A$25,657 | A$307,884 |

*Bear = AM-only at 70% of the 8/day GTT cap, no PM Spa Packages and no ancillary trade. Bull = +20% revenue from a richer Package 3 mix and PM hours extended beyond 6/day, with +A$1,500/month in extra casual hours.*

### Cost Sensitivity — Rent Variation (at base revenue A$84,623, Month 5+)
| Rent Scenario | Monthly Rent | Monthly Profit |
|---|---|---|
| Low (Osborne Park, A$5,500) | A$5,500 | A$12,732 |
| Base (Subiaco/Nedlands, A$8,000) | A$8,000 | A$10,232 |
| High (CBD adjacent, A$12,000) | A$12,000 | A$6,232 |

**Insight:** Profitability starts Month 4 (marginal, +A$4,188), reaching full run-rate (+A$10,232/month) at Month 5 once both AM (8/day) and PM (6/day) hit capacity. Even at high-rent locations the margin remains workable (+A$6,232/month) — but location choice (see Open Decisions / Quinn research) still materially affects the speed of capital recovery.

### Break-Even Visits (at different avg package prices)
| Avg Package | Break-Even Visits/Month | Break-Even Visits/Day |
|---|---|---|
| A$200 (Package 1 only) | 372 | 16.9 |
| A$250 (base model, 30/40/30 mix) | 298 | 13.5 |
| A$300 (Package 3 only) | 248 | 11.3 |

Modelled Month 5+ stable-state volume is 308 visits/month (14/day) — above break-even at A$250 (13.5/day) and A$300 (11.3/day), but below break-even at A$200 (16.9/day). The 30/40/30 package mix (`services-pricing-locked.md`) is the model's pricing assumption — see `financial-break-even-staff.md` Sensitivity for the price-vs-margin table if the mix skews toward Package 1.

---

## CASH FLOW NOTES

### Tax Treatment (YETI Holding Trust)
- GTT Center Perth trading profits flow to YETI Holding Trust as trust income
- Trustee (YETI Tipi Holdings PTY LTD) distributes to beneficiaries each financial year
- Anthony's TPI pension: trust distributions are separate income — consult accountant on pension interaction
- GST: GTT medical test (GST-free supply under GSTD 2004/6). Wellness services: standard-rated 10% GST applies
- Important: mixed supply entity — requires split GST accounting in Xero
- **Proposed 30% trust-distribution tax (national budget, not yet legislated):** if enacted, a flat 30% tax would apply to trust distributions before they reach beneficiaries. Illustrative post-tax effect on this model's Net Profit (pre-tax, P&L level — does not change the operating figures above, only what reaches the trust's beneficiaries):
  - Year 1 (M1–M12) Net A$37,232 → post-tax ≈ **A$26,062**
  - Year 2 (M13–M18 ×2) Net A$122,784 → post-tax ≈ **A$85,949**
  - Verify final rate/threshold/effective date with accountant once legislated — this is a planning placeholder, not advice

### GST Note
| Service | GST Status |
|---|---|
| GTT (pathology collection) | GST-free (medical) |
| Massage, facials, nails, brows, hair | Taxable (10% GST) |
| PM Spa Packages (Pkg 1/2/3, standalone) | Taxable (10% GST) |
| Spray tan, retail, cafe | Taxable (10% GST) |

**CF-06 resolved Day 50:** all revenue/cost figures above are GST-inclusive (as invoiced/paid) — consistent treatment throughout. Net GST position (output GST on taxable wellness/retail supplies less input GST credits on costs) is a BAS/balance-sheet item, not a P&L line, for a GST-registered mixed-supply entity. No separate P&L adjustment required; accountant to confirm exact quarterly net position from Month 1 (GST registration is immediate per `financial-model.md` §1).

### Working Capital Management
- Month 1–3: tight. Ensure A$55,000 working capital reserve held in trust account
- Month 4+: self-funding. Distribute surplus to trust quarterly
- Cash buffer rule: never let operating account fall below A$25,000

### Property Acquisition (Trust)
| Timeline | Action |
|---|---|
| Year 1 | Lease only. Build proof of model. |
| Year 2–3 | YETI Trust purchases suitable commercial property (200–300 sqm). GTT Center Perth pays rent to trust. |
| Indicative Perth commercial property (Subiaco area) | A$1.2M–A$2.5M. Rental yield 6–7%. Rent income A$84K–175K/year covers mortgage. |

---

## MODEL LIMITATIONS & ASSUMPTIONS TO VERIFY

1. **Rent estimate (A$8,000/month):** Based on Perth commercial market June 2026. Verify with local agent before committing.
2. **Avg package price (A$250, 30/40/30 Package 1/2/3 mix):** Will shift based on actual booking mix — track weekly from Day 1, especially the Package 1 vs Package 3 ratio (A$50 swing either side of A$250 moves the model meaningfully — see `financial-break-even-staff.md` Sensitivity).
3. **Volume ramp:** 300+ waitlist target requires consistent social media execution during fit-out. Model assumes this is achieved.
4. **PM Spa Package ramp to 6/day by Month 5:** the single biggest assumption in this model (Months 1–4 = 2/3/4/5 packages/day). If the PM Service Therapist's afternoon book fills more slowly, Months 4 onward stay loss-making until it does — see `financial-break-even-staff.md` Lever 2.
5. **WDP accreditation timeline:** WDP site inspection takes 4–8 weeks after application. Do not open GTT services until accreditation confirmed.
6. **GST split:** Requires qualified accountant setup in Xero from Day 1. Do not attempt DIY.
7. **Award rate increases:** Fair Work Commission reviews award rates annually (usually effective 1 July). Budget for 3–5% wage increase Year 2.

---

*Document owner: Bruno (Finance & Bookkeeping) | Reviewed by: Grace (Operations Manager)*  
*Next review: Month 3 actuals vs model*

---

## Changelog

**2026-07-19 (Phase 6 verification)** — Confirmed this document meets the required spec granularity (monthly cash flow through Year 1+, startup capital outlay through break-even — see the 18-Month Month-by-Month table and Pre-Launch Capital Deployment table above). However, found via cross-document verification that this entire file is built on the superseded 8-client Scenario B model and 3-package structure, and that its own supersession banner pointed to `pm-staffing-roster.md` as authoritative — which is itself superseded by `profit-loss-tables.md` v2.0's current 10-client Scenario C figures. Added a further-update note above documenting this three-way discrepancy. Not rewritten this session (a full rebuild under the current model is a substantial task, recommended as a priority follow-up — see `docs/04_roadmap_next_steps.md` and `docs/01_conflicts_log.md`).
