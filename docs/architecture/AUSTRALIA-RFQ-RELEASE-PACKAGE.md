# Australia RFQ Release Package

Status: current as of 2026-08-23. Identifies which Australian RFQs are genuinely ready to issue today (not gated by a venue, a founder decision, or a professional-verification step), grouped so comparable quotes come back from named suppliers, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` and `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 2. **Not sent to anyone. No quote requested yet.**

## RFQ Group 1: Bulk Salon/Spa Furniture and Equipment

**Exact scope:** professional hair dryers (J03), straightening irons (J04), UV/LED nail lamps (H04, if Australian-sourced rather than China), client manicure chairs (H03).

**Exact quantities:** 4 hair dryers, 4 straightening irons, 4 nail lamps, 4 manicure chairs.

**Minimum specification:** named-brand hair dryer/straightener (Dyson, GHD, or Cloud Nine, or an equivalent professional-salon brand with an Australian direct-trade account), professional-grade UV/LED lamp, standard commercial manicure chair.

**Preferred specification:** matches the locked 7-colour palette for the manicure chair upholstery; direct-trade-account pricing tier for the named-brand tools where available.

**Compliance requirements:** SAA electrical safety mark on all electrical items.

**Delivery:** standard Australian courier/freight to the confirmed venue address once known; interim delivery to a nominated holding address if ordered before the venue is secured (see `PROCUREMENT-EXECUTION-QUEUES.md` Queue 1, Tier 1c reasoning on storage risk for bulkier items in this group).

**Installation:** none required, freestanding/portable.

**Warranty:** state the manufacturer's standard warranty term for each item; confirm local repair/service availability for the named-brand tools specifically.

**Lead time:** to be stated by the supplier.

**Quote validity:** request a minimum 30-day validity given the venue timeline is not yet fixed.

**Exclusions:** installation, delivery beyond standard courier, any bespoke colour/finish beyond the supplier's standard range.

**GST treatment:** standard-rated (10%), input tax credit claimable against the trust's GST-registered ABN.

**Freight:** request freight cost itemised separately from unit price.

**Disposal of packaging:** not required from the supplier; standard commercial packaging, disposed of by GTT Center Perth on receipt.

**After-sales support:** confirm whether the named suppliers (National Salon Supplies, Salon Supply Australia, Diamond Nail Supplies, American Beauty Supply, The Salon Furniture Hub) offer a service/repair channel for electrical tools specifically.

## RFQ Group 2: Beauty Treatment Furniture

**Exact scope:** Beauty treatment bed (G01).

**Exact quantities:** 2 day-one, up to 3 with the growth reservation (order 2 now, confirm the 3rd once growth is triggered).

**Minimum specification:** electric, adjustable, vinyl surface.

**Preferred specification:** matches the locked 7-colour palette.

**Compliance requirements:** SAA electrical mark for the recline mechanism.

**Delivery:** to the confirmed venue address; hold for delivery until the Beauty room is fit-out-ready (see Queue 1, Tier 1c).

**Installation:** none required, freestanding.

**Warranty:** confirm the electric recline mechanism's warranty term specifically, since this is the most failure-prone component.

**Lead time:** to be stated by the supplier.

**Quote validity:** minimum 30 days.

**Exclusions:** installation, GPO connection (a licensed-electrician task, not part of this RFQ).

**GST treatment:** standard-rated.

**Freight:** itemised separately.

**Disposal of packaging:** not required from the supplier.

**After-sales support:** confirm replacement-parts availability for the recline mechanism before order.

## RFQ Group 3: Clinical Furniture and Equipment (Direct Purchase, Not Via Any Furniture OEM)

**Exact scope:** phlebotomy chairs (E01, E02), vasovagal recliner/exam couch (E04).

**Exact quantities:** 2 phlebotomy chairs day-one (E01, E02), 1 recliner/couch (E04). The 3rd phlebotomy chair (E03) is a growth-triggered purchase, not included in this release.

**Minimum specification:** reclines to flat, adjustable arm support, vinyl wipe-clean surface, wide/bariatric seat (phlebotomy chairs); full recline to flat (recliner/couch).

**Preferred specification:** named Perth medical-furniture brands (Sunflower Medical, Alphatec Australia, Ultramedic) for the phlebotomy chairs specifically.

**Compliance requirements:** none beyond general consumer/clinical product safety; not TGA-regulated furniture.

**Delivery:** to the confirmed venue address; hold for delivery until the Blood Collection Room is fit-out-ready.

**Installation:** none required, freestanding.

**Warranty:** confirm standard warranty term.

**Lead time:** to be stated by the supplier.

**Quote validity:** minimum 30 days.

**Exclusions:** installation.

**GST treatment:** standard-rated.

**Freight:** itemised separately.

**Disposal of packaging:** not required from the supplier.

**After-sales support:** confirm repair/replacement-parts channel for the recline mechanism.

## What Is Deliberately Not Included in This Release

Builder/fit-out RFQs (require a confirmed, measured venue, per `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md` Category 3), specialist contractor engagement (electrician, plumber, HVAC/LEV, require a confirmed venue, Category 4), the Massage table (F01a, gated on the table-vs-chair founder decision), any item classified Readiness C/D/E/F/G in the master register. These are tracked in `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 3 and Queue 4, not in this release.

## Sourcing

`docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md`, `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md`, `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the genuinely-ready-now Australian RFQ release package, grouped into 3 comparable-quote groups (bulk salon/spa, Beauty furniture, clinical furniture), each with the full field set a supplier needs to quote against. Not sent to anyone.
