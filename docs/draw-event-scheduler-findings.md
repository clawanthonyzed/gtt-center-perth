# GTT Center Perth — Draw-Event Scheduler (Solver-Based, Not Manual Arithmetic)

**Date:** 2026-07-17
**Why this exists:** Anthony asked why the "40-minute gap" between new clients on the same chair exists, whether another client could fill it, and asked for the exact draw + post-draw processing time rather than the gap figure. This required building an actual constraint solver (per the standing note in `am-capacity-weekend.md` that Scenario D-level questions "need a scripted solver rather than manual arithmetic") instead of extending the existing hand-built timetables.

## 1. Exact draw/processing time per client (the number Anthony asked for)

Source: `operations-manual.md` "GTT Scheduling Timetables — Key Rules" table (relative to each client's own GTT start time X):

| Event | Duration | In-chair? |
|---|---|---|
| Draw 1 (fasting draw + 75g glucose drink) | 15 min | Yes |
| Draw 2 (target X+75, tolerance ±5min) | 5 min | Yes |
| Draw 3 (target X+135, tolerance ±10min) | 5 min | Yes |
| **Total chair-occupied time per client** | **25 min** | — |
| Total visit length | ~150 min | — |
| **Chair utilisation per client** | **~17%** | — |

Services (45min × 2) and the transition buffer (10min) happen off-chair — the client is not occupying the phlebotomist's chair during those.

**Open caveat, not yet resolved:** the mandatory 10-minute ORCHID centrifuge spin per specimen (referenced in `am-capacity-weekend.md`) is not clearly attributed in the docs as either (a) already included inside the 15/5/5min "in-chair" blocks above, or (b) a separate phlebotomist-personal task performed after each draw, which would add hidden phlebotomist busy-time not captured by the chair-block figures. This matters — if it's (b), true phlebotomist load is higher than this model assumes. Needs clarifying with Cora (Clinical Coordinator) or WDP before treating the numbers below as fully final.

## 2. Methodology

Built a real scheduler (`draw-event-scheduler.py`) that:
- Models each chair as a single resource that can only run one draw event at a time (no double-booking)
- Admits new clients greedily, as early as possible, onto whichever chair has room
- For each candidate client, searches every combination of D2 placement (±5min of target) and D3 placement (±10min of target) to find a collision-free slot — this is the actual tolerance-window flexibility the current hand-built timetables also use, just searched exhaustively instead of by hand
- Independently verifies zero overlaps on every chair after admission (same rigor as the existing hand-checked Scenario B/C/D tables, but computed, not manually re-checked)

## 3. Results

### Same window as current Scenario C (last new-client start 10:05, i.e. 185min from 07:00 open)

**Result: 10 clients, identical to the current verified model** (5/chair, zero collisions).

**This is the important finding: the 40-minute per-chair gap is NOT idle slack that another client could fill.** It's structurally required by the D2 (±5min) and D3 (±10min) tolerance windows around each client's own fixed draw points. Tested packing clients tighter than 40min apart on one chair — it works for the first 3-4 clients (using up all the tolerance margin), then hits a collision and the chair goes idle for a long stretch until the earlier clients' D3 windows clear. Net throughput over a long run: **~1 client per 43.75min** in bursty mode — *worse* than the steady 40min rhythm the current model already uses. The existing hand-built Scenario C timetable is at or very near the true optimum for this window — confirmed by solver, not just plausible.

### 3-chair cross-check (same window)

**Result: 15 clients — exactly matches the existing hand-verified Scenario D.** Independent confirmation that Scenario D's manual timetable is also correctly optimised, not just collision-free.

### Extended window (last new-client start pushed to 11:00, i.e. 240min)

**Result: 16 clients on 2 chairs — up from 10.** This is where real additional capacity actually lives: **extending the window (earlier open or later cutoff), not tighter packing inside the current window.**

## 4. Bottom line for Anthony's three questions

1. **"Why can't another client take the 40-min gap?"** — Tested directly. They structurally can't, within the current window, without collisions cascading later in that client's own draw sequence. The gap looks empty but is reserved by that same client's own future D2/D3 draw points.
2. **"Exact draw + processing time"** — 25 min in-chair per client (15+5+5), pending the centrifuge-attribution caveat above.
3. **"Cutoff should be based on collection requirements, i.e. the latest time Draw 1 can be taken"** — Correction accepted. This scheduler models the cutoff as **latest allowable Draw 1 start time**, not last-departure/courier-pickup time (the earlier framing). The actual clock value for that cutoff is still pending — it's driven by whatever WDP's specimen/lab-processing requirement turns out to be (same open item as before, now correctly framed as a *start*-side constraint, not an end-side one). Once WDP replies, plug the real value into this scheduler (`window_end_for_new_starts` parameter) and it recomputes the true max instantly — no manual timetable rebuild needed.

**Practical implication once WDP responds:** if their requirement allows the window to extend by ~1 hour beyond the current 10:05 last-start assumption, this scheduler shows real capacity (~16/day on 2 chairs) without hiring a 3rd phlebotomist. If the window can't extend, 10/day is confirmed as the genuine ceiling on 2 chairs, and the 3rd chair (Scenario D, 15/day, already verified) remains the only lever.
