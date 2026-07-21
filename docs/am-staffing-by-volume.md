# GTT Center Perth — AM Staffing by Client Volume (3-10/day)

**Version:** 1.0 | **Date:** 2026-07-20
**Purpose:** Anthony wants to roster AM staff based on how many clients actually book on a given day, not always run the full 10-client complement. This document gives the checked (solver-verified, not estimated) staffing requirement — phlebotomists and treatment staff by role — for every volume from 3 to 10 clients/day, plus a full-day roster for each volume.

**Method:** built directly on the same verified structure as `scenario-c-sync-timetables.md` (10-client Scenario C) and `multirole-CORRECTION.md` (Massage+Beauty cross-training pooling) — same 40-minute admission rhythm per chair, same 45-minute service slots (Service 1: X+15 to X+60; Service 2: X+80 to X+125), same draw timing (Draw 1 = 15min; Draw 2 target X+75, ±5min tolerance; Draw 3 target X+135, ±10min tolerance). For N clients, this document takes the **first N clients of the exact same verified 10-client schedule** (i.e. "what if the day simply stops after client N books," using the identical roster pattern already proven safe) — not a new, separately-invented schedule. This is the lowest-risk way to answer the question, since it reuses timing already checked for collisions rather than inventing new draw times.

---

## Important Caveat Before Reading the Table

This document assumes, for modelling purposes, that **Chair A's clients choose Massage + Beauty and Chair B's clients choose Nails + Hair** — the same convention already used in the verified 10-client model. In reality, at lower volume, whichever chair a client is assigned to should reflect the treatment lines their **actual booking** requests, not an arbitrary assumption. The genuine planning takeaway from this document is the **shape** of the staffing requirement (how many phlebotomists, and the ceiling on treatment concurrency per active chair) — the specific service-line labels (Massage vs Nails, etc.) should be swapped to match whichever 2 lines that day's real Chair-A and Chair-B bookings actually need, per the booking-driven rostering principle already established in `pm-staffing-roster.md` §AM + PM Rostering Methodology ("the Manager reviews the following week's confirmed Fresha schedule and rosters exactly the staff each day requires").

---

## Summary Table — Genuine Staffing Requirement by Volume

| Clients/day | Chairs active | Phlebotomists | Massage | Beauty | Nails | Hair | Treatment staff (no pooling) | Treatment staff (Massage+Beauty pooled) |
|---|---|---|---|---|---|---|---|---|
| 3 | 1 | 1 | 2 | 2 | 0 | 0 | 4 | 3 |
| 4 | 1 | 1 | 2 | 2 | 0 | 0 | 4 | 3 |
| 5 | 1 | 1 | 2 | 2 | 0 | 0 | 4 | 3 |
| 6 | 2 | 2 | 2 | 2 | 1 | 1 | 6 | 5 |
| 7 | 2 | 2 | 2 | 2 | 2 | 2 | 8 | 7 |
| 8 | 2 | 2 | 2 | 2 | 2 | 2 | 8 | 7 |
| 9 | 2 | 2 | 2 | 2 | 2 | 2 | 8 | 7 |
| 10 | 2 | 2 | 2 | 2 | 2 | 2 | 8 | 7 |

**How to read the "0" entries at N=3-5:** with only 1 chair active, this document's Chair-A-only convention means no clients are modelled as choosing Nails/Hair at those volumes — this is an artifact of the illustrative chair-assignment convention above, not a claim that nail/hair services genuinely have zero demand at low volume. In practice, whichever 2 lines that day's bookings actually need should be read into the "2/2" columns instead (see caveat above).

**Where the Massage+Beauty pooling number comes from:** per `multirole-CORRECTION.md`, Massage and Beauty (both Cert IV under MA000005) can be combined into a single cross-trained pool, sized to their **combined** concurrent demand rather than each needing separate staff — this pool peaks at 3 people at every volume from 3-10 (it doesn't grow with volume within this range because the peak is driven by the fixed 40-minute rhythm and 45-minute service slots, not raw client count, once at least 3 clients are on that chair). Nails and Hair cannot pool (separate trade qualifications, confirmed in `am-capacity-weekend.md`'s Multi-Role Relief Hiring analysis) — each needs its own dedicated headcount.

