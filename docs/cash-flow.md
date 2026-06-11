# GTT Center Perth — 18-Month Cash Flow Projection
## YETI Holding Trust | GTT Center Perth trading entity
### Version 1.0 | June 2026

---

## ⚠ DAY 50 RECONCILIATION

This model has been reconciled to the Day-49 12-staff payroll model (`financial-break-even-staff.md` v2.0). The previous fixed-cost base of A$39,523/month was built on a 6-staff pre-Day-49 structure (1 phlebotomist, Imara as MD, 11.5% super) and is superseded. The new fixed-cost base is **A$71,236/month** (12-staff payroll @ A$675,589/yr incl. 12% super, 2 phlebotomists — see Cost Assumptions below). At the same time, three ancillary revenue streams already counted in `financial-break-even-staff.md` v2.0's Revenue Model (spray tan, retail, cafe = +A$8,167/month combined) were missing here — these are unlocked by the CF-01 afternoon AM/PM shift design (no new hires, see `financial-break-even-staff.md` v2.0 §Shift Structure). Net effect: stable-month profit falls from A$29,192 to **A$5,646/month**, and capital recovery moves from ~Month 8–13 to **~Month 22+** (mid-estimate ~Month 34). The venture remains profitable but margins are materially thinner — see SUMMARY METRICS and SENSITIVITY ANALYSIS below. Cross-ref: `review-audit.md` CF-01/CF-04/CF-05/CF-06, IC-01/IC-04/IC-06/IC-07.

---

## Model Assumptions

### Revenue Assumptions
| Parameter | Value | Basis |
|---|---|---|
| Morning GTT package avg | A$225 | 10% GTT Lounge (A$25) / 70% GTT Wellness (A$225) / 20% GTT Luxe (A$325) mix = (0.10×25)+(0.70×225)+(0.20×325) = **A$225** — identical to prior blended figure, no recalculation needed elsewhere. See `financial-break-even-staff.md` v2.0 Package Pricing Model. |
| Afternoon wellness avg | A$175 | Blended: Single service A$120–165 (70%), multi-service A$200–250 (30%) |
| Morning GTT wave capacity | 8 patients/day (2 phlebotomists, 2 chairs, Day 1) | RESOLVED Day 49 — 2 phlebotomists/2 collection chairs from Day 1, corrected draw-timing pathway. See operations-manual.md for the verified timetable (review-audit.md CF-02 resolved) |
| Afternoon capacity | 6–8 visits/afternoon | Requires full-time staff (see review-audit.md CF-01) |
| Operating days/month | 22 days (Mon–Fri, 4.4 weeks) | Closed Sat–Sun. Saturday requires penalty rates — not in current model. |
| Subtenant income (Bloom Baby scan) | A$1,500/month | 3 days/week × A$500/day |
| Subtenant income (dietitian) | A$665/month | 2.5 days/week × A$266/half-day |
| Total subtenant income | A$2,165/month | Fixed from Month 3 (operational) |
| Spray tan (ancillary) | A$4,833/month | A$58,000/yr ÷ 12 — see `financial-break-even-staff.md` v2.0 Revenue Model |
| Retail (ancillary) | A$2,083/month | A$25,000/yr ÷ 12 — see `financial-break-even-staff.md` v2.0 Revenue Model |
| Cafe (ancillary) | A$1,250/month | A$15,000/yr ÷ 12 — see `financial-break-even-staff.md` v2.0 Revenue Model |
| **Total ancillary revenue** | **A$8,167/month** | Available from Month 1 — staffed via CF-01 afternoon-shift model (no new hires), ramps with afternoon-visit ratio (see 18-month table below) |

### Cost Assumptions — Fixed Monthly (Stable Operations)
| Line Item | Monthly | Basis |
|---|---|---|
| Payroll (12 staff, incl. 12% super) | A$56,299 | A$675,589/yr ÷ 12 — see `financial-break-even-staff.md` v2.0 Total Annual Payroll |
| Workers comp (WA, ~1.7% of payroll) | A$957 | Scaled from old A$380/A$22,575 ratio |
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
| **TOTAL FIXED + SEMI-FIXED** | **A$71,236** | A$854,832/yr |

**Footnote:** This granular non-wage total (A$13,980/mo = A$167,760/yr — rent through misc, excluding payroll/workers comp) is more detailed than `financial-break-even-staff.md`'s "~A$100,000/yr" rough overhead estimate. `financial-break-even-staff.md` v2.0 has been updated to cross-reference this table as canonical.

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

| Month | GTT visits/day | Wellness visits/day | Total visits/day | Operating days | Total visits |
|---|---|---|---|---|---|
| Month 1 (soft open) | 4 | 4 | 8 | 22 | 176 |
| Month 2 | 6 | 5 | 11 | 22 | 242 |
| Month 3 | 7 | 6 | 13 | 22 | 286 |
| Month 4+ (stable) | 8 | 7 | 15 | 22 | 330 |
| Year 2 avg (growth) | 9 | 8 | 17 | 22 | 374 |

