# Plain-English Shopping List

Status: current as of 2026-08-23. A non-expert view of `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, in the format CATEGORY / PURCHASE / QUANTITY / SPECIFICATION / SOURCE / ACTION / PURCHASE WHEN, so someone without procurement or clinical background can understand what to buy, how many, and what to do next.

**Scope, stated honestly:** this covers the 6 areas the founder specifically named (Blood Collection, Nail, Hair, Cafe, Massage, Beauty), consolidating related consumables (nail polishes, hair products, PPE lines) into single rows for readability, with register IDs kept in brackets so each row traces back to the exact source rows. It does not restate all 281 items in this format; the remaining 20 categories (Reception, Lounge, Staff Area, Storage, Toilets, Cleaning, Signage, Lighting, IT, and others) stay in the master register's own technical format, which is already usable, just not translated into this plain-English layout.

**PURCHASE WHEN** below uses the phase names from `docs/architecture/PROCUREMENT-DEPENDENCY-MAP.md`.

## Blood Collection

| CATEGORY | PURCHASE | QUANTITY | SPECIFICATION | SOURCE | ACTION | PURCHASE WHEN |
|---|---|---|---|---|---|---|
| Furniture | Phlebotomy chairs [E01, E02] | 2 (day-one), 3rd held for growth [E03] | Reclines flat, wipe-clean vinyl, wide seat | Named Perth medical-furniture brand (Sunflower Medical, Alphatec Australia, Ultramedic) | Order once venue confirmed | Phase 3 (Fit-Out) |
| Furniture | Fainting-recovery couch, desk, stool [E04-E06] | 1 couch, 1 desk, 2 stools | Full-recline couch; standard clinical desk/stool | Australian medical-furniture retailer | Order | Phase 3 |
| Storage | Lockable medical cabinet and document drawer [E07, E08] | 1 each | Standard clinical storage, privacy-compliant | Australian retailer | Order | Phase 3 |
| Sharps and waste | Sharps containers, biohazard bins, waste disposal contract [E09-E12, E14] | 2 bench + 2 room sharps containers, 2 biohazard bins, 1 waste contract | AS/NZS 23907:2023 compliant | Daniels Health, Cleanaway Medical, or Stericycle | Order containers now; confirm waste contract once WDP's own arrangement is clarified | Waste contract Phase 2, containers Phase 3 |
| Critical equipment | Refrigerated centrifuge [E15] | 1 | 3,000 RPM minimum, 8+ position rotor | Sourced through the WDP relationship, not general retail | Do not purchase independently, wait for WDP confirmation | Phase 2 (WDP dependent) |
| Equipment | Specimen fridge, transport bags, ice packs, label printer [E16-E19] | 1 fridge, 2 bags, 6 ice packs, 1 printer | 2-8C cold chain, temperature-logged | Australian medical retailer | Order | Phase 3 |
| Consumables | Pathology collection consumables and glucose drink [E20, E21] | Ongoing | GTT-specific (fluoride-oxalate tubes), commercially prepared glucose solution | Largely WDP-supplied; glucose drink confirm with WDP | Hold pending WDP's commercial arrangement | Phase 2 |
| PPE and hygiene | Gloves, masks, hand sanitiser, soap, paper towel [E22, E23, E25-E27] | Ongoing consumable | AS/NZS-compliant | Australian medical/hygiene supplier | Order as part of opening stock | Phase 5 (Opening Stock) |
| Cleaning | TGA-listed disinfectant, blood spill kit, clinical wipes [E28-E30] | Ongoing | TGA-listed, effective against blood-borne pathogens | Australian clinical-cleaning supplier | Order as part of opening stock | Phase 5 |
| Fit-out | Room construction, curtain partitions, signage, emergency call button, ventilation [E31-E36, E38] | 1 room, 2-3 curtains | Solid walls, 6 ACH ventilation, AS/NZS signage | Builder, licensed electrician, HVAC contractor | Site quote required | Phase 1-2 |
| Staff | Phlebotomist uniforms [E39] | 4 (employment pool) | Per staff position register | Uniform supplier | Order once headcount confirmed | Phase 2 |

## Nail

| CATEGORY | PURCHASE | QUANTITY | SPECIFICATION | SOURCE | ACTION | PURCHASE WHEN |
|---|---|---|---|---|---|---|
| Furniture | Nail tables with dust collector, technician chairs, client chairs, tool trolleys [H01-H03, H07] | 4 each | Professional grade, commercial duty | China sourcing group or Australian salon supplier (either works) | RFQ | Phase 3 |
| Equipment | UV/LED nail lamps, nail drills [H04, H05] | 4 lamps, 2-4 drills | Professional grade, SAA electrical mark | Either | RFQ | Phase 3 |
| Ventilation | LEV (extraction) unit [H06] | 1, sized for 4 stations | WorkSafe WA compliant | Licensed HVAC/LEV contractor, none identified yet | Identify a contractor first, then RFQ | Phase 2 |
| Consumables | Nail files, buffers, cuticle tools, polishes, gel polish (20+ colours), remover, wipes [H08-H17] | Ongoing, opening lot | 9-free formula polishes | China (tools/basics) or Australia (polish, remover) | Order as opening stock | Phase 5 |
| PPE and cleaning | Gloves, N95 dust masks, disinfection solution [H18-H20] | Ongoing | AS/NZS-compliant | Australian supplier | Order as opening stock | Phase 5 |
| Electrical | GPO per station [H21] | 4 | Licensed electrician | Australian licensed electrician | Site quote required | Phase 2 |

## Hair

| CATEGORY | PURCHASE | QUANTITY | SPECIFICATION | SOURCE | ACTION | PURCHASE WHEN |
|---|---|---|---|---|---|---|
| Furniture | Styling chairs, mirror, tool trolleys [J01, J02, J15] | 4 chairs, 1 mirror (custom-fit), 4 trolleys | Hydraulic, wipe-clean; mirror spans 4 chairs | Either for chairs/trolleys; mirror is site-dependent (final wall length) | RFQ chairs/trolleys now; mirror once venue measured | Phase 3 (chairs), Phase 1-2 (mirror) |
| Equipment | Professional hair dryers and straightening irons [J03, J04] | 4 each | Named brand (Dyson, GHD, Cloud Nine) | Australian direct trade account, not China-sourced (warranty reasons) | Order | Phase 3 |
| Equipment | Curling tools, clippers [J05, J06] | 2-4 curling tools; clippers only if offered as a service | SAA electrical mark | Australian retailer | Confirm clippers against current service catalogue before ordering | Phase 0 (decision), Phase 3 (order) |
| Consumables | Brushes, combs, capes, towels, shampoo, conditioner, treatment/styling products [J07-J13] | Ongoing, opening lot | Pregnancy-safe formulations | China (tools) or Australia (hair products) | Order as opening stock | Phase 5 |
| Colour equipment | Colour bowls, brushes, foils, capes [J14] | 1 lot, only if colour services confirmed | Product safety | Either | Confirm against the service catalogue before ordering | Phase 0 (decision), Phase 3 (order) |
| Waste and PPE | Hair waste bin, disposable gloves [J16, J17] | 1-2 bins, ongoing gloves | Lidded bin | Either | Order as opening stock | Phase 5 |
| Electrical | GPO near each chair [J18] | 4 | Licensed electrician | Australian licensed electrician | Site quote required | Phase 2 |

## Cafe

| CATEGORY | PURCHASE | QUANTITY | SPECIFICATION | SOURCE | ACTION | PURCHASE WHEN |
|---|---|---|---|---|---|---|
| Equipment | Beverage fridge, display fridge, coffee machine, chilled/boiling water tap, toastie press [C01-C05] | 1 each | Commercial grade, food-safety cold-chain | Australian commercial-kitchen retailer (fridges/tap); either for coffee machine/toastie press | Order | Phase 3 |
| Storage and food safety | Food containers, fridge thermometers, food-handling gloves, chopping boards [C06-C09] | 1 lot; 2 thermometers | Commercial food-grade | Either | Order as opening stock | Phase 5 |
| Crockery and takeaway | Cups, plates, takeaway cups/lids, napkins, cutlery [C10-C15] | 24-36 cups, 12-24 plates, ongoing takeaway lot | Ceramic dine-in; compostable/recyclable takeaway | China (takeaway items) or either (crockery) | Order as opening stock | Phase 5 |
| Display and POS | Display shelving, menu board, POS (shares Reception's terminal) [C16-C18] | 1 each | Matches locked brand palette | Either; menu board gated on final venture name | Order shelving now; hold menu board until the name is confirmed | Phase 3 (shelving), Phase 0 (name decision) |
| Fit-out | Prep/serving counter, handwashing station [C19, C20] | 1 each | Site-installed, food-business hygiene standard | Local trade, licensed electrician/plumber | Site quote required | Phase 1-2 |
| Waste | Cafe-specific food-waste bin [C21] | 1-2 | Lidded, foot-pedal | Either | Order as opening stock | Phase 5 |
| Food supplier | Pre-made sandwiches/rolls, coffee beans/milk, herbal tea, cold drinks [C22-C25] | Ongoing | External food supplier not yet identified (genuine dependency); coffee/tea/drink suppliers not yet selected | Suppliers to be identified, none contacted | Identify suppliers first, this is a business-development task, not a standard RFQ | Phase 0-1 |
| Compliance | Food Business Notification [C26] | 1 filing | WA Food Act 2008, at least 14 days before trading | Local council | File once venue and menu are confirmed | Phase 2 |

## Massage

| CATEGORY | PURCHASE | QUANTITY | SPECIFICATION | SOURCE | ACTION | PURCHASE WHEN |
|---|---|---|---|---|---|---|
| Furniture | Massage table or chair, format not yet decided [F01a/F01b] | 2 day-one, up to 3 growth | Table: face hole + side cutouts, vinyl. Chair: no spec exists yet | Table is hybrid (China + mandatory Australian reference unit); chair format needs fresh research if adopted | Resolve the table-vs-chair founder decision first | Phase 0 (decision), then Phase 3 (order) |
| Equipment | Bolster sets, heated blankets, trolleys [F02, F03, F05] | 2-3 sets, 4 blankets, 2-3 trolleys | Electric blanket, machine-washable | Either | RFQ | Phase 3 |
| Optional | Oil warming units [F04] | 2-3, optional | Electrical safety mark | Either | Defer, future/optional | Phase 7 (revisit post-opening) |
| Linen and consumables | Table linen, pregnancy-safe massage oil, aromatherapy items [F06-F08] | 2 sets/station, 5L oil bulk | Lavender/mandarin/chamomile only | Australian for oil; either for linen | Order as opening stock | Phase 5 |
| Fit-out | Curtain partitions, task lighting [F09, F10] | 2-3 each | Washable fabric, warm dimmable lighting | Either | RFQ, lighting per Section X | Phase 3 |
| PPE | Table-roll paper barrier [F11] | Ongoing | Infection control | Either | Order as opening stock | Phase 5 |
| Staff | Practitioner apron/uniform [F12] | 6 (employment pool) | Per staff position register | Uniform supplier | Order once headcount confirmed | Phase 2 |

## Beauty

| CATEGORY | PURCHASE | QUANTITY | SPECIFICATION | SOURCE | ACTION | PURCHASE WHEN |
|---|---|---|---|---|---|---|
| Furniture | Treatment beds, practitioner stools, magnifying lamps [G01-G03] | 2 day-one, up to 3 growth beds; 2-3 stools/lamps | Electric adjustable bed, SAA electrical mark | Either | RFQ | Phase 3 |
| Equipment | Wax heater, brow/lash tool kits [G04, G05] | 1 wax heater, 2-3 tool sets | Dual-pot professional wax heater | Either | Order | Phase 3 |
| Optional | Facial steamer [G06] | 0-1, only if deeper facials offered | SAA electrical mark | Either | Confirm against the service catalogue before ordering | Phase 0 (decision) |
| Storage | Trolleys [G07] | 2-3 | N/A | Either | Order | Phase 3 |
| Hygiene fit-out | 2-sink hand-wash/instrument fitout [G08] | 1-2 | WA Skin Penetration Code, hands-free tap | Licensed hydraulic trade | Site quote required | Phase 1-2 |
| Consumables | Treatment bed linen, PPD-free brow tint, wax, facial products, disposables [G09-G13] | Ongoing, opening lot | Pregnancy-safe formulations throughout | Australian for tint/wax/facial products; either for linen/disposables | Order as opening stock | Phase 5 |
| Electrical | GPO and task lighting per station [G14] | 2-3 | Licensed electrician | Australian licensed electrician | Site quote required | Phase 2 |
| Staff | Practitioner uniform [G15] | Staff-dependent | Shared with Massage where dual-qualified | Uniform supplier | Order once headcount confirmed | Phase 2 |

## What This List Deliberately Does Not Include

Any snack pack, spray tan service, or service not currently confirmed in the service catalogue. Prices are not repeated here; the master register carries the priced/unpriced status per item, this list is for what to buy and when, not what it costs.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/PROCUREMENT-DEPENDENCY-MAP.md`, `docs/architecture/PROCUREMENT-FOUNDER-DECISIONS.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 9) as the plain-English, non-expert shopping list view for the 6 explicitly emphasized areas (Blood Collection, Nail, Hair, Cafe, Massage, Beauty), consolidating related consumables for readability while preserving register-ID traceability. Scope limitation to these 6 areas stated explicitly rather than silently narrowing the founder's full-register request.
