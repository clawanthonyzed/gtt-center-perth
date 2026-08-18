# PM Session/Transaction Capacity Reconciliation

**Date:** 2026-08-18 | **Purpose:** Resolve the PM package/revenue contradiction flagged in `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §3b, per Anthony's explicit Priority 1 instruction: determine how PM Refresh and PM Restore are actually delivered, compare the viable staffing models and their financial consequence, and only then propagate a resolved figure through the canonical model — not force a number to look better.

---

## 1. The Contradiction, Restated Precisely

`data/canonical/client_assumptions.yml#pm_steady_state_capacity` (16 sessions/day) was originally built for an individual-services-only PM revenue model (`docs/pm-staffing-roster.md`, "PM Revenue — Individual Services, A$95 avg/session, NOT packages"). Once `docs/architecture/PM-PACKAGES.md` introduced two real packages (PM Refresh, PM Restore) and a blended A$117 average transaction value, the revenue formula (`tools/revenue_ramp_model.py`) kept multiplying "16" directly by the new blended price — but a package transaction consumes MORE than one staff-session's worth of treatment-staff time. Counting a 2-session-consuming package as if it were 1 session overstates how many client transactions 16 sessions' worth of capacity can actually produce.

## 2. Research — How Are PM Refresh and PM Restore Actually Delivered?

**Question:** does each package need ONE dual-qualified therapist delivering both components, or TWO separate staff members?

**PM Refresh (Massage 45min + Mini facial 30min):**
- This venture's own AM staffing model ALREADY treats Massage and Beauty as ONE shared, dual-qualified pool (`docs/architecture/STAFF-PROFILES.md` Position 03: "Massage+Beauty pool... one role, not two, per the venue's common-pool staffing model"; `scenario-c-sync-timetables.md` confirms Massage+Beauty dual-qualification is real and load-bearing for the AM headcount math).
- Real Perth comparable research (already done, `docs/architecture/PM-PACKAGES.md` §2): Keturah Spa, Hidden Valley Eco Day Spa, and endota Spa Perth CBD all bundle massage with a facial/beauty component as a single continuous booking — none of the cited comparables' package descriptions imply a mid-booking staff handover.
- **Resolution: PM Refresh is delivered by ONE dual-qualified Massage+Beauty-pool therapist**, performing both the massage and the facial component sequentially for the same client, consistent with the venture's own existing common-pool design. This is a single continuous 75-minute booking occupying ONE person's time, not two people's.

**PM Restore (Gel manicure 45min + Blow-dry/styling 30min):**
- Nails and Hair are explicitly NOT confirmed as a dual-qualification pairing anywhere in this repo — `scenario-c-sync-timetables.md` §0.4 states directly: "Nails and Hair have no confirmed dual-qualification pairing, so each stays on its own line at its individually-checked peak."
- No comparable-business research or catalogue evidence suggests nail technicians and hairdressers are cross-trained in this market segment (they are genuinely distinct trade qualifications — Cert III Nail Technology vs. Cert III Hairdressing — with materially different skill sets, unlike Massage/Beauty which share more overlapping technique and product knowledge).
- **Resolution: PM Restore genuinely requires TWO different specialists** — a Nail Technician for the 45-minute manicure and a Hairdresser for the 30-minute blow-dry, run either concurrently (2 staff at once, if the room layout allows, `PM-PACKAGES.md` §6) or sequentially (1 client, 2 staff at different times) — either way, it consumes two separate people's time, not one.

**This is an asymmetric finding, not a blanket "packages = 2 sessions" rule** — the two packages behave differently because the underlying qualification-pairing reality differs between Massage+Beauty (real, established, load-bearing pairing) and Nails+Hair (explicitly no confirmed pairing).

## 3. Comparison of Viable Staffing/Capacity Models, With Financial Consequence Shown for Each

| Model | Description | PM weekday transaction capacity | PM revenue/month | vs. current (16-session) model |
|---|---|---|---|---|
| **A — Current (unresolved) model** | 16 "sessions" = 16 transactions, regardless of package staffing reality | 16.00/day | A$45,236.88 | baseline — known to be wrong, retained only for comparison |
| **B — All packages = 2 sessions (conservative, session-count method)** | Every package (both Refresh and Restore) treated as consuming 2 staff-sessions, ignoring the Massage+Beauty dual-qualification finding | 11.43/day | ≈A$32,004 (session-count method) | -29.2% — over-corrects, ignores real evidence that Refresh needs only 1 person |
| **C — Researched, asymmetric, staff-minutes method (RECOMMENDED, adopted below)** | PM Refresh = 1 dual-qualified therapist (75min, 1 person); PM Restore = 2 specialists (75 total staff-minutes, 2 people); staff-minutes capacity model (739.2 min/day weekday) | 12.8128/day | A$36,215.12 | -19.9% |
| **D — No correction, keep A$117 x 16** | Ignore the finding entirely | 16.00/day | A$45,236.88 | 0% — not defensible once the underlying staffing reality is known |

**Model C is adopted** as the best-evidenced resolution — it is the only model that reflects the ACTUAL researched staffing pattern for each package individually, rather than either ignoring the problem (Model D) or over-correcting with an undifferentiated assumption (Model B).

## 4. Full Calculation, Model C

