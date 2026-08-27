# Construction and Fit-Out Requirements

Status: current as of 2026-08-23. Physical venue requirements beyond furniture and consumables: walls, doors, flooring, ceilings, lighting, electrical, data, plumbing, drainage, HVAC, LEV, hot/cold water, sinks, clinical room requirements, Cafe services, toilets, accessibility, fire/life safety, signage, acoustic requirements, storage, joinery, cabinetry, mirrors, privacy curtains, wall finishes, painting, flooring finishes, and Reception/Cafe/salon joinery. Every line is classified as exactly one of: **PURCHASED ITEM** (a physical product bought from a supplier), **TRADE/CONTRACTOR** (labour engaged directly, not a product purchase), **SITE-DEPENDENT** (cannot be quantified before a venue is measured), or **PROFESSIONAL DESIGN/VERIFICATION** (requires a licensed Australian professional's sign-off). **No construction quantity is invented before the site is measured.**

## Walls, Doors, Flooring, Ceilings (General Construction)

**TRADE/CONTRACTOR.** General venue construction (walls, doors, flooring, ceilings) is not itemised as individual product line items in the master register; it is captured as part of the whole-of-venue builder quote once a site is measured and a floor plan is finalised, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3 (Builder/Fit-Out Quote), requiring 3 real, independent builder quotes. **SITE-DEPENDENT.** No quantity or cost figure for general construction exists in this repository beyond the independently-derived fit-out cost estimate already flagged in `docs/architecture/STARTUP-COST-RECONCILIATION.md` as covering fit-out only, not comparable to a bindable quote without a confirmed venue.

The Blood Collection Room's own construction (solid walls, one door, no public-facing window, Item ID E31) is itemised specifically because of its clinical function, not because general construction elsewhere is itemised differently.

## Flooring Finishes, Wall Finishes, Painting

**TRADE/CONTRACTOR, SITE-DEPENDENT.** Not itemised as individual purchase line items; part of the whole-of-venue builder quote. Material/finish direction (the locked 7-colour palette, `outputs/brand/warm-stone-tokens.css`) is confirmed and should be supplied to the builder as a brief, but the actual flooring/wall-finish product selection and quantity depends on the confirmed floor area.

## Ceilings, Acoustic Requirements

**TRADE/CONTRACTOR, SITE-DEPENDENT.** No acoustic requirement has been researched or itemised anywhere in this repository; this is a genuine gap, not a resolved requirement. If acoustic treatment between treatment rooms (Massage/Beauty curtain-partitioned, not stud-wall) is a genuine client-experience concern, it should be raised with the builder at quote stage, not assumed adequate by default.

## Electrical (GPO, Circuits)

**PROFESSIONAL DESIGN/VERIFICATION, SITE-DEPENDENT.** Item IDs: A05 (general power outlets), G14 (Beauty station electrical), H21 (Nail station electrical), J18 (Hair station electrical), C04 (Cafe water tap electrical), E36 (Blood Collection emergency call button). All require a licensed electrician engaged post-venue, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 4 (Specialist Contractor).

## Data (Network Cabling, WiFi)

**PURCHASED ITEM plus TRADE/CONTRACTOR.** Item IDs: T01 (WiFi router, Order-Ready, already priced), T02 (network switches, Site-Dependent), T03 (access points, Site-Dependent). Cabling installation itself is a licensed-trade task, not itemised separately in the register; it should be included in the electrical contractor's scope at quote stage.

## Plumbing, Drainage, Hot/Cold Water, Sinks

**PROFESSIONAL DESIGN/VERIFICATION, SITE-DEPENDENT.** Item IDs: C04 (Cafe chilled/boiling water tap), E24 (Blood Collection clinical hand-hygiene sink), G08 (Beauty 2-sink fitout), I02 (Pedicure chair plumbing), K02/K04 (Hair Wash hot water supply/system capacity), L04 (Staff sink). All require a licensed plumber engaged post-venue, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 4.

## HVAC (General)

**TRADE/CONTRACTOR, SITE-DEPENDENT.** Item ID: A04 (air conditioning/HVAC servicing). No named contractor identified yet, a genuine gap disclosed in `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 4.

## LEV (Local Exhaust Ventilation, Nail Station)

**PURCHASED ITEM plus TRADE/CONTRACTOR, PROFESSIONAL DESIGN/VERIFICATION.** Item ID: H06 (LEV unit, already priced A$1,500-4,000 installed, but no WorkSafe-WA-familiar contractor has been identified for the specific installation, a genuine, disclosed gap).

## Clinical Room Requirements (Blood Collection)

**PROFESSIONAL DESIGN/VERIFICATION, SITE-DEPENDENT.** Room construction (E31), room ventilation at 6 ACH (E38), clinical sink fitout (E24), emergency call button (E36). **Founder decision, closed 2026-08-27: 2 Blood Collection Rooms, one per phlebotomist, for privacy** (`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` Section E, `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` Part B): E31 now quantity 2; E24/E36/E38 flagged as likely-2/genuinely-open per-room questions in the master register, not asserted here. Full detail in `docs/architecture/PROCUREMENT-CLINICAL-GTT-WDP-SPLIT.md` Category D.

## Cafe Services

**SITE-DEPENDENT, TRADE/CONTRACTOR.** Preparation/serving counter (C19, custom, site-installed within the Cafe's own footprint), Cafe-specific handwashing station (C20, professional verification, confirm exact requirement with the local council Environmental Health Officer). Full detail in `docs/architecture/PROCUREMENT-CAFE-BREAKDOWN.md`.

## Toilets

**PURCHASED ITEM plus SITE-DEPENDENT plus PROFESSIONAL DESIGN/VERIFICATION.** Fixtures depending on final toilet count (Item IDs N04-N06, N09, N10, N14, all Site-Dependent since the exact toilet count is not fixed before venue confirmation), accessibility grab rails/fittings (N13, Professional Verification, AS 1428.1), hand dryer vs paper towel (N08, a genuine Founder Decision, not yet resolved).

## Accessibility

**PROFESSIONAL DESIGN/VERIFICATION.** AS 1428.1 accessibility clearances for the accessible toilet (N13) and for the venue's general accessible-path requirements (not itemised as a separate line, since accessibility is a whole-of-venue design requirement confirmed by an access consultant at floor-plan stage, not a single purchasable item).

## Fire/Life Safety

**PROFESSIONAL DESIGN/VERIFICATION.** Fire extinguishers (A01), smoke detectors/alarm system (A03), emergency lighting (X14, AS 2293), all requiring building surveyor/fire safety officer sign-off. A03's own register note already flags this is "likely landlord/base-building responsibility, confirm at lease", not assumed to be a tenant fit-out cost.

## Signage

**PURCHASED ITEM plus SITE-DEPENDENT.** Toilet signage including accessibility symbol (N14), Blood Collection biohazard/hand-hygiene/no-entry signage (E33-E35), external signage (X16, gated on the final naming founder decision, not resolved here).

## Lighting

**PROFESSIONAL DESIGN/VERIFICATION for functional/task lighting (Section X, 12 of 16 items), PURCHASED ITEM for decorative lighting (China Sourcing Group 5).** Every functional lighting fixture in Section X (Reception X01, Cafe X02, Blood Collection X04, Nail X05, Pedicure X06, Massage X07, Hair Wash X10, Toilets X11, Staff X12, Storage X13, Emergency X14) requires an Australian lighting designer/electrician, since it must be specified against the confirmed site's own electrical design, not a China sourcing candidate. Decorative/ambient lighting (D04 Lounge floor lamps, X15 optional feature lighting) is a purchased item, see `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md` Sourcing Group 5.

## Storage, Joinery, Cabinetry

**PURCHASED ITEM plus TRADE/CONTRACTOR.** Storage shelving (M01, M03, M04, purchased items, China Sourcing Group 1/6/10 candidates), custom Reception/Cafe cabinetry (a licensed joiner, `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3, not a purchased catalogue item since it is bespoke).

