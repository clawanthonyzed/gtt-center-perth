# GTT Center Perth — Scenario C, Synchronized Chair Start — Verified Timetables

**Date:** 2026-07-17 (10-client version, now historical) | **Superseded 2026-07-30** — 12 clients/day is the committed model, see §0 below.

## 0. COMMITTED MODEL (2026-07-30) — 12 Clients/Day, 6 Slots/Chair

**Anthony corrected the committed AM volume to 12 clients/day (from 10), using the extended morning that WDP's real start-time guidance ("would not normally commence a GTT after 10:30am," Carole Rivers, email, 2026-07-30) allows.** Same 2 chairs, 2 phlebotomists, synchronized start, now 6 slots/chair (was 5) at the same 40-minute spacing. Solver-verified — full rebuild below, not carried over from the 10-client tables.

### 0.1 Client / Chair Timetable (12 Clients)

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
| **11** | **A** | **10:20–10:35** | **10:35–11:20 Massage (M2)** | **11:35–11:40** | **11:40–12:25 Beauty (B2)** | **12:35–12:40** | **~12:48** |
| **12** | **B** | **10:20–10:35** | **10:35–11:20 Nails (N2)** | **11:35–11:40** | **11:40–12:25 Hair (H2)** | **12:35–12:40** | **~12:48** |

Clients 11 and 12 (bold) are the new 6th slot per chair. Last Draw 1 at 10:20am — 10 minutes inside WDP's "not normally after 10:30am" guidance. Last departure ~12:48pm (vs ~12:05-12:08 at 10 clients — a real ~40min extension to the AM day).

### 0.2 Full Staff Timetable (12 Clients) — Every Staff Member Now Has 3 Bookings, Not the Old 3-or-2 Mix

| Staff | Bookings (time — client) |
|---|---|
| **Phlebotomist A** (Chair A) | Draws for clients 1/3/5/7/9/11 at the same clock pattern as the client table above (18 draws total) |
| **Phlebotomist B** (Chair B) | Identical clock times to Phlebotomist A, mirrored onto clients 2/4/6/8/10/12 (18 draws) |
| **Massage 1 (M1)** | C1 07:15–08:00, C5 08:35–09:20, C9 09:55–10:40 (3 bookings — unchanged from the 10-client model) |
| **Massage 2 (M2)** | C3 07:55–08:40, C7 09:15–10:00, **C11 10:35–11:20** (3 bookings — was 2 at the 10-client model; gains the new client) |
| **Beauty 1 (B1)** | C1 08:20–09:05, C5 09:40–10:25, C9 11:00–11:45 (3 bookings — unchanged) |
| **Beauty 2 (B2)** | C3 09:00–09:45, C7 10:20–11:05, **C11 11:40–12:25** (3 bookings — was 2) |
| **Nails 1 (N1)** | C2 07:15–08:00, C6 08:35–09:20, C10 09:55–10:40 (3 bookings — unchanged) |
| **Nails 2 (N2)** | C4 07:55–08:40, C8 09:15–10:00, **C12 10:35–11:20** (3 bookings — was 2) |
| **Hair 1 (H1)** | C2 08:20–09:05, C6 09:40–10:25, C10 11:00–11:45 (3 bookings — unchanged) |
| **Hair 2 (H2)** | C4 09:00–09:45, C8 10:20–11:05, **C12 11:40–12:25** (3 bookings — was 2) |

**Every one of the 8 treatment staff now works 3 bookings/day (135 min booked each)** — the "2-booking" staff (M2, B2, N2, H2) each pick up the new 6th slot's client. This is a genuinely different pattern from the 10-client model, not just more of the same — see `docs/CURRENT-STATE.md` §8 and `profit-loss-tables.md` for how this changes the downtime-fill and early-release figures.

### 0.3 Verification (programmatic, not manual) — Both the Chair/Phlebotomist Side and Treatment Concurrency

| Line | Peak concurrent | Capacity (8-staff, no pooling) | Result |
|---|---|---|---|
| Massage | 2 | 2 | OK |
| Beauty | 2 | 2 | OK |
| Nails | 2 | 2 | OK |
| Hair | 2 | 2 | OK |

**Zero double-bookings, all 12 clients placed.** Phlebotomist/chair side independently re-verified (not assumed from the 10-client pattern) — zero collisions across both chairs' full 18-draw sequences each.

