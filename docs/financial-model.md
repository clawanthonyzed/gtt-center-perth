# GTT Center Perth — Financial Model

**Version:** 2.0 | **Date:** 2026-06-11 | **Author:** Idea Lobster
**Status:** Day 51 package-price model. Canonical figures live in `cash-flow.md` (18-month P&L) and `financial-break-even-staff.md` (staffing, break-even, sensitivity). This document covers business structure, the confirmed commercial model, and trust tax treatment.

---

> **Day 51 rewrite — Option A removed.** Earlier versions of this document (through v1.3) ran a side-by-side comparison of Option A (venue-fee + subtenant room rental, RECOMMENDED at the time) vs Option B (full package, employed staff). Anthony confirmed Option B on 2026-06-05 and, on Day 51, locked the package structure at Package 1/A$200, Package 2/A$250, Package 3/A$300 (`services-pricing-locked.md`), removed all subtenants (3D scan operator, dietitian) from scope, and confirmed Option B as the ONLY model going forward. Option A, the old Relax/Restore/Glow/Complete package set (A$145–360), and the side-by-side comparison have been removed entirely — the full pre-Day-51 analysis remains available in git history.

---

## 1. BUSINESS STRUCTURE

**Operating entity:** YETI Holding Trust (discretionary trust)
**Corporate trustee:** YETI Tipi Holdings PTY LTD
**Trading name:** GTT Center Perth
**ABN registration:** Under trust — confirm new ABN or existing covers this trading activity
**GST:** Must register (turnover will exceed A$75K threshold immediately)
**Revenue protection:** All revenue stays in trust. Does NOT flow to Anthony personally. TPI pension is protected.

**Proposed 30% trust-distribution tax (national budget, not yet legislated):** if enacted, a flat 30% tax would apply to trust distributions before they reach beneficiaries. See §3 below for the illustrative post-tax impact on this model's Year 1/Year 2 figures, and `cash-flow.md` Tax Treatment section for the same note applied to the 18-month P&L.

---

## 2. CONFIRMED MODEL — WAGE EMPLOYMENT, IN-HOUSE GTT, PACKAGE PRICING

**Decided 2026-06-05, package structure locked Day 51 (2026-06-11) by Anthony.**

### Confirmed Decisions
- **Staff model:** all service delivery staff employed directly by YETI Holding Trust (12 roles + Casual Relief Pool — no subtenants, no sublease income)
- **GTT model:** 2 phlebotomists employed from Day 1, operating under WDP/PathWest NATA accreditation umbrella, 2 collection chairs (Scenario B verified timetable, 8 GTT clients/day cap)
- **Commercial model:** full package sales — GTT Center Perth prices and collects 100% of revenue, no room rent, no per-session subtenant payments
- **Packages (structure locked, prices negotiable):** Package 1 = A$200 (2 × 30-min services), Package 2 = A$250 (1×30-min + 1×45-min), Package 3 = A$300 (2 × 45-min). Venue + lounge access bundled FREE into all 3 — no separate fee, no lounge-only option. 30/40/30 mix → blended avg **A$250/visit**, applied identically to AM GTT visits and standalone PM Spa Packages (`services-pricing-locked.md`)
- **3D keepsake scan + dietitian:** removed from scope entirely (Day 51) — no equipment, no contracts, no subtenant revenue. See `services-pricing-locked.md` FUTURE SERVICES for IBCLC (Month 4+) as the only retained future contractor role

### Staffing & Payroll
Full Award Wage Summary, Total Annual Payroll, and Shift Structure (CF-01) are canonical in `financial-break-even-staff.md`. Headline:
- 12 employed roles (incl. 1 new PM Service Therapist hire, replacing the removed 3D scan operator) + A$15,000/yr Casual Relief Pool for sick/leave cover
- **Total Annual Payroll: A$713,067/yr** (A$59,422/month average)
- Receptionist/Manager works a split shift (AM 07:00–12:00 + PM 15:00–18:00) — same role, no new hire

### Full Monthly P&L
Full 18-month ramp is canonical in `cash-flow.md`. Headline (Month 5+, steady state — both AM at 8 GTT/day and PM at 6 Spa Packages/day):

| Line | Monthly | Annual |
|---|---|---|
| Total Revenue | A$84,623 | A$1,015,476 |
| Total Fixed Costs | A$74,391 | A$892,694 |
| **Net P&L** | **+A$10,232** | **+A$122,784** |

Year 1 (M1–M12, including ramp-up losses) Net: **+A$37,232**. Months 1–3 are loss-making during ramp-up; Month 4 is marginally positive (+A$4,188); Month 5+ is flat profitable once both AM and PM capacity ceilings are reached.

### Break-Even
~298 visits/month (13.5/day) at A$250 avg package price (A$74,391 ÷ A$250) — see `cash-flow.md` Ramp-Up Traffic Model. The PM Spa Package ramp to 6/day by Month 5 is the model's single biggest assumption (`financial-break-even-staff.md` Lever 2); the Sensitivity table there gives the price-based fallback if PM volume underperforms.

