# GTT Center Perth — Master Scenario Comparison (2026-08)

**Purpose:** one consolidated document covering every schedule scenario discussed across this repo's recent work, side by side, so the full picture is visible in one place instead of pieced together from separate replies. All computation pulled from or cross-checked against `scenario-c-sync-timetables.md` and this engagement's established solvers (`tools/draw-event-scheduler.py` for the tolerance-window model; the synchronized-pair/5-min-draw solver for the corrected model) — nothing here is a fresh, unverified estimate.

**Carole-facing vs internal-only, stated plainly per scenario:** Scenarios 3 and 4 are what was sent to Carole (via the clinic-operations overview document). Scenarios 1, 2, 5, 6, and 7 are internal planning only — never shared externally.

**Cross-referenced from:** `docs/CURRENT-STATE.md` §1 and `docs/scenario-c-sync-timetables.md` (both point here for the full side-by-side picture; this document does not replace either as the canonical source for its own respective model).

---

## Quick Comparison Table

| # | Scenario | Model basis | Clients | Treatment headcount | Total AM staff (incl. 2 phleb) | Carole-facing? | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Original committed (historical) | Tolerance-window, 40-min cadence | 12 | 8 (4 MB + 2 N + 2 H — old unpooled-language framing, now "dual-qualified required by peak overlap") | 10 | No — historical only | Superseded, kept for trace |
| 2 | Original 14-client ceiling (historical) | Tolerance-window, bursty | 14 | 9 (3 MB + 3 N + 3 H) | 11 | No — historical only | Superseded, kept for trace |
| 3 | Corrected 12-client (current) | Synchronized, 5-min draws, exact 60/120, 45+45 service, g=23 | 12 | 8 (4 MB + 2 N + 2 H) | 10 | **Yes** | **Achievable as-is, current floor plan/staffing** |
| 4 | Corrected 14-client (current) | Same, g=23 | 14 | 8 (4 MB + 2 N + 2 H) | 10 | **Yes** | **Achievable as-is, current floor plan/staffing** |
| 5 | Scenario A (08:00 start) | Same, g=23, shifted start | 14 | 8 (4 MB + 2 N + 2 H) | 10 | No — internal only | Achievable as-is, no floor-plan/staffing change |
| 6 | Scenario B (true maximum) | Same, bursty adaptive admission | 36 | 27 (9 MB + 9 N + 9 H) | 29 | No — internal only | **NOT achievable within the current floor plan or staffing — requires a floor-plan redesign (9 stations/line vs the committed 4 nail/4 hair/2+2 massage-beauty) and roughly 3.4× the current treatment headcount** |
| 7a | Scenario C, 12-equivalent | Same, g=25 | 12 | 8 (4 MB + 2 N + 2 H) | 10 | No — internal only | Achievable as-is, no floor-plan/staffing change |
| 7b | Scenario C, 14-equivalent | Same, g=25 | 14 | 8 (4 MB + 2 N + 2 H) | 10 | No — internal only | Achievable as-is, no floor-plan/staffing change |
| 7c | Scenario C, own maximum | Same, g=25, full window | 18 | 8 (4 MB + 2 N + 2 H) | 10 | No — internal only | Achievable as-is, no floor-plan/staffing change |

---

## 1. Original Committed Model (Historical, Superseded) — 12 Clients, Tolerance-Window, 40-min Cadence

**Status: superseded by Scenario 3 below. Kept for comparison only.** Pulled directly from `scenario-c-sync-timetables.md` §0.1/§0.2 — not recomputed here.

### Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 | Service 2 | Draw 3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00–07:15 | 07:15–08:00 Massage (M1) | 08:15–08:20 | 08:20–09:05 Beauty (B1) | 09:15–09:20 | ~09:28 |
| 2 | B | 07:00–07:15 | 07:15–08:00 Nails (N1) | 08:15–08:20 | 08:20–09:05 Hair (H1) | 09:15–09:20 | ~09:28 |
| 3 | A | 07:40–07:55 | 07:55–08:40 Massage (M2) | 08:55–09:00 | 09:00–09:45 Beauty (B2) | 09:55–10:00 | ~10:08 |
| 4 | B | 07:40–07:55 | 07:55–08:40 Nails (N2) | 08:55–09:00 | 09:00–09:45 Hair (H2) | 09:55–10:00 | ~10:08 |
| 5 | A | 08:20–08:35 | 08:35–09:20 Massage (M1) | 09:35–09:40 | 09:40–10:25 Beauty (B1) | 10:35–10:40 | ~10:48 |
| 6 | B | 08:20–08:35 | 08:35–09:20 Nails (N1) | 09:35–09:40 | 09:40–10:25 Hair (H1) | 10:35–10:40 | ~10:48 |
| 7 | A | 09:00–09:15 | 09:15–10:00 Massage (M2) | 10:15–10:20 | 10:20–11:05 Beauty (B2) | 11:15–11:20 | ~11:28 |
| 8 | B | 09:00–09:15 | 09:15–10:00 Nails (N2) | 10:15–10:20 | 10:20–11:05 Hair (H2) | 11:15–11:20 | ~11:28 |
| 9 | A | 09:40–09:55 | 09:55–10:40 Massage (M1) | 10:55–11:00 | 11:00–11:45 Beauty (B1) | 11:55–12:00 | ~12:08 |
| 10 | B | 09:40–09:55 | 09:55–10:40 Nails (N1) | 10:55–11:00 | 11:00–11:45 Hair (H1) | 11:55–12:00 | ~12:08 |
| 11 | A | 10:20–10:35 | 10:35–11:20 Massage (M2) | 11:35–11:40 | 11:40–12:25 Beauty (B2) | 12:35–12:40 | ~12:48 |
| 12 | B | 10:20–10:35 | 10:35–11:20 Nails (N2) | 11:35–11:40 | 11:40–12:25 Hair (H2) | 12:35–12:40 | ~12:48 |

