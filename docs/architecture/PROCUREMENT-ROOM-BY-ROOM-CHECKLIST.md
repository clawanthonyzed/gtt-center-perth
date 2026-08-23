# Room-by-Room Procurement Checklist

Status: current as of 2026-08-23. Answers "what needs to exist here before we can open?" for 18 physical/functional areas, generated mechanically by `tools/generate_procurement_room_checklist.py` directly from `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`. This is a cross-reference view only: it lists Item IDs and names per area and bucket, tagged with the register's own Readiness classification. **It does not restate quantities.** `MASTER-PROCUREMENT-SHOPPING-LIST.md` remains the single quantity/source of truth; look up the Item ID there for the actual quantity, price, and full specification.

Each area is divided into: Furniture, Equipment, Fixtures, Electrical, Plumbing, Lighting, HVAC/Ventilation, Consumables, Technology, Signage, Safety, Cleaning, Opening Stock, Future/Optional. An item appears in exactly one bucket per area: Future/Optional items are pulled out first (Readiness H), then Opening Stock items (register's own Opening Stock? = Yes), then everything else is bucketed by its own sub-area/location field.

## 1. Blood Collection Area

**Furniture:**

- [ORDER-READY] E01: Phlebotomy chair (Chair A)
- [ORDER-READY] E02: Phlebotomy chair (Chair B)
- [RFQ-READY] E03: 3rd phlebotomy chair (growth reservation)
- [ORDER-READY] E04: Vasovagal recliner/exam couch
- [RFQ-READY] E05: Documentation desk/bench
- [RFQ-READY] E06: Phlebotomist stool (adjustable height)

**Equipment:**

- [WDP-DEPENDENT] E15: Tabletop centrifuge (refrigerated)
- [RFQ-READY] E16: Specimen refrigerator
- [ORDER-READY] E17: Insulated specimen transport bag
- [ORDER-READY] E19: Thermal label printer
- [INFORMATION REQUIRED] E39: Phlebotomist uniform/scrubs

**Fixtures:**

- [ORDER-READY] E07: Medical consumables cabinet (lockable)
- [ORDER-READY] E08: Patient documentation drawer (lockable)
- [RFQ-READY] E31: Solid walls, one door, no public-facing window
- [RFQ-READY] E32: Per-chair curtain/partition between the up-to-3 chair positions

**HVAC/Ventilation:**

- [PROFESSIONAL VERIFICATION] E38: Room ventilation

**Signage:**

- [RFQ-READY] E33: Biohazard symbol (room door)
- [RFQ-READY] E34: Hand hygiene reminder signage
- [RFQ-READY] E35: "No entry when in use" signage

**Safety:**

- [ORDER-READY] E11: Wall-mounted sharps container bracket
- [ORDER-READY] E12: Biohazard waste bin (yellow, lidded)
- [WDP-DEPENDENT] E14: Medical waste disposal contract
- [SITE-DEPENDENT] E24: Clinical sink + elbow/sensor tap fitout
- [RFQ-READY] E25: Alcohol-based hand rub (ABHR) dispenser
- [SITE-DEPENDENT] E36: Emergency call button/intercom to reception

**Opening Stock:**

- [ORDER-READY] E09: Sharps container, bench size (1.4L)
- [ORDER-READY] E10: Sharps container, room size (5L)
- [RFQ-READY] E13: Biohazard specimen pouches
- [ORDER-READY] E18: Ice packs (reusable, cold chain)
- [WDP-DEPENDENT] E20: Pathology collection equipment (vacutainers, needles, tourniquets, alcohol swabs, gauze, tape)
- [RFQ-READY] E21: 75g glucose solution (Polycal or equivalent)
- [RFQ-READY] E22: Disposable gloves (nitrile)
- [RFQ-READY] E23: Face masks (surgical)
- [RFQ-READY] E26: Hand soap (clinical grade)
- [RFQ-READY] E27: Paper towel (clinical)
- [RFQ-READY] E28: Surface disinfectant (hospital-grade)
- [ORDER-READY] E29: Blood spill kit
- [RFQ-READY] E30: Disposable wipes (surface, clinical-grade)
- [RFQ-READY] E40: Collection log, specimen dispatch log, adverse event register (printed forms)

---

## 2. Hair Wash Area

**Plumbing:**

- [PROFESSIONAL VERIFICATION] K02: Hot water supply, drainage per basin
- [PROFESSIONAL VERIFICATION] K04: Hot water system capacity

**Opening Stock:**

- [RFQ-READY] K03: Towels (hair-wash-specific)

**Future/Optional:**

- [FUTURE/OPTIONAL] K01: Backwash basin + client chair

---

## 3. Hair Styling Area

**Furniture:**

- [ORDER-READY] J01: Styling chair (hydraulic, wipe-clean)
- [SITE-DEPENDENT] J02: Salon mirror (lighted, full-length)

**Equipment:**

- [ORDER-READY] J03: Professional hair dryer
- [ORDER-READY] J04: Straightening iron
- [INFORMATION REQUIRED] J05: Curling tools
- [FOUNDER DECISION] J06: Hair clippers

**Fixtures:**

- [ORDER-READY] J15: Tool trolley + organiser

**Electrical:**

- [PROFESSIONAL VERIFICATION] J18: GPO nearby each chair

**Cleaning:**

- [RFQ-READY] J16: Hair waste bin

**Opening Stock:**

- [RFQ-READY] J07: Brushes/combs
- [RFQ-READY] J08: Capes
- [RFQ-READY] J09: Towels (hair-specific)
- [RFQ-READY] J10: Shampoo
- [RFQ-READY] J11: Conditioner
- [RFQ-READY] J12: Treatment products
- [RFQ-READY] J13: Styling products (mousse, spray, serum)
- [FOUNDER DECISION] J14: Colour bowls, brushes, foils, capes
- [RFQ-READY] J17: Disposable gloves

---

## 4. Nail Area

**Furniture:**

- [ORDER-READY] H01: Nail table with built-in dust collector
- [RFQ-READY] H02: Nail technician chair
- [ORDER-READY] H03: Client manicure chair

**Equipment:**

- [ORDER-READY] H04: UV/LED nail lamp
- [INFORMATION REQUIRED] H05: Nail drill

**Fixtures:**

- [ORDER-READY] H07: Nail tool trolley

**Electrical:**

- [PROFESSIONAL VERIFICATION] H21: GPO per station (2x 10A)

**HVAC/Ventilation:**

- [PROFESSIONAL VERIFICATION] H06: LEV (local exhaust ventilation) unit

**Opening Stock:**

- [RFQ-READY] H08: Nail files
- [RFQ-READY] H09: Buffing blocks
- [RFQ-READY] H10: Cuticle pushers
- [RFQ-READY] H11: Cuticle nippers
- [RFQ-READY] H12: Base coat
- [RFQ-READY] H13: Top coat
- [RFQ-READY] H14: Gel polish
- [RFQ-READY] H15: Regular (non-gel) polish
- [RFQ-READY] H16: Remover/acetone
- [RFQ-READY] H17: Lint-free wipes
- [RFQ-READY] H18: Disposable gloves
- [RFQ-READY] H19: Nail dust masks (N95)
- [RFQ-READY] H20: Disinfection solution + containers

---

## 5. Pedicure Area

**Furniture:**

- [ORDER-READY] I01: Pedicure spa chair (pipeless)

**Plumbing:**

- [PROFESSIONAL VERIFICATION] I02: Chair plumbing (hot/cold water, drainage)

**Opening Stock:**

- [RFQ-READY] I03: Foot files/pumice
- [RFQ-READY] I04: Foot towels
- [RFQ-READY] I05: Toe separators (disposable)
- [RFQ-READY] I06: Pipeless chair sanitation kit

---

## 6. Massage Area

**Furniture:**

- [RFQ-READY] F01a: Pregnancy massage table
- [FOUNDER DECISION] F01b: Massage station chair

**Equipment:**

- [RFQ-READY] F02: Bolster/positioning pillow set
- [INFORMATION REQUIRED] F12: Practitioner apron/uniform

**Fixtures:**

- [RFQ-READY] F05: Trolley/tool cart
- [RFQ-READY] F09: Curtain partition per treatment room

**Lighting:**

- [RFQ-READY] F10: Task/ambient lighting per station

**Consumables:**

- [RFQ-READY] F03: Heated blanket

**Opening Stock:**

- [RFQ-READY] F06: Massage table linen (sheets, pillowcases)
- [RFQ-READY] F07: Pregnancy-safe massage oil
- [RFQ-READY] F08: Aromatherapy/hamper items
- [RFQ-READY] F11: Disposable table-roll paper or equivalent barrier

**Future/Optional:**

- [FUTURE/OPTIONAL] F04: Massage oil warming unit

---

## 7. Beauty Area

**Furniture:**

- [RFQ-READY] G01: Facial/beauty treatment bed
- [RFQ-READY] G02: Practitioner stool

**Equipment:**

- [ORDER-READY] G04: Wax heater (dual-pot, professional)
- [RFQ-READY] G05: Brow/lash tool kit
- [FOUNDER DECISION] G06: Facial steamer
- [INFORMATION REQUIRED] G15: Practitioner uniform

**Fixtures:**

- [RFQ-READY] G07: Trolley/tool cart

**Electrical:**

- [PROFESSIONAL VERIFICATION] G14: Standard GPO, task lighting per station

**Lighting:**

- [RFQ-READY] G03: Magnifying lamp (LED, adjustable)

**Safety:**

- [PROFESSIONAL VERIFICATION] G08: 2-sink fitout (hand-wash + instrument decontamination)

**Opening Stock:**

- [RFQ-READY] G09: Treatment bed linen (disposable or machine-washable)
- [RFQ-READY] G10: PPD-free brow tint
- [RFQ-READY] G11: Wax (strip + hard, pregnancy-safe)
- [RFQ-READY] G12: Facial products (HA serum, niacinamide, pregnancy-safe masks)
- [RFQ-READY] G13: Disposable brow/wax consumables

---

## 8. Reception

**Fixtures:**

- [RFQ-READY] B01: Reception counter
- [RFQ-READY] B02: Reception chair (Venue Manager)
- [ORDER-READY] B03: Computer/laptop
- [RFQ-READY] B04: Monitor
- [RFQ-READY] B05: Keyboard/mouse
- [RFQ-READY] B06: Phone (landline or VoIP)
- [ORDER-READY] B07: POS terminal
- [ORDER-READY] B08: iPad (9th gen or Air), core
- [ORDER-READY] B09: iPad kiosk stand
- [ORDER-READY] B10: B&W laser printer
- [ORDER-READY] B13: Booking software subscription (Fresha)
- [RFQ-READY] B14: Cable management (under-desk)
- [RFQ-READY] B16: Filing storage (lockable, for referral forms/patient records)
- [RFQ-READY] B17: Charging station (staff phones/devices)
- [FOUNDER DECISION] B18: Retail display shelving

**Opening Stock:**

- [RFQ-READY] B15: Stationery (pens, notepads, staplers, folders)

**Future/Optional:**

- [FUTURE/OPTIONAL] B11: Colour inkjet printer
- [FUTURE/OPTIONAL] B12: Scanner

---

## 9. Cafe

**Equipment:**

- [ORDER-READY] C01: Full-size beverage refrigerator
- [ORDER-READY] C02: Display refrigerator (sandwiches/rolls)
- [ORDER-READY] C03: Coffee machine
- [ORDER-READY] C04: Chilled and boiling water tap
- [ORDER-READY] C05: Toastie press
- [SITE-DEPENDENT] C19: Preparation/serving counter
- [PROFESSIONAL VERIFICATION] C20: Handwashing station (Cafe-specific)

**Fixtures:**

- [ORDER-READY] C16: Customer-accessible display shelving
- [FOUNDER DECISION] C17: Menu board/signage

**Consumables:**

- [RFQ-READY] C07: Fridge/freezer thermometer
- [RFQ-READY] C09: Chopping board/utensils (toastie assembly only, no raw-ingredient prep)
- [PROFESSIONAL VERIFICATION] C26: Food Business Notification (local council)

**Technology:**

- [RFQ-READY] C18: Cafe POS integration

**Cleaning:**

- [RFQ-READY] C21: Cafe-specific waste bin (food waste, separate from general/biohazard)

**Opening Stock:**

- [RFQ-READY] C06: Food storage containers (sealed, stackable)
- [RFQ-READY] C08: Food handling gloves
- [RFQ-READY] C10: Cups (dine-in)
- [RFQ-READY] C11: Plates (dine-in)
- [RFQ-READY] C12: Takeaway cups (hot drinks)
- [RFQ-READY] C13: Takeaway lids
- [RFQ-READY] C14: Napkins
- [RFQ-READY] C15: Cutlery (disposable or reusable)
- [RFQ-READY] C22: Pre-made sandwiches/rolls
- [RFQ-READY] C23: Coffee beans/milk/syrups
- [RFQ-READY] C24: Herbal tea (free to all clients)
- [RFQ-READY] C25: Bottled/canned cold drinks

---

## 10. Lounge

**Furniture:**

- [SITE-DEPENDENT] D01: Three-seat couch
- [SITE-DEPENDENT] D02: Side table with charging port
- [SITE-DEPENDENT] D03: Low coffee table

**Fixtures:**

- [FOUNDER DECISION] D10: Signage (Lounge wayfinding)
- [FOUNDER DECISION] D12: Portable AV/PA equipment for classes/ticketed sessions

**Lighting:**

- [ORDER-READY] D04: Floor lamp (soft, warm)

**Technology:**

- [RFQ-READY] D05: Tablet (kiosk-mounted, pregnancy/postpartum information)
- [RFQ-READY] D06: Tablet stand/mount
- [RFQ-READY] D07: Wi-Fi access point (Lounge zone)

**Cleaning:**

- [SITE-DEPENDENT] D11: Bin (general waste, Lounge zone)

**Opening Stock:**

- [RFQ-READY] D08: Heated throw blankets
- [ORDER-READY] D09: Curated reading material

---

## 11. Staff Area

**Furniture:**

- [INFORMATION REQUIRED] L01: Lockers
- [RFQ-READY] L02: Staff table
- [INFORMATION REQUIRED] L05: Chairs (staff break)

**Equipment:**

- [RFQ-READY] L03: Kettle

**Fixtures:**

- [RFQ-READY] L06: Small fridge (staff use)
- [RFQ-READY] L07: Microwave (staff use)

**Plumbing:**

- [PROFESSIONAL VERIFICATION] L04: Staff sink

---

## 12. Storage

**Fixtures:**

- [RFQ-READY] M01: Clean linen storage shelving/cabinet
- [RFQ-READY] M02: Dirty linen/biohazard storage
- [SITE-DEPENDENT] M03: General retail/product storage shelving
- [RFQ-READY] M04: Consumables stockroom shelving (nail/hair/beauty products)

---

## 13. Toilets

**Fixtures:**

- [SITE-DEPENDENT] N04: Soap dispenser
- [SITE-DEPENDENT] N05: Paper towel dispenser
- [SITE-DEPENDENT] N06: Sanitary disposal unit
- [FOUNDER DECISION] N08: Hand dryer (if selected instead of paper towel)
- [PROFESSIONAL VERIFICATION] N13: Accessibility grab rails, accessible WC fittings

**Signage:**

- [SITE-DEPENDENT] N14: Toilet signage (including accessibility symbol)

**Cleaning:**

- [SITE-DEPENDENT] N09: Bin (general)
- [SITE-DEPENDENT] N10: Toilet brush
- [RFQ-READY] N11: Plunger

**Opening Stock:**

- [RFQ-READY] N01: Toilet paper
- [RFQ-READY] N02: Paper towel (hand-drying)
- [RFQ-READY] N03: Hand soap
- [RFQ-READY] N16: Spare stock (toilet paper, soap, paper towel reserve)

**Future/Optional:**

- [FUTURE/OPTIONAL] N07: Sanitary products (complimentary)
- [FUTURE/OPTIONAL] N12: Air freshener (if appropriate to the brand)

---

## 14. Cleaning / Laundry

**Equipment:**

- [RFQ-READY] O13: Cleaning caddies
- [RFQ-READY] P06: Laundry bags/hampers
- [FOUNDER DECISION] P10: Commercial washer/dryer

**Fixtures:**

- [RFQ-READY] O01: Commercial vacuum
- [RFQ-READY] O02: Mop system (bucket + wringer)
- [RFQ-READY] O03: Buckets
- [RFQ-READY] O04: Dustpans/brooms
- [RFQ-READY] O17: Cleaning products storage (lockable)
- [FOUNDER DECISION] P11: Outsourced commercial laundry contract

**Signage:**

- [RFQ-READY] O14: Wet floor warning signs

**Safety:**

- [RFQ-READY] O16: Spill kit (general, non-biohazard)

**Opening Stock:**

- [RFQ-READY] O05: Microfibre cloths
- [RFQ-READY] O06: General-purpose disinfectant
- [RFQ-READY] O07: Bathroom cleaner
- [RFQ-READY] O08: Glass cleaner
- [RFQ-READY] O09: Floor cleaner
- [RFQ-READY] O10: Bin liners (general)
- [RFQ-READY] O12: Cleaning gloves (heavy-duty)
- [RFQ-READY] O15: Paper products (general-area hand towel, tissues)
- [RFQ-READY] P01: Towels (general/hand)
- [RFQ-READY] P02: Face towels
- [RFQ-READY] P07: Detergent
- [RFQ-READY] P08: Stain remover
- [RFQ-READY] P09: Disinfecting laundry additive (for clinical/treatment linen)

---

## 15. Clinical / Waste Area

**Fixtures:**

- [RFQ-READY] Q03: Digital thermometer (general use, non-cold-chain)
- [SITE-DEPENDENT] AA03: General waste collection contract

**Opening Stock:**

- [RFQ-READY] Q01: Consent/intake forms (printed)
- [RFQ-READY] Q02: Referral cards (printed)

---

## 16. General Venue Infrastructure

**Equipment:**

- [RFQ-READY] AB03: Equipment service/maintenance contracts (centrifuge, LEV units, coffee machine)

**Fixtures:**

- [PROFESSIONAL VERIFICATION] A01: Fire extinguishers
- [SITE-DEPENDENT] A02: Emergency exit signage
- [PROFESSIONAL VERIFICATION] A03: Smoke detectors/alarm system
- [SITE-DEPENDENT] A04: Air conditioning/HVAC servicing
- [PROFESSIONAL VERIFICATION] A05: Power outlets (GPO), general
- [PROFESSIONAL VERIFICATION] A06: Data/network cabling
- [RFQ-READY] A07: Building insurance certificate of currency
- [FOUNDER DECISION] A08: Business name/lease signage (external)
- [RFQ-READY] A10: Umbrella stand
- [RFQ-READY] AB01: Basic tool kit (screwdrivers, allen keys for furniture assembly/maintenance)
- [RFQ-READY] AD01: Spare phlebotomy chair componentry (armrests, wipe-clean covers)
- [FOUNDER DECISION] W01: External signage (business name/logo)
- [SITE-DEPENDENT] W02: Internal wayfinding signage
- [INFORMATION REQUIRED] W06: Name badges
- [SITE-DEPENDENT] W08: Decor/artwork
- [FOUNDER DECISION] W11: Scent/ambience diffuser
- [PROFESSIONAL VERIFICATION] X01: General ambient lighting
- [PROFESSIONAL VERIFICATION] X02: Task + ambient lighting
- [PROFESSIONAL VERIFICATION] X04: Clinical-standard lighting
- [PROFESSIONAL VERIFICATION] X05: Task lighting per station
- [PROFESSIONAL VERIFICATION] X06: Task lighting per chair
- [PROFESSIONAL VERIFICATION] X07: Task/ambient lighting per station
- [PROFESSIONAL VERIFICATION] X10: General ambient lighting
- [PROFESSIONAL VERIFICATION] X11: General ambient lighting
- [PROFESSIONAL VERIFICATION] X12: General ambient lighting
- [PROFESSIONAL VERIFICATION] X13: Basic utility lighting
- [PROFESSIONAL VERIFICATION] X14: Emergency lighting
- [FOUNDER DECISION] X16: Signage lighting

**Opening Stock:**

- [SITE-DEPENDENT] A09: Floor mats (entry, wet-weather)
- [RFQ-READY] AB02: Spare lightbulbs/fixtures
- [RFQ-READY] AD02: Spare GPO adaptors/power boards
- [RFQ-READY] AD03: Spare AED pads/battery
- [RFQ-READY] AD04: Spare sharps containers, biohazard bags
- [RFQ-READY] W04: Printed materials (brochures, referral cards)
- [RFQ-READY] W07: Branded stationery

**Future/Optional:**

- [FUTURE/OPTIONAL] W09: Mirrors (decorative, beyond the functional Hair mirror in J02)
- [FUTURE/OPTIONAL] W10: Planters (if appropriate)
- [FUTURE/OPTIONAL] X15: Feature/decorative lighting

---

## 17. IT / Security

**Fixtures:**

- [ORDER-READY] T01: WiFi router (commercial grade)
- [SITE-DEPENDENT] T02: Network switches
- [SITE-DEPENDENT] T03: Access points (WiFi coverage across the full floor plate)
- [RFQ-READY] T11: Backup device/cloud backup subscription

**Future/Optional:**

- [FUTURE/OPTIONAL] T08: Security cameras
- [FUTURE/OPTIONAL] T09: Access control (e.g. keypad/fob entry)
- [FUTURE/OPTIONAL] T10: UPS (uninterruptible power supply)
- [FUTURE/OPTIONAL] T13: Small TV/display
- [FUTURE/OPTIONAL] V03: Alarm system

---

## 18. Staff / Emergency Equipment

**Fixtures:**

- [RFQ-READY] R01: AED (Automated External Defibrillator)
- [SITE-DEPENDENT] R03: Panic buttons
- [INFORMATION REQUIRED] R06: First Aid/CPR accredited course (per staff member)

**Opening Stock:**

- [ORDER-READY] R02: First aid kit (comprehensive)
- [RFQ-READY] R07: EpiPen (anaphylaxis)
- [RFQ-READY] S01: Disposable gloves (general, non-clinical, non-nail)
- [RFQ-READY] S02: Hand sanitiser (public-facing, Reception/Lounge/Cafe)

---

## Coverage Check

All 26 register categories accounted for across the 18 areas above: Yes.

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (authoritative quantities, prices, and full specification for every Item ID above), `docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md`, `tools/generate_procurement_room_checklist.py`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 3) as a room-by-room walk-through checklist, generated mechanically as a cross-reference view over the master register rather than a duplicated quantity table, to avoid any risk of the two documents disagreeing.