~~Break-even = 108 visits/month ≈ 5 visits/day. Month 1 already exceeds break-even.~~ **Updated Day 50:** post-reconciliation, operational break-even (fixed costs covered) is reached at Month 4 (~330 visits/month total) — see SUMMARY METRICS below. Month 1 (176 visits) through Month 3 (286 visits) do not yet cover the new A$71,236/month fixed-cost base.

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
- Morning GTT revenue = GTT visits × A$225 avg
- Afternoon wellness revenue = Wellness visits × A$175 avg
- Subtenant income = A$2,165/month (from Month 3)

### Cost Formula (Monthly)
- Fixed costs = A$71,236/month (stable operations from Month 3+; ramps at 90%/95% Months 1-2, +A$477 from Month 8, +A$2,477 from Month 13 — same ramp shape as before, applied to new base)
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

| Month | GTT Visits | Wellness | Total Visits | GTT Rev | Wellness Rev | Subtenant | Ancillary | **Total Revenue** | Fixed Costs | **Net P&L** | Cumulative |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **M1** | 88 | 88 | 176 | A$19,800 | A$15,400 | — | A$4,666 | **A$39,866** | A$64,112 | **A$(24,246)** | A$(173,746) |
| **M2** | 132 | 110 | 242 | A$29,700 | A$19,250 | — | A$5,834 | **A$54,784** | A$67,674 | **A$(12,890)** | A$(186,636) |
| **M3** | 154 | 132 | 286 | A$34,650 | A$23,100 | A$2,165 | A$6,999 | **A$66,914** | A$71,236 | **A$(4,322)** | A$(190,958) |
| **M4** | 176 | 154 | 330 | A$39,600 | A$26,950 | A$2,165 | A$8,167 | **A$76,882** | A$71,236 | **A$5,646** | A$(185,312) |
| **M5** | 176 | 154 | 330 | A$39,600 | A$26,950 | A$2,165 | A$8,167 | **A$76,882** | A$71,236 | **A$5,646** | A$(179,666) |
| **M6** | 176 | 154 | 330 | A$39,600 | A$26,950 | A$2,165 | A$8,167 | **A$76,882** | A$71,236 | **A$5,646** | A$(174,020) |
| **M7** | 176 | 154 | 330 | A$39,600 | A$26,950 | A$2,165 | A$8,167 | **A$76,882** | A$71,236 | **A$5,646** | A$(168,374) |
| **M8** | 185 | 165 | 350 | A$41,625 | A$28,875 | A$2,165 | A$8,750 | **A$81,415** | A$71,713 | **A$9,702** | A$(158,672) |
| **M9** | 185 | 165 | 350 | A$41,625 | A$28,875 | A$2,165 | A$8,750 | **A$81,415** | A$71,713 | **A$9,702** | A$(148,970) |
| **M10** | 185 | 165 | 350 | A$41,625 | A$28,875 | A$2,165 | A$8,750 | **A$81,415** | A$71,713 | **A$9,702** | A$(139,268) |
| **M11** | 185 | 165 | 350 | A$41,625 | A$28,875 | A$2,165 | A$8,750 | **A$81,415** | A$71,713 | **A$9,702** | A$(129,566) |
| **M12** | 185 | 165 | 350 | A$41,625 | A$28,875 | A$2,165 | A$8,750 | **A$81,415** | A$71,713 | **A$9,702** | A$(119,864) |
| | | | | | | | | | | | |
| **M13** | 198 | 176 | 374 | A$44,550 | A$30,800 | A$2,165 | A$9,334 | **A$86,849** | A$73,713 | **A$13,136** | A$(106,728) |
| **M14** | 198 | 176 | 374 | A$44,550 | A$30,800 | A$2,165 | A$9,334 | **A$86,849** | A$73,713 | **A$13,136** | A$(93,592) |
| **M15** | 198 | 176 | 374 | A$44,550 | A$30,800 | A$2,165 | A$9,334 | **A$86,849** | A$73,713 | **A$13,136** | A$(80,456) |
| **M16** | 198 | 176 | 374 | A$44,550 | A$30,800 | A$2,165 | A$9,334 | **A$86,849** | A$73,713 | **A$13,136** | A$(67,320) |
| **M17** | 198 | 176 | 374 | A$44,550 | A$30,800 | A$2,165 | A$9,334 | **A$86,849** | A$73,713 | **A$13,136** | A$(54,184) |
| **M18** | 198 | 176 | 374 | A$44,550 | A$30,800 | A$2,165 | A$9,334 | **A$86,849** | A$73,713 | **A$13,136** | A$(41,048) |

---

## SUMMARY METRICS

### Payback Period
| Scenario | Startup Capital | Month Breakeven Ops | Month Capital Recovered |
|---|---|---|---|
| Low (A$209K) | A$209,000 | Month 4 | ~Month 27 |
| Mid (A$305K) | A$305,000 | Month 4 | ~Month 34 |
| High (A$431K) | A$431,000 | Month 4 | ~Month 44 |

