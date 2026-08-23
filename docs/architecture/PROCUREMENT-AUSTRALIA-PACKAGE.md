# Australia Procurement Package

Status: current as of 2026-08-23. Built from the AU-only, PRO (professional procurement), and WDP-classified items in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (110 AU, 7 PRO, 3 WDP). Organised into the 8 supplier-type categories a genuine purchasing package needs, each stating exactly what that supplier needs to quote. **No supplier has been contacted. No order or RFQ has been sent.**

## 1. Retail Purchase

**Items:** general office stationery (B15), staff-area kettle/microwave/fridge (L03/L06/L07), general cleaning consumables (O05-O17), general first aid kit (R02), basic tool kit (AB01).

**Procurement route:** normal purchasing, no formal RFQ, standard retail/business-account channels.

**What the supplier needs to quote:** unit price per catalogue item, standard delivery timeframe. No specification negotiation required, these are off-the-shelf items.

## 2. Trade/RFQ (Bulk Commercial Salon/Spa Suppliers)

**Items:** professional hair dryers/straighteners (named brand, direct trade account), UV/LED nail lamps, client chairs where not sourced via the China package.

**Named suppliers already identified, none contacted:** National Salon Supplies, Salon Supply Australia, Diamond Nail Supplies, American Beauty Supply, The Salon Furniture Hub (all national, Australia-wide delivery, per `docs/architecture/ITEMISED-PURCHASE-LIST.md`).

**Procurement route:** AU RFQ REQUIRED for bulk quantities.

**What the supplier needs to quote:** unit price at the confirmed quantity per item, trade-account pricing tier if applicable, lead time, delivery cost to the confirmed venue, warranty term, and whether a direct-trade-account relationship (required for named-brand hair dryers/straighteners specifically, for warranty reasons) is available.

## 3. Builder/Fit-Out Quote

**Items:** general construction/fit-out (walls, flooring, ceilings, electrical/plumbing rough-in, HVAC), custom Reception/Cafe joinery and cabinetry.

**Procurement route:** SITE QUOTE REQUIRED. Cannot be sought before a venue is confirmed and measured. 3 real, independent builder quotes required per `docs/architecture/DOSSIER-CURRENT-STATE-RECONCILIATION-MATRIX.md` and Dossier Chapter 24/25's own standing requirement; a licensed joiner separately for custom Reception/Cafe cabinetry.

**What the supplier needs to quote:** a full fit-out quote against the confirmed floor plan (not before), broken down by trade (electrical, plumbing, HVAC, joinery, flooring, painting) so the quotes are comparable, itemised separately from any furniture/equipment cost, with a stated completion timeframe.

## 4. Specialist Contractor

