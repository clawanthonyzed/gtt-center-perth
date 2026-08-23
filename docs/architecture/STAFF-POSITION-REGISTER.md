# Staff Position Register

Status: current as of 2026-08-23. Single authoritative position-ID register, replacing scattered PMM01/PMH01/PMN01/PMB01-style shorthand used elsewhere in this dossier with one real, complete register. Every position below traces to `data/canonical/staffing.yml` and the AM/PM solver output (`tools/am_staggered_staffing_solver.py`, `tools/pm_solver.py`).

Terminology: "AM eligibility" and "PM eligibility" describe whether a position's skillset is capable of that shift, not whether the committed payroll model currently rosters that specific instance there. AM and PM treatment positions are costed as separate headcount in the committed model (data/canonical/staffing.yml keeps AM and PM treatment records distinct), even where the same real person could in principle work both shifts on different rostered days.

## Venue leadership

| Position ID | Title | Role | Employment pool | AM eligible | PM eligible | Relief eligible | Saturday eligible | Normal hours | Wage assumption | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| VM01 | Venue Manager | Operational leadership | 1, no relief pool (single point of failure, disclosed) | Yes, covers AM reception personally | Yes, overlaps 13:00-15:00 | No (Mon-Fri emergency-only fill by a cross-trained senior treatment staff member, not a standing relief position) | Yes | 07:00-15:00, Mon-Sat | A$40.00/hr, Hair & Beauty Industry Award MA000005 Level 6, Researched-best-evidenced | Critical-path hire, recruitment gated on securing a venue |

## Phlebotomy

| Position ID | Title | Role | Employment pool | AM eligible | PM eligible | Relief eligible | Saturday eligible | Normal hours | Wage assumption | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| PHL01 | Phlebotomist, Chair A | Blood collection | 4 recommended (2 committed simultaneous + 2 relief; 3 total is the disclosed lower bound) | Yes, AM only | No (no PM clinical role) | N/A, committed | Yes | 07:00-13:00, Mon-Sat | A$34.375/hr midpoint, Health Professionals and Support Services Award MA000027 | Zero substitution capability from any other position |
| PHL02 | Phlebotomist, Chair B | Blood collection | See PHL01 | Yes, AM only | No | N/A, committed | Yes | 07:00-13:00, Mon-Sat | Same as PHL01 | Same as PHL01 |
| PHL03 | Phlebotomist, relief | Blood collection | Recommended pool member (not simultaneous) | Yes, AM only, on relief | No | Yes | Yes | On-call | Same as PHL01 | Founder decision outstanding: 4 recommended vs 3 lower bound |
| PHL04 | Phlebotomist, relief | Blood collection | Recommended pool member (not simultaneous) | Yes, AM only, on relief | No | Yes | Yes | On-call | Same as PHL01 | Only exists if the 4-person pool is confirmed over the 3-person lower bound |

## AM treatment: Massage+Beauty pool (dual-qualified)

