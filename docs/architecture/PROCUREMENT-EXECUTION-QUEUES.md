# Procurement Execution Queues

Status: current as of 2026-08-23. Built directly from `docs/architecture/PROCUREMENT-EXECUTION-MATRIX.md` and `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`. This document does not reclassify any item; it splits the existing 281 items into 5 practical execution queues and, for Queue 1 specifically, applies a real practicality check beyond the Readiness A label (storage location, subscription timing), per direct founder instruction not to treat "Order Ready" as automatically "should be bought today."

## Queue 1: Buy Now

All 39 Readiness-A items pass the structural test (locked specification and quantity, already priced, no venue/site/professional/WDP/founder blocker). They are split below into 3 practical tiers based on a genuine question: is there anywhere to receive and store this item today, and is there any cost-timing reason to wait.

### Tier 1a: Genuinely buy now, no reason to delay

Small, portable, no meaningful storage burden, no recurring-cost timing issue.

| Item ID | Item | Qty | Min spec | Preferred spec | Source | Consumable/Durable | Shelf-life issue | Storage risk | Reason to delay |
|---|---|---|---|---|---|---|---|---|---|
| B03 | Computer/laptop | 1 | Business-grade laptop, current OS | Per JB Hi-Fi/Officeworks business account range | AU | Durable | No | No | None |
| B08 | iPad (9th gen or Air) | 2 | 9th gen or newer | Air, for longevity | AU | Durable | No | No | None |
| B09 | iPad kiosk stand | 2-3 | Secure countertop stand | Matches locked palette | AU | Durable | No | No | None |
| B10 | B&W laser printer | 1 | Business-grade laser | Networked model | AU | Durable | No | No | None |
| T01 | WiFi router (commercial grade) | 1 | Business-grade router | Ubiquiti/TP-Link business range | AU | Durable | No | No | None |
| E19 | Thermal label printer | 1 | Zebra ZD420 or equivalent | Zebra ZD420 | AU | Durable | No | No | None |
| R02 | First aid kit (comprehensive) | 2 | WorkSafe-compliant kit | Same | AU | Durable (contents expire, kit does not) | Yes, kit contents have use-by dates | No | Consider ordering close enough to opening that contents are not already aged when the venue opens |
| E17 | Insulated specimen transport bag | 2 | Cold-chain rated | Same | AU | Durable | No | No | None |
| E18 | Ice packs (reusable, cold chain) | 6 | Reusable, food/medical grade | Same | AU | Durable | No | No | None |
| E29 | Blood spill kit | 2 | Infection-control standard kit | Same | AU | Durable (some contents expire) | Yes, check kit expiry date at purchase | No | Buy close to opening if the kit has a short shelf life; confirm expiry date before ordering |
| E09 | Sharps container, bench size (1.4L) | 2 | AS/NZS 23907:2023 | Same | AU | Consumable | No | No | None |
| E10 | Sharps container, room size (5L) | 2 | AS/NZS 23907:2023 | Same | AU | Consumable | No | No | None |
| E11 | Wall-mounted sharps container bracket | 2 | Standard bracket | Same | AU | Durable | No | No | None |
| D09 | Curated reading material | 1 lot | General pregnancy/postnatal interest | Curated to brand tone | AU | Durable | No | No | None |

### Tier 1b: Buy now, but delay activation/billing

| Item ID | Item | Qty | Reason to delay |
|---|---|---|---|
| B13 | Booking software subscription (Fresha) | 1 | The item itself (account setup) can be actioned now, but activating a paid monthly subscription before the venue is trading burns ongoing SaaS cost for no revenue. Recommend setting up the account now if useful for pre-opening admin, but not starting the paid tier until closer to opening. |

### Tier 1c: Structurally order-ready, but genuinely better to hold for storage/delivery reasons

These items pass every specification/pricing/dependency test but are bulky furniture or fixed equipment with nowhere to be delivered or stored until a venue exists. Ordering now would require paying for and arranging interim storage, a real cost the register itself does not price. **Recommendation: treat these as "ready to order the moment a venue is secured," not "buy this week."**