**Items:** licensed electrician (all GPO, lighting circuit, and LEV-unit power installation, Sections A05, G14, H21, J18, X01-X16), licensed plumber (Cafe's chilled/boiling water tap, Blood Collection Room's clinical hand-hygiene sink, Hair Wash basins, Pedicure chair plumbing, Sections C04, E24, I02, K02, K04), HVAC/LEV contractor (Nail Station's LEV unit H06, general HVAC servicing A04, Blood Collection Room ventilation E38).

**Procurement route:** licensed trade engagement, post-venue, not a product purchase in the conventional sense. **Genuine gap: no HVAC/LEV contractor has been identified yet**, distinct from electrical/plumbing where the engagement type is understood even though a specific tradesperson has not been selected either.

**What the contractor needs to quote:** a scope-of-works quote against the confirmed floor plan and the specific compliance standard applicable (WorkSafe WA for the LEV unit, NSQHS Standards for the clinical hand-hygiene sink, AS/NZS wiring rules for electrical), stated as a fixed quote or hourly rate plus materials, with a compliance sign-off included in the deliverable, not billed as a separate step.

## 5. Clinical Supplier

**Items:** phlebotomy chairs (Sunflower Medical, Alphatec Australia, Ultramedic, named Perth medical-furniture brands), sharps containers and biohazard waste equipment (Daniels Health, Cleanaway Medical, Stericycle), AED (via St John Ambulance WA or a registered medical supplier, a leasing option exists), pathology consumables (largely via the WDP relationship, E20, WDP DEPENDENT, not independently sourced), clinical-grade (TGA-listed) cleaning/disinfectant products (kept as an explicitly separate product line from general cleaning supplies, Section E4), general first-aid/CPR training via a registered training organisation (R06, a training booking, not a physical purchase).

**Procurement route:** AU RFQ REQUIRED, direct purchase, not via any interior/furniture OEM, for phlebotomy chairs/sharps containers/AED. WDP-dependent for pathology consumables. Standard training-provider booking for CPR/first aid.

**Certification requirement:** ARTG registration for the AED; AS/NZS 23907:2023 for sharps containers; TGA listing for clinical-grade disinfectant, confirmed before purchase, not assumed from a generic household product.

**What the supplier needs to quote:** unit price at the confirmed quantity, certification/registration documentation supplied with the quote (not after purchase), delivery timeframe, and for the AED specifically, both a purchase price and a lease price so the two can be compared.

## 6. Food/Beverage Supplier

**Items:** coffee/beverage wholesale supplier (not yet selected), the external pre-made food supplier (**not yet identified, a genuine dependency, not invented here**), commercial-grade Cafe equipment (standard commercial kitchen equipment retailers).

**Procurement route:** AU RFQ REQUIRED once suppliers are identified for equipment; the external food supplier itself is a business-development identification task, not a standard RFQ, since no supplier exists yet to request a quote from.

**What the supplier needs to quote (once identified):** for the food supplier, per-unit wholesale price for pre-made sandwiches/rolls, delivery frequency and minimum order, the supplier's own food-safety certification (a prerequisite for the WA Food Business Notification, not optional). For the coffee/beverage wholesaler, per-unit price for beans/milk/syrups/cold drinks, delivery frequency. For Cafe equipment, unit price, warranty term, and installation/connection requirements for the chilled/boiling water tap specifically (plumbing-dependent, see Category 4 above).

## 7. Waste Supplier

**Items:** general waste collection contract (council or private contractor, AA03), medical waste disposal contract (E14, WDP-dependent pending confirmation of whether WDP's own arrangement already covers it).

**Procurement route:** standard council/contractor engagement for general waste; hold on medical waste until the WDP dependency resolves, per `docs/architecture/PROCUREMENT-DEPENDENCY-MAP.md`.

**What the supplier needs to quote:** collection frequency and monthly contract cost for general waste; for medical waste (only once WDP's own position is known), collection frequency, monthly contract cost, and confirmation of compliant handling per council/WorkSafe WA requirements.

## 8. IT/Security Supplier

**Items:** computers/laptop, printer, WiFi router (JB Hi-Fi, Officeworks business accounts), iPads (Apple, direct or via retailer), POS terminals (Square/Tyro), optional security cameras and access control (Section T, Future/Optional).

**Procurement route:** standard retail/business-account purchasing, no formal RFQ required for this scale of order; the optional security items (T08/T09) are Future/Optional, not being actioned now.

**What the supplier needs to quote:** unit price per catalogue item, business-account discount tier if applicable, standard delivery timeframe, and for POS terminals specifically, the ongoing transaction-fee structure (not just the hardware price), since that recurring cost matters more than the one-off hardware purchase.

## Categories Needing a Formal RFQ Versus Normal Purchasing

**Formal RFQ required:** salon/spa bulk furniture and equipment (Category 2), clinical equipment and furniture (Category 5, excluding WDP-dependent items), builder/construction quotes (Category 3), specialist contractor engagement (Category 4), food supplier engagement once identified (Category 6).

**Normal purchasing (no formal RFQ needed at this scale):** general retail/office items (Category 1), standard IT hardware from retail business accounts (Category 8), general (non-clinical-grade) cleaning supplies (folded into Category 1).

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/ITEMISED-PURCHASE-LIST.md` (named supplier research), `docs/architecture/PROCUREMENT-DEPENDENCY-MAP.md`, `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the Australian-side companion to the China procurement package, separating retail, commercial-salon, clinical, trade, food-service, IT, cleaning, waste, and builder categories, and distinguishing which need a formal RFQ from which are normal purchasing.

**2026-08-23 (reorganised):** Per direct founder instruction (Part 7), reorganised into the 8 requested supplier-type categories (Retail Purchase, Trade/RFQ, Builder/Fit-Out Quote, Specialist Contractor, Clinical Supplier, Food/Beverage Supplier, Waste Supplier, IT/Security Supplier), with an explicit "what the supplier needs to quote" statement added to every category so this is a genuine RFQ/purchasing package rather than a descriptive list.