**Pooling re-checked at 12 clients, both FAIL** (see `profit-loss-tables.md`'s Treatment Headcount section for full detail):
- Massage+Beauty pooled (7-staff, cap 3): peak concurrent demand on the pool exceeds 3 — 2 clients unassignable.
- Massage+Beauty AND Nails+Hair both pooled (6-staff, cap 3 each): 4 clients unassignable.

**The committed 12-client model requires 8 dual-qualified treatment staff, required by peak overlap — there is no "unpooled" model.** The 7-staff/6-staff findings from 2026-07-29 (Massage+Beauty pool sized to 3) are correct only for the now-superseded 10-client model — at 12 clients/day the pool's own peak concurrency is 4 (same as the sum of the individual Massage and Beauty peaks). **Clarifying note: 8 is correct and expected at this 12-client design ceiling. 7 (pool sized to 3) remains a legitimate daily-rostering choice on lower-volume actual days, below this ceiling.**

### 0.4 14 Clients/Day — PROVEN CEILING (Maximum Verified Capacity), NOT the Daily Operating Target

Per Anthony's direct instruction ("we are aiming for 12 or max capacity for 2 chairs and last client before 10:30am"), re-ran the full optimization search (`tools/draw-event-scheduler.py`'s `run()`, multi-resolution sweep of `CANDIDATE_STEP` from 1 to 44+, not the fixed 40-min-cadence assumption above), bounded by last Draw 1 strictly before 10:30am (minute 210 from 07:00).

**True chair/phlebotomist-only ceiling: 14 clients/day** (best found at search resolution step=1; every other tested resolution gives 12 or 13). The 14-client schedule packs clients into two tight bursts (07:00-07:46 and 09:55-10:26) separated by a ~2hr09min mid-morning gap with zero new arrivals — a materially different shape from the smooth 40-min-cadence rhythm above.

**Corrected method:** the first headcount check used a naive per-line multiply (peak concurrency 3 × 4 lines = 12) and was never tested against Massage+Beauty dual-qualification, the way the 10-client and 12-client cases were. Re-tested via direct interval-overlap simulation on the real bursty timing: combining every Massage window and every Beauty window from the 7 chair-A clients into one shared-pool timeline gives a true peak of **3, not 6** — the massage-cluster (peak 07:45) and beauty-cluster (peak 08:50) occur at different clock times, so the pool genuinely shares capacity. Nails and Hair have no confirmed dual-qualification pairing, so each stays on its own line at its individually-checked peak of 3.

**True minimum treatment headcount at N=14: 9 (3 Massage+Beauty pool + 3 Nails + 3 Hair), not 12.** `[VERIFICATION NEEDED — Nails+Hair pairing not yet confirmed as hireable]`: if confirmed, the same method gives a hypothetical 6 total — flagged only, not assumed.

**Financial verdict, recomputed:** extra revenue from 12→14 = A$11,000/month. Extra labor cost at 9 staff (A$551,058/yr) vs the 12-client model's 8 staff (A$492,920/yr) = +A$4,844.83/month, not +A$20,538.33/month. **Net: +A$6,155.17/month if 14 is pursued with the correctly dual-qualification-optimized 9-person roster — better than staying at 12.**

**Conclusion, Anthony's decision 2026-07-31: "have 14 as the ceiling and prove it. 12 clients a day is what we will aim for each day."** 14 is now proven — 9-staff headcount confirmed via two independent methods (sweep-line peak concurrency + greedy first-fit assignment, exact agreement), full whole-venture P&L completed (+A$36,726.23/month, see `profit-loss-tables.md`) — and documented as a proven ceiling/growth-headroom figure. **12 clients/day (§0 above) remains the committed daily operating target, unchanged.** See `docs/CURRENT-STATE.md` §1/§4/§7 for the same finding recorded canonically.

---

### 0.5 Carole's Hard Clinical-Mark Constraint (Exact 60/120-Minute Draw Spacing) — SOLVED, 2026-08

**Background:** every schedule above (§0-§0.4) used the draw-event model's D2/D3 TOLERANCE windows (Draw 2 target X+75 ±5min, Draw 3 target X+135 ±10min) to dodge chair collisions — verified for internal double-booking/concurrency only, never checked against clinical tolerance for OGTT draw-timing accuracy. Carole Rivers' (WDP) full email chain includes her own indicative timetable for a ~14-patient morning, using **exact clinical marks**: Fasting (Draw 1) → **exactly 1-Hour** (Draw 2, X+60) → **exactly 2-Hour** (Draw 3, X+120), no flex mentioned, pairs starting roughly every 15 minutes. **Minor inconsistency noted, not silently resolved:** Carole's own narrative says "~14 patients," but her table lists 8 pairs = 16 patients — both her numbers are shown here, neither picked silently.

**(a) Re-ran the scheduler constrained to EXACT 60-minute and 120-minute post-Draw-1 spacing (zero tolerance), both draw-timing feasibility and wellness-service fit, at 12 and 14 clients:**

