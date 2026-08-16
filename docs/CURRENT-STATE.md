# GTT Center Perth — Current State (Canonical Numbers)

**Created:** 2026-07-29 | **Purpose:** The single canonical file for today's actual figures — package prices, client capacity, headcount, monthly net P&L, and startup capital range. Every other document in this repo defers to this file for these figures; they no longer independently restate them as sources of truth.

**Why this file exists:** an outside review of this repo found the financial model had moved 5+ times across different documents with contradicting numbers, false precision on a pre-revenue business, and a stale document (`operations-manual.md`) still training staff on an abandoned scheduling model 10 days after being flagged. This file exists to stop that pattern: one number per fact, one tag per number, one place to look.

**Tagging system — every figure below carries exactly one tag:**
- `[VERIFIED — source, date]` — confirmed by an external party (a real WDP email, a signed quote, an accountant confirmation, or a programmatic scheduling simulation that is itself the primary source, not an assumption about the real world)
- `[MODELED — assumption: <name it>]` — internally calculated from other modeled or verified inputs
- `[PLACEHOLDER — not yet known]` — still a guess, or genuinely unreconciled across this repo's own documents

**No figure enters this file without a tag. If you can't tag it, don't put a number here — write PLACEHOLDER and add it to `docs/VERIFICATION-TRACKER.md` instead.**

---

## 1. Operational Model

> **REBASE 2026-08-05 — the 25-minute-cadence tables are now the actual basis for ALL financial calculations venture-wide, not just the Carole-facing presentation.** Per Anthony's direct instruction: the corrected-schedule tables (exact 60/120min clinical marks, 5-min draws, synchronized chairs, 25-min pair cadence) that were built for Carole's benefit are now what every committed P&L, headcount-for-costing, and capacity figure in this file is calculated from. **New PRIMARY committed daily model: Table 1, 07:00 start, 18 clients/day, 9 pairs, g=25** (strictly dominates Table 2 — same 8-treatment/2-phlebotomist headcount, more revenue — the natural pick for "the committed daily target"; **flagged explicitly in case Anthony means something different by "these tables"** — if the intent was instead to keep 12 clients/day as the daily aim and only change the underlying schedule *shape*, Table 2 below is the correct secondary reference for that reading). **New SECONDARY/alternative reference model: Table 2, 08:00 start, 12 clients/day, 6 pairs, g=25** — same headcount as Table 1, fewer clients (later start leaves less room before the 10:30 WDP guidance limit). **The old 23-minute-cadence/12-14-client pair (used as the committed basis from 2026-07-30 to 2026-08-05) is RETIRED to historical/superseded status below — not deleted, kept for trace, same treatment given to every earlier superseded scenario in this file.** Full client/staff tables for both models: `docs/scenario-c-sync-timetables.md` §0.6a. Full scenario comparison: `docs/scenario-comparison-master-2026-08.md`.
>
> **Item 1 finding, same date — a 7th pair CANNOT be added to Table 2 at 10:25 without breaking headcount.** Anthony asked whether Table 2 (6 pairs, last pair 10:05) could take a 7th pair at 10:25 (a tighter 20-min gap from the previous pair, instead of the uniform 25-min cadence that would land at 10:30 — right at the guidance boundary). Checked programmatically, not hand-verified: inserting a pair at exactly 10:25 (5-min draws, +60/+120min marks) **collides** with the existing schedule — client 3 (started 08:25)'s Draw 3 lands at 10:25-10:30 on the same chair as the new pair's Draw 1, an exact clash, confirmed on both chairs (mirrored). Swept every whole-minute candidate from 10:10-10:29: only **10:10** and **10:20** are collision-free. Both were then checked against treatment-staff headcount via both sweep-line peak concurrency and greedy first-fit (independent methods, as required) — **both give Massage+Beauty pool=5, Nails=3, Hair=3, TOTAL=11**, up from 8. **Conclusion: a 7th pair does NOT work at 8 staff at any collision-free insertion point tested — it requires 11, not 8.** Not adopted. Table 2 remains 6 pairs/12 clients at 8 staff, as stated above.

### CURRENT COMMITTED MODEL (2026-08-05) — 25-Minute-Cadence Tables

| Parameter | Table 1 — PRIMARY committed daily model | Table 2 — SECONDARY reference model | Tag |
|---|---|---|---|
| AM client volume/day | **18 clients (9 pairs)** | **12 clients (6 pairs)** | `[VERIFIED — scenario-c-sync-timetables.md §0.6a, hard-constraint solver, zero chair/phlebotomist collisions]` |
| AM start time | 07:00, synchronized dual-chair start | 08:00, synchronized dual-chair start | `[VERIFIED — same source]` |
| Pair-to-pair cadence | 25 minutes, uniform | 25 minutes, uniform | `[VERIFIED — same source]` |
| Last Draw 1 / last departure | 10:20 / last departure well inside the shift window | 10:05 / last departure well inside the shift window | `[VERIFIED — same source]` |
| Chairs / phlebotomists | 2 chairs, 2 phlebotomists | 2 chairs, 2 phlebotomists | `[VERIFIED — same source]` |
| Treatment headcount | **8 dual-qualified (4 Massage+Beauty pool + 2 Nails + 2 Hair)** | **8 dual-qualified (4 Massage+Beauty pool + 2 Nails + 2 Hair) — identical to Table 1** | `[VERIFIED — sweep-line peak concurrency AND greedy first-fit, exact agreement, scenario-c-sync-timetables.md §0.6a]` |
| Total headcount (incl. phlebotomists) | 10 | 10 | `[VERIFIED — same source]` |
| 7th-pair extension tested (Item 1, 2026-08-05) | n/a | **Tested and REJECTED** — a 7th pair at 10:25 collides at the chair level; the only collision-free insertion points (10:10, 10:20) both raise headcount to 11 (5 pool + 3 Nails + 3 Hair), not 8. Table 2 stays at 6 pairs/12 clients. See the Item 1 finding banner above. | `[VERIFIED — collision + headcount check, both sweep-line and greedy first-fit]` |

**Table 1 strictly dominates Table 2 for "committed daily target" purposes — identical headcount, more revenue.** Full recomputed P&L for both: §5, §7, §8 below.

