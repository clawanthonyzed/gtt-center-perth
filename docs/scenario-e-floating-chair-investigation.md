# GTT Center Perth — Scenario E: Floating-Chair Investigation

**Version:** 1.0 | **Date:** 2026-07-20
**Status:** EXPLORATORY ANALYSIS ONLY — NOT a committed operational model change. This document answers a specific question with real scheduling analysis; it does not recommend adopting the floating-chair model, because the analysis shows no benefit to doing so (see verdict below).

---

## The Question

Anthony asked: *"Is there a way to fit more clients in if the client doesn't have to go back to the same chair?"* — i.e., in the current Scenario C/D model, each client's full visit (Draw 1 → Service 1 → Draw 2 → Service 2 → Draw 3) is pinned to a single chair (Chair A, B, or C) for the whole visit. Would decoupling this — letting a client return to *whichever chair is free* for Draw 2 and Draw 3, not necessarily their original Draw 1 chair — increase daily capacity beyond the current verified 10-client (Scenario C) or 15-client (Scenario D) ceilings?

---

## Method — Built and Ran an Actual Solver, Not a Theoretical Argument

Per the standing project convention (`draw-event-scheduler-findings.md`: "this required building an actual constraint solver... instead of extending the existing hand-built timetables"), this question was answered by building a second scheduler variant, not by reasoning about it in the abstract.

**Existing model (`tools/draw-event-scheduler.py`, verified 2026-07-17):** treats each chair as an independent resource; a client's Draw 1, Draw 2, and Draw 3 are all placed on the *same* chair once that chair is chosen at Draw 1. This is the "pinned" model — it already matches the current operational Scenario C/D design (Chair A/B/C, one phlebotomist per chair, client returns to the same chair each time).

**New model (built for this investigation, `floating_chair_scheduler.py`):** identical task durations and tolerance windows (Draw 1 = 15 min fixed at the client's start time X; Draw 2 = 5 min, movable within X+70 to X+80; Draw 3 = 5 min, movable within X+125 to X+145 — sourced from `operations-manual.md`'s "Key Rules" table, same as the existing scheduler). The only change: **each of the three draws for a given client is independently allowed to land on any chair with a free slot at that time** — a client's Draw 2 or Draw 3 does not need to be on the same chair as their Draw 1.

Both models were run under identical conditions for a direct, apples-to-apples comparison:
- 2 chairs, current committed window (last new-client start 10:05, matching Scenario C)
- 2 chairs, an extended window (last new-client start 11:00, for reference against the existing "what if the window extends" analysis in `draw-event-scheduler-findings.md`)
- 3 chairs, current window (matching Scenario D)
- 3 chairs, extended window

---

## Results

| Configuration | Pinned-chair (existing model) | Floating-chair (this investigation) | Difference |
|---|---|---|---|
| 2 chairs, current window (last start 10:05) | 10 clients | 10 clients | **0** |
| 2 chairs, extended window (last start 11:00) | 16 clients | 16 clients | **0** |
| 3 chairs, current window (last start 10:05) | 15 clients | 15 clients | **0** |
| 3 chairs, extended window (last start 11:00) | 24 clients | 24 clients | **0** |

**Verdict: no capacity gain from decoupling clients from a fixed chair, in any tested configuration.** Both models were also verified independently (a post-hoc pass confirming zero collisions on every chair), and a stress test at finer time granularity (checking every 1 minute instead of every 5) produced identical results — ruling out a step-size artifact.

**A further, telling detail:** in every single test run, the floating-chair solver's own greedy algorithm — which was completely free to place any client's Draw 2 or Draw 3 on a different chair whenever that was advantageous — never actually chose to do so. Zero clients, across all four configurations, ended up using more than one physical chair for their visit, even though the solver had no rule preventing it. This is not a coincidence; it reflects the underlying reason floating doesn't help (see below).

---

## Why Floating Doesn't Help — The Actual Reason

The binding constraint on capacity is **the total number of draw-events (Draw 1 + Draw 2 + Draw 3 for every client) that can be packed into the available chair-minutes across the whole window**, not which specific chair each individual draw happens to land on. Chairs in this model are functionally identical to each other (same phlebotomist skillset, same draw durations, same tolerance rules) — there is no chair that's "faster" or has spare capacity the others don't. When the existing pinned scheduler load-balances new clients across chairs (assigning each new arrival to whichever chair currently has the fewest bookings), it already achieves the same effect that letting individual draws float would achieve: even utilisation across all chairs, no chair sitting idle while another is overloaded.