## Mirrors

**PURCHASED ITEM, SITE-DEPENDENT.** Hair styling mirror (J02, custom-fit to the venue's actual wall length, cannot be finalised before a venue is confirmed and measured, per `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`). Full detail in `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md` Sourcing Group 4.

## Privacy Curtains

**PURCHASED ITEM.** Blood Collection per-chair curtain/partition (E32), Massage curtain partition (F09), Beauty implied curtain-partitioned layout per the venue program. All washable fabric, matching the locked palette.

## Reception/Cafe/Salon Joinery

**TRADE/CONTRACTOR, SITE-DEPENDENT.** Custom Reception counter and Cafe cabinetry require a licensed joiner once the venue is confirmed and measured; not a catalogue purchase, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3.

## What This Document Deliberately Does Not Do

It does not invent a construction quantity, floor area, or cost figure before a venue is measured. Where the register itself has no itemised line for a construction category (walls, ceilings, painting, acoustic treatment), this document says so explicitly rather than inventing a placeholder item ID or figure.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3/4, `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`, `docs/architecture/PROCUREMENT-CLINICAL-GTT-WDP-SPLIT.md`, `docs/architecture/STARTUP-COST-RECONCILIATION.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 12) so procurement is not reduced to furniture and consumables; separates every physical venue requirement into Purchased Item, Trade/Contractor, Site-Dependent, or Professional Design/Verification, without inventing any construction quantity before the site is measured.
