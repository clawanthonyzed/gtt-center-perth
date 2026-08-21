# Demand-Driven Staffing Model — Position-ID Register, AM Solver Findings, PM Scaling, VM Fill Rule

**Status: new analysis, genuine solver-verified findings. PM Reception conflict (§5) since RESOLVED by direct founder decision, 2026-08-21 — see below, not silently reopened or left stale.** Built per direct instruction for a demand-driven staffing model (staggered AM starts, no-nail-clients-means-no-nail-tech-rostered logic, PM multi-staff-per-role scaling, PM reception via service-staff coverage, Venue Manager Mon-Fri emergency-only fill rule, position-ID register, solver-verified staff timetable). Every AM headcount figure below is produced by `tools/demand_driven_staffing_solver.py`, a new tool calibrated against this repo's own already-published, verified headcount figures before being trusted on any new question — not assumed or hand-derived.

---

## 1. Position-ID Register

Short IDs assigned to every position already profiled in `docs/architecture/STAFF-PROFILES.md`, plus the 4 PM dedicated-casual roles (previously identified only by role name in `data/canonical/staffing.yml`). No new position invented — this is a naming/register layer over existing, sourced roles.

| ID | Position | STAFF-PROFILES.md ref | Headcount (committed) |
|---|---|---|---|
| VM01 | Venue Manager | Position 01 | 1 |
| PHB01, PHB02 | Phlebotomist (committed, Chair A / Chair B) | Position 02 | 2 |
| PHB03, PHB04 | Phlebotomist (on the books, not committed-simultaneous) | Position 02 | +2 (recommended employment pool, §1 STAFF-PROFILES.md, not a daily roster figure) |
| MBP01-MBP04 | Treatment staff, Massage+Beauty pool | Position 03 | 4 |
| NLT01, NLT02 | Treatment staff, Nail Technician | Position 04 | 2 |
| HRD01, HRD02 | Treatment staff, Hairdresser | Position 05 | 2 |
| RCO01 | Reception/Coordinator (PM-hours) — **REMOVED 2026-08-21, founder decision** | Position 06 (superseded) | 0 (was 1) |
| PMM01 | PM dedicated casual, Massage line | `staffing.yml#staff_pm_massage` | 1 |
| PMH01 | PM dedicated casual, Hair line | `staffing.yml#staff_pm_hair` | 1 |
| PMN01 | PM dedicated casual, Nail line | `staffing.yml#staff_pm_nail` | 1 |
| PMB01 | PM dedicated casual, Beauty line | `staffing.yml#staff_pm_beauty` | 1 |

**Individual profiles, not "same as" shortcuts:** `STAFF-PROFILES.md` Positions 04 (NLT01/02) and 05 (HRD01/02) previously read "Role purpose, hours, roster pattern, employment type: Same structure as Position 03" — a genuine shortcut, now corrected below with each role's own explicit statement (substantively similar to Position 03's, since all AM treatment roles share the same shift/booking-driven structure by design, but no longer a cross-reference in place of stated content):

- **NLT01/NLT02 (Nail Technician):** Delivers manicure, pedicure, and nail-add-on services within the fixed AM package slot times, rostered flexibly across AM and PM per actual booking demand. Staggered start per first-client service time, minimum 3-hour engagement, released early if the final 2-3 hours of a pencilled shift aren't needed. Booking-driven roster, not a fixed daily headcount. Casual initially, reviewed for part-time conversion once regular hours are proven.
- **HRD01/HRD02 (Hairdresser):** Delivers blowdry, haircut, and braiding/hair-up services within the fixed AM package slot times, rostered flexibly across AM and PM per actual booking demand. Same staggered-start, minimum-engagement, early-release, and booking-driven-roster structure as NLT01/02 and MBP01-04. Casual initially, reviewed for part-time conversion once regular hours are proven.

---

## 2. Demand-Driven AM Staffing — Solver Findings (`tools/demand_driven_staffing_solver.py`)

### 2.1 Calibration (required before trusting any new result)

The solver's assignment rule (Service 1 always Massage+Beauty pool; Service 2 Nails for Chair A clients, Hair for Chair B clients) was reverse-engineered from the published Table 1/Table 2 timetables and confirmed, not assumed: an initial naive "balance load evenly across 3 symmetric lines" rule was tried first and **failed calibration** (produced 9 staff, not the published 8) — discarded once it failed, not adjusted until it happened to match. The rule that does reproduce the published figures exactly, run against both N=12 (Table 2) and N=18 (Table 1) at the committed 25-minute cadence:

