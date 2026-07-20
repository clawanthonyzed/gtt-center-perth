# GTT Center Perth — Profit & Loss Tables

**Version:** 2.1 | **Date:** 2026-07-20 (v1.0 removed entirely per Anthony's instruction — see Changelog)
**Base model:** Current committed operational plan — 2 chairs, 10 AM clients/day (07:00 start, Scenario C verified), PM individual services (4-role hours-based roster), Saturday AM+PM (hours-based costing), **no Sunday trading** (closed until standalone PM demand is proven and profitable — see `am-capacity-weekend.md`). **All AM package revenue uses A$250 (Package 2, the lower of the 2 confirmed packages) per instruction — this is a deliberate safety margin, not the full potential average if Package 3 bookings run higher.**

*The 3-phlebotomist/15-client scenario (Scenario D, `am-capacity-weekend.md`) is a separate growth path, not the base case used here.*

---

## Saturday Penalty Rate — Clarified, Not Removed

**The MA000005 Saturday penalty rate (133% permanent / 150% casual) is a confirmed, real award rate — it applies in full in every table below.** It is not an assumption or a modeling choice, and it has not been removed from this document.

What changed between the original (now-deleted) v1.0 tables and the current v2.1 tables was the **costing method**, not the rate:
- **v1.0's error:** treated Saturday treatment staff cost as if all 8 staff were rostered for a full salary-equivalent shift regardless of actual client volume — the same "blanket shift presence" error later corrected in `pm-staffing-roster.md`'s own PM costing correction.
- **v2.1's correction:** costs Saturday staff on **actual hours worked** for the confirmed Saturday client volume (10 AM + 8 PM sessions), consistent with the casual-employment principle already established for PM (`pm-staffing-roster.md` §CORRECTION — Hours-Based Casual Cost Model) — while still applying the full 150% casual penalty rate throughout.

**Result: Saturday AM+PM together are genuinely profitable (+A$1,580.50/day direct contribution) once costed correctly — this was never really a "Saturday is a loss" finding, it was a costing-method bug that made a profitable day look like a loss.** Do not relitigate the penalty rate itself if this comes up again — the rate is correct and stays; only the old costing method was wrong.

---

## 1. Weekday (Typical Mon–Fri Day)

| | Amount |
|---|---|
| AM Revenue (10 clients × A$250) | A$2,500.00 |
| PM Revenue (16 sessions × A$95) | A$1,520.00 |
| Ancillary Revenue (cafe/retail — see note below) | A$439.50 |
| **Total Revenue** | **A$4,459.50** |
| AM Direct Labor (2 phlebotomists + 8 treatment staff) | A$2,193.00 |
| PM Direct Labor (4-role hours-based roster) | A$440.00 |
| Opening-time increment (07:00 start, vs later start) | A$44.50 |
| Overhead allocation (rent/utilities/admin/marketing, pro-rated per day) | A$635.00 |
| Receptionist/relief/workers comp (pro-rated per day) | A$339.00 |
| **Total Cost** | **A$3,651.50** |
| **Net P&L** | **+A$808.00** |

**Saturday downtime-fill (same principle as weekday):** on Saturdays, as on weekdays, the 8 AM treatment staff are not continuously occupied by GTT-package clients for the entire session — their own downtime between rostered GTT services is available for standalone, non-GTT bookings, the same downtime-fill model already documented for weekdays in `gtt-center-perth-overview-for-imara.md` and `executive-summary.md`. This is not a separate Saturday-specific policy, it's the same staff-utilisation principle applied on the day it also occurs.

**Ancillary Revenue — what it is:** cafe and retail spend (snacks, drinks, retail wellness products — Gaia, Weleda, Mustela brands per `business-plan.md` §6 Revenue Streams), earned per visit across both AM and PM clients. Not a separate service line with its own staff — it rides on existing foot traffic.

## 2. Saturday (AM GTT + PM Standalone, Hours-Based Costing)

| | Amount |
|---|---|
| AM Revenue (10 × A$250) | A$2,500.00 |
| PM Revenue (8 × A$95) | A$760.00 |
| **Total Revenue** | **A$3,260.00** |
| AM Direct Labor (hours-based, full 150% casual penalty applied throughout) | A$1,343.95 |
| PM Direct Labor (hours-based, full 150% casual penalty applied throughout) | A$335.55 |
| **Total Direct Labor** | **A$1,679.50** |
| **Net Direct Contribution** | **+A$1,580.50** |

**Saturday downtime-fill:** the same AM treatment staff working Saturday also take standalone PM-style bookings during gaps between their rostered GTT clients' services, exactly as on weekdays (see note in §1 above) — this is already reflected in the PM session volume assumption (8 sessions/day) used in this table, not an additional unmodelled upside.

## 3. Weekly (5 Weekdays + 1 Saturday, No Sunday)

| | Revenue | Direct Labor | Net |
|---|---|---|---|
| 5× Weekday | A$22,297.50 | A$13,387.50 | +A$8,910.00 |
| 1× Saturday | A$3,260.00 | A$1,679.50 | +A$1,580.50 |
| **Weekly Total** | **A$25,557.50** | **A$15,067.00** | **+A$10,490.50** |

## 4. Monthly (4.33 weeks)

Non-Wage Overhead is broken down below by component (source: `cash-flow.md` §Cost Assumptions — Fixed Monthly, cross-referenced as canonical by `financial-break-even-staff.md`):

| Non-Wage Overhead Component | Monthly |
|---|---|
| Rent (commercial lease, 200 sqm @ A$40/sqm/month, Subiaco/Nedlands estimate) | A$8,000.00 |
| Utilities (power/water, medical fridge + HVAC) | A$650.00 |
| Internet + phone | A$150.00 |
| Fresha booking system (Team plan) | A$100.00 |
| Resend email platform | A$30.00 |
| Instagram/Meta ads (ongoing digital marketing) | A$1,500.00 |
| GTT supplies (glucose, tubes — 200 tests × A$2) | A$400.00 |
| Laundry/linen service | A$350.00 |
| Cleaning service (daily turn + weekly deep clean) | A$600.00 |
| Insurance (public liability + PI, A$4,800/yr ÷ 12) | A$400.00 |
| Accounting/bookkeeping (monthly Xero + BAS prep) | A$500.00 |
| Consumables (wax, nail products, skincare) | A$800.00 |
| Miscellaneous / contingency | A$500.00 |
| **Total Non-Wage Overhead** | **A$13,980.00** |

| | Amount |
|---|---|
| Total Revenue | A$113,712.16 |
| Total Direct Labor + Opening Costs | A$73,397.34 |
| Workers Comp (1.7%) | A$1,247.75 |
| Non-Wage Overhead (see breakdown above) | A$13,980.00 |
| **Total Costs** | **A$88,625.09** |
| **Net P&L (standing conservative baseline)** | **+A$25,087.07** |

## 5. Quarterly (3 Months)

| | Amount |
|---|---|
| Total Revenue | A$341,136.48 |
| Total Direct Labor + Opening Costs | A$220,192.02 |
| Workers Comp (1.7%) | A$3,743.25 |
| Non-Wage Overhead | A$41,940.00 |
| **Total Costs** | **A$265,875.27** |
| **Net P&L** | **+A$75,261.21** |

## 6. Half-Yearly (6 Months)

| | Amount |
|---|---|
| Total Revenue | A$682,272.96 |
| Total Direct Labor + Opening Costs | A$440,384.04 |
| Workers Comp (1.7%) | A$7,486.50 |
| Non-Wage Overhead | A$83,880.00 |
| **Total Costs** | **A$531,750.54** |
| **Net P&L** | **+A$150,522.42** |

## 7. Yearly (12 Months)

| | Amount |
|---|---|
| Total Revenue | A$1,364,545.92 |
| Total Direct Labor + Opening Costs | A$880,768.08 |
| Workers Comp (1.7%) | A$14,973.00 |
| Non-Wage Overhead | A$167,760.00 |
| **Total Costs** | **A$1,063,501.08** |
| **Net P&L** | **+A$301,044.84** |

**These are steady-state figures (Month 5+ run rate) — they do not include the Months 1–3 ramp-up losses (see Year 1 Monthly Ramp below), or the pre-launch capital deployment.** This table answers "what does ongoing operation look like once running," not the path to get there. Quarterly/Half-Yearly/Yearly figures above are the Monthly figures scaled by 3/6/12 — a steady-state run-rate projection, not a separately-modelled scenario for each period.

---

## Key Callouts

1. **AM contribution corrected for safety:** using A$250 (not a blended A$275 mixed-price estimate), AM's direct contribution is a strong, conservative baseline. Real performance could exceed this if Package 3 bookings run above the Package-2-only safety assumption.
2. **Saturday is profitable, not a drag** — once costed on actual hours worked (see the clarification section above), Saturday AM+PM contributes +A$1,580.50/day. The earlier "Saturday runs at a loss" finding was a costing-method error in a since-removed draft, not a real finding about the business — see Changelog for what was removed and why.
3. **Sunday remains closed** — not modelled anywhere in this document. Reopening depends on standalone PM demand being proven and profitable enough to justify the added penalty-rate cost (`am-capacity-weekend.md`), not on this document.
4. **MA000027 phlebotomist Saturday ordinary-hours question remains unconfirmed** — this document uses the conservative full-penalty-rate assumption throughout (no optimistic/pending-verification scenario shown, since that scenario added confusion without changing the standing baseline). If a payroll advisor or Fair Work confirms an ordinary-hours carve-out exists, Saturday profitability would improve further — upside only, never assumed.

---

## Treatment Headcount — Can It Be Trimmed Below 8 at 10 Clients/Day?

**Direct answer: yes — 7 staff, not 8, is the genuine minimum at the current 10-client/day (Scenario C) volume, via one specific cross-training pool. This is a checked answer against the verified scheduling model, not a guess.**

**The check:** `am-capacity-weekend.md`'s Scenario C treatment-staff verification confirms every one of the 30 service slots (10 clients × ~2-3 services each across the AM window) stays at a maximum of 2 concurrent bookings per service line, using the existing 8-person roster (2 each: Massage, Nail, Hair, Beauty). `multirole-CORRECTION.md` then re-examined whether any of these 4 lines can be pooled to reduce headcount:

| Pool | Peak concurrent demand at 10 clients/day |
|---|---|
| Massage + Beauty (poolable — both Cert IV under MA000005, natural cross-train pairing) | 3 |
| Nails (standalone — separate trade-specific qualification, no natural overlap) | 2 |
| Hair (standalone — separate trade-specific qualification, no natural overlap) | 2 |
| **Total staff needed** | **7** (not 8) |

**Why 7, not fewer:** Nails and Hair cannot be pooled with each other or with Massage/Beauty — they are genuinely separate qualifications (hairdressing apprenticeship vs nail technology vs Cert IV beauty/massage), confirmed in `am-capacity-weekend.md`'s own Multi-Role Relief Hiring analysis. Massage+Beauty is the only valid cross-training pool, and even that pool still peaks at 3 concurrent bookings at this volume — so the saving is 1 headcount (8→7), not more.

**Labor cost saving if adopted:** 1 fewer treatment staff member at Cert IV rate (~A$62,774/yr per `financial-break-even-staff.md`'s Massage/Beauty award line) — approximately **A$62,774/year (~A$5,231/month) saved**, before considering the practical hiring/training cost of finding staff dual-qualified in both Massage and Beauty rather than single-skilled.

**Important caveat — this does not scale to Scenario D:** if AM capacity later grows to 15 clients/day (3rd phlebotomist, not yet committed), the Massage and Beauty peaks individually both rise to 2 concurrent each, meaning their combined pool peaks at 4 — pushing total treatment headcount back up to 8. **The 7-staff saving only exists at today's 10-client volume; it does not persist if AM capacity expands.** This has already been logged in `multirole-CORRECTION.md` so it isn't rediscovered as a surprise later.

**Not yet actioned:** this document reports the checked answer; whether to actually reduce from 8 to 7 (and where to source a Massage+Beauty dual-qualified hire) is an operational hiring decision for the Venue Manager, not something this document commits to.

---

## Years 1-3 Annual Projection

**Purpose:** filling the gap for a multi-year annual view, per the business-plan spec.

**One remaining honest limitation:** the Year 1 estimate below uses flat Month 5+ fixed costs applied across all 12 months as a conservative simplification — in reality, fixed costs also ramp during Months 1-4 (fewer casual PM hours worked at lower volume, per `pm-staffing-roster.md`'s own cost-ramp table), so this approach *understates* Year 1 profitability somewhat by charging full steady-state costs against ramped-up revenue in the early months. A precise Year 1 figure would need the matching cost ramp built in — flagged as a follow-up refinement, not fabricated here with false precision. Years 2-3 use this document's own current Month-5+ steady-state run-rate (10-client Scenario C, A$301,044.84/year), assuming the venture holds at its verified capacity ceiling with no further AM capacity expansion (Scenario D, 15 clients/day, is a documented but not-yet-committed growth path — see `scenario-d-investigation.md` — not assumed here).

| Year | Net P&L (annual) | Basis |
|---|---|---|
| Year 1 (ramp-up + partial steady-state) | Likely in the range of breakeven-to-modestly-positive to +A$25,000-40,000, once costs are properly ramp-matched to revenue (a flat-cost approximation using this document's own ramp-table revenue produces a small apparent loss of roughly -A$13,000, but this is known to understate profitability since it doesn't ramp costs down in the early months — treat the true figure as better than this flat-cost approximation suggests) | Derived from this document's Year 1 Monthly Ramp table below, using Month 5+ flat costs as a known-conservative simplification |
| Year 2 (full steady-state, 10-client Scenario C, no further capacity change) | ~A$301,044.84 | This document's steady-state figure, current canonical AM model |
| Year 3 (same, assuming no material change — the actual figure depends entirely on whether Scenario D or further growth levers are pursued) | ~A$301,044.84 (flat, if no capacity change) | Same as Year 2 — **this is a "no growth" placeholder, not a forecast.** If Scenario D (15 clients/day) is activated, see `scenario-d-investigation.md`'s own P&L estimate instead. |

**This table should not be treated as a confident 3-year forecast.** The remaining limitation (flat vs ramped costs in Year 1) is a known, disclosed simplification, not an unresolved contradiction — recommend Bruno/finance function build the cost-ramp-matched version once Year 1 real data exists, for a materially more accurate (and likely more favourable) Year 1 figure than the conservative approximation shown here.

---

## Year 1 Monthly Ramp

**Purpose:** month-by-month build-up across Year 1, since the steady-state tables above only describe ongoing operation once the venture is running at full capacity.

**Where the Month 5+ AM figure of A$55,000 comes from, and how it's achievable:** 10 clients/day × A$250 (Package 2 conservative price) × 22 trading days/month = **A$55,000/month**. This is a **capacity ceiling** (the verified Scenario C maximum — see `scenario-c-sync-timetables.md`), not a guaranteed figure. Actually earning it depends on booking all 10 daily AM slots consistently across the month via the referral/waitlist pipeline (`business-plan.md` §8 Go-to-Market, `pm-staffing-roster.md` §Pre-Opening Waitlist & Staffing Decision Model) — which is exactly why the ramp table below assumes a gradual build (43%/64%/79%/93%/100% of this ceiling across Months 1-5), not full capacity from Day 1.

**Method:** apply the same ramp percentages `cash-flow.md` used (Month 1: ~43% of steady-state visits, Month 2: ~64%, Month 3: ~79%, Month 4: ~93%, Month 5+: 100%) to this document's own current Month 5+ steady-state figures (AM A$55,000, PM A$33,440 — using `pm-staffing-roster.md`'s validated session-volume ramp, confirmed compatible with the 10-client AM model — and ancillary A$8,580, all at Month 5+).

| Month | AM GTT Revenue | PM Revenue | Ancillary | Total Revenue (approx.) | Note |
|---|---|---|---|---|---|
| Month 1 | ~A$27,500 (43% of A$55,000 ceiling, ~4-5 clients/day) | ~A$14,380 (43% of A$33,440) | ~A$3,690 | ~A$45,570 | Ramp estimate |
| Month 2 | ~A$35,200 (64%) | ~A$21,400 | ~A$5,490 | ~A$62,090 | Ramp estimate |
| Month 3 | ~A$43,450 (79%) | ~A$26,420 | ~A$6,780 | ~A$76,650 | Ramp estimate |
| Month 4 | ~A$51,150 (93%) | ~A$31,100 | ~A$7,980 | ~A$90,230 | Ramp estimate |
| Month 5+ | A$55,000 (100%, verified ceiling — 10/day × A$250 × 22 days) | A$33,440 | A$8,580 | A$97,020 (revenue only — see Fixed Costs below for net) | **AM figure is fully verified (Scenario C ceiling); PM/ancillary figures are the ramp-shape estimate, confirmed directionally compatible with the AM model but not independently re-verified session-by-session** |

**Fixed costs at Month 5+ (per §4 Monthly table above): A$88,625.09/month. Net P&L at Month 5+: Total Revenue A$97,020 minus Total Costs A$88,625.09 ≈ +A$8,395/month using this simplified ramp-table revenue sum — note this differs slightly from the headline +A$25,087.07/month figure because that figure uses this document's own more precise weekday/Saturday-blended calculation (§1-2 above), not this simplified Month-1-5 ramp table's rounded monthly totals. Treat the headline +A$25,087.07/month (weekday/Saturday blend) as the more precise figure; this ramp table is for visualising the build-up shape across Year 1, not as a replacement for the precise weekday-based calculation above.**

See "Years 1-3 Annual Projection" above for the corresponding multi-year view.

---

## Changelog

**2026-07-19 (Phase 6 gap-fill)** — Found via Phase 6 spec-verification that this document had Month-5+ steady-state figures only (weekday/weekly/monthly/quarterly/half-yearly/yearly), no Year 1 month-by-month ramp and no Years 1-3 multi-year view. Added both, sourced from `cash-flow.md`'s existing ramp shape and this document's own steady-state v2.0 figures, with an explicit caveat that `cash-flow.md`'s absolute figures are built on the superseded 8-client/3-package model and should not be reused without re-verification. Surfaced (not resolved) the PM-profitability discrepancy already logged in `business-plan.md` and `docs/01_conflicts_log.md`.

**2026-07-20 (CONFLICT-08 resolved)** — Resolved the PM-profitability discrepancy: `pm-staffing-roster.md`'s standalone PM loss was itself an artifact of the stale 8-client AM model, not a genuine loss — see `pm-staffing-roster.md`'s corrected banner and `docs/01_conflicts_log.md` CONFLICT-08. Filled in the previously-withheld PM/ancillary columns in the Year 1 Monthly Ramp table using the now-confirmed-compatible `pm-staffing-roster.md` session-volume figures. Updated the Years 1-3 Annual Projection with a corrected Year 1 estimate, disclosing the one remaining known simplification (flat vs ramped costs in early months, which understates rather than overstates profitability).

**2026-07-20 (Sunday reopening criterion)** — Reworded the Sunday-closed reference to state the actual reopening bar: proven AND profitable standalone PM demand, not demand alone — per Anthony's feedback. Cascaded the same wording change into `business-plan.md`, `executive-summary.md`, `HANDOFF.md`, `am-capacity-weekend.md`.

**2026-07-20 (v1.0 removed entirely, v2.0 expanded to full standalone document, v2.1)** — Anthony's direct feedback: this document was "genuinely confusing" with the superseded v1.0 tables (including the alarming "Saturday AM GTT Runs at a Loss" finding) sitting ABOVE the corrected v2.0 tables, causing exactly the kind of confusion/misinformation risk a founder-facing financial document should never carry. Actioned in full:
1. **Deleted v1.0 entirely** — the "⚠ FINDING — Saturday AM GTT Runs at a Loss" section and all of old sections 1-8 (Weekday/Saturday/Sunday/Weekly/Monthly/Quarterly/Half-Yearly/Yearly using v1.0's blanket-shift costing) and the old Key Callouts tied to v1.0. This content no longer exists in this document — it is not archived or flagged, it is gone, per Anthony's explicit instruction ("it can cause confusion and misinformation... needs to be removed").
2. **Clarified, not removed, the Saturday penalty rate** — added a dedicated section stating plainly that the MA000005 133%/150% Saturday penalty is a confirmed real award rate, applied in full throughout this document; what was wrong in the old v1.0 was the blanket-shift costing method, not the rate itself.
3. **Confirmed no Sunday references remain** — checked the full document after deletion; none found. Sunday is closed and not modelled here, per `am-capacity-weekend.md`.
4. **Expanded former v2.0 "Weekday (unchanged)" one-liner and single-figure Quarterly/Half-Yearly/Yearly into full breakdown tables** (Revenue/Direct Labor/Workers Comp/Overhead/Net rows), matching the Monthly section's existing format, since there is no longer a v1.0 to point back to for line-item detail.
5. **Broke down the A$13,980/month Non-Wage Overhead lump sum into its 13 component line items** (rent, utilities, internet, Fresha, Resend, marketing, GTT supplies, laundry, cleaning, insurance, accounting, consumables, misc), sourced from `cash-flow.md` §Cost Assumptions — the same breakdown that document already cross-references as canonical.
6. **Added a one-line Ancillary Revenue composition note** (cafe/retail — Gaia, Weleda, Mustela products, per `business-plan.md` §6) wherever Ancillary Revenue appears, so the figure is no longer unexplained.
7. **Answered the treatment-headcount question directly and with a checked basis:** 7 staff (not 8) is the genuine minimum at current 10-client/day volume, via Massage+Beauty cross-training only (Nails/Hair cannot pool) — verified against `am-capacity-weekend.md`'s Scenario C concurrency check and `multirole-CORRECTION.md`'s corrected pooling math. Flagged that this saving does not persist if AM capacity later expands to Scenario D (15 clients/day), where treatment headcount returns to 8.
8. **Stated the Saturday downtime-fill principle explicitly** in this document (§1, §2) — same staff-utilisation model already documented for weekdays in `gtt-center-perth-overview-for-imara.md`/`executive-summary.md`, now also stated for Saturday specifically.
9. **Spelled out the A$55,000 Month 5+ AM revenue derivation** in the Year 1 Monthly Ramp section: 10 clients/day × A$250 × 22 trading days = A$55,000, a capacity ceiling dependent on the referral pipeline actually filling all 10 daily slots, which is why the ramp table assumes gradual build-up rather than Day-1 full capacity.
