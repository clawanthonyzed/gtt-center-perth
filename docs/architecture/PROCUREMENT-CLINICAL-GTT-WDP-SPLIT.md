# Clinical Procurement: GTT Center vs WDP Split

Status: current as of 2026-08-23. A detailed, unambiguous split of every Blood Collection item (Section E of `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, 40 items) into exactly one of 5 responsibility categories, so a clinical procurement person can understand the split without inferring it from prose. **Nothing here assumes WDP supplies an item, or assumes GTT Center purchases an item, beyond what the repository already establishes.** Where the repository itself discloses genuine uncertainty (e.g. the glucose solution, the medical waste contract), that uncertainty is stated as uncertainty, not resolved by assumption.

## Category A: GTT Center Perth Purchases Directly

These items are purchased by GTT Center Perth, not supplied by WDP, and are not clinical-professional-verification-gated beyond standard product compliance.

| Item ID | Item | Notes |
|---|---|---|
| E01 | Phlebotomy chair (Chair A) | Named Perth medical-furniture brands (Sunflower Medical, Alphatec Australia, Ultramedic) |
| E02 | Phlebotomy chair (Chair B) | Same as E01 |
| E03 | 3rd phlebotomy chair (growth reservation) | Room built/serviced for 3 chairs from day one; the 3rd chair itself is a staffing/demand-triggered purchase, not day-one |
| E04 | Vasovagal recliner/exam couch | Non-TGA furniture item |
| E05 | Documentation desk/bench | Standard furniture |
| E06 | Phlebotomist stool (adjustable height) | Standard furniture |
| E07 | Medical consumables cabinet (lockable) | Standard storage |
| E08 | Patient documentation drawer (lockable) | Privacy Act record storage |
| E09 | Sharps container, bench size (1.4L) | AS/NZS 23907:2023 compliant, named brands (Daniels Health, Cleanaway Medical, Stericycle) |
| E10 | Sharps container, room size (5L) | Same standard as E09 |
| E11 | Wall-mounted sharps container bracket | N/A |
| E12 | Biohazard waste bin (yellow, lidded) | AS/NZS clinical waste standard |
| E13 | Biohazard specimen pouches | Box of 100 |
| E16 | Specimen refrigerator | 2-8C, temperature-logged |
| E17 | Insulated specimen transport bag | For courier/drop-off dispatch |
| E18 | Ice packs (reusable, cold chain) | N/A |
| E19 | Thermal label printer | Zebra ZD420 or equivalent |
| E22 | Disposable gloves (nitrile) | Powder-free |
| E23 | Face masks (surgical) | AS 4381 |
| E25 | Alcohol-based hand rub (ABHR) dispenser | Wall-mounted |
| E26 | Hand soap (clinical grade) | Dispenser refill |
| E27 | Paper towel (clinical) | Dispenser refill |
| E28 | Surface disinfectant (hospital-grade) | Must be TGA-listed, not a generic household disinfectant |
| E29 | Blood spill kit | Infection control standard |
| E30 | Disposable wipes (surface, clinical-grade) | Infection control standard |
| E33 | Biohazard symbol (room door) | AS/NZS signage standard |
| E34 | Hand hygiene reminder signage | At sink |
| E35 | "No entry when in use" signage | Door-mounted |
| E39 | Phlebotomist uniform/scrubs | Per staff position register (PHL01-PHL04) |
| E40 | Collection log, specimen dispatch log, adverse event register | 7-year retention requirement, patient record-keeping |

## Category B: WDP Directly Supplies

These items are established in the repository as largely or entirely supplied under WDP's own NATA Licensed Collection Centre accreditation, not general retail.

| Item ID | Item | Notes |
|---|---|---|
| E20 | Pathology collection equipment (vacutainers, needles, tourniquets, alcohol swabs, gauze, tape) | GTT-specific fluoride-oxalate tubes; largely supplied under WDP's own accreditation umbrella, not general retail. **The register's own note is explicit: do not invent pathology equipment WDP would supply beyond what current documentation establishes; the final split is confirmed once WDP's commercial arrangement is settled, not assumed now.** |

## Category C: WDP-Dependent, Confirmation Required Before Any Action

These items require WDP's own confirmation on their commercial/supply arrangement before GTT Center Perth can determine who purchases them. This is genuinely unresolved, not resolved by assumption in either direction.

| Item ID | Item | What Specifically Needs WDP Confirmation |
|---|---|---|
| E14 | Medical waste disposal contract | Whether WDP's own collection-centre arrangement already covers medical waste disposal, or whether GTT Center Perth needs its own separate contract. Genuinely open, not assumed either way. **Correspondence status: already asked, in Anthony's 2026-08-21 follow-up to Carole Rivers (`docs/wdp-followup-draft-2026-08-20.md`, sent directly, outside this repository's workflow). No reply received yet.** |
| E15 | Tabletop centrifuge (refrigerated) | Whether it is sourced via the WDP relationship (the register's own Notes state this is "likely") and whether NATA acceptance confirmation is required before purchasing any non-established-brand alternative. This is the single most critical piece of equipment in the venue; do not compromise by purchasing independently before this is confirmed. **Correspondence status: not yet specifically asked in any sent correspondence with WDP.** |
| E21 | 75g glucose solution (Polycal or equivalent) | Whether WDP supplies this as part of their pathology relationship, or whether GTT Center Perth sources it independently. The register itself flags this as "possibly WDP-supplied, confirm", a genuinely open, disclosed uncertainty, not resolved here. **Correspondence status: not yet specifically asked in any sent correspondence with WDP.** |

**Do not draft another WDP follow-up for E15/E21 without a genuine reason; per standing instruction, wait for a reply to the 2026-08-21 send before raising further questions.** Full correspondence history: `docs/reed-partnerships.md`, `docs/VERIFICATION-TRACKER.md`.

## Category D: Professional Verification Required (Australian Licensed Professional, Not WDP)

These items or requirements need sign-off from a licensed Australian professional (not WDP) before they can be finalised.

| Item ID | Item | Who Confirms |
|---|---|---|
| E24 | Clinical sink + elbow/sensor tap fitout | NSQHS Standards, licensed hydraulic trade, install once venue confirmed |
| E31 | Solid walls, one door, no public-facing window (room construction) | Building surveyor, WA construction standard |
| E36 | Emergency call button/intercom to reception | Electrical, WorkSafe, local trade install |
| E38 | Room ventilation (6 ACH) | Australian HVAC contractor verification, site-specific |

## Category E: Site/Building Requirement (Neither GTT Center Purchase Nor WDP Responsibility)

| Item ID | Item | Notes |
|---|---|---|
| E32 | Per-chair curtain/partition between the up-to-3 chair positions | Washable curtain fabric, matches the recommended growth-first 3-chair-ready design; fit-out cost, purchased by GTT Center Perth once the room is built, listed here separately from Category A only because it is tied to the room's own construction timeline, not because responsibility is unclear |
| E37 | AED (venue-wide, not room-specific) | Cross-reference only, see Section R (First Aid), not double-counted in Blood Collection |

## What This Split Deliberately Does Not Do

It does not invent an internal "phlebotomy supervisor" clinical escalation role or equipment for one; escalation beyond the second on-site phlebotomist is a genuine, disclosed dependency on WDP's own Licensed Collection Centre protocol, not resolved by procurement. It does not assume the Category C items resolve in either direction (GTT-purchased or WDP-supplied) before WDP actually confirms; all 3 Category C items remain genuinely open.

## Summary Counts

30 items are GTT Center Perth's own direct purchase (Category A). 1 item is WDP-supplied (Category B). 3 items require WDP confirmation before action (Category C). 4 items require Australian professional verification (Category D). 2 items are site/construction-timeline items, not a responsibility ambiguity, one of which (E37) is itself a cross-reference to Section R, not an independently scored item (Category E). 30 + 1 + 3 + 4 + 2 = 40 total Item IDs (E01 through E40), of which 39 are independently scored and 1 (E37) is a cross-reference, matching Section E's own 39 scored items exactly.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` Section E, `docs/architecture/WDP-COMMERCIAL-ALIGNMENT-REVIEW.md`, `docs/reed-partnerships.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 10) as an unambiguous, item-by-item GTT-vs-WDP responsibility split for Blood Collection, replacing prose-only disclosure with an explicit 5-category table. No item's responsibility was assumed beyond what the repository already establishes; genuine open questions (E14, E15, E21) are stated as open, not resolved by assumption.
