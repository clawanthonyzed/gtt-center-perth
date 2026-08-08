# GTT Center Perth — Model Architecture

**Purpose:** define the future architecture of Layer 3 (MODELS, see `TARGET-ARCHITECTURE.md`) — the calculation logic that turns `data/canonical/*.yml` facts into derived figures. **No model is built this phase.** This document specifies what each model consumes, what it produces, and which existing document/script is its prior art.

**Standing rule for every model described below:** a model reads Layer 2 (`data/canonical/*.yml`) and other models' outputs — it never hardcodes a fact that could instead be a canonical reference, and it never reads Layer 1 (source evidence) directly. See `TARGET-ARCHITECTURE.md` §1.

---

## 1. Master Financial Model (`models/financial/`)

### Purpose
Turn pricing/volume/staffing/cost assumptions into P&L, cash flow, balance sheet, break-even, and unit-economics outputs — replacing the currently hand-calculated figures spread across `docs/profit-loss-tables.md`, `docs/cash-flow.md`, `docs/break-even-sensitivity-analysis.md`, `docs/unit-economics.md`, `docs/financial-break-even-staff.md`.

### Modules and Data Flow

```
assumptions (data/canonical/*.yml)
   |
   v
services + pricing  ---->  revenue
                                |
client_assumptions (volume) ---+
                                v
staffing + wages  ---->  payroll  ---->  COGS
                                            |
opex  ------------------------------------>|
                                            v
                                          P&L  ---->  cash flow  ---->  balance sheet
                                            |
                          startup_costs + capex  ---->  funding requirement
                                            |
                                            v
                                   break-even + unit economics
                                            |
                                            v
                          scenarios (alternate assumption sets through the same engine)
                                            |
                                            v
                              sensitivity (parametrized sweep over 1+ assumptions)
                                            |
                                            v
                                        KPIs + model checks
```