| Item ID | Item | Qty | Reason |
|---|---|---|---|
| C01 | Full-size beverage refrigerator | 1 | Bulky, requires powered storage space |
| C02 | Display refrigerator | 1 | Bulky, requires powered storage space |
| C03 | Coffee machine | 1 | Moderate size, benefits from being installed once, not moved |
| C04 | Chilled and boiling water tap | 1 | Requires a plumbed connection; no benefit to holding stock before install is possible |
| C05 | Toastie press | 1 | Low storage risk, but no benefit ordering before the Cafe counter is built |
| C16 | Customer-accessible display shelving | 1 | Bulky, palette-matched to a specific space not yet measured |
| D04 | Floor lamp (soft, warm) | 4 | Low individual bulk but 4 units add up; low urgency |
| B07 | POS terminal | 2 | No benefit activating a payment terminal before trading; provider account setup can start, hardware can wait |
| E01 | Phlebotomy chair (Chair A) | 1 | Bulky, clinical furniture, best delivered directly to the fitted-out room |
| E02 | Phlebotomy chair (Chair B) | 1 | Same as E01 |
| E04 | Vasovagal recliner/exam couch | 1 | Bulky clinical furniture |
| E07 | Medical consumables cabinet (lockable) | 1 | Bulky, better installed once room fit-out is underway |
| E08 | Patient documentation drawer (lockable) | 1 | Same as E07 |
| E12 | Biohazard waste bin (yellow, lidded) | 2 | Low bulk individually, no benefit ordering before the room exists |
| G04 | Wax heater (dual-pot, professional) | 1 | Low bulk, but no benefit ordering before the Beauty room exists |
| H01 | Nail table with built-in dust collector | 4 | Bulky, requires the Nail zone's electrical point already installed |
| H03 | Client manicure chair | 4 | Bulky furniture |
| H04 | UV/LED nail lamp | 4 | Low bulk individually but tied to station fit-out timing |
| H07 | Nail tool trolley | 4 | Bulky, better ordered with the rest of the Nail station set |
| I01 | Pedicure spa chair (pipeless) | 4 | Bulky, requires plumbing connection already in place |
| J01 | Styling chair (hydraulic, wipe-clean) | 4 | Bulky furniture |
| J03 | Professional hair dryer | 4 | Low bulk, but a direct-trade-account item best timed with staff onboarding |
| J04 | Straightening iron | 4 | Same as J03 |
| J15 | Tool trolley + organiser | 4 | Bulky, better ordered with the rest of the Hair station set |

## Queue 2: RFQ Now

Items quotable now without knowing the final venue, since specification and quantity are already locked (Readiness B). Grouped by who the RFQ goes to, not a flat list, so comparable quotes come back from each group.

### Group A: China Sourcing-Agent RFQs

