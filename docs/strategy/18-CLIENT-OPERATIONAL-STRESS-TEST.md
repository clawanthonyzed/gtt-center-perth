# 18-Client/Day Operational Stress Test

**Date:** 2026-08-14 | **Status:** Current. Single document, per instruction. Reconstructs the actual, solver-verified Table 1 schedule (`docs/scenario-c-sync-timetables.md` §0.6a) minute-by-minute and stress-tests it against the founder's operating rules below. No financial-model figures, service pricing, staffing costs, or naming are touched. Where the repository doesn't contain an answer, that gap is named explicitly rather than filled with an invented number.

**Founder rules treated as settled, not re-litigated:** 18 clients/day is the operating design target; 12/day is now a downside/lower-utilisation scenario only. Every AM/GTT service is 45 minutes or less, no exceptions, for every category (massage, beauty, hair, nails, wellness, future services) — this resolves `docs/services-pricing-locked.md`'s nail-service ambiguity (French gel manicure 50min, gel pedicure 50min, French gel pedicure 55min are **PM-only**, not GTT-window services). The underlying pricing document is not edited here, per instruction; this document records the ceiling as the operative rule going forward.

---

## 1. Reconstructing the 18-Client Day

Sourced directly from `docs/scenario-c-sync-timetables.md` §0.6a, Table 1 — 07:00 start, 25-minute pair cadence, 9 pairs, 2 chairs. Every client's own visit follows the identical fixed shape: Draw 1 (5 min) → Service 1 (45-min slot) → 10-min buffer → Draw 2 (5 min, exactly +60min from her own Draw 1) → Service 2 (45-min slot) → 10-min buffer → Draw 3 (5 min, exactly +120min from her own Draw 1) → departure.

| Hour block | What's happening |
|---|---|
| **07:00–08:00** | Pairs 1, 2, 3 admitted (07:00, 07:25, 07:50). Both chairs continuously cycling Draw 1s. First Service 1 blocks running by 07:05. |
| **08:00–09:00** | Pairs 4, 5 admitted (08:15, 08:40). Pair 1's Draw 2 at 08:00; pair 2's at 08:25; pair 3's at 08:50. Venue now has 3-4 pairs simultaneously in different phases — the steady-state overlapping pattern begins here. |
| **09:00–10:00** | Pairs 6, 7 admitted (09:05, 09:30). Pair 1 departs (~09:10-09:13, first departure of the day). Draw 2s and Draw 3s and Service blocks all running concurrently across 5-6 pairs. |
| **10:00–11:00** | Pairs 8, 9 admitted (09:55, 10:20 — the last pair of the day). Pairs 2-5 progressively finish and depart through this hour. |
| **11:00–11:30** | Pair 8 (clients 15/16) in Service 2 (11:00-11:45). Pair 9 (17/18, the last pair) in Service 1 (10:25-11:10) then buffer. Pair 7 (13/14) finishing Service 2 (ends 11:20). |
| **11:30–12:00** | See §2 for full 15-min detail — this is the AM tail. |
| **12:00–12:30** | See §2 — last active AM service ends 12:10; last draw 12:20-12:25. |
| **12:30–13:00** | AM fully cleared (last estimated departure ~12:30-12:33 — see the flagged assumption in §2). PM operating status depends entirely on which opening option is chosen (§5). |
| **13:00 onward** | Pure PM operation, no AM activity remaining under any of the three tested opening options. |

**One derived figure, flagged as an assumption rather than a repository fact:** Table 1's own timetable gives exact Draw 3 end times but does not carry an explicit "Depart" column for this specific table (unlike the historical 10/12-client 40-minute-cadence tables, which did). Using the same ~5-8 minute walkout convention those historical tables established, the last pair's estimated departure is **~12:30-12:33pm**. `[MODELED — assumption: consistent with the source document's own historical Depart-column convention, not independently re-stated for Table 1]`.

---

## 2. Physical Client Count, 11:30–13:00 (15-Minute Increments)

