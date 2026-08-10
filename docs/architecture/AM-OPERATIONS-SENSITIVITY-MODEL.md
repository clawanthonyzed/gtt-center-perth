# AM Operations Sensitivity Model — 1-18 Clients/Day

**Phase:** Commercial Assumption Alignment & External Readiness, focus area 1 of 4 — investigation and optimisation only. **No financial model file was modified.** Every figure below is derived from already-canonical data (`data/canonical/staffing.yml`, `wages.yml`, `pricing.yml`, `client_assumptions.yml`, `cost_ramp.yml`) — no new operational assumption (headcount, cadence, or schedule) was invented. Where the canonical data does not extend to a given volume, that gap is stated explicitly, not filled with an invented figure.

**Date:** 2026-08-10

---

## 1. What Is Already Canonical (the only solid ground)

- **AM weekday treatment + phlebotomist labour is a genuinely FIXED monthly cost across the entire committed 12–18 client/day range** — confirmed directly from `data/canonical/cost_ramp.yml`: `am_weekday_direct_labor` is **identically A$48,254.67/month** in both `cost_table1_m5plus` (18/day) and `cost_table2_m5plus` (12/day) records. This is not an assumption of this document — it is the canonical figure, and it is flat because headcount (8 dual-qualified treatment staff + 2 phlebotomists) is solver-verified identical at both volumes (`data/canonical/staffing.yml`).
- **AM Saturday labour scales linearly with committed volume** — the one payroll component that genuinely differs between Table 1 and Table 2: A$10,474.75/month at 18/day vs. A$6,983.16/month at 12/day. Dividing through by `operating_saturdays_per_month` (4.33) and client volume, both figures resolve to an **identical A$134.395/client/Saturday-day rate** — confirming this component is priced per-client, not per-headcount-block, in this venture's own canonical data.
- **No canonical schedule-solver result exists anywhere in this repository for any volume below 12 or above 18.** The two committed points (12, 18) are both independently solver-verified (sweep-line peak concurrency + greedy first-fit, exact agreement, per `staffing.yml`'s own notes). Below 12, the only reference point is a historical, **unverified** finding: `staffing.yml#staff_treatment_massage_beauty_pool` discloses that a 7-staff option (Massage+Beauty pool capped at 3, not 4) "was found valid at the historical 12-client/23-min-cadence model... NOT independently re-verified against Table 1/Table 2's 25-min cadence." This document uses that figure as a disclosed, flagged alternative — not a new solver result.

---

## 2. Sensitivity Table — AM Segment Only (Revenue, Direct Labour, Contribution)

**Methodology, fully disclosed:** AM Revenue = client volume × A$250 (`am_price_used_for_revenue`) × 26.33 operating days/month (22 weekday + 4.33 Saturday, both canonical). AM Direct Labour = the fixed A$41,076.67/month treatment-staff component (already includes superannuation, per the item 46 resolution) + the fixed A$7,178.00/month phlebotomist component (superannuation added at 12%, per the same resolution) + the linear Saturday component (A$134.395/client/Saturday-day) + superannuation on the phlebotomist and Saturday components + Workers Compensation (1.7%, applied to the AM labour subtotal only, an approximation for this AM-segment-only view — the canonical figure applies it to a broader subtotal including PM/opening/receptionist costs, not isolated by segment anywhere in this repo). **This AM-segment contribution figure is NOT the whole-venture Net Operating Result** — PM revenue/costs and fixed operating expenses sit on top, unaffected by AM volume (see §4).

**Primary case — full committed 8+2 headcount, held constant (the only solver-confirmed structure):**

| Volume/day | AM Revenue (mo) | AM Direct Labour (mo) | AM Contribution (mo) | Contribution Margin |
|---|---|---|---|---|
| 1 | A$6,582.50 | A$50,613.84 | -A$44,031.34 | negative |
| 2 | A$13,165.00 | A$51,276.69 | -A$38,111.69 | negative |
| 4 | A$26,330.00 | A$52,602.37 | -A$26,272.37 | negative |
| 6 | A$39,495.00 | A$53,928.05 | -A$14,433.05 | negative |
| **8** | A$52,660.00 | A$55,253.74 | **-A$2,593.74** | -4.9% |
| **9** | A$59,242.50 | A$55,916.58 | **+A$3,325.92** | +5.6% |
| 10 | A$65,825.00 | A$56,579.42 | +A$9,245.58 | +14.0% |
| 12 (Table 2, committed) | A$78,990.00 | A$57,905.10 | +A$21,084.90 | +26.7% |
| 14 | A$92,155.00 | A$59,230.79 | +A$32,924.21 | +35.7% |
| 16 | A$105,320.00 | A$60,556.47 | +A$44,763.53 | +42.5% |
| 18 (Table 1, committed) | A$118,485.00 | A$61,882.16 | +A$56,602.84 | +47.8% |

**AM-segment break-even (8+2 headcount, full committed structure): between 8 and 9 clients/day** — the AM segment alone (before PM revenue and fixed opex are added) crosses from loss to contribution at approximately **8.4 clients/day**.

**Alternative case — unverified 7-staff option (Massage+Beauty pool capped at 3):** using the already-disclosed ~A$5,231/month treatment-labour saving (`docs/VERIFICATION-TRACKER.md` item 12), the same break-even point shifts to approximately **7.2 clients/day** (crossing between 7 and 8). **This alternative is flagged, not adopted** — it has never been re-verified against the current 25-min cadence.

---

## 3. Rooms and Stations — A Different Question From Staffing

Physical rooms/stations do not vary with daily client volume — they are a one-time fit-out decision, not a daily operating decision. The current committed build (per `docs/architecture/MVP-OPENING-DECISION-REVIEW.md` §4.3) opens with 2 of 4 possible nail stations and 2 of 4 possible hair chairs staffed/equipped, with the remaining 2 of each purchased by Month 4 (tied to the PM revenue ramp reaching 93%+ of steady state — see `docs/architecture/PM-OPERATIONS-MODEL.md`). **What varies with AM client volume is which built stations are actively staffed, not how many exist** — and per `staffing.yml`'s own solver-verified finding, peak concurrent AM demand for both Nails and Hair is exactly 2 technicians at both 12 and 18 clients/day, meaning the AM segment specifically never requires more than the 2-of-4 staged stations across the entire committed range.

---

## 4. Are the 43/64/79/93/100% Ramp Assumptions Operationally Realistic?

**No — not without qualification, and this is the single most important finding of this document.** The revenue ramp assumes AM revenue climbs smoothly (43% → 100% of steady state over 4 months). AM Direct Labour does not ramp at all — `data/canonical/cost_ramp.yml`'s own disclosed `conflict_am_labor_ramp_unmodelled` confirms it is "FIXED at the scenario's committed level throughout." Combining the two, already-canonical figures:

- **Table 1, Month 1:** implied AM revenue ≈A$50,948.55/month (43% of A$118,485.00, per `docs/architecture/REVENUE-RAMP-METHODOLOGY.md` §7) — against the fixed A$48,254.67/month weekday-only labour figure, **before** Saturday labour, superannuation, Workers Comp, PM costs, or fixed opex are even added. Cross-checked against §2's own sensitivity table: Month 1's implied ≈7.74 clients/day sits almost exactly at the computed AM-segment break-even band (8–9 clients/day) — the two independent figures corroborate each other closely.

**This means the revenue ramp's own Month 1–2 figures are structurally tighter than the "43%/64% of steady state" framing alone suggests.** The ramp curve describes revenue building smoothly; it does not describe cost holding flat while revenue builds under it — both facts are already disclosed separately in this repo (items 41/42/43), but this document is the first to show precisely where they intersect on a client-volume axis. This is consistent with, not a contradiction of, the already-known Month 1 operating-cash trough (Table 1: -A$30,885.75).

---

## 5. Risks Identified

- **No solver-verified schedule exists below 12 clients/day.** Every figure in §2 for volumes 1–11 assumes the full 8+2 headcount structure holds unchanged down to 1 client/day — a real, disclosed inference, not a confirmed operational fact. If a genuinely different (cheaper) staffing structure is feasible at low volume, this document cannot quantify it without a new scheduling-solver run.
- **The 7-staff alternative is unverified for the current cadence.** It remains attractive on paper (moves break-even from ~8.4 to ~7.2 clients/day) but was only confirmed valid under the superseded 23-minute cadence.
- **The ramp curve's own cost-side blind spot compounds a known revenue-side uncertainty.** Item 41/42 already flag that the ramp curve's origin is undocumented; this document adds that even if the ramp curve is accurate on the revenue side, the AM segment's true early-month margin is thinner than the ramp percentage alone implies, because labour cost does not ramp with it.

## 6. Recommended Next Decisions

1. **Commission a scheduling-solver run for the 1–11 client/day range under the current 25-min cadence** — the single highest-value piece of analytical work this document identifies. It would resolve both the true minimum-viable-opening volume and re-verify (or reject) the 7-staff alternative under the cadence this venture actually uses.
2. **Treat Months 1–2 of any real trading period as the highest cash-risk window**, consistent with both this document's AM-segment break-even analysis and the already-known operating-cash trough — not a new finding, but now corroborated by an independent method.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. Every figure is either quoted directly from `data/canonical/*.yml` or computed transparently from those figures using formulas already established in this repository's own methodology documents (see full validation summary in this phase's combined report-back).