**Why 7-8 is the ceiling from N=7 onward, not just at N=10:** once a chair has 2 or more clients whose 45-minute service slots overlap under the 40-minute admission rhythm, that line's concurrency ceiling of 2 is already reached — this happens at the 2nd client on a given chair, so Chair B's Nails/Hair requirement reaches its final "2 each" ceiling as soon as Chair B has 2 clients (N=7 in this document's chair-filling convention), not only when the whole day reaches 10.

**Important update (2026-07-21) — this table is one illustrative mix, not a true minimum or worst case:** see §Does Pre-Known Service Composition Tighten the Roster Further? below. The "7 staff" figure assumes a specific 50/50 Massage+Beauty / Nails+Hair split — real bookings could need as few as 6 (if concentrated on the poolable Massage+Beauty combo) or more than 7 (if concentrated on Nails or Hair specifically) once actual per-client service selections are known, rather than just a headcount.

---

## Full-Day Rosters by Volume

Each roster below is the exact same verified draw/service timing as `scenario-c-sync-timetables.md`, truncated to N clients. D1/D2/D3 = Draw 1/2/3 (phlebotomist), S1/S2 = Service 1/2 (treatment staff).

### N = 3 (1 chair, 1 phlebotomist, Massage+Beauty pool of 3)

| Client | Chair | D1 | S1 | D2 | S2 | D3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00-07:15 | 07:15-08:00 (Massage) | 08:15-08:20 | 08:20-09:05 (Beauty) | 09:15-09:20 | ~09:30 |
| 2 | A | 07:40-07:55 | 07:55-08:40 (Massage) | 08:55-09:00 | 09:00-09:45 (Beauty) | 09:55-10:00 | ~10:10 |
| 3 | A | 08:20-08:35 | 08:35-09:20 (Massage) | 09:35-09:40 | 09:40-10:25 (Beauty) | 10:35-10:40 | ~10:50 |

**Roster:** 1 phlebotomist (Chair A only), 3 Massage+Beauty-qualified staff (pooled), Venue Manager/Receptionist for opening/coordination. No Nails/Hair staff rostered this day (unless that day's actual bookings request those services — see caveat above).

### N = 4 (1 chair, 1 phlebotomist, Massage+Beauty pool of 3)

| Client | Chair | D1 | S1 | D2 | S2 | D3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00-07:15 | 07:15-08:00 | 08:15-08:20 | 08:20-09:05 | 09:15-09:20 | ~09:30 |
| 2 | A | 07:40-07:55 | 07:55-08:40 | 08:55-09:00 | 09:00-09:45 | 09:55-10:00 | ~10:10 |
| 3 | A | 08:20-08:35 | 08:35-09:20 | 09:35-09:40 | 09:40-10:25 | 10:35-10:40 | ~10:50 |
| 4 | A | 09:00-09:15 | 09:15-10:00 | 10:15-10:20 | 10:20-11:05 | 11:15-11:20 | ~11:30 |

**Roster:** same as N=3 — 1 phlebotomist, Massage+Beauty pool of 3. Adding a 4th client on the same chair doesn't add headcount, only extends the day.

### N = 5 (1 chair, 1 phlebotomist, Massage+Beauty pool of 3 — Chair A at its own full capacity)

| Client | Chair | D1 | S1 | D2 | S2 | D3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00-07:15 | 07:15-08:00 | 08:15-08:20 | 08:20-09:05 | 09:15-09:20 | ~09:30 |
| 2 | A | 07:40-07:55 | 07:55-08:40 | 08:55-09:00 | 09:00-09:45 | 09:55-10:00 | ~10:10 |
| 3 | A | 08:20-08:35 | 08:35-09:20 | 09:35-09:40 | 09:40-10:25 | 10:35-10:40 | ~10:50 |
| 4 | A | 09:00-09:15 | 09:15-10:00 | 10:15-10:20 | 10:20-11:05 | 11:15-11:20 | ~11:30 |
| 5 | A | 09:40-09:55 | 09:55-10:40 | 10:55-11:00 | 11:00-11:45 | 11:55-12:00 | ~12:10 |

**Roster:** 1 phlebotomist, Massage+Beauty pool of 3. This is the maximum a single chair can carry within the 07:00-09:40 admission window — a 6th client cannot be added to Chair A alone (would need a 2nd chair, i.e. N=6 below).

### N = 6 (2 chairs, 2 phlebotomists, Massage+Beauty pool of 3, Nails 1, Hair 1)

| Client | Chair | D1 | S1 | D2 | S2 | D3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00-07:15 | 07:15-08:00 (Massage) | 08:15-08:20 | 08:20-09:05 (Beauty) | 09:15-09:20 | ~09:30 |
| 2 | A | 07:40-07:55 | 07:55-08:40 (Massage) | 08:55-09:00 | 09:00-09:45 (Beauty) | 09:55-10:00 | ~10:10 |
| 3 | A | 08:20-08:35 | 08:35-09:20 (Massage) | 09:35-09:40 | 09:40-10:25 (Beauty) | 10:35-10:40 | ~10:50 |
| 4 | A | 09:00-09:15 | 09:15-10:00 (Massage) | 10:15-10:20 | 10:20-11:05 (Beauty) | 11:15-11:20 | ~11:30 |
| 5 | A | 09:40-09:55 | 09:55-10:40 (Massage) | 10:55-11:00 | 11:00-11:45 (Beauty) | 11:55-12:00 | ~12:10 |
| 6 | B | 07:00-07:15 | 07:15-08:00 (Nails) | 08:15-08:20 | 08:20-09:05 (Hair) | 09:15-09:20 | ~09:30 |

**Roster:** 2 phlebotomists (both chairs now active), Massage+Beauty pool of 3, 1 Nail Technician, 1 Hairdresser. Note: opening a 2nd chair for just 1 extra client is a real operational trade-off — a 2nd phlebotomist's full AM shift cost is incurred for only 1 additional client's revenue at this exact volume, worth the Venue Manager's judgement call rather than an automatic trigger (see `staff-plan.md` §7A's volume-triggered growth-plan logic for the same principle applied to the PM side).

### N = 7 (2 chairs, 2 phlebotomists, Massage+Beauty pool of 3, Nails 2, Hair 2 — treatment ceiling reached)

| Client | Chair | D1 | S1 | D2 | S2 | D3 | Depart |
|---|---|---|---|---|---|---|---|
| 1 | A | 07:00-07:15 | 07:15-08:00 (Massage) | 08:15-08:20 | 08:20-09:05 (Beauty) | 09:15-09:20 | ~09:30 |
| 2 | A | 07:40-07:55 | 07:55-08:40 (Massage) | 08:55-09:00 | 09:00-09:45 (Beauty) | 09:55-10:00 | ~10:10 |
| 3 | A | 08:20-08:35 | 08:35-09:20 (Massage) | 09:35-09:40 | 09:40-10:25 (Beauty) | 10:35-10:40 | ~10:50 |
| 4 | A | 09:00-09:15 | 09:15-10:00 (Massage) | 10:15-10:20 | 10:20-11:05 (Beauty) | 11:15-11:20 | ~11:30 |
| 5 | A | 09:40-09:55 | 09:55-10:40 (Massage) | 10:55-11:00 | 11:00-11:45 (Beauty) | 11:55-12:00 | ~12:10 |
| 6 | B | 07:00-07:15 | 07:15-08:00 (Nails) | 08:15-08:20 | 08:20-09:05 (Hair) | 09:15-09:20 | ~09:30 |
| 7 | B | 07:40-07:55 | 07:55-08:40 (Nails) | 08:55-09:00 | 09:00-09:45 (Hair) | 09:55-10:00 | ~10:10 |

**Roster:** 2 phlebotomists, Massage+Beauty pool of 3, 2 Nail Technicians, 2 Hairdressers — **this is the full 7-person treatment ceiling reached at only 7 clients/day**, not just at 10. Adding clients 8, 9, or 10 on Chair B does not add further treatment headcount — it only extends the day and increases utilisation of the same 7 people.

### N = 8, 9, 10 (2 chairs, 2 phlebotomists, Massage+Beauty pool of 3, Nails 2, Hair 2 — same 7-person ceiling as N=7)

These three volumes share the identical staffing requirement as N=7 above — only the number of clients on Chair B (and the length of the day) changes:

| Client | Chair | D1 | S1 | D2 | S2 | D3 | Depart |
|---|---|---|---|---|---|---|---|
| 8 | B | 08:20-08:35 | 08:35-09:20 (Nails) | 09:35-09:40 | 09:40-10:25 (Hair) | 10:35-10:40 | ~10:50 |
| 9 | B | 09:00-09:15 | 09:15-10:00 (Nails) | 10:15-10:20 | 10:20-11:05 (Hair) | 11:15-11:20 | ~11:30 |
| 10 | B | 09:40-09:55 | 09:55-10:40 (Nails) | 10:55-11:00 | 11:00-11:45 (Hair) | 11:55-12:00 | ~12:10 |

(Clients 1-7 on both chairs are identical to the N=7 roster above — add Client 8 for N=8, Clients 8-9 for N=9, Clients 8-10 for N=10.)

**This confirms the finding already established for the full 10-client model in `multirole-CORRECTION.md`: 7 treatment staff (not 8) is the genuine ceiling from N=7 all the way to N=10** — the treatment-staff requirement does not scale further with volume once both chairs have reached their own individual 2-client-overlap threshold. Only the phlebotomist requirement (fixed at 2 once both chairs are active) and the day's total length change between N=7 and N=10.

---

## Does Pre-Known Service Composition (Not Just Client Count) Tighten the Roster Further? (Added 2026-07-21)

**Anthony's clarified question:** within the existing 10-client/day ceiling (no capacity change), if each of the 10 clients has already pre-booked a specific Package (1 or 2) with a **known service selection**, not just a headcount — does knowing exactly which services each client will use let AM roster fewer (or different) treatment staff than the volume-only model above (7 treatment staff at N=10)?

### The Summary Table Above Was Never a Worst-Case Model — This Is the Key Finding

**Checked, and the answer changes the framing of the existing table:** the "7 treatment staff at N=10" figure in the Summary Table above is not a worst-case ceiling and not a true minimum — it's the result of **one specific, illustrative, assumed service mix** (Chair A's 5 clients always want Massage+Beauty, Chair B's 5 clients always want Nails+Hair, evenly split). The document's own caveat already flagged this convention as illustrative, but did not check what happens under a *different* real mix. This section checks that directly.

**True worst case (checked via the same concurrency solver):** if enough real clients' bookings happen to cluster onto the same single service line (a legitimate possibility — nothing in the booking system prevents 6+ clients all choosing, say, Massage as one of their 2 services), peak concurrent demand on that **one line alone can reach 6** — not the "2 per line" ceiling the illustrative model assumes. If that heavily-demanded line is Nails or Hair (non-poolable), this could require **more than 7 total treatment staff** to safely cover a real, unfavourable-but-plausible booking mix.

**True best case (checked the same way):** if the real bookings cluster favourably — e.g. all 10 clients happen to only want services from the poolable Massage+Beauty combo, with zero demand for Nails or Hair that day — the Massage+Beauty pool only needs to cover **6** concurrent bookings (not 3), and Nails/Hair need **zero** staff, for a genuine total of **6 treatment staff, one fewer than the illustrative model's 7.**

### Direct Answer

**Yes, pre-known service composition can tighten (or loosen) the roster below/above the volume-only model's 7-staff figure — in both directions, depending on what that specific day's real bookings actually are.** The volume-only model (client count alone) cannot distinguish between a favourable day (needs 6) and an unfavourable day (could need more than 7) — it only produces one illustrative middle answer. **Knowing the actual service composition in advance lets the Manager roster exactly what that specific day requires, rather than a single blanket number every day** — this is the same "booking-driven, not calendar-driven" rostering principle already established in `pm-staffing-roster.md` §AM + PM Rostering Methodology, now confirmed to apply to treatment-line allocation specifically, not just overall headcount ramp.

**Practical implication:** once GTT Center Perth is live and Fresha shows real, confirmed package/service selections for the coming week, the Manager should compute that specific week's actual per-line concurrency (using the same method demonstrated here) rather than defaulting to the illustrative 7-staff figure every day. On a day where bookings happen to concentrate on the poolable Massage+Beauty combo, 6 staff may genuinely be enough — a real, checked cost saving, not a guess. Conversely, if a real day's bookings cluster heavily onto Nails or Hair specifically, the Manager needs to check whether more than 7 is actually required, rather than assuming 7 is always a safe ceiling.

**What this does not change:** the phlebotomist requirement (1 per active chair, 2 at N≥6) is unaffected by service composition — phlebotomists handle blood draws regardless of which treatment services a client selected, so this finding is specific to treatment staff only.

---

## What This Enables — Natural Next Step (Flagged, Not Built Here)

With a genuine per-volume staffing requirement now established, the natural next step is a **per-volume P&L** — recalculating AM revenue, direct labor cost, and net contribution at each of 3-10 clients/day, the same way `profit-loss-tables.md` currently does only for the full 10-client steady-state case. This would show, for example, whether a 6-client day (2 phlebotomists rostered for just 1 extra Chair-B client) is worth running versus holding at 5 (1 phlebotomist, no 2nd chair needed) — a genuine cost/revenue trade-off this document's staffing table alone can't answer. **Not built in this document** — flagged as the logical follow-up once Anthony confirms this staffing table is correct, per his own framing of the request.

---

## Related Documents

- `scenario-c-sync-timetables.md` — the verified 10-client model this document's timing is directly built from
- `multirole-CORRECTION.md` — the Massage+Beauty pooling logic (7-not-8 finding) applied here across all volumes
- `am-capacity-weekend.md` — Multi-Role Relief Hiring analysis confirming Nails/Hair cannot pool
- `pm-staffing-roster.md` §AM + PM Rostering Methodology — the booking-driven principle this document's real-world caveat relies on
- `staff-plan.md` §7A — the volume-triggered staff growth model this document's roster-by-volume approach complements

---

## Changelog

**2026-07-20** — Created per Anthony's request: checked (not estimated) phlebotomist and treatment-staff requirements for AM client volumes 3-10/day, built directly on the verified Scenario C timing and the existing Massage+Beauty pooling finding. Includes a full-day roster for each volume. Flagged the per-volume P&L as a natural next step, not built in this document. Flagged explicitly that the specific service-line labels (Massage vs Nails etc.) at low volume are an illustrative convention matching the verified 10-client model's structure, not a claim about which services real bookings will actually request — the Manager should roster the specific lines that day's real Fresha bookings need, per the existing booking-driven principle.

**2026-07-21 (pre-known composition question answered)** — Anthony clarified the "10+10" question was actually about AM (not PM): within the existing 10-client ceiling, does knowing each client's actual pre-booked service selection (not just the headcount) tighten the roster below the 7-staff figure? Checked directly with the same concurrency solver: **the existing "7 staff" Summary Table figure was never a true worst-case or minimum — it's one specific, illustrative, 50/50 service-mix assumption.** True worst case (adversarial clustering onto one non-poolable line) can require more than 7; true best case (clustering onto the poolable Massage+Beauty combo) needs as few as 6. Confirmed pre-known composition genuinely changes the answer in both directions and lets the Manager roster the exact right number for that specific day, rather than a single blanket figure — the same booking-driven principle already established in `pm-staffing-roster.md`, now confirmed to apply to treatment-line allocation specifically. Phlebotomist requirement unaffected (draws don't depend on treatment-service choice).
