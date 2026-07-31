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

### 0.4 True Maximum (N_max) Search — RE-CORRECTED 2026-07-31 — dual-qualification re-tested against the real 14-client timing

Per Anthony's direct instruction ("we are aiming for 12 or max capacity for 2 chairs and last client before 10:30am"), re-ran the full optimization search (`tools/draw-event-scheduler.py`'s `run()`, multi-resolution sweep of `CANDIDATE_STEP` from 1 to 44+, not the fixed 40-min-cadence assumption above), bounded by last Draw 1 strictly before 10:30am (minute 210 from 07:00).

**True chair/phlebotomist-only ceiling: 14 clients/day** (best found at search resolution step=1; every other tested resolution gives 12 or 13). The 14-client schedule packs clients into two tight bursts (07:00-07:46 and 09:55-10:26) separated by a ~2hr09min mid-morning gap with zero new arrivals — a materially different shape from the smooth 40-min-cadence rhythm above.

**Corrected method:** the first headcount check used a naive per-line multiply (peak concurrency 3 × 4 lines = 12) and was never tested against Massage+Beauty dual-qualification, the way the 10-client and 12-client cases were. Re-tested via direct interval-overlap simulation on the real bursty timing: combining every Massage window and every Beauty window from the 7 chair-A clients into one shared-pool timeline gives a true peak of **3, not 6** — the massage-cluster (peak 07:45) and beauty-cluster (peak 08:50) occur at different clock times, so the pool genuinely shares capacity. Nails and Hair have no confirmed dual-qualification pairing, so each stays on its own line at its individually-checked peak of 3.

**True minimum treatment headcount at N=14: 9 (3 Massage+Beauty pool + 3 Nails + 3 Hair), not 12.** `[VERIFICATION NEEDED — Nails+Hair pairing not yet confirmed as hireable]`: if confirmed, the same method gives a hypothetical 6 total — flagged only, not assumed.

**Financial verdict, recomputed:** extra revenue from 12→14 = A$11,000/month. Extra labor cost at 9 staff (A$551,058/yr) vs the 12-client model's 8 staff (A$492,920/yr) = +A$4,844.83/month, not +A$20,538.33/month. **Net: +A$6,155.17/month if 14 is pursued with the correctly dual-qualification-optimized 9-person roster — better than staying at 12.**

**Conclusion: this reverses the earlier "12 remains committed, N_max=14 explored and rejected" finding, which used an uncorrected headcount estimate.** Whether to adopt 14 as the new committed model is presented as a finding, not decided unilaterally — Anthony's call. See `docs/CURRENT-STATE.md` §1/§4/§7 for the same finding recorded canonically.

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
