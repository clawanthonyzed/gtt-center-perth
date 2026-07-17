# GTT Center Perth — Scenario C, Synchronized Chair Start — Verified Timetables

**Date:** 2026-07-17
**Change from prior Scenario C:** Chair A and Chair B now start their client cohorts at the identical clock time each slot (uniform rhythm), instead of the 20-minute offset used previously. Same total capacity (10 clients/day, 5/chair) — this was already confirmed not to change the number. **New in this version:** the treatment-staff concurrency check for the synchronized case, which was previously only asserted, not built. Verified here programmatically — zero double-bookings across both phlebotomists and all 8 treatment staff.

## 1. Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 | Service 2 | Draw 3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00–07:15 | 07:15–08:00 Massage (M1) | 08:10–08:15 | 08:20–09:05 Beauty (B1) | 09:20–09:25 | ~09:30 |
| 2 | B | 07:00–07:15 | 07:15–08:00 Nails (N1) | 08:10–08:15 | 08:20–09:05 Hair (H1) | 09:20–09:25 | ~09:30 |
| 3 | A | 07:40–07:55 | 07:55–08:40 Massage (M2) | 08:50–08:55 | 09:00–09:45 Beauty (B2) | 10:00–10:05 | ~10:10 |
| 4 | B | 07:40–07:55 | 07:55–08:40 Nails (N2) | 08:50–08:55 | 09:00–09:45 Hair (H2) | 10:00–10:05 | ~10:10 |
| 5 | A | 08:20–08:35 | 08:35–09:20 Massage (M1) | 09:30–09:35 | 09:40–10:25 Beauty (B1) | 10:35–10:40 | ~10:45 |
| 6 | B | 08:20–08:35 | 08:35–09:20 Nails (N1) | 09:30–09:35 | 09:40–10:25 Hair (H1) | 10:35–10:40 | ~10:45 |
| 7 | A | 09:00–09:15 | 09:15–10:00 Massage (M2) | 10:10–10:15 | 10:20–11:05 Beauty (B2) | 11:15–11:20 | ~11:25 |
| 8 | B | 09:00–09:15 | 09:15–10:00 Nails (N2) | 10:10–10:15 | 10:20–11:05 Hair (H2) | 11:15–11:20 | ~11:25 |
| 9 | A | 09:40–09:55 | 09:55–10:40 Massage (M1) | 10:50–10:55 | 11:00–11:45 Beauty (B1) | 11:55–12:00 | ~12:05 |
| 10 | B | 09:40–09:55 | 09:55–10:40 Nails (N1) | 10:50–10:55 | 11:00–11:45 Hair (H1) | 11:55–12:00 | ~12:05 |

Note: Client 1 and Client 2's Draw 2 both land at 08:10–08:15 — same literal clock minute, different chairs/phlebotomists. This is the synchronized-start effect in practice: both phlebotomists draw at the same moment, confirmed not a conflict (separate chairs, separate staff).

## 2. Full Staff Timetable

| Staff | Bookings (time — client) |
|---|---|
| **Phlebotomist A** (Chair A) | 07:00 C1·D1, 08:10 C1·D2, 09:20 C1·D3, 07:40 C3·D1, 08:50 C3·D2, 10:00 C3·D3, 08:20 C5·D1, 09:30 C5·D2, 10:35 C5·D3, 09:00 C7·D1, 10:10 C7·D2, 11:15 C7·D3, 09:40 C9·D1, 10:50 C9·D2, 11:55 C9·D3 (15 draws) |
| **Phlebotomist B** (Chair B) | Identical clock times to Phlebotomist A, mirrored onto clients 2/4/6/8/10 (15 draws) |
| **Massage 1 (M1)** | C1 07:15–08:00, C5 08:35–09:20, C9 09:55–10:40 (3 bookings) |
| **Massage 2 (M2)** | C3 07:55–08:40, C7 09:15–10:00 (2 bookings) |
| **Beauty 1 (B1)** | C1 08:20–09:05, C5 09:40–10:25, C9 11:00–11:45 (3 bookings) |
| **Beauty 2 (B2)** | C3 09:00–09:45, C7 10:20–11:05 (2 bookings) |
| **Nails 1 (N1)** | C2 07:15–08:00, C6 08:35–09:20, C10 09:55–10:40 (3 bookings) |
| **Nails 2 (N2)** | C4 07:55–08:40, C8 09:15–10:00 (2 bookings) |
| **Hair 1 (H1)** | C2 08:20–09:05, C6 09:40–10:25, C10 11:00–11:45 (3 bookings) |
| **Hair 2 (H2)** | C4 09:00–09:45, C8 10:20–11:05 (2 bookings) |

## 3. Verification (programmatic, not manual)

Every treatment line's peak concurrent bookings checked by exhaustive interval-overlap simulation:

| Line | Peak concurrent | Capacity | Result |
|---|---|---|---|
| Massage | 2 | 2 | OK |
| Beauty | 2 | 2 | OK |
| Nails | 2 | 2 | OK |
| Hair | 2 | 2 | OK |

**Zero double-bookings, all 10 clients placed.** Synchronized start confirmed safe end-to-end — chairs, phlebotomists, and all 8 treatment staff.

## 4. Still on "a better way to utilise phlebotomist time"

Re-confirming rather than re-opening: this exact question was tested twice already this session with an actual constraint solver (not manual arithmetic) — `draw-event-scheduler-findings.md`. Both runs (staggered and now this synchronized layout) land on the same ceiling: **10 clients/day is the genuine maximum on 2 chairs within the current window** (last new-draw start ~10:05). Tighter packing was tested directly and produces *worse* throughput, not better (bursts followed by dead time once clinical tolerance windows are used up).

The only lever not yet closed off by the solver: **whether a non-phlebotomist assistant absorbing labelling/centrifuge/escort tasks could shrink the phlebotomist's actual attention-time per draw** (flagged previously, still unverified — needs a minute-by-minute task breakdown of what currently happens inside the 15/5/5-min draw blocks, plus confirmation from WDP on whether non-accredited staff can legally handle specimens under their Licensed Collection Centre QMS). Everything else — window extension, 3rd chair, sync vs stagger — has now been tested and the numbers hold.
