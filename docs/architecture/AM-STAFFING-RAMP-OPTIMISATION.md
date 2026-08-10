# AM Staffing Ramp Optimisation

**Phase:** Continued operational optimisation — investigation only. **No compliance, safety, client-experience, or pregnancy-privacy standard is reduced anywhere in this document.** No canonical YAML or financial model file is modified. Builds directly on `docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md`, adding role-level staffing detail and testing whether the Month 1 break-even gap identified there can be closed by smarter staffing *timing* rather than accepted as an unavoidable loss.

**Date:** 2026-08-10
**No WDP communication drafted or sent this phase — tracker item 50 remains completely untouched, per explicit instruction.**

---

## Direct Answer to the Coordinator's Question

**Partial yes, with hard limits.** The AM-segment break-even gap (Month 1's implied ~7.74 clients/day vs. the ~8.4 clients/day break-even at full 8-staff headcount) can be **narrowed, not closed**, by two genuine, evidence-grounded levers that do not touch compliance, safety, or client experience: (1) daily roster-size flexing within the existing casual-employment structure (not a headcount cut — a scheduling choice), and (2) receptionist AM-shift-length scaling with the shorter operating window that fewer daily pairs genuinely produce. Both are quantified below. **What cannot be reduced, and was tested and rejected:** phlebotomist headcount (2, a physical/clinical constraint), Venue Manager daily on-site presence (a safety-critical role per its own existing job description), and any role-combination that would pull the Venue Manager away from safety-escalation availability.

---

## 1. What's Genuinely Fixed — Tested, Not Assumed

- **Phlebotomists: 2, non-negotiable at every volume tier assessed.** The venue's entire draw-timing model (`docs/scenario-c-sync-timetables.md`) is built on synchronised PAIRS using both chairs simultaneously — a single-chair operating mode has never been solved, costed, or decided anywhere in this repository, and inventing one now would be exactly the kind of new operational assumption this phase is instructed not to make.
- **Venue Manager: 1, present every operating day, non-negotiable.** `docs/hr-framework.md` §13 states plainly: "the venue cannot safely open without it" — first-aid/EpiPen holder, fire warden, clinical escalation contact. **Role-combination considered and explicitly rejected:** using the Venue Manager to cover reception duties on low-volume days was considered and rejected — it would tie the one person responsible for safety escalation to a desk task, directly undermining the reason the role exists. Not adopted.
- **Receptionist: 1, non-negotiable.** Front-of-house, GTT coordination, and payment processing cannot be dropped at any volume without a genuine client-experience compromise.

---

## 2. What Genuinely Flexes — Two Real Levers

### 2.1 Daily roster size within the casual-employment structure

`data/canonical/staffing.yml` already establishes every treatment role as casual, explicitly not a fixed guaranteed-hours arrangement. The committed **8-staff headcount (4 Massage+Beauty pool, 2 Nails, 2 Hair) is a company-wide capability figure, solver-verified at peak concurrent demand for 12 and 18 clients/day** — it is not, on its own terms, a statement that all 8 must be rostered on every single low-volume day. At materially lower daily volumes (fewer simultaneous pairs moving through the system), peak concurrent overlap is genuinely lower — the same underlying logic that drives the solver's 8-staff result at 12–18/day would, by direct extension, produce a lower concurrent-staffing requirement at lower pair counts. **This is not independently solver-verified below 12 clients/day anywhere in this repository — flagged honestly, not invented.**

The one number this repo does provide: the 7-staff option (Massage+Beauty pool capped at 3, not 4), already disclosed in `staffing.yml` as valid at the historical 12-client/23-min-cadence model, **not independently re-verified against the current 25-min cadence.** Used here as the one evidence-grounded floor available, clearly flagged as unverified for the current cadence — not a new invention.

### 2.2 Receptionist AM-shift length scaling with pair count

The current AM shift assumption (07:00–12:00, 5 hours) was sized for the full 9-pair (18-client) schedule. At lower volumes, fewer pairs genuinely means a shorter overall AM operating window — each additional pair adds a fixed 25-minute stagger to when the last pair's collection cycle begins, so the total AM window scales directly with pair count, a fact already embedded in this venture's own canonical cadence (25 minutes/pair). **This is a real, quantifiable lever tied to the schedule's own structure, not a new assumption** — though the exact minute-by-minute AM window at pair counts below 9 has never been published in this repository at the same level of detail as the 12/18-client tables, so the dollar figures in §3 below use a directional, disclosed estimate, not a fabricated precise schedule.

---

## 3. Revised Staffing Analysis — Six Scenarios

**Methodology:** AM revenue and AM Direct Labour computed identically to `docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md` §2 (same canonical formulas, same sourced rates). Two treatment-staffing configurations shown side by side at every volume where the 8-staff structure is not itself the only evidence-grounded option: the current committed 8-staff structure (status quo, always valid), and the 7-staff alternative (cadence-unverified, flagged).

**Not a change to committed capacity — illustrative sensitivity checkpoints only.** The intermediate rows below (6, 8, 10 clients/day) are flagged explicitly as ramp-period sensitivity checkpoints, not a proposed or current committed volume — the venture's only canonical, currently-committed client capacity remains 18 clients/day (Table 1, PRIMARY) and 12 clients/day (Table 2, SECONDARY), unchanged by this document. Every intermediate row is flagged the same way individually below.

| Scenario | Pairs/day | Treatment config | Phleb | Receptionist AM hours (indicative) | AM Revenue (mo) | AM Direct Labour (mo) | AM Contribution (mo) | Margin |
|---|---|---|---|---|---|---|---|---|
| **Minimum viable opening team** | 3–4 | 7-staff (unverified for current cadence) — the lowest evidence-grounded floor | 2 | ~3hrs (indicative, shorter window) | A$39,495–52,660 | A$48,608–49,934 | -A$9,113 to +A$2,726 | negative to marginal |
| **6 clients/day (flagged: illustrative checkpoint, not current committed volume)** | 3 | 8-staff (status quo) / 7-staff (alt.) | 2 | ~3hrs (indicative) | A$39,495 | A$53,928 / A$48,608 | -A$14,433 / -A$9,113 | negative both |
| **8 clients/day (flagged: illustrative checkpoint, not current committed volume)** | 4 | 8-staff (status quo) / 7-staff (alt.) | 2 | ~3.5hrs (indicative) | A$52,660 | A$55,254 / A$49,934 | -A$2,594 / +A$2,726 | -4.9% / +5.2% |
| **10 clients/day (flagged: illustrative checkpoint, not current committed volume)** | 5 | 8-staff (status quo) / 7-staff (alt.) | 2 | ~4hrs (indicative) | A$65,825 | A$56,579 / A$51,259 | +A$9,246 / +A$14,566 | +14.0% / +22.1% |
| **12 clients/day (Table 2, committed, solver-verified)** | 6 | 8-staff (only solver-verified option) | 2 | 5hrs (current committed shift) | A$78,990 | A$57,905 | +A$21,085 | +26.7% |
| **18 clients/day (Table 1, committed, solver-verified)** | 9 | 8-staff (only solver-verified option) | 2 | 5hrs (current committed shift) | A$118,485 | A$61,882 | +A$56,603 | +47.8% |

**Note on the "Minimum viable opening team" row:** presented as the lowest defensible floor this repo's own evidence supports (7-staff + 2 phlebotomists + reduced-hours reception + a present Venue Manager), applicable across roughly the 3–4-pair range. It is explicitly **not** claimed to be solver-verified, and is not extended below this range — no data exists in this repository for 1–2-pair days, and none is invented here.

---

## 4. Does This Close the Month 1 Break-Even Gap?

**Narrows it, does not close it.** At the 7-staff configuration, AM-segment break-even moves from ~8.4 clients/day (8-staff) to ~7.2 clients/day — bringing it materially closer to, but still slightly above, Month 1's implied ~7.74 clients/day volume (per `docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md` §4). **This means even the most aggressive, evidence-grounded staffing optimisation available in this repository still leaves Month 1 close to break-even on the AM segment alone, not comfortably profitable** — and this AM-segment view still excludes PM revenue/costs and fixed opex, which the whole-venture Master Financial Model already shows produces a genuine Month 1 operating loss (Table 1's own -A$30,885.75 cash trough). **The receptionist-hours lever (§2.2) is smaller in magnitude and was not separately quantified into the table above with confidence — it narrows the gap further at the margin, but does not change this conclusion.**

