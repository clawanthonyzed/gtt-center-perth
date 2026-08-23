# Opening Stock Schedule

Status: current as of 2026-08-23. This document builds a genuine opening-stock methodology for the consumable groups in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, rather than leaving an arbitrary quantity beside each consumable. It does not invent a real-world consumption rate this venture has never measured (it hasn't opened yet); it discloses a reasoned, standard inventory-planning methodology as a planning assumption, explicitly labelled as an assumption requiring calibration once real trading data exists, not a measured fact.

## Methodology (applied consistently below)

**Opening stock period:** sized to cover the first 4 weeks of trading at the committed 18-client/day AM volume plus the current PM model (Chapter 9), a standard initial-stock planning window, not a measured consumption rate.

**Reorder point:** set at 25% of the opening-stock quantity remaining, a standard min/max inventory convention, not a venture-specific measurement.

**Reorder quantity:** restores stock to the original opening-stock level.

**Basis label used throughout:** every row states the actual planning assumption behind its figure (client-volume-linked, area-count-linked, or a flat administrative estimate), and is explicitly flagged for recalibration against real usage once the venture has traded for a representative period (recommended: after the first 4-8 weeks of actual trading).

---

## General Facility Consumables

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| Toilet paper | Quantity to be determined once toilet count is confirmed (site-dependent, Section N of the master register) | 25% remaining | Restock to opening level | Toilet-count-linked; cannot be finalised before a venue is confirmed |
| Paper towel (hand-drying) | Same as toilet paper | 25% remaining | Restock to opening level | Toilet-count-linked |
| Hand soap | Same as toilet paper | 25% remaining | Restock to opening level | Toilet-count-linked |
| Hand sanitiser (public-facing) | 3-4 dispensers filled, plus 2 refill bottles per dispenser | 1 refill bottle remaining per dispenser | Restock to 2 refills per dispenser | Fixed dispenser count (Section S02), refill rate is a planning assumption pending real usage data |
| Bin liners (general) | 1 box per bin location (approximately 10-15 bin locations across the venue, per the areas itemised in Sections C/D/J/N) | 20% of box remaining | 1 new box per location | Area-count-linked; exact bin count is site-dependent |
| Cleaning chemicals (general disinfectant, bathroom cleaner, glass cleaner, floor cleaner) | 1 bottle of each per cleaning trolley/caddy (2-3 caddies, Section O13) | 25% remaining | Restock to 1 bottle per caddy | Caddy-count-linked, a planning assumption, not measured |
| Laundry detergent/stain remover | Only applicable if the in-house laundry model is adopted (Founder Decision, `PROCUREMENT-FOUNDER-DECISIONS.md`); not sized until that decision is made | N/A | N/A | Blocked by the laundry-model founder decision |
| Tissues (general-area) | 1 box per public-facing area (Reception, Lounge, Cafe) | 20% of box remaining | 1 new box per area | Area-count-linked |

## Clinical Consumables (Blood Collection, cross-referenced to Section E of the master register)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| Disposable gloves (nitrile, clinical) | 4 weeks at 2 pairs/client (one per phlebotomist per draw event, 3 draws/client) x 18 clients/day x 22 trading days | 25% remaining | Restock to opening level | Client-volume-linked (18/day committed AM model); the 2-pairs/client planning assumption is a reasoned estimate, not measured, flagged for recalibration after opening |
| Face masks (surgical) | 4 weeks at 1/phlebotomist/shift x 2 phlebotomists x 22 trading days | 25% remaining | Restock to opening level | Staff-shift-linked |
| Sharps containers, biohazard bags | Per Section E09/E10/E13's already-itemised opening quantities | Container/bag nearing capacity (a clinical-practice trigger, not a stock-level trigger) | Replace per clinical protocol, not a stock-level reorder | Clinical-practice-linked, not consumption-volume-linked |
| TGA-listed surface disinfectant | 4 weeks at 1 bottle/week per Blood Collection Room | 25% remaining | Restock to opening level | Room-count-linked (1 room) |
| Alcohol swabs, gauze, tape (pathology consumables) | WDP-dependent, see Section E20; not sized independently of the WDP supply arrangement | N/A | N/A | WDP DEPENDENT, per the master register |

## Nail Consumables (cross-referenced to Section H)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| Gel polish (20+ colours) | Already itemised: A$300-500 opening lot, 20 colours | 25% of any single colour remaining | Restock that colour | Existing repository research figure, not re-estimated |
| Regular (non-gel) polish | Already itemised, 20 colours | 25% remaining | Restock that colour | Existing repository research figure |
| Base coat, top coat | 4 weeks at 1 application/client x 18 AM clients/day (where nail services are selected) x 22 days, a planning estimate since real service-selection mix is not yet known | 25% remaining | Restock to opening level | Client-volume-linked, disclosed estimate |
| Files, buffers, cuticle tools | 1 set per station (4 stations) plus a 50% spare buffer | Visible wear, a quality-practice trigger, not purely a stock-level trigger | Replace worn items | Station-count-linked |
| Remover/acetone | 4 weeks at estimated 1L per 40 services | 25% remaining | Restock to opening level | Disclosed estimate, not measured |
| Nail dust masks (N95) | Already itemised: 2 boxes of 50 | 25% of a box remaining | 1 new box | Existing repository research figure |
| Disinfection solution | Already itemised: A$80-150 opening lot | 25% remaining | Restock to opening level | Existing repository research figure |

## Hair Consumables (cross-referenced to Section J)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| Shampoo, conditioner (pregnancy-safe) | 4 weeks at estimated 1 wash/client where hair services are selected, a disclosed estimate | 25% remaining | Restock to opening level | Client-volume-linked, disclosed estimate |
| Treatment/styling products | Already itemised: A$350-650 combined opening lot (equipment-costs.md §5) | 25% remaining | Restock to opening level | Existing repository research figure |
| Towels (hair-specific) | 12-20 units, sized for same-day laundry turnover across 4 chairs + 2 wash stations | Laundry-cycle-linked, not a stock-depletion trigger | N/A, replenished via laundry cycle | Station-count-linked, laundry-model-dependent (see the laundry founder decision) |
| Colour equipment/consumables | Blocked pending the colour-services founder decision, `PROCUREMENT-FOUNDER-DECISIONS.md` | N/A | N/A | FOUNDER DECISION REQUIRED |

## Beauty Consumables (cross-referenced to Section G)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| PPD-free brow tint | Already itemised: A$150-250 opening lot | 25% remaining | Restock to opening level | Existing repository research figure |
| Wax (strip + hard, pregnancy-safe) | Already itemised: A$100-200 opening lot | 25% remaining | Restock to opening level | Existing repository research figure |
| Facial products | Already itemised: A$300-600 opening lot | 25% remaining | Restock to opening level | Existing repository research figure |
| Disposable brow/wax consumables | Already itemised: A$100-200 opening lot | 25% remaining | Restock to opening level | Existing repository research figure |

## Massage Consumables (cross-referenced to Section F)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| Pregnancy-safe massage oil | Already itemised: 5L bulk, A$25-50/L | 25% remaining | Restock to opening level | Existing repository research figure |
| Massage table linen (sheets, pillowcases) | 2 sets per station (3 stations) | Laundry-cycle-linked | N/A, replenished via laundry cycle | Station-count-linked, laundry-model-dependent |
| Disposable table-roll paper/barrier | 4 weeks at 1 roll per 10 services, a disclosed estimate | 25% remaining | Restock to opening level | Disclosed estimate |

## Cafe Consumables (cross-referenced to Section C)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| Coffee beans/milk/syrups | 2 weeks initial supply, calibrated against the current planning assumption of 50% of AM clients spending A$10 at the Cafe (approximately 9 transactions/day at 18 clients/day) | 25% remaining | Restock to opening level | Cafe-revenue-assumption-linked (Chapter 28's own 50%-of-AM-clients spend assumption) |
| Herbal tea (free to all clients) | 4 weeks at 1 serving per AM client (18/day x 22 days), since it is offered free to every client regardless of purchase | 25% remaining | Restock to opening level | Client-volume-linked, not a purchase-conversion assumption |
| Bottled/canned cold drinks | 2 weeks initial supply, same Cafe-revenue-assumption basis as coffee | 25% remaining | Restock to opening level | Cafe-revenue-assumption-linked |
| Pre-made sandwiches/rolls | Blocked pending the external food supplier being identified, a genuine procurement dependency, not a stock-planning gap | N/A | N/A | INFORMATION REQUIRED: supplier not yet identified |
| Cups, takeaway cups/lids | 2 weeks initial supply, same Cafe-revenue-assumption basis | 25% remaining | Restock to opening level | Cafe-revenue-assumption-linked |
| Napkins, cutlery | 2 weeks initial supply, same basis | 25% remaining | Restock to opening level | Cafe-revenue-assumption-linked |

## Office/Admin Consumables

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| POS receipt paper rolls | 10 rolls (a standard small-business starting quantity, not venture-specific) | 3 rolls remaining | 10 rolls | Flat administrative estimate, not client-volume-linked |
| Printer supplies (toner/ink) | 1 spare cartridge/toner per printer | Cartridge empty | 1 replacement | Equipment-count-linked |
| General stationery | 1 lot, per Section B15 | Visible depletion | Restock as needed | Flat administrative estimate |

## First Aid / Emergency Supplies (cross-referenced to Section R)

| Item | Opening Stock | Reorder Point | Reorder Qty | Basis |
|---|---|---|---|---|
| First aid kit contents | Fully stocked kit per WorkSafe-compliant specification (Section R02) | Any item used/expired | Replace that item | Compliance-standard-linked, not consumption-volume-linked |
| EpiPen | 1-2, in date | Approaching expiry | Replace before expiry | Expiry-driven, not consumption-linked |
| AED pads/battery | 1 spare set | Approaching expiry | Replace before expiry | Expiry-driven |

## What this schedule does not do

It does not invent a measured consumption rate for a venture that has not opened yet. Every client-volume-linked figure above is explicitly disclosed as a planning estimate using the venture's own committed volume assumptions (18 AM clients/day, the Cafe's 50%-of-AM-clients-spend-A$10 assumption), not a guessed number. The 25%-remaining reorder-point convention is a standard inventory-planning practice, not a venture-specific finding. All figures should be recalibrated against real usage after the first 4-8 weeks of actual trading.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/equipment-costs.md` (existing opening-stock lot figures), Dossier Chapter 9 (client volume model), Dossier Chapter 28 (Cafe revenue assumption).

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as a genuine opening-stock methodology, using a standard 25%-remaining reorder-point convention and the venture's own committed client-volume assumptions as the disclosed basis for each figure, rather than an arbitrary quantity beside each consumable.