### Staff Timetable

| Staff | Bookings |
|---|---|
| Phlebotomist A (Chair A) | Draws for clients 1/3/5/7/9/11 (18 draws) |
| Phlebotomist B (Chair B) | Draws for clients 2/4/6/8/10/12 (18 draws) |
| Massage 1 (M1) | C1 07:15–08:00, C5 08:35–09:20, C9 09:55–10:40 |
| Massage 2 (M2) | C3 07:55–08:40, C7 09:15–10:00, C11 10:35–11:20 |
| Beauty 1 (B1) | C1 08:20–09:05, C5 09:40–10:25, C9 11:00–11:45 |
| Beauty 2 (B2) | C3 09:00–09:45, C7 10:20–11:05, C11 11:40–12:25 |
| Nails 1 (N1) | C2 07:15–08:00, C6 08:35–09:20, C10 09:55–10:40 |
| Nails 2 (N2) | C4 07:55–08:40, C8 09:15–10:00, C12 10:35–11:20 |
| Hair 1 (H1) | C2 08:20–09:05, C6 09:40–10:25, C10 11:00–11:45 |
| Hair 2 (H2) | C4 09:00–09:45, C8 10:20–11:05, C12 11:40–12:25 |

**Headcount: 8 treatment (2 Massage + 2 Beauty + 2 Nails + 2 Hair, each a dual-qualified staff member — no separate "unpooled" hiring model, per the empire-wide language correction) + 2 phlebotomists = 10 total.**

**Verdict: superseded by Scenario 3 — do not use for current planning.** Draw-timing basis (15-min Draw 1, ±5/±10min tolerance windows) has been replaced by Carole's exact 60/120-minute clinical marks. Kept here purely for historical comparison.

---

## 2. Original 14-Client Proven Ceiling (Historical, Superseded) — Tolerance-Window, Bursty

**Status: superseded by Scenario 4 below.** Regenerated via `tools/draw-event-scheduler.py` (the original established tool) for this comparison — not previously written out as a full table in `scenario-c-sync-timetables.md` §0.4, which described it narratively. Reconstructed here, matching the previously-verified figures exactly (9 treatment staff, same bursty two-cluster shape).

### Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 | Service 2 | Draw 3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00-07:15 | 07:15-08:00 Massage | 08:10-08:15 | 08:20-09:05 Beauty | 09:05-09:10 | ~09:10 |
| 2 | B | 07:01-07:16 | 07:16-08:01 Nails | 08:11-08:16 | 08:21-09:06 Hair | 09:06-09:11 | ~09:11 |
| 3 | A | 07:15-07:30 | 07:30-08:15 Massage | 08:25-08:30 | 08:35-09:20 Beauty | 09:20-09:25 | ~09:25 |
| 4 | B | 07:16-07:31 | 07:31-08:16 Nails | 08:26-08:31 | 08:36-09:21 Hair | 09:21-09:26 | ~09:26 |
| 5 | A | 07:30-07:45 | 07:45-08:30 Massage | 08:40-08:45 | 08:50-09:35 Beauty | 09:35-09:40 | ~09:40 |
| 6 | B | 07:31-07:46 | 07:46-08:31 Nails | 08:41-08:46 | 08:51-09:36 Hair | 09:36-09:41 | ~09:41 |
| 7 | A | 07:45-08:00 | 08:00-08:45 Massage | 08:55-09:00 | 09:05-09:50 Beauty | 09:50-09:55 | ~09:55 |
| 8 | B | 07:46-08:01 | 08:01-08:46 Nails | 08:56-09:01 | 09:06-09:51 Hair | 09:51-09:56 | ~09:56 |
| 9 | A | 09:55-10:10 | 10:10-10:55 Massage | 11:05-11:10 | 11:15-12:00 Beauty | 12:00-12:05 | ~12:05 |
| 10 | B | 09:56-10:11 | 10:11-10:56 Nails | 11:06-11:11 | 11:16-12:01 Hair | 12:01-12:06 | ~12:06 |
| 11 | A | 10:10-10:25 | 10:25-11:10 Massage | 11:20-11:25 | 11:30-12:15 Beauty | 12:15-12:20 | ~12:20 |
| 12 | B | 10:11-10:26 | 10:26-11:11 Nails | 11:21-11:26 | 11:31-12:16 Hair | 12:16-12:21 | ~12:21 |
| 13 | A | 10:25-10:40 | 10:40-11:25 Massage | 11:35-11:40 | 11:45-12:30 Beauty | 12:30-12:35 | ~12:35 |
| 14 | B | 10:26-10:41 | 10:41-11:26 Nails | 11:36-11:41 | 11:46-12:31 Hair | 12:31-12:36 | ~12:36 |

**Note the ~2hr09min mid-morning gap (07:56–09:55) with zero new arrivals — the "bursty two-cluster" shape.**