All items in `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md` Sourcing Groups 1-2, 6, 9-10 (items not gated by a founder decision or site dimension): reception/Cafe display shelving components not already Order-Ready, general furniture (D02/D03 Lounge tables, L01 lockers pending headcount, M03/M04 storage shelving), decorative hardware (W09/W10), other commercial fit-out items (D06, B14, B17, O01-O04). **Required with the RFQ:** functional specification, material/finish matching the locked palette, reference image, certification requirement where electrical, factory QC requirement (sample, pre-production approval, pre-shipment inspection), packaging suitable for sea freight. **Landed cost required:** yes, once quotes exist, per `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §7. **Installation required:** no for these items (freestanding). **Samples required:** yes, material/finish sample before full production. **Quotable before venue selection:** yes.

### Group B: China Factory RFQs (Direct, if a Sourcing Agent Is Not Used)

Pipeless pedicure chairs (I01, highest-confidence saving in the register) and nail station items (H01, H07) if Anthony chooses direct factory contact instead of an agent. **Required:** the same specification/QC/packaging set as Group A, plus explicit factory confirmation of the pipeless design (I01 specifically). **Quotable before venue selection:** yes for specification and unit price; final quantity for I01/H01/H07 is already locked at 4 each, not site-dependent.

### Group C: Australian Supplier RFQs (Bulk Commercial Salon/Spa)

Per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 2: professional hair dryers/straighteners (J03/J04, named brand direct-trade account), UV/LED nail lamps (H04, if sourced Australian rather than China), client chairs (H03). **Required:** unit price at confirmed quantity (4 each), trade-account pricing tier, warranty term. **Quotable before venue selection:** yes.

### Group D: Australian Furniture/Equipment Suppliers

Beauty treatment beds (G01), massage tables (F01a, gated on the founder decision, see Queue 4), general Lounge/BOH furniture not already Order-Ready. **Required:** unit price, delivery timeframe, warranty. **Quotable before venue selection:** yes for G01; F01a only quotable once the table/bed format decision is made.

### Group E: Specialist Trades (Not Yet Scopeable Without a Site)

Licensed electrician, licensed plumber, HVAC/LEV contractor. **These cannot be genuinely quoted before a venue exists**, since scope depends on the confirmed floor plan. Listed here only to state explicitly why they are not in this queue; see Queue 3.

### Group F: Builder/Fit-Out RFQs Scopeable Without a Site

None. Per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3, 3 real builder quotes are explicitly gated on a confirmed, measured venue; no builder scope can be genuinely quoted before that. This is stated here as a real, checked finding, not assumed.

## Queue 3: Venue Hold

Every item blocked solely by not having a venue (Readiness C, 24 items) is already itemised with its exact measurement/confirmation requirement in `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`; not re-researched here. The sequence immediately after securing a venue:

| Step | Action | Owner | Depends On |
|---|---|---|---|
| 1 | Site measurement (full floor plate, room dimensions, ceiling heights) | Venue Manager once hired, or Anthony/builder in the interim | Venue secured (lease signed) |
| 2 | Service/utility verification (existing power capacity, existing plumbing/drainage, existing HVAC plant) | Licensed electrician, licensed plumber, HVAC contractor | Step 1 |
| 3 | Electrical assessment (GPO count/placement per room, LEV/dust-collector power draw, lighting circuit capacity) | Licensed electrician | Step 1 |
| 4 | Plumbing/hydraulic assessment (Cafe water tap, clinical hand-hygiene sink, Hair Wash basins, Pedicure chair plumbing) | Licensed plumber | Step 1 |
| 5 | HVAC/LEV assessment (Nail Station extraction, Blood Collection Room 6 ACH, general HVAC capacity) | HVAC/LEV contractor (not yet identified, see Queue 5) | Steps 1, 3 |
| 6 | Accessibility assessment (AS 1428.1 clearances, accessible WC fittings) | Access consultant or building surveyor | Step 1 |
| 7 | Clinical requirements verification (Blood Collection Room final layout, WDP sign-off on the room) | WDP, per `docs/architecture/PROCUREMENT-CLINICAL-GTT-WDP-SPLIT.md` Category D | Steps 1, 3, 4, 5 |
| 8 | Food/Cafe requirements verification (Food Business Notification tier, EHO confirmation) | Local council Environmental Health Officer | Step 1, menu locked |
| 9 | Furniture/layout confirmation (final Lounge seating count, mirror dimensions, joinery dimensions) | Venue Manager once hired, or Anthony | Step 1 |
| 10 | Builder RFQs (3 real, independent quotes) | Anthony, via `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3 | Steps 1-9 |
| 11 | Final equipment quantities locked (toilet-count-dependent consumables, exact Lounge seating, mirror size) | Venue Manager once hired, or Anthony | Steps 1-10 |
| 12 | Procurement release (Queue 3 items move to Queue 2, RFQ Now) | Anthony | Step 11 |

## Queue 4: Founder Decisions

Reviewed against `docs/architecture/PROCUREMENT-FOUNDER-DECISIONS.md` and the current authoritative venue-program documents. Only genuinely still-open decisions are listed; already-settled ones are not reopened.