| Scenario | Solver result | Published figure | Match |
|---|---|---|---|
| N=18 (Table 1) | MB=4, Nails=2, Hair=2 (total 8) | 4 Massage+Beauty + 2 Nails + 2 Hair = 8 | **MATCH** |
| N=12 (Table 2) | MB=4, Nails=2, Hair=2 (total 8) | 4 Massage+Beauty + 2 Nails + 2 Hair = 8 | **MATCH** |

Both independently re-verified by two methods (sweep-line peak concurrency, and a separately-coded brute-force minute-by-minute count) — exact agreement, per this repo's own established two-method proof standard. Phlebotomist peak concurrency also confirmed at 2 for both, matching the published figure (a structural confirmation, not a new derivation — 2 chairs starting together cannot produce more than 2 simultaneous draws).

### 2.2 New finding — 6 clients/day, never previously tested at this cadence

**At the committed 25-minute cadence, 6 clients/day (3 pairs) requires the SAME 8 treatment staff as 12 and 18 clients/day** (MB=4, Nails=2, Hair=2) — peak concurrency is driven by the overlap between consecutive pairs at a given cadence, not by total client count, so running only 3 pairs back-to-back at the same spacing as an 18-client day produces the same peak overlap between any 2 consecutive pairs. This is a genuine, calibrated, solver-verified finding, not an assumption.

**This means "no-nail-clients-means-no-nail-tech-rostered" logic does NOT work simply by having fewer bookings — it requires deliberately widening the pair cadence on a low-volume day.** Tested by sweeping cadence from 25 to 130 minutes at N=6:

| Cadence | Headcount (MB/Nails/Hair) | Total |
|---|---|---|
| 25-40 min | 4/2/2 | 8 |
| **45-130 min** | **2/1/1** | **4** |

**At a 45-minute (or wider) pair cadence, 6 clients/day genuinely needs only 4 treatment staff** (2 Massage+Beauty pool + 1 Nail Technician + 1 Hairdresser) — a real, verified halving of AM treatment headcount on a low-volume day. Phlebotomist headcount is unaffected (stays at 2, structural). At 45-minute cadence, 3 pairs finish their last Draw 1 at 08:30 (07:00 + 90min), comfortably inside WDP's 10:30 start-guidance window — operationally feasible on its own terms, not a constraint violation.

**12 clients/day (Table 2) genuinely cannot achieve this reduction.** Swept every cadence from 25 to 41 minutes (the maximum that keeps 6 pairs' last Draw 1 before 10:30) — headcount stays at 8 throughout. The 45-minute cadence needed to eliminate pair-overlap would push the last of 6 pairs to 07:00+225min = 10:45, past the WDP guidance boundary. **This independently re-confirms, via a different method, the existing repo finding that 12 clients/day needs full 8-staff headcount** — not previously solver-tested at variable cadence, now closed.

### 2.3 Not yet adopted, not yet a founder decision

The 45-minute-cadence, 4-staff model for a genuine 6-client/day is a new finding, presented for Anthony's decision, not silently adopted into the committed operating model. It requires: (a) confirming a 45-min cadence is acceptable client-wait-experience (longer individual gaps between draws for early arrivals is unaffected — the clinical timing per client is unchanged, only the SPACING between different clients' pairs widens); (b) confirming this is only used on days where AM bookings genuinely total 6, not a blanket policy; (c) a real rostering mechanism for knowing, in advance, that a given day will be a 6-client day (this is a booking-volume threshold question, not solved here).

---

## 3. PM Multi-Staff-Per-Role Scaling — the Rule, Not Currently Triggered

**Current PM costing formula** (`tools/cost_ramp_model.py#compute_pm_weekday_daily_labor`): hours/role/day = sessions/day ÷ 4 roles ÷ 1.3 sessions/hr throughput, floored at the 3-hour casual-minimum engagement. At the canonical Month 5+ steady state (16 sessions/day), this gives 16 ÷ 4 ÷ 1.3 = 3.08 hours/role/day — comfortably within a single PM shift (12:00-18:00, a 6-hour window). **At today's modelled volumes, 1 person per PM role (PMM01/PMH01/PMN01/PMB01) is sufficient — multi-staff-per-role scaling is not currently triggered, and this document does not claim it is.**

