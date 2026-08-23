# Opening the Doors: Procurement Sequence

Status: current as of 2026-08-23. A 10-stage operational sequence (Stage 0 through Stage 9) for procurement specifically, complementing `docs/architecture/PROCUREMENT-DEPENDENCY-MAP.md`'s Phase 0-7 planning logic with the exact granularity the founder requested for opening-day sequencing (splitting fit-out ordering from fit-out execution, and adding staff setup and final compliance as their own stages). No procurement quantity or date is invented; each stage lists the procurement actions only.

## Stage 0: Before Venue

Resolve the founder decisions that do not depend on a site (Massage table-vs-chair format, laundry model, hand dryer vs paper towel, service-scope decisions), per `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 4. Execute Queue 1 (Buy Now) for items with no storage/timing constraint. Issue Queue 2 RFQs (China sourcing-agent enquiry, Australia RFQ release package) so quotes are in hand before they are needed. Begin identifying candidates for the still-unidentified external dependencies (HVAC/LEV contractor, Cafe food supplier, coffee/beverage supplier), per Queue 5.

## Stage 1: Venue Secured

Lease signed. Triggers Queue 3 (Venue Hold) Step 1: site measurement. Builder/fit-out RFQ process can now genuinely begin (3 independent quotes, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3).

## Stage 2: Site Measured and Professionally Verified

Queue 3 Steps 2-9: service/utility verification, electrical assessment, plumbing/hydraulic assessment, HVAC/LEV assessment, accessibility assessment, clinical requirements verification (WDP sign-off on the Blood Collection Room), food/Cafe requirements verification (council Food Business Notification), furniture/layout confirmation (final Lounge seating count, mirror dimensions, joinery dimensions). All Readiness-C (site-dependent) items in the master register move toward RFQ-ready once their specific measurement is confirmed, per `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`.

## Stage 3: Fit-Out Ordered

3 builder quotes compared and one selected. Specialist contractors (electrician, plumber, HVAC/LEV) engaged against the confirmed floor plan. Custom joinery (Reception/Cafe cabinetry, the site-dependent mirror) ordered against confirmed dimensions. Remaining Queue 2 RFQs (anything that was gated on venue confirmation) issued now that dimensions exist.

## Stage 4: Fit-Out Underway

Construction proceeds per the builder's schedule. Electrical, plumbing, and HVAC/LEV installation proceeds per the licensed trades' own schedule. No procurement action beyond monitoring the build against the confirmed specification; this stage is construction execution, not a procurement decision point.

## Stage 5: Equipment/Furniture Delivery

China-sourced items (per `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`) undergo pre-shipment inspection, then ship, clear customs, and are delivered. Australian-sourced items (per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md`) are delivered directly. Installation of site-dependent equipment (pedicure chair plumbing, mirror mounting, dust-collector electrical connection) happens as each trade's own installation step, coordinated against the fit-out timeline, not before the relevant room is ready to receive it.

## Stage 6: Consumables and Opening Stock

Opening stock ordered per `docs/architecture/PROCUREMENT-OPENING-STOCK-SCHEDULE.md`'s 4-week methodology, timed to arrive shortly before opening (not months in advance, since most consumables benefit from fresh stock at launch). This includes Blood Collection consumables (pending final WDP confirmation on the 3 WDP-dependent items), nail/hair/massage/beauty consumables, Cafe food/beverage stock (pending the food/coffee suppliers being identified), cleaning products, first aid/emergency supplies, toilet/paper products, and office supplies.

## Stage 7: Staff Setup/Training

Staff hired and trained on the delivered equipment specifically (not a generic induction): phlebotomists on the centrifuge and clinical equipment, nail/hair/beauty/massage staff on their own station equipment, Reception/Venue Manager on the POS/booking system. This stage depends on equipment already being delivered and installed (Stage 5), not run in parallel with it.

## Stage 8: Final Compliance/Operational Checks

Fire safety officer/building surveyor sign-off (smoke detectors, emergency lighting, fire extinguishers), WDP's final sign-off on the Blood Collection Room, council Food Business Notification confirmed active (at least 14 days before trading), accessibility compliance confirmed (AS 1428.1), electrical/plumbing/HVAC compliance certificates collected and filed against their Item IDs (a genuine, disclosed gap: no central warranty/compliance-documentation register exists yet, per `docs/architecture/PROCUREMENT-WORKFLOW.md` Step 15, should be built during this stage, not invented as already existing).

## Stage 9: Opening

First client-facing day. Ongoing replenishment begins per `docs/architecture/PROCUREMENT-OPENING-STOCK-SCHEDULE.md`'s reorder-point methodology, recalibrated against real consumption after 4-8 weeks of actual trading.

## What This Sequence Deliberately Does Not Do

It does not attach a date or duration to any stage; launch timing is not yet set, per this repository's own standing fact. It does not skip ahead: Stage 4 (fit-out underway) and Stage 5 (equipment delivery) are kept genuinely sequential, not parallel, since installing equipment before the relevant trade has finished its own work in that room risks damage and rework.

## Sourcing

`docs/architecture/PROCUREMENT-DEPENDENCY-MAP.md`, `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md`, `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`, `docs/architecture/PROCUREMENT-OPENING-STOCK-SCHEDULE.md`, `docs/architecture/PROCUREMENT-WORKFLOW.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the 10-stage (Stage 0-9) opening-day procurement sequence, at a finer granularity than the existing Phase 0-7 dependency map (splitting fit-out ordering from execution, adding staff training and final compliance as explicit stages), cross-referencing rather than duplicating the underlying dependency logic.