| Decision | Options | Recommendation | Cost Impact | Operational Impact | Procurement Impact | Blocks Other Procurement? | Blocks Venue? | Urgent? |
|---|---|---|---|---|---|---|---|---|
| Massage station format (table/bed vs chair-based) | Table/bed (F01a) vs chair-based (F01b) | None forced; genuinely unlocked, no repository basis exists for a chair-based spec | Table A$800-2,500 AU / A$300-800 China; chair format entirely unpriced | Affects treatment delivery method for all Massage services | Blocks F01a/F01b RFQ (Queue 2 Group D item), blocks the Massage station furniture order | No | **Yes, should be resolved before RFQ, since specification differs entirely between options** |
| Laundry model (in-house vs outsourced) | In-house wash vs outsourced contract | None forced; genuinely unconfirmed | Affects whether laundry equipment/detergent is purchased at all | Affects linen/towel turnover timing across Massage, Beauty, Hair Wash | Blocks the laundry detergent opening-stock line (`PROCUREMENT-OPENING-STOCK-SCHEDULE.md`) | No | Can wait until closer to opening, not urgent now |
| Hand dryer vs paper towel (toilets) | Hand dryer (N08) vs paper towel | Paper towel recommended as current default | Low cost difference | Low | Blocks N08 specifically, a single low-value item | No | Not urgent, can be decided any time before opening stock is ordered |
| Facial steamer (deeper facials) | Purchase (G06) vs not offered | No recommendation forced, service-scope dependent | A$150-350 | Determines whether "deeper facials" are a real service offering | Blocks G06 only | No | Not urgent |
| Colour hair services | Offer (J14 equipment) vs not offered | No recommendation forced; current confirmed service list does not include colour | A$ range not itemised until confirmed | Determines whether colour equipment/training is needed | Blocks J14 only | No | Not urgent |
| Hair clippers | Offer (J06) vs not offered | No recommendation forced; current confirmed service list does not include clipper services | Low cost | Low | Blocks J06 only | No | Not urgent |
| Retail brand selection | Various | Deferred, not a priority | Low | Low | Blocks B18 (retail display shelving) sizing only | No | Not urgent |

**Not reopened, already settled:** Beauty station count (3, recommended matching Massage, Round 3, carried forward as-is, no new evidence changes this); China/Australia procurement model (Hybrid, standing recommendation); Blood Collection Room count (1 room, built for 3 chairs, recommended, Round 3). **Verified this round against `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`:** Massage format is confirmed still genuinely open ("format open" stated explicitly in that document); Beauty station count is confirmed as "Recommended" (pending sign-off) not "genuinely unresolved", consistent with its existing treatment, not reopened here.

**Most urgent:** the Massage table-vs-chair format, since it is the only Queue 4 item that directly blocks an RFQ that would otherwise be ready to send today (Queue 2 Group D). Every other Queue 4 decision affects a single low-value item or can wait until closer to opening without blocking anything else.

## Queue 5: External Dependencies