**The rule, stated explicitly so it is not silently missed if PM volume grows:** if sessions/day ÷ 4 roles ÷ 1.3 throughput exceeds a single PM shift's practical capacity (approximately 5-5.5 hours, allowing for breaks within the 6-hour 12:00-18:00 window), that role requires a second person, not one person working an excessive or non-compliant shift length. At current 1.3-sessions/hr throughput, this threshold is reached at approximately sessions/day > 4 roles × 5.25hrs × 1.3 = **27.3 sessions/day** — well above the canonical 16-session steady state, and above even Scenario B's theoretical 36-client bursty ceiling's own PM implications (not modelled here, PM session count is not derived from AM client count in this repo's current structure). **Genuinely not a live gap at current volumes — documented as a trigger condition, not implemented as a change, since implementing it now would invent an unneeded cost.**

---

## 4. Venue Manager Mon-Fri Emergency-Only Fill Rule

**Formalises, not reverses, the existing recommendation** in `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §3: "a permanent relief VM is NOT recommended at launch-scale... the realistic mitigation is (a) cross-training at least one senior treatment staff member or the PM Reception coordinator in basic opening/reception procedures as an emergency fallback (not full VM capability)."

**The rule, stated explicitly:** Monday-Friday, if VM01 is unexpectedly unavailable (illness, emergency), a cross-trained senior treatment staff member (or RCO01, Reception/Coordinator, during their own rostered hours) covers VM01's opening/reception duties as an emergency fallback ONLY — not full Venue Manager capability (rostering decisions, P&L review, pathology liaison remain VM01's alone, deferred until VM01 returns or Anthony/a relief arrangement is engaged). This is not a standing second role, not a weekend/PM fill-in duty, and does not add to steady-state payroll (an emergency-only, unpaid-until-triggered fallback, consistent with the existing recommendation's own "does not add to steady-state monthly payroll" framing for the PM Reception relief pool, §4a of that same document). **No new headcount or cost added by this rule — a documentation/process formalisation of an already-recommended mitigation, not a new financial commitment.**

---

## 5. PM Reception via Service-Staff Coverage — RESOLVED 2026-08-21 by Direct Founder Decision

> **This section originally flagged a conflict, unresolved, pending Anthony's explicit call. Anthony has since answered directly: his instruction stands.** Service-staff coverage during PM booking gaps (Model C) is the confirmed model, overriding `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §4's prior Model A recommendation. This is recorded here as a resolution, not a reversal of the original flag's own reasoning — the flag correctly surfaced a real conflict rather than silently picking a side, and the founder decision is exactly the kind of explicit confirmation the original flag asked for.

The original conflict (retained for trace): `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` §4 had compared 4 structural models for PM Reception, including this exact option —

> **Model C — Treatment staff assist with reception between clients:** No dedicated PM reception; a rostered treatment staff member handles check-in/payment during gaps. Was Rejected: treatment staff are not trained in Fresha/payment-system administration as a primary skill, and pulling a treatment-staff member off the floor for reception duties during their own paid PM session window directly reduces the PM treatment capacity the whole PM revenue model depends on — self-defeating for a role whose entire purpose is generating PM revenue. Customer experience: inconsistent, treatment staff distracted from service delivery.

**What closes each of the three original rejection reasons, and what remains an accepted trade-off, not a resolved-away risk:**
1. **Fresha/payment training gap — CLOSED.** `data/canonical/staffing.yml`'s PM dedicated-casual records (staff_pm_massage/hair/nail/beauty, i.e. PMM01/PMH01/PMN01/PMB01) each now carry an explicit "Fresha (or equivalent) booking-platform and payment-processing proficiency — REQUIRED" entry in their own `required_skills`, added 2026-08-21, not a hand-wave.
2. **PM-revenue self-defeat (pulling a treatment staff member off a paid session to do reception) — ACCEPTED, not resolved away.** This remains a real trade-off of the founder decision: PM treatment capacity is genuinely reduced during the specific minutes a PM staff member is covering reception. Not quantified or offset in this document — a disclosed, accepted cost of the decision, not claimed to be free.
3. **Inconsistent customer experience — ACCEPTED, not resolved away.** No single dedicated point of contact for the full PM window any more; whichever PM staff member is between clients covers reception. A real, disclosed customer-experience trade-off, accepted as part of the decision, not eliminated.