*Draw-timing (chair/phlebotomist collision) feasibility:* **both 12 and 14 clients remain achievable** on 2 chairs within the existing last-Draw-1-before-10:30am window — confirmed via a dedicated hard-constraint solver (fixed Draw2=X+60, Draw3=X+120 for every client, multi-resolution sweep). The best schedule (14 clients) naturally converges to the same ~15-minute pair-arrival cadence Carole's own table uses — a genuine cross-check that the two independently-built schedules agree on shape, not just headcount.

*Wellness-service-block fit — this is where a real trade-off exists, reported plainly:*
- **Service 1 window (between Draw 1 end and Draw 2's exact mark):** X+15 to X+60 = 45 minutes total, for the service itself plus a walk-back/prep transition buffer.
  - Package 1 (30-min service): 30min service + 15min buffer — **fits comfortably.**
  - A 45-min service scheduled FIRST: 45min service + 0min buffer — **does not fit** (no time for the client to return to the collection-room chair or for the phlebotomist to prep). Using this repo's own established 10-minute transition-buffer convention (already used for the flexible-tolerance model), **Service 1 is capped at 35 minutes**, not 45.
- **Service 2 window (between Draw 2 end and Draw 3's exact mark):** X+65 to X+120 = 55 minutes total.
  - A 45-min service scheduled SECOND: 45min service + 10min buffer — **fits fine**, same buffer convention as elsewhere in this document.

**Exactly what has to give:** Package 1 (2×30min) is entirely unaffected by Carole's hard clinical marks. Package 2's flexible combos work **if the 45-min service is always routed to Slot 2, never Slot 1** — a booking-system rule (whichever of the client's two chosen services is 30min goes first, whichever is 45min goes second), not a structural blocker. **The one combo that genuinely cannot fit as specified is "2×45min both slots"** — the first of the two 45-min blocks would need to shrink to ≤35 minutes (a real, disclosed reduction), or that specific combo should not be offered under this constraint. This is a legitimate, reportable trade-off, not a failure to hide.

**(b) Tested Carole's own ~15-minute pair-spacing cadence against treatment-line peak concurrency (Massage+Beauty pool, Nails, Hair), using the sweep-line + greedy first-fit methods already established for the 12/14-client checks — not eyeballed:**

| Volume | Massage+Beauty pool | Nails | Hair | **Total headcount** | vs. previously-established figure |
|---|---|---|---|---|---|
| 12 clients (hard-constraint, Carole's cadence) | 3 | 2 | 3 | **8** | **Unchanged from the committed model's 8** — same total, but the split shifts (Hair needs 3 not 2, the Massage+Beauty pool needs 3 not 4, under this specific tighter-cadence arrangement). Checked at two different N=12 configurations (both give the same 8/3-2-3 split), not a one-off. |
| 14 clients (hard-constraint, Carole's cadence) | 3 | 3 | 3 | **9** | **Exactly matches** the already-proven 14-client ceiling headcount (§0.4 above) — Carole's tighter ~15-min cadence does not add headcount beyond what was already found. |

**Conclusion: Carole's ~15-minute pair-spacing cadence is workable at both 12 and 14 clients, on 2 chairs, without any additional treatment headcount beyond the already-committed/proven figures (8 at 12/day, 9 at 14/day).** The genuine trade-off is not headcount — it's the wellness-service-block constraint in (a) above: Package 2's "2×45min" combo needs adjusting (route the 45-min service to Slot 2, or accept a shortened first block) once the exact clinical marks are the design basis rather than the flexible-tolerance windows used throughout this document until now. See `docs/VERIFICATION-TRACKER.md` for the same finding logged canonically.

---

## 1. Client / Chair Timetable (10 Clients — HISTORICAL, superseded 2026-07-30, retained for trace)

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

## 2. Full Staff Timetable (10 Clients — HISTORICAL)

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

## 3. Verification (10 Clients — HISTORICAL, programmatic, not manual)

Every treatment line's peak concurrent bookings checked by exhaustive interval-overlap simulation:

| Line | Peak concurrent | Capacity | Result |
|---|---|---|---|
| Massage | 2 | 2 | OK |
| Beauty | 2 | 2 | OK |
| Nails | 2 | 2 | OK |
| Hair | 2 | 2 | OK |

**Zero double-bookings, all 10 clients placed.** Synchronized start confirmed safe end-to-end — chairs, phlebotomists, and all 8 treatment staff. **This was the committed model until 2026-07-30 — see §0 above for the current 12-client model.**

## 4. Still on "a better way to utilise phlebotomist time" (historical framing — the ceiling discussed below has since moved)

Re-confirming rather than re-opening at the time: this exact question was tested twice already with an actual constraint solver (not manual arithmetic) — `draw-event-scheduler-findings.md`. Both runs (staggered and synchronized layout) landed on the same ceiling **at the time**: 10 clients/day was believed to be the genuine maximum on 2 chairs within the then-assumed window (last new-draw start ~10:05, driven by an unconfirmed ~12:30 courier cutoff). **This ceiling has since moved twice:** WDP's real courier/cutoff answer (2026-07-30) turned out to be conditional, not a hard 12:30 wall, and WDP's real start-time guidance (10:30am, not the ~10:00 assumption this section's ceiling was built around) opened room for the 6th slot verified in §0 above. The lever flagged below (non-phlebotomist assistant reducing draw attention-time) remains untested either way.

The only lever not yet closed off by the solver: **whether a non-phlebotomist assistant absorbing labelling/centrifuge/escort tasks could shrink the phlebotomist's actual attention-time per draw** (flagged previously, still unverified — needs a minute-by-minute task breakdown of what currently happens inside the 15/5/5-min draw blocks, plus confirmation from WDP on whether non-accredited staff can legally handle specimens under their Licensed Collection Centre QMS).

## Changelog

**2026-07-17 (created)** — Synchronized-start verification for the then-current 10-client model.

**2026-07-30 (superseded, full rebuild)** — Anthony corrected the committed AM volume to 12 clients/day, per WDP's real 10:30am start-time guidance (Carole Rivers, email, 2026-07-30) and a solver check confirming the extended 6-slot/chair schedule clears both draw-timing and treatment-staff concurrency. Added §0 with the full 12-client client/chair timetable, staff timetable, and verification (both re-derived directly, not assumed from the 10-client pattern). The 10-client tables (§1-3) are retained below, explicitly marked historical, for trace — not deleted, since they document a real verified milestone, just no longer the current model. §4's ceiling discussion updated to reflect that the constraint that originally capped this at 10 (an assumed ~12:30 courier cutoff) has since been shown to be more flexible than assumed.

**2026-07-30 (later still — N_max search completed, added as §0.4, first pass explored and rejected using a naive headcount estimate)** — Per Anthony's "12 or max capacity" instruction, re-ran the full optimization search with a multi-resolution sweep — true chair-only ceiling is 14, not 12. Headcount check used an uncorrected per-line multiply (12), not yet tested against dual-qualification.

**2026-07-31 ("unpooled" retired everywhere per Anthony's direct instruction; N_max headcount re-corrected via dual-qualification, conclusion reversed)** — Removed all "unpooled" language from §0.3/§0.4 — every treatment-staff figure restated as "dual-qualified, required by peak overlap." Re-tested §0.4's N=14 headcount with Massage+Beauty dual-qualification against the real bursty timing (interval-overlap simulation): true minimum is 9, not 12. Net financial verdict reverses to +A$6,155.17/month better than staying at 12. Presented as a finding for Anthony's decision, not adopted unilaterally. See `docs/CURRENT-STATE.md` §1/§4/§7 for full method.

**2026-07-31 (later same day — Anthony's decision: 14 is a PROVEN CEILING, 12 stays the committed daily target)** — Retitled §0.4 to reflect the final framing. Anthony: "have 14 as the ceiling and prove it. 12 clients a day is what we will aim for each day." Completed the proof: full whole-venture P&L (+A$36,726.23/month, `profit-loss-tables.md`) and a second independent headcount check (greedy first-fit assignment, agrees exactly with the sweep-line method). 12 clients/day (§0) remains the committed daily operating target throughout this document, unchanged.

**2026-08 (later — Carole's hard clinical-mark constraint solved, added as new §0.5)** — Per Carole's full email chain (her own indicative timetable uses exact 60/120-min post-Draw-1 marks, no flex), built a dedicated hard-constraint solver (zero tolerance on Draw2/Draw3 timing) and re-ran both the draw-timing feasibility check and the wellness-service-block fit check at 12 and 14 clients. **Draw-timing: both 12 and 14 remain achievable** — the resulting schedule naturally converges to Carole's own ~15-min pair cadence, a genuine cross-check. **Service-block fit: Package 1 unaffected; Package 2 works if the 45-min service always routes to Slot 2 (booking-system rule); the pure "2×45min" combo genuinely cannot fit both blocks at full length — one must shrink to ≤35min, a disclosed trade-off, not hidden.** Tested Carole's ~15-min cadence against treatment-line peak concurrency using the established sweep-line + greedy first-fit methods: **headcount unchanged at both volumes (8 at 12/day, 9 at 14/day)** — the per-line split shifts slightly at 12/day (Hair 3 not 2, Massage+Beauty pool 3 not 4) but the total headcount does not increase. Logged the same finding in `docs/VERIFICATION-TRACKER.md`.
