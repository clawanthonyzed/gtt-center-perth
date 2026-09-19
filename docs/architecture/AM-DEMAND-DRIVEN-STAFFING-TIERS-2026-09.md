# AM Demand-Driven Staffing Tiers — Solver-Verified Headcount at 5 Client Volumes

**Date:** 2026-09-19 | **Purpose:** Replace the flat "always 8 treatment staff regardless of AM client volume" assumption in the profitability ladder, per Anthony's direct instruction: *"SOLENA may employ a full staff pool capable of supporting the maximum operating capacity. However, staff are not all rostered every day. The roster flexes according to client demand... Do not use a flat 8 service staff every day assumption across every client-volume scenario."*

---

## 1. Method

`tools/am_volume_tier_staffing_solver.py` extends the already-published, calibrated concurrency solver (`tools/demand_driven_staffing_solver.py`) in two ways:

1. **Odd client-count support.** The original solver only builds even-numbered synchronized pairs (Chair A + Chair B together). A real day's booking count can be odd — the extension lets the final pair-slot use only Chair A, consistent with this repo's own already-established Chair B enquiry-threshold policy (`docs/CURRENT-STATE.md` §1), not an invented mechanic.
2. **Cadence sweep per volume tier.** For each target AM volume, the tool rounds up to the nearest whole client count (you cannot roster a fractional client), then sweeps pair cadence from the committed 25 minutes up to the widest cadence that still clears the WDP guidance window (last Draw 1 no later than 10:30am, i.e. no more than 210 minutes after a 07:00 start), and reports the cadence/headcount combination that achieves the minimum headcount at the smallest (tightest) cadence.

**Calibration, not a fresh assumption:** the extension is run first against N=12 and N=18 at 25-minute cadence and must reproduce the already-published 8-staff figure (4 Massage+Beauty + 2 Nails + 2 Hair) before its output on the new tiers is trusted — confirmed exactly, see `tests/test_am_volume_tier_staffing_solver.py`.

---

## 2. Target Volumes and Solver Output

Anthony's own 5 profitability-ladder points: 9.00, 11.29, 13.50, 15.50, 18.00 AM clients/day.

| Target volume/day | Rostered for (ceiling) | Pair-slots | Max feasible cadence (WDP window) | Chosen cadence | Treatment headcount | Last Draw 1 | Last departure |
|---|---|---|---|---|---|---|---|
| 9.00 | 9 | 5 | 50min | **45min** | **4 (2 MB + 1 Nail + 1 Hair)** | 10:00 | 11:55 |
| 11.29 | 12 | 6 | 40min | 25min | **8 (4 MB + 2 Nails + 2 Hair)** | 09:05 | 11:00 |
| 13.50 | 14 | 7 | 35min | 25min | **8 (4 MB + 2 Nails + 2 Hair)** | 09:30 | 11:25 |
| 15.50 | 16 | 8 | 30min | 25min | **8 (4 MB + 2 Nails + 2 Hair)** | 09:55 | 11:50 |
| 18.00 | 18 | 9 | 25min | 25min | **8 (4 MB + 2 Nails + 2 Hair)** | 10:20 | 12:15 |

**Phlebotomist headcount is unaffected at every tier tested — 2 (structural, 2 collection chairs, cannot be reduced within this synchronized-pair model regardless of client volume).**

---

## 3. Why Only the Lowest Tier Reduces

The mathematics: with `n_pairs` pair-slots and a cadence `c`, headcount reduction to 4 (from the existing, already-published N=6 finding) requires a cadence of 45 minutes or more. The WDP guidance window constrains `(n_pairs - 1) × c ≤ 210`. Solving for the maximum `n_pairs` that still permits `c = 45`: `n_pairs ≤ 210/45 + 1 = 5.67`, i.e. **at most 5 pair-slots (10 clients)** can reach the widened cadence within the guidance window. 9.00/day (5 pair-slots, one single-chair) clears this; 11.29/day (6 pair-slots, since ceil(11.29/2)=6) does not — its own maximum feasible cadence is only 40 minutes, below the 45-minute threshold the headcount reduction requires. This is not a modelling artefact — it is a direct, disclosed mathematical consequence of pairing two clients per synchronized slot and the fixed 60/120-minute clinical marks each client's own test requires.

**This finding is presented, not adopted as policy** — same status as the already-published N=6 finding (`docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md` §2.2-2.3). Adopting the 45-minute cadence for genuinely low-volume days requires: (a) confirming a 45-minute pair spacing is acceptable client-wait experience (the per-client clinical timing is unaffected — only the SPACING between different clients' pairs widens); (b) a real day-ahead rostering mechanism to know a given day will be a 9-or-fewer-client day; (c) Anthony's explicit sign-off. None of these is resolved here.

---

## 4. Financial Ladder

`tools/am_demand_tier_financial_ladder.py` combines the headcount above with `tools/cost_ramp_model.py`'s canonical wage rates (unchanged rates, just parameterized by headcount via the new `am_treatment_monthly_for_headcount` function) and the new PM Model E revenue figure (`docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md`, fixed regardless of AM tier). Full table: `docs/CURRENT-STATE.md` §10.

**Headline finding:** the HIGH-headcount tier's own total operating cost (A$107,883.97/month) is calibrated to match `data/canonical/cost_ramp.yml`'s Table 1 M5plus record exactly (both sourced from the same underlying constants) — confirmed by `tests/test_am_demand_tier_financial_ladder.py`, not a second, independently-diverging calculation.

---

## 5. Break-Even, Recomputed

Because cost is now a genuine step function of AM volume (not a single fixed committed-model figure), break-even is not a single number — it is segment-specific:

- **LOW segment (4-staff, 45-minute cadence, valid for volumes up to ~10/day):** break-even = **8.266 clients/day**.
- **HIGH segment (8-staff, 25-minute cadence, the standing committed model, valid for volumes from ~11/day upward):** break-even = **12.655 clients/day**.

**The pre-rebuild 11.290 clients/day break-even figure is now stale** — it predates both the demand-driven staffing rebuild and the PM/Venue Manager recompute, and does not correspond to either segment's own genuine break-even under the current model. Do not quote it.

**Which to present:** the HIGH-segment figure (12.655/day) is the correct "the break-even" figure under the currently-committed operating model, since demand-flexed low-volume staffing (the LOW segment) is not yet a founder decision. Both are shown, clearly labelled, rather than blended into one misleading number.

---

## Changelog

**2026-09-19** — Created per Anthony's direct instruction to rebuild the profitability ladder with genuine demand-driven staffing instead of a flat 8-staff assumption at every volume. Extended the existing calibrated solver to odd client counts and cadence sweeps (`tools/am_volume_tier_staffing_solver.py`, `tests/test_am_volume_tier_staffing_solver.py`), built the combined financial ladder tool (`tools/am_demand_tier_financial_ladder.py`, `tests/test_am_demand_tier_financial_ladder.py`), and propagated the recomputed break-even and profitability ladder into `docs/CURRENT-STATE.md` §10.