| Module | Consumes (from `data/canonical/`) | Produces | Prior art in this repo |
|---|---|---|---|
| **Assumptions** | All domain files, read-only | A single resolved assumption set per model run (with each field's status carried through) | `docs/CURRENT-STATE.md` header/tagging convention |
| **Services + Pricing** | `services.yml`, `pricing.yml` | Per-service/package revenue-per-unit | `docs/services-master-table.md`, `docs/services-pricing-locked.md` |
| **Client Volume** | `client_assumptions.yml`, `scenarios.yml` | Daily/weekly/monthly visit counts by AM/PM/Saturday | `docs/CURRENT-STATE.md` §3, `docs/scenario-comparison-master-2026-08.md` |
| **Revenue** | Pricing × Volume | Revenue by line (AM package, PM à la carte, PM packages, ancillary) | `docs/profit-loss-tables.md`, `docs/cash-flow.md` |
| **COGS** | Direct per-visit costs (if any — currently none identified beyond labor) | COGS line | Not currently separately modelled in this repo — flagged as a gap; today's docs fold direct labor into "Direct Labor" rather than a distinct COGS line |
| **Staffing** | `staffing.yml`, `scheduling_assumptions.yml`, `clinical_timing.yml` | Headcount by role, by scenario/volume | `docs/staff-plan.md`, output of `models/operations/` (see §2) |
| **Payroll** | `wages.yml` × Staffing headcount | Payroll cost by role, by day-type (weekday/Saturday) | `docs/financial-break-even-staff.md`, `docs/CURRENT-STATE.md` §5 |
| **Opex** | `opex.yml` | Non-wage overhead line items | `docs/CURRENT-STATE.md` §5, `docs/rent-budget-2026-07-28.md` |
| **Startup Costs / Capex** | `startup_costs.yml`, `capex.yml` | Funding requirement range | `docs/CURRENT-STATE.md` §6/§7, `docs/equipment-costs.md`, `docs/floor-plan-concept.md` |
| **P&L** | Revenue − COGS − Payroll − Opex | Monthly/quarterly/half-yearly/yearly P&L | `docs/profit-loss-tables.md`, `docs/CURRENT-STATE.md` §5 |
| **Cash Flow** | P&L + startup-cost timing + capex timing | Monthly cash position, funding drawdown schedule | `docs/cash-flow.md` |
| **Balance Sheet** | Cash flow + capex + funding | Balance sheet snapshot | Not currently built anywhere in this repo — flagged as a genuine gap, no prior art |
| **Break-Even** | P&L structure (fixed vs variable costs) | Break-even client volume / revenue | `docs/break-even-sensitivity-analysis.md`, `docs/VERIFICATION-TRACKER.md` item 1d-be (phlebotomist-only break-even, a worked micro-example of exactly this kind of calculation) |
| **Unit Economics** | Revenue + COGS + Payroll per visit | Revenue/cost/margin per visit | `docs/unit-economics.md` |
| **Scenarios** | Alternate `client_assumptions.yml`/`scenarios.yml` selections run through the same modules above | A named, tagged, side-by-side output set (never blended into the base case) | Table 1 vs Table 2, Scenario D — currently computed as separate one-off passes rather than one engine run twice |
| **Sensitivity** | A parametrized sweep of one or more assumption fields (e.g. utilisation %, price) | A range/table of outcomes | `docs/break-even-sensitivity-analysis.md`'s best/base/worst structure — currently manual, not a parametrized sweep |
| **Funding** | Startup costs + cash-flow trough | Capital-raise requirement, timing | `docs/CURRENT-STATE.md` §6/§7, `docs/revenue-extraction-options.md` |
| **KPIs** | Selected outputs from the above (revenue/visit, margin %, break-even distance) | A small tracked set for `dashboards/` | Not currently built — flagged as a gap; `docs/CURRENT-STATE.md` implicitly tracks some of these in prose |
| **Model Checks** | Internal reconciliation between modules | Pass/fail + discrepancy report | `docs/profit-loss-tables.md`'s own disclosed Appendix gap (a ~A$2,576 weekly-to-monthly scaling artifact, present since 2026-07-30, explicitly disclosed rather than hidden) — this is a real example of exactly the kind of check this module should catch automatically going forward |

### A Concrete Example of the Gap This Closes
`docs/CURRENT-STATE.md` §5 discloses: *"a first-principles revenue sum lands ~A$2,576 below the delta-built A$157,792.16 figure — the same fixed-size weekly-to-monthly scaling artifact already flagged ... present identically at the 10-client and 12-client stages too."* This is a real, currently-manual reconciliation the venture has caught and disclosed three times by hand across three model revisions. A Model Checks module (§ above, detailed further in `VALIDATION-ARCHITECTURE.md`) is the architectural fix — it would flag this class of discrepancy automatically on every model run, not rely on a human noticing it again at the next rebase.

---

## 2. Master Operations Model (`models/operations/`)

### Purpose
Turn operating-hours/scheduling/clinical-timing assumptions into capacity, timetable, and roster-requirement outputs — replacing the currently one-off, hardcoded-per-scenario `tools/*.py` scripts.

### Modules and Data Flow

```
operating_hours + scheduling_assumptions + clinical_timing (data/canonical/*.yml)
   |
   v
client timetable (per-client draw/service events)
   |
   +--> chair/room allocation (feasibility check: any double-booking?)
   |
   +--> staff allocation (sweep-line peak concurrency + greedy first-fit, both methods)
   |         |
   |         v
   |     roster requirement (by role, by day-type)
   |
   v
combined timetable (client + staff + chair, one view)
   |
   v
capacity (max clients/day under given constraints)
   |
   v
utilisation + bottleneck analysis
```

| Module | Consumes | Produces | Prior art |
|---|---|---|---|
| **Operating Hours** | `operating_hours.yml` | Trading calendar | `docs/CURRENT-STATE.md` §1 |
| **Client Timetable** | `scheduling_assumptions.yml`, `clinical_timing.yml` | Per-client draw/service event list | `docs/scenario-c-sync-timetables.md`, `tools/draw-event-scheduler.py` |
| **GTT Timing** | `clinical_timing.yml` | Draw 1/2/3 marks, service-block windows | `docs/gtt-clinical-protocol.md`, `docs/CURRENT-STATE.md` §1 |
| **Chair/Room Allocation** | `facilities.yml` + client timetable | Zero-collision check per chair/phlebotomist | `tools/sync-treatment-solver.py` |
| **Service/Staff Allocation** | `services.yml` + client timetable | Peak concurrency per staff category (sweep-line + greedy first-fit, **both required**, per this repo's own established double-verification convention) | `tools/multirole-analysis.py`, `tools/scenario-d-staff-solver.py` |
| **Roster** | Staff allocation output + `staffing.yml` | Required headcount by role, by day-type | `docs/staff-plan.md`, `docs/am-staffing-by-volume.md` |
| **Combined Timetable** | Client timetable + roster | A single client+staff+chair view | `docs/scenario-c-sync-timeline.html` (hand-built prior art — target state: generated from this module, see `DOCUMENT-GENERATION.md`) |
| **Capacity** | Full sweep across candidate volumes/start-times, bounded by `scheduling_assumptions.yml` constraints (e.g. WDP's 10:30am guidance) | Maximum feasible client count | `tools/draw-event-scheduler.py`'s `run()` multi-resolution sweep |
| **Utilisation** | Capacity output vs. actual/assumed booking volume | % utilisation | Not currently modelled — flagged as a gap (no real booking data exists yet, per `docs/CURRENT-STATE.md` throughout) |
| **Bottleneck Analysis** | Peak-concurrency output across all resource types (chairs, phlebotomists, each staff category) | Which resource binds capacity first | Implicit in `docs/CURRENT-STATE.md` §1's headcount findings (e.g. the Massage+Beauty pool's peak-concurrency-of-4 finding) — not yet a standalone, reusable module |

### The Core Refactor This Requires
Every one of the six `tools/*.py` scripts (see `REPOSITORY-AUDIT.md` §4) hardcodes its own scenario's `clients_x`/`chair_of`/`slots` data as an in-file dict. The target architecture requires these become **functions that accept a scenario definition** (start time, client count, cadence, chair count) as a parameter, sourced from `data/canonical/scenarios.yml`, so that re-running the same rigorous two-method verification against a new scenario (as happened four times already: 10→12→14→18 clients) becomes "run the existing function with new inputs" rather than "write a new script." **This refactor is not done this phase** — it is the concrete first implementation task the target architecture is designed to enable.

---

## 3. Staffing Model (`models/staffing/`)

### Purpose
Turn positions/skills/availability assumptions into FTE requirements, payroll costs, and rostering rules — feeding both the Financial Model (§1, payroll) and the Operations Model (§2, roster requirement) rather than duplicating logic in both.

### Modules

| Module | Consumes | Produces | Prior art |
|---|---|---|---|
| **Positions** | `staffing.yml` | Role catalogue (Venue Manager, Phlebotomist, Treatment Staff, Receptionist, PM Casual) | `docs/staff-plan.md` |
| **FTE Requirements** | Operations Model's roster-requirement output (§2) | Headcount by role, by scenario | `docs/CURRENT-STATE.md` §4 |
| **Hourly Rates** | `wages.yml` | Rate per role, including award/casual-loading references | `docs/financial-break-even-staff.md`, `docs/hr-framework.md` |
| **Payroll Costs** | FTE × Hourly Rates, with the 3-hour casual minimum rule applied | Payroll by role, by day-type | `docs/CURRENT-STATE.md` §5, `docs/VERIFICATION-TRACKER.md` item 1i (a real example of this exact rule being under- then correctly-applied — a genuine bug this model's rules would prevent recurring) |
| **Availability** | Not currently tracked anywhere in this repo (no real staff hired yet) | Roster-fit check once real hires exist | Flagged as a genuine future gap — no prior art, pre-hire venture |
| **Skills** | `staffing.yml` (dual-qualification pairings, e.g. Massage+Beauty) | Which pooling reductions are valid at which volume | `docs/multirole-CORRECTION.md`, `docs/dual-role-staffing-model-2026-07-28.md` |
| **Roster Requirements** | Operations Model peak-concurrency output | Minimum staff per category, per scenario | Shared output with Operations Model §2 — **this model does not recompute it, it consumes the same output**, avoiding the current risk of the two figures (a staffing-plan headcount and a scheduling-solver headcount) silently drifting apart |
| **Staffing-by-Volume** | Roster Requirements swept across a volume range | A table of headcount vs. client volume | `docs/am-staffing-by-volume.md` — directly mirrors this module's intended output already |

---

## 4. Cross-Model Dependency Rule

**The Financial Model's payroll figure and the Operations Model's roster-requirement figure must be the same number, sourced from one calculation, not two.** This is the single most important architectural rule in this document, because the audit found this exact class of drift already happened once in this repo's history (`rules/CLAUDE.md`'s "Why This Rule Exists" — the AM/GTT segment losing money in `pm-staffing-roster.md` nine days after being corrected elsewhere). The Staffing Model (§3) exists specifically as the shared middle layer both other models consume, rather than each maintaining its own copy of "how many treatment staff are needed."

---

## 5. What This Document Does Not Do

It does not choose an implementation technology (Python module, spreadsheet formulas, or a hybrid) — that is an implementation-phase decision. It does not build any model, write any code beyond what already exists in `tools/`, or change any existing calculation's output.