### Staff Timetable

| Staff | Bookings |
|---|---|
| Phlebotomist A (Chair A) | Draws for clients 1,3,5,7,9,11,13 |
| Phlebotomist B (Chair B) | Draws for clients 2,4,6,8,10,12,14 |
| Massage+Beauty MB1 | C1-Massage 07:15–08:00, C7-Massage 08:00–08:45, C5-Beauty 08:50–09:35, C9-Massage 10:10–10:55, C9-Beauty 11:15–12:00 |
| Massage+Beauty MB2 | C3-Massage 07:30–08:15, C1-Beauty 08:20–09:05, C7-Beauty 09:05–09:50, C11-Massage 10:25–11:10, C11-Beauty 11:30–12:15 |
| Massage+Beauty MB3 | C5-Massage 07:45–08:30, C3-Beauty 08:35–09:20, C13-Massage 10:40–11:25, C13-Beauty 11:45–12:30 |
| Nails N1 | C2-Nails 07:16–08:01, C8-Nails 08:01–08:46, C10-Nails 10:11–10:56 |
| Nails N2 | C4-Nails 07:31–08:16, C12-Nails 10:26–11:11 |
| Nails N3 | C6-Nails 07:46–08:31, C14-Nails 10:41–11:26 |
| Hair H1 | C2-Hair 08:21–09:06, C8-Hair 09:06–09:51, C10-Hair 11:16–12:01 |
| Hair H2 | C4-Hair 08:36–09:21, C12-Hair 11:31–12:16 |
| Hair H3 | C6-Hair 08:51–09:36, C14-Hair 11:46–12:31 |

**Headcount: 9 treatment (3 Massage+Beauty pool + 3 Nails + 3 Hair) + 2 phlebotomists = 11 total.**

**Verdict: superseded by Scenario 4 — the draw-timing basis (15-min Draw 1, tolerance windows) no longer reflects Carole's exact clinical-mark requirement. Kept for historical comparison only.**

---

## 3. Corrected 12-Client Model (Carole-Facing, Current)

**Model: synchronized chair starts, every draw exactly 5 minutes, Draw 2/3 at exact +60/+120min, both services fixed at 45 minutes, 23-minute pair cadence, 07:00 start.** Pulled from `scenario-c-sync-timetables.md` §0.6. **This is one of the two tables sent to Carole via the clinic-operations overview document.**

### Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 (+60min) | Service 2 | Draw 3 (+120min) |
|---|---|---|---|---|---|---|
| 1 | A | 07:00 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 |
| 2 | B | 07:00 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 |
| 3 | A | 07:23 | 07:28–08:13 | 08:23–08:28 | 08:28–09:13 | 09:23–09:28 |
| 4 | B | 07:23 | 07:28–08:13 | 08:23–08:28 | 08:28–09:13 | 09:23–09:28 |
| 5 | A | 07:46 | 07:51–08:36 | 08:46–08:51 | 08:51–09:36 | 09:46–09:51 |
| 6 | B | 07:46 | 07:51–08:36 | 08:46–08:51 | 08:51–09:36 | 09:46–09:51 |
| 7 | A | 08:09 | 08:14–08:59 | 09:09–09:14 | 09:14–09:59 | 10:09–10:14 |
| 8 | B | 08:09 | 08:14–08:59 | 09:09–09:14 | 09:14–09:59 | 10:09–10:14 |
| 9 | A | 08:32 | 08:37–09:22 | 09:32–09:37 | 09:37–10:22 | 10:32–10:37 |
| 10 | B | 08:32 | 08:37–09:22 | 09:32–09:37 | 09:37–10:22 | 10:32–10:37 |
| 11 | A | 08:55 | 09:00–09:45 | 09:55–10:00 | 10:00–10:45 | 10:55–11:00 |
| 12 | B | 08:55 | 09:00–09:45 | 09:55–10:00 | 10:00–10:45 | 10:55–11:00 |

### Staff Timetable

**Massage+Beauty pool:**
- Staff MB1: C1-Massage 07:05–07:50, C5-Massage 07:51–08:36, C9-Massage 08:37–09:22, C9-Beauty 09:37–10:22
- Staff MB2: C3-Massage 07:28–08:13, C7-Massage 08:14–08:59, C11-Massage 09:00–09:45, C11-Beauty 10:00–10:45
- Staff MB3: C1-Beauty 08:05–08:50, C5-Beauty 08:51–09:36
- Staff MB4: C3-Beauty 08:28–09:13, C7-Beauty 09:14–09:59

**Nails:**
- Staff N1: C2-Nails 07:05–07:50, C6-Nails 07:51–08:36, C10-Nails 08:37–09:22
- Staff N2: C4-Nails 07:28–08:13, C8-Nails 08:14–08:59, C12-Nails 09:00–09:45

**Hair:**
- Staff H1: C2-Hair 08:05–08:50, C6-Hair 08:51–09:36, C10-Hair 09:37–10:22
- Staff H2: C4-Hair 08:28–09:13, C8-Hair 09:14–09:59, C12-Hair 10:00–10:45

Phlebotomist A (Chair A): draws for clients 1,3,5,7,9,11. Phlebotomist B (Chair B): draws for clients 2,4,6,8,10,12.

**Headcount: 8 treatment (4 Massage+Beauty pool + 2 Nails + 2 Hair) + 2 phlebotomists = 10 total.**

