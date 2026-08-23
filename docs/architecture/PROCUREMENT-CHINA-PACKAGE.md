# China Procurement Package

Status: current as of 2026-08-23. Built from the China-candidate (CN) and hybrid (HY) items already classified in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (42 CN, 93 HY). No item is assumed safe to import simply because it is furniture; clinical, regulated, and fire/life-safety items remain excluded per `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`'s existing classification. **No supplier or sourcing agent has been contacted. No order, RFQ, or sample request has been sent.**

Each sourcing group below is written to stand alone: a sourcing agent reading only one group should have everything currently known about that group without needing to read the rest of this document. Where a field is genuinely not yet determined, it says so and states what would resolve it, rather than being left blank or guessed.

## Sourcing Group 1: Reception/Cafe Joinery-Adjacent Furniture (not the structural joinery itself)

- **Items included:** retail display shelving (pending the retail founder decision), customer-accessible Cafe display shelving.
- **Item IDs:** B18, C16.
- **Quantity:** 1 each.
- **Functional specification:** open shelving for customer self-selection of packaged retail/Cafe items, commercial-duty.
- **Dimensions:** not yet determined, depends on the final Reception/Cafe floor plan once a venue is confirmed.
- **Material:** not yet determined beyond "matches the locked palette"; timber or timber-look commercial shelving is the likely category.
- **Finish:** warm stone/timber tones per the locked palette.
- **Colour:** matches the locked 7-colour palette (`outputs/brand/warm-stone-tokens.css`).
- **Required customisation:** none identified; catalogue/near-catalogue items are expected to be adequate.
- **Reference image requirement:** yes, a reference image matching the palette should be supplied with any RFQ; no specific reference image has been selected yet.
- **Technical drawing requirement:** not required for a catalogue item; would be required only if a bespoke size is ultimately needed once the floor plan is known.
- **Certification requirements:** none beyond general consumer product safety (non-electrical items).
- **Factory requirements:** confirmed commercial-furniture manufacturing capability, not a residential-only supplier.
- **Sample requirements:** factory sample of the finish/material before full production.
- **QC requirements:** pre-shipment inspection on the full order.
- **Packaging requirements:** flat-pack or assembled, freight-dependent; not yet decided which, pending freight-cost comparison.
- **Freight requirements:** not yet quoted, part of the whole-order consolidated freight calculation, see `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §7.
- **Installation requirements:** minimal, freestanding/wall-mounted shelving, no licensed trade required beyond wall-fixing if wall-mounted.
- **Warranty requirements:** not yet determined, no warranty term has been confirmed for any item in this package; must be obtained at quote stage.

## Sourcing Group 2: Nail Stations

- **Items included:** nail table with built-in dust collector, nail tool trolley.
- **Item IDs:** H01, H07.
- **Quantity:** 4 each.
- **Functional specification:** professional grade, built-in dust collector, cable management, durable cleanable surface.
- **Dimensions:** not yet determined, to be confirmed against the final floor plan (Section H of the master register).
- **Material:** not yet determined beyond "matches the locked palette"; a durable, cleanable laminate or solid-surface worktop is the expected category.
- **Finish:** wipe-clean, matches the locked palette.
- **Colour:** matches the locked 7-colour palette.
- **Required customisation:** dust-collector integration is a functional requirement, not a cosmetic customisation; no bespoke sizing identified yet.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** not required for a catalogue item with a built-in dust collector; would be required if the final floor plan forces a bespoke footprint.
- **Certification requirements:** electrical safety mark (SAA) for the built-in dust collector.
- **Factory requirements:** demonstrated experience manufacturing nail tables with integrated ventilation, not a generic furniture factory.
- **Sample requirements:** factory sample of the unit before full production.
- **QC requirements:** pre-production approval, pre-shipment inspection.
- **Packaging requirements:** export-grade packaging suitable for sea freight, not yet confirmed as included in any quote.
- **Freight requirements:** not yet quoted, part of the whole-order consolidated freight calculation.
- **Installation requirements:** yes, the dust collector requires connection to a suitable GPO on-site; confirm Australian electrical safety compliance even if manufactured overseas, with an Australian-based sourcing agent or electrician before purchase.
- **Warranty requirements:** not yet determined, must be obtained at quote stage.

## Sourcing Group 3: Hair Styling Stations

- **Items included:** styling chair (hydraulic, wipe-clean), tool trolley/organiser.
- **Item IDs:** J01, J15.
- **Quantity:** 4 each.
- **Functional specification:** hydraulic recline/height adjustment, wipe-clean upholstery, commercial salon duty.
- **Dimensions:** not yet determined, standard styling-chair footprint, exact spacing depends on the final floor plan.
- **Material:** vinyl upholstery (wipe-clean), metal hydraulic base.
- **Finish:** wipe-clean, matches the locked palette.
- **Colour:** matches the locked 7-colour palette.
- **Required customisation:** none identified, catalogue hydraulic chairs meeting AS/NZS 4088 are expected to be adequate.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** not required for a catalogue item.
- **Certification requirements:** AS/NZS 4088 stability standard.
- **Factory requirements:** demonstrated experience manufacturing commercial salon seating, not general office/domestic seating.
- **Sample requirements:** factory sample of the upholstery material and finish.
- **QC requirements:** pre-production approval, pre-shipment inspection.
- **Packaging requirements:** export-grade packaging suitable for sea freight, not yet confirmed.
- **Freight requirements:** not yet quoted.
- **Installation requirements:** no, freestanding, no licensed trade required for the chair itself (a GPO nearby each chair is a separate site-dependent electrical item, see the master register's J18).
- **Warranty requirements:** not yet determined, must be obtained at quote stage, particularly important for the hydraulic mechanism specifically.
- **Excluded from this group:** professional hair dryers and straightening irons (J03/J04) remain Australian-sourced via direct trade accounts (Dyson, GHD, Cloud Nine), poor import candidates on warranty grounds, per the existing sourcing strategy, not reclassified here.

## Sourcing Group 4: Mirrors

- **Items included:** salon mirror, lighted, full-length.
- **Item IDs:** J02.
- **Quantity:** 1 (spans 4 chairs).
- **Functional specification:** full-length mirror with integrated LED strip lighting, warm colour temperature matching the palette.
- **Dimensions:** not yet determined. This item is site-dependent; it cannot be finalised before a venue is confirmed and the actual wall length is measured, see `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`.
- **Material:** glass mirror panel, integrated LED strip.
- **Finish:** warm colour-temperature LED matching the palette.
- **Colour:** matches the locked 7-colour palette for the LED colour temperature and any surrounding frame.
- **Required customisation:** yes, custom-fit to the venue's actual wall length once measured; this is a bespoke-dimension item by design, not a catalogue item.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** yes, required once the wall length is known, since this is a custom-dimension item.
- **Certification requirements:** SAA electrical mark for the integrated LED strip.
- **Factory requirements:** demonstrated experience manufacturing custom-length lighted mirrors, not a generic mirror supplier.
- **Sample requirements:** LED colour-temperature and mirror-glass sample before full production.
- **QC requirements:** pre-production approval against the confirmed dimensions, pre-shipment inspection.
- **Packaging requirements:** glass-safe export packaging, a genuine freight-damage risk given the size and fragility; not yet confirmed with any supplier.
- **Freight requirements:** not yet quoted; likely requires specialised glass-freight handling, distinct from standard furniture freight.
- **Installation requirements:** yes, wall-mounted, licensed electrician required for the LED strip connection.
- **Warranty requirements:** not yet determined, must be obtained at quote stage.
- **Status note:** this item is RFQ-ready in specification but not yet orderable in final size.

## Sourcing Group 5: Decorative Lighting

- **Items included:** Lounge floor lamps, feature/decorative lighting (optional).
- **Item IDs:** D04, X15.
- **Quantity:** 4 (floor lamps), remainder optional.
- **Functional specification:** warm, dimmable ambient lighting matching the palette.
- **Dimensions:** not yet determined.
- **Material:** not yet determined beyond "matches the locked palette".
- **Finish:** warm, dimmable, matches the locked palette.
- **Colour:** matches the locked 7-colour palette.
- **Required customisation:** none identified for the floor lamps; the optional feature lighting (X15) has no confirmed specification at all yet.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** not required for catalogue floor lamps.
- **Certification requirements:** SAA electrical mark.
- **Factory requirements:** demonstrated experience manufacturing commercial dimmable lighting.
- **Sample requirements:** factory sample of the fitting and dimming behaviour.
- **QC requirements:** pre-shipment inspection.
- **Packaging requirements:** export-grade packaging suitable for sea freight, not yet confirmed.
- **Freight requirements:** not yet quoted.
- **Installation requirements:** no, freestanding floor lamps, standard GPO only.
- **Warranty requirements:** not yet determined, must be obtained at quote stage.
- **Note:** functional/task lighting throughout the venue (Section X generally) remains an Australian professional-verification item (electrician/lighting designer), not a China sourcing candidate, since it must be specified against the confirmed site's own electrical design. Only the decorative/ambient items above are China candidates.

## Sourcing Group 6: Furniture (General)

- **Items included:** Lounge side tables, Lounge coffee tables, staff lockers (pending final headcount), storage shelving.
- **Item IDs:** D02, D03, L01, M01, M03, M04.
- **Quantity:** per the master register's own figures for each Item ID.
- **Functional specification:** commercial-duty Lounge furniture (heavy daily use), standard-duty BOH storage.
- **Dimensions:** not yet determined for most items; standard catalogue dimensions expected, confirm against the final floor plan.
- **Material:** not yet determined beyond "matches the locked palette" for Lounge furniture; storage shelving is typically metal or laminate, not yet specified.
- **Finish:** matches the locked palette for Lounge furniture; storage shelving finish not yet specified (not client-facing).
- **Colour:** matches the locked 7-colour palette for Lounge furniture; storage shelving colour not palette-constrained since it is back-of-house.
- **Required customisation:** none identified.
- **Reference image requirement:** yes for Lounge furniture, not yet selected; not required for BOH storage shelving.
- **Technical drawing requirement:** not required for catalogue items.
- **Certification requirements:** none identified beyond general consumer product safety.
- **Factory requirements:** demonstrated commercial-furniture manufacturing capability for Lounge items; general furniture/shelving manufacturer acceptable for BOH storage.
- **Sample requirements:** factory sample for finish (Lounge items only).
- **QC requirements:** pre-shipment inspection.
- **Packaging requirements:** flat-pack likely for shelving, assembled or flat-pack for Lounge furniture, not yet decided.
- **Freight requirements:** not yet quoted.
- **Installation requirements:** no, freestanding.
- **Warranty requirements:** not yet determined, must be obtained at quote stage.

## Sourcing Group 7: Treatment Furniture

- **Items included:** Massage table (Option A, if the table/bed format is confirmed), Beauty treatment bed.
- **Item IDs:** F01a, G01.
- **Quantity:** 2-3 each, per the current venue program.
- **Functional specification:** Massage table: face hole plus side cutouts, vinyl surface. Beauty bed: electric adjustable, vinyl surface.
- **Dimensions:** not yet determined.
- **Material:** vinyl, wipe-clean.
- **Finish:** wipe-clean, matches the palette.
- **Colour:** matches the locked 7-colour palette.
- **Required customisation:** none identified beyond palette-matched finish.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** not required for catalogue items.
- **Certification requirements:** SAA electrical mark for the Beauty bed's electric recline mechanism; general consumer product safety for the Massage table (non-electric).
- **Factory requirements:** demonstrated experience manufacturing commercial treatment/massage furniture, not domestic furniture.
- **Sample requirements:** vinyl-grade material sample, factory sample of the full unit.
- **QC requirements:** pre-shipment inspection.
- **Packaging requirements:** export-grade packaging suitable for sea freight, not yet confirmed.
- **Freight requirements:** not yet quoted.
- **Installation requirements:** no, freestanding.
- **Warranty requirements:** not yet determined, must be obtained at quote stage; particularly important for the Beauty bed's electric recline mechanism.
- **Mandatory Australian reference unit:** an Australian-sourced comparison unit should be obtained before committing to a China-sourced Massage table, per the existing sourcing strategy's own disclosed caution.
- **Founder decision note:** the Massage table itself only proceeds to RFQ if the table/bed format is confirmed as the chosen format; see `docs/architecture/PROCUREMENT-FOUNDER-DECISIONS.md`. This is not silently resolved here.

## Sourcing Group 8: Pedicure Furniture

- **Items included:** pipeless pedicure spa chair.
- **Item IDs:** I01.
- **Quantity:** 4.
- **Functional specification:** pipeless/no-jet design mandatory for hygiene (no hidden jets that can trap bacteria).
- **Dimensions:** not yet determined, standard pedicure-chair footprint, exact spacing depends on the final floor plan.
- **Material:** wipe-clean upholstery, plumbing fittings for the built-in basin.
- **Finish:** matches the locked palette.
- **Colour:** matches the locked 7-colour palette.
- **Required customisation:** none identified; the pipeless design itself is the critical functional requirement, not a cosmetic customisation.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** not required for a catalogue pipeless unit.
- **Certification requirements:** CE/SAA electrical mark, pipeless design confirmed before order.
- **Factory requirements:** demonstrated experience manufacturing pipeless pedicure spa chairs specifically, not a generic salon-furniture factory claiming pipeless capability without evidence.
- **Sample requirements:** material sample, factory confirmation of the pipeless design specifically (not merely claimed in a product listing).
- **QC requirements:** pre-production approval, pre-shipment inspection.
- **Packaging requirements:** export-grade packaging suitable for sea freight, not yet confirmed.
- **Freight requirements:** not yet quoted; plumbing fittings add weight/bulk relative to a simple chair.
- **Installation requirements:** yes, water supply/drain connection per chair, licensed plumber required on-site regardless of the chair's manufacturing origin.
- **Warranty requirements:** replacement-parts availability (motor/plumbing fittings, jets/pumps are not applicable to this design) should be confirmed as locally available or importable before order; warranty term itself not yet determined.
- **This is the single highest-confidence quantified China-sourcing saving in the entire register** (A$500-1,500 China-sourced vs A$800-2,000 Australian).

## Sourcing Group 9: Decorative Hardware

- **Items included:** decorative mirrors (optional), planters (optional).
- **Item IDs:** W09, W10.
- **Quantity:** 2-4 each.
- **Functional specification:** decorative use only, matches the locked palette.
- **Dimensions:** not yet determined.
- **Material:** not yet determined.
- **Finish:** matches the locked palette.
- **Colour:** matches the locked 7-colour palette.
- **Required customisation:** none identified.
- **Reference image requirement:** yes, not yet selected.
- **Technical drawing requirement:** not required.
- **Certification requirements:** none identified, decorative items only.
- **Factory requirements:** general commercial-decor manufacturer acceptable.
- **Sample requirements:** finish sample.
- **QC requirements:** pre-shipment inspection on the full order.
- **Packaging requirements:** standard export packaging, not yet confirmed.
- **Freight requirements:** not yet quoted; low priority given these are Future/Optional items in the master register.
- **Installation requirements:** no, freestanding/decorative placement.
- **Warranty requirements:** not applicable, low-value decorative items.

## Sourcing Group 10: Other Suitable Commercial Fit-Out Items

- **Items included:** tablet mounts, cable management/charging stations, general cleaning equipment (vacuum, mop systems, buckets), clean linen storage.
- **Item IDs:** D06, B14, B17, O01, O02, O03, O04, M01.
- **Quantity:** per the master register's own figures for each Item ID.
- **Functional specification:** varies by item; commercial-duty cleaning equipment, standard tablet mounts/cable management.
- **Dimensions:** not yet determined for most items.
- **Material:** not yet determined.
- **Finish:** not palette-constrained for BOH cleaning equipment; tablet mounts/cable management in client-facing areas should match the palette where visible.
- **Colour:** matches the locked 7-colour palette where client-visible; not constrained for BOH items.
- **Required customisation:** none identified.
- **Reference image requirement:** yes for client-visible items (tablet mounts), not required for BOH cleaning equipment.
- **Technical drawing requirement:** not required for catalogue items.
- **Certification requirements:** electrical safety mark where applicable (tablet mounts with charging, cable management with power).
- **Factory requirements:** general commercial-equipment manufacturer acceptable.
- **Sample requirements:** not required for standard catalogue cleaning equipment; factory sample for tablet mounts/cable management finish.
- **QC requirements:** standard factory confirmation and pre-shipment inspection for bulk orders.
- **Packaging requirements:** standard export packaging, not yet confirmed.
- **Freight requirements:** not yet quoted; this group is a bulk, lower-value consolidation candidate within a larger China order.
- **Installation requirements:** no for freestanding cleaning equipment; tablet mounts may require minor fixing, no licensed trade required.
- **Warranty requirements:** not yet determined, must be obtained at quote stage.

## What Is Explicitly Excluded From China Sourcing (Category C, Australian-Only, Unchanged From the Existing Sourcing Strategy)

Phlebotomy chairs, refrigerated centrifuge (WDP-dependent regardless), sharps containers, biohazard bins, TGA-listed disinfectant, AED, professional hair dryers/straighteners (named-brand warranty reasons), all clinical/regulated/fire-life-safety items.

## Every China Package Item Still Requires, Before Any RFQ Is Actually Sent

Supplier specification confirmed in writing, an approved drawing/spec, a material sample, a finish sample, factory confirmation of the specific design requirement (e.g. pipeless pedicure chairs), pre-production approval, an independent pre-shipment inspection (SGS/Bureau Veritas/QIMA, already-researched day rates in `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`), confirmed packaging suitable for sea/air freight, and a stated warranty/replacement-parts policy. This is restated per group above so each group is independently usable; this closing section is the summary, not a separate requirement. **None of this has been requested from any supplier yet.**

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md`, `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`, `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md`, `docs/architecture/PROCUREMENT-SOURCING-AGENT-BRIEF.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as a specific, packaged China RFQ structure grouping the register's own CN/HY-classified items into 10 supplier-facing packages, preserving the existing Australian-only classification for clinical/regulated/warranty-sensitive items rather than reclassifying anything to make China sourcing look more comprehensive than it should be.

**2026-08-23 (expanded):** Per direct founder instruction (Part 6), expanded every group to the full field set an actual sourcing agent would need (functional specification, dimensions, material, finish, colour, required customisation, reference image requirement, technical drawing requirement, certification, factory requirements, sample requirements, QC requirements, packaging requirements, freight requirements, installation requirements, warranty requirements), stating "not yet determined" honestly wherever the repository has no basis rather than inventing a plausible-looking value.
