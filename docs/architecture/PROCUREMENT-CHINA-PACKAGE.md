# China Procurement Package

Status: current as of 2026-08-23. Built from the China-candidate (CN) and hybrid (HY) items already classified in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (42 CN, 93 HY). No item is assumed safe to import simply because it is furniture; clinical, regulated, and fire/life-safety items remain excluded per `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`'s existing classification. **No supplier or sourcing agent has been contacted. No order, RFQ, or sample request has been sent.**

## Sourcing Group 1: Reception/Cafe Joinery-Adjacent Furniture (not the structural joinery itself)

**Items:** retail display shelving (B18, pending the retail founder decision), customer-accessible Cafe display shelving (C16). **Quantity:** 1 each. **Material/finish:** matches the locked 7-colour palette (`outputs/brand/warm-stone-tokens.css`), warm stone/timber tones. **Packaging:** flat-pack or assembled, freight-dependent. **Commercial-use requirement:** commercial-duty shelving, not domestic-grade. **Certification:** none beyond general consumer product safety. **Australian electrical requirement:** none (non-electrical items). **QC requirements:** factory sample of the finish/material before full production; pre-shipment inspection on the full order.

## Sourcing Group 2: Nail Stations

**Items:** H01 (nail table with dust collector), H07 (nail tool trolley). **Quantity:** 4 each. **Specification:** professional grade, built-in dust collector, cable management, durable cleanable surface. **Material/finish:** matches the locked palette. **Dimensions:** to be confirmed against the final floor plan (Section H of the master register). **Commercial-use requirement:** commercial salon duty, not domestic. **Certification:** electrical safety mark (SAA) for the built-in dust collector. **Australian electrical requirement:** the dust collector must meet Australian electrical safety standards even if manufactured overseas; confirm with an Australian-based sourcing agent or electrician before purchase. **QC requirements:** factory sample, pre-production approval, pre-shipment inspection.

## Sourcing Group 3: Hair Styling Stations

**Items:** J01 (styling chair, hydraulic), J15 (tool trolley). **Quantity:** 4 each. **Specification:** hydraulic, wipe-clean upholstery. **Material/finish:** matches the locked palette. **Commercial-use requirement:** commercial salon duty. **Certification:** AS/NZS 4088 stability standard. **Excluded from this package:** professional hair dryers and straightening irons (J03/J04) remain Australian-sourced via direct trade accounts (Dyson, GHD, Cloud Nine), poor import candidates on warranty grounds, per the existing sourcing strategy, not reclassified here.

## Sourcing Group 4: Mirrors

**Items:** J02 (salon mirror, lighted, full-length). **Quantity:** 1 (spans 4 chairs). **Specification:** custom-fit to the venue's actual wall length once measured, LED strip lighting, warm colour temperature matching the palette. **Certification:** SAA electrical mark for the integrated LED strip. **Note:** dimensions cannot be finalised before a venue is confirmed (site-dependent, see `PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`); this sourcing group's item is RFQ-ready in specification but not yet orderable in final size.

## Sourcing Group 5: Decorative Lighting

**Items:** D04 (Lounge floor lamps), X15 (feature/decorative lighting, optional). **Quantity:** 4 (floor lamps), remainder optional. **Specification:** warm, dimmable, matches the locked palette. **Certification:** SAA electrical mark. **Note:** functional/task lighting throughout the venue (Section X) generally remains an Australian professional-verification item (electrician/lighting designer), not a China sourcing candidate, since it must be specified against the confirmed site's own electrical design.

## Sourcing Group 6: Furniture (General)

**Items:** D02/D03 (Lounge side tables, coffee tables), L01 (staff lockers, pending final headcount), M01/M03/M04 (storage shelving). **Quantity:** per the master register's own figures. **Material/finish:** matches the locked palette. **Commercial-use requirement:** commercial duty for Lounge furniture (heavy daily use), standard for BOH storage. **QC requirements:** factory sample for finish, pre-shipment inspection.

## Sourcing Group 7: Treatment Furniture

**Items:** F01a (Massage table, if the table/bed format is confirmed, a genuine founder decision, `PROCUREMENT-FOUNDER-DECISIONS.md`), G01 (Beauty treatment bed). **Quantity:** 2-3 each, per the current venue program. **Material/finish:** vinyl, wipe-clean, matches the palette. **Certification:** SAA electrical mark for the electric recline mechanism (Beauty bed); general consumer product safety for the Massage table. **Mandatory Australian reference unit:** an Australian-sourced comparison unit should be obtained before committing to a China-sourced Massage table, per the existing sourcing strategy's own disclosed caution. **QC requirements:** material sample (vinyl grade), factory sample, pre-shipment inspection.

## Sourcing Group 8: Pedicure Furniture

**Items:** I01 (pipeless pedicure spa chair). **Quantity:** 4. **Specification:** pipeless/no-jet design mandatory for hygiene (no jets that can trap bacteria). **Certification:** CE/SAA electrical mark, pipeless design confirmed before order. **This is the single highest-confidence quantified China sourcing saving in the entire register** (A$500-1,500 China-sourced vs A$800-2,000 Australian). **QC requirements:** factory confirmation of the pipeless design specifically (not merely claimed in a listing), material sample, pre-production approval, pre-shipment inspection, replacement-parts availability confirmed before order (jets/pumps are not applicable to this design, but motor/plumbing fittings should have confirmed local or importable replacement parts).

## Sourcing Group 9: Decorative Hardware

**Items:** W09 (decorative mirrors, optional), W10 (planters, optional). **Quantity:** 2-4 each. **Specification:** matches the locked palette. **Commercial-use requirement:** low, decorative use only. **QC requirements:** finish sample.

## Sourcing Group 10: Other Suitable Commercial Fit-Out Items

**Items:** D06 (tablet mounts), B14/B17 (cable management, charging stations), O01-O04 (general cleaning equipment: vacuum, mop systems, buckets), M01 (clean linen storage). **Quantity:** per the master register. **Certification:** electrical safety mark where applicable. **QC requirements:** standard factory confirmation and pre-shipment inspection for bulk orders.

## What is explicitly excluded from China sourcing (Category C, Australian-only, unchanged from the existing sourcing strategy)

Phlebotomy chairs, refrigerated centrifuge (WDP-dependent regardless), sharps containers, biohazard bins, TGA-listed disinfectant, AED, professional hair dryers/straighteners (named-brand warranty reasons), all clinical/regulated/fire-life-safety items.

## Every China package item still requires, before any RFQ is actually sent

Supplier specification confirmed in writing, an approved drawing/spec, a material sample, a finish sample, factory confirmation of the specific design requirement (e.g. pipeless pedicure chairs), pre-production approval, an independent pre-shipment inspection (SGS/Bureau Veritas/QIMA, already-researched day rates in `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`), confirmed packaging suitable for sea/air freight, and a stated warranty/replacement-parts policy. **None of this has been requested from any supplier yet.**

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`, `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as a specific, packaged China RFQ structure grouping the register's own CN/HY-classified items into 10 supplier-facing packages, preserving the existing Australian-only classification for clinical/regulated/warranty-sensitive items rather than reclassifying anything to make China sourcing look more comprehensive than it should be.