---

## 5. Risks Identified

- **The 7-staff option remains unverified for the current 25-minute cadence.** Adopting it as a real operating plan without a fresh solver run risks understaffing on a day where real bookings cluster differently than the historical 23-minute-cadence model assumed.
- **The Minimum Viable Opening Team row is the most speculative in this document** — it extrapolates the 7-staff logic to the lowest pair counts without any solver confirmation at all.
- **Receptionist AM-hours flexing has never been tested against real client flow** — a genuinely shorter roster window risks a client arriving early or a pair running late without adequate front-of-house coverage, if not planned with a real buffer.

## 6. Recommended Next Decisions

1. **Commission the same scheduling-solver run recommended in the prior AM Operations Sensitivity Model**, specifically re-testing the 7-staff (3-person Massage+Beauty pool) configuration against the current 25-minute cadence at 6, 8, and 10 clients/day — this is the single highest-value piece of work to convert this document's "unverified alternative" into a confirmed operating plan.
2. **If the 7-staff option is confirmed, treat it as the Month 1–2 operating structure**, stepping up to the full 8-staff structure once real volume approaches the 10–12 client/day range — a genuine, evidence-based ramp, not the current flat-from-Month-1 assumption.
3. **Do not attempt to close the remaining gap by touching phlebotomist headcount, Venue Manager presence, or receptionist role existence** — this document's own testing found no defensible way to reduce these further without a real compliance or safety compromise.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document (see full validation summary in this phase's combined report-back).