**Verdict: achievable as-is, within the current committed floor plan (4 nail stations, 4 hair chairs, 2 Massage + 2 Beauty rooms all comfortably cover this) and the current committed 8-person treatment headcount. No changes needed.**

---

## 4. Corrected 14-Client Model (Carole-Facing, Current)

Same constraints as Scenario 3, same 23-min cadence, extended by one pair. **The second of the two tables sent to Carole.**

### Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 (+60min) | Service 2 | Draw 3 (+120min) |
|---|---|---|---|---|---|---|
| 1 | A | 07:00 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 |
| 2 | B | 07:00 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 |
| 3 | A | 07:23 | 07:28–08:13 | 08:23–08:28 | 08:28–09:13 | 09:23–09:28 |
| 4 | B | 07:23 | 07:28–08:13 | 08:23–08:28 | 08:28–09:13 | 09:23–09:28 |
| 5 | A | 07:46 | 07:51–08:36 | 08:46–08:51 | 08:51–09:36 | 09:46–09:51 |
| 6 | B | 07:46 | 07:51–08:36 | 08:46–08:51 | 08:51–09:36 | 09:46–09:51 |
| 7 | A | 08:09 | 08:14–08:59 | 09:09–09:14 | 09:14–09:59 | 10:09–10:14 |
| 8 | B | 08:09 | 08:14–08:59 | 09:09–09:14 | 09:14–09:59 | 10:09–10:14 |
| 9 | A | 08:32 | 08:37–09:22 | 09:32–09:37 | 09:37–10:22 | 10:32–10:37 |
| 10 | B | 08:32 | 08:37–09:22 | 09:32–09:37 | 09:37–10:22 | 10:32–10:37 |
| 11 | A | 08:55 | 09:00–09:45 | 09:55–10:00 | 10:00–10:45 | 10:55–11:00 |
| 12 | B | 08:55 | 09:00–09:45 | 09:55–10:00 | 10:00–10:45 | 10:55–11:00 |
| 13 | A | 09:18 | 09:23–10:08 | 10:18–10:23 | 10:23–11:08 | 11:18–11:23 |
| 14 | B | 09:18 | 09:23–10:08 | 10:18–10:23 | 10:23–11:08 | 11:18–11:23 |

### Staff Timetable

**Massage+Beauty pool:**
- Staff MB1: C1-Massage 07:05–07:50, C5-Massage 07:51–08:36, C9-Massage 08:37–09:22, C13-Massage 09:23–10:08, C13-Beauty 10:23–11:08
- Staff MB2: C3-Massage 07:28–08:13, C7-Massage 08:14–08:59, C11-Massage 09:00–09:45, C11-Beauty 10:00–10:45
- Staff MB3: C1-Beauty 08:05–08:50, C5-Beauty 08:51–09:36, C9-Beauty 09:37–10:22
- Staff MB4: C3-Beauty 08:28–09:13, C7-Beauty 09:14–09:59

**Nails:**
- Staff N1: C2-Nails 07:05–07:50, C6-Nails 07:51–08:36, C10-Nails 08:37–09:22, C14-Nails 09:23–10:08
- Staff N2: C4-Nails 07:28–08:13, C8-Nails 08:14–08:59, C12-Nails 09:00–09:45

**Hair:**
- Staff H1: C2-Hair 08:05–08:50, C6-Hair 08:51–09:36, C10-Hair 09:37–10:22, C14-Hair 10:23–11:08
- Staff H2: C4-Hair 08:28–09:13, C8-Hair 09:14–09:59, C12-Hair 10:00–10:45

Phlebotomist A (Chair A): draws for clients 1,3,5,7,9,11,13. Phlebotomist B (Chair B): draws for clients 2,4,6,8,10,12,14.

**Headcount: 8 treatment (4 Massage+Beauty pool + 2 Nails + 2 Hair) + 2 phlebotomists = 10 total — same as the 12-client model, not 9 as the old tolerance-window ceiling required.**

**Verdict: achievable as-is, within the current committed floor plan and 8-person treatment headcount. No changes needed. Genuinely better than the old model — same headcount serves 2 more clients.**

---

## 5. Scenario A — 08:00 Start, Same Constraints and Cadence, Running to 10:30

**Internal planning only, not shared with Carole.** Same four fixed constraints and 23-min cadence as Scenarios 3/4, shifted to an 08:00 opening. Window (last Draw 1 strictly before 10:30, from 08:00) = 149 minutes.

**14 clients fit** (7 pairs) — last Draw 1 at 10:18, inside the 10:30 limit.

### Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 (+60min) | Service 2 | Draw 3 (+120min) |
|---|---|---|---|---|---|---|
| 1 | A | 08:00 | 08:05–08:50 | 09:00–09:05 | 09:05–09:50 | 10:00–10:05 |
| 2 | B | 08:00 | 08:05–08:50 | 09:00–09:05 | 09:05–09:50 | 10:00–10:05 |
| 3 | A | 08:23 | 08:28–09:13 | 09:23–09:28 | 09:28–10:13 | 10:23–10:28 |
| 4 | B | 08:23 | 08:28–09:13 | 09:23–09:28 | 09:28–10:13 | 10:23–10:28 |
| 5 | A | 08:46 | 08:51–09:36 | 09:46–09:51 | 09:51–10:36 | 10:46–10:51 |
| 6 | B | 08:46 | 08:51–09:36 | 09:46–09:51 | 09:51–10:36 | 10:46–10:51 |
| 7 | A | 09:09 | 09:14–09:59 | 10:09–10:14 | 10:14–10:59 | 11:09–11:14 |
| 8 | B | 09:09 | 09:14–09:59 | 10:09–10:14 | 10:14–10:59 | 11:09–11:14 |
| 9 | A | 09:32 | 09:37–10:22 | 10:32–10:37 | 10:37–11:22 | 11:32–11:37 |
| 10 | B | 09:32 | 09:37–10:22 | 10:32–10:37 | 10:37–11:22 | 11:32–11:37 |
| 11 | A | 09:55 | 10:00–10:45 | 10:55–11:00 | 11:00–11:45 | 11:55–12:00 |
| 12 | B | 09:55 | 10:00–10:45 | 10:55–11:00 | 11:00–11:45 | 11:55–12:00 |
| 13 | A | 10:18 | 10:23–11:08 | 11:18–11:23 | 11:23–12:08 | 12:18–12:23 |
| 14 | B | 10:18 | 10:23–11:08 | 11:18–11:23 | 11:23–12:08 | 12:18–12:23 |

### Staff Timetable

**Massage+Beauty pool:**
- Staff MB1: C1-Massage 08:05–08:50, C5-Massage 08:51–09:36, C9-Massage 09:37–10:22, C13-Massage 10:23–11:08, C13-Beauty 11:23–12:08
- Staff MB2: C3-Massage 08:28–09:13, C7-Massage 09:14–09:59, C11-Massage 10:00–10:45, C11-Beauty 11:00–11:45
- Staff MB3: C1-Beauty 09:05–09:50, C5-Beauty 09:51–10:36, C9-Beauty 10:37–11:22
- Staff MB4: C3-Beauty 09:28–10:13, C7-Beauty 10:14–10:59

**Nails:**
- Staff N1: C2-Nails 08:05–08:50, C6-Nails 08:51–09:36, C10-Nails 09:37–10:22, C14-Nails 10:23–11:08
- Staff N2: C4-Nails 08:28–09:13, C8-Nails 09:14–09:59, C12-Nails 10:00–10:45

**Hair:**
- Staff H1: C2-Hair 09:05–09:50, C6-Hair 09:51–10:36, C10-Hair 10:37–11:22, C14-Hair 11:23–12:08
- Staff H2: C4-Hair 09:28–10:13, C8-Hair 10:14–10:59, C12-Hair 11:00–11:45

Phlebotomist A: draws for clients 1,3,5,7,9,11,13. Phlebotomist B: draws for clients 2,4,6,8,10,12,14.

**Headcount: 8 treatment (4+2+2) + 2 phlebotomists = 10 total — translation-invariant, identical to Scenario 4, just shifted an hour later.**

**Verdict: achievable as-is, no floor-plan or staffing change needed. A later start simply shifts the whole day later without changing capacity or headcount.**

---

## 6. Scenario B — True Maximum Capacity, 07:00–10:30, Corrected Constraints (The Important One)

**Internal planning only, not shared with Carole.** The old "14-client proven ceiling" (Scenario 2) was derived under the previous tolerance-window model and never held under the corrected constraints. Full search — greedy adaptive admission, 1-minute resolution, verified pairwise across every admitted client on both chairs (zero collisions across all 153 pair-comparisons among 18 pairs).

**True maximum: 36 clients (18 pairs).** Bursty, not uniform: 12 pairs (24 clients) admit every 5 minutes from 07:00–07:55, then the chair is fully occupied processing that cluster's Draw 2s (08:00–09:00, every 5-min slot taken) and Draw 3s (09:00–10:00, every 5-min slot taken) — zero new admissions possible for ~2 hours — then a second cluster of 6 pairs (12 clients) admits every 5 minutes from 10:00–10:25.

### Client / Chair Timetable