| Party | What We Need | Why | What We Already Have | What Remains Unknown | Document/Package to Send | Contact Now or Wait? | Preferred Candidate Already Researched? |
|---|---|---|---|---|---|---|---|
| WDP (pathology partner) | Confirmation on the centrifuge sourcing/brand-acceptance, the medical waste disposal contract overlap, and the glucose solution supply | 3 genuine WDP-dependent procurement items (E14, E15, E21) cannot be actioned without this | Existing correspondence with Carole Rivers, medical waste question already asked 2026-08-21 (awaiting reply); centrifuge and glucose solution not yet specifically asked in any sent correspondence | Whether WDP's own collection-centre arrangement covers medical waste; whether the centrifuge must be a WDP-nominated brand; whether WDP supplies the glucose solution | No new document; these are follow-up questions to the existing correspondence thread, not a fresh package | Wait for a reply to the 2026-08-21 send before raising more questions, per the founder's own instruction not to draft another follow-up without genuine reason | Yes, Carole Rivers, already an active, responsive contact |
| HVAC/LEV contractor | A WorkSafe-WA-familiar contractor for the Nail Station LEV unit and general venue HVAC | Genuinely no contractor identified yet, a disclosed gap | LEV method/spec already researched (downdraft capture-hood systems) | Which specific contractor, their availability, their quote | None yet; this is a genuine business-development identification task | Can start identifying candidates now, does not need to wait for a venue, but the actual scoped quote waits for the site | No |
| External Cafe food supplier | A pre-made sandwich/roll supplier meeting WA food-safety requirements | Cafe cannot open without this | The confirmed Cafe model (external, pre-made, may be warmed/toasted) | Which supplier, their pricing, their delivery terms | None yet; business-development identification task | Can start identifying candidates now | No |
| Coffee/beverage wholesale supplier | A coffee bean/milk/syrup and cold-drink wholesaler | Cafe cannot open without this | The confirmed Cafe revenue-assumption basis | Which supplier, pricing, delivery terms | None yet | Can start identifying candidates now | No |
| Builder (fit-out) | 3 independent construction/fit-out quotes | Required before any construction proceeds | General construction requirement categories (Part of `PROCUREMENT-CONSTRUCTION-FITOUT.md`) | Everything site-specific | The whole-of-venue brief once a venue is secured | Must wait for a confirmed, measured venue | No |
| Australian salon/spa suppliers | Bulk quotes for Queue 2 Group C items | To fill the RFQ-Now queue | Named suppliers already identified (National Salon Supplies, Salon Supply Australia, Diamond Nail Supplies, American Beauty Supply, The Salon Furniture Hub) | Actual quotes, none obtained | `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 2 | Can contact now | Yes, all 5 named, none contacted |
| China sourcing agent | A scoping conversation and RFQ response for Queue 2 Group A items | To execute the China sourcing route | `docs/architecture/PROCUREMENT-SOURCING-AGENT-BRIEF.md` and `CHINA-SOURCING-AGENT-ENQUIRY-PACKAGE.md` (this task) fully prepared | Whether Epic Sourcing Australia or another agent is genuinely capable, not independently verified | `docs/architecture/CHINA-SOURCING-AGENT-ENQUIRY-PACKAGE.md` | Can contact now for an exploratory, no-commitment scoping conversation | Yes, Epic Sourcing Australia is the closest candidate found, not independently verified beyond their own public materials |
| Freight forwarder | A real freight quote for whole-order container-scale shipping | The existing per-parcel placeholder figure is inadequate at this scale | 2 candidates already identified (DB Schenker Perth, Toll Global Forwarding) | Actual quote, none obtained | Not yet prepared; should follow once a locked China order list exists | Should wait until the China RFQ responses exist, so the freight quote is against a real shipment, not a guess | Yes, 2 named candidates |
| Australian licensed professionals (electrician, plumber, access consultant, building surveyor) | Site-specific scope quotes | Required post-venue per Queue 3 | Named engagement type understood | Which specific tradesperson, their availability | The whole-of-venue brief once a venue is secured | Must wait for a confirmed, measured venue | No |

**No supplier, sourcing agent, WDP contact, or professional has been contacted as part of building this document.** This is a preparation and sequencing document only.

## Sourcing

`docs/architecture/PROCUREMENT-EXECUTION-MATRIX.md`, `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`, `docs/architecture/PROCUREMENT-FOUNDER-DECISIONS.md`, `docs/architecture/PROCUREMENT-CLINICAL-GTT-WDP-SPLIT.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/reed-partnerships.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the 5 practical execution queues (Buy Now, RFQ Now, Venue Hold, Founder Decisions, External Dependencies), applying a real practicality check to Queue 1 beyond the Readiness A label (storage location, subscription-billing timing) rather than treating "Order Ready" as automatically "buy today." Queue 4 re-verified the Massage/Beauty decision status against the current authoritative venue-program documents rather than assuming it, confirming both remain correctly classified as-is.
