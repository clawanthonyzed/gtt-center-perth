# Cafe Procurement Breakdown

Status: current as of 2026-08-23. Built strictly against the current, confirmed Cafe model: a small cafe, food not prepared from raw ingredients on site, externally supplied, may be warmed or toasted on site, coffee and hot/cold drinks available for purchase, free water and free herbal tea available to every client regardless of purchase. **No snack pack. No end-of-GTT snack. No old GDM snack pack concept.** All items below are cross-referenced to Section C of `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, the single quantity/source of truth; this document organises the same items by function, it does not duplicate or re-quantify them.

## Equipment

Full-size beverage refrigerator (C01, commercial grade), display refrigerator for sandwiches/rolls (C02, temperature-controlled, customer-visible), toastie press (C05, commercial grade). **Status:** all three Order-Ready, already priced from existing repository research.

## Furniture

None specific to the Cafe counter itself beyond the display shelving covered under Display below; seating for Cafe patrons is the shared Lounge seating (Section D), not a separate Cafe furniture line.

## Plumbing

Chilled and boiling water tap (C04, under-counter unit, requires a plumbed water supply). **Status:** Order-ready for the unit itself; the plumbed connection is a site-dependent install requiring a licensed plumber once the venue is confirmed.

## Electrical

Coffee machine (C03, requires a dedicated electrical circuit), toastie press (C05), chilled/boiling water tap (C04, electrical safety mark for the heating element), display/beverage refrigerators (C01/C02, standard GPO). All electrical connections are confirmed by a licensed electrician once the venue is confirmed, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 4 (Specialist Contractor).

## POS

Cafe POS shares Reception's own POS terminal (C18, B07); this is confirmed as no separate Cafe POS hardware purchase, not an oversight.

## Food Display

Customer-accessible display shelving (C16, self-selection of packaged items), menu board/signage (C17, gated on the final venture naming decision, a genuine founder decision not silently resolved here).

## Food Storage

Sealed, stackable commercial food-grade storage containers (C06), fridge/freezer digital thermometer with log sheet (C07, food-safety cold-chain temperature logging requirement).

## Food Service

Chopping board/utensils (C09, colour-coded, dishwasher-safe, for toastie assembly/toasting only, explicitly not raw-ingredient cooking, consistent with the current model), food handling gloves (C08, disposable, food-grade).

## Takeaway Packaging

Takeaway cups (C12, compostable/recyclable, branded), takeaway lids (C13), napkins (C14), cutlery (C15, reusable preferred for the premium positioning, disposable as a fallback), dine-in cups and plates (C10, C11, ceramic).

## Coffee

Coffee beans/milk/syrups (C23), sourced from a wholesale coffee supplier not yet selected. The coffee machine itself (C03) is Order-Ready and separate from the ongoing bean/milk supply.

## Tea

Herbal tea (C24), free to all clients regardless of purchase, per the confirmed customer promise; bulk supply, supplier not yet selected.

## Drinks

Bottled/canned cold drinks (C25), wholesale beverage supplier not yet selected.

## Cleaning

Cafe-specific waste bin (C21, lidded, foot-pedal, food waste separated from general/biohazard waste per food-safety waste segregation requirements). General Cafe surface cleaning uses the same commercial cleaning products as the rest of the venue (Section O), not a separate Cafe-specific cleaning line.

## Food Safety

Food Business Notification (C26, local council, at least 14 days before trading, gated on a confirmed venue and a locked menu), Cafe-specific handwashing station (C20, separate from any clinical hand-hygiene station, professional verification required, confirm the exact requirement with the local council Environmental Health Officer), preparation/serving counter (C19, site-dependent, custom-installed within the Cafe's own footprint).

## Opening Stock

Coffee beans/milk/syrups, herbal tea, cold drinks, dine-in crockery, and takeaway packaging are all sized in `docs/architecture/PROCUREMENT-OPENING-STOCK-SCHEDULE.md`'s Cafe Consumables table, calibrated against the current planning assumption of 50% of AM clients spending A$10 at the Cafe (approximately 9 transactions/day at 18 clients/day). Pre-made sandwiches/rolls opening stock is explicitly blocked pending the external food supplier being identified.

## Supplier Requirements

**Do not invent the food supplier.** The external pre-made food supplier is a genuine, outstanding procurement dependency, not yet identified anywhere in this repository. It cannot be resolved by research within this repository; it requires an actual business-development step (identifying and approaching candidate suppliers), which has not been taken. The same applies to the coffee/beverage wholesale supplier, also not yet selected. Both are listed in `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 6 (Food/Beverage Supplier) with the specific quote requirements a selected supplier would need to respond to.

## What This Breakdown Deliberately Does Not Include

Any snack pack, any end-of-GTT snack, the old GDM snack pack concept, or any menu item not already confirmed in the current Cafe model above. The glucose drink administered during blood collection (E21) is a phlebotomist workflow item under Blood Collection, not a Cafe item, and is not repeated here.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` Section C, `docs/architecture/PROCUREMENT-OPENING-STOCK-SCHEDULE.md`, `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 6.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 9) as a functional breakdown of the existing Cafe procurement items, strictly matching the confirmed current Cafe model, with the external food supplier and coffee/beverage wholesaler explicitly stated as outstanding dependencies rather than invented.