---

## 3. TRUST STRUCTURE — TAX TREATMENT

### TPI Protection (Non-Negotiable)
Anthony cannot receive this income personally — TPI pension compliance requires it. Trust structure is **mandatory regardless of tax efficiency**. The question is only how to optimise within the trust.

### Tax Comparison — Year 1 (A$37,232 net, pre-tax)

| Structure | Tax | After-tax |
|---|---|---|
| Trust → distribute to Imara (sole income, no salary) | ~A$6,700 (avg ~18%) | ~A$30,530 |
| PTY LTD company (25% base rate) | ~A$9,310 | ~A$27,920 |
| Trust → distribute to Imara (earns A$60K salary too, marginal ~37%) | ~A$13,780 | ~A$23,450 |
| **If 30% flat trust-distribution tax enacted** | ~A$11,170 | ~A$26,060 |

### Tax Comparison — Year 2 (A$122,784 net, pre-tax)

| Structure | Tax | After-tax |
|---|---|---|
| Trust → distribute to Imara (sole income, no salary) | ~A$31,920 (avg ~26%) | ~A$90,860 |
| PTY LTD company (25%) | ~A$30,700 | ~A$92,090 |
| Trust → split between Imara + one other low-income beneficiary | ~A$18,500–22,500 | ~A$100,300–104,300 |
| Trust → distribute to Imara (earns A$60K salary from trust) | ~A$41,000 on distribution alone | ~A$81,780 |
| **If 30% flat trust-distribution tax enacted** | ~A$36,840 | ~A$85,950 |

### Findings

1. **Year 1 (A$37K):** trust-direct to Imara (sole income) is most efficient — lowest tax, no company setup/accounting overhead.
2. **Year 2 (A$123K):** trust-direct and PTY LTD are roughly equal; splitting between Imara and a second low-income beneficiary is most efficient if eligible beneficiaries exist.
3. **If the proposed 30% flat trust-distribution tax is enacted:** it becomes the WORST option at Year 2 profit levels (worse than both trust-direct-to-Imara and PTY LTD) — an operating PTY LTD under the trust (25% company rate, retain-and-reinvest) becomes clearly preferable once this passes. Build for this now per Anthony's instruction; do not wait for legislation to pass before planning the structure.
4. **Imara's salary vs distribution:** accountant must model the split. A reasonable salary for an owner-operator of a wellness venue is A$55–75K. Everything above that can stay in trust or company.

### Structure Recommendation

**NOTE — 2026-07 UPDATE:** Imara returns to full-time employment from April 2026 (maternity leave ended). Tax rows above assuming "sole income" are no longer applicable — she has her own salary income. Accountant must remodel distributions for her new employment income bracket. Consult accountant before distributing trust income.

**Now (2026):** YETI Trust trades directly. Distribute to Imara (and/or other family beneficiaries at accountant's advice) — most tax-efficient at current Year 1/Year 2 projected profit levels.

**If/when 30% trust-distribution tax is legislated:** add an operating PTY LTD under the trust before the effective date. Re-run §3 with the legislated rate/threshold once known.

---

## 4. DECISION CHECKLIST

| Decision | Status | Reference |
|---|---|---|
| Commercial model | DECIDED — Option B (full package, employed staff, no subtenants) | Decided 2026-06-05 |
| Package pricing | DECIDED — Package 1/A$200, Package 2/A$250, Package 3/A$300 (structure locked, prices negotiable) | `services-pricing-locked.md`, Day 51 |
| 3D scan + dietitian | DECIDED — removed from scope entirely | Day 51 |
| Trust structure 2026 | Trust direct — review if 30% trust-distribution tax legislated | §3 above |
| Imara salary vs distribution | OPEN — accountant brief required before first revenue | §3 above |
| GST registration | Required immediately — register before first booking | §1 above |
| Pathology fee structure (PathWest/WDP) | OPEN — contact before finalising package pricing | `services-pricing-locked.md` |
| PM Spa Package ramp to 6/day by Month 5 | OPEN — single biggest assumption in the model | `financial-break-even-staff.md` Lever 2, `cash-flow.md` |

---

## Sources
- [Fair Work Commission — Hair & Beauty Award MA000005](https://www.fairwork.gov.au/employment-conditions/awards/awards-summary/ma000005-summary)
- [Fair Work Commission — Clerks Award MA000002](https://www.fairwork.gov.au/employment-conditions/awards/awards-summary/ma000002-summary)
- [ATO — Trust taxation](https://www.ato.gov.au/individuals-and-families/investments-and-assets/trusts)
- [ATO — Company tax rates](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-concessions-and-incentives/lower-tax-rate-for-small-companies)
- [ASIC — Business name registration](https://asic.gov.au/for-business/registering-a-business-name/)
- Commercial rent estimates: Perth metro, wellness/health use, 100–140 sqm