In short: **the pinning constraint was never actually the thing limiting capacity.** The real limit is the fixed relationship between each client's own Draw 2 (±5min of X+75) and Draw 3 (±10min of X+135) tolerance windows and the total width of the operating window — exactly the finding already established in `draw-event-scheduler-findings.md` for the pinned model. Floating removes a constraint that wasn't binding, so removing it changes nothing.

---

## What WOULD Increase Capacity (Cross-Reference, Not Repeated Here)

Per the existing, already-verified findings in `draw-event-scheduler-findings.md` (not re-derived in this document):
- **Extending the operating window** (earlier open, later last-start cutoff) is the only lever shown to add real capacity within a fixed chair count — e.g., 10 → 16 clients on 2 chairs if the window extends by ~1 hour, once WDP confirms whether the courier/specimen constraint allows it.
- **Adding a 3rd chair** (Scenario D, already verified) adds capacity in the current window — 10 → 15 clients.
- **Tighter packing within the current window** was already tested and shown to make throughput *worse*, not better (bursty admission then long idle stretches) — this applies equally to the floating-chair model, since the binding constraint (draw-event tolerance windows) is identical in both.

---

## New Constraints the Floating-Chair Model Would Introduce (If It Did Help — Documented for Completeness)

Even though the analysis shows zero capacity benefit, Anthony's question also asked what new constraints floating would introduce if it *did* help — worth documenting since a future session may revisit this:

- **Phlebotomist coordination complexity:** under the pinned model, each phlebotomist owns their chair's full client list and can plan their own draw sequence independently. Under a floating model, a phlebotomist could be handed a Draw 2 or Draw 3 for a client they haven't met before (a different phlebotomist did that client's Draw 1) — this requires a shared, real-time coordination system (whiteboard or booking-software view) so any phlebotomist knows exactly which client is due next on their chair, including clients they didn't originally admit. The current model's whiteboard/Fresha tracking (`operations-manual.md`) is built around each chair's own client list — this would need redesigning.
- **Client confusion / experience risk:** a pregnant, fasting client returning for her second or third blood draw and being directed to a different phlebotomist/chair than her first draw is a small but real experience discontinuity — the current model's "Phlebotomist A/B introduces themselves once and sees the same client through their whole visit" continuity would be lost. Not modelled here as a hard blocker, but a genuine soft cost with no offsetting capacity benefit to justify it.
- **Chair-cleaning/turnover between different clients:** the current pinned model doesn't need a between-client wipe-down check built into the schedule, since only one client occupies a chair between draws is a different question already handled by service timing — but a floating model would need explicit confirmation that a chair vacated by Client A's Draw 2 is cleaned/reset before Client B's Draw 1 lands on it a few minutes later, adding an operational step not currently modelled.
- **Specimen/labelling handoff risk:** if a phlebotomist who didn't perform Client X's Draw 1 performs their Draw 2 or Draw 3, they need Client X's full history (fasting confirmation, prior draw times, any adverse-event flags) handed off cleanly — a real clinical-safety consideration, not just a scheduling one, and outside the scope of what this scheduling-only analysis can validate.

**None of this needs to be resolved, since the model shows no capacity benefit to justify introducing these new constraints in the first place.**

---

## Bottom Line

**Decoupling clients from a fixed chair does not increase daily capacity in this model, under any tested configuration.** The current pinned-chair Scenario C (10 clients/2 chairs) and Scenario D (15 clients/3 chairs) are already at the true optimum for their respective chair counts and operating window — confirmed by solver, independently of the pinning question. The only capacity levers that do work are extending the operating window (pending the WDP cutoff-time confirmation) or adding chairs (Scenario D, already verified). This document is not a recommendation to change the operational model — it answers the specific question asked and finds no basis for a change.

---

## Sourcing / Reproducibility

- Task durations and tolerance windows: `operations-manual.md` "GTT Scheduling Timetables — Key Rules" table
- Existing pinned-chair scheduler: `tools/draw-event-scheduler.py` (2026-07-17)
- New floating-chair scheduler built for this investigation: reproduces the same task-duration constants, with chair-assignment decoupled per-draw rather than per-client. Not committed as a permanent tool script in this repo (this was a one-off investigation, not an ongoing scheduling tool) — the logic and full results are documented above; the underlying analysis can be rebuilt from this document's method description if needed again.

---

## Changelog

**2026-07-20** — Created in response to Anthony's direct question about floating/decoupled chair assignment. Built and ran an actual scheduler variant (not theoretical reasoning) to test the question against 4 configurations (2/3 chairs × current/extended window), verified with an independent collision check and a finer-granularity stress test. Result: zero capacity gain in every configuration — logged as exploratory analysis only, explicitly not a recommended operational change.

---

## Addendum — One Additional (11th) Client at a 09:55 Start (2026-07-20)

**Anthony's clarified question:** not "can 2 extra clients fit" (already answered no, above/in `business-plan.md`) — specifically, can exactly **one** additional (11th) client be squeezed onto the existing 10-client Scenario C schedule using a 09:55 start slot on one of the 2 chairs?

**Method:** built a direct collision check (not manual eyeballing) against the real, already-scheduled Scenario C timetable (`scenario-c-sync-timetables.md`) — testing whether an 11th client's full draw sequence (Draw 1 at 09:55, Draw 2 at target+tolerance, Draw 3 at target+tolerance) can be placed on Chair A without colliding with Client 9 (the chair's last currently-scheduled client, Draw 1 at 09:40).