**Operational break-even (monthly costs covered): Month 4** (was "Month 1" under the pre-reconciliation cost base — no longer true under the new A$71,236/month fixed-cost base)  
**Capital recovery (against Month-0 baseline of A$149,500): ~Month 22** (cumulative crosses zero between M21 ≈ A$(1,640) and M22 ≈ +A$11,496, continuing at the M13–M18 run-rate of +A$13,136/month). For full startup capital (incl. working capital), see Payback Period table above.

### Annual P&L Summary
| Period | Revenue | Costs | Net Profit |
|---|---|---|---|
| Year 1 (M1–M12) | A$876,167 | A$846,531 | **A$29,636** |
| Year 2 (M13–M18 annualised ×2) | A$1,042,188 | A$884,556 | **A$157,632** |

### Key Milestones
| Milestone | Target |
|---|---|
| Pre-launch Instagram live | Week 9 (fit-out start) |
| 100 waitlist signups | Week 13 |
| 300 waitlist signups | Week 18 |
| Soft open (reduced capacity) | Week 20 |
| Full open (all services live) | Month 1 + 2 weeks |
| Break-even operations | Month 4 (post-reconciliation — see Day 50 Reconciliation note above) |
| Subtenant income live | Month 3 |
| Full capacity (15 visits/day) | Month 4 |
| Capital recovery (mid estimate) | ~Month 34 (mid estimate, post-reconciliation) |
| Second phlebotomist | RESOLVED Day 49 — both phlebotomists hired pre-launch (Day 1), not a Month 6 trigger. See financial-break-even-staff.md |
| Property purchase evaluation | Month 18 (Year 2–3 if rent+proof of model) |

---

## SENSITIVITY ANALYSIS

### Revenue Sensitivity (Stable Month — 330 GTT/Wellness visits at A$225/A$175 avg, plus A$8,167 ancillary)

| Scenario | Monthly Revenue | Monthly Costs | Monthly Profit | Annual Profit |
|---|---|---|---|---|
| Bear (70% capacity, no afternoon/ancillary) | A$34,650 | A$71,236 | A$(36,586) | A$(439,032) |
| Base (100% as modelled, incl. ancillary) | A$76,882 | A$71,236 | A$5,646 | A$67,752 |
| Bull (120% utilisation) | A$92,258 | A$72,736 | A$19,522 | A$234,264 |

### Cost Sensitivity — Rent Variation (at base revenue A$76,882)
| Rent Scenario | Monthly Rent | Monthly Profit |
|---|---|---|
| Low (Osborne Park, A$5,500) | A$5,500 | A$8,146 |
| Base (Subiaco/Nedlands, A$8,000) | A$8,000 | A$5,646 |
| High (CBD adjacent, A$12,000) | A$12,000 | A$1,646 |

**Insight:** Profitability now starts Month 4, not Month 1. At high-rent locations the margin is thin (A$1,646/month) — location choice (see Open Decisions / Quinn research) materially affects viability.

### Break-Even Visits (at different avg package prices)
| Avg Package | Break-Even Visits/Month | Break-Even Visits/Day |
|---|---|---|
| A$180 (conservative) | 350 | 15.9 |
| A$225 (base model) | 280 | 12.7 |
| A$260 (premium tier dominant) | 243 | 11.0 |

Modelled stable-state volume is 15 visits/day — above break-even at A$225 (12.7/day) but below break-even at A$180 (15.9/day). Pricing discipline (GTT Wellness A$225 default tier) matters.

---

## CASH FLOW NOTES

### Tax Treatment (YETI Holding Trust)
- GTT Center Perth trading profits flow to YETI Holding Trust as trust income
- Trustee (YETI Tipi Holdings PTY LTD) distributes to beneficiaries each financial year
- Anthony's TPI pension: trust distributions are separate income — consult accountant on pension interaction
- GST: GTT medical test (GST-free supply under GSTD 2004/6). Wellness services: standard-rated 10% GST applies
- Important: mixed supply entity — requires split GST accounting in Xero

### GST Note
| Service | GST Status |
|---|---|
| GTT (pathology collection) | GST-free (medical) |
| Massage, facials, nails, brows | Taxable (10% GST) |
| Subtenant rental income | Taxable (10% GST) |
| 3D ultrasound scan (Bloom Baby) | Input-taxed or GST-free — Bloom Baby's obligation |

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
2. **Avg package price (A$225 GTT, A$175 wellness):** Will shift based on actual booking mix. Track weekly from Day 1.
3. **Volume ramp:** 300+ waitlist target requires consistent social media execution during fit-out. Model assumes this is achieved.
4. **Subtenant income (Month 3):** Bloom Baby scan and dietitian contracts must be signed before model is valid.
5. **WDP accreditation timeline:** WDP site inspection takes 4–8 weeks after application. Do not open GTT services until accreditation confirmed.
6. **GST split:** Requires qualified accountant setup in Xero from Day 1. Do not attempt DIY.
7. **Award rate increases:** Fair Work Commission reviews award rates annually (usually effective 1 July). Budget for 3–5% wage increase Year 2.

---

*Document owner: Bruno (Finance & Bookkeeping) | Reviewed by: Grace (Operations Manager)*  
*Next review: Month 3 actuals vs model*
