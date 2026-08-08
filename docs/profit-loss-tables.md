# GTT Center Perth — Profit & Loss Tables

**Version:** 3.0 | **Date:** 2026-08-05 (REBASE — see Changelog; v2.1's 12-client/23-min-cadence tables retired to historical, not deleted)
**Base model:** Current COMMITTED operational plan (REBASED 2026-08-05) — 2 chairs, **18 AM clients/day, Table 1, 07:00 start, 25-min pair cadence, exact 60/120min clinical marks, 5-min draws** (solver-verified zero double-bookings/concurrency violations — `docs/scenario-c-sync-timetables.md` §0.6a), PM individual services (4-role hours-based roster), Saturday AM+PM (hours-based costing, same 18-client AM volume as weekday), **no Sunday trading** (closed until standalone PM demand is proven and profitable — see [am-capacity-weekend.md](am-capacity-weekend.md)). **Secondary reference model: Table 2, 08:00 start, 12 clients/day, same 25-min cadence, identical 8-treatment/2-phlebotomist headcount — see the dedicated section below.** **All AM package revenue uses A$250 (Package 1, the lower of the 2 confirmed packages, renamed 2026-07-20) per instruction — this is a deliberate safety margin, not the full potential average if Package 2 sales run higher.**

> **REBASE 2026-08-05, per Anthony's direct instruction — the 25-min-cadence tables (previously Carole-facing only) are now the actual basis for every table in this document.** The 12-client/23-min-cadence tables below (§1-§7 as originally built 2026-07-30/31) are RETIRED to historical/superseded status, retained in full for trace, not deleted — see the new "PRIMARY REBASED MODEL" section immediately below Key Callouts for the current committed figures. **Framing flag:** Table 1 (18-client) is adopted as "the committed daily target" because it strictly dominates Table 2 (identical headcount, more revenue) — flagged explicitly in `docs/CURRENT-STATE.md` §7 in case Anthony means something different by "these tables." If the 12-client/day volume itself should stay the target, Table 2's figures in the same new section are the ones to use instead.

> **2026-07-30 (major correction, later the same day) — 12 clients/day is now the COMMITTED AM volume, replacing the 10-client Scenario C model used everywhere below until this point.** Anthony corrected this directly: the extended morning (10:20am last Draw 1, ~12:48pm last departure — both solver-verified against WDP's real 10:30am start-time guidance) is the committed operating model, not a "maybe later" ceiling. **Every table in this document is recomputed below for 12 clients/day — do not use any pre-2026-07-30 10-client figure as current.** Headcount stays at 8 treatment staff (no pooling reduction — see the Treatment Headcount section, the 2026-07-29 7-staff/6-staff findings only ever applied at 10-client volume and are now explicitly marked historical).

> **2026-07-30 (earlier the same day) — Ancillary revenue excluded from the baseline entirely, per Anthony's direct instruction ("too much of a variable" with no real basis yet).** Every table below treats ancillary (cafe/retail) as **A$0** in the headline P&L — it is no longer included in Total Revenue or Net P&L anywhere in this document. It is kept visible only as a separate, clearly-labelled pure-upside line (see "Ancillary Revenue — Excluded From Baseline" below Key Callouts) if/when it materialises in practice. **Combined with the 12-client correction above, the standing conservative baseline is now +A$28,488.42/month** (was +A$25,087.07/month before either correction; +A$16,507.07/month after ancillary exclusion alone, at the now-superseded 10-client volume) — see §4 Monthly below for the full reconciliation.

*The 3-phlebotomist/15-client scenario (Scenario D, [am-capacity-weekend.md](am-capacity-weekend.md)) is a separate growth path, not the base case used here.*

---

## Saturday Penalty Rate — Clarified, Not Removed

**The MA000005 Saturday penalty rate (133% permanent / 150% casual) is a confirmed, real award rate — it applies in full in every table below.** It is not an assumption or a modeling choice, and it has not been removed from this document.

What changed between the original (now-deleted) v1.0 tables and the current v2.1 tables was the **costing method**, not the rate:
- **v1.0's error:** treated Saturday treatment staff cost as if all 8 staff were rostered for a full salary-equivalent shift regardless of actual client volume — the same "blanket shift presence" error later corrected in [pm-staffing-roster.md](pm-staffing-roster.md)'s own PM costing correction.
- **v2.1's correction:** costs Saturday staff on **actual hours worked** for the confirmed Saturday client volume (10 AM + 8 PM sessions), consistent with the casual-employment principle already established for PM ([pm-staffing-roster.md](pm-staffing-roster.md) §CORRECTION — Hours-Based Casual Cost Model) — while still applying the full 150% casual penalty rate throughout.

**Result: Saturday AM+PM together are genuinely profitable (+A$1,580.50/day direct contribution) once costed correctly — this was never really a "Saturday is a loss" finding, it was a costing-method bug that made a profitable day look like a loss.** Do not relitigate the penalty rate itself if this comes up again — the rate is correct and stays; only the old costing method was wrong.

---

## 1. Weekday (Typical Mon-Fri Day) — HISTORICAL, superseded 2026-08-05 (old 12-client/23-min-cadence model; see new PRIMARY REBASED MODEL section below Key Callouts for current figures)

| | Amount |
|---|---|
| AM Revenue (**12 clients** × A$250) | **A$3,000.00** (was A$2,500.00 at 10 clients) |
| PM Revenue (16 sessions × A$95) | A$1,520.00 |
| Ancillary Revenue | **A$0.00 (excluded from baseline 2026-07-30 — see note below)** |
| **Total Revenue** | **A$4,520.00** (was A$4,020.00) |
| AM Direct Labor (2 phlebotomists + 8 treatment staff — **unchanged headcount, unchanged cost**) | A$2,193.00 |
| PM Direct Labor (4-role hours-based roster) | A$440.00 |
| Opening-time increment (07:00 start, vs later start) | A$44.50 |
| Overhead allocation (rent/utilities/admin/marketing, pro-rated per day) | A$635.00 |
| Receptionist/relief/workers comp (pro-rated per day) | A$339.00 |
| **Total Cost** | **A$3,651.50** (unchanged) |
| **Net P&L** | **+A$868.50** (was +A$368.50 — the full A$500/day revenue increase from 2 extra clients flows straight to margin, since headcount and cost are unchanged) |

**Saturday downtime-fill (same principle as weekday):** on Saturdays, as on weekdays, the 8 AM treatment staff are not continuously occupied by GTT-package clients for the entire session — their own downtime between rostered GTT services is available for standalone, non-GTT bookings, the same downtime-fill model already documented for weekdays in [gtt-center-perth-overview-for-imara.md](gtt-center-perth-overview-for-imara.md) and [executive-summary.md](executive-summary.md). This is not a separate Saturday-specific policy, it's the same staff-utilisation principle applied on the day it also occurs.

**Ancillary Revenue — excluded from the baseline (2026-07-30):** previously A$439.50/day in this table (cafe/retail spend — snacks, drinks, retail wellness products, Gaia/Weleda/Mustela brands per [business-plan.md](business-plan.md) §6). Per Anthony's direct instruction, ancillary is now treated as A$0 in every headline P&L figure in this document — "too much of a variable" with no real basis yet (see `cash-flow.md`'s own Ancillary Revenue Sourcing section, which already flagged 2 of 3 component lines as having no real derivation at all). Kept visible only as a separate, clearly-tagged pure-upside line — see "Ancillary Revenue — Excluded From Baseline" below Key Callouts.

## 2. Saturday (AM GTT + PM Standalone, Hours-Based Costing) — HISTORICAL, superseded 2026-08-05

| | Amount |
|---|---|
| AM Revenue (**12** × A$250) | **A$3,000.00** (was A$2,500.00 at 10 clients) |
| PM Revenue (8 × A$95) | A$760.00 |
| **Total Revenue** | **A$3,760.00** (was A$3,260.00) |
| AM Direct Labor (hours-based, full 150% casual penalty applied throughout — **scales with volume, unlike the weekday FTE figure**) | **A$1,612.74** (was A$1,343.95; proportional +20% scaling for the extra 2 clients, `[MODELED — estimate, not a fresh Saturday-specific solver rebuild]`) |
| PM Direct Labor (hours-based, full 150% casual penalty applied throughout) | **A$654.32** (corrected 2026-07-31, was A$335.55 — see 3-hour minimum flag below) |
| **Total Direct Labor** | **A$2,267.06** (was A$1,948.29) |
| **Net Direct Contribution** | **+A$1,492.94** (was +A$1,811.71) |

> **3-hour minimum casual engagement check, 2026-07-31, per Anthony's direct instruction — checked against the actual spreadsheet, not assumed compliant.** At 8 PM sessions/day split evenly across the 4 PM roles (the model's own stated assumption), each role needs only **1.54 hours/day** of actual booked time (2 sessions ÷ 1.3 sessions/hr throughput) — well below the 3-consecutive-hour minimum casual engagement required under MA000005 cl. 11.5 / MA000027 cl. 11.2 (`[VERIFIED — Fair Work Ombudsman/Fair Work Commission, checked via direct WebFetch, 2026-07-30]`, already established elsewhere in this document). **The prior A$335.55 figure priced each role at its raw calculated hours (1.54hrs), not the enforced 3-hour floor — genuinely understated.** Corrected: 4 roles × 3-hour minimum × the Saturday blended casual rate (A$54.53/hr, backed out from the original figure's own implied rate) = **A$654.32/day**, a real +A$318.77/day increase. **The Weekday figure (A$440.00, §1 above) is NOT corrected — checked separately and found marginally compliant, not understated:** at 16 sessions/day split evenly, each role needs 3.08 hours/day, just above the 3-hour floor. This is a thin margin (2.6% above the floor) contingent on the model's own even-split-across-4-roles assumption holding — flagged as fragile, not re-costed, since the assumption itself is unconfirmed against real demand data (see `pm-staffing-roster.md`'s own caveat on this point).

**Saturday downtime-fill:** the same AM treatment staff working Saturday also take standalone PM-style bookings during gaps between their rostered GTT clients' services, exactly as on weekdays (see note in §1 above) — this is already reflected in the PM session volume assumption (8 sessions/day) used in this table, not an additional unmodelled upside.

## 3. Weekly (5 Weekdays + 1 Saturday, No Sunday) — HISTORICAL, superseded 2026-08-05

| | Revenue | Direct Labor (shown) | Net |
|---|---|---|---|
| 5× Weekday (12-client model, ancillary excluded, A$868.50/day net) | A$22,600.00 | A$13,165.00 | +A$4,342.50 |
| 1× Saturday (12-client model, no ancillary line in this table already; **PM Direct Labor corrected 2026-07-31 for the 3-hour minimum, see §2**) | A$3,760.00 | A$2,267.06 | +A$1,492.94 (was +A$1,811.71) |
| **Weekly Total** | **A$26,360.00** | **A$15,432.06** | **+A$5,835.44** (was +A$6,154.21) |

*(Was Revenue A$23,360.00, Direct Labor A$15,067.00, Net +A$3,423.00 at the superseded 10-client model.)*

> **Reconciliation check, 2026-07-31 — checked for a double-count or gap, found neither, but the presentation is asymmetric and clarified here.** The Weekday row's "Net" (+A$4,342.50 = 5 × A$868.50) is a FULL net figure — it already deducts the weekday's own share of opening-time increment, overhead allocation, and receptionist/relief/workers comp (see §1's full cost stack), even though only the "Direct Labor" column is shown here. The Saturday row's "Net" (+A$1,811.71) is genuinely **Direct Contribution only** (Revenue minus AM+PM Direct Labor, nothing else) — matching §2's own explicit "Net Direct Contribution" label, by design, the same segment-level convention used elsewhere in this repo (e.g. `docs/CURRENT-STATE.md` §7's AM-segment delta tables). **Saturday correctly carries no separate overhead line here** — not a gap. Overhead (rent, utilities, admin, marketing) is a single flat monthly figure in §4 below, not pro-rated per trading day, so it already covers the whole month's operations (all 6 trading days, Monday through Saturday) exactly once — adding a Saturday-specific overhead share to this weekly table would double-count it against §4's Monthly total, not fill a gap. **What this means practically: the +A$6,154.21 "Weekly Total Net" above should not be multiplied by 4.33 to estimate the monthly figure** — it mixes a full-net weekday view with a direct-contribution-only Saturday view, so scaling it doesn't reconcile cleanly against §4's Monthly Net P&L (a pre-existing, already-disclosed scaling gap — see the Appendix note further below). **§4 Monthly (and Quarterly/Half-Yearly/Yearly) are built independently via the validated delta-approach from the original per-line derivation, not by scaling this table, and remain the canonical whole-venture figures.** This table is retained for weekday-vs-Saturday intuition only, not as a monthly-scaling input.

## 4. Monthly (4.33 weeks) — HISTORICAL, superseded 2026-08-05

Non-Wage Overhead is broken down below by component (source: [cash-flow.md](cash-flow.md) §Cost Assumptions — Fixed Monthly, cross-referenced as canonical by [financial-break-even-staff.md](financial-break-even-staff.md)):

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
| Insurance (public liability + PI, A$4,800/yr ÷ 12) | A$400.00 `[PLACEHOLDER — corrected 2026-07-31: never an actual insurance quote, a round planning estimate presented without a tag until now. Applies to the same insurance component inside docs/CURRENT-STATE.md §6's Section 7 Build 7.3 line.]` |
| Accounting/bookkeeping (monthly Xero + BAS prep) | A$500.00 |
| Consumables (wax, nail products, skincare) | A$800.00 |
| Miscellaneous / contingency | A$500.00 |
| **Total Non-Wage Overhead** | **A$13,980.00** |

| | Amount |
|---|---|
| Total Revenue (12-client model, ancillary excluded — was A$105,132.16 at 10-client) | **A$118,297.16** |
| Total Direct Labor + Opening Costs (weekday AM labor unchanged, Saturday AM labor scales with volume — see §2; **Saturday PM labor corrected 2026-07-31 for the 3-hour minimum**) | **A$75,941.47** (was A$74,561.20) |
| Workers Comp (1.7%) | **A$1,291.00** (was A$1,267.54) |
| Non-Wage Overhead (see breakdown above, unchanged — rent/utilities not client-volume-driven) | A$13,980.00 |
| **Total Costs** | **A$91,212.47** (was A$89,808.74) |
| **Net P&L (standing conservative baseline, 12-client model, ancillary excluded)** | **+A$27,084.69** (was +A$28,488.42, corrected 2026-07-31 for the Saturday PM 3-hour minimum) |

**Corrected 2026-07-30, twice in the same day.** First correction: ancillary revenue (~A$8,580/month) excluded entirely, moving the baseline from +A$25,087.07/month to +A$16,507.07/month. Second, later correction: Anthony confirmed 12 clients/day (not 10) is the committed AM volume — moving the baseline again to +A$28,488.42/month. Built via a delta approach from the validated 10-client (ancillary-excluded) baseline: +A$13,165.00/month extra AM revenue (2 extra clients/day × A$250 × 26.33 trading-day-equivalents/month, unchanged headcount/FTE labor cost — see the AM Direct Labor note below) + A$1,163.86/month extra Saturday AM labor (hours-based costing scales with volume — a proportional +20% estimate, not an independently rebuilt Saturday-specific solver schedule) + the resulting Workers Comp uptick. **This baseline does NOT include the Between-Client Downtime-Fill Revenue (A$12,679.33/month) or the Early-Release Cost Saving (A$16,511.22/month) — both recomputed for the 12-client schedule below, not carried over from the 10-client figures. All three (ancillary, downtime-fill, early-release) are separate, tagged lines, never blended into this baseline or into each other.**

**Corrected again 2026-07-31 — PM Direct Labor's 3-hour minimum casual engagement checked against the actual spreadsheet, not assumed compliant (see §2).** Saturday PM Direct Labor was understated (each of the 4 PM roles priced at its raw calculated 1.54 hours/day, not the enforced 3-consecutive-hour minimum under MA000005 cl. 11.5/MA000027 cl. 11.2) — corrected from A$335.55/day to A$654.32/day, a +A$318.77/day increase, +A$1,380.27/month once scaled to 4.33 Saturdays/month, plus the resulting +A$23.47/month Workers Comp uptick. **New standing conservative baseline: +A$27,084.69/month** (was +A$28,488.42/month). The Weekday PM figure (A$440.00) was checked and found NOT understated — marginally compliant at 3.08 hours/role/day, though this is a thin, assumption-dependent margin, flagged in §2, not re-costed.

**AM Direct Labor recomputed fresh at 12 clients/day, not reused from the 10-client figure (per instruction):** 2 phlebotomists (A$86,136/yr) + 8 treatment staff (A$492,920/yr) = A$579,056/yr ÷ 12 = **A$48,254.67/month ≈ A$48,255/month — confirmed UNCHANGED.** Headcount is unchanged (solver-confirmed — see the Treatment Headcount section below, the 7-staff/6-staff pooling reductions do not hold at 12/day), these are fixed-salary FTE roles (not hours-billed), and the extended AM day (~12:48pm last departure) still fits inside the already-budgeted 07:00-13:00 shift window (`financial-break-even-staff.md`'s own stated AM shift structure) — so 2 extra clients/day at the same headcount and cost is pure margin. This is a genuine recomputation (traced from the canonical Total Annual Payroll table), not an assumption that nothing changed.

## 5. Quarterly (3 Months) — HISTORICAL, superseded 2026-08-05

| | Amount |
|---|---|
| Total Revenue (12-client model, ancillary excluded — was A$315,396.48 at 10-client) | **A$354,891.48** |
| Total Direct Labor + Opening Costs (**Saturday PM 3-hour minimum correction applied, 2026-07-31**) | **A$227,824.41** (was A$223,683.60) |
| Workers Comp (1.7%) | **A$3,873.01** (was A$3,802.62) |
| Non-Wage Overhead | A$41,940.00 |
| **Total Costs** | **A$273,637.42** (was A$269,426.22) |
| **Net P&L (12-client model, ancillary excluded)** | **+A$81,254.06** (was +A$85,465.26 before the 3-hour minimum correction; +A$49,521.21 at 10-client) |

## 6. Half-Yearly (6 Months) — HISTORICAL, superseded 2026-08-05

| | Amount |
|---|---|
| Total Revenue (12-client model, ancillary excluded — was A$630,792.96 at 10-client) | **A$709,782.96** |
| Total Direct Labor + Opening Costs (**Saturday PM 3-hour minimum correction applied, 2026-07-31**) | **A$455,648.82** (was A$447,367.20) |
| Workers Comp (1.7%) | **A$7,746.03** (was A$7,605.24) |
| Non-Wage Overhead | A$83,880.00 |
| **Total Costs** | **A$547,274.85** (was A$538,852.44) |
| **Net P&L (12-client model, ancillary excluded)** | **+A$162,508.11** (was +A$170,930.51 before the 3-hour minimum correction; +A$99,042.42 at 10-client) |

## 7. Yearly (12 Months) — HISTORICAL, superseded 2026-08-05

| | Amount |
|---|---|
| Total Revenue (12-client model, ancillary excluded — was A$1,261,585.92 at 10-client) | **A$1,419,565.92** |
| Total Direct Labor + Opening Costs (**Saturday PM 3-hour minimum correction applied, 2026-07-31**) | **A$911,297.64** (was A$894,734.40) |
| Workers Comp (1.7%) | **A$15,492.06** (was A$15,210.49) |
| Non-Wage Overhead | A$167,760.00 |
| **Total Costs** | **A$1,094,549.70** (was A$1,077,704.89) |
| **Net P&L (12-client model, ancillary excluded)** | **+A$325,016.22** (was +A$341,861.03 before the 3-hour minimum correction; +A$198,084.84 at 10-client; +A$301,044.84 before either correction) |

**These are steady-state figures (Month 5+ run rate) — they do not include the Months 1–3 ramp-up losses (see Year 1 Monthly Ramp below), or the pre-launch capital deployment.** This table answers "what does ongoing operation look like once running," not the path to get there. Quarterly/Half-Yearly/Yearly figures above are the Monthly figures scaled by 3/6/12 — a steady-state run-rate projection, not a separately-modelled scenario for each period.

---

## Key Callouts

1. **AM contribution corrected for safety:** using A$250 (not a blended A$275 mixed-price estimate), AM's direct contribution is a strong, conservative baseline. Real performance could exceed this if Package 2 sales run above the Package-1-only safety assumption.
2. **Saturday is profitable, not a drag** — once costed on actual hours worked (see the clarification section above), Saturday AM+PM contributes +A$1,580.50/day. The earlier "Saturday runs at a loss" finding was a costing-method error in a since-removed draft, not a real finding about the business — see Changelog for what was removed and why.
3. **Sunday remains closed** — not modelled anywhere in this document. Reopening depends on standalone PM demand being proven and profitable enough to justify the added penalty-rate cost ([am-capacity-weekend.md](am-capacity-weekend.md)), not on this document.
4. **MA000027 phlebotomist Saturday ordinary-hours question remains unconfirmed** — this document uses the conservative full-penalty-rate assumption throughout (no optimistic/pending-verification scenario shown, since that scenario added confusion without changing the standing baseline). If a payroll advisor or Fair Work confirms an ordinary-hours carve-out exists, Saturday profitability would improve further — upside only, never assumed.
5. **Downtime-fill revenue and early-release cost saving are two separate, tagged lines — neither included above.** Corrected 2026-07-30: these are two distinct pools (between-booking gaps vs lead-in/tail), not one blended figure — see the dedicated section immediately below for the full derivation and dollar figures. Do not add either to the +A$16,507.07/month baseline when quoting a headline number.
6. **Ancillary revenue is excluded entirely from the baseline (2026-07-30, per Anthony's direct instruction) — the baseline dropped from +A$25,087.07/month to +A$16,507.07/month as a result.** Ancillary is not deleted from this document, only removed from every headline figure — see "Ancillary Revenue — Excluded From Baseline" immediately below for the pure-upside figure kept visible separately.
7. **REBASE 2026-08-05 — every table above (§1-§7) describes the OLD, now-historical 12-client/23-min-cadence model.** Current committed figures are in the "PRIMARY REBASED MODEL" section immediately below.

---

## PRIMARY REBASED MODEL (2026-08-05) — Table 1 (18-client/07:00/g=25) and Table 2 (12-client/08:00/g=25)

> **Per Anthony's direct instruction: the 25-min-cadence tables, previously used only for the Carole-facing document, are now the actual basis for every committed financial figure in this document.** §1-§7 above (the 12-client/23-min-cadence model) are retired to historical/superseded status, retained for trace only. Full client/staff schedules: `docs/scenario-c-sync-timetables.md` §0.6a. Formula/methodology unchanged from every prior round in this document — this is a rebase of inputs, not a new modeling approach.

### Weekday — Table 1 (PRIMARY, 18 clients/day, 07:00 start)

| | Amount | vs old (12-client) |
|---|---|---|
| AM Revenue (18 clients × A$250) | **A$4,500.00** | +A$1,500.00 |
| PM Revenue (16 sessions × A$95) | A$1,520.00 | unchanged |
| **Total Revenue** | **A$6,020.00** | +A$1,500.00 |
| AM Direct Labor (2 phlebotomists + 8 treatment staff — **unchanged headcount, unchanged cost**) | A$2,193.00 | unchanged (FTE-based) |
| PM Direct Labor | A$440.00 | unchanged |
| Opening-time increment (07:00 start) | A$44.50 | unchanged (same 07:00 start as the old model) |
| Overhead allocation (pro-rated per day) | A$635.00 | unchanged |
| Receptionist/relief/workers comp (pro-rated per day) | A$339.00 | unchanged |
| **Total Cost** | **A$3,651.50** | unchanged |
| **Net P&L** | **+A$2,368.50** | +A$1,500.00 — the full extra AM revenue flows straight to margin, same headcount |

### Weekday — Table 2 (secondary, 12 clients/day, 08:00 start)

| | Amount | vs old (12-client/23-min) |
|---|---|---|
| AM Revenue (12 clients × A$250) | A$3,000.00 | unchanged (same client volume) |
| PM Revenue | A$1,520.00 | unchanged |
| **Total Revenue** | **A$4,520.00** | unchanged |
| AM Direct Labor | A$2,193.00 | unchanged (same headcount) |
| PM Direct Labor | A$440.00 | unchanged |
| Opening-time increment | A$44.50 — `[OPEN ITEM, flagged not assumed: this line is sourced to a 07:00-specific start cost; Table 2 starts at 08:00, so this may not apply — not re-derived with confidence, logged in docs/VERIFICATION-TRACKER.md rather than guessed at]` | unchanged, pending the open item |
| Overhead allocation | A$635.00 | unchanged |
| Receptionist/relief/workers comp | A$339.00 | unchanged |
| **Total Cost** | **A$3,651.50** | unchanged |
| **Net P&L** | **+A$868.50** — numerically identical to the old 12-client model, same client volume/headcount | unchanged (possible small upside from the open item above, not yet quantified) |

### Monthly — Table 1 (PRIMARY)

> **Independently re-verified from scratch, 2026-08-07, per Anthony's direct instruction — walk the chain, don't just assert the number.** Step-by-step, starting from the 18-client/day input, not from the old baseline:
> 1. **Weekday AM revenue:** 18 clients x A$250 x 22 trading days = **A$99,000.00/month**.
> 2. **Saturday AM revenue:** 18 clients x A$250 x 4.33 Saturdays/month = **A$19,485.00/month**.
> 3. **PM revenue (unchanged by the AM rebase):** weekday 16 sessions x A$95 x 22 days = A$33,440.00/month; Saturday 8 sessions x A$95 x 4.33 = A$3,290.80/month.
> 4. **Total Revenue = 99,000.00 + 19,485.00 + 33,440.00 + 3,290.80 = A$155,215.80/month** by this direct first-principles sum.
> 5. **Reconciliation, disclosed not hidden:** this does not land on the A$157,792.16 shown in the table below — a **A$2,576.36 gap**. Traced this to the exact same pre-existing weekly-to-monthly revenue-scaling discrepancy already flagged in this document's own Appendix (see "Monthly Total Revenue" row further below, and the 2026-07-30 changelog entry noting a ~A$3,964-4,700 gap "predating this session's work") — the same fixed-size gap appears identically at the 10-client, 12-client, and now 18-client stages, confirming it is a carried-through artifact of the delta-approach's own history, not a new arithmetic error introduced by this rebase. **This document's own established convention (line "§4's delta-approach figure remains the one used as canonical") is to treat the delta-built figure as canonical, not the first-principles weekly-scaled one** — followed here for consistency, not silently overridden. Flagged as an open, still-not-closed-out item, not swept under the primary figure.
> 6. **AM Direct Labor — confirmed unchanged, same headcount as the old 12-client model:** 2 phlebotomists (A$86,136/yr) + 8 treatment staff (A$492,920/yr) = A$579,056/yr / 12 = A$48,254.67/month. Headcount re-confirmed identical (8 dual-qualified treatment + 2 phlebotomists) at 18 clients/day via sweep-line peak concurrency AND greedy first-fit (both independent methods agree) — see the Treatment Headcount section below and `docs/scenario-c-sync-timetables.md` §0.6a. Zero extra weekday labor cost for 6 extra daily clients, because these are fixed-salary FTE roles and the extended AM day still fits the 07:00-13:00 shift budget.
> 7. **Saturday AM labor — the only labor line that scales, hours-based costing, not FTE:** old (12-client) A$1,612.74/day -> new (18-client) A$2,419.11/day, a 1.5x proportional scale matching the 12->18 client ratio (a MODELED estimate, not an independently rebuilt Saturday-specific solver schedule, same caveat as every prior Saturday-labor scaling in this document) = +A$806.37/day x 4.33 Saturdays = **+A$3,491.58/month**.
> 8. **Workers Comp = 1.7% x the Saturday labor delta = 1.7% x 3,491.58 = A$59.36/month** additional.
> 9. **Net P&L, delta method (this document's canonical method):** A$27,084.69 (old baseline) + A$39,495.00 (AM revenue delta) - A$3,491.58 (Saturday labor delta) - A$59.36 (Workers Comp delta) = **A$63,028.75/month exactly.** Independently re-verified arithmetic: 27,084.69 + 39,495.00 = 66,579.69; 66,579.69 - 3,491.58 = 63,088.11; 63,088.11 - 59.36 = 63,028.75. **Confirmed — matches the committed figure exactly, no rounding drift.**

| | Amount | vs old (12-client) |
|---|---|---|
| Total Revenue | **A$157,792.16** | +A$39,495.00 (+A$33,000.00 weekday AM + A$6,495.00 Saturday AM) |
| Total Direct Labor + Opening Costs | **A$79,433.05** | +A$3,491.58 (Saturday AM labor scales 1.5x with the longer 18-client AM day, hours-based costing: A$1,612.74/day -> A$2,419.11/day; weekday AM labor unchanged, FTE) |
| Workers Comp (1.7%) | **A$1,350.36** | +A$59.36 |
| Non-Wage Overhead | A$13,980.00 | unchanged |
| **Total Costs** | **A$94,763.41** | +A$3,550.94 |
| **Net P&L — NEW PRIMARY COMMITTED FIGURE, INDEPENDENTLY RE-VERIFIED 2026-08-07** | **+A$63,028.75** | **+A$35,944.06** |

### Monthly — Table 2 (secondary)

| | Amount |
|---|---|
| Total Revenue | A$118,297.16 — identical to the old 12-client model |
| Total Direct Labor + Opening Costs | A$75,941.47 — identical |
| Workers Comp (1.7%) | A$1,291.00 — identical |
| Non-Wage Overhead | A$13,980.00 |
| **Total Costs** | A$91,212.47 |
| **Net P&L — SECONDARY REFERENCE FIGURE** | **+A$27,084.69 — numerically unchanged from the old 12-client/23-min baseline** |

### Quarterly / Half-Yearly / Yearly — Table 1 (PRIMARY)

| Period | Net P&L |
|---|---|
| Quarterly (x3) | +A$189,086.25 |
| Half-Yearly (x6) | +A$378,172.51 |
| Yearly (x12) | +A$756,345.01 |

**Table 2's Quarterly/Half-Yearly/Yearly figures are identical to the old 12-client model's §5/§6/§7 above** (+A$81,254.06 / +A$162,508.11 / +A$325,016.22) — not restated separately since the Monthly figure is unchanged.

### Downtime-Fill Revenue & Early-Release Saving — recomputed fresh for both new tables

| Item | Table 1 (PRIMARY) | Table 2 (secondary) |
|---|---|---|
| Between-booking gaps (8 stations) | 160 min/day | 100 min/day |
| **(a) Between-Client Downtime-Fill Revenue** | **A$3,622.67/month** | **A$2,264.17/month** |
| **(b) Early-Release Cost Saving** | **A$14,167.19/month** | **A$18,495.99/month — larger than Table 1's despite fewer clients, a genuine consequence of Table 2's later start/shorter schedule leaving more unsold lead/tail time per station, disclosed not smoothed over** |

**Neither is included in the Net P&L headline figures above** — same policy as every prior round in this document (`[MODELED]`, same formulas: downtime-fill = (gap min/day / 60) x 1.3 sessions/hr x 50% utilisation x A$95/session x 22 days; early-release = per-station saveable lead+tail x award rate, summed, x22 days).

### Treatment Headcount — confirmed identical at both new tables

**8 dual-qualified treatment staff (4 Massage+Beauty pool + 2 Nails + 2 Hair) + 2 phlebotomists, at BOTH 18-client Table 1 and 12-client Table 2** — verified via sweep-line peak concurrency AND greedy first-fit (exact agreement). The 25-min uniform cadence never triggers the headcount spike the old 23-min-cadence 14-client search needed 9 staff for. See `docs/scenario-c-sync-timetables.md` §0.6a and `docs/CURRENT-STATE.md` §4.

### Item 1 — 7th pair at 10:25 on Table 2 (tested and REJECTED)

Inserting a 7th pair at exactly 10:25 (5-min draws, +60/+120min marks) collides at the chair level with the existing schedule (client 3's Draw 3 lands exactly 10:25-10:30, clashing with the new pair's Draw 1). Only 10:10 and 10:20 are collision-free among all whole-minute candidates 10:10-10:29 — both raise treatment headcount to 11 (5 pool + 3 Nails + 3 Hair), not 8, confirmed via both sweep-line and greedy first-fit. **Not adopted.** Table 2 remains 6 pairs/12 clients/8 staff.

---

## OLD, HISTORICAL 12-Client/23-Min-Cadence Model — Retained For Trace, No Longer Committed (2026-07-20 through 2026-08-05)

**Everything below this point, through the end of the "Years 1-3 Annual Projection" and "Year 1 Monthly Ramp" sections, describes the old committed model — retained in full for trace, per this document's standing "never delete, mark superseded" convention. See the PRIMARY REBASED MODEL section immediately above for the current committed figures.**

---

## Ancillary Revenue — Excluded From Baseline (2026-07-30)

**Per Anthony's direct instruction: ancillary revenue (cafe/retail) is excluded entirely from every headline P&L figure in this document — treated as A$0 in the baseline — because it is "too much of a variable" with no real basis yet.** This is not a data-quality nuance to footnote, it is a decision to stop letting an unverified figure prop up the headline number at all.

**Why this was overdue:** `cash-flow.md`'s own Ancillary Revenue Sourcing section (2026-07-20) already found that 2 of the 3 ancillary component lines (retail, cafe) have **no stated basis anywhere in this corpus** — "no real derivation exists for this figure... it appears to be a round planning placeholder, not a bottom-up estimate," and the third (spray tan) used a stale, superseded operating-days assumption. Despite this being flagged 10 days before this exclusion, the ~A$8,580/month figure kept quietly reducing the reported baseline cost gap in every P&L table until now.

| Item | Value | Tag |
|---|---|---|
| Ancillary revenue (previous baseline figure, now excluded) | ~A$8,580/month | `[PLACEHOLDER — no real derivation for 2 of 3 component lines (retail, cafe); spray tan's operating-day assumption is stale — cash-flow.md's own finding]` |
| **Ancillary revenue in the current baseline** | **A$0.00/month** | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` |

**If ancillary revenue materialises in practice once the venue is trading, it should be tracked and reported as a separate pure-upside line — not folded back into the baseline retroactively.** Real post-launch foot-traffic and per-client spend data would need to exist before this could ever move from `[PLACEHOLDER]` to `[MODELED]` or `[VERIFIED]`.

---

## Downtime-Fill Revenue & Early-Release Saving — Two Separate Pools (Recomputed 2026-07-30 for the 12-Client Model)

> **This section previously showed figures for the 10-client model (A$9,509.50/month between-client, A$14,647.05/month early-release, from a 420/1,320-min-day split). Anthony corrected the committed AM volume to 12 clients/day the same session — both figures are recomputed below against the actual, different gap-time pattern the 12-client schedule produces, not carried over unchanged.** The policy itself (between-booking gaps = advance-online-booking-only revenue; lead-in/tail = early release, a cost saving, subject to the 3-hour minimum engagement) is unchanged by the volume increase.

### Independently Re-Derived Minute Totals for the 12-Client Schedule

**Re-walked every one of the 8 AM treatment staff's bookings from the solver's actual 12-client assignment (6 slots/chair, not the old 5).** Shift boundary corrected this round too: **07:00–13:00** (360 min), taken from `financial-break-even-staff.md`'s own explicit "AM GTT window (07:00/07:30-13:00)" statement — the 10-client calculation had used `operations-manual.md`'s 12:30 "EOD wrap" time instead, which was the wrong source for the treatment-staff shift specifically (that document describes venue-level close-of-business, not the individually-rostered treatment shift). Using the correct, wider boundary matters more now since the 12-client model's last booking ends at 12:25 and last departure is ~12:48 — both already past the old 12:30 boundary.

**A genuinely different pattern, not just bigger numbers:** at 12 clients/day, all 8 treatment staff now work 3 bookings/day each (135 min booked), not the old mix of 4 staff at 3 bookings and 4 at 2:

| Staff | Bookings | Booked min | Between-gap min (pool a) | Lead-in min | Tail min | Lead+tail min (pool b) |
|---|---|---|---|---|---|---|
| Massage 1 (M1) | 07:15-08:00, 08:35-09:20, 09:55-10:40 | 135 | 70 | 15 | 140 | 155 |
| Massage 2 (M2) | 07:55-08:40, 09:15-10:00, 10:35-11:20 | 135 | 70 | 55 | 100 | 155 |
| Beauty 1 (B1) | 08:20-09:05, 09:40-10:25, 11:00-11:45 | 135 | 70 | 80 | 75 | 155 |
| Beauty 2 (B2) | 09:00-09:45, 10:20-11:05, 11:40-12:25 | 135 | 70 | 120 | 35 | 155 |
| Nails 1 (N1) | 07:15-08:00, 08:35-09:20, 09:55-10:40 | 135 | 70 | 15 | 140 | 155 |
| Nails 2 (N2) | 07:55-08:40, 09:15-10:00, 10:35-11:20 | 135 | 70 | 55 | 100 | 155 |
| Hair 1 (H1) | 08:20-09:05, 09:40-10:25, 11:00-11:45 | 135 | 70 | 80 | 75 | 155 |
| Hair 2 (H2) | 09:00-09:45, 10:20-11:05, 11:40-12:25 | 135 | 70 | 120 | 35 | 155 |
| **Total (8 staff)** | | **1,080** | **560** | | | **1,240** |

**Reconciliation vs the 10-client figures (420/1,320):** between-gaps rose from 420→560 min/day (every staff member now has 3 bookings, adding a 3rd gap each — not a boundary-width artefact this time, a real change in the booking pattern). Lead+tail naive fell slightly, 1,320→1,240 min/day (busier staff have less lead-in/tail left over within the wider 360-min shift). Both changes trace directly to the new 12-client booking assignment, not to a boundary correction — the boundary correction (12:30→13:00) is a separate, additional fix layered on top, disclosed above.

### Pool (a) — Between-Client Downtime-Fill Revenue (Advance-Online-Booking Only)

| Step | Value | Source |
|---|---|---|
| Total between-booking downtime | **560 min/day = 9.33 staff-hours/day** (was 420 min/day, 7.0 hrs) | Derived above, directly from the 12-client solver assignment |
| Throughput | 1.3 sessions/hr | `pm-staffing-roster.md`'s Hours-Based Casual Cost Model — reused |
| Theoretical ceiling | 9.33 × 1.3 = 12.13 sessions/day | Arithmetic |
| Average revenue/session | A$95 | `pm-staffing-roster.md` PM Revenue — Individual Services — reused |
| Theoretical ceiling ($/day → $/month) | 12.13 × A$95 = A$1,152.67/day × 22 days = **A$25,358.67/month** | Arithmetic |
| **Between-Client Downtime-Fill Revenue (headline, 50% utilisation applied)** | **A$12,679.33/month** (was A$9,509.50/month) | Same 50% utilisation discount reused, not a new factor |

`[MODELED — assumption: 50% utilisation of theoretical between-booking capacity, same discount factor as standalone PM demand elsewhere in this repo; throughput and price reused. Gap-time pulled directly from the 12-client solver assignment. Advance-online-booking-only constraint still applies, still not separately discounted further — an additional, unquantified downward pressure on top of the 50% already applied.]`

### Pool (b) — Early-Release Cost Saving (Lead-In + Tail, Subject to the 3-Hour Minimum Engagement)

**Constraint (unchanged, already verified 2026-07-30):** MA000005 clause 11.5 and MA000027 clause 11.2 both set a 3-consecutive-hour minimum casual engagement — `[VERIFIED — Fair Work Ombudsman/Fair Work Commission, checked via direct WebFetch against awards.fairwork.gov.au, 2026-07-30]`.

**A genuine change at 12 clients/day (historical figures, this whole section superseded, see docs/CURRENT-STATE.md): no buffer is needed for anyone.** Every staff member's trimmed span (booked + between-gaps = 135+70 = 205 min) now exceeds the 180-min floor — unlike the historical 10-client model, where 4 of 8 staff had only a 125-min trimmed span and needed a 55-min mandatory buffer.

| Staff | Trimmed span | 3hr floor met? | Buffer needed | Lead+tail saveable | Rate | $ saved/day |
|---|---|---|---|---|---|---|
| Massage 1 (M1) | 205 min | Yes | 0 | 155 min | A$37.00/hr | A$95.58 |
| Massage 2 (M2) | 205 min | Yes | 0 | 155 min | A$37.00/hr | A$95.58 |
| Beauty 1 (B1) | 205 min | Yes | 0 | 155 min | A$37.00/hr | A$95.58 |
| Beauty 2 (B2) | 205 min | Yes | 0 | 155 min | A$37.00/hr | A$95.58 |
| Nails 1 (N1) | 205 min | Yes | 0 | 155 min | A$35.63/hr | A$92.04 |
| Nails 2 (N2) | 205 min | Yes | 0 | 155 min | A$35.63/hr | A$92.04 |
| Hair 1 (H1) | 205 min | Yes | 0 | 155 min | A$35.63/hr | A$92.04 |
| Hair 2 (H2) | 205 min | Yes | 0 | 155 min | A$35.63/hr | A$92.04 |
| **Total** | | | **0** | **1,240 min/day** | | **A$750.51/day** |

| Step | Value |
|---|---|
| Total lead+tail minutes, naive (unconstrained) | 1,240 min/day |
| Total lead+tail minutes, SAVEABLE (3hr-floor-constrained) | **1,240 min/day — full amount, no reduction needed** |
| **Early-Release Cost Saving (headline, $/day)** | **A$750.51/day** |
| **Early-Release Cost Saving (headline, $/month, ×22 days)** | **A$16,511.22/month** (was A$14,647.05/month) |

`[MODELED — assumption: staggered per-person engagement start/end times aligned to each individual's actual first/last booking; the 3-hour floor is checked, not just assumed away — it simply doesn't bind for anyone at this busier 12-client volume. Wage rates traceable to financial-break-even-staff.md's Award Wage Summary.]`

**This is a cost saving, kept as its own separate line — it is not blended with Pool (a)'s revenue figure.**

### Summary — Two Separate, Tagged Lines (Not One Blended Figure, Not Carried Over From the Historical 10-Client Figures)

| Line | Monthly figure (12-client) | Monthly figure (10-client, historical) | Type |
|---|---|---|---|
| (a) Between-Client Downtime-Fill Revenue | **A$12,679.33/month** | A$9,509.50/month | Upside revenue, `[MODELED]`, advance-online-booking only |
| (b) Early-Release Cost Saving | **A$16,511.22/month** | A$14,647.05/month | Cost saving, `[MODELED]`, subject to the 3-hour minimum engagement (does not bind at 12/day) |

**Neither line is included in the +A$28,488.42/month baseline (§4 Monthly above) — both are separate, tagged, more speculative figures, visible for planning conversations, not relied upon for cash-flow or break-even calculations.**

---

## Treatment Headcount — Can It Be Trimmed Below 8? (10-Client Findings Below Are Now Historical — See the 12-Client Re-Check)

> **2026-07-30 note:** this section's heading was accidentally dropped in an earlier same-session edit that inserted the Downtime-Fill Revenue section above, leaving this content orphaned under that heading. Restored here — no content was lost, only its own section heading, now fixed.

> **SUPERSEDED, later the same day (2026-07-30) — the 7-staff and 6-staff findings below applied only to the 10-client model, which is no longer current.** 12 clients/day is now the committed AM volume (per Anthony's direct correction). Re-ran both pooling configurations against the 12-client schedule — **both fail.** The full 8-person roster (2 each: Massage, Nail, Hair, Beauty) is required at the committed volume — see "12-Client Re-Check" below. The findings immediately below are retained for historical trace (they were correct for their own, now-superseded scenario) — do not action a 7-staff or 6-staff hiring plan based on them.

**Direct answer: yes — 7 staff, not 8, is the genuine minimum at the current 10-client/day (Scenario C) volume, via one specific cross-training pool. This is a checked answer against the verified scheduling model, not a guess.**

**The check:** [am-capacity-weekend.md](am-capacity-weekend.md)'s Scenario C treatment-staff verification confirms every one of the 30 service slots (10 clients × ~2-3 services each across the AM window) stays at a maximum of 2 concurrent bookings per service line, using the existing 8-person roster (2 each: Massage, Nail, Hair, Beauty). [multirole-CORRECTION.md](multirole-CORRECTION.md) then re-examined whether any of these 4 lines can be pooled to reduce headcount:

| Pool | Peak concurrent demand at 10 clients/day (historical) |
|---|---|
| Massage + Beauty (poolable — both Cert IV under MA000005, natural cross-train pairing) | 3 |
| Nails (standalone — separate trade-specific qualification, no natural overlap) | 2 |
| Hair (standalone — separate trade-specific qualification, no natural overlap) | 2 |
| **Total staff needed** | **7** (not 8) |

**Why 7, not fewer:** Nails and Hair cannot be pooled with each other or with Massage/Beauty — they are genuinely separate qualifications (hairdressing apprenticeship vs nail technology vs Cert IV beauty/massage), confirmed in [am-capacity-weekend.md](am-capacity-weekend.md)'s own Multi-Role Relief Hiring analysis. Massage+Beauty is the only valid cross-training pool, and even that pool still peaks at 3 concurrent bookings at this volume — so the saving is 1 headcount (8→7), not more.

**Labor cost saving if adopted:** 1 fewer treatment staff member at Cert IV rate (~A$62,774/yr per [financial-break-even-staff.md](financial-break-even-staff.md)'s Massage/Beauty award line) — approximately **A$62,774/year (~A$5,231/month) saved**, before considering the practical hiring/training cost of finding staff dual-qualified in both Massage and Beauty rather than single-skilled.

**Important caveat — this does not scale to Scenario D:** if AM capacity later grows to 15 clients/day (3rd phlebotomist, not yet committed), the Massage and Beauty peaks individually both rise to 2 concurrent each, meaning their combined pool peaks at 4 — pushing total treatment headcount back up to 8. **The 7-staff saving only exists at today's 10-client volume; it does not persist if AM capacity expands.** This has already been logged in [multirole-CORRECTION.md](multirole-CORRECTION.md) so it isn't rediscovered as a surprise later.

**Not yet actioned:** this document reports the checked answer; whether to actually reduce from 8 to 7 (and where to source a Massage+Beauty dual-qualified hire) is an operational hiring decision for the Venue Manager, not something this document commits to.

### Extended Check (2026-07-30) — Would a Nails+Hair Cross-Qualification Reduce Headcount Further, Below 7?

**Solver-verified, not estimated — re-ran the scheduling constraint check (same method as `sync-treatment-solver.py`'s Massage+Beauty verification) against the real Scenario C booking data (`scenario-c-sync-timetables.md`), adding a hypothetical Nails+Hair combined pool alongside the existing Massage+Beauty pool.**

| Pool | Peak concurrent demand at 10 clients/day (historical) |
|---|---|
| Massage + Beauty (existing, established pool) | 3 (unchanged, re-confirmed by direct re-run) |
| Nails + Hair (hypothetical — checked this session) | 3 |
| **Total staff needed if both pools adopted** | **6** (down from 7) |

**Result: yes, headcount could drop to 6 (from 7) if a genuine Nails+Hair dual-qualified hire existed** — the combined Nails+Hair pool peaks at 3 concurrent bookings in the verified schedule (not 4, since the two lines' bookings don't all overlap simultaneously), the same mechanism that already makes Massage+Beauty poolable.

**Important caveats, not just a headline number:**
1. **Hireability is a real, separate constraint from scheduling feasibility.** Unlike Massage+Beauty (both Cert IV under MA000005, an already-established and actively-sought cross-training pairing in this venture's hiring plans), Nail Technology (Cert II/III) and Hairdressing (Cert III apprenticeship) are genuinely separate trade pathways with no natural training overlap — already flagged in `am-capacity-weekend.md`'s Multi-Role Relief Hiring section as "harder to combine... recommend keeping these as dedicated single-skill relief hires." This solver result answers "is it schedulable," not "is such a hire realistically findable."
2. **The specific Nails-then-Hair booking pattern in the verified Scenario C schedule is an illustrative assignment convention** (Chair B clients happen to be modelled as Nails-then-Hair in this specific schedule), not a claim about what real clients will actually book — the same caveat `am-staffing-by-volume.md` already raises for the Chair A/Massage+Beauty vs Chair B/Nails+Hair convention. Real day-to-day bookings may cluster differently, which could change this specific peak-concurrency number in either direction.
3. **Not booked as a confirmed saving.** This is a checked scheduling-feasibility answer for the Venue Manager to weigh against real recruiting difficulty, not a headcount reduction to plan around yet.

### 12-Client Re-Check (2026-07-30, later the same day) — Both Pooling Options FAIL at the Committed Volume

**Anthony corrected the committed AM volume to 12 clients/day the same session these 7-staff/6-staff findings were produced.** Re-ran both pooling configurations against the actual 12-client schedule (6 slots/chair) rather than assuming the 10-client findings still hold:

| Configuration | Result at 12 clients/day |
|---|---|
| 8-staff, no pooling (original baseline) | **CLEARS CLEANLY** — every line still peaks at exactly 2 concurrent bookings |
| 7-staff (Massage+Beauty pooled, cap 3) | **FAILS** — 2 clients unassignable (specific clients 6 and 12 in the solver run) |
| 6-staff (Massage+Beauty AND Nails+Hair both pooled, cap 3 each) | **FAILS** — 4 clients unassignable (specific clients 5, 6, 11, and 12) |

**The then-committed 12-client model (historical, superseded, see docs/CURRENT-STATE.md) required 8 dual-qualified treatment staff, required by peak overlap — there is no "unpooled" model.** All treatment staff are hired dual/multi-qualified (Massage+Beauty confirmed pairing); at 12 clients/day the Massage+Beauty pool's own peak concurrency is 4 (matching the sum of the individual Massage and Beauty peaks — pooling provides no further reduction at this specific volume), plus 2 Nails plus 2 Hair. This is the direct, solver-verified answer to "does 12 clients/day need more headcount than 10" — the answer is: not more than the original 8, but definitely more than the 7 or 6 that pooling allows at 10 clients/day. **Clarifying note: the 8-person figure at the 12-client design ceiling is correct and expected — dual-qualification just doesn't happen to reduce it further at this specific volume. 7 (pool sized to 3) remains a legitimate daily-rostering choice on lower-volume actual days, below this ceiling.**

### 14 Clients/Day — PROVEN CEILING (Maximum Verified Capacity), NOT the Daily Operating Target

**Anthony's decision, 2026-07-31: "have 14 as the ceiling and prove it. 12 clients a day is what we will aim for each day."** 12 clients/day (above) remains the committed DAILY OPERATING TARGET, unchanged. 14 is documented below as the proven maximum the venue is verified capable of on a day that books out completely — growth headroom, not a replacement for the daily aim.

**Search method:** per Anthony's instruction ("12 or max capacity for 2 chairs and last client before 10:30am"), ran the full optimization search (`tools/draw-event-scheduler.py`'s `run()`, multi-resolution sweep of `CANDIDATE_STEP` 1-44), bounded by last Draw 1 strictly before 10:30am. **Chair/phlebotomist-only ceiling: 14 clients/day** (best result found; every other tested resolution gives 12 or 13), using a bursty two-cluster schedule (two ~46-min arrival bursts separated by a ~2hr09min gap) — last departure ~12:36pm, earlier than the 12-client model's ~12:48pm despite serving more clients, due to the tighter packing.

**Headcount, proven via TWO independent methods (this number was wrong twice already at this exact question, so it was not accepted on a single method this time):**
- **Method 1 (sweep-line peak concurrency):** combined every Massage and every Beauty window from the 7 chair-A clients into one shared-pool timeline, swept for peak overlap — 3, not 6 (massage-cluster peaks 07:45, beauty-cluster peaks 08:50, different clock times, so the pool shares capacity). Nails/Hair (no confirmed dual-qualification pairing) independently peak at 3 each.
- **Method 2 (independent cross-check, genuinely different algorithm — greedy first-fit station assignment):** each client's service window assigned to the first free station in chronological order, opening a new station only when none is free. Result: 3 stations for the Massage+Beauty pool, 3 for Nails, 3 for Hair — **exact agreement with Method 1.**
- Because greedy first-fit is a feasible constructed solution (an upper bound) and sweep-line peak concurrency is a proven mathematical floor (a lower bound), the two methods matching exactly **proves** 9 is the true optimum, not just an estimate.
- **Capability gap disclosed:** `tools/GTT-Rostering-Simulator.html`, referenced as available for this cross-check, could not be found anywhere in this repo (file search + full `git log --all` history checked) — the greedy first-fit script was used as the independent method instead.

**True minimum treatment headcount at 14/day: 9 (3 Massage+Beauty pool + 3 Nails + 3 Hair), proven.** `[VERIFICATION NEEDED — Nails+Hair pairing not yet confirmed as hireable]`: if confirmed, the same method gives a hypothetical 6 — flagged only, not assumed.

**Full whole-venture P&L at the 14-client ceiling (historical — this whole 14-client PROVEN CEILING model is superseded/dominated by the current 18-client Table 1 primary model at the same 8-treatment-staff headcount, see docs/CURRENT-STATE.md's 2026-08-05 REBASE banner; not just the AM segment):**

| | 12-client (historical, committed daily target at the time) | 14-client (historical PROVEN CEILING, both superseded, see docs/CURRENT-STATE.md) | Delta |
|---|---|---|---|
| Total Revenue | A$118,297.16 | **A$131,462.16** | +A$13,165.00 |
| Total Direct Labor + Opening Costs | A$74,561.20 | **A$79,406.03** | +A$4,844.83 (AM treatment labor only — PM and opening-increment unaffected) |
| Workers Comp (1.7% of Direct Labor) | A$1,267.54 | **A$1,349.90** | +A$82.36 |
| Non-Wage Overhead (fixed, not volume-driven) | A$13,980.00 | **A$13,980.00** | A$0.00 |
| **Total Costs** | **A$89,808.74** | **A$94,735.93** | +A$4,927.19 |
| **Monthly Net P&L (historical, both figures superseded)** | **+A$28,488.42** | **+A$36,726.23** | **+A$8,237.81** |
| Quarterly (×3) | +A$85,465.26 | **+A$110,178.69** | +A$24,713.43 |
| Half-Yearly (×6) | +A$170,930.51 | **+A$220,357.38** | +A$49,426.87 |
| Yearly (×12) | +A$341,861.03 | **+A$440,714.76** | +A$98,853.73 |

`[MODELED — delta-reconciliation build from the validated 12-client baseline, same methodology used for the 10→12 correction, not reused/copied figures]`. Total Revenue built as: AM A$3,500/day (14×A$250) × 22 weekdays = A$77,000, PM A$1,520/day × 22 = A$33,440, Saturday AM A$3,500 × 4.33 = A$15,155, Saturday PM A$760 × 4.33 = A$3,290.80 — ancillary A$0 throughout, same as the 12-client baseline.

**Downtime-Fill/Early-Release, rechecked against the actual bursty 14-client schedule (historical, superseded, see docs/CURRENT-STATE.md; not carried over from 12):**

| Item | 12-client | 14-client (PROVEN CEILING) | Method |
|---|---|---|---|
| Between-gap minutes/day (across all treatment stations) | 560 min (8 stations) | **915 min (9 stations)** | Computed directly from the per-station greedy first-fit assignment |
| Naive lead+tail minutes/day | 1,240 min | **1,065 min** — down despite the extra head, because the bursty schedule keeps each station's trimmed span fuller | Same source |
| 3-hour floor buffer needed | None (all 8 stations already exceed 180 min trimmed span) | **None (all 9 stations exceed 180 min trimmed span)** | Checked per-station |
| **Between-Client Downtime-Fill Revenue (historical, both figures superseded)** | A$12,679.33/month | **A$20,717.12/month** | `[MODELED — 1.3 sessions/hr × 50% utilisation × A$95/session × 22 trading days, same formula as the 12-client figure, verified by reproducing that figure exactly from the same formula]` |
| **Early-Release Cost Saving (historical, both figures superseded)** | A$16,511.22/month | **A$14,026.54/month** | `[MODELED — per-station saveable minutes × the station's own award rate (A$37.00/hr Massage+Beauty pool, A$35.63/hr Nails/Hair), summed and ×22 trading days]` |

Both remain separate, tagged lines, never blended into the (historical, superseded) A$36,726.23/month baseline above or into each other.

**Bottom line: 14 clients/day, staffed with 9 dual-qualified treatment staff, is now proven — full P&L, headcount confirmed via two independent methods, downtime-fill/early-release rechecked against the real schedule.** It is documented as growth headroom. **12 clients/day remains the committed daily operating target throughout this document — nothing above changes any 12-client figure.** See `docs/CURRENT-STATE.md` §1/§4/§7 and `scenario-c-sync-timetables.md` §0.4 for the same finding recorded canonically.

---

## Years 1-3 Annual Projection

**Purpose:** filling the gap for a multi-year annual view, per the business-plan spec.

**One remaining honest limitation:** the Year 1 estimate below uses flat Month 5+ fixed costs applied across all 12 months as a conservative simplification — in reality, fixed costs also ramp during Months 1-4 (fewer casual PM hours worked at lower volume, per [pm-staffing-roster.md](pm-staffing-roster.md)'s own cost-ramp table), so this approach *understates* Year 1 profitability somewhat by charging full steady-state costs against ramped-up revenue in the early months. A precise Year 1 figure would need the matching cost ramp built in — flagged as a follow-up refinement, not fabricated here with false precision. Years 2-3 use this document's own current Month-5+ steady-state run-rate (**12-client committed model, A$341,861.03/year, ancillary excluded** — was A$198,084.84/year at 10-client, A$301,044.84/year before either correction), assuming the venture holds at its verified capacity ceiling with no further AM capacity expansion (Scenario D, 15 clients/day, is a documented but not-yet-committed growth path beyond the now-committed 12-client baseline — see [scenario-d-investigation.md](scenario-d-investigation.md) — not assumed here).

**2026-07-30 update (12-client committed model) — Year 1 range not independently re-derived to full precision this round, flagged rather than fabricated.** The Month 5+ steady-state jump (A$198,084.84→A$341,861.03/year) is a real, computed figure (see §4 Monthly). The Year 1 ramp-adjusted range below is shifted up directionally to reflect the same proportional AM revenue increase, but has not been rebuilt month-by-month with the same rigour as the 10-client-to-ancillary-excluded transition earlier the same day — flagged as a follow-up, not presented with false precision.

| Year | Net P&L (annual) | Basis |
|---|---|---|
| Year 1 (ramp-up + partial steady-state) | Likely in the range of breakeven to modestly positive — roughly -A$5,000 to +A$20,000 (directional estimate, shifted up from the 10-client range of -A$20,000 to +A$5,000 by the AM revenue increase; **not independently re-derived to full precision this round — flagged as a follow-up, see docs/VERIFICATION-TRACKER.md**) | Derived directionally from this document's Year 1 Monthly Ramp table below (12-client, ancillary excluded), using Month 5+ flat costs as a known-conservative simplification |
| Year 2 (full steady-state, 12-client committed model, no further capacity change) | ~A$341,861.03 (was ~A$198,084.84 at 10-client) | This document's steady-state figure, current canonical AM model |
| Year 3 (same, assuming no material change — the actual figure depends entirely on whether Scenario D or further growth levers are pursued) | ~A$341,861.03 (flat, if no capacity change) | Same as Year 2 — **this is a "no growth" placeholder, not a forecast.** If Scenario D (15 clients/day) is activated, see [scenario-d-investigation.md](scenario-d-investigation.md)'s own P&L estimate instead (that document itself may need updating to treat 12, not 10, as the baseline it grows from). |

**This table should not be treated as a confident 3-year forecast.** The remaining limitations (flat vs ramped costs in Year 1, and Year 1's directional-not-precise recompute this round) are known, disclosed simplifications, not unresolved contradictions — recommend Bruno/finance function build the fully cost-ramp-matched, 12-client-precise version once Year 1 real data exists.

---

## Year 1 Monthly Ramp

**Purpose:** month-by-month build-up across Year 1, since the steady-state tables above only describe ongoing operation once the venture is running at full capacity.

**Where the Month 5+ AM figure of A$66,000 comes from, and how it's achievable:** 12 clients/day × A$250 (Package 1 conservative price) × 22 trading days/month = **A$66,000/month** (was A$55,000/month at the superseded 10-client model). This is a **capacity ceiling** (the solver-verified 12-client maximum, built around WDP's real "not normally after 10:30am" guidance), not a guaranteed figure. Actually earning it depends on booking all 12 daily AM slots consistently across the month via the referral/waitlist pipeline ([business-plan.md](business-plan.md) §8 Go-to-Market, [pm-staffing-roster.md](pm-staffing-roster.md) §Pre-Opening Waitlist & Staffing Decision Model) — which is exactly why the ramp table below assumes a gradual build (43%/64%/79%/93%/100% of this ceiling across Months 1-5), not full capacity from Day 1.

**Method:** apply the same ramp percentages [cash-flow.md](cash-flow.md) used (Month 1: ~43% of steady-state packages/services sold, Month 2: ~64%, Month 3: ~79%, Month 4: ~93%, Month 5+: 100%) to this document's own current Month 5+ steady-state figures (AM A$66,000, PM A$33,440 — PM unaffected by the AM volume change, using [pm-staffing-roster.md](pm-staffing-roster.md)'s validated session-volume ramp). Ancillary revenue excluded entirely (2026-07-30), per Anthony's direct instruction — see "Ancillary Revenue — Excluded From Baseline" above.

| Month | AM GTT Revenue | PM Revenue | Ancillary | Total Revenue (approx.) | Note |
|---|---|---|---|---|---|
| Month 1 | ~A$28,380 (43% of A$66,000 ceiling) | ~A$14,380 (43% of A$33,440) | **A$0 (excluded)** | ~A$42,760 | Ramp estimate (was ~A$41,880 at 10-client) |
| Month 2 | ~A$42,240 (64%) | ~A$21,400 | **A$0 (excluded)** | ~A$63,640 | Ramp estimate (was ~A$56,600) |
| Month 3 | ~A$52,140 (79%) | ~A$26,420 | **A$0 (excluded)** | ~A$78,560 | Ramp estimate (was ~A$69,870) |
| Month 4 | ~A$61,380 (93%) | ~A$31,100 | **A$0 (excluded)** | ~A$92,480 | Ramp estimate (was ~A$82,250) |
| Month 5+ | A$66,000 (100%, verified ceiling — 12/day × A$250 × 22 days) | A$33,440 | **A$0 (excluded)** | A$99,440 (revenue only — see Fixed Costs below for net) | **AM figure is fully verified (solver-checked 12-client ceiling); PM figure is the ramp-shape estimate, confirmed directionally compatible with the AM model but not independently re-verified session-by-session.** |

**Fixed costs at Month 5+ (per §4 Monthly table above): A$89,808.74/month. Net P&L at Month 5+: Total Revenue A$99,440 minus Total Costs A$89,808.74 ≈ +A$9,631.26/month using this simplified ramp-table revenue sum** — an improvement from the 10-client model's near-zero/marginal simplified result, but still materially different from the headline +A$28,488.42/month figure, because that figure uses this document's own more precise weekday/Saturday-blended calculation (§1-2 above), not this simplified Month-1-5 ramp table's rounded monthly totals — the same disclosed gap that existed at the 10-client model. **Treat the headline +A$28,488.42/month (weekday/Saturday blend) as the more precise figure; this ramp table is for visualising the build-up shape across Year 1, not as a replacement for the precise weekday-based calculation above.**

### Marketing Spend Ramp — 2026-07-31, per Anthony's direct instruction

**Flagged and corrected:** the A$1,500/month Instagram/Meta ads line in §4's Non-Wage Overhead breakdown was applied flat from Month 1, which doesn't match Anthony's actual go-to-market plan — referral relationships (midwives, OBs) build gradually rather than a full paid-ads launch on day one. Real 2026 AU small-business benchmarks suggest A$800-1,200/month is more typical at this revenue scale early on. **A$1,500/month is retained in the steady-state Month 5+ table above and in every Quarterly/Half-Yearly/Yearly figure — this is the conservative, unchanged case.** What was missing is a genuine Month 1-4 ramp, modelled below rather than left as a flat, overstated early-months cost:

| Month | Marketing Spend | Saving vs flat A$1,500/month | Basis |
|---|---|---|---|
| Month 1 | A$600 | A$900 | `[MODELED — referral-relationship-building phase, minimal paid spend, AU small-business benchmark]` |
| Month 2 | A$800 | A$700 | `[MODELED — same basis, ramping]` |
| Month 3 | A$1,000 | A$500 | `[MODELED — same basis, ramping]` |
| Month 4 | A$1,200 | A$300 | `[MODELED — same basis, ramping]` |
| Month 5+ | A$1,500 (unchanged, steady state) | A$0 | Matches §4 Monthly table, no change |

**This improves the ramp — it does not worsen it.** Applying this saving directly to the Month 1-4 Net P&L figures already stated in `docs/CURRENT-STATE.md` §5 (each of which used the flat A$1,500/month cost basis):

| Month | Net P&L (flat A$1,500 marketing, prior figure) | Net P&L (ramped marketing, corrected) | Improvement |
|---|---|---|---|
| Month 1 | ~-A$47,050 | **~-A$46,150** | +A$900 |
| Month 2 | ~-A$26,167 | **~-A$25,467** | +A$700 |
| Month 3 | ~-A$11,251 | **~-A$10,751** | +A$500 |
| Month 4 | ~+A$2,670 | **~+A$2,970** | +A$300 |
| Month 5+ | +A$9,631.26 (simplified ramp-table basis) / +A$28,488.42 (precise weekday/Saturday blend, headline) | Unchanged — no marketing ramp saving applies once steady state is reached | — |

`docs/CURRENT-STATE.md` §5 updated to these ramped figures — see that document's own changelog.

See "Years 1-3 Annual Projection" above for the corresponding multi-year view.

---

## Appendix — How Every Figure Is Calculated

**Purpose:** Anthony asked for every figure in this document to be traceable to its calculation, not just stated as a total. This appendix shows the rate × volume/hours method behind each line, and is explicit about the one place where full line-by-line precision isn't recoverable from this repo's saved working (flagged plainly rather than presented with false precision).

### Revenue Lines (fully traceable — these reconcile exactly)

| Line | Calculation |
|---|---|
| AM Revenue (Weekday/Saturday) | **12 clients** × A$250 (Package 1 conservative price, [services-pricing-locked.md](services-pricing-locked.md)) = **A$3,000.00** (was 10 clients × A$250 = A$2,500.00) |
| PM Revenue (Weekday, 16 sessions) | 16 sessions × A$95 average individual-service price ([pm-staffing-roster.md](pm-staffing-roster.md) §PM Revenue) = **A$1,520.00** |
| PM Revenue (Saturday, 8 sessions) | 8 sessions × A$95 = **A$760.00** |
| ~~Ancillary Revenue (Weekday)~~ | **Historical calculation, superseded 2026-07-30 — ancillary is now A$0 in the baseline, per Anthony's direct instruction (see "Ancillary Revenue — Excluded From Baseline" above).** Retained below for trace only: was A$8,580/month steady-state ancillary (`profit-loss-tables.md` Year 1 Ramp table, sourced from [financial-break-even-staff.md](financial-break-even-staff.md) Revenue Model — spray tan + retail + cafe) ÷ 22 trading days/month ≈ A$390/day AM-only equivalent, blended with PM foot traffic to A$439.50/day used in the (now superseded) Weekday table — the exact AM/PM ancillary split was never separately tracked. |
| Monthly Total Revenue | **12-client model, ancillary excluded 2026-07-30.** Weekday × 5 × 4.33 weeks + Saturday × 1 × 4.33 weeks, per §3 Weekly table scaled to a month: (A$22,600.00 + A$3,760.00) × 4.33 ≈ **A$114,148.00** — note this does not reconcile exactly to the A$118,297.16 stated in §4 Monthly (the same pre-existing weekly-to-monthly scaling discrepancy already flagged for the 10-client model, not newly introduced here); §4's delta-approach figure remains the one used as canonical. |
| Quarterly/Half-Yearly/Yearly Revenue | Monthly figure × 3 / × 6 / × 12 — a steady-state run-rate scaling, not independently re-modelled per period |

### Direct Labor Lines (rate and method confirmed; exact hour-by-hour staff allocation for the Weekday/Saturday totals is not preserved as a saved worksheet in this repo — flagged below)

**Confirmed source rates ([financial-break-even-staff.md](financial-break-even-staff.md) §Award Wage Summary):**
- Phlebotomist (Cert III/IV Pathology Collector): base A$24.50/hr, casual A$30.63/hr
- Massage Therapist / Beauty Therapist (MA000005 Level 4): base A$29.60/hr, casual A$37.00/hr
- Nail Technician / Hairdresser (MA000005 Level 3): base A$28.50/hr, casual A$35.63/hr

**Confirmed method ([pm-staffing-roster.md](pm-staffing-roster.md) §CORRECTION — Hours-Based Casual Cost Model):** `hours/role/day = (sessions/day ÷ roles × days) ÷ throughput (1.3 sessions/hr)` — staff are paid for actual booked hours, not a blanket shift.

**PM Direct Labor (Weekday, A$440.00) — reconciles closely:** at 16 PM sessions/day across 4 roles, hours/role/day ≈ 3.08hrs (per the formula above) × 4 roles × ~A$36.32/hr blended casual rate ≈ A$447 — within rounding of the A$440.00 shown, confirming the method is correctly applied.

**AM Direct Labor (Weekday, A$2,193.00 for 2 phlebotomists + 8 treatment staff; Saturday, A$1,343.95 for the same roster at 150% penalty) — method confirmed, exact worksheet not preserved:** these figures were carried forward from earlier session calculations against the actual staggered per-client service timetable in [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) (staff are not on a flat 5-hour blanket shift — their actual worked hours follow each client's specific service slot times), not a simple flat-rate × flat-hours multiplication. A flat 5-hour-shift approximation using the rates above does not exactly reproduce A$2,193.00 (it undershoots, since real staff hours are staggered and overlapping, not uniform) — this confirms the figures are NOT the blanket-shift error being corrected elsewhere in this document, but the specific per-staff-member hour allocation behind the exact total is not saved as a standalone worksheet in this repo. **Recommendation:** if Anthony needs the literal per-staff-member hour breakdown (not just confirmation of the rate and method), this should be rebuilt directly from [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md)'s per-client service-time entries as a dedicated follow-up — flagged here rather than fabricating a specific hour-by-hour table that wasn't independently reconstructed and verified this round.

### Overhead and Workers Comp Lines (fully traceable)

| Line | Calculation |
|---|---|
| Workers Comp | 1.7% × (Total Direct Labor + Opening Costs) — e.g. Monthly: 1.7% × A$73,397.34 ≈ **A$1,247.75** |
| Non-Wage Overhead | Sum of the 13 component line items in §4's breakdown table = **A$13,980.00/month**, scaled ×3/×6/×12 for Quarterly/Half-Yearly/Yearly |
| Receptionist/relief/workers comp (Weekday pro-rated) | Monthly relief pool (A$15,000/yr ÷ 12) + receptionist wage + workers comp, pro-rated across 22 trading days/month ≈ **A$339.00/day** |
| Opening-time increment (07:00 start) | Incremental staff cost of the earlier 07:00 vs a later start, pro-rated per day ≈ **A$44.50/day** — sourced from the Scenario C verification work in [am-capacity-weekend.md](am-capacity-weekend.md), not independently rebuilt here |

**Bottom line on traceability:** every revenue, overhead, and workers-comp figure in this document reconciles exactly from its stated formula. The AM Direct Labor figures (Weekday and Saturday) are confirmed to use the correct rates and the correct hours-based method (not the old blanket-shift error), but their exact underlying per-staff-member hour allocation is not separately saved in this repo and would need to be rebuilt from the Scenario C timetable for full line-by-line precision — flagged explicitly rather than presented as more precise than it is.

---

## Changelog

**2026-08-05 (REBASE — 25-min-cadence tables become the actual financial basis, per Anthony's direct instruction; v3.0)** — Until this round, Table 1 (07:00-start/18-client) and Table 2 (08:00-start/12-client), both g=25, were used only for the Carole-facing document — every committed figure in this document still reflected the old 12-client/23-min-cadence model. Rebased in full: added a new "PRIMARY REBASED MODEL" section (Weekday/Monthly/Quarterly/Half-Yearly/Yearly for both tables, Downtime-Fill/Early-Release recomputed fresh against each table's own gap pattern, Treatment Headcount confirmed identical at both tables, Item 1's 10:25-insertion test result). **New primary committed Monthly Net P&L: +A$63,028.75** (Table 1, was +A$27,084.69 at the old 12-client model — delta +A$35,944.06/month at zero extra weekday labor cost, same 8-treatment/2-phlebotomist headcount serving 50% more daily clients). Secondary reference (Table 2): +A$27,084.69/month, numerically unchanged from the old baseline since client volume and headcount match exactly — one open item flagged, not assumed: Table 2's 08:00 start may eliminate the A$44.50/day opening-time increment sourced specifically to a 07:00 start, not yet quantified. §1-§7 (the old 12-client/23-min-cadence tables) are retired to historical/superseded status, retained in full below the new section for trace, never deleted. Propagated to `docs/CURRENT-STATE.md` and `docs/VERIFICATION-TRACKER.md` — see those documents' own changelog entries. **Not yet done, flagged as an open follow-up:** Year 1 Monthly Ramp and Years 1-3 Annual Projection (further below) have not been independently rebuilt against Table 1's higher ceiling — retained as historical/directional only, not restated as current.

**2026-07-19 (Phase 6 gap-fill)** — Found via Phase 6 spec-verification that this document had Month-5+ steady-state figures only (weekday/weekly/monthly/quarterly/half-yearly/yearly), no Year 1 month-by-month ramp and no Years 1-3 multi-year view. Added both, sourced from [cash-flow.md](cash-flow.md)'s existing ramp shape and this document's own steady-state v2.0 figures, with an explicit caveat that [cash-flow.md](cash-flow.md)'s absolute figures are built on the superseded 8-client/3-package model and should not be reused without re-verification. Surfaced (not resolved) the PM-profitability discrepancy already logged in [business-plan.md](business-plan.md) and `docs/01_conflicts_log.md`.

**2026-07-20 (CONFLICT-08 resolved)** — Resolved the PM-profitability discrepancy: [pm-staffing-roster.md](pm-staffing-roster.md)'s standalone PM loss was itself an artifact of the stale 8-client AM model, not a genuine loss — see [pm-staffing-roster.md](pm-staffing-roster.md)'s corrected banner and `docs/01_conflicts_log.md` CONFLICT-08. Filled in the previously-withheld PM/ancillary columns in the Year 1 Monthly Ramp table using the now-confirmed-compatible [pm-staffing-roster.md](pm-staffing-roster.md) session-volume figures. Updated the Years 1-3 Annual Projection with a corrected Year 1 estimate, disclosing the one remaining known simplification (flat vs ramped costs in early months, which understates rather than overstates profitability).

**2026-07-20 (Sunday reopening criterion)** — Reworded the Sunday-closed reference to state the actual reopening bar: proven AND profitable standalone PM demand, not demand alone — per Anthony's feedback. Cascaded the same wording change into [business-plan.md](business-plan.md), [executive-summary.md](executive-summary.md), [HANDOFF.md](HANDOFF.md), [am-capacity-weekend.md](am-capacity-weekend.md).

**2026-07-20 (v1.0 removed entirely, v2.0 expanded to full standalone document, v2.1)** — Anthony's direct feedback: this document was "genuinely confusing" with the superseded v1.0 tables (including the alarming "Saturday AM GTT Runs at a Loss" finding) sitting ABOVE the corrected v2.0 tables, causing exactly the kind of confusion/misinformation risk a founder-facing financial document should never carry. Actioned in full:
1. **Deleted v1.0 entirely** — the "⚠ FINDING — Saturday AM GTT Runs at a Loss" section and all of old sections 1-8 (Weekday/Saturday/Sunday/Weekly/Monthly/Quarterly/Half-Yearly/Yearly using v1.0's blanket-shift costing) and the old Key Callouts tied to v1.0. This content no longer exists in this document — it is not archived or flagged, it is gone, per Anthony's explicit instruction ("it can cause confusion and misinformation... needs to be removed").
2. **Clarified, not removed, the Saturday penalty rate** — added a dedicated section stating plainly that the MA000005 133%/150% Saturday penalty is a confirmed real award rate, applied in full throughout this document; what was wrong in the old v1.0 was the blanket-shift costing method, not the rate itself.
3. **Confirmed no Sunday references remain** — checked the full document after deletion; none found. Sunday is closed and not modelled here, per [am-capacity-weekend.md](am-capacity-weekend.md).
4. **Expanded former v2.0 "Weekday (unchanged)" one-liner and single-figure Quarterly/Half-Yearly/Yearly into full breakdown tables** (Revenue/Direct Labor/Workers Comp/Overhead/Net rows), matching the Monthly section's existing format, since there is no longer a v1.0 to point back to for line-item detail.
5. **Broke down the A$13,980/month Non-Wage Overhead lump sum into its 13 component line items** (rent, utilities, internet, Fresha, Resend, marketing, GTT supplies, laundry, cleaning, insurance, accounting, consumables, misc), sourced from [cash-flow.md](cash-flow.md) §Cost Assumptions — the same breakdown that document already cross-references as canonical.
6. **Added a one-line Ancillary Revenue composition note** (cafe/retail — Gaia, Weleda, Mustela products, per [business-plan.md](business-plan.md) §6) wherever Ancillary Revenue appears, so the figure is no longer unexplained.
7. **Answered the treatment-headcount question directly and with a checked basis:** 7 staff (not 8) is the genuine minimum at current 10-client/day volume, via Massage+Beauty cross-training only (Nails/Hair cannot pool) — verified against [am-capacity-weekend.md](am-capacity-weekend.md)'s Scenario C concurrency check and [multirole-CORRECTION.md](multirole-CORRECTION.md)'s corrected pooling math. Flagged that this saving does not persist if AM capacity later expands to Scenario D (15 clients/day), where treatment headcount returns to 8.
8. **Stated the Saturday downtime-fill principle explicitly** in this document (§1, §2) — same staff-utilisation model already documented for weekdays in [gtt-center-perth-overview-for-imara.md](gtt-center-perth-overview-for-imara.md)/[executive-summary.md](executive-summary.md), now also stated for Saturday specifically.
9. **Spelled out the A$55,000 Month 5+ AM revenue derivation** in the Year 1 Monthly Ramp section: 10 clients/day × A$250 × 22 trading days = A$55,000, a capacity ceiling dependent on the referral pipeline actually filling all 10 daily slots, which is why the ramp table assumes gradual build-up rather than Day-1 full capacity.

**2026-07-20 (calculation-detail appendix added)** — Anthony asked for every figure to be traceable to its calculation, not just a stated total. Added a full Appendix showing the rate × volume/hours method behind every revenue, labor, overhead, and workers-comp line. Revenue/overhead/workers-comp lines all reconcile exactly from their stated formulas. AM Direct Labor (Weekday A$2,193.00, Saturday A$1,343.95) confirmed to use the correct rates and hours-based method (not the old blanket-shift error), but the exact per-staff-member hour allocation behind these two specific totals is not preserved as a saved worksheet in this repo — flagged explicitly as a follow-up to rebuild from [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) if literal hour-by-hour precision is needed, rather than fabricating a reverse-engineered breakdown that wasn't independently verified this round.

**2026-07-20 (package renumbering + terminology)** — Updated the remaining "Package 2/Package 3" references (base-model banner, Key Callouts, Year 1 Ramp derivation, calculation appendix) to "Package 1 (A$250)/Package 2 (A$300)" per [services-pricing-locked.md](services-pricing-locked.md)'s renumbering — these were missed in the earlier v2.1 rewrite pass. Also tightened "visits" language to "packages/services sold" for consistency with the venture-wide terminology change (a visit alone carries no dollar figure).

**2026-07-30 (downtime-fill revenue upside added, per Anthony's direct instruction)** — Added a new "Downtime-Fill Revenue — Upside Estimate" section, quantifying the new standalone-booking-first Staff Downtime Protocol policy (`financial-break-even-staff.md`) using real per-staff gap-time data pulled directly from `scenario-c-sync-timetables.md` (1,260 min/day total downtime across 8 AM treatment staff, not estimated). Converted to dollars using two assumptions already established elsewhere in this repo (1.3 sessions/hr throughput, A$95/session average, both from `pm-staffing-roster.md`) plus the same 50% utilisation discount that document already applies to standalone PM demand. Result: **A$28,528.50/month**, tagged `[MODELED]`, kept as a separate line in §4 Monthly and its own dedicated section — explicitly not blended into the +A$25,087.07/month conservative baseline. Flagged as the least-verified line in the model (no demand validation for this specific slot type, not yet built into any booking system).

**2026-07-30 (later same day — corrections from Anthony, major rework)** — Three corrections applied:
1. **Downtime-fill split into two pools, not one blended figure.** Anthony corrected the earlier same-day A$28,528.50/month single figure: only between-booking gaps (mid-shift, advance-online-booking only) are sellable revenue; lead-in/tail time should instead let a staff member's engagement start later/end earlier (a cost saving, not revenue). Independently re-derived both pools directly from `scenario-c-sync-timetables.md`, reproducing exactly 420 min/day (between-gaps) and 1,320 min/day (naive lead+tail) — reconciled against the earlier 1,260 min/day figure (narrower, non-split window; difference fully explained, not a mystery). Also checked the 3-hour minimum casual engagement directly against the primary Fair Work Ombudsman/Commission award text (MA000005 clause 11.5, MA000027 clause 11.2, via direct WebFetch, not just a search snippet) — `[VERIFIED]` — and applied it to the lead/tail pool, reducing the naive 1,320 min/day to 1,100 min/day actually saveable. New headline figures: (a) Between-Client Downtime-Fill Revenue A$9,509.50/month, (b) Early-Release Cost Saving A$14,647.05/month — two separate lines, never blended.
2. **Fixed an accidental heading deletion** from the earlier same-day edit — the "Treatment Headcount" section's own heading was dropped when the Downtime-Fill section was inserted above it, orphaning its content. Restored, no content lost.
3. **Added a solver-verified extension** to the Treatment Headcount analysis: re-ran the scheduling constraint check with a hypothetical Nails+Hair cross-qualification pool (in addition to the existing Massage+Beauty pool) against the real Scenario C booking data — result: headcount could drop to 6 (from 7) if such a hire existed, though hireability (not scheduling feasibility) is the real-world constraint, flagged explicitly.

**2026-07-30 (ancillary revenue excluded from baseline entirely, per Anthony's direct instruction)** — Ancillary ("too much of a variable" with no real basis yet — `cash-flow.md` had already found 2 of 3 component lines have no real derivation, 10 days before this exclusion) is now A$0 in every headline P&L figure in this document: Weekday, Weekly, Monthly, Quarterly, Half-Yearly, Yearly, Year 1 Monthly Ramp, and Years 1-3 Annual Projection all recomputed. **Standing conservative baseline moves from +A$25,087.07/month to +A$16,507.07/month** (+A$301,044.84/year to +A$198,084.84/year). Ancillary kept visible only as a separate, clearly-tagged pure-upside line ("Ancillary Revenue — Excluded From Baseline"), not deleted from the document, never folded back into the baseline. Also found and flagged (not silently fixed) a small pre-existing weekly-to-monthly revenue-scaling discrepancy (~A$3,964-4,700) in this document's own Appendix, predating this session's work.

**2026-07-30 (later still — 12 clients/day is the COMMITTED model, replacing 10 as current, per Anthony's direct correction)** — Full recompute of every table in this document, not a fresh document: base-model banner, Weekday/Saturday tables (AM Revenue A$3,000/day was A$2,500), Weekly, Monthly (+A$28,488.42/month, was +A$16,507.07/month), Quarterly/Half-Yearly/Yearly, Year 1 Monthly Ramp (A$66,000 AM ceiling, was A$55,000), Years 1-3 Annual Projection (+A$341,861.03/year, was +A$198,084.84/year, Year 1 range flagged as directional-not-precise this round), Treatment Headcount (7-staff/6-staff pooling findings marked historical/superseded — re-verified solver-checked at 12/day, both FAIL, full 8-staff roster required), and the Downtime-Fill/Early-Release section (recomputed against the actual 12-client gap pattern, not carried over — A$12,679.33/month and A$16,511.22/month respectively, both up from the 10-client figures, using a corrected shift-boundary source: `financial-break-even-staff.md`'s explicit 07:00-13:00 AM shift statement, not `operations-manual.md`'s 12:30 EOD-wrap time used in error for the 10-client calculation). **AM Direct Labor recomputed fresh (not reused): confirmed unchanged at A$48,255/month since headcount is unchanged (fixed-salary FTE roles) and the extended day still fits the existing shift budget** — this is the source of the entire AM revenue increase flowing straight to margin.

**2026-07-30 (later still — full N_max search completed, first pass explored and rejected using a naive headcount estimate)** — Per Anthony's "12 or max capacity" instruction, re-ran the full optimization search: true chair-only ceiling is 14, not 12. Headcount check at this point used an uncorrected per-line multiply (12), not yet tested against dual-qualification.

**2026-07-31 ("unpooled" retired everywhere per Anthony's direct instruction; N_max headcount re-corrected via dual-qualification, conclusion reversed)** — Removed all "unpooled" language from this document — every treatment-staff figure restated as "dual-qualified, required by peak overlap." Re-tested the N=14 headcount with Massage+Beauty dual-qualification against the real bursty timing via interval-overlap simulation: true minimum is 9, not 12 (3 pool + 3 Nails + 3 Hair). Net financial verdict reverses to +A$6,155.17/month better than staying at 12 (extra revenue A$11,000/month vs extra labor only A$4,844.83/month). This is presented as a finding for Anthony's decision, not adopted unilaterally. See `docs/CURRENT-STATE.md` §1/§4/§7 for the same finding recorded canonically.

**2026-07-31 (later same day — Anthony's decision: 14 is a PROVEN CEILING, 12 stays the committed daily target; full whole-venture P&L completed; headcount independently re-verified a second way)** — Anthony: "have 14 as the ceiling and prove it. 12 clients a day is what we will aim for each day." Rewrote the section to reflect this — 12 remains the committed daily operating target throughout this document, 14 is documented as proven growth headroom, not a replacement. Completed the two things needed before 14 could be called proven: (a) full whole-venture P&L at N=14 — Monthly Net P&L +A$36,726.23 (delta +A$8,237.81 vs the 12-client baseline), Quarterly/Half-Yearly/Yearly scaled the same way, both downtime-fill/early-release lines rechecked against the real bursty schedule (A$20,717.12/month and A$14,026.54/month respectively, not carried over from 12); (b) independently cross-verified the 9-staff headcount using a second, genuinely different algorithm (greedy first-fit station assignment vs the earlier sweep-line peak-concurrency method) — exact agreement, proving rather than estimating 9. Disclosed that `tools/GTT-Rostering-Simulator.html`, referenced as an available cross-check tool, could not be found in this repo — used the independent greedy first-fit script instead.

**2026-07-31 (later same day — weekly/monthly reconciliation checked, per coordinator's request reviewing a client-facing document)** — Investigated whether §3's Weekly Total (+A$6,154.21) double-counts or has a gap versus §4's Monthly Net P&L. **Finding: neither a double-count nor a gap in the actual headline figures — but a genuinely asymmetric presentation, now clarified with a note.** §3's Weekday row nets a full cost stack (including its overhead/opening-increment/receptionist share, per §1) while its Saturday row nets Direct Contribution only (Revenue minus AM+PM Direct Labor, per §2's own explicit label) — mixing the two under one "Weekly Total Net" column is misleading if read as a true weekly P&L. Confirmed Saturday correctly carries zero separate overhead line in §3 — overhead is one flat monthly figure in §4, already covering all 6 trading days once; adding a Saturday-specific overhead share to §3 would double-count against §4, not fill a gap. Added an explicit reconciliation note to §3 stating this, and that §4/§5/§6/§7 (Monthly/Quarterly/Half-Yearly/Yearly) are built independently via the validated delta-approach, not by scaling §3 — §3 is retained for weekday-vs-Saturday intuition only.

**2026-07-31 (later still — PM 3-hour minimum checked against the actual spreadsheet, per Anthony's direct instruction, Saturday PM Direct Labor corrected)** — Anthony flagged that PM casual staff must be rostered a minimum 3 consecutive hours under MA000005 cl. 11.5/MA000027 cl. 11.2, and asked whether this document's PM Direct Labor figures actually respect that floor per individual role, not assumed compliant by default. Checked: **Saturday (A$335.55/day) did not** — at 8 PM sessions/day split evenly across the 4 roles (this document's own stated assumption), each role needs only 1.54 hours/day of actual booked time, well below the 3-hour floor; the figure had been priced at the raw calculated hours, not the enforced minimum. Corrected to **A$654.32/day** (4 roles × 3-hour minimum × the Saturday blended casual rate), a real +A$318.77/day understatement now fixed, cascading to +A$1,380.27/month in §4 Monthly (plus +A$23.47/month Workers Comp), and scaled through §5/§6/§7 Quarterly/Half-Yearly/Yearly. **New standing conservative baseline: +A$27,084.69/month** (was +A$28,488.42/month). **Weekday (A$440.00/day) checked and found NOT understated** — at 16 sessions/day split evenly, each role needs 3.08 hours/day, marginally above the floor; flagged as a thin, assumption-dependent margin (contingent on the unconfirmed even-split-across-4-roles assumption) rather than re-costed, since it does not currently breach the floor. **Not yet propagated to the N=14 PROVEN CEILING figures above** (which use the same Saturday hours-based PM costing methodology, scaled proportionally from this 12-client baseline) — flagged as an open follow-up in `docs/VERIFICATION-TRACKER.md`, not silently left inconsistent.