**Historical, superseded 2026-08-05 — relocated 2026-08-16 (D1) to keep this file current-state-only.** The 12-client/23-minute-cadence pair (and the 14-client proven-ceiling figures built on the same cadence) was the committed financial basis from 2026-07-30 to 2026-08-05 — it is no longer what any current P&L, headcount, or capacity figure in this file is built from. **Full historical detail (not deleted, just relocated so it can't be mistaken for current): [`docs/archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md`](archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md) §"Historical §1."** See the REBASE banner and CURRENT COMMITTED MODEL table immediately above for the current model.

**Bottom line: 14 clients/day was a PROVEN CEILING at the old cadence, documented for headroom/growth-capacity purposes at the time — it never replaced 12 as the then-committed daily operating target, and both figures are now superseded in turn by Table 1 (18 clients/day) at identical headcount.**
| Chair B opening policy — design ceiling vs daily rostering, CLARIFIED 2026-07-30, not a conflict | The Chair B enquiry-threshold policy (Chair A default/guaranteed, Chair B opens only on a 2nd enquiry per slot) and the 12-client committed model are **two different levels, not competing rules.** Design/target capacity (12 clients/day, both chairs synchronized) is what the venue is staffed and scheduled to handle at full booking. Daily rostering (this Chair B policy) is what actually gets staffed on any given real day, based on real confirmed bookings, which may run below the ceiling — if a day's Chair B slots have fewer than 2 confirmed enquiries, Chair B simply doesn't open that day; Chair A still runs as normal. Nothing left for Anthony to decide on this specific point. | `[VERIFIED — Anthony's direct instruction re: enquiry threshold, 2026-07-30; framing clarified 2026-07-30 later the same day]`. See `docs/VERIFICATION-TRACKER.md` item 1f and `ivy-booking-system.md`. |
| Rostering policy | Roster only the roles a given day's confirmed bookings actually require — a **standing, permanent operating rule**, not a ramp-up-period measure | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` — see `pm-staffing-roster.md`'s Booking-Driven Rostering Policy section, formalized as permanent 2026-07-30 |
| Staff downtime policy | **Two separate pools (corrected 2026-07-30):** between-client gaps fillable by advance-online-booking only (not walk-in/day-of) — sellable revenue. Lead-in/tail (before first/after last booking) — not sellable, staff engagement starts later/ends earlier instead (early release), subject to the 3-hour minimum casual engagement. | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` — see `financial-break-even-staff.md`'s Staff Downtime Protocol. Quantified: §8 below. |

---

## 2. Package Prices

| Item | Value | Tag |
|---|---|---|
| Package 1 (fixed 2×30-min services) | A$250 | `[MODELED — assumption: Anthony's locked launch price, services-pricing-locked.md renumbered 2026-07-20; not externally market-tested]` |
| Package 2 (flexible: 2×45min, or 1×45+1×30min, or 2×30min) | A$300 | `[MODELED — same basis]` |
| AM revenue calculations use which price | A$250 (Package 1) as a deliberate conservative safety price, not a blended average | `[MODELED — standing instruction, not a re-derivation]` |
| PM individual a-la-carte average | ~A$95/session | `[MODELED — assumption: pm-staffing-roster.md planning estimate, no real booking data]` |
| PM set/fixed packages | **Confirmed direction 2026-07-30** (PM Duo/Refresh/Glow menu) — pricing itself still requires Anthony's final sign-off | `[VERIFIED — Anthony's direct instruction, 2026-07-30, direction confirmed]` + `[PLACEHOLDER — final pricing not yet signed off, pm-package-structure.md]` |

---

## 3. Client Capacity

> **REBASED 2026-08-05 — see the CURRENT COMMITTED MODEL table in §1 above.** Primary figures below use Table 1 (18-client/07:00). Table 2 (12-client/08:00) figures shown alongside as the secondary reference. The old 264/month (12/day) figure is HISTORICAL/superseded, retained beneath for trace.

| Item | Value (Table 1, PRIMARY) | Value (Table 2, secondary) | Tag |
|---|---|---|---|
| AM GTT capacity ceiling | **396 visits/month (18/day × 22 trading days)** | 264 visits/month (12/day × 22 trading days — identical to the old committed figure by coincidence of arithmetic, not a like-for-like re-derivation) | `[VERIFIED capacity — scenario-c-sync-timetables.md §0.6a]` + `[MODELED — depends on referral pipeline filling all daily slots; not a revenue guarantee]` |
| AM GTT weekly ceiling (6-day week incl. Saturday) | **108 slots/week** (18/day × 6 days) | 72 slots/week (12/day × 6 days) | `[MODELED — derived]` |
| Perth metro GTT tests/week (addressable market) | ~515/week `[VERIFIED — KPMG analysis of ABS Births, Australia 2024, see full citation below]` | ~515/week (same) | `[VERIFIED — see below]` |
| Share of addressable market at full AM capacity | **~21% (108 slots/week ÷ ~515/week)** — up from ~14% at the old 12-client committed figure, since Table 1 serves 50% more clients/day at the same headcount | ~14% (unchanged from the old committed figure's arithmetic, since Table 2 also serves 12/day) | `[MODELED — derived from the market-size row above]` |
| PM individual services capacity (steady state) | ~16 sessions/day (~350/month) — unaffected by this rebase, AM-only change | same | `[MODELED — assumption: ~50% utilisation of theoretical 4-line capacity, pm-staffing-roster.md; no real demand data exists yet]` |

**Historical, superseded 2026-08-05:**

| Item | Value | Tag |
|---|---|---|
| AM GTT capacity ceiling (old, 23-min-cadence/12-client model) | 264 visits/month (12/day × 22 trading days) — was 220/month at the superseded 10-client model | `[VERIFIED capacity — solver-checked 2026-07-30]` + `[MODELED — depends on referral pipeline filling all 12 daily slots; not a revenue guarantee]` |
| AM GTT weekly ceiling (old model) | 72 slots/week (was 60/week) | `[MODELED — derived: 12/day × 6 days]` |
| Perth metro GTT tests/week (addressable market) — **CORRECTED 2026-07-31** | ~515/week (was ~277/week — the old figure was an unsourced estimate, not real ABS data) | `[VERIFIED — KPMG analysis of ABS Births, Australia 2024 (media release 17 July 2025); real 2024 Greater Perth GCCSA figure ~26,790 births/year ÷ 52 weeks = ~515/week, universal GTT screening assumed. ABS figures noted as preliminary/subject to revision.]` |
| Share of addressable market at full AM capacity (old model) | ~14% (6-day operating week, 72 slots/week ÷ ~515/week) (was ~26%, itself corrected from ~22%) | `[MODELED — derived]` |

---

## 4. Headcount

| Role | Qty | Tag |
|---|---|---|
| Venue Manager (Managing Director) | 1 — new hire, not yet in place | `[PLACEHOLDER — critical-path hire, recruitment gated on securing a physical venue location, not yet begun]` |
| Phlebotomist (AM only, Chair A / Chair B) | 2 | `[MODELED — financial-break-even-staff.md award-rate structure]`. **CRITICAL OPEN DEPENDENCY (flagged 2026-07-30):** this entire row, and the ~A$48,255/month AM Direct Labor figure it feeds into (§7 below), assumes GTT Center Perth employs its own phlebotomist(s) directly — the current modelled baseline. Carole Rivers' 2026-07-30 email raises a real possibility that under WDP's rental-clinic model, WDP supplies/employs the phlebotomist instead (their email: phlebotomist "safety, wellbeing and employment responsibilities... would remain with Western Diagnostic Pathology"), which would replace this wage line with a to-be-negotiated rental fee. **Anthony's explicit answer: NOT DECIDED — needs to ask Carole directly.** Do not treat the current in-house figure as settled once this is answered — it may change materially. `[PLACEHOLDER — critical, high-priority, see docs/VERIFICATION-TRACKER.md]` |
| **AM treatment staff — REBASED 2026-08-05: same 8-staff design ceiling now confirmed to hold identically at the new committed 18-client volume (Table 1) AND the 12-client secondary reference (Table 2)** — `[VERIFIED — sweep-line + greedy first-fit, exact agreement, scenario-c-sync-timetables.md §0.6a]`. The 25-min uniform cadence never triggers the headcount spike the old bursty 14-client search needed 9 staff for — a genuinely better finding, same headcount now serving up to 18 clients/day, not just 12. | | |
| AM treatment staff — HISTORICAL, superseded 2026-08-05, design ceiling at the old committed 12-client volume | **8 dual-qualified staff, required by peak overlap at this volume — not "unpooled," there is no unpooled model.** All treatment staff are hired dual/multi-qualified (Massage+Beauty confirmed pairing); the headcount is 8 because peak concurrent client overlap at 12 clients/day requires 4 people simultaneously on the Massage+Beauty pool (dual-qualification provides no further reduction at this specific volume — the pool's own peak concurrency is 4, same as the sum of the individual Massage and Beauty peaks, so pooling doesn't help here) plus 2 on Nails plus 2 on Hair. One person can only be in one place at a time — that is why 8 is required, not because anyone was hired single-skilled. | `[VERIFIED — solver-checked 2026-07-30 against the 12-client model; re-verified via interval-overlap simulation testing the Massage+Beauty dual-qualified pool directly, 2026-07-31]`. Testing 7 (Massage+Beauty pool capped at 3) against the 12-client schedule fails — 2 clients unassignable, confirming the pool's true peak is 4, not 3, at this volume. |
| AM treatment staff — daily rostering on lower-volume actual days (below the 12-client ceiling) | **7 (Massage+Beauty dual-qualified pool sized to 3, not 4) remains a legitimate choice on days where real confirmed bookings are low enough to fit it** — this is the same dual-qualified staff working a smaller roster on a quieter day, not a different hiring model. | `[VERIFIED — solver-confirmed the Massage+Beauty pool clears at 3 below 12 clients/day, still valid at lower volume]`. **This is a genuine daily-rostering saving on quieter days, same principle as Chair-B-on-demand and early-release** — roster to what the day's actual bookings need, not to the ceiling by default. Design ceiling (8, required by peak overlap at 12/day) and daily rostering (7, valid below it) are two different levels, not a contradiction. Recruiting implication: still prefer a Massage+Beauty (Cert IV) dual-qualified hire for one treatment position — see `docs/pm-casual-roles-job-posting.md`. |
| AM treatment staff — at the 14-client PROVEN CEILING (growth capacity, NOT the daily target — see §1 above for full method) | **9 dual-qualified staff (3 on the Massage+Beauty pool + 3 Nails + 3 Hair)**, proven via two independent methods (sweep-line peak concurrency AND greedy first-fit assignment, exact agreement). The Massage+Beauty pool's true peak concurrency at 14 clients/day is 3 (not 4 as at the 12-client daily target) — a genuine reduction, because the massage-demand cluster and beauty-demand cluster in the bursty schedule peak at different clock times, letting the shared pool cover both with fewer people than the sum of their individual peaks. | `[VERIFIED — two independent methods, 2026-07-31]`. Nails and Hair have no confirmed dual-qualification pairing, so each is costed as its own 3-person line: `[VERIFICATION NEEDED — Nails+Hair pairing not yet confirmed as hireable]` for any further reduction below 9. |
| Receptionist / Manager (split shift) | 1 | `[MODELED]` |
| PM dedicated casual roster (1 each: massage, hair, nail, beauty) | 4 | `[MODELED — pm-staffing-roster.md, hours-based costing, not a flat FTE headcount]` |
| Casual Relief Pool | Budget line, not a fixed headcount | `[MODELED — A$15,000/yr budgeted]` |
| **Total heads (AM 8-staff, no-pooling + PM + relief pool structure)** | **~16-17** | `[MODELED — sum of above; unchanged in absolute headcount from the 10-client model, since 8-staff was always the traceable payroll baseline — what changed 2026-07-30 is that the pooling REDUCTIONS below it are no longer valid at the committed 12-client volume]` |
| Possible combined AM/PM rotating pool (2026-07-28 proposal) | Potentially fewer than 11 total treatment/PM heads across both shifts | `[PLACEHOLDER — dual-role-staffing-model-2026-07-28.md v3.0 explicitly states this is "not booked as a confirmed saving," pending real roster data]` |
| Hiring model | **Settled 2026-07-30:** cross-qualified hires where trades allow (Massage+Beauty dual-Cert-IV pairing, per `profit-loss-tables.md`'s Treatment Headcount section). All service staff hired as casuals initially; reviewed for conversion to part-time once regular, proven hours exist per role (matches `pm-staffing-roster.md`'s existing "casual for first 3-6 months, review conversion at Month 3-6" policy). | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` |
| ~~Possible Nails+Hair cross-qualification (solver-checked 2026-07-29)~~ SUPERSEDED 2026-07-30 | ~~Would bring combined treatment headcount to 6~~ — **this finding was correct only for the 10-client model, which is now superseded.** At the committed 12-client volume, neither the Massage+Beauty (7-staff) nor the Nails+Hair (6-staff) pooling reduction holds — both fail (see the row above). | `[SUPERSEDED — the 2026-07-29 solver result was accurate for its own (now-historical) 10-client scenario; do not action a 6-staff or 7-staff hiring plan]` |

---

## 5. Monthly Net P&L

> **REBASED 2026-08-05 — the 25-min-cadence tables are now the actual basis, per Anthony's direct instruction (see §1 REBASE banner).** New PRIMARY committed steady-state figure: **+A$63,028.75/month** (Table 1, 18-client/07:00). New SECONDARY reference: **+A$27,084.69/month** (Table 2, 12-client/08:00 — numerically unchanged from the old committed baseline, since client volume and headcount are identical; see the flagged open item below). The old 12-client/23-min-cadence Month 1-5+ ramp table is HISTORICAL, retained beneath for trace — Month 1-4 ramp has NOT yet been independently rebuilt against the new, higher Table 1 ceiling, flagged as an open follow-up rather than fabricated (see `docs/VERIFICATION-TRACKER.md`).
>
> **SUPERANNUATION CORRECTION, 2026-08-14 — narrow headline-figure fix only.** The two PRIMARY/SECONDARY figures immediately above (A$63,028.75 / A$27,084.69) predate the 2026-08-09 superannuation fix (`docs/VERIFICATION-TRACKER.md` item 46) and are now stale. The canonical model's current, superannuation-corrected steady-state Net Operating Result is **A$56,581.70/month (Table 1)** and **A$21,056.64/month (Table 2)** — `data/models/master_financial_model.yml#outputs.steady_state_summary`, RECALCULATED 2026-08-09. **Only the two headline Net P&L numbers below (§5's PRIMARY/SECONDARY table rows) have been corrected to match.** The surrounding Total Costs, Quarterly, Half-Yearly, and Yearly rows in both tables below, the Fourth Delta table (§7), and every dated changelog entry elsewhere in this file are, deliberately, **NOT** recomputed here — they remain on the pre-superannuation historical/inherited-revenue basis, flagged as a real, open follow-up rather than silently left inconsistent or guessed at. Do not quote the Total Costs/Quarterly/Half-Yearly/Yearly rows below as superannuation-corrected; only the two Net P&L headline figures are.

