# Scenario D — 3rd Phlebotomist Investigation: Staff Timetable + P&L

**Date:** 2026-07-17
**Status: PROVISIONAL.** Every figure below assumes the 12:30 last-departure cutoff. **That number has not been confirmed by WDP — see `cutoff-time-CORRECTION.md`.** Anthony has not received a WDP reply. Treat this whole document as "what the numbers look like if the window holds at ~12:30" — not a final recommendation to hire.

## 1. Client / Chair Timetable

Already verified (`am-capacity-weekend.md`, Scenario D): 15 clients, 3 chairs (offsets 0/+10/+20min), zero collisions, last client departs ~12:25 — only a 5-minute buffer before the assumed cutoff. That tightness is itself a reason to want the real WDP number before committing.

## 2. Staff Timetable (NEW — corrected 8-person cross-trained pool)

Uses the corrected multi-role model: 4× Massage/Beauty dual-qualified (Staff 1–4), 2× Nails (Staff 5–6), 2× Hair (Staff 7–8). Verified with a real constraint solver — zero double-bookings, every client placed, "client picks 2 services / business picks the order" flexibility used where needed.

| Staff | Bookings |
|---|---|
| Staff 1 | 07:15–08:00 C1 (Massage), 08:35–09:20 C7 (Massage), 09:25–10:10 C11 (Massage), 10:15–11:00 C15 (Massage) |
| Staff 2 | 07:35–08:20 C3 (Massage), 08:40–09:25 C3 (Beauty), 09:40–10:25 C7 (Beauty), 10:30–11:15 C11 (Beauty) |
| Staff 3 | 08:05–08:50 C5 (Massage), 08:55–09:40 C9 (Massage), 09:55–10:40 C13 (Massage), 11:00–11:45 C13 (Beauty) |
| Staff 4 | 08:20–09:05 C1 (Beauty), 09:10–09:55 C5 (Beauty), 10:00–10:45 C9 (Beauty), 11:20–12:05 C15 (Beauty) |
| Staff 5 | 07:25–08:10 C2 (Nails), 08:15–09:00 C6 (Nails), 09:15–10:00 C10 (Nails), 10:05–10:50 C14 (Nails) |
| Staff 6 | 07:55–08:40 C4 (Nails), 08:45–09:30 C8 (Nails), 09:35–10:20 C12 (Nails) |
| Staff 7 | 08:30–09:15 C2 (Hair), 09:20–10:05 C6 (Hair), 10:20–11:05 C10 (Hair), 11:10–11:55 C14 (Hair) |
| Staff 8 | 09:00–09:45 C4 (Hair), 09:50–10:35 C8 (Hair), 10:40–11:25 C12 (Hair) |
| Phlebotomist A/B/C | 15 draws each across their 5 chair-assigned clients (see am-capacity-weekend.md Scenario D per-chair breakdown) |

Busiest treatment staff: 4 bookings/day (up from 3 at today's 10-client volume) — real increase in workload, not a casual buffer, worth watching for fatigue once live.

## 3. P&L — Current (7-staff, 2 phlebotomists) vs Scenario D (8-staff, 3 phlebotomists)

Both use the conservative safe price (A$250/client, per standing instruction) and 22 trading days/month.

| | Current (10 clients/day) | Scenario D (15 clients/day) |
|---|---|---|
| Revenue | 10×22×$250 = **$55,000** | 15×22×$250 = **$82,500** |
| Phlebotomist labor | 2× ≈ **$7,178** | 3× ≈ **$10,767** |
| Treatment labor | 7-staff ≈ **$35,942** (approx — 8-staff figure of $41,077 less ~1 headcount) | 8-staff ≈ **$41,077** (unchanged headcount from today's uncrossed model — multi-role saving doesn't apply at this volume, see multirole-CORRECTION.md) |
| Opening cost (07:00 start) | **$980** | **$980** |
| **AM Direct Contribution** | **≈+$10,900/month** | **≈+$29,676/month** |
| **Incremental gain from 3rd phlebotomist** | | **≈+$18,776/month** |

## 4. What's still missing before this is a real hiring decision

1. **The WDP cutoff itself — not confirmed, possibly not even real at 12:30.** Scenario D's 5-minute buffer is tighter than Scenario C's — if the true cutoff is earlier than assumed, Scenario D may not even be achievable at 15 clients.
2. **One-off costs not included above:** 3rd phlebotomist recruitment, WDP credentialing (Cert III/IV Pathology + WDP QMS training + police clearance etc., per `gtt-clinical-protocol.md` §8) — a relief-pool 3rd phlebotomist is already approved on the books for cover, but converting that role to an *active* 3rd chair is a different commitment (more regular hours), not automatically the same cost.
3. **Treatment labor figures above are approximate**, not a full payroll recalculation — Massage/Beauty (~A$37/hr) and Nails/Hair (~A$35.63/hr) rates differ slightly; the 7-staff current-model figure is a proportional estimate, not itemized. Worth a proper recalc before finalizing, same rigor as `pm-staffing-roster.md`'s hours-based correction.

**Bottom line: the incremental economics look strong (~$18.8K/month) but the entire case is provisional on the WDP window confirmation. Recommend holding the hiring decision until that reply comes back.**
