# GTT Center Perth — Scenario C, Synchronized Chair Start — Verified Timetables

**Date:** 2026-07-17 (10-client version, now historical) | **Superseded 2026-07-30** — 12 clients/day is the committed model, see §0 below.

> **See `docs/scenario-comparison-master-2026-08.md` for all 7 schedule scenarios discussed across this engagement (this file's own models plus Scenario A/B/C internal-planning variants) side by side in one consolidated comparison — that document pulls its client tables directly from this file where they already exist here, and adds full staff rosters for every scenario.**

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

### 0.5 Carole's Hard Clinical-Mark Constraint (Exact 60/120-Minute Draw Spacing) — SUPERSEDED 2026-08, retained for trace

> **SUPERSEDED, later in 2026-08 — this section's specific schedule spec (15-min Draw 1, asymmetric 35/45-min service caps, non-synchronized chair starts) is replaced by §0.6 below.** Anthony's follow-up instruction fixed four exact constraints not used here: synchronized chair starts (both chairs start each pair at the identical clock minute), every draw exactly 5 minutes (not 15 for Draw 1), and BOTH service windows fixed at 45 minutes (not one capped at 35). **Do not use this section's tables or the 35-min-cap finding going forward — see §0.6.** Kept below for trace only, since it documents a real intermediate step (proving the exact-clinical-mark constraint was solvable at all, before the further synchronized/5-min-draw refinement).

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

### 0.6 CANONICAL Synchronized-Pair Model — Exact 60/120-min Marks, 5-min Draws, Both Services Fixed at 45min

**This is the current, canonical hard-constraint schedule — supersedes §0.5 entirely.** Four fixed constraints, per Anthony's direct instruction: (1) Chair A and Chair B start every pair at the identical clock minute — no offset. (2) Every draw (D1, D2, D3) is exactly 5 minutes, same duration for every client. (3) Draw 2 = own Draw 1 + exactly 60 min; Draw 3 = own Draw 1 + exactly 120 min — no exceptions. (4) Both Service 1 and Service 2 are exactly 45 minutes, same fixed length in both slots. Per-client shape: Draw1[0-5] → Service1[5-50] → 10-min buffer[50-60] → Draw2[60-65] → Service2[65-110] → 10-min buffer[110-120] → Draw3[120-125] — each 60-minute block is 5(draw)+45(service)+10(buffer)=60, exactly accounted for.

**Method:** since both chairs are perfect mirrors (always starting together), feasibility reduces to a single chair's own client sequence being collision-free. Verified programmatically for every table below — zero double-bookings, checked pairwise across every client on each chair, not just adjacent ones.

**Headcount is cadence-dependent, not fixed** — re-derived explicitly for every scenario below via sweep-line peak concurrency AND greedy first-fit assignment (both methods agree throughout). A tighter pair-to-pair gap packs more clients into a shorter morning but raises peak service overlap (more clients "in service" simultaneously), which raises headcount. A wider gap holds headcount down but takes longer.

**Standard 12/14-client tables (pair gap = 23 minutes, chosen because it holds headcount at 8 for both volumes — the tightest gap that does):**

*Sent to Carole via the clinic-operations overview document — these are the only two tables from this section shared externally.*

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

12-client headcount: **8 total (4 Massage+Beauty pool + 2 Nails + 2 Hair).**

14-client table adds two more rows at the same g=23 cadence: Client 13/14, Chair A/B, Draw1 09:18, Service1 09:23–10:08, Draw2 10:18–10:23, Service2 10:23–11:08, Draw3 11:18–11:23. 14-client headcount: **8 total (same split — 4+2+2), better than the previously-assumed 9.**

**Below this line: Anthony's internal planning scenarios only — NOT part of what was sent to Carole, not for external use.**

#### Scenario A — 08:00 Start, Same g=23 Cadence, Running to the 10:30 Guidance Limit

Shifted start, same four constraints, same 23-min cadence. Window (last Draw1 strictly before 10:30, from 08:00) = 149 minutes. **7 pairs (14 clients) fit** — last Draw 1 at 10:18, still inside the 10:30 limit. Headcount unchanged at **8** (translation-invariant — same relative pattern, just shifted in clock time, so the same collision-freedom and concurrency findings carry over exactly).

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

#### Scenario B — True Maximum Capacity, 07:00–10:30, Under the Corrected Constraints (the important one)

**The old "14-client proven ceiling" was derived under the previous draw-timing model (15-min Draw 1, tolerance windows) and has never held under the corrected constraints.** Full search, not cadence arithmetic: greedy adaptive admission (try to admit a new pair as early as possible, at 1-minute resolution, skip only if it collides with an already-admitted client's draws on that chair), swept across multiple resolutions, verified programmatically pairwise across every admitted client.

**True maximum: 18 pairs = 36 clients.** Verified: zero collisions across all 18×17/2=153 pair-comparisons, both chairs. The schedule is bursty, not uniform: 12 pairs (24 clients) admit in a tight cluster from 07:00 to 07:55 (every 5 minutes), then the chair is fully occupied processing that cluster's Draw 2s (08:00-09:00, every 5-min slot taken) and Draw 3s (09:00-10:00, every 5-min slot taken) — zero new admissions possible in that ~2-hour stretch — then a second cluster of 6 pairs (12 clients) admits from 10:00 to 10:25.

**Headcount re-derived explicitly, not assumed — and it does NOT hold at 8/9:** Massage+Beauty pool peak = 9, Nails peak = 9, Hair peak = 9 (sweep-line and greedy first-fit agree). **Total treatment headcount: 27** — more than triple the committed 8.

**Revenue/cost implications, same method as the 12-vs-14 comparison:** extra revenue vs the 12-client baseline = 24 extra clients × A$250 × 22 days = **+A$132,000/month**. Extra labor (19 additional heads: +5 Massage+Beauty pool, +7 Nails, +7 Hair) = **+A$96,687.83/month**. Net, on labor alone: **+A$35,312.17/month better than the 12-client baseline.**

**This labor-only comparison is not the real constraint — flagged prominently, not glossed over.** `docs/floor-plan-concept.md`'s committed day-one floor plan has only 4 nail stations, 4 hairdressing chairs, and 2 Massage + 2 Beauty rooms — nowhere near the 9 stations per line this 36-client schedule would need simultaneously. **The true mathematical draw-timing maximum is real and verified, but is not achievable within the venue's planned physical footprint without a floor-plan rebuild far beyond anything currently costed.** Presented as a theoretical ceiling for awareness, not a recommended operating point.

*(Full 36-client table not reproduced here — 18 pairs at the specific bursty admission times above; available on request if needed for further planning.)*

#### Scenario C — Same Model, 25-Minute Cadence (Rounder Number, Looser Than the Tightest-Found 23 Minutes)

Confirmed, not assumed: 25 minutes is looser than the tightest collision-free gap (23), so collision-freedom holds — verified programmatically for every table below.

**12-equivalent (6 pairs, g=25) — headcount 8 (4+2+2):**

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

**14-equivalent (7 pairs, g=25) — headcount 8 (4+2+2):** adds Client 13/14, Draw1 09:30, Service1 09:35–10:20, Draw2 10:30–10:35, Service2 10:35–11:20, Draw3 11:30–11:35.

**Scenario C's own maximum (uniform 25-min cadence, full window):** 9 pairs = **18 clients**, last pair Draw1 10:20 (before 10:30). Headcount still **8 (4+2+2)** — unlike Scenario B's bursty 36-client maximum, the uniform-cadence approach never triggers the headcount spike, because arrivals never cluster.

**Trade-off vs Scenario B, quantified:** 36 (Scenario B, bursty adaptive) − 18 (Scenario C, uniform 25-min) = **18 fewer clients** at the wider, rounder, easier-to-communicate cadence — but Scenario C's 18-client maximum needs no extra headcount at all (still 8), while Scenario B's 36-client maximum needs 27. The rounder cadence trades raw capacity for a much simpler staffing story.

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

**2026-08 (later still — synchronized-pair/5-min-draw/45+45-service model supersedes §0.5 entirely; added as canonical §0.6; three internal planning scenarios added)** — Anthony fixed four exact constraints, superseding the §0.5 spec: synchronized chair starts, every draw exactly 5 minutes, Draw2/Draw3 at exact +60/+120min, both service windows fixed at 45 minutes (5+45+10 buffer = 60min per block, exactly accounted for). Since both chairs always start together, feasibility reduces to one chair's own sequence being collision-free — verified programmatically throughout. **Standard 12/14-client tables at a 23-minute pair cadence (headcount 8 at both volumes, the tightest gap that holds headcount there) — these two tables are what went into the client-facing clinic-operations overview sent to Carole, nothing else in §0.6.** Three additional scenarios added, explicitly Anthony's internal planning only, not shared externally: **Scenario A** (08:00 start, same cadence — 14 clients fit before 10:30, headcount unchanged at 8, translation-invariant). **Scenario B** (true maximum search, greedy adaptive admission, verified pairwise — **36 clients (18 pairs), a bursty two-cluster schedule, materially higher than the old 14-client "proven ceiling," which never held under these corrected constraints**; headcount re-derived at **27**, more than triple the committed 8; net financial upside on labor alone (+A$35,312.17/month) but flagged prominently that the venue's committed floor plan has nowhere near enough physical stations — 4 nail/4 hair/2+2 massage-beauty vs the 9-per-line this schedule needs — making this a theoretical ceiling, not an achievable operating point without a floor-plan rebuild). **Scenario C** (uniform 25-min cadence, confirmed looser than the tightest-found 23min — 12/14-equivalent tables plus its own maximum of 18 clients, headcount holding at 8 throughout; quantified trade-off vs Scenario B: 18 fewer clients for a much simpler, headcount-neutral cadence).

**2026-08 (later still — master scenario comparison assembled)** — Added a cross-reference to `docs/scenario-comparison-master-2026-08.md`, which pulls Scenarios 1, 3, and 4's client tables directly from this file (§0.1 and §0.6), reconstructs Scenario 2's full client table and staff roster (never previously written out in full — only described narratively in §0.4), and adds full named-staff rosters for every scenario in this file that previously only stated headcount totals (§0.6's Scenarios A/B/C). Scenario B's 27-person treatment roster is shown explicitly there, not just as a headcount figure.