**Verdict: No — a genuine 11th client cannot start at 09:55.**

**The specific constraint that blocks it:** Client 9's Draw 1 occupies the chair from 09:40 to 09:55 exactly — there is zero gap before an 11th client's own Draw 1 could begin. Testing every possible placement of the 11th client's Draw 2/Draw 3 within their tolerance windows (±5min/±10min) against Client 9's actual scheduled draws (not just Client 9's outer tolerance bounds) confirms there is no collision-free assignment starting at 09:55 — the chair is occupied at that exact moment, and shifting the 11th client's later draws doesn't fix a Draw-1-vs-Draw-1 conflict at the start.

**Sweep of nearby times (same chair, checked in 5-minute increments):** the next genuinely free start time after 09:40 is **10:00**, not 09:55 — a 20-minute gap, not 15. 09:45, 09:50, 09:55, and 10:05-10:15 all remain blocked; 10:00, 10:20, 10:40, 11:00 are the pattern of genuinely free slots (each exactly 20 minutes apart, half the normal 40-minute new-client rhythm — this is a real but much smaller residual gap than a full new-client slot, not usable for a full 11th client without also moving the last-draw completion time later, see below).

**What a 10:00-start 11th client would actually require:** Draw 1 10:00-10:15, Draw 2 ~11:15-11:20, Draw 3 ~12:15-12:20, departing ~12:30 — twenty minutes later than the current last client's ~12:10 departure. This pushes the last specimen dispatch ~20 minutes later than today's model, which is exactly the kind of window-extension question already flagged as pending WDP's specimen-cutoff confirmation (`draw-event-scheduler-findings.md`, `cutoff-time-CORRECTION.md`) — not something achievable within the current committed 10:05-last-start assumption without that confirmation.

**Bottom line:** 09:55 specifically does not work for an 11th client — the chair is occupied by Client 9's Draw 1 at that exact minute. 10:00 is the next genuinely free start, but using it depends on the same still-unconfirmed WDP window-extension question already tracked elsewhere in this corpus, not a new, independent finding. This is consistent with (not contradicted by) last round's answer that "10/day is the ceiling within the current window" — the ceiling holds for the current window; only extending the window (whether by 15, 20, or 60 minutes) moves it, and that lever was already known and already pending WDP.

**2026-07-20 (11th-client addendum)** — Anthony clarified the ask was for exactly one extra client, not two — re-checked with a direct collision test against the real scheduled Scenario C timetable rather than relying on the prior 2-client answer. Confirmed 09:55 specifically is blocked (Client 9's Draw 1 occupies the chair at that exact time); the next genuinely free slot is 10:00, which depends on the same pending WDP window-extension question as the rest of this corpus, not a new independent capacity source.