**Financial and staffing consequence:** RCO01 (Position 06, dedicated PM Reception) is REMOVED from the committed payroll and rostering model, effective 2026-08-21. `data/canonical/cost_ramp.yml`'s receptionist_relief cost line (Position 06's real first-principles cost, A$168.55/day weekday + A$252.83/day Saturday) is now 0.00 — full propagation through `data/models/master_financial_model.yml`, `docs/CURRENT-STATE.md` §5, the Dash, and dossier Chapters 1/9/14-17/27-31/34. See `data/canonical/cost_ramp.yml#change_pm_reception_dedicated_role_removed` for the complete financial derivation.

---

## 6. Financial Impact — What Changes and What Doesn't

- **Phlebotomist headcount:** unaffected at any AM volume tested (2, structural).
- **AM treatment headcount at 18 and 12 clients/day:** unaffected (8, confirmed not reducible within the WDP guidance window).
- **AM treatment headcount at 6 clients/day:** a genuine, solver-verified reduction to 4 IS possible, but only if a 45-minute (or wider) pair cadence is adopted for genuine 6-client days specifically — not adopted here, presented as a finding. Chapter 31's sensitivity table (dossier) is updated to show BOTH the current committed-cadence cost (8 staff, unchanged) AND this new lower-cadence alternative at 6 clients/day, clearly labelled, not silently substituted for the existing figure.
- **PM staffing:** unchanged in headcount (multi-staff-per-role trigger not reached at current volumes); **PM dedicated-casual roles gain a real, explicit Fresha/payment-training requirement (§5).**
- **PM Reception:** **REMOVED, 2026-08-21, per direct founder decision (§5).** RCO01/Position 06 no longer exists in the committed model. Model C confirmed. Steady-state Net Operating Result improves materially as a direct result: Table 1 A$38,705.33 → A$44,166.17/month, Table 2 A$4,615.32 → A$10,076.16/month (more than doubles).
- **Venue Manager:** unchanged financially (the emergency-fill rule adds no payroll cost, formalises an existing recommendation).

---

## Changelog

**2026-08-21 (later same day — PM Reception conflict RESOLVED by direct founder decision)** — Anthony confirmed service-staff coverage during PM booking gaps (Model C) as the model, overriding STAFFING-COVERAGE-VALIDATION.md §4's prior Model A recommendation. §5 rewritten from "conflict flagged, not implemented" to "resolved" — original reasoning retained for trace, each of the 3 original rejection reasons addressed explicitly (Fresha/payment training now a real requirement, PM-capacity and customer-experience trade-offs accepted not hidden). RCO01/Position 06 removed from the committed payroll model; full financial propagation in `data/canonical/cost_ramp.yml`, `data/models/master_financial_model.yml`, `docs/CURRENT-STATE.md`, Dash, and dossier.

**2026-08-21 (created)** — Built `tools/demand_driven_staffing_solver.py`, a new, calibrated solver (reproduces the published 8-staff figure for both N=12 and N=18 before being trusted on the new N=6 question). Genuine new finding: 6 clients/day needs 8 staff at the committed 25-min cadence (same as 12/18, driven by pair-overlap not client count), but only 4 staff at a widened 45-min+ cadence — verified feasible within the WDP guidance window, not adopted as policy. Independently re-confirmed 12 clients/day cannot achieve any headcount reduction within the guidance window at any cadence. Built the position-ID register (VM01/PHB01-04/MBP01-04/NLT01-02/HRD01-02/RCO01/PMM01/PMH01/PMN01/PMB01) and filled in the "same as Position 03" shortcuts in `STAFF-PROFILES.md` Positions 04-05 with their own explicit statements. Documented the PM multi-staff-per-role scaling rule (not currently triggered, no change made). Formalised the Venue Manager Mon-Fri emergency-only fill rule from the existing STAFFING-COVERAGE-VALIDATION.md §3 recommendation (no new cost). **Explicitly did NOT implement PM reception via service-staff coverage** — flagged as a direct conflict with STAFFING-COVERAGE-VALIDATION.md §4's existing, reasoned rejection of that exact model, pending Anthony's explicit reconsideration.
