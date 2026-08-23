# Procurement Dependency Map and Buy-Now/Buy-Later Phasing

Status: current as of 2026-08-23. Sets out the order in which procurement activity genuinely becomes possible, and assigns the earliest sensible phase to each category of item in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`. This is a planning sequence, not a committed timeline; no dates are attached because launch date is not yet set (per this repo's own standing fact).

## 1. Dependency Chain

VENUE SECURED, then MEASURED SITE, then FINAL FLOOR PLAN, then CLINICAL DESIGN VERIFICATION (WDP sign-off on the Blood Collection Room), then ELECTRICAL / PLUMBING / HVAC DESIGN (licensed trades), then JOINERY DESIGN (Reception/Cafe cabinetry, custom items), then RFQ, then SUPPLIER SELECTION, then SAMPLES, then PRODUCTION, then INSPECTION, then SHIPPING, then INSTALLATION, then OPENING STOCK, then OPENING.

Each step depends on the one before it being genuinely complete, not merely started. A small number of items can move ahead of this chain (see Phase 0 below) because they do not depend on the venue at all.

## 2. Phase 0: Pre-Venue / Planning (can proceed today)

No physical dependency on a venue. Covers: brand/design decisions not tied to a specific floor plate (palette, material language, already locked), the founder decisions in `PROCUREMENT-FOUNDER-DECISIONS.md` that are answerable without a site (Massage station format, laundry model, hand dryer vs paper towel, service-scope decisions), and early-stage supplier/agent research that stops short of contact (already largely done in `CHINA-AUSTRALIA-SOURCING-STRATEGY.md`). No item should be ordered in this phase; this phase is decisions and preparation only.

## 3. Phase 1: Venue Secured

Triggers: site measurement can begin (`PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`), lease terms confirm floor area for final Lounge seating count and Beauty/Massage room dimensions, and the builder/trade quoting process in `PROCUREMENT-AUSTRALIA-PACKAGE.md`'s "Builders/Trades" section can start (3 real builder quotes, gated on a confirmed venue).

## 4. Phase 2: Design / Approval

Final floor plan locked, clinical design verification (WDP sign-off on the Blood Collection Room's exact layout), council food-business notification for the Cafe (14 days before trading, gated on the menu being locked), and licensed-trade electrical/plumbing/HVAC design sign-off. Items classified D. PROFESSIONAL VERIFICATION REQUIRED or E. WDP DEPENDENT in the master register are resolved in this phase, not before.

## 5. Phase 3: Fit-Out

Joinery design finalised (Reception/Cafe cabinetry), RFQs sent for site-dependent categories (C. SITE DEPENDENT items in the master register move to B. RFQ READY once dimensions are confirmed), supplier selection, sample review, and production for both the China Procurement Package and the Australian Procurement Package's formal-RFQ categories.

## 6. Phase 4: Equipment Installation

Inspection (pre-shipment, per the QC requirements in `PROCUREMENT-CHINA-PACKAGE.md`), shipping, customs clearance, and on-site installation of all capital equipment and furniture. Licensed-trade interface work (GPO placement, LEV ducting, plumbing connections) happens alongside installation, not before it, since it depends on the actual delivered equipment's exact specifications.

## 7. Phase 5: Opening Stock

Consumables ordered per `PROCUREMENT-OPENING-STOCK-SCHEDULE.md`'s 4-week opening-stock methodology, timed to arrive shortly before opening, not months in advance (most consumables have a shelf life or a preference for fresh stock at launch).

## 8. Phase 6: Opening Week

Final walk-through against the room-by-room checklist (once built, see the still-pending Part 13 room schedule), staff trained on equipment use, first client-facing day.

## 9. Phase 7: Ongoing Replenishment

Reorder-point-triggered replenishment per `PROCUREMENT-OPENING-STOCK-SCHEDULE.md`, recalibrated against real consumption data after 4-8 weeks of actual trading (the opening-stock methodology is explicitly disclosed as a planning assumption, not a measured rate).

## 10. Readiness-to-Phase Mapping (Master Register Cross-Reference)

| Readiness classification (master register) | Earliest phase it can be actioned |
|---|---|
| A. ORDER READY | Phase 3 (Fit-Out) at the earliest, no site dependency blocking it |
| B. RFQ READY | Phase 3 (Fit-Out) |
| C. SITE DEPENDENT | Phase 1-2 (measurement, then RFQ becomes possible) |
| D. PROFESSIONAL VERIFICATION REQUIRED | Phase 2 (Design/Approval) |
| E. WDP DEPENDENT | Phase 2 (Design/Approval), pathology partner sign-off |
| F. FOUNDER DECISION REQUIRED | Phase 0 (Pre-Venue/Planning), must resolve before the item can move to any later phase |
| G. INFORMATION REQUIRED | Phase 0-1, depends on the specific information gap (see the item's own Next Action in the master register) |
| H. FUTURE/OPTIONAL | Not phased, deferred until after opening, revisited against actual trading performance |

Consumables (Opening Stock schedule) are Phase 5 regardless of their Readiness classification, since they are timed to trading, not to the fit-out sequence.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`, `docs/architecture/PROCUREMENT-FOUNDER-DECISIONS.md`, `docs/architecture/PROCUREMENT-OPENING-STOCK-SCHEDULE.md`, `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`, `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Parts 5 and 15) as the procurement dependency chain and Phase 0-7 buy-now/buy-later logic, cross-referencing the Readiness classification already assigned to all 281 items rather than re-phasing each item individually.