Built directly from Table 1's client-level draw/service times (§0.6a) — not invented.

| Time | AM at blood draw | AM receiving service | AM in transition/buffer | AM departing | **Total AM present** | PM (Option A, opens 12:00) | PM (Option B, opens 12:30) | PM (Option C, opens 13:00) |
|---|---|---|---|---|---|---|---|---|
| 11:30 | 2 (C13/14, Draw 3) | 4 (C15/16 + C17/18, both in Service 2) | 0 | 0 | **6** | 0 | 0 | 0 |
| 11:45 | 0 | 2 (C17/18, Service 2) | 2 (C15/16, buffer) | 0 | **4** | 0 | 0 | 0 |
| 12:00 | 2 (C15/16, Draw 3 ending) | 2 (C17/18, Service 2) | 0 | 0 | **4** | ~1 arriving `[not modelled — illustrative]` | 0 | 0 |
| 12:15 | 0 | 0 | 2 (C17/18, buffer, awaiting final draw) | 0 | **2** | ~1-2 in early service | ~1 arriving | 0 |
| 12:30 | 0 | 0 | 0 | 2 (C17/18) | **2** | ~2-3 across various stages | ~1 arriving (overlaps 2 departing AM) | 0 |
| 12:45 | 0 | 0 | 0 | 0 | **0** | ~3-4 | ~1-2 | 0 |
| 13:00 | 0 | 0 | 0 | 0 | **0** | ~3-5 (steady state) | ~2-3 | ~1 arriving |

PM figures are explicitly not modelled bookings from the repository — no PM demand/arrival-rate data exists anywhere in this venture's documents (`docs/strategy/STRATEGIC-REPORT.md` §12 already flags PM capacity as a planning estimate, not real data). The illustrative counts above exist only to show the *shape* of overlap under each option, not a forecast.

**Answering the key question directly: what is the maximum number of customers physically present during the transition?**

- **Option A (PM opens 12:00):** peak overlap moment is 12:00 itself — 4 AM clients (2 finishing their final draw, 2 still receiving Service 2) plus the first PM arrival(s), landing at roughly **5 total**, with the added complexity that one AM pair is mid-clinical-procedure (a blood draw) at the exact moment PM opens.
- **Option B (PM opens 12:30):** peak overlap is 2 AM clients (already in pure, quiet departure mode — no active service or clinical procedure happening) plus early PM arrivals, landing at roughly **3-4 total**, with no clinical activity in progress.
- **Option C (PM opens 13:00):** **zero physical overlap** — the venue is genuinely empty of clients from ~12:33 to 13:00, a ~27-30 minute gap with nobody on site.

---

## 3. Staff Count, 11:30–13:00

Using only existing, documented headcount (`docs/CURRENT-STATE.md` §4) — no new staff invented.

| Group | Headcount | Source |
|---|---|---|
| AM treatment/clinical staff (4 Massage+Beauty pool + 2 Nails + 2 Hair) | 8 | `docs/CURRENT-STATE.md` §1/§4, verified via sweep-line + greedy first-fit |
| AM phlebotomists (Chair A / Chair B) | 2 | Same source |
| Reception/hospitality | **1** | `docs/business-plan.md` §5: "Receptionist/Manager, split shift covering AM open + PM administrative window" — **a single person, not a dedicated AM role plus a dedicated PM role.** This is the single most consequential headcount fact for this stress test — see §5, §13. |
| PM treatment staff | 4 dedicated casual hires (1 each: massage, hair, nail, beauty) | `docs/pm-staffing-roster.md` — hours-based costing, rostered to confirmed bookings, no reason they need to be on-site before PM's chosen opening time |
| PM reception/hospitality | Same 1 person as AM (no separate PM-only reception role exists in any document) | Same as above |
| Management/other | Venue Manager (1), **not yet hired**, recruitment gated on venue confirmation | `docs/CURRENT-STATE.md` §4 |
| Relief/backup pool (not rostered by default) | 3 dual/cross-trained roles + 1 relief phlebotomist | Available to be pulled in, at cost, not part of the standing daily roster |