| Position ID | Title | Role | Employment pool | AM eligible | PM eligible | Relief eligible | Saturday eligible | Normal hours | Wage assumption | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| MB01-MB04 | Massage+Beauty Treatment Staff | Pregnancy massage + pregnancy-safe facials | 6 recommended (4 committed simultaneous + 2 relief; 5 total is the disclosed lower-reliability alternative) | Yes, staggered start (07:05 or 07:30, per the solver's own calibrated output, tools/am_staggered_staffing_solver.py) | Only if separately rostered as PMM01/PMB01 (a distinct PM position, not the same headcount) | N/A, committed | Yes | 07:00-13:00, Mon-Sat | A$37.50/hr, MA000005 Level 4 | Dual-qualification is the confirmed cross-cover mechanism between Massage and Beauty; solver-verified peak concurrency of 4 at both 12 and 18 clients/day |
| MB05-MB06 | Massage+Beauty Treatment Staff, relief | Same as above | Recommended pool members (not simultaneous) | Yes, on relief | Only if separately rostered as PM | Yes | Yes | On-call | Same as MB01-04 | Founder decision outstanding: 6 recommended vs 5 lower-reliability alternative |

## AM treatment: Nail Technician

| Position ID | Title | Role | Employment pool | AM eligible | PM eligible | Relief eligible | Saturday eligible | Normal hours | Wage assumption | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| NAIL01-NAIL02 | Nail Technician | Manicure, pedicure, nail add-ons | 3 recommended (2 committed simultaneous + 1 relief) | Yes, staggered start (07:30, per the solver's own calibrated output) | Only if separately rostered as PMN01 | N/A, committed | Yes | 07:00-13:00, Mon-Sat | A$36.81/hr, MA000005 Level 3 | No confirmed dual-qualification with Hair or Massage+Beauty; costed independently |
| NAIL03 | Nail Technician, relief | Same as above | Recommended pool member (not simultaneous) | Yes, on relief | Only if separately rostered as PM | Yes | Yes | On-call | Same as NAIL01-02 | Part of the 12-total treatment employment pool recommendation |

## AM treatment: Hairdresser

| Position ID | Title | Role | Employment pool | AM eligible | PM eligible | Relief eligible | Saturday eligible | Normal hours | Wage assumption | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| HAIR01-HAIR02 | Hairdresser | Blowdry, haircut, braiding/hair up (GTT window) | 3 recommended (2 committed simultaneous + 1 relief) | Yes, staggered start (07:30, per the solver's own calibrated output) | Only if separately rostered as PMH01 | N/A, committed | Yes | 07:00-13:00, Mon-Sat | A$36.81/hr, MA000005 Level 3 | No confirmed dual-qualification with Nails or Massage+Beauty; costed independently |
| HAIR03 | Hairdresser, relief | Same as above | Recommended pool member (not simultaneous) | Yes, on relief | Only if separately rostered as PM | Yes | Yes | On-call | Same as HAIR01-02 | Part of the 12-total treatment employment pool recommendation |

## PM dedicated-casual roles

Committed structure: 1 per line, not pooled for headcount purposes, though Massage and Beauty share a documented cross-training pairing. Demand-driven scaling to 2-3 per role is solver-verified as genuinely required only during a real peak-period cluster of concurrent arrivals (`tools/pm_solver.py`'s demand-scaling scenario), not as a standing headcount increase.

| Position ID | Title | Role | Employment pool | AM eligible | PM eligible | Relief eligible | Saturday eligible | Normal hours | Wage assumption | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| PMM01 | PM Massage Therapist | Standalone/afternoon pregnancy massage, PM Refresh | 1 committed; 2-3 on demand (solver-verified peak scenario, not a standing hire) | Only if separately rostered as MB01-06 | Yes, 13:00-18:00 | Small on-call relief pool, all operating hours | Yes | Hours-based costing, not a fixed shift length | Hours-based, per `data/canonical/wages.yml` | Covers PM reception during own natural booking gaps (Model C); Fresha/payment-processing required skill |
| PMB01 | PM Beauty Therapist | Standalone/afternoon facials, PM Refresh | 1 committed; 2-3 on demand | Only if separately rostered as MB01-06 | Yes, 13:00-18:00 | Small on-call relief pool, all operating hours | Yes | Hours-based costing | Hours-based | Cross-trained with PMM01 for PM Refresh delivery; covers PM reception during own gaps |
| PMN01 | PM Nail Technician | Standalone/afternoon manicure, pedicure, PM Restore (Nails half) | 1 committed; 2-3 on demand | Only if separately rostered as NAIL01-03 | Yes, 13:00-18:00 | Small on-call relief pool, all operating hours | Yes | Hours-based costing | Hours-based | PM Restore's Nails half runs sequentially before the Hair half, never concurrently; covers PM reception during own gaps |
| PMH01 | PM Hairdresser | Standalone/afternoon blowdry, haircut, PM Restore (Hair half) | 1 committed; 2-3 on demand | Only if separately rostered as HAIR01-03 | Yes, 13:00-18:00 | Small on-call relief pool, all operating hours | Yes | Hours-based costing | Hours-based | PM Restore's Hair half runs sequentially after the Nails half, never concurrently; covers PM reception during own gaps |

## What this replaces

Prior references to "PMM01/PMH01/PMN01/PMB01" in the dossier were descriptive shorthand for the 4 PM dedicated-casual roles, not a formal, complete register. This document is now the single authoritative position-ID source; the dossier's staffing chapters (14-17) should cite this register rather than restate position IDs independently.

## Sourcing

`data/canonical/staffing.yml` (headcount, wage assumptions, required skills), `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` (reliability-based employment pool recommendations), `tools/am_staggered_staffing_solver.py` (AM staggered-start verification), `tools/pm_solver.py` (PM demand-driven verification), `docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md` (Model C, PM Reception resolution).

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 11) as the single, complete staff position register, using real position IDs (VM01, PHL01-04, MB01-06, NAIL01-03, HAIR01-03, PMM01/PMB01/PMN01/PMH01) rather than descriptive shorthand, incorporating the AM/PM solvers' own verified output for staggered-start and demand-driven fields.