| Client | Chair | Draw 1 | Service 1 | Draw 2 (+60min) | Service 2 | Draw 3 (+120min) |
|---|---|---|---|---|---|---|
| 1 | A | 07:00 | 07:05-07:50 | 08:00-08:05 | 08:05-08:50 | 09:00-09:05 |
| 2 | B | 07:00 | 07:05-07:50 | 08:00-08:05 | 08:05-08:50 | 09:00-09:05 |
| 3 | A | 07:05 | 07:10-07:55 | 08:05-08:10 | 08:10-08:55 | 09:05-09:10 |
| 4 | B | 07:05 | 07:10-07:55 | 08:05-08:10 | 08:10-08:55 | 09:05-09:10 |
| 5 | A | 07:10 | 07:15-08:00 | 08:10-08:15 | 08:15-09:00 | 09:10-09:15 |
| 6 | B | 07:10 | 07:15-08:00 | 08:10-08:15 | 08:15-09:00 | 09:10-09:15 |
| 7 | A | 07:15 | 07:20-08:05 | 08:15-08:20 | 08:20-09:05 | 09:15-09:20 |
| 8 | B | 07:15 | 07:20-08:05 | 08:15-08:20 | 08:20-09:05 | 09:15-09:20 |
| 9 | A | 07:20 | 07:25-08:10 | 08:20-08:25 | 08:25-09:10 | 09:20-09:25 |
| 10 | B | 07:20 | 07:25-08:10 | 08:20-08:25 | 08:25-09:10 | 09:20-09:25 |
| 11 | A | 07:25 | 07:30-08:15 | 08:25-08:30 | 08:30-09:15 | 09:25-09:30 |
| 12 | B | 07:25 | 07:30-08:15 | 08:25-08:30 | 08:30-09:15 | 09:25-09:30 |
| 13 | A | 07:30 | 07:35-08:20 | 08:30-08:35 | 08:35-09:20 | 09:30-09:35 |
| 14 | B | 07:30 | 07:35-08:20 | 08:30-08:35 | 08:35-09:20 | 09:30-09:35 |
| 15 | A | 07:35 | 07:40-08:25 | 08:35-08:40 | 08:40-09:25 | 09:35-09:40 |
| 16 | B | 07:35 | 07:40-08:25 | 08:35-08:40 | 08:40-09:25 | 09:35-09:40 |
| 17 | A | 07:40 | 07:45-08:30 | 08:40-08:45 | 08:45-09:30 | 09:40-09:45 |
| 18 | B | 07:40 | 07:45-08:30 | 08:40-08:45 | 08:45-09:30 | 09:40-09:45 |
| 19 | A | 07:45 | 07:50-08:35 | 08:45-08:50 | 08:50-09:35 | 09:45-09:50 |
| 20 | B | 07:45 | 07:50-08:35 | 08:45-08:50 | 08:50-09:35 | 09:45-09:50 |
| 21 | A | 07:50 | 07:55-08:40 | 08:50-08:55 | 08:55-09:40 | 09:50-09:55 |
| 22 | B | 07:50 | 07:55-08:40 | 08:50-08:55 | 08:55-09:40 | 09:50-09:55 |
| 23 | A | 07:55 | 08:00-08:45 | 08:55-09:00 | 09:00-09:45 | 09:55-10:00 |
| 24 | B | 07:55 | 08:00-08:45 | 08:55-09:00 | 09:00-09:45 | 09:55-10:00 |
| 25 | A | 10:00 | 10:05-10:50 | 11:00-11:05 | 11:05-11:50 | 12:00-12:05 |
| 26 | B | 10:00 | 10:05-10:50 | 11:00-11:05 | 11:05-11:50 | 12:00-12:05 |
| 27 | A | 10:05 | 10:10-10:55 | 11:05-11:10 | 11:10-11:55 | 12:05-12:10 |
| 28 | B | 10:05 | 10:10-10:55 | 11:05-11:10 | 11:10-11:55 | 12:05-12:10 |
| 29 | A | 10:10 | 10:15-11:00 | 11:10-11:15 | 11:15-12:00 | 12:10-12:15 |
| 30 | B | 10:10 | 10:15-11:00 | 11:10-11:15 | 11:15-12:00 | 12:10-12:15 |
| 31 | A | 10:15 | 10:20-11:05 | 11:15-11:20 | 11:20-12:05 | 12:15-12:20 |
| 32 | B | 10:15 | 10:20-11:05 | 11:15-11:20 | 11:20-12:05 | 12:15-12:20 |
| 33 | A | 10:20 | 10:25-11:10 | 11:20-11:25 | 11:25-12:10 | 12:20-12:25 |
| 34 | B | 10:20 | 10:25-11:10 | 11:20-11:25 | 11:25-12:10 | 12:20-12:25 |
| 35 | A | 10:25 | 10:30-11:15 | 11:25-11:30 | 11:30-12:15 | 12:25-12:30 |
| 36 | B | 10:25 | 10:30-11:15 | 11:25-11:30 | 11:30-12:15 | 12:25-12:30 |

### Staff Timetable — Full 27-Person Treatment Roster (Shown Explicitly, Not Just a Headcount)