**Capacity basis:** 4 treatment lines (Massage, Beauty, Nails, Hair) share the PM window. Weekday total staff-minutes available = 4 roles × 3.08hrs/role (the existing, unchanged labour-hours figure from `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §3e) × 60 = **739.2 minutes/day**. This figure is UNCHANGED by this reconciliation — it is the same total labour-hours capacity the payroll model already correctly pays for; only how many CLIENT TRANSACTIONS that capacity converts into is being corrected here.

**Weighted minutes-per-transaction**, using the disclosed 60% individual / 25% PM Refresh / 15% PM Restore mix:

| Transaction type | Share | Minutes consumed | Weighted contribution |
|---|---|---|---|
| Individual a-la-carte | 60% | 46.15 (60÷1.3, existing throughput assumption) | 27.69 |
| PM Refresh (1 therapist, 75min) | 25% | 75 | 18.75 |
| PM Restore (2 specialists, 75 total staff-min) | 15% | 75 | 11.25 |
| **Weighted average** | | | **57.69 min/transaction** |

**Weekday transaction capacity:** 739.2 ÷ 57.69 = **12.8128 transactions/day** (was 16 under the uncorrected model).

**Saturday:** Saturday demand is preserved at the ORIGINAL 50% ratio to weekday (`rev_pm_saturday_sessions` = 8, exactly half of weekday's 16 staff-session figure) — **not** re-derived from Saturday's own PAID labour capacity, because that paid capacity is inflated by the 3-hour casual-minimum-engagement floor (a cost mechanism reflecting low Saturday demand, not evidence that Saturday demand doubles). Saturday transaction capacity = 12.8128 × 0.5 = **6.4064 transactions/day**.

**Revenue, using the SAME A$116.97 blended average transaction value** (the average itself is unaffected by this correction — only the daily transaction COUNT was wrong, not the per-transaction price):

| | Transactions/day | Revenue/day | Days/month | Revenue/month |
|---|---|---|---|---|
| Weekday | 12.8128 | A$1,498.66 | 22 | A$32,970.52 |
| Saturday | 6.4064 | A$749.33 | 4.33 | A$3,244.60 |
| **TOTAL** | | | | **A$36,215.12** |

**Compared to the current (uncorrected) canonical figure:** A$45,236.88/month → **A$36,215.12/month**, a decrease of **A$9,021.76/month (-19.9%)**.

## 5. What This Changes and What It Doesn't

**Changes:** PM revenue only (`data/canonical/revenue_ramp.yml`, `data/models/master_financial_model.yml`, `docs/CURRENT-STATE.md` — full propagation in the same commit as this document).

**Does NOT change:** PM labour cost. The payroll model already correctly pays for 4 roles × 3.08hrs/role weekday (and the 3-hour floor Saturday) — the SAME staff-minutes capacity used in this reconciliation's own §4 calculation. `pm_steady_state_capacity` (16, `client_assumptions.yml`) and `rev_pm_saturday_sessions` (8) remain unchanged and continue to correctly drive the labour-hours formula in `tools/cost_ramp_model.py` — only their reuse as a REVENUE multiplier is corrected, via the new `rev_pm_weekday_transactions`/`rev_pm_saturday_transactions` records.

## 6. Remaining Disclosed Uncertainty

The individual-service average duration used above (46.15 minutes) is inherited from the existing throughput assumption (`docs/pm-staffing-roster.md`'s "1.3 sessions/hr"), not independently re-verified against the actual weighted-average duration of the 9 specific catalogue services used to build the A$84.11 individual-transaction average price. If those 9 services' real average duration differs materially from 46.15 minutes, this reconciliation's precise numbers would shift somewhat (though the DIRECTION of the correction — PM revenue was overstated — would not change, since it stems from the package-session-consumption finding, not the individual-service duration figure). Flagged as a bounded, disclosed limitation, not claimed as final precision.

## 7. Whether Package Delivery Should Be Concurrent or Sequential (Nails+Hair) — Still Genuinely Open

`docs/architecture/PM-PACKAGES.md` §6 already flagged this as undecided ("whether Package B's two services should run concurrently... or sequentially... an operational decision for later"). This reconciliation does NOT depend on resolving that specific question — either way, PM Restore consumes 75 total staff-minutes split across 2 different specialists (Nails + Hair), which is what the capacity model above already assumes. The concurrent-vs-sequential choice affects room/scheduling logistics and how quickly a single PM Restore client can be served end-to-end, not the total staff-minutes consumed — so it does not change this document's revenue conclusion, though it remains a real open operational decision for the eventual Venue Manager.

---

## Changelog

**2026-08-18** — Created per Anthony's explicit Priority 1 instruction, resolving the PM session/transaction contradiction flagged in `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §3b. Researched the actual staffing pattern for each package (PM Refresh = 1 dual-qualified therapist per the existing Massage+Beauty common-pool design; PM Restore = 2 specialists, no confirmed Nails+Hair pairing) rather than assuming a blanket rule. Compared 4 viable models with their financial consequence shown for each; adopted the researched, asymmetric, staff-minutes-based model (Model C) as best-evidenced. New PM revenue: A$36,215.12/month (was A$45,236.88, a genuine 19.9% decrease from correcting a real capacity-counting error, not from making the numbers look worse for its own sake).
