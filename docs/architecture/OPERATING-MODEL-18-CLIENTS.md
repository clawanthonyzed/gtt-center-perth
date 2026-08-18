# Operating Model — 18 Clients/Day (Table 1, Planning Case)

**Date:** 2026-08-18 (Phase D) | **Purpose:** One place that visually demonstrates how the 18-client/day committed model actually runs, minute by minute, and reconciles that operating reality against the financial model — not asserted, shown. This document is written to be dossier-ready (Phase L will reference it directly, not duplicate it).

**Status of the underlying numbers, restated so this document is never read as "all settled":** Revenue A$163,721.88/month (VERIFIED derivation, `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §4), Payroll A$101,717.02/month (MODELLED — includes one MODELLED/CORRECTED-not-VERIFIED wage figure, the Venue Manager, see §7 below), Operating Result A$48,024.86/month (CALCULATED from the above), Break-even 10.704 clients/day (CALCULATED), cash trough -A$54,016.81 at Month 2, cumulative positive from Month 5 (CALCULATED, accrual-basis proxy). None of this is real trading data — there is no venue open yet.

---

## 1. Operating Hours Overview

| Window | Hours | Purpose |
|---|---|---|
| AM (GTT) | 07:00–13:00 | GTT collection + wellness services, synchronized 2-chair model |
| PM | 13:00–18:00 | Standalone wellness services, PM packages, gap-fill |
| Total trading day | 07:00–18:00, Monday–Saturday | 11 hours, no formal handover period (per Anthony's explicit instruction — the AM and PM windows are staffed by different people on different shift patterns, not a single continuous shift with a handover meeting) |

**No afternoon GTT collection** — GTT blood draws occur only in the AM window, ending by ~12:25 for the last pair (see §2). Phlebotomists are not rostered for any PM/general-venue duties (`docs/architecture/STAFF-PROFILES.md` Position 02).

---

## 2. AM Operating Timetable — 18 Clients, 9 Pairs, Solver-Verified Timing

**Source of timing data:** `docs/scenario-c-sync-timetables.md` §0.6a, "Table 1 — 07:00 start, 25-min cadence" — the exact schedule sent to WDP's Carole Rivers, independently verified programmatically for zero chair/phlebotomist collisions across all 18×17/2=153 pairwise comparisons. **GTT draws occur at EXACTLY +60min (Draw 2) and +120min (Draw 3) from each client's own Draw 1 — never approximate, per Carole's own hard clinical-mark requirement.** Every draw is exactly 5 minutes.

**Staff-to-client assignment shown below (which named staff member serves which client) is an ILLUSTRATIVE, reasonable rotation consistent with the pattern already established at the 12-client volume (`scenario-c-sync-timetables.md` §0.1/§0.2) — NOT independently re-solved by the scheduling solver at 18 clients specifically.** What IS solver-verified at 18 clients: (a) zero draw/chair timing collisions, (b) peak concurrent demand on each treatment line stays within its committed capacity (Massage+Beauty pool ≤4, Nails ≤2, Hair ≤2, `scenario-c-sync-timetables.md` §0.6), (c) total headcount = 8 treatment + 2 phlebotomists. The specific M1-vs-M2 (etc.) client rota is a day-to-day rostering decision for the eventual Venue Manager, not a fixed structural requirement.

| Pair | Chair A client / Chair B client | Draw 1 (5min) | Service 1 (45min) | Draw 2 (+60min, 5min) | Service 2 (45min) | Draw 3 (+120min, 5min) | Chair A room/staff | Chair B room/staff | Reception/VM | Lounge status |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C1 / C2 | 07:00–07:05 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 | Massage room (M1) → Beauty room (B1) | Nail station 1 (N1) → Hair chair 1 (H1) | VM checks in C1/C2, manages Fresha | Buffer only — no lounge dwell in the fixed-block model (see note below) |
| 2 | C3 / C4 | 07:25–07:30 | 07:30–08:15 | 08:25–08:30 | 08:30–09:15 | 09:25–09:30 | Massage room (M2) → Beauty room (B2) | Nail station 2 (N2) → Hair chair 2 (H2) | VM checks in C3/C4 while C1/C2 mid-Service 1 | Buffer only |
| 3 | C5 / C6 | 07:50–07:55 | 07:55–08:40 | 08:50–08:55 | 08:55–09:40 | 09:50–09:55 | Massage room (M1) | Nail station 1 (N1) | VM checks in C5/C6; C1/C2 depart ~09:13 | Buffer only |
| 4 | C7 / C8 | 08:15–08:20 | 08:20–09:05 | 09:15–09:20 | 09:20–10:05 | 10:15–10:20 | Massage room (M2) | Nail station 2 (N2) | VM checks in C7/C8; C3/C4 depart ~09:38 | Buffer only |
| 5 | C9 / C10 | 08:40–08:45 | 08:45–09:30 | 09:40–09:45 | 09:45–10:30 | 10:40–10:45 | Massage room (M1) | Nail station 1 (N1) | VM checks in C9/C10; C5/C6 depart ~10:03 | Buffer only |
| 6 | C11 / C12 | 09:05–09:10 | 09:10–09:55 | 10:05–10:10 | 10:10–10:55 | 11:05–11:10 | Massage room (M2) | Nail station 2 (N2) | VM checks in C11/C12; C7/C8 depart ~10:28 | Buffer only |
| 7 | C13 / C14 | 09:30–09:35 | 09:35–10:20 | 10:30–10:35 | 10:35–11:20 | 11:30–11:35 | Massage room (M1) | Nail station 1 (N1) | VM checks in C13/C14; C9/C10 depart ~10:53 | Buffer only |
| 8 | C15 / C16 | 09:55–10:00 | 10:00–10:45 | 10:55–11:00 | 11:00–11:45 | 11:55–12:00 | Massage room (M2) | Nail station 2 (N2) | VM checks in C15/C16; C11/C12 depart ~11:18 | Buffer only |
| 9 | C17 / C18 | 10:20–10:25 | 10:25–11:10 | 11:20–11:25 | 11:25–12:10 | 12:20–12:25 | Massage room (M1) | Nail station 1 (N1) | VM checks in C17/C18 (last new pair); C13/C14 depart ~11:38 | Buffer only |

**Lounge status, honestly answered:** the AM model's fixed per-client block is Draw1[0-5min] → Service1[5-50min] → 10min buffer[50-60min] → Draw2[60-65min] → Service2[65-110min] → 10min buffer[110-120min] → Draw3[120-125min] → depart. There is **no scheduled idle lounge-waiting period built into this timetable** — every minute is accounted for as draw, service, or a 10-minute walk-back/prep buffer. The GTT Lounge (8 reclining chairs, `docs/floor-plan-concept.md`) is used for the two 10-minute buffer windows per client (walking from the collection chair to the treatment room and back) and as the departure point after Draw 3, but is not a place clients wait idle for an extended period under this model. This is a genuine, useful finding surfaced by building the visual timetable: **the "lounge experience" is largely two 10-minute transition windows plus a brief post-Draw-3 farewell, not a long relaxed wait** — worth flagging for the customer-experience chapter (Phase I), not something this document resolves.

**GTT capacity confirmed by this timetable:** 9 pairs × 2 clients = **18 clients/day**, last Draw 1 at 10:20 (10 minutes inside WDP's "not normally after 10:30am" guidance), last departure ~12:33pm — all within the 07:00-13:00 AM shift window (no treatment staff or phlebotomist needs to work past 13:00 to finish the day's committed bookings).

**No AM gap-fill built into this table.** The AM window is fully occupied by the 18-client GTT+package structure — there is no idle treatment-staff capacity in the 07:00-13:00 window to sell as standalone/gap-fill bookings under this schedule, since every treatment slot (Massage/Beauty/Nails/Hair) is already allocated to a GTT client's Service 1 or Service 2. **This is a real, useful finding, not previously stated explicitly anywhere in this repo:** "AM gap-fill revenue," where it appears elsewhere in this repo's ramp/downtime-fill discussion, refers to filling GAPS BETWEEN bookings on a lower-volume actual day (below the 18-client design ceiling), not additional revenue on top of a full 18-client day. At full committed capacity, there is no AM gap-fill capacity — flagged here so it is not double-counted anywhere.

---

## 3. PM Operating Timetable — 16 Sessions/Day Steady State, and a Real Reconciliation Finding

**PM capacity basis:** `data/canonical/client_assumptions.yml#pm_steady_state_capacity` — 16 sessions/day, "~50% utilisation of theoretical 4-line capacity," MODELLED, no real demand data exists yet. Four treatment lines (Massage, Beauty, Nails, Hair) share the 5-hour PM window (13:00-18:00, 300 minutes), each averaging 16÷4 = 4 sessions/day at ~46 minutes/session (1÷1.3 sessions/hr throughput) — consistent with `docs/pm-staffing-roster.md`'s own original hours-based costing formula.

### 3a. Illustrative PM Session Schedule (one treatment line shown; the other 3 lines follow the same pattern, offset)

| Time | Massage line | Beauty line | Nails line | Hair line | PM Reception | Lounge/gap-fill |
|---|---|---|---|---|---|---|
| 13:00–13:46 | Session 1 (individual or 1st half of a package) | Session 1 | Session 1 | Session 1 | Check-in, Fresha, payment for 13:00 arrivals | Standalone/gap-fill clients seated, browsing retail |
| 13:46–14:32 | Session 2 | Session 2 | Session 2 | Session 2 | Ongoing check-in/checkout | — |
| 14:32–15:18 | gap (buffer/no booking) | Session 3 | gap | Session 3 | Ongoing | — |
| 15:18–16:04 | Session 3 | gap | Session 3 | gap | Ongoing | — |
| 16:04–16:50 | Session 4 | Session 4 | Session 4 | Session 4 | Ongoing | — |
| 16:50–18:00 | Wind-down / early-release window if no further bookings | Same | Same | Same | Closing procedures | Last checkout ~17:50 |

**This is illustrative, not solver-verified** — no scheduling solver has been run against the PM window the way the AM window has (a genuine, disclosed gap; PM demand has no real booking data, so building a hard-constraint solve against an assumed pattern would risk manufactured precision). The table demonstrates the SHAPE (4 sessions/role/day, spread across the window with real gaps for staggered/early-release rostering) that the financial model's own hours-based costing formula (§3e of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`) already assumes — it does not independently verify a specific booking sequence.

### 3b. A Real Reconciliation Finding — PM "Sessions" vs. PM "Transactions" Are Not the Same Unit, and the Model Currently Conflates Them

**Built while constructing this timetable, not previously surfaced anywhere in this repo.** The 16-sessions/day figure (`client_assumptions.yml#pm_steady_state_capacity`, named "PM individual services capacity") was originally defined, per `docs/pm-staffing-roster.md` line 126, for an **"Individual Services (NOT packages)"** revenue model — every session was a single 1-therapist, 1-client booking. `docs/architecture/PM-PACKAGES.md` (created 2026-08-17) later introduced two real packages (PM Refresh: Massage 45min + Mini facial 30min; PM Restore: Gel manicure 45min + Blow-dry 30min) and a blended average transaction value (A$117 = 60% individual + 25% PM Refresh + 15% PM Restore). **The A$117 figure was then multiplied directly by the same "16 sessions/day" figure** (`FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §4b: "16 sessions x A$117 x 22 days") — but a package like PM Refresh uses services from TWO different treatment lines (Massage room AND Beauty room), consuming **2 of the "16 sessions"** for what is really only **1 client transaction**.

**Quantified impact, worked through directly, using the disclosed 60/25/15 mix:**

| Component | Share of transactions | Sessions consumed per transaction | Sessions per 100 transactions |
|---|---|---|---|
| Individual a-la-carte | 60% | 1 | 60 |
| PM Refresh (Massage+Beauty) | 25% | 2 | 50 |
| PM Restore (Nails+Hair) | 15% | 2 | 30 |
| **Total** | **100%** | | **140 sessions per 100 transactions** |

If treatment-staff capacity is genuinely fixed at 16 sessions/day (the figure the labour-cost model correctly uses), then the actual number of **client transactions** the venue can serve per day, once package bookings are accounted for, is **16 × (100/140) = 11.43 transactions/day**, not 16. Recomputing PM weekday revenue directly from this transaction mix:

- Individual: 6.86 sessions-worth ÷ 1 session/transaction = 6.86 transactions × A$84.11 = A$576.75
- PM Refresh: 5.71 sessions ÷ 2 = 2.86 transactions × A$185.00 = A$528.57
- PM Restore: 3.43 sessions ÷ 2 = 1.71 transactions × A$135.00 = A$231.43
- **Total PM revenue at 16 sessions/day capacity, transaction-consistent basis: ≈ A$1,336.75/day weekday** — versus the current canonical model's A$1,872.00/day (16 × A$117) — **a ≈28.6% overstatement in the current PM revenue figure, if this interpretation is correct.**

**This is NOT corrected in the canonical model this pass — flagged as a genuine open item requiring Anthony's decision, not unilaterally rewritten.** The reason it is not simply "fixed": `docs/architecture/PM-PACKAGES.md` §6 itself already discloses that whether a package's two services run **concurrently (2 staff members simultaneously, genuinely consuming 2 "sessions" of capacity at once)** or **sequentially (1 client occupying 2 different staff members' time slots one after the other, which is operationally identical to 2 sessions from a capacity standpoint but could alternatively be resourced by ONE dual-qualified staff member doing both parts, consuming only 1.5x a normal session's time from a single person)** is an "operational decision for later, not decided here." The financial/capacity impact of this reconciliation issue depends entirely on that undecided operational question — resolving it by picking an interpretation unilaterally here would risk exactly the "force a match" error Anthony explicitly warned against. See §9 (Decisions Required) below.

**What IS safe to state without waiting on that decision:** the current canonical PM revenue figure (A$45,236.88/month, `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §4b) is very likely an **overestimate**, by an amount between 0% (if a single dual-qualified therapist delivers both halves of a package back-to-back, consuming only marginally more than 1 session's worth of capacity) and ~28.6% (if packages fully consume 2 independent staff-sessions each, as modelled above). This is a real, bounded, quantified uncertainty — not a vague caveat.

---

## 4. Staff-Lane Timetable, 07:00–18:00

| Lane | 07:00 | 08:00 | 09:00 | 10:00 | 11:00 | 12:00 | 13:00 | 14:00 | 15:00 | 16:00 | 17:00 | 18:00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Venue Manager | **START — AM reception, floor management** | active | active | active | active | active | **wind-down/admin** | admin/rostering/P&L review | admin | admin | **END (15:00)** | — |
| AM Reception | *(covered personally by VM, no separate role)* | | | | | | | | | | | |
| Phlebotomist A (Chair A) | **START — draws for odd-numbered clients** | active | active | active | active (last draw ~12:25) | **END (~12:33, shift ends 13:00)** | — | — | — | — | — | — |
| Phlebotomist B (Chair B) | **START — draws for even-numbered clients** | active | active | active | active | **END (~12:33, shift ends 13:00)** | — | — | — | — | — | — |
| Treatment — Massage+Beauty pool (4) | **START — first client's Service 1/2** | active | active | active | active (last client ~12:10) | **END (AM), early-released or transitions to PM per booking demand** | *(if rostered PM)* active | active | active | active | active | *(if still rostered)* END by 18:00 |
| Treatment — Nails (2) | **START** | active | active | active | active | **END (AM)** | *(if rostered PM)* active | active | active | active | active | END by 18:00 |
| Treatment — Hair (2) | **START** | active | active | active | active | **END (AM)** | *(if rostered PM)* active | active | active | active | active | END by 18:00 |
| PM Reception/Coordinator | — | — | — | — | — | — | **START (13:00)** | active | active | active | active | **END (18:00)** |
| Relief/backup pool | *(on-call, not rostered unless covering an absence)* | | | | | | | | | | | |

**How this visually demonstrates 18/day is genuinely supportable:** every treatment-staff member's AM block (07:00-~12:10/12:33) is fully occupied by the solver-verified 18-client schedule in §2 — there is no idle AM capacity being claimed twice. The Venue Manager's single continuous 07:00-15:00 shift covers the entire AM client-facing window personally (no reception gap at any point, the previously-flagged 07:00/07:15 inconsistency corrected in `STAFF-PROFILES.md` §3) plus a genuine 2-hour post-AM administrative block (rostering, P&L review, pathology-partner liaison) before handing off implicitly (not a formal meeting, just a shift boundary) to PM Reception at 15:00 — PM Reception's own 13:00-18:00 shift already overlaps the VM's last 2 hours, so there is no reception gap at the 13:00 AM-to-PM transition point either.

**Early-release, shown not asserted:** treatment staff who are NOT rostered for any PM bookings (a real possibility on a lower-volume actual day, though not modelled as a headline saving per `conflict_am_labor_ramp_unmodelled`) are released after their last AM client departs (as early as ~10:03 for the M1/N1 pairing's early clients, per §2's departure column) rather than held to a fixed clock-off time — this is the mechanism `STAFF-PROFILES.md` Position 03-05 describes ("minimum 3-hour engagement, released early if the final 2-3 hours of a pencilled shift aren't needed"), shown here operating against the real timetable rather than asserted abstractly. **This upside is NOT included in the headline payroll figure** (§7 below reconciles against the full-shift, no-early-release conservative basis) — early release remains a separate, disclosed, tagged saving (`docs/CURRENT-STATE.md` §8), not blended in.

---

## 5. Financial / Roster Reconciliation — Shown, Not Asserted

**Method:** for every position, (rostered hours/month) × (wage rate) × (Saturday penalty where applicable) = the exact figure `tools/cost_ramp_model.py` computes, cross-checked against a live run of that code, not hand-derived separately.

| Position | Headcount rostered/day | Hours/day (AM) | Hours/day (Sat) | Wage rate | Weekday monthly (22 days) | Saturday monthly (4.33 days) | Monthly total | Matches `cost_ramp.yml`? |
|---|---|---|---|---|---|---|---|---|
| Treatment — Massage+Beauty | 4 | 6 | 6 | A$37.50/hr (A$56.25 Sat) | 4×6×37.50×22 = A$19,800.00 | 4×6×56.25×4.33 = A$5,845.50 | A$25,645.50 | Yes — matches §3a of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` exactly |
| Treatment — Nails | 2 | 6 | 6 | A$36.81/hr (A$55.215 Sat) | 2×6×36.81×22 = A$9,717.84 | 2×6×55.215×4.33 = A$2,868.97 | A$12,586.81 | Yes |
| Treatment — Hair | 2 | 6 | 6 | A$36.81/hr (A$55.215 Sat) | A$9,717.84 | A$2,868.97 | A$12,586.81 | Yes |
| Phlebotomists | 2 | 6 | 6 | A$34.375/hr (A$51.5625 Sat) | 2×6×34.375×22 = A$9,075.00 | 2×6×51.5625×4.33 = A$2,679.19 | A$11,754.19 | Yes |
| Venue Manager | 1 | 8 | 8 | A$40.00/hr (A$60.00 Sat) — **MODELLED/CORRECTED, see §7** | 1×8×40.00×22 = A$7,040.00 | 1×8×60.00×4.33 = A$2,078.40 | A$9,118.40 | Yes — matches `cost_ramp_model.py`'s `OPENING_TIME_INCREMENT_DAILY`/`VENUE_MANAGER_SATURDAY_DAILY` output exactly |
| PM Reception | 1 | 5 | 5 | A$33.71/hr (A$50.565 Sat) | 1×5×33.71×22 = A$3,708.10 | 1×5×50.565×4.33 = A$1,094.73 | A$4,802.83 | Yes |
| PM Treatment (4 roles, session-based) | 4 (shared with AM pool) | ~3.08 | 3.0 (floor) | A$37.155/hr blended (A$55.7325 Sat) | A$10,070.72 | A$2,895.83 | A$12,966.55 | Approximately — small floating-point rounding gap (~A$0.21-0.44/month) already disclosed in §3e, immaterial |
| **TOTAL WAGES** | | | | | | | **≈A$89,461.09 (hand-sum) / A$89,460.88 (live code)** | Reconciles within the disclosed rounding gap |
| + Superannuation (12%) | | | | | | | A$10,735.31 | Matches |
| + Workers Comp (1.7%, PLACEHOLDER) | | | | | | | A$1,520.83 | Matches |
| **= TOTAL MONTHLY PAYROLL** | | | | | | | **A$101,717.02** | **Matches `data/canonical/cost_ramp.yml#cost_table1_m5plus.payroll_costs` exactly** |

**Verification method, disclosed:** this table was built by manually re-deriving every line from the wage rates in `data/canonical/wages.yml` and the hours/headcount in `docs/architecture/STAFF-PROFILES.md`, then cross-checked against a fresh live run of `tools/cost_ramp_model.py`. **No manual patching was required** — the reconciliation holds because the roster and the financial model are built from the same source constants (`tools/cost_ramp_model.py`'s own named, commented constants), not two independently-maintained numbers that happen to coincide. This is the structural reason a reconciliation gap has not appeared here (unlike §3b's PM session/transaction finding, which IS a real gap, between two conceptually different quantities that were never meant to be the same number in the first place).

---

## 6. Treatment Staff — Why 8, Answered Directly

- **Required simultaneous capacity:** peak concurrent demand at 18 clients/day is 4 on the Massage+Beauty pool, 2 on Nails, 2 on Hair (`scenario-c-sync-timetables.md` §0.6, sweep-line + greedy first-fit, both methods agree) = **8 total**, not derivable from a naive "clients ÷ appointment slots" estimate — it required the actual solver run.
- **Appointment durations:** every AM service block is fixed at 45 minutes (§2), both Service 1 and Service 2, per Carole's own exact-clinical-mark requirement forcing this fixed-block structure.
- **Utilisation:** at 18 clients/day, each of the 8 treatment staff serves either 2 or 3 clients across the 6-hour AM shift (roughly 90-135 minutes of active service time out of 360 minutes rostered) — meaning **AM treatment-staff utilisation is genuinely low (25-37.5%)** under the conservative no-early-release costing basis used in the headline payroll figure. This is not hidden: it is exactly why the Downtime-Fill/Early-Release framework (`docs/CURRENT-STATE.md` §8) exists as a separate, disclosed upside.
- **Employed vs. rostered simultaneously:** all 8 are rostered simultaneously every trading day at the committed 18-client volume (§2's timetable requires all 8 present) — but the venue plans to EMPLOY 10-11 people across this pool (`STAFF-PROFILES.md` §1), with 2-3 not rostered on any given day, providing absence coverage.
- **Casual/part-time mix:** all treatment staff are casual initially, reviewed for conversion to part-time once regular proven hours exist (`STAFF-PROFILES.md` Position 03, `docs/CURRENT-STATE.md`'s hiring-model settlement, 2026-07-30).
- **How early release actually works, shown against the real timetable:** see §4 above — a treatment staff member with no PM bookings can be released as soon as their last AM client departs (as early as ~10:03 for the earliest-finishing rotation), rather than held to a fixed end-of-shift time, per the minimum-3-hour-engagement/staggered-release policy already established.

## 7. Phlebotomy — Answered Directly, WDP Dependency Flagged Explicitly

- **Required per day and why:** 2, one per collection chair — the synchronized two-chair model requires exactly 2 simultaneous phlebotomists for the 07:00-12:25 draw sequence to run without collision (`scenario-c-sync-timetables.md` §0.6).
- **Shift times:** 07:00-13:00 (AM window only — a settled, non-negotiable scope boundary per `STAFF-PROFILES.md` Position 02; phlebotomists do not work PM shifts).
- **Qualifications:** Cert III/IV in Pathology Collection, credentialed under the pathology partner's own accreditation umbrella — not an independent accreditation the venue itself holds.
- **Minimum coverage:** 2, every trading day, no exceptions (both chairs cannot run without both phlebotomists present).
- **Leave/sick coverage:** the tightest coverage constraint in the entire staffing model (`STAFF-PROFILES.md` §1) — a same-day replacement cannot be casually sourced the way a beauty-therapist gap might be, because of the partner-credentialing lead time. Recommended pool: 3-4 on the books, 1-2 above the daily-committed 2.
- **Backup pool:** 1-2 extra credentialed phlebotomists recommended, not all rostered daily.
- **WDP employment-arrangement dependency — flagged explicitly, NOT assumed:** whether phlebotomists are ultimately employed directly by GTT Center Perth, or supplied/employed by WDP (Western Diagnostic Pathology) under the eventual pathology-partner agreement, remains an open commercial question **still waiting on Carole Rivers/WDP** (per the standing constraint: do not send anything further to Carole or speculate new commercial assumptions on this point). **This document does NOT make a final assumption about that employment arrangement.** The headcount, hours, and coverage figures above are correct regardless of WHO employs the phlebotomists (the operational requirement — 2 simultaneous, credentialed, AM-only — does not change), but the WAGE COST currently modelled in `data/canonical/wages.yml` (`Health Professionals and Support Services Award MA000027`) assumes the venue itself bears this cost directly as an employer. If WDP ultimately supplies and pays its own phlebotomists under a service-fee arrangement instead, this entire payroll line (A$11,754.19/month wages, plus its super/workers-comp share) could move OFF the venue's own payroll and into a different cost category (a per-test service fee to WDP) — a materially different P&L shape, not modelled here, explicitly flagged as dependent on the still-open WDP commercial conversation.

## 8. PM Reception Relief — Answered Directly, Genuinely Open Where It's Open

- **Required PM hours:** ~13:00-18:00 (5 hours), sized to the PM window specifically, per `STAFF-PROFILES.md` Position 06.
- **One person vs. relief pool:** ONE person is sufficient for normal day-to-day PM coverage — modelled, not assumed, via real session-load math (§2a of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`: 16 sessions ÷ 5 hours ≈ 3.2 sessions/hour, a normal single-reception-desk workload by real Perth day-spa comparable standards).
- **Minimum headcount:** 1, every PM trading day.
- **Leave/sick coverage — genuinely unresolved, not assumed away:** no relief pool has been sized for this role. This was flagged as an open item in last round's audit and remains open this round — it is a real gap, not a oversight being repeated silently.
- **Is VM covering PM gaps operationally sensible?** **No, not as a standing solution** — the Venue Manager's own rostered hours (07:00-15:00) end before the PM Reception role's own hours even begin in earnest (the two roles overlap only 13:00-15:00, per §4's staff-lane timetable). The VM could plausibly cover a SHORT PM Reception absence during that 13:00-15:00 overlap window, but has no presence at all from 15:00-18:00 — meaning a PM Reception absence in the back half of the PM shift (15:00-18:00) currently has **no coverage plan whatsoever**. This is a genuine, disclosed gap, not resolved by this document.
- **Financial impact if it changes:** if a PM Reception relief pool were added (e.g. 1 extra casual on the books, paid only when covering an absence), the steady-state monthly payroll figure would be UNCHANGED (relief staff are only paid when they actually work, per §9 of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`'s five-concepts distinction) — the cost only materialises on days an absence is actually covered. The practical exposure is: **zero PM Reception coverage on any day the sole PM Reception employee is unexpectedly unavailable during 15:00-18:00**, a real operational risk with no dollar cost currently attached to mitigating it (because no relief has been hired yet).

---

## 9. Decisions Required From Anthony

1. **PM package staffing model (drives §3b's revenue reconciliation):** should PM Refresh/PM Restore packages be delivered by ONE dual-qualified staff member doing both service components back-to-back (minimising capacity consumption, closer to 1 session), or by TWO different staff members handing off (consuming a full 2 sessions of capacity each, materially reducing achievable daily transaction volume and/or overstating current PM revenue by up to ~28.6%)? This was already flagged as undecided in `docs/architecture/PM-PACKAGES.md` §6 — this round's timetable-building exercise shows it has a real, quantified financial consequence, not just an operational preference.
2. **PM Reception relief pool:** should a relief/backup person be identified and put on the books for the 15:00-18:00 gap specifically, even if not regularly rostered? No dollar cost to deciding this now (only to actually using the relief), but the coverage gap is real.
3. **Venue Manager wage classification:** the MA000005 Level 6 correction ($40.00/hr) is this document's best-evidenced figure, but per the standing instruction, still needs professional (accountant/Fair Work) confirmation before being locked as final for real contracts — not a decision this document can make.

---

## 10. Third-Party Dependencies, Restated

- **WDP/Carole Rivers:** phlebotomist employment-arrangement question (§7) remains open, waiting on WDP — not actioned or speculated on further this round, per the standing constraint.
- **Professional wage-classification confirmation:** the Venue Manager's MA000005 L6 reclassification (§7 of `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`) needs accountant/Fair Work sign-off before being used in a real employment contract.
- **Workers compensation rate (1.7%):** re-investigated again this round — Safe Work Australia's own comparison tables were attempted as an alternate source to WorkCover WA's (blocked 403 last round); this round's attempts returned network connection errors (`ECONNRESET`) rather than a 403, a different but equally genuine tooling limitation. One useful data point WAS found via search (not a direct primary-source fetch): Safe Work Australia's own reporting cites a **national average workers-compensation premium rate across all industries of approximately 1.73% for 2024-25** — and beauty/personal-care services are generally characterised as a lower-risk category than the all-industry average. This suggests the current 1.7% placeholder, being roughly EQUAL to the all-industry average rather than below it, is **plausibly a slight overestimate for this specific, lower-risk classification** — but this is a secondary/inferential data point, not a verified WA-specific PRC rate for this venture's actual classification. **Remains explicitly PLACEHOLDER**, not upgraded to VERIFIED. Anthony or a broker should obtain the actual current WorkCover WA PRC rate directly.

---

## Changelog

**2026-08-18 (Phase D)** — Created per Anthony's explicit instruction to visually demonstrate that the 18-client model actually works and that staffing genuinely feeds the financial model. Built the AM operating timetable (reusing solver-verified timing from `scenario-c-sync-timetables.md` §0.6a, adding room/staff/reception/lounge columns), an illustrative PM operating timetable, a staff-lane timetable (07:00-18:00), and a full financial/roster reconciliation table (verified line-by-line against `tools/cost_ramp_model.py`'s live output, no manual patching required). Surfaced one real, previously-undetected reconciliation problem: PM "sessions" (a staffing-capacity unit) and PM "transactions" (a revenue-counting unit) are conflated in the current canonical model, because package bookings consume 2 sessions per 1 transaction but are counted as consuming only 1 — current PM revenue is likely overstated by up to ~28.6%, bounded and quantified but NOT unilaterally corrected this round, since the resolution depends on an already-flagged, still-undecided operational question (`PM-PACKAGES.md` §6). Answered the Treatment Staff / Phlebotomy / PM Reception coverage questions directly, with the WDP phlebotomist-employment dependency explicitly flagged rather than assumed. Workers comp re-investigated via an alternate source (Safe Work Australia) — blocked by network errors, remains PLACEHOLDER; one useful secondary data point found (1.73% national all-industry average) suggesting the current 1.7% may be a slight overestimate for this lower-risk classification, not confirmed.