### PRIMARY — Table 1 (18-client/07:00/g=25), steady state

> **Independently re-verified from scratch, 2026-08-07** — full 9-step first-principles walkthrough (18 clients x A$250 x 22/4.33 days, headcount re-confirmation, Saturday labor scaling, Workers Comp, final arithmetic check) in `docs/profit-loss-tables.md`'s "Monthly — Table 1 (PRIMARY)" section. **Result: A$63,028.75/month confirmed, exact match, no rounding drift** — this is Net P&L (profit), not a revenue figure; Table 1's revenue is the separate Total Revenue line below. One pre-existing, already-disclosed gap surfaced during re-verification (not new, not this rebase's fault): a first-principles revenue sum lands ~A$2,576 below the delta-built A$157,792.16 figure below — the same fixed-size weekly-to-monthly scaling artifact already flagged in `profit-loss-tables.md`'s Appendix since 2026-07-30, present identically at the 10-client and 12-client stages too.
>
> **REVENUE METHODOLOGY UPDATE, 2026-08-09 — per Anthony's direct decision, following a dedicated investigation into the gap above** (`docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md`): the days-based first-principles revenue formula is now the **canonical** methodology for future revenue modelling — see `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` for the full formula, inputs, and worked examples (Table 1 = A$155,215.80/month, Table 2 = A$115,720.80/month). The Total Revenue figures in the tables immediately below (A$157,792.16 / A$118,297.16) are the venture's original, historical/inherited figures — preserved here for trace and still the basis every other figure in this section (Net P&L, Total Costs) is built from, but they are **not** the output of the new canonical methodology. `docs/VERIFICATION-TRACKER.md` item 36 has the full status.

| Line | Amount | Tag |
|---|---|---|
| Total Revenue (Monthly) — **HISTORICAL/INHERITED figure, not the canonical methodology as of 2026-08-09 — see banner above** | **A$157,792.16** (was A$118,297.16 at the old 12-client/23-min model — delta +A$39,495.00, all from AM: +A$33,000.00 weekday (6 extra clients × A$250 × 22 days) + A$6,495.00 Saturday (6 extra clients × A$250 × 4.33 Saturdays), PM/ancillary unchanged) | `[MODELED — delta-reconciliation build from the validated 12-client baseline in profit-loss-tables.md, same methodology as every prior model-change round in this file]` |
| Total Direct Labor + Opening Costs | **A$79,433.05** (was A$75,941.47 — delta +A$3,491.58, entirely Saturday AM labor: hours-based costing scales proportionally with the longer 18-client AM day, A$1,612.74/day → A$2,419.11/day, a 1.5× scale-up matching the 12→18 client ratio; weekday AM labor UNCHANGED at A$48,254.67/month, FTE-based, same 8+2 headcount) | `[MODELED — proportional-scaling estimate for Saturday, same caveat as every prior Saturday-labor scaling in this file: not an independently rebuilt Saturday-specific solver schedule]` |
| Workers Comp (1.7%) | **A$1,350.36** (was A$1,291.00 — delta +A$59.36, 1.7% of the Saturday labor delta above) | `[MODELED — same 1.7% convention]` |
| Non-Wage Overhead | A$13,980.00 (unchanged — rent/utilities not client-volume-driven) | `[MODELED — unchanged]` |
| **Total Costs** | **A$94,763.41** | |
| **Net P&L — NEW PRIMARY COMMITTED STEADY-STATE FIGURE** | ~~+A$63,028.75/month~~ **+A$56,581.70/month (superannuation-corrected, 2026-08-14 — see banner above; A$63,028.75 was the pre-superannuation figure, retained struck-through for trace, not deleted)** | `[MODELED — full recompute, delta-from-baseline method; headline figure only, RECALCULATED 2026-08-09 per data/models/master_financial_model.yml, see banner above for what has and hasn't been propagated]` |
| Quarterly | +A$189,086.25 | `[MODELED — Monthly × 3]` |
| Half-Yearly | +A$378,172.51 | `[MODELED — Monthly × 6]` |
| Yearly | +A$756,345.01 | `[MODELED — Monthly × 12]` |

### SECONDARY — Table 2 (12-client/08:00/g=25), steady state

| Line | Amount | Tag |
|---|---|---|
| Total Revenue (Monthly) — **HISTORICAL/INHERITED figure, not the canonical methodology as of 2026-08-09 — see banner above §5** | A$118,297.16 — identical to the old committed model's revenue, since Table 2 also serves 12 clients/day | `[MODELED — same arithmetic as the old 12-client baseline]` |
| Total Direct Labor + Opening Costs | A$75,941.47 — identical, same headcount, same client volume | `[MODELED — same]` |
| **Net P&L — SECONDARY REFERENCE FIGURE** | ~~+A$27,084.69/month~~ **+A$21,056.64/month (superannuation-corrected, 2026-08-14 — see banner above; A$27,084.69 was the pre-superannuation figure, retained struck-through for trace, not deleted)** | `[MODELED, RECALCULATED 2026-08-09 per data/models/master_financial_model.yml]` |

**Open item, flagged not assumed:** the Weekday P&L's "Opening-time increment" line (A$44.50/day, `profit-loss-tables.md` §1) is sourced specifically to the incremental cost of a **07:00** start vs a later one. Table 2 starts at 08:00, not 07:00 — this increment may not apply, which would make Table 2's true Net P&L slightly HIGHER than A$27,084.69/month. Not quantified or baked into the headline above, since the source document does not state the increment's exact mechanism (staff arrival penalty vs something else) precisely enough to re-derive with confidence — logged as an open item in `docs/VERIFICATION-TRACKER.md` rather than guessed at.

**AM Direct Labor, both models — UNCHANGED at A$48,254.67/month (weekday, FTE-based):** 2 phlebotomists (A$86,136/yr) + 8 treatment staff (A$492,920/yr) = A$579,056/yr ÷ 12. Headcount is identical (8 dual-qualified + 2 phlebotomists) at both 18-client Table 1 and 12-client Table 2 — see §4. This is the central finding of the rebase: **Table 1 serves 50% more daily clients than the old committed model at literally zero extra weekday labor cost**, because these are fixed-salary FTE roles and the extended day still fits the shift budget.

**Also not included in any figure above:** the Between-Client Downtime-Fill Revenue and Early-Release Cost Saving — both recomputed fresh against each table's own actual gap pattern (not carried over from the old 12-client/23-min figures), see §8 below.

---

### HISTORICAL, superseded 2026-08-05 — old 12-client/23-min-cadence committed model

**Relocated 2026-08-16 (D1) to keep this file current-state-only.** The old committed model's Month 1-5+ ramp table (12-client/23-min-cadence, pre-superannuation) is no longer current — full detail: [`docs/archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md`](archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md) §"Historical §5."

**None of the above (nor the current figures elsewhere in this file) is based on real trading data — there is no venue open yet.**

---

## 6. Startup Capital Range — UNRECONCILED, Flagged Rather Than Resolved

**This is the clearest example of the "financial model moved 5+ times" finding.** Three different ranges exist across this repo's own documents, none confirmed as authoritative:

| Source | Range | Tag |
|---|---|---|
| `investor-memorandum.md` (original itemised build: fit-out, equipment, IT, working capital, legal) — HISTORICAL COMPARISON figure, one of 3+ unreconciled ranges, not settled | A$363,000 mid / A$292,000-493,000 range | `[PLACEHOLDER — itemised, but not re-verified against the current committed model (18-client/day Table 1, 2-package structure)]` |
| `HANDOFF.md` (2026-07-17) — HISTORICAL COMPARISON figure, one of 3+ unreconciled ranges, not settled | "~A$144,500-242,500 realistic range, down from an inflated A$363,000 original figure" | `[PLACEHOLDER — no itemised build shown in that document — cannot be traced]` |
| `business-plan.md` §9 (attributed to `cash-flow.md`) | Low A$209,000 / Mid A$305,000 / High A$431,000 | `[PLACEHOLDER — this breakdown does not currently exist anywhere in cash-flow.md's own content as of its 2026-07-20 full rebuild; the citation could not be verified this session]` |
| `docs/floor-plan-concept.md`'s Fit-Out Cost Estimate (2026-07-31 recompute — open-plan/curtain layout, 4 hair chairs/4 nail stations, spray tan moved to Phase 2) | A$228,142-457,559 range, mid A$341,851; net after landlord contribution ~A$311,851 | `[MODELED — itemised bottom-up build, own methodology, not reconciled against the 3 ranges above]`. A 4th, also-unreconciled data point — **fixture-count expansion pushed this figure UP versus the prior 2026-07-28 version (was A$222,300-449,700), despite a real, confirmed A$10,736-17,256 saving from converting Massage/Beauty rooms to curtain partitions and Lounge/Hairdressing/Nails to open-plan — the saving was real but smaller than the added cost of 4 hair chairs and 4 nail stations.** |

**No single figure is presented here as canonical.** Picking one of the three arbitrarily would repeat exactly the false-precision problem this file exists to prevent. **What's actually needed:** a fresh, itemised fit-out/equipment/legal/working-capital build against the current model (10-client Scenario C, 2-package structure, current staffing) — tracked as an open item in `docs/VERIFICATION-TRACKER.md`. Anthony and an accountant/quantity surveyor should confirm before this figure is used in any real funding conversation.

### Section 7 Build — RECONCILED 2026-07-31, Supersedes the Same-Day Rebuild Above

> **This reconciled version supersedes the original 2026-07-31 Section 7 rebuild (A$268,142–583,559) — that figure is retired, not left standing alongside this one.** Anthony reviewed the original rebuild directly and applied two corrections, both disclosed rather than smoothed over: (1) the landlord fit-out contribution is removed from the headline total entirely — Anthony is skeptical a landlord will actually contribute and doesn't want it baked into the best-case figure; (2) the insurance component is relabelled `[PLACEHOLDER]`, not a modelled certainty — it was never an actual quote. Construction cost also recomputed using this document's own established rate (A$800-1,250/sqm) at the corrected 239sqm footprint, rather than reusing the earlier itemised bottom-up figure — the two land close but not identical, a small disclosed gap, not forced into exact agreement.

**A 6th data point overall, still not canonical** (this file continues to present no single figure as authoritative — see the 5 historical/prior entries above), but this is the version assembled specifically to patch the client-facing document prepared for Anthony's partner Imara, and the one to use going forward for that purpose.

**7.1 Equipment, Furniture, Fixtures & Expendables (unchanged from the original rebuild)**

| Component | Low | High | Source |
|---|---|---|---|
| Equipment (pathology, massage, nails ×4, hair ×4, beauty, lounge, tech, safety, consumables — day-one only; **was A$42,690-96,530, +A$500-900 for the vasovagal reclining chair/couch added 2026-08-07**) | A$43,190 | A$97,430 | `equipment-costs.md` Summary Budget, 2026-08-07 recompute |
| Furniture and fittings (lounge chairs, reception counter, styling chairs) | A$15,000 | A$35,000 | `floor-plan-concept.md` Fit-Out Cost Estimate |
| Signage (shopfront + internal wayfinding) | A$3,000 | A$8,000 | `floor-plan-concept.md` Fit-Out Cost Estimate |
| **7.1 TOTAL (was A$60,690-139,530)** | **A$61,190** | **A$140,430** | `[MODELED — sum of the two source documents above, both independently tagged in their own files]` |

**7.2 Fit-out/Construction (construction cost only, RECOMPUTED at this document's established A$800-1,250/sqm rate — no landlord contribution deducted anywhere in the headline)**

| Component | Low | High | Source |
|---|---|---|---|
| Construction (raw-shell scenario, 239sqm day-one, A$800-1,250/sqm) | A$191,200 | A$298,750 | `[MODELED — 239sqm × A$800-1,250/sqm, this document's own established rate]`. Compare to `floor-plan-concept.md`'s independent itemised bottom-up build (A$162,452-306,029, same 239sqm, wall-to-curtain savings itemised separately) — the two land close but not identical; both retained, not forced to agree. |
| Landlord fit-out contribution | **Removed from the headline entirely, per Anthony's instruction** | — | Previously applied as a deduction (A$30,000-60,000); Anthony is skeptical a landlord will actually contribute and does not want it assumed in the best-case figure. Still a real possible upside if negotiated — see `floor-plan-concept.md`'s Landlord Contribution note — just not counted here. |
| **7.2 TOTAL** | **A$191,200** | **A$298,750** | |

**Not attempted, flagged rather than fabricated:** a "former health/beauty tenancy" discount scenario (lower construction cost for taking over an existing compatible fit-out) was explicitly requested against and declined — it would require inventing a fresh discount percentage with no basis in this repo. **Needs a fresh assessment once a specific venue candidate exists**, not a reused/invented percentage.

**7.3 Working Capital & Pre-Launch Costs (insurance component relabelled PLACEHOLDER)**

| Component | Low | High | Tag |
|---|---|---|---|
| Working capital reserve (funds Months 1-3 operating losses) | A$85,000 | A$110,000 | `[MODELED — from Anthony's partner-brief working session, basis stated: Section 6's ~A$84,468 combined Month 1-3 loss, plus a buffer]` |
| Legal/entity setup, lease bond (~2 months' rent) | ~A$19,600 | ~A$27,600 | `[MODELED — from Anthony's partner-brief working session]` |
| First-year insurance (embedded in the range above, ~A$400/month basis) | ~A$400 | ~A$400 | `[PLACEHOLDER — corrected 2026-07-31: never an actual insurance quote, a round planning estimate — same figure flagged in `profit-loss-tables.md`'s Non-Wage Overhead breakdown]` |
| **7.3 TOTAL** | **A$105,000** | **A$138,000** | Sourced from Anthony directly, 2026-07-31 — not independently re-derived in this repo; insurance sub-component now correctly tagged `[PLACEHOLDER]`, not implied as confirmed |

**7.4 Full Picture — Total Startup Capital Required (RECONCILED, landlord contribution removed from headline)**

- **Best case:** 7.1 low (A$61,190) + 7.2 low (A$191,200) + 7.3 low (A$105,000) = **A$357,390** (was A$356,890, +A$500 from the 2026-08-07 equipment addition)
- **Higher case:** 7.1 high (A$140,430) + 7.2 high (A$298,750) + 7.3 high (A$138,000) = **A$577,180** (was A$576,280, +A$900)

**Adopted total, per Anthony's own reconciliation: A$292,335 – A$594,900.** `[MODELED — Anthony's reconciled figure, adopted as instructed]`. **Disclosed, not hidden: this agent's own component-by-component sum above (A$357,390–577,180) does not land exactly on the adopted A$292,335-594,900 range** — the gap is a few percent on both ends, most plausibly from reconciliation choices in how Anthony combined the underlying components that aren't fully visible in this repo (e.g. a different low-end scenario weighting, or a partial/negotiated landlord-contribution assumption reinstated at the very low end despite the "removed from headline" instruction). **The adopted A$292,335-594,900 figure is what should be quoted and patched into the client-facing document — it is Anthony's own reconciliation, not superseded by this agent's component sum.** Both this agent's component build and the adopted total are shown side by side rather than silently reconciled to hide the small gap.

**Up from A$276,635-554,900 (the original reference range this whole Section 7 exercise started from) — both corrections (landlord contribution removed, construction recomputed at the higher established rate) push the range up. Disclosed plainly, not smoothed over.**

**UPDATE 2026-08-10 — a newer, more current planning figure exists alongside all ranges above, not replacing any of them.** Following a bottom-up reconstruction (`docs/architecture/startup-cost-reconstruction.md`), a cost-optimisation pass (`docs/architecture/STARTUP-COST-OPTIMISATION.md`), and a founder risk-acceptance review (`docs/architecture/MVP-OPENING-DECISION-REVIEW.md`), Anthony approved a Revised Recommended Opening Strategy of **A$251,198** (Pre-Opening Capital scope, same scope as this section) "in principle" as the current planning assumption — explicitly a planning figure, not a locked final cost, pending venue confirmation and final supplier/quote validation (`docs/VERIFICATION-TRACKER.md` item 49, OPEN). See `data/canonical/startup_costs.yml#adopted_planning_scenarios` for the full itemised record and `data/models/master_financial_model.yml#funding_requirement_investigation.updated_planning_case_2026_08_10` for the updated combined funding-requirement case. None of the historical ranges above are altered or superseded by this update.

---

## 7. AM/GTT Segment Profitability — Delta Table (Old Model vs Current Model)

### Fourth Delta — REBASE 2026-08-05: Old 23-Min-Cadence/12-Client (now historical) vs New 25-Min-Cadence/18-Client Table 1 (new PRIMARY committed model)

**This is the current, active delta — read this one first.** All prior deltas below (10→12, 12→14) are retained for trace but describe superseded models.

| Input | Old value (12-client, 23-min, now historical) | New value (18-client, Table 1, PRIMARY committed) | Changed? | Tag |
|---|---|---|---|---|
| AM client volume/day | 12 | 18 | **Yes** | Old: `[VERIFIED — 2026-07-30]`. New: `[VERIFIED — scenario-c-sync-timetables.md §0.6a, hard-constraint solver, zero collisions]` |
| AM treatment headcount | 8 dual-qualified (pool=4, Nails=2, Hair=2) | **8 dual-qualified — identical** | **No** | `[VERIFIED — sweep-line + greedy first-fit, exact agreement]` |
| AM direct labor cost (weekday, FTE) | A$48,254.67/month | A$48,254.67/month | **No — unchanged**, same headcount, same fixed-salary roles, extended day still fits the 07:00-13:00 shift budget | `[MODELED — traceable]` |
| AM revenue (weekday, 22 days) | A$66,000/month | **A$99,000/month** | **Yes, +A$33,000/month** | `[MODELED — 18 × A$250 × 22]` |
| **AM segment standalone contribution (weekday)** | **+A$17,745/month** | **+A$50,745.33/month** | **+A$33,000.33/month** | Revenue delta, labor unchanged |
| **Whole-venture Monthly Net P&L** | **+A$27,084.69/month** | **+A$63,028.75/month** | **+A$35,944.06/month** — includes Saturday AM labor scaling (+A$3,491.58/month) and the resulting Workers Comp uptick (+A$59.36/month), not just the weekday AM segment swing | Full build in §5 above |

**Bottom line: the new Table 1 primary model is a strict improvement over the old committed baseline at zero extra weekday labor cost — same 8 treatment staff + 2 phlebotomists, 50% more daily clients, +A$35,944.06/month whole-venture.** This dominates every prior "12 vs 14" tradeoff analysis below, which is now retained for historical trace only — the 14-client proven-ceiling figure (+A$36,726.23/month, needing 9 staff) is itself now beaten by Table 1's +A$63,028.75/month at 8 staff.

**Framing flag, per the brief that requested this rebase:** the above adopts Table 1 (18-client/07:00) as "the committed daily target" because it strictly dominates Table 2 (same headcount, more revenue) — this is the most natural reading of "these tables become the actual basis for financial calculations." **If Anthony instead means the venue should keep aiming for a 12-client/day operating rhythm and only wants the underlying schedule shape corrected (not the target volume raised to 18), Table 2's secondary figures (§5 above, +A$27,084.69/month, numerically unchanged from the old baseline) are the ones to use instead.** Flagged explicitly rather than assumed either way.

**Anthony's belief, per the task brief:** a revised model now shows the AM segment profitable on its own, versus the previously-modeled loss (revenue A$44,000/mo vs direct labor A$48,255/mo, per `pm-staffing-roster.md`).

**Finding after tracing every input:** the swing from loss to profit is real and traceable, but it is **not a new model** — it is the existing 10-client Scenario C capacity change (verified 2026-07-17, already resolved venture-wide as CONFLICT-08 on 2026-07-20) applied to a segment-level table (`pm-staffing-roster.md`'s "Profit Breakdown — AM vs PM Contribution") that had never been updated to match. No document in this repo describes any further AM-specific model change beyond this. The one candidate that could have introduced a further change — `dual-role-staffing-model-2026-07-28.md` v3.0 (combined AM/PM rotating staff pool) — explicitly states its potential headcount saving is **"not booked as a confirmed saving,"** pending real roster data. **I found no sourced basis for any AM-segment improvement beyond the Scenario C change below — if Anthony means something more recent than that, it isn't in this repo's documents and should not be presented as a number until it is.**

| Input | Old value | New value | Changed? | Tag |
|---|---|---|---|---|
| AM client volume/day | 8 (Scenario B) | 10 (Scenario C) | **Yes — this is the only changed input** | Old: `[PLACEHOLDER — early Scenario B planning assumption, never independently verified as a capacity claim]`. New: `[VERIFIED — scenario-c-sync-timetables.md, 2026-07-17, programmatic zero-double-booking simulation]` |
| Package price used | A$250 | A$250 | No | `[MODELED — unchanged, conservative safety price both times]` |
| AM treatment headcount (2 phlebotomists + 8 treatment staff) | 10 people | 10 people | No — same peak-concurrency requirement at both volumes per `profit-loss-tables.md`'s Treatment Headcount analysis | `[MODELED — financial-break-even-staff.md award rates, traceable]` |
| AM direct labor cost | A$48,255/month | A$48,255/month | No | `[MODELED — same, traceable calculation: 2 phlebotomists ($7,178/mo) + 8 treatment staff ($41,077/mo)]` |
| AM revenue (client volume × price × 22 days) | A$44,000/month | A$55,000/month | **Yes — direct consequence of the volume change above** | `[MODELED — arithmetic on the VERIFIED capacity ceiling above; actually earning A$55,000/month still depends on filling all 10 daily slots, which is a referral-pipeline/demand question, not yet proven]` |
| **AM segment standalone contribution (revenue minus direct labor only), historical (8-client vs 10-client delta)** | **-A$4,255/month** | **+A$6,745/month** | **Swing: +A$11,000/month, exactly matching the revenue delta — confirms no other input changed** | See rows above |

**Bottom line:** the AM segment can be presented as profitable on a standalone direct-labor basis (+A$6,745/month) using figures already fully traceable in this repo — but this is the 12-day-old Scenario C correction reaching a table that was overlooked, not a new finding. `pm-staffing-roster.md` has been corrected to match (see that document's 2026-07-29 changelog entry). This does not change the venture-level headline figure, which already incorporated the Scenario C AM revenue correctly since 2026-07-20 — only this one segment-level table was stale.

> **PROMINENT FLAG, added 2026-07-30 — the entire AM Direct Labor figure (A$48,255/month) in this table is contingent on an unresolved employment-model question, not yet settled.** Carole Rivers' (WDP) 2026-07-30 email raises the real possibility that WDP, not GTT Center Perth, employs the phlebotomist under WDP's venue-rental clinic model (their email: phlebotomist employment responsibilities "would remain with Western Diagnostic Pathology"). **Anthony's explicit instruction: this is NOT DECIDED — ask Carole to clarify before assuming either way.** The A$48,255/month figure above assumes the current in-house employment model and has NOT been changed — this flag exists so nobody mistakes it for settled once the employment-model question is actually answered. If WDP ends up supplying/employing the phlebotomist, this whole AM segment delta table would need to be rebuilt against a rental-fee cost structure instead of a wage cost structure — a materially different, not-yet-modeled scenario. See `docs/VERIFICATION-TRACKER.md` (high-priority item) and `cutoff-time-CORRECTION.md`.

### Second and Third Deltas — HISTORICAL, superseded 2026-08-05

**Relocated 2026-08-16 (D1) to keep this file current-state-only.** The Second Delta (10-client vs 12-client, 2026-07-30) and Third Delta (12-client daily target vs 14-client proven ceiling, 2026-07-31, including the superseded naive-headcount version) are both fully superseded by the Fourth Delta above. Full historical detail: [`docs/archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md`](archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md) §"Historical §7."

---

## 8. Downtime-Fill Revenue & Early-Release Saving — Two Separate Tagged Pools

> **REBASED 2026-08-05 — recomputed fresh against each new table's own actual gap pattern, per Anthony's instruction not to carry over the old 12-client figures.** Formula unchanged: Downtime-Fill = (between-gap min/day ÷ 60) × 1.3 sessions/hr × 0.5 utilisation × A$95/session × 22 trading days/month. Early-Release = per-station saveable lead+tail minutes × that station's own award rate, summed, × 22 trading days/month.

| Item | Table 1 (18-client/07:00, PRIMARY) | Table 2 (12-client/08:00, secondary) | Tag |
|---|---|---|---|
| Between-booking gaps (pool a), 8 stations | 160 min/day | 100 min/day | `[VERIFIED — walked from each table's own per-staff booking assignment, scenario-c-sync-timetables.md §0.6a]` |
| **(a) Between-Client Downtime-Fill Revenue** | **A$3,622.67/month** | **A$2,264.17/month** | `[MODELED — same formula/assumptions as every prior downtime-fill figure in this file: 50% utilisation, 1.3 sessions/hr, A$95/session]` |
| **(b) Early-Release Cost Saving** | **A$14,167.19/month** | **A$18,495.99/month — genuinely LARGER than Table 1's despite fewer clients**, because Table 2's later 08:00 start and shorter 6-pair schedule leaves more unsold lead/tail time per station relative to its shorter booked span | `[MODELED — per-station saveable lead+tail × award rate, summed, ×22 days; wage rates financial-break-even-staff.md]` |

**Neither (a) nor (b) is included in §5's headline Net P&L figures above — both are separate, tagged lines, and are not blended with each other either.** A genuine, disclosed finding: Table 2's early-release saving exceeds Table 1's, even though Table 1 serves more clients and generates more revenue — a real consequence of the different schedule shapes, not an error.

---

### HISTORICAL, superseded 2026-08-05 — old 12-client/23-min-cadence downtime-fill figures

**Relocated 2026-08-16 (D1) to keep this file current-state-only.** Full historical detail (12-client and 10-client downtime-fill/early-release figures, both superseded by the Table 1/Table 2 recompute in §8 above): [`docs/archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md`](archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md) §"Historical §8." **The permanent policy itself (between-client gaps fillable, lead-in/tail not sellable, subject to the 3-hour minimum casual engagement) is unchanged and still current — only the old dollar figures were relocated.**

---

## 9. Orphaned Local Clone — Do Not Edit

**A second, never-pushed, now-diverged local clone of this repo exists at `C:\Users\azed9\Documents\GitHub\gtt-center-perth`** (created by an earlier "Claude in Cowork" session on Anthony's machine). Confirmed 2026-07-30:
- Its `git log` shows it stopped at commit `d7fe9bc` — it is missing every commit since (including this file's creation and all subsequent updates).
- It has its own uncommitted, never-pushed local files: a competing `docs/CURRENT-STATE.md` (superseded, do not use), an uncommitted `docs/partner-profitability-brief.md`, and its own `CLAUDE.md` still carrying the "Imara's personal savings" wording error fixed in this repo on 2026-07-29.
- **This scratchpad clone (wherever this session is running from) and the GitHub remote (`clawanthonyzed/gtt-center-perth`) are the only canonical sources.** The orphaned clone should not be edited by any future session.
- **Do not delete it without checking with Anthony first** — it may contain content (the partner-profitability-brief.md draft, a standalone HTML profitability calculator mentioned in a prior session) he still wants to review before it's discarded. If it's ever touched again, re-clone fresh from GitHub rather than trying to reconcile its diverged history.

---

## 10. How to Use This File

- Every document in `docs/` that states a package price, client capacity, headcount, monthly P&L figure, or startup capital range should point here, not restate the figure as its own independent source.
- Run `python tools/check_consistency.py` before quoting any figure externally (investor conversation, lease negotiation, staff training) — it greps every `docs/*.md` file for values that contradict this file.
- When a figure changes here, it does not need to be manually propagated to every other document — those documents should already be pointing here. If you find one that restates a figure independently, add a pointer instead of a second copy.
- See `docs/VERIFICATION-TRACKER.md` for every unconfirmed fact and who can confirm it.

---

## Changelog

**2026-08-16 (D1 — historical clutter removed, relocated to a clearly-labelled archive)** — Per direct founder instruction, this file should contain current-state information only. Found (not previously flagged as its own issue) that this file had accumulated multiple full superseded/historical tables inline (§1's old 12-14-client/23-min model, §5's old Month 1-5+ ramp table, §7's Second and Third Delta tables, §8's old downtime-fill figures) plus every changelog entry from this file's 2026-07-29 creation through the 2026-08-05 rebase (~50 lines of dense history) — none of it deleted, all of it relocated to [`docs/archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md`](archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md), with a one-line pointer left in each place it used to sit inline. This file's own remaining content (§1-§9 above, and this changelog going forward) is now current-state-only, matching its own stated purpose for the first time since early rounds of superseding began. **Everything below this changelog entry, chronologically, remains here** (documents changes made while this file already reflected the current 18-client Table 1 model, not superseded history in its own right).

**2026-08-07 (reclining chair/exam couch added as a real costed line, per Anthony's direct instruction)** — Previously only a flagged gap (`docs/VERIFICATION-TRACKER.md` item 30). Added to `equipment-costs.md` §1 as A$500-900 `[MODELED]`. Propagated here: Equipment line A$42,690-96,530 -> A$43,190-97,430, §7.1 TOTAL A$60,690-139,530 -> A$61,190-140,430, §7.4 this-agent's-own component sum A$356,890-576,280 -> A$357,390-577,180. Anthony's own adopted total (A$292,335-594,900) is unaffected — it was never derived from this agent's component sum, per the pre-existing disclosed gap noted in §7.4.

> **The remaining changelog entries below (2026-07-29 through the 2026-08-05 REBASE) predate this file's own "current state as of today" framing and describe how the 18-client Table 1 model came to be adopted — genuinely historical narrative, not current-state figures. Relocated in full to [`docs/archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md`](archive/CURRENT-STATE-HISTORICAL-ARCHIVE.md)'s own "Full Historical Changelog" section (2026-08-16, D1) rather than duplicated here — see that file for the complete, unabridged entries.**