**Explicit flag, per instruction:** the reception/hospitality headcount is stated in the source documents as a single shared role. This document does not invent a second reception body — it is flagged here as an assumption/decision the founder needs to make explicitly (§13, §14), not silently resolved.

---

## 4. Staff Utilisation, 11:30–13:00

Derived directly from §2's client-phase data — each AM client actively receiving a service occupies exactly one treatment staff member; each AM client at a draw occupies both phlebotomists (Chair A and Chair B always run in sync under Table 1).

| Time | Phlebotomists busy (of 2) | Treatment staff busy (of 8) | What's happening |
|---|---|---|---|
| 11:30 | 2 (drawing C13/14) | 4 (serving C15/16 + C17/18) | Peak of this window — both clinical and treatment sides fully engaged |
| 11:45 | **0 — idle** | 2 (serving C17/18 only) | A genuine, real gap: no draw scheduled between 11:35 and 11:55 (a 20-minute phlebotomist idle window) |
| 12:00 | 2 (finishing C15/16's draw) | 2 (serving C17/18) | Last-but-one draw of the day wrapping up |
| 12:15 | 0 — idle, next draw in 5 min | **0 — all treatment staff free** | AM treatment work for the day is effectively complete 10 minutes before the very last draw |
| 12:30 | 0 — fully done for the day | 0 | Both phlebotomists and all 8 treatment staff are free; only 2 clients remain, in pure departure |
| 12:45 | 0 | 0 | AM side fully cleared |
| 13:00 | 0 | 0 | AM side fully cleared |

**Genuine bottleneck identified:** not treatment or clinical capacity — both wind down naturally and well ahead of the last client's departure. The bottleneck is **reception**, specifically at 12:00 under Option A, where the single shared reception role would need to simultaneously manage two AM clients finishing a blood draw, two AM clients still receiving a service, *and* welcome the first PM arrival — four distinct client-facing tasks converging on one person.

---

## 5. The AM/PM Transition — Three Options Stress-Tested

| Factor | Option A (PM 12:00) | Option B (PM 12:30) | Option C (PM 13:00) |
|---|---|---|---|
| Customer congestion | Real: up to ~5 clients present, including 2 mid-clinical-procedure | Minimal: ~3-4 clients, no active clinical procedure | None: 0 clients present for ~27-30 min |
| Reception workload | High — one person managing departure + arrival + a clinical handoff simultaneously | Low — one person managing a quiet departure + early arrivals, no clinical activity | None during the gap, then a normal single-direction PM opening |
| Treatment-room availability | Constrained — 2 of 8 treatment staff and both AM treatment rooms/stations still occupied by C17/18's tail | Fully available — AM treatment already wound down by 12:15 | Fully available, with room to spare |
| Staff lunch/break feasibility | Poor — no natural break exists at exactly 12:00 (phlebotomists' one real gap is 11:45, not 12:00) | Good — 12:00-12:30 (or a 12:15-12:30 slice of it) aligns closely with the natural clinical lull already present in the schedule | Best on paper, but sacrifices ~30 more minutes of PM capacity than Option B for no clear operational gain beyond what B already provides |
| Handover requirements | Highest — genuine simultaneous AM/PM activity | Low — the AM side is already essentially finished | None — sequential, not overlapping |
| Customer perception | Risk of feeling processed — an AM client finishing a blood draw while a PM client walks in for a facial is the closest this model comes to "a busy clinic changing shift" | Calmer — the last AM clients are already in quiet departure mode, not visibly mid-procedure, when PM activity begins | Calmest in principle, but an empty venue for half an hour is its own (different) signal, and isn't free — see revenue note below |
| Operational complexity | Highest | Low | Lowest, but at a real capacity cost |
| Revenue/capacity impact | No AM capacity lost; earliest possible PM start | ~30 minutes of PM capacity later than Option A | ~60 minutes of PM capacity later than Option A — the largest forgone-capacity cost of the three |
| Premium-experience impact | Real risk of undermining the founder's own standard at exactly the wrong moment (§12) | Best alignment between "calm and personal" and "not wasting capacity" | Cleanest experience in isolation, but not clearly better than Option B for the extra capacity given up |

**Recommendation, based on the evidence above:** **Option B (PM opens 12:30)** is the strongest of the three. It is not an arbitrary middle choice — it specifically captures a real, already-existing lull in the schedule (treatment staff and phlebotomists are both already idle by 12:15-12:20, ten minutes before the very last draw even happens), so almost none of Option A's genuine congestion risk is inherited, while giving up only 30 minutes of PM capacity rather than Option C's 60. Option A's core problem is not volume, it's timing: at exactly 12:00, two AM clients are still mid-clinical-procedure, which is the one moment this model should most want to avoid overlapping with a PM arrival. Option C solves the congestion problem completely but at a real, avoidable capacity cost that the data doesn't otherwise justify. This is a recommendation, not a decision made on the founder's behalf — the founder may still prefer Option C's cleaner separation, or Option A's earlier PM start, for reasons this document doesn't have visibility into (e.g. staff preference, real early-PM booking demand).

---

## 6. Staff Handover / Lunch — Testing a Deliberate Closure

Testing the founder's own framing directly: *"If it feels like a busy clinic changing shift we can close for staff handover/lunch."*

**Finding: a deliberate closure is not clinically or operationally required** — §4 shows the schedule already contains a natural lull (phlebotomists idle 11:45-12:15 in the relevant sense once the final draw sequence is accounted for; all treatment staff free from 12:15 onward). A closure would not be fixing a scheduling defect — it would be a deliberate choice to convert an already-existing quiet period into a formal break, primarily to solve the single-reception-role problem (§3, §13) and to give staff an actual scheduled rest rather than an informal gap.

**Testing 15 / 30 / 45 minutes:**
- **15 minutes (e.g. 12:15-12:30):** aligns closely with the natural lull already present. Sufficient for a reception handover and a short breather, but likely too brief for a genuine staff lunch.
- **30 minutes (e.g. 12:00-12:30, functionally equivalent to Option B above):** gives a real break window, fully resolves the single-reception-role conflict, and costs only the same 30 minutes of PM capacity Option B already costs — this is not really a separate additional item from §5's recommendation, it's the same decision viewed through a staff-welfare lens rather than a customer-congestion lens, and both lenses point to the same answer.
- **45 minutes:** pushes the PM capacity cost higher without a correspondingly larger benefit, since the natural lull and a 30-minute deliberate close already cover the real need.

**Conclusion:** 30 minutes, aligned with Option B's 12:30 PM opening, is operationally sufficient and is the strongest evidence-based choice among the three tested durations — not because 30 is inherently the "right" number, but because it's the smallest closure that fully absorbs both the reception conflict and a genuine break, without giving up capacity the data doesn't otherwise justify.

---

## 7. Open-Plan Environment

Cross-referenced against `docs/floor-plan-concept.md`'s committed layout, not redesigned:

- **Blood-draw privacy** is structurally solved already — the Blood Collection Room is the only solid-walled, genuinely clinical space in the venue; nothing in this stress test changes that.
- **Treatment privacy** (massage/facial rooms) relies on curtain partitions, which handle visual privacy adequately but **not acoustic separation** — a real, previously-disclosed limitation (`docs/floor-plan-concept.md`) worth restating here specifically because the AM/PM transition period is exactly when a quieter venue would make any sound leakage more noticeable, not less.
- **Sightlines and reception positioning:** the floor plan does not currently specify whether reception has a sightline to the Blood Collection Room door — relevant here because the transition-period reception workload (§4) would be easier to manage with a clear line of sight to both the Lounge/arrival zone and the collection room, rather than neither. Flagged as unresolved, not assumed either way.
- **PM customer arriving while AM customers remain — is this actually a problem?** Per the brief's own instruction not to treat density as automatically negative: the answer here is **largely no, on its own**. Because the brand's own operating principle is "no clinical signalling outside the one room that needs it" (`docs/strategy/BRAND-ARCHITECTURE.md`), an AM client sitting in the open-plan GTT Lounge already looks like any other guest — not visibly medical. Two women, one AM and one PM, coexisting in the same open Lounge is not inherently a worse experience for either of them; it can read as simply a calm, populated, premium space. **The real risk identified by this stress test is not visual or social incompatibility between AM and PM guests — it's the single reception role's bandwidth (§3, §4, §5) at the specific moment a clinical procedure (a blood draw) is still active.** This distinction matters: it means the fix is a timing/staffing decision (§5's recommendation), not a design change to keep the two customer types apart.
- **Circulation, arrival/departure paths:** not independently assessed here beyond what §2's presence counts already show — peak simultaneous AM presence in the 11:30-13:00 window is 6 people (11:30), well within what an open, spacious 35sqm Lounge plus adjoining zones should comfortably absorb, though this document does not attempt to verify that quantitatively (that would require the floor plan work explicitly out of scope here).

---

## 8. 18-Client Capacity Test Under Varying AM Add-On Uptake

**A key structural finding: the schedule's timing is invariant to service selection, within the 45-minute ceiling.** Because Table 1's timing is driven entirely by fixed clinical draw marks (exact +60/+120-minute marks, zero tolerance — `scenario-c-sync-timetables.md` §0.6), not by which specific service or add-on combination a client chooses, the throughput and duration of the day itself does not change between minimal, moderate, or high AM service uptake — provided every booked service (including any stacked add-ons) fits inside the 45-minute slot.

- **A. Minimal AM add-ons (e.g. Package 1's fixed 2×30min):** operationally the lightest case — real slack exists inside each 45-minute slot. Viable with margin.
- **B. Moderate AM add-on uptake (e.g. a 45-min core service plus one short add-on where duration allows):** viable, provided the combined duration is checked against 45 minutes at time of booking — see the control gap below.
- **C. High AM add-on uptake (e.g. maximum stacked add-ons within Package 2's 45-min slots):** still schedule-viable on paper (the clock doesn't change), but this is where a **soft, non-schedule risk** emerges: staff are performing more complex, multi-step services back-to-back with the same fixed 10-minute buffer between clients. The buffer size doesn't change with service complexity, so pacing may feel more compressed to staff even though the clock timing is identical — a genuine, if not strictly measurable, experience risk under Scenario C specifically.

**A control gap, not previously flagged anywhere in this repository:** nothing in the booking system or service documentation currently prevents a client from selecting a base service plus add-ons whose combined duration exceeds 45 minutes within a single AM slot. This needs a booking-system-level safeguard (validating combined duration at time of booking) — a configuration task, not a pricing or scheduling change, and not something this document resolves.

---

## 9. Room Utilisation Cross-Check

Against the committed day-one floor plan (`docs/floor-plan-concept.md`): 4 treatment rooms, 4 nail stations, 4 hairdressing chairs.

- **Peak utilisation:** the documented concurrency finding (verified for the 12-client model, and consistent with Table 1's identical headcount derivation methodology — `[MODELED — inferred from the same sweep-line/greedy-first-fit methodology, not independently re-quoted per-line for Table 1 in the source]`) is 2 concurrent clients per line (Massage, Beauty, Nails, Hair) at any given moment, against 4 physical stations per line.
- **Unused capacity:** roughly 50% of physical station capacity is unused at peak, even at the 18-client target — the binding constraint on throughput is staffing, not physical rooms/stations.
- **Bottleneck check:** no room-level bottleneck is evident from this analysis — the spare physical capacity is, if anything, a genuine asset during the AM/PM transition, since a room freed by the last AM client is immediately available for the first PM client without needing to wait for a specific room type to free up.
- **Room-type flexibility:** would still help — not because current capacity is insufficient, but because if treatment rooms remain labelled strictly "Massage" vs "Facial/Beauty" rather than generically fit-out for either (already flagged as unresolved in `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §15), the AM/PM handover could be needlessly constrained by room labelling rather than by real capacity.

---

## 10. Staffing Stress Test — Headcount vs. Timing/Deployment

**Verifying the premise directly:** `docs/CURRENT-STATE.md` §4 confirms treatment/phlebotomist headcount (8 + 2 = 10) is identical at both 12 and 18 clients/day, verified via two independent methods (sweep-line peak concurrency and greedy first-fit assignment) at each volume. **Confirmed, not re-derived here.**

**Is the issue headcount or timing/deployment? The evidence in this document points clearly to timing/deployment, not headcount:**
- Treatment and clinical headcount is proven sufficient at 18/day — §4 shows both groups winding down naturally well ahead of the last client's departure, with real idle windows (20 minutes for phlebotomists, the full final 15-20 minutes of the AM day for treatment staff).
- The one real staffing gap identified in this entire stress test is **not a headcount shortage in the clinical/treatment lines** — it's the single, shared reception/hospitality role (§3) being asked, under Option A specifically, to perform overlapping AM-closing and PM-opening functions simultaneously.
- **No headcount increase is indicated by this analysis.** The fix identified (§5's recommended Option B, or an equivalent deliberate transition window) is a scheduling decision, not a staffing decision — it resolves the reception conflict without adding a person.

---

## 11. PM Capacity Under Each Opening Time

Capacity only, no revenue calculation (none of PM's pricing supports a precise revenue figure here, per instruction) — treatment-hours available in a standard 12:00-18:00 or later PM window:

| PM opening | PM operating window | Treatment-hours theoretically available (4 dedicated PM lines × window length) |
|---|---|---|
| 12:00 | 6 hours (12:00-18:00) | ~24 staff-hours across the 4 PM lines |
| 12:30 | 5.5 hours (12:30-18:00) | ~22 staff-hours |
| 13:00 | 5 hours (13:00-18:00) | ~20 staff-hours |

PM's own duration range (30/45/60/90/120+ minutes, `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §7) means the actual number of *bookings* this supports varies by service mix — not calculated here, since no service-mix assumption for PM exists in this repository beyond the already-flagged, unvalidated "even split across 4 lines" planning assumption (`docs/pm-staffing-roster.md`). The capacity delta between 12:00 and 12:30 openings is real but modest (~2 staff-hours, roughly one 90-120 minute service's worth per line) — consistent with §5's finding that Option B's cost is genuinely small relative to its congestion benefit.

---

## 12. Customer Experience Stress Test

Answered directly against each transition option, not in generic terms:

- **Option A (12:00):** real risk of "rushed" and "processed" — a PM arrival at the exact moment two AM clients are mid-blood-draw and two more are still receiving treatment is the closest this model comes to visibly resembling "a clinic changing shift," which is precisely the outcome the founder flagged as something worth avoiding.
- **Option B (12:30):** the AM clients still present are in a quiet, already-finished state — nothing clinical is visibly in progress. A PM arrival at this point is much closer to "welcomed into a calm space that happens to have two other guests finishing up" than "walking into an operational handoff."
- **Option C (13:00):** cleanest in isolation — no AM presence at all — but an empty venue for half an hour doesn't obviously read as "designed around her" either; it simply removes the question rather than answering it, at a real capacity cost (§11).

**Overall:** the experience principle ("the experience is the product") is best served by Option B among the three tested, for the same reason it's the strongest operationally — it's the option where the founder's own worry (a visible shift-change) is least likely to actually occur, without giving up meaningful capacity to guarantee it.

---

## 13. Top 10 Failure Modes

| # | Failure mode | Trigger | Consequence | Severity | Mitigation | Requires added cost/staff? |
|---|---|---|---|---|---|---|
| 1 | Single reception role cannot handle simultaneous AM departure + PM arrival + active clinical procedure | Option A specifically, or any PM opening scheduled before AM treatment/clinical work has wound down | Congestion, rushed feeling at the front desk, the "clinic changing shift" outcome | Medium-High | Adopt Option B (or equivalent 30-min buffer) — a scheduling fix, not a staffing fix | No, if Option B is adopted. Yes, only if a second reception body is added instead. |
| 2 | A real-world delay (late arrival, difficult draw) cascades through that client's own remaining slots | Any day — the model has zero built-in slack, since the 10-min buffer serves both clinical timing and room turnover simultaneously | Knock-on delay to that pair's Draw 2/Service 2/Draw 3 | Medium-High | No slack currently exists to mitigate this for free; either accept the day-to-day risk or find budget for a genuine contingency buffer | Yes, if a buffer is added — not currently costed anywhere |
| 3 | Two staff need a break at the same real peak moment (e.g. 11:30) | Peak overlap of clinical + treatment demand | Nobody free to cover a gap | Low-Medium | Relief pool exists but isn't rostered by default | Yes, only if relief is actually pulled in |
| 4 | A service runs slightly over its 45-min slot | Client or staff extending past the scheduled close | Cascades into the next client's slot on that station | Medium | Staff training/on-time-close discipline | No |
| 5 | A blood draw takes longer than the zero-tolerance 5-minute mark allows | Harder vein access, anxious client — a real clinical variance not modelled by the solver | Delays that client's own subsequent Draw 2/3 marks, which are fixed at exact +60/+120min offsets | Medium-High | WDP protocol/phlebotomist judgment; already an implicit, disclosed risk of the move to zero-tolerance hard marks (`scenario-c-sync-timetables.md` §0.6) | No new cost identified, but no existing mitigation is documented either |
| 6 | Room-turnover/reset takes longer than the 10-minute built-in buffer | Higher-mess services, or a rushed prior client | Delays the next client's start on that station | Medium | Explicit reset-task ownership/process discipline — not currently modelled as a separate task or cost | No, if absorbed into existing staff process; yes if a dedicated reset role is added |
| 7 | PM demand spikes right at the AM/PM transition moment | Coincides with whichever PM opening option is chosen | Compounds failure mode #1 | Medium | Same as #1 | Same as #1 |
| 8 | A nail-service booking (or any service) exceeds 45 minutes without the booking system catching it | No documented combined-duration check exists at time of booking (§8) | Breaks the absolute 45-minute AM ceiling, cascades into the schedule | Low-Medium | Booking-system-level duration validation (a configuration task) | Minor — Fresha configuration effort, not new staff |
| 9 | Referral pipeline doesn't actually fill 18 slots/day in practice | A demand risk, not an operational one | The "friendly" failure — under-capacity is not itself dangerous, it just means this stress test's worst cases aren't being exercised yet | Low | None needed — inverts rather than threatens the stress test | No |
| 10 | Cumulative staff fatigue across a full week of zero-slack, back-to-back 25-minute-cadence days | Sustained 18-client days over time, not a single-day risk | Degraded service quality/staff turnover risk over weeks/months, not visible in any single day's schedule | High, if unaddressed | The AM/PM transition closure (§6) doubling as a genuine daily reset point; the relief pool for rostered days off | Yes — whatever the chosen closure duration costs in forgone PM capacity, already quantified in §11 |

---

## 14. What 18 Clients/Day Actually Requires

| Category | MUST HAVE | SHOULD HAVE | NICE TO HAVE | NOT REQUIRED |
|---|---|---|---|---|
| Rooms | 4 treatment rooms, 4 nail stations, 4 hair chairs, solid-wall Blood Collection Room (all already in the committed floor plan) | Generic (non-Massage/Beauty-labelled) treatment-room fit-out for AM/PM handover flexibility | A 5th treatment room/station buffer | A floor-plan redesign — current room counts already match peak concurrency (§9) |
| Staffing | 8 treatment staff + 2 phlebotomists (already confirmed sufficient at 18/day) | A documented plan for who covers reception during the AM/PM transition window | A dedicated transition-specific reception role | Any increase to treatment/phlebotomist headcount |
| Reception | A single, clearly-defined transition protocol (§5, §13 #1) | A sightline between reception and the Blood Collection Room | A second reception body during the transition window specifically | Two full-time, separately-staffed AM and PM reception roles |
| Hospitality | The welcome/itinerary card established in `docs/experience/CUSTOMER-JOURNEY.md` (the previously-referenced departure "leaving gesture" is REMOVED 2026-08-19, not approved) | A specific script/process for the AM/PM handover moment | — | — |
| Clinical workflow | The existing zero-tolerance draw-timing model (already verified) | An explicit contingency plan for real-world draw delays (§13 #5) | A small built-in schedule buffer beyond the current 10-min combined buffer | A redesign of the clinical timing model itself |
| Service scheduling | The 45-minute AM ceiling, enforced (§8) | A booking-system safeguard checking combined add-on duration against 45 minutes | — | Any AM service exceeding 45 minutes |
| PM transition | A decided opening time (this document recommends Option B, 12:30) | A short deliberate closure/handover window (§6, 30 min recommended) | A formal staff lunch break built into that window | A 45+ minute closure — not justified by this analysis |
| Customer flow | Nothing beyond the current open-plan Lounge design | Clarified reception sightlines (as above) | — | Physical separation of AM and PM guests — not shown to be necessary (§7) |
| Technology | Existing Fresha booking system | Combined-service-duration validation at booking (§8, §13 #8) | AM→PM client-linking data capture (already flagged in `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §8, §15) | — |
| SOPs | An explicit AM/PM handover protocol (currently undocumented) | A staff script for on-time service close (§13 #4) | A documented room-reset task assignment (§13 #6) | — |

---

## 15. Final Verdict

**1. Is the existing 18-client/day model operationally viable?** Yes, on the evidence in this document. The clinical schedule is solver-verified with zero collisions, treatment/clinical headcount is confirmed sufficient with real idle margin built in, and physical room/station capacity has real headroom (§9). Viability is not in question at the schedule level.

**2. What is the biggest operational bottleneck?** The single shared reception/hospitality role during the AM/PM transition window, specifically if PM opens before AM clinical/treatment activity has naturally wound down (Option A).

**3. Is the bottleneck space, staffing, scheduling, reception, or customer flow?** **Reception, and specifically its interaction with scheduling** — not space (§9 shows spare room capacity), not treatment/clinical headcount (§10 confirms it's already sufficient), and not customer flow in the open-plan sense (§7 finds AM/PM co-presence is not itself the problem).

**4. What PM opening time produces the strongest balance between premium experience, staff welfare, operational simplicity, and PM revenue capacity?** **12:30 (Option B)**, optionally formalised as a deliberate 30-minute transition window (12:00-12:30) that doubles as a staff break — this captures nearly all of Option C's calm, avoids nearly all of Option A's congestion, and costs only 30 minutes of PM capacity rather than 60.

**5. Does the existing 4 treatment / 4 nail / 4 hair configuration remain appropriate?** Yes — §9 shows it comfortably exceeds the peak concurrency the 18-client model actually generates, with room to spare. No change indicated by this analysis.

**6. What needs to be resolved before proceeding to detailed venue planning?** A founder decision on the PM opening time (this document recommends Option B); a decision on whether to formalise a deliberate transition/lunch window and its exact duration; a decision on whether treatment rooms should be fit out generically rather than labelled Massage vs. Beauty (carried over from `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §15); a booking-system-level safeguard for the 45-minute AM ceiling; and an explicit, documented AM/PM handover protocol, which does not yet exist in any form in this repository.
