# Australia Procurement Package

Status: current as of 2026-08-23. Built from the AU-only, PRO (professional procurement), and WDP-classified items in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (110 AU, 7 PRO, 3 WDP). **No supplier has been contacted. No order or RFQ has been sent.**

## Australian Retail Purchases

Items purchasable directly from standard retail/business-account channels, no formal RFQ required: general office stationery (B15), staff-area kettle/microwave/fridge (L03/L06/L07), general cleaning consumables (O05-O17), general first aid kit (R02), basic tool kit (AB01). **Procurement route:** normal purchasing, no RFQ.

## Australian Commercial Suppliers (Salon/Spa)

National Salon Supplies, Salon Supply Australia, Diamond Nail Supplies, American Beauty Supply, The Salon Furniture Hub, all national suppliers with Australia-wide delivery, already identified in `docs/architecture/ITEMISED-PURCHASE-LIST.md`, none yet contacted. **Covers:** professional hair dryers/straighteners (named brand, direct trade account), UV/LED nail lamps, client chairs (where not sourced via the China package). **Procurement route:** AU RFQ REQUIRED for bulk quantities.

## Specialist Clinical Suppliers

Phlebotomy chairs (Sunflower Medical, Alphatec Australia, Ultramedic, named Perth medical-furniture brands), sharps containers and biohazard waste equipment (Daniels Health, Cleanaway Medical, Stericycle), AED (via St John Ambulance WA or a registered medical supplier, leasing option exists). **Procurement route:** AU RFQ REQUIRED, direct purchase, not via any interior/furniture OEM. **Certification requirement:** ARTG registration for the AED; AS/NZS 23907:2023 for sharps containers.

## Electrical Suppliers

Licensed electrician required for all GPO, lighting circuit, and LEV-unit power installation (Sections A05, G14, H21, J18, X01-X16). **Procurement route:** licensed trade engagement, post-venue, not a product purchase in the conventional sense.

## Plumbing Suppliers

Licensed plumber required for the Cafe's chilled/boiling water tap, the Blood Collection Room's clinical hand-hygiene sink, Hair Wash basins, and Pedicure chair plumbing (Sections C04, E24, I02, K02, K04). **Procurement route:** licensed trade engagement, post-venue.

## HVAC/LEV Suppliers

A WorkSafe-WA-familiar HVAC/extraction contractor for the Nail Station's LEV unit (H06), general HVAC servicing (A04), Blood Collection Room ventilation (E38). **Genuine gap: no named contractor identified yet**, distinct from the electrical/plumbing categories where named suppliers already exist. **Procurement route:** identify a contractor first (a real, disclosed action item), then AU RFQ REQUIRED.

## Food-Service Suppliers

Coffee/beverage wholesale supplier (not yet selected), the external pre-made food supplier (**not yet identified, a genuine dependency**), commercial-grade Cafe equipment suppliers (standard commercial kitchen equipment retailers). **Procurement route:** AU RFQ REQUIRED once suppliers are identified; the food supplier itself is a business-development task, not a standard RFQ.

## Medical Suppliers

Pathology consumables largely via the WDP relationship (E20, WDP DEPENDENT), general first-aid/CPR training via a registered training organisation (R06, not a physical purchase). **Procurement route:** WDP-dependent for pathology items; standard training-provider booking for CPR/first aid.

## Office/IT Suppliers

JB Hi-Fi, Officeworks (business accounts) for computers, printers, WiFi router; Apple (direct or via retailer) for iPads; Square/Tyro for POS terminals. **Procurement route:** standard retail/business-account purchasing, no formal RFQ required for this scale of order.

## Cleaning Suppliers

Standard commercial cleaning-supply wholesalers for general and clinical-grade (TGA-listed) products, kept as two explicitly separate product lines (Sections E4 and O). **Procurement route:** normal purchasing for general supplies; confirm TGA listing specifically for clinical-grade disinfectant before purchase.

## Waste Suppliers

General waste collection contract (council or private contractor, AA03), medical waste disposal contract (E14, WDP-dependent pending confirmation of whether WDP's own arrangement already covers it). **Procurement route:** standard council/contractor engagement for general waste; hold on medical waste until the WDP dependency resolves.

## Builders/Trades

3 real builder quotes required for construction/fit-out (gated on a confirmed venue, per Dossier Chapter 24/25), a licensed joiner for custom Reception/Cafe cabinetry. **Procurement route:** SITE QUOTE REQUIRED, cannot be sought before a venue is confirmed.

## Categories needing a formal RFQ versus normal purchasing

**Formal RFQ required:** salon/spa bulk furniture and equipment (all 4 rooms), clinical equipment and furniture, builder/construction quotes, HVAC/LEV contractor engagement, food supplier engagement. **Normal purchasing (no formal RFQ needed at this scale):** general retail/office items, standard cleaning supplies, standard IT hardware from retail business accounts.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/ITEMISED-PURCHASE-LIST.md` (named supplier research).

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the Australian-side companion to the China procurement package, separating retail, commercial-salon, clinical, trade (electrical/plumbing/HVAC), food-service, medical, IT, cleaning, waste, and builder categories, and distinguishing which need a formal RFQ from which are normal purchasing.