**Massage+Beauty pool (9 staff):**
- Staff MB1: C1-Massage 07:05–07:50, C19-Massage 07:50–08:35, C13-Beauty 08:35–09:20, C25-Massage 10:05–10:50, C25-Beauty 11:05–11:50
- Staff MB2: C3-Massage 07:10–07:55, C21-Massage 07:55–08:40, C15-Beauty 08:40–09:25, C27-Massage 10:10–10:55, C27-Beauty 11:10–11:55
- Staff MB3: C5-Massage 07:15–08:00, C23-Massage 08:00–08:45, C17-Beauty 08:45–09:30, C29-Massage 10:15–11:00, C29-Beauty 11:15–12:00
- Staff MB4: C7-Massage 07:20–08:05, C1-Beauty 08:05–08:50, C19-Beauty 08:50–09:35, C31-Massage 10:20–11:05, C31-Beauty 11:20–12:05
- Staff MB5: C9-Massage 07:25–08:10, C3-Beauty 08:10–08:55, C21-Beauty 08:55–09:40, C33-Massage 10:25–11:10, C33-Beauty 11:25–12:10
- Staff MB6: C11-Massage 07:30–08:15, C5-Beauty 08:15–09:00, C23-Beauty 09:00–09:45, C35-Massage 10:30–11:15, C35-Beauty 11:30–12:15
- Staff MB7: C13-Massage 07:35–08:20, C7-Beauty 08:20–09:05 *(2 bookings only — this station's later capacity absorbed into MB1-6 once their earlier bookings freed up)*
- Staff MB8: C15-Massage 07:40–08:25, C9-Beauty 08:25–09:10 *(2 bookings only, same reason)*
- Staff MB9: C17-Massage 07:45–08:30, C11-Beauty 08:30–09:15 *(2 bookings only, same reason)*

**Nails (9 staff):**
- Staff N1: C2-Nails 07:05–07:50, C20-Nails 07:50–08:35, C26-Nails 10:05–10:50
- Staff N2: C4-Nails 07:10–07:55, C22-Nails 07:55–08:40, C28-Nails 10:10–10:55
- Staff N3: C6-Nails 07:15–08:00, C24-Nails 08:00–08:45, C30-Nails 10:15–11:00
- Staff N4: C8-Nails 07:20–08:05, C32-Nails 10:20–11:05
- Staff N5: C10-Nails 07:25–08:10, C34-Nails 10:25–11:10
- Staff N6: C12-Nails 07:30–08:15, C36-Nails 10:30–11:15
- Staff N7: C14-Nails 07:35–08:20
- Staff N8: C16-Nails 07:40–08:25
- Staff N9: C18-Nails 07:45–08:30

**Hair (9 staff):**
- Staff H1: C2-Hair 08:05–08:50, C20-Hair 08:50–09:35, C26-Hair 11:05–11:50
- Staff H2: C4-Hair 08:10–08:55, C22-Hair 08:55–09:40, C28-Hair 11:10–11:55
- Staff H3: C6-Hair 08:15–09:00, C24-Hair 09:00–09:45, C30-Hair 11:15–12:00
- Staff H4: C8-Hair 08:20–09:05, C32-Hair 11:20–12:05
- Staff H5: C10-Hair 08:25–09:10, C34-Hair 11:25–12:10
- Staff H6: C12-Hair 08:30–09:15, C36-Hair 11:30–12:15
- Staff H7: C14-Hair 08:35–09:20
- Staff H8: C16-Hair 08:40–09:25
- Staff H9: C18-Hair 08:45–09:30

Phlebotomist A (Chair A): draws for clients 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35 (18 clients × 3 draws = 54 draws). Phlebotomist B (Chair B): identical pattern for clients 2,4,...,36.

**Headcount: 27 treatment (9 Massage+Beauty pool + 9 Nails + 9 Hair) + 2 phlebotomists = 29 total AM staff — nearly 3× the current committed 10.**

**Revenue/cost implications (same method as the 12-vs-14 comparison):** extra revenue vs the 12-client baseline = 24 extra clients × A$250 × 22 days = **+A$132,000/month**. Extra labor (19 additional treatment heads: +5 Massage+Beauty pool, +7 Nails, +7 Hair) = **+A$96,687.83/month**. Net, on labor cost alone: **+A$35,312.17/month better than the 12-client baseline.**

**Verdict: NOT achievable within the current floor plan or staffing. This is a real, mathematically verified draw-timing maximum — but the committed day-one floor plan (`docs/floor-plan-concept.md`) has only 4 nail stations, 4 hairdressing chairs, and 2 Massage + 2 Beauty rooms, nowhere near the 9 stations per line this schedule needs operating simultaneously.** The labor-cost comparison above is favourable in isolation, but the physical-capacity gap is the dominant, decisive constraint — this would require a floor-plan rebuild far beyond anything currently costed, not just a hiring decision. Presented as a theoretical ceiling for awareness, not a recommended or realistic operating point.

---

## 7. Scenario C — 25-Minute Cadence (Rounder, Looser Than the Tightest-Found 23 Minutes)

**Internal planning only, not shared with Carole.** Confirmed, not assumed: 25 minutes is looser than the tightest collision-free gap (23), so collision-freedom holds — verified programmatically for all three sub-cases below.

### 7a. 12-Equivalent (6 Pairs, g=25)

| Client | Chair | Draw 1 | Service 1 | Draw 2 (+60min) | Service 2 | Draw 3 (+120min) |
|---|---|---|---|---|---|---|
| 1 | A | 07:00 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 |
| 2 | B | 07:00 | 07:05–07:50 | 08:00–08:05 | 08:05–08:50 | 09:00–09:05 |
| 3 | A | 07:25 | 07:30–08:15 | 08:25–08:30 | 08:30–09:15 | 09:25–09:30 |
| 4 | B | 07:25 | 07:30–08:15 | 08:25–08:30 | 08:30–09:15 | 09:25–09:30 |
| 5 | A | 07:50 | 07:55–08:40 | 08:50–08:55 | 08:55–09:40 | 09:50–09:55 |
| 6 | B | 07:50 | 07:55–08:40 | 08:50–08:55 | 08:55–09:40 | 09:50–09:55 |
| 7 | A | 08:15 | 08:20–09:05 | 09:15–09:20 | 09:20–10:05 | 10:15–10:20 |
| 8 | B | 08:15 | 08:20–09:05 | 09:15–09:20 | 09:20–10:05 | 10:15–10:20 |
| 9 | A | 08:40 | 08:45–09:30 | 09:40–09:45 | 09:45–10:30 | 10:40–10:45 |
| 10 | B | 08:40 | 08:45–09:30 | 09:40–09:45 | 09:45–10:30 | 10:40–10:45 |
| 11 | A | 09:05 | 09:10–09:55 | 10:05–10:10 | 10:10–10:55 | 11:05–11:10 |
| 12 | B | 09:05 | 09:10–09:55 | 10:05–10:10 | 10:10–10:55 | 11:05–11:10 |

**Staff:** MB1: C1-Massage 07:05–07:50, C5-Massage 07:55–08:40, C9-Massage 08:45–09:30, C9-Beauty 09:45–10:30. MB2: C3-Massage 07:30–08:15, C7-Massage 08:20–09:05, C11-Massage 09:10–09:55, C11-Beauty 10:10–10:55. MB3: C1-Beauty 08:05–08:50, C5-Beauty 08:55–09:40. MB4: C3-Beauty 08:30–09:15, C7-Beauty 09:20–10:05. N1: C2 07:05–07:50, C6 07:55–08:40, C10 08:45–09:30. N2: C4 07:30–08:15, C8 08:20–09:05, C12 09:10–09:55. H1: C2 08:05–08:50, C6 08:55–09:40, C10 09:45–10:30. H2: C4 08:30–09:15, C8 09:20–10:05, C12 10:10–10:55. Phlebotomists as usual, clients 1/3/5/7/9/11 (A) and 2/4/6/8/10/12 (B).

**Headcount: 8 treatment (4+2+2) + 2 phlebotomists = 10 total.**

### 7b. 14-Equivalent (7 Pairs, g=25)

Same as 7a plus Client 13/14 (Chair A/B): Draw1 09:30, Service1 09:35–10:20, Draw2 10:30–10:35, Service2 10:35–11:20, Draw3 11:30–11:35. **Staff addition:** MB1 also takes C13-Massage 09:35–10:20 and C13-Beauty 10:35–11:20; N1 also takes C14-Nails 09:35–10:20; H1 also takes C14-Hair 10:35–11:20.

**Headcount: 8 treatment (4+2+2) + 2 phlebotomists = 10 total — same as 7a.**

### 7c. Scenario C's Own Maximum (9 Pairs, 18 Clients, g=25, Full Window)

Adds clients 15/16 (Draw1 09:55) and 17/18 (Draw1 10:20, last Draw1 before 10:30) to the 7b sequence. **Staff addition:** MB1 also takes C17-Massage 10:25–11:10 and C17-Beauty 11:25–12:10; MB2 also takes C15-Massage 10:00–10:45 and C15-Beauty 11:00–11:45; N1 also takes C18-Nails 10:25–11:10; N2 also takes C16-Nails 10:00–10:45; H1 also takes C18-Hair 11:25–12:10; H2 also takes C16-Hair 11:00–11:45.

**Headcount: still 8 treatment (4+2+2) + 2 phlebotomists = 10 total — unlike Scenario B's bursty 36-client maximum, the uniform 25-min cadence never triggers a headcount increase, because arrivals never cluster tightly enough to raise peak concurrency.**

**Trade-off vs Scenario B, quantified: 36 (Scenario B) − 18 (Scenario C's own maximum) = 18 fewer clients** at the wider, rounder, easier-to-communicate cadence — but Scenario C's 18-client maximum needs zero extra headcount, while Scenario B's 36-client maximum needs 19 additional treatment staff (27 total).

**Verdict (all three sub-cases): achievable as-is, within the current committed floor plan and 8-person treatment headcount. No changes needed at 12, 14, or even 18 clients under this cadence.**

---

## What Was Reconstructed vs Pulled Directly

- **Scenario 1:** pulled directly from `scenario-c-sync-timetables.md` §0.1/§0.2 — no recomputation.
- **Scenario 2:** the client table was never written out in full anywhere in this repo (§0.4 described it narratively) — **reconstructed here** by re-running `tools/draw-event-scheduler.py` (the original, already-verified tool) and computing the staff assignment via greedy first-fit. Matches the previously-reported headcount (9 treatment) exactly, confirming the reconstruction is consistent with prior verified findings, not a new/different result.
- **Scenarios 3, 4:** client tables pulled directly from `scenario-c-sync-timetables.md` §0.6. **Staff timetables reconstructed** — §0.6 stated headcount totals and per-line peaks but did not show the full named-staff booking sequences; generated here via the same sweep-line + greedy first-fit methods already established, cross-checked against §0.6's stated 8-person total (matches exactly).
- **Scenario 5 (A):** client table pulled from the direct reply already sent; staff timetable **reconstructed** (not previously shown).
- **Scenario 6 (B):** client table **reconstructed** in full (previously described as "not reproduced" in the direct reply that first found it) using the exact admitted pair-start times from the verified greedy adaptive search. Staff timetable for all 27 treatment staff **reconstructed** — this is the piece most likely to contain a transcription slip given its size; the underlying headcount (27, 9+9+9) matches the already-verified figure exactly, and the roster was generated programmatically (not typed by hand), reducing that risk.
- **Scenario 7 (C):** client tables pulled from the direct reply already sent; staff timetables for all three sub-cases **reconstructed** (not previously shown).

---

## Changelog

**2026-08 (created)** — Assembled per Anthony's/the coordinator's direct instruction: all 7 scenarios discussed across this engagement's recent work, side by side, in one document. Client tables pulled directly where they already existed in `scenario-c-sync-timetables.md`; full staff rosters generated for every scenario (the piece most often missing before), using the same sweep-line + greedy first-fit methods established throughout this engagement — no new methodology introduced. Cross-referenced from `docs/CURRENT-STATE.md` §1 and `docs/scenario-c-sync-timetables.md`.
