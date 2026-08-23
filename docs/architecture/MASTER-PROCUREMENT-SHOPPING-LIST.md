# Master Procurement & Shopping List

Status: current as of 2026-08-23. This is the single authoritative, itemised procurement register for physically opening GTT Center Perth: every purchasable item, its quantity and the basis for that quantity, its specification, its sourcing classification, and what still needs professional or site verification before it can be purchased. It supersedes `docs/equipment-costs.md` and `docs/architecture/FIT-OUT-EQUIPMENT-SCHEDULE.md`'s role as the primary procurement source; those documents remain as historical research trail, not the current reference.

**Test this document is built to pass:** a competent person who has never worked in a wellness centre, salon, cafe, or pathology collection centre should be able to read a row and know what to buy, how many, what area it belongs to, what specification it must meet, whether it is a China candidate or an Australian purchase, and what still needs verification.

**Source-of-truth basis (read first, per `docs/architecture/SOURCE-OF-TRUTH-TIERS.md`):** `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md` (current venue program), `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` (Round 3 recommendations), `docs/architecture/STAFF-POSITION-REGISTER.md` and `STAFF-PROFILES-COMPLETE.md` (headcount basis for staff-dependent quantities), `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` (sourcing classification), `docs/CURRENT-STATE.md`, the current Master Dossier, the current Dash. Superseded figures from older documents (2 Massage/Beauty rooms, spray tan, GDM snack pack, landlord contribution, current property listings) are not carried forward here.

**Quantity basis key:** LOCKED (a fixed, already-decided quantity) / CALCULATED (derived from the operating model, position register, or solver output) / SITE-DEPENDENT (depends on the confirmed venue's actual floor plate) / STAFF-DEPENDENT (depends on employed headcount) / CONSUMPTION-DEPENDENT (opening stock plus an ongoing reorder, no invented consumption rate) / OPTIONAL (a genuine upgrade, not core) / PROFESSIONAL-VERIFICATION (needs a named type of Australian professional before finalising) / FOUNDER-DECISION (a real, unresolved decision) / WDP-DEPENDENT (depends on the pathology partner's final commercial arrangement).

**Sourcing key:** AU (Australia/local purchase) / CN (genuine China sourcing candidate) / HY (hybrid, source-dependent on final spec) / PRO (professional procurement, e.g. medical/clinical equipment via a named channel) / WDP (WDP-dependent) / SITE (venue-dependent, cannot be sourced before a venue is confirmed).

**Pricing key:** where an existing repository price exists, it is used directly, not re-estimated. Where none exists: QUOTE REQUIRED (general), CHINA RFQ REQUIRED, AU RFQ REQUIRED, or SITE QUOTE REQUIRED. No price is invented.

**Research standard applied in this document:** genuine information gaps that can be answered through research have been researched this round (WA Skin Penetration Code, WA Food Business Risk Classification, cleaning/infection-control product categories), not left as "needs research." Genuinely open founder decisions and genuinely site-dependent items are labelled as such, not disguised as research gaps.

---

## A. Venue / General Building

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A01 | Venue | General | Fire extinguishers | ABE-rated dry chemical, per venue floor area | To be determined | each | PROFESSIONAL-VERIFICATION | No | N/A | AU | Fire safety officer/building surveyor sign-off | No | Yes | No | Yes | Open | Local council/building code will dictate exact count and type |
| A02 | Venue | General | Emergency exit signage | Illuminated, AS 2293 compliant | To be determined | each | SITE-DEPENDENT | No | N/A | AU | AS 2293, building surveyor | No | Yes | No | Yes | Open | Depends on venue exit configuration |
| A03 | Venue | General | Smoke detectors/alarm system | Building-code compliant | To be determined | each | PROFESSIONAL-VERIFICATION | No | N/A | AU | Building surveyor, fire safety | No | Yes | No | Yes | Open | Likely landlord/base-building responsibility, confirm at lease |
| A04 | Venue | General | Air conditioning/HVAC servicing | Ongoing service contract | 1 | contract | SITE-DEPENDENT | No | Yes, annual | AU | HVAC contractor | No | Yes | No | Yes | Open | Depends on existing venue plant |
| A05 | Venue | General | Power outlets (GPO), general | Standard double GPO, per room per the venue program | To be determined | each | PROFESSIONAL-VERIFICATION | No | N/A | AU | Licensed electrician | No | Yes | No | Yes | Open | Exact count is an electrician's job, not a shopping-list quantity |
| A06 | Venue | General | Data/network cabling | Cat6, to reception, cafe POS, and any networked device location | To be determined | run | PROFESSIONAL-VERIFICATION | No | N/A | AU | Licensed data cabler | No | Yes | No | Yes | Open | Site-specific |
| A07 | Venue | General | Building insurance certificate of currency | Public Liability + Professional Indemnity + Property/Contents, A$708.34/month (Chapter 27) | 1 | policy | LOCKED | No | Yes, annual | AU | Insurance broker | No | Yes | No | No | Open | Real broker quotes already in motion |
| A08 | Venue | General | Business name/lease signage (external) | Design-dependent, gated on the final name decision (Chapter 5) | 1 | unit | FOUNDER-DECISION | No | N/A | AU | Local council signage permit | No | Yes | No | Yes | Open | Cannot be finalised until SOLENA/ELOWEN is decided |
| A09 | Venue | General | Floor mats (entry, wet-weather) | Commercial-grade, slip-resistant | 2-3 | each | SITE-DEPENDENT | Yes | Yes | AU | AS/NZS 4586 slip resistance | No | Yes | No | Yes | Open | |
| A10 | Venue | General | Umbrella stand | For wet-weather clients | 1 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | Low-value, either sourcing works |

---

## B. Reception

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B01 | Reception | Reception | Reception counter | 900mm standard height + 750mm low accessible section, warm stone/timber finish matching the locked palette | 1 | each | LOCKED | No | No | SITE | Custom, site-installed local trade, not a shippable import | No | Yes | No | Yes | Open | Structural build, not a China-sourceable item |
| B02 | Reception | Reception | Reception chair (Venue Manager) | Ergonomic office chair | 1 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |
| B03 | Reception | Reception | Computer/laptop | Business-grade, A$800-1,500 | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Priced | A$800-1,500, JB Hi-Fi/Officeworks business account |
| B04 | Reception | Reception | Monitor | Standard business monitor | 1 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |
| B05 | Reception | Reception | Keyboard/mouse | Standard | 1 set | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |
| B06 | Reception | Reception | Phone (landline or VoIP) | Business line | 1 | each | LOCKED | No | No | AU | Telco compliance | No | Yes | No | No | Open | |
| B07 | Reception | Reception | POS terminal | Square/Tyro/Stripe Reader, A$0-120 | 2 | each | LOCKED | No | No | AU | Payment-industry standard | No | Yes | No | No | Priced | A$0-120, Square Terminal A$299 alternative |
| B08 | Reception | Reception | iPad (9th gen or Air), core | Booking/check-in via Fresha | 2 | each | LOCKED | No | No | AU | N/A | No | Yes | No | No | Priced | A$550-750 each |
| B09 | Reception | Reception | iPad kiosk stand | Lockable, charging | 2-3 | each | LOCKED | No | No | AU | Electrical safety mark on charging module | No | Yes | No | No | Priced | A$80-150 each |
| B10 | Reception | Reception | B&W laser printer | For consent forms, referral copies | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Priced | A$200-400 |
| B11 | Reception | Reception | Colour inkjet printer | Optional upgrade | 1 | each | OPTIONAL | No | No | AU | None | No | Yes | No | No | Priced | A$150-300, deferred in MVP scenario |
| B12 | Reception | Reception | Scanner | If separate from printer | 0-1 | each | OPTIONAL | No | No | AU | None | No | Yes | No | No | Open | Most business printers include scan function, may not be a separate purchase |
| B13 | Reception | Reception | Booking software subscription (Fresha) | Team plan, 1-2 seats | 1 | subscription | LOCKED | No | N/A | AU | N/A | No | Yes | No | No | Priced | A$14.95/user/month |
| B14 | Reception | Reception | Cable management (under-desk) | Standard | 1 lot | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| B15 | Reception | Reception | Stationery (pens, notepads, staplers, folders) | General office | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | Opening stock policy TBD |
| B16 | Reception | Reception | Filing storage (lockable, for referral forms/patient records) | Lockable cabinet | 1 | each | LOCKED | No | No | HY | Privacy Act record-keeping compliance | Possible | Either | No | No | Open | 7-year retention requirement (Chapter 7) |
| B17 | Reception | Reception | Charging station (staff phones/devices) | Multi-port USB | 1 | each | LOCKED | No | No | CN | Electrical safety mark | Yes | Yes | No | No | Open | |
| B18 | Reception | Reception | Retail display shelving | Wall-mounted, visible from Lounge | 1 | each | FOUNDER-DECISION | No | No | HY | None | Possible | Either | No | Yes | Open | Retail is not currently a priority; no locked brand selected, per current direction |

**Explicitly not procured: a dedicated PM Reception workstation or role.** PM reception is covered by rostered service staff during natural gaps between their own PM bookings (Model C, confirmed founder decision), using the same Fresha/POS equipment already itemised above, not a second set of reception equipment.

---

## C. Cafe / Food & Beverage

**Current model (researched and current, not a snack-pack model):** clients purchase food and beverages directly. Food is not manufactured or cooked from raw ingredients on site; it is supplied pre-made by an external supplier (not yet identified, a genuine procurement dependency, not invented here), stored correctly, and displayed for sale. Selected items may be warmed or toasted on site. Coffee and other hot/cold drinks are available for purchase. Free water and herbal tea remain available to every client regardless of purchase. Researched this round against the WA Food Business Risk Classification System's own 2024 scoring rubric: this model scores in the Low risk band (approximately 36 points of 7-39), with council notification still required at least 14 days before trading regardless of tier.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Cafe | Food Service Equipment | Full-size beverage refrigerator | Commercial grade | 1 | each | LOCKED | No | No | AU | Food-safety cold-chain requirement | No | Yes | No | No | Priced | A$800-1,800 |
| C02 | Cafe | Refrigeration | Display refrigerator (sandwiches/rolls) | Temperature-controlled, customer-visible | 1 | each | LOCKED | No | No | AU | Food-safety cold-chain requirement | No | Yes | No | No | Priced | A$1,200-2,500 |
| C03 | Cafe | Beverage Equipment | Coffee machine | Espresso-capable, hot and cold drink formats | 1 | each | LOCKED | No | No | HY | Electrical safety mark | Possible for base unit, service/parts AU | Either | No | No | Priced | A$1,500-4,000 |
| C04 | Cafe | Beverage Equipment | Chilled and boiling water tap | Under-counter unit | 1 | each | LOCKED | No | No | AU | Plumbing, electrical safety mark | No | Yes | No | Yes | Priced | A$800-1,800; requires plumbed water supply, site-dependent install |
| C05 | Cafe | Heating/Toasting | Toastie press | Commercial grade | 1 | each | LOCKED | No | No | HY | Electrical safety mark | Possible | Either | No | No | Priced | A$150-350 |
| C06 | Cafe | Storage | Food storage containers (sealed, stackable) | Commercial food-grade | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Food-safety storage requirement | Yes | Either | No | No | Open | |
| C07 | Cafe | Food Safety | Fridge/freezer thermometer | Digital, with log sheet | 2 | each | LOCKED | No | No | AU | Food-safety cold-chain temperature logging | No | Yes | No | No | Open | Low cost |
| C08 | Cafe | Food Safety | Food handling gloves | Disposable, food-grade | 1 lot | box | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Food handling standard | Yes | Either | No | No | Open | |
| C09 | Cafe | Food Safety | Chopping board/utensils (toastie assembly only, no raw-ingredient prep) | Colour-coded, dishwasher-safe | 1 set | set | LOCKED | No | No | CN | Food-safety hygiene | Yes | Yes | No | No | Open | Assembly/toasting only, not raw-ingredient cooking |
| C10 | Cafe | Crockery | Cups (dine-in) | Ceramic, branded or plain per current brand palette | 24-36 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Yes | Either | No | No | Open | |
| C11 | Cafe | Crockery | Plates (dine-in) | Ceramic | 12-24 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Yes | Either | No | No | Open | |
| C12 | Cafe | Takeaway Items | Takeaway cups (hot drinks) | Compostable/recyclable, branded | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | Food-safe packaging standard | Yes | Yes | No | No | Open | |
| C13 | Cafe | Takeaway Items | Takeaway lids | Matching takeaway cup size | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | Food-safe packaging standard | Yes | Yes | No | No | Open | |
| C14 | Cafe | Takeaway Items | Napkins | Branded or plain | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| C15 | Cafe | Takeaway Items | Cutlery (disposable or reusable) | Food-grade | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Food-safe standard | Yes | Either | No | No | Open | Reusable preferred for the premium positioning, disposable as a fallback |
| C16 | Cafe | Display | Customer-accessible display shelving | Self-selection of packaged items | 1 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Priced | A$150-400 |
| C17 | Cafe | Display | Menu board/signage | Design-dependent, current brand palette | 1 | each | FOUNDER-DECISION | No | No | HY | None | Possible | Either | No | Yes | Open | Gated on final naming decision |
| C18 | Cafe | POS | Cafe POS integration | Shares reception's POS terminal (B07), not a separate purchase | 0 | each | LOCKED | No | No | AU | N/A | No | Yes | No | No | Locked | No separate cafe POS hardware required |
| C19 | Cafe | Staff Equipment | Preparation/serving counter | Within the Cafe's existing solid-walled footprint | 1 | each | SITE-DEPENDENT | No | No | SITE | Local trade, food-business fitout standard | No | Yes | No | Yes | Open | Custom, site-installed |
| C20 | Cafe | Staff Equipment | Handwashing station (Cafe-specific) | Separate from any clinical hand-hygiene station | 1 | each | PROFESSIONAL-VERIFICATION | No | No | AU | WA food-business hygiene requirement | No | Yes | No | Yes | Open | Confirm exact requirement with local council EHO |
| C21 | Cafe | Waste | Cafe-specific waste bin (food waste, separate from general/biohazard) | Lidded, foot-pedal | 1-2 | each | LOCKED | No | No | HY | Food-safety waste segregation | Possible | Either | No | No | Open | |
| C22 | Cafe | Supplier/Food Stock | Pre-made sandwiches/rolls | External supplier, not yet identified | Ongoing | unit | CONSUMPTION-DEPENDENT | Yes | Yes | PRO | WA food business notification, supplier's own food-safety certification | No | Yes (supplier, not this venture) | No | No | Open | **Genuine procurement dependency: no external food supplier identified yet, not invented here** |
| C23 | Cafe | Supplier/Food Stock | Coffee beans/milk/syrups | Wholesale coffee supplier | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Food-safety storage | No | Yes | No | No | Open | Supplier not yet selected |
| C24 | Cafe | Supplier/Food Stock | Herbal tea (free to all clients) | Bulk supply | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| C25 | Cafe | Supplier/Food Stock | Bottled/canned cold drinks | Wholesale beverage supplier | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| C26 | Cafe | Food Safety | Food Business Notification (local council) | Administrative, not a physical item, required at least 14 days before trading | 1 | filing | PROFESSIONAL-VERIFICATION | No | N/A | AU | WA Food Act 2008, Food Business Notification Form | No | N/A | No | Yes | Open | Council-specific, gated on venue confirmation |

**Not procured: any snack pack. No item is provided to clients after the final blood draw as a separate food/snack service.** The glucose drink itself is a phlebotomist workflow item, covered under Blood Collection (Section E), not Cafe.

---

## D. Lounge / Waiting Area

**Current model:** the Lounge is the waiting area, seated with couches, not reclining chairs. Approximately 3-4 three-seat couches, final quantity set by the actual floor area once a venue is confirmed. Clients not currently receiving a blood draw or treatment use the Lounge. Tablets are available for pregnancy/postpartum information and documents. The Lounge may later host classes or ticketed information sessions outside normal operating hours (a future-use consideration, not a day-one physical requirement beyond adequate general floor space).

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Lounge | Furniture | Three-seat couch | Not reclining chairs, per current direction | 3-4 | each | SITE-DEPENDENT | No | No | HY | AS/NZS 4088 stability, upholstery flammability standard | Possible | Genuinely needs in-person testing before bulk purchase | No | Yes | Priced | A$1,200-3,000 each; final count set by venue floor area, do not lock a number before a venue is confirmed |
| D02 | Lounge | Furniture | Side table with charging port | USB-A/USB-C | 4-6 | each | SITE-DEPENDENT | No | No | CN | Electrical safety mark on charging module | Yes | Yes | No | Yes | Priced | A$150-300 each |
| D03 | Lounge | Furniture | Low coffee table | N/A | 3-4 | each | SITE-DEPENDENT | No | No | CN | None | Yes | Yes | No | Yes | Priced | A$100-250 each |
| D04 | Lounge | Lighting | Floor lamp (soft, warm) | Matches the locked palette | 4 | each | LOCKED | No | No | CN | SAA electrical mark | Yes | Yes | No | No | Priced | A$80-150 each |
| D05 | Lounge | Technology | Tablet (kiosk-mounted, pregnancy/postpartum information) | Curated content only, no open browser, no app store, no social login | 2 | each | LOCKED | No | No | AU | Kiosk-mode device management | No | Yes | No | No | Open | Content licensing and device brand not yet finalised |
| D06 | Lounge | Technology | Tablet stand/mount | Kiosk-mode, secure, charging | 2 | each | LOCKED | No | No | CN | Electrical safety mark | Yes | Yes | No | No | Open | |
| D07 | Lounge | Technology | Wi-Fi access point (Lounge zone) | Part of venue-wide network | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Open | Shared with venue-wide IT, Section T |
| D08 | Lounge | Decor | Heated throw blankets | Complimentary for clients | 20 | each | CONSUMPTION-DEPENDENT | Yes | Yes | CN | Electrical safety mark | Yes | Yes | No | No | Priced | A$15-25 each |
| D09 | Lounge | Decor | Curated reading material | Pregnancy/postpartum information and documents | 1 lot | lot | LOCKED | Yes | Yes | AU | None | No | Yes | No | No | Priced | A$200-400 |
| D10 | Lounge | Decor | Signage (Lounge wayfinding) | Design-dependent | 1 | each | FOUNDER-DECISION | No | No | HY | None | Possible | Either | No | Yes | Open | Gated on naming decision |
| D11 | Lounge | Waste | Bin (general waste, Lounge zone) | Lidded | 1-2 | each | SITE-DEPENDENT | No | No | CN | None | Yes | Yes | No | Yes | Open | |
| D12 | Lounge | Future Use | Portable AV/PA equipment for classes/ticketed sessions | Only if the Lounge's future-use plan is activated | 0 (future) | each | FOUNDER-DECISION | No | No | AU | None | No | Yes | No | No | Open | Not a day-one requirement; flagged for the venture's own growth path, Chapter 33 |

**Not procured: a small TV/screen, snack display stand, mini fridge, or herbal tea station in the Lounge.** Beverage/food service now belongs entirely to the Cafe (Section C); the Lounge is purely a waiting/seating area with tablets, per current direction.

---

## E. Blood Collection (Core Business: Maximum Detail)

**Current model (`docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`):** one Blood Collection Room, built and serviced for 3 chairs from day one, staffed with 2 chairs (Chair A/Chair B) at opening, compatible with a 4-phlebotomist employment pool (PHL01-PHL04, 2 simultaneous, 2 relief). Solid walls, no public-facing window. Distinguishing: (1) GTT Center Perth purchases directly, (2) WDP-supplied items, (3) items dependent on WDP's final commercial arrangement, (4) items requiring Australian clinical/professional verification.

### E1. Furniture and Clinical Work Surfaces

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E01 | Blood Collection | Furniture | Phlebotomy chair (Chair A) | Reclines to flat, adjustable arm support, vinyl wipe-clean, wide/bariatric seat | 1 | each | LOCKED | No | No | PRO | Clinical suitability sign-off from the pathology partner | No | Yes, named Perth medical-furniture brands (Sunflower Medical, Alphatec Australia, Ultramedic) | No, GTT Center purchases | No | Priced | A$800-1,200 |
| E02 | Blood Collection | Furniture | Phlebotomy chair (Chair B) | Same as E01 | 1 | each | LOCKED | No | No | PRO | Same as E01 | No | Yes | No | No | Priced | A$800-1,200 |
| E03 | Blood Collection | Furniture | 3rd phlebotomy chair (growth reservation) | Same spec as E01/E02, room built to accommodate but not purchased at day-one | 0 (day-one), 1 (growth) | each | CALCULATED | No | No | PRO | Same as E01 | No | Yes | No | No | Open | Room is built/serviced for 3 chairs from day one (Chapter 20); the 3rd chair itself is a staffing/demand-triggered purchase, not a day-one purchase |
| E04 | Blood Collection | Furniture | Vasovagal recliner/exam couch | Full recline to flat, separate from the 2 active phlebotomy chairs, for fainting/vasovagal recovery | 1 | each | LOCKED | No | No | AU | Non-TGA furniture item | No | Yes | No | No | Priced | A$500-900 |
| E05 | Blood Collection | Furniture | Documentation desk/bench | 900mm min width | 1 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |
| E06 | Blood Collection | Furniture | Phlebotomist stool (adjustable height) | Wipe-clean, adjustable | 2 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |

### E2. Storage, Sharps Disposal, Clinical Waste

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E07 | Blood Collection | Storage | Medical consumables cabinet (lockable) | N/A | 1 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Priced | A$200-400 |
| E08 | Blood Collection | Storage | Patient documentation drawer (lockable) | Privacy Act compliant record storage | 1 | each | LOCKED | No | No | HY | Privacy Act record-keeping | Possible | Either | No | No | Priced | A$100-200 |
| E09 | Blood Collection | Sharps Disposal | Sharps container, bench size (1.4L) | AS/NZS 23907:2023 compliant | 2 | each | LOCKED | Yes | Yes | AU | AS/NZS 23907:2023 | No | Yes, named brands (Daniels Health, Cleanaway Medical, Stericycle) | No | No | Priced | A$5-15 each, consumable |
| E10 | Blood Collection | Sharps Disposal | Sharps container, room size (5L) | AS/NZS 23907:2023 compliant | 2 | each | LOCKED | Yes | Yes | AU | AS/NZS 23907:2023 | No | Yes | No | No | Priced | A$5-15 each, consumable |
| E11 | Blood Collection | Sharps Disposal | Wall-mounted sharps container bracket | N/A | 2 | each | LOCKED | No | No | AU | AS/NZS 23907:2023 | No | Yes | No | No | Priced | A$20-40 each |
| E12 | Blood Collection | Clinical Waste | Biohazard waste bin (yellow, lidded) | AS/NZS clinical waste standard | 2 | each | LOCKED | No | No | AU | Clinical waste handling standard | No | Yes | No | No | Priced | A$35-60 each |
| E13 | Blood Collection | Clinical Waste | Biohazard specimen pouches | Box of 100 | 2 boxes | box | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Clinical waste standard | No | Yes | No | No | Priced | A$25-40/box |
| E14 | Blood Collection | Clinical Waste | Medical waste disposal contract | Annual service, not a one-off purchase | 1 | contract | WDP-DEPENDENT | No | Yes, annual | AU | Council/WorkSafe WA compliance | No | Yes | Possibly, confirm whether WDP's own collection-centre setup already covers it | Yes (confirm at lease) | Open | **Genuine open dependency: whether WDP's own arrangement covers this, not assumed either way (Chapter 34)** |

### E3. Specimen Handling and Pathology/Collection Equipment

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E15 | Blood Collection | Specimen Handling | Tabletop centrifuge (refrigerated) | 3,000 RPM min, 8+ position rotor; GDM underdiagnosis risk without centrifugation within 10 minutes | 1 | each | LOCKED | No | No | WDP | NATA acceptance confirmation before purchase of any non-established-brand alternative | No | Yes, if purchased directly (Hettich Universal 320R, Thermo Scientific CL10) | Likely, sourced via the WDP relationship, not general retail | No | Priced | A$1,800-5,000; the single most critical piece of equipment in the venue, do not compromise on quality |
| E16 | Blood Collection | Specimen Handling | Specimen refrigerator | 2-8°C, temperature logged | 1 | each | LOCKED | No | No | AU | Cold-chain, temperature-logging requirement | No | Yes | No | No | Open | |
| E17 | Blood Collection | Specimen Handling | Insulated specimen transport bag | For courier/drop-off dispatch | 2 | each | LOCKED | No | Yes | AU | Cold-chain standard | No | Yes | No | No | Priced | A$40-60 each |
| E18 | Blood Collection | Specimen Handling | Ice packs (reusable, cold chain) | N/A | 6 | each | LOCKED | Yes | Yes | AU | None | No | Yes | No | No | Priced | A$8-15 each |
| E19 | Blood Collection | Specimen Handling | Thermal label printer | Zebra ZD420 or equivalent | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Priced | A$350 |
| E20 | Blood Collection | Pathology Equipment | Pathology collection equipment (vacutainers, needles, tourniquets, alcohol swabs, gauze, tape) | GTT-specific (fluoride-oxalate tubes for GTT tubes) | Ongoing | lot | WDP-DEPENDENT | Yes | Yes | WDP | NATA Licensed Collection Centre umbrella | No | No | Yes, largely supplied under WDP's accreditation, not general retail | No | Open | **Do not invent pathology equipment WDP would supply beyond what current documentation establishes; final split confirmed once WDP's commercial arrangement is settled** |
| E21 | Blood Collection | Glucose Drink | 75g glucose solution (Polycal or equivalent) | Commercially prepared, NOT home-made, one bottle per client, refrigerated | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pathology-grade product | No | Yes | Possibly WDP-supplied, confirm | No | Open | Administered by the phlebotomist as part of the collection workflow, not a separate cafe/snack item |

### E4. PPE, Hand Hygiene, Cleaning/Disinfection

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E22 | Blood Collection | PPE | Disposable gloves (nitrile) | Powder-free | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | AU | AS/NZS 4179/4011 | No | Yes | No | No | Open | |
| E23 | Blood Collection | PPE | Face masks (surgical) | For phlebotomist use where clinically indicated | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | HY | AS 4381 | Yes | Either | No | No | Open | |
| E24 | Blood Collection | Hand Hygiene | Clinical sink + elbow/sensor tap fitout | Elbow-operated or sensor tap, stainless/tiled splashback | 1 | each | SITE-DEPENDENT | No | No | SITE | NSQHS Standards | No | Yes | No | Yes | Open | **Australian hydraulic verification required, local trade install** |
| E25 | Blood Collection | Hand Hygiene | Alcohol-based hand rub (ABHR) dispenser | Wall-mounted | 2 | each | LOCKED | No | No | AU | Infection control standard | No | Yes | No | No | Open | |
| E26 | Blood Collection | Hand Hygiene | Hand soap (clinical grade) | Dispenser refill | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Infection control standard | No | Yes | No | No | Open | |
| E27 | Blood Collection | Hand Hygiene | Paper towel (clinical) | Dispenser refill | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Infection control standard | No | Yes | No | No | Open | |
| E28 | Blood Collection | Cleaning | Surface disinfectant (hospital-grade) | TGA-listed disinfectant, effective against blood-borne pathogens | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | TGA listing | No | Yes | No | No | Open | Must be TGA-listed, not a generic household disinfectant |
| E29 | Blood Collection | Cleaning | Blood spill kit | N/A | 2 | each | LOCKED | Yes | Yes | AU | Infection control standard | No | Yes | No | No | Priced | A$80-120 each |
| E30 | Blood Collection | Cleaning | Disposable wipes (surface, clinical-grade) | N/A | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Infection control standard | No | Yes | No | No | Open | |

### E5. Privacy, Curtains, Walls/Partitions, Signage, Emergency

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E31 | Blood Collection | Construction | Solid walls, one door, no public-facing window | Room construction, not a shippable product | 1 | room | LOCKED | No | No | SITE | Building surveyor, WA construction standard | No | Yes | No | Yes | Open | Built and serviced for 3 chairs from day one (Fit-Out Program Decision Analysis, Round 3) |
| E32 | Blood Collection | Privacy | Per-chair curtain/partition between the up-to-3 chair positions | Washable curtain fabric | 2-3 | each | CALCULATED | No | No | HY | Infection control (washable fabric) | Possible | Either | No | Yes | Open | Matches the recommended growth-first 3-chair-ready design |
| E33 | Blood Collection | Signage | Biohazard symbol (room door) | AS/NZS signage standard | 1 | each | LOCKED | No | No | AU | AS/NZS signage standard | No | Yes | No | No | Open | |
| E34 | Blood Collection | Signage | Hand hygiene reminder signage | At sink | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Open | |
| E35 | Blood Collection | Signage | "No entry when in use" signage | Door-mounted | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Open | |
| E36 | Blood Collection | Emergency | Emergency call button/intercom to reception | Wired circuit | 1 | each | SITE-DEPENDENT | No | No | AU | Electrical, WorkSafe | No | Yes | No | Yes | Open | Local trade install |
| E37 | Blood Collection | Emergency | AED (venue-wide, not room-specific) | See Section R | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference Section R, not double-counted here |
| E38 | Blood Collection | Ventilation | Room ventilation | 6 ACH per current spec | 1 | system | PROFESSIONAL-VERIFICATION | No | No | SITE | Australian HVAC verification required | No | Yes | No | Yes | Open | Site-specific, local HVAC contractor |
| E39 | Blood Collection | Staff Equipment | Phlebotomist uniform/scrubs | Per staff position register (PHL01-PHL04) | 4 (employment pool) | set | STAFF-DEPENDENT | No | No | HY | None | Possible | Either | No | No | Open | 2 committed + 2 relief pool |
| E40 | Blood Collection | Documentation | Collection log, specimen dispatch log, adverse event register (printed forms) | 7-year retention requirement | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Patient record-keeping requirement | No | Yes | No | No | Open | |

**Not invented: an internal "phlebotomy supervisor" clinical escalation role or equipment for one.** Escalation beyond the second on-site phlebotomist is a genuine, disclosed dependency on WDP's own Licensed Collection Centre protocol, not resolved by procurement.

---

## F. Massage

**Current model:** 3 stations (2 day-one + 1 growth reservation), curtain-partitioned, not stud-wall. Table-vs-chair format is a genuine, unresolved founder decision (`docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §6), not silently resolved here. Both options' procurement implications are shown.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01a | Massage | Furniture (OPTION A: table/bed) | Pregnancy massage table | Face hole + side cutouts, vinyl | 2 (day-one), up to 3 (growth) | each | CALCULATED | No | No | HY | General consumer product safety | Possible, mandatory AU reference unit | Hybrid | No | No | Priced | A$800-2,500 AU / A$300-800 China-sourced |
| F01b | Massage | Furniture (OPTION B: chair-based) | Massage station chair | Format and spec not previously modelled anywhere in this repository | Qty TBC if adopted | each | FOUNDER-DECISION | No | No | Open | None established | Unknown | Unknown | No | No | Open | **Genuinely unlocked, no existing spec: if Anthony adopts chair-based format, this line requires fresh research before quoting** |
| F02 | Massage | Equipment | Bolster/positioning pillow set | N/A | 2-3 sets | set | CALCULATED | No | No | HY | None | Possible | Either | No | No | Priced | A$80-150/set |
| F03 | Massage | Linen | Heated blanket | Electric, machine-washable | 4 | each | CALCULATED | No | No | HY | Electrical safety mark | Possible | Either | No | No | Priced | A$80-150 each, 2 per room including wash rotation |
| F04 | Massage | Equipment | Massage oil warming unit | Optional comfort upgrade | 2-3 | each | OPTIONAL | No | No | HY | Electrical safety mark | Possible | Either | No | No | Priced | A$50-100 each |
| F05 | Massage | Storage | Trolley/tool cart | N/A | 2-3 | each | CALCULATED | No | No | HY | None | Possible | Either | No | No | Open | Category A, China candidate |
| F06 | Massage | Linen | Massage table linen (sheets, pillowcases) | Machine-washable | 2 sets per station minimum | set | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| F07 | Massage | Consumables | Pregnancy-safe massage oil | Lavender, mandarin, chamomile only | 5L bulk | litre | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe formulation | No | Yes | No | No | Priced | A$25-50/L |
| F08 | Massage | Consumables | Aromatherapy/hamper items | Opening stock | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Pregnancy-safe formulation | Possible | Either | No | No | Open | |
| F09 | Massage | Privacy | Curtain partition per treatment room | Washable fabric, matches locked palette | 3 (day-one 2 + growth 1) | each | CALCULATED | No | No | HY | Infection control (washable fabric) | Possible | Either | No | No | Open | Fit-out cost, not equipment |
| F10 | Massage | Lighting | Task/ambient lighting per station | Warm, dimmable | 2-3 | each | CALCULATED | No | No | HY | Electrical safety, professional lighting design | Possible | Either | No | No | Open | See Section X |
| F11 | Massage | PPE | Disposable table-roll paper or equivalent barrier | N/A | Ongoing | roll | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Infection control | Possible | Either | No | No | Open | |
| F12 | Massage | Practitioner Equipment | Practitioner apron/uniform | Per position register (MB01-MB06) | 6 (employment pool) | set | STAFF-DEPENDENT | No | No | HY | None | Possible | Either | No | No | Open | 4 committed + 2 relief pool |

---

## G. Beauty

**Current model:** 3 stations (2 day-one + 1 growth reservation, recommended, matching Massage, pending Anthony's final sign-off, `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` Round 3). Services provided: pregnancy-safe facials, brow/lash work. Facial steamer only if deeper facials are offered (service-dependent, not yet confirmed as a locked service).

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G01 | Beauty | Furniture | Facial/beauty treatment bed | Electric, adjustable, vinyl | 2 (day-one), up to 3 (growth, recommended) | each | CALCULATED | No | No | HY | SAA electrical mark (recline mechanism) | Possible | Either | No | No | Priced | A$400-900 each |
| G02 | Beauty | Furniture | Practitioner stool | Adjustable height | 2-3 | each | CALCULATED | No | No | HY | None | Possible | Either | No | No | Open | |
| G03 | Beauty | Lighting | Magnifying lamp (LED, adjustable) | N/A | 2-3 | each | CALCULATED | No | No | HY | SAA electrical mark | Possible | Either | No | No | Priced | A$80-150 each |
| G04 | Beauty | Equipment | Wax heater (dual-pot, professional) | N/A | 1 | each | LOCKED | No | No | HY | SAA electrical mark | Possible | Either | No | No | Priced | A$120-250 |
| G05 | Beauty | Equipment | Brow/lash tool kit | Tweezers, brushes, applicators | 2-3 sets | set | CALCULATED | No | No | HY | None | Possible | Either | No | No | Priced | A$60-120/set |
| G06 | Beauty | Equipment | Facial steamer | Only if deeper facials are offered | 0-1 | each | FOUNDER-DECISION | No | No | HY | SAA electrical mark | Possible | Either | No | No | Priced | A$150-350, service-dependent, not confirmed as locked |
| G07 | Beauty | Storage | Trolley/tool cart | N/A | 2-3 | each | CALCULATED | No | No | HY | None | Possible | Either | No | No | Priced | A$100-200 each |
| G08 | Beauty | Hygiene | 2-sink fitout (hand-wash + instrument decontamination) | Hands-free tap on hand-wash sink | 1-2 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | WA Skin Penetration Code (researched this round: waxing, tweezing, and electrolysis are within the Code's scope; a hands-free handwash basin with hot/cold water, soap, and paper towel is required in the immediate treatment area, per the Code of Practice for Skin Penetration Procedures 1998) | No | Yes | No | Yes | Open | Local hydraulic trade install |
| G09 | Beauty | Linen | Treatment bed linen (disposable or machine-washable) | N/A | 2 sets per station minimum | set | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Infection control | Possible | Either | No | No | Open | |
| G10 | Beauty | Consumables | PPD-free brow tint | Pregnancy-safe | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe, PPD-free | No | Yes | No | No | Priced | A$150-250 |
| G11 | Beauty | Consumables | Wax (strip + hard, pregnancy-safe) | N/A | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe | No | Yes | No | No | Priced | A$100-200 |
| G12 | Beauty | Consumables | Facial products (HA serum, niacinamide, pregnancy-safe masks) | N/A | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe formulation | No | Yes | No | No | Priced | A$300-600 |
| G13 | Beauty | Disposables | Disposable brow/wax consumables | Spatulas, strips, patch-test kits | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Infection control | Possible | Either | No | No | Priced | A$100-200 |
| G14 | Beauty | Electrical | Standard GPO, task lighting per station | N/A | 2-3 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed electrician | No | Yes | No | Yes | Open | |
| G15 | Beauty | Practitioner Equipment | Practitioner uniform | Per position register | Staff-dependent | set | STAFF-DEPENDENT | No | No | HY | None | Possible | Either | No | No | Open | Shared with Massage where dual-qualified (MB01-MB06) |

**Not invented: services not currently offered.** No spray tan, no service beyond facials/brow/lash currently confirmed in the service catalogue is procured for here.

---

## H. Nail

**Current model:** 4 nail stations, open-plan, LEV extraction mandatory.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H01 | Nail | Furniture | Nail table with built-in dust collector | Professional grade | 4 | each | LOCKED | No | No | HY | Electrical safety mark (built-in collector) | Possible | Either | No | No | Priced | A$500-800 each |
| H02 | Nail | Furniture | Nail technician chair | Adjustable | 4 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |
| H03 | Nail | Furniture | Client manicure chair | N/A | 4 | each | LOCKED | No | No | HY | AS/NZS 4088 general seating standard | Possible | Either | No | No | Priced | A$200-400 each |
| H04 | Nail | Equipment | UV/LED nail lamp | Professional grade | 4 | each | LOCKED | No | No | HY | SAA electrical mark | Possible | Either | No | No | Priced | A$100-200 each |
| H05 | Nail | Equipment | Nail drill | Professional grade | 2-4 | each | STAFF-DEPENDENT | No | No | HY | SAA electrical mark | Possible | Either | No | No | Open | Not itemised in prior source documents; genuine gap now flagged and filled |
| H06 | Nail | Ventilation | LEV (local exhaust ventilation) unit | Sized for 4 stations, installed | 1 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | WorkSafe WA pre-application; researched this round: LEV/downdraft capture-hood systems are the standard method for open-plan nail-station air-quality compliance, but no WorkSafe-WA-familiar contractor has been identified for this specific installation | No | Yes, local install regardless of unit origin | No | Yes | Priced | A$1,500-4,000 installed; **genuine gap: no contractor identified yet** |
| H07 | Nail | Storage | Nail tool trolley | N/A | 4 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Priced | A$150-300 each |
| H08 | Nail | Consumables | Nail files | N/A | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| H09 | Nail | Consumables | Buffing blocks | N/A | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| H10 | Nail | Consumables | Cuticle pushers | N/A | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| H11 | Nail | Consumables | Cuticle nippers | N/A | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| H12 | Nail | Consumables | Base coat | 9-free formula | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Product safety, 9-free formulation | Possible | Either | No | No | Priced | Part of A$830-1,480 combined opening stock |
| H13 | Nail | Consumables | Top coat | 9-free formula | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Product safety | Possible | Either | No | No | Open | |
| H14 | Nail | Consumables | Gel polish | 20+ colours, 9-free formula | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Product safety | Possible | Either | No | No | Priced | A$15-25 each, 20 colours = A$300-500 |
| H15 | Nail | Consumables | Regular (non-gel) polish | 20+ colours | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | CN | Product safety | Yes | Yes | No | No | Priced | A$8-15 each |
| H16 | Nail | Consumables | Remover/acetone | N/A | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Flammable-liquid storage standard | No | Yes | No | No | Open | |
| H17 | Nail | Disposables | Lint-free wipes | N/A | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| H18 | Nail | PPE | Disposable gloves | Food/beauty-grade | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Product safety | Possible | Either | No | No | Open | |
| H19 | Nail | PPE | Nail dust masks (N95) | Box of 50 | 2 boxes | box | CONSUMPTION-DEPENDENT | Yes | Yes | AU | AS/NZS respiratory protection standard | No | Yes | No | No | Priced | A$25-40/box |
| H20 | Nail | Cleaning | Disinfection solution + containers | Instrument disinfection | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Infection control standard | No | Yes | No | No | Priced | A$80-150 |
| H21 | Nail | Electrical | GPO per station (2x 10A) | N/A | 4 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed electrician | No | Yes | No | Yes | Open | |

**Note: French gel manicure = 45 minutes in the AM/GTT window (Chapter 10); available as a standalone PM service too, per current model. No additional procurement implication beyond the items above.**

---

## I. Pedicure

**Current model:** 4 pedicure chairs, same zone as the 4 nail stations, not an additional 8-station expansion.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I01 | Pedicure | Furniture/Equipment | Pedicure spa chair (pipeless) | Pipeless/no-jet design mandatory for hygiene | 4 (same zone as Nail, not an additional 8) | each | LOCKED | No | No | CN | CE/SAA electrical mark, pipeless design confirmed | Yes, highest-confidence quantified saving in this whole schedule | Also available | No | No | Priced | A$800-2,000 AU / A$500-1,500 China-sourced |
| I02 | Pedicure | Plumbing | Chair plumbing (hot/cold water, drainage) | Per chair | 4 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed plumber | No | Yes | No | Yes | Open | |
| I03 | Pedicure | Consumables | Foot files/pumice | N/A | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| I04 | Pedicure | Consumables | Foot towels | Machine-washable | 8-12 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| I05 | Pedicure | Consumables | Toe separators (disposable) | N/A | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | CN | Product safety | Yes | Yes | No | No | Open | |
| I06 | Pedicure | Cleaning | Pipeless chair sanitation kit | Disinfectant compatible with the pipeless system's specific hygiene design | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Manufacturer-specified sanitation compliance | Possible | Either | No | No | Open | Must match the specific chair's own sanitation system |

**Not additional: gel manicure/pedicure = 45-minute AM/GTT-window service, available as standalone PM service too. No spray tan reintroduced anywhere in this section.**

---

## J. Hair

**Current model:** 4 hairdresser stations, deliberately allowing hairdressers to work behind chairs without requiring an unnecessarily large room. No colour service currently confirmed beyond what the service catalogue states (Chapter 10 confirms colour services exist in the catalogue at PM/standalone level; colour equipment procured accordingly).

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J01 | Hair | Furniture | Styling chair (hydraulic, wipe-clean) | Professional grade | 4 | each | LOCKED | No | No | HY | AS/NZS 4088 | Possible | Either | No | No | Priced | A$500-1,200 each |
| J02 | Hair | Furniture | Salon mirror (lighted, full-length) | Custom-fit to actual wall length, spans 4 chairs | 1 | each | SITE-DEPENDENT | No | No | HY | SAA electrical mark for the LED strip | Possible | Either | No | Yes | Priced | A$200-500 |
| J03 | Hair | Equipment | Professional hair dryer | Named brand (Dyson, GHD, or equivalent) | 4 | each | LOCKED | No | No | AU | SAA electrical mark | No, poor import candidate on warranty grounds | Yes, direct trade account | No | No | Priced | A$250-500 each |
| J04 | Hair | Equipment | Straightening iron | Named brand (GHD, Cloud Nine, or equivalent) | 4 | each | LOCKED | No | No | AU | SAA electrical mark | No, same reasoning as J03 | Yes | No | No | Priced | A$150-300 each |
| J05 | Hair | Equipment | Curling tools | Professional grade | 2-4 | each | STAFF-DEPENDENT | No | No | AU | SAA electrical mark | No | Yes | No | No | Open | Genuine gap not itemised in prior source documents, now filled |
| J06 | Hair | Equipment | Hair clippers | If offered as a service | 0-2 | each | FOUNDER-DECISION | No | No | AU | SAA electrical mark | No | Yes | No | No | Open | Confirm against the current service catalogue before purchasing |
| J07 | Hair | Tools | Brushes/combs | Professional grade, various | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| J08 | Hair | Linen | Capes | Wipe-clean, machine-washable | 8-12 | each | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| J09 | Hair | Linen | Towels (hair-specific) | N/A | 12-20 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| J10 | Hair | Consumables | Shampoo | Pregnancy-safe (no harsh chemicals) | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe formulation | No | Yes | No | No | Open | |
| J11 | Hair | Consumables | Conditioner | Pregnancy-safe | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe formulation | No | Yes | No | No | Open | |
| J12 | Hair | Consumables | Treatment products | Pregnancy-safe | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe formulation | No | Yes | No | No | Priced | Part of A$350-650 combined opening stock |
| J13 | Hair | Consumables | Styling products (mousse, spray, serum) | Pregnancy-safe | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Pregnancy-safe formulation | No | Yes | No | No | Open | |
| J14 | Hair | Colour Equipment | Colour bowls, brushes, foils, capes | Only if the current service model includes colour services | 1 lot | lot | FOUNDER-DECISION | Yes | Yes | HY | Product safety | Possible | Either | No | No | Open | Confirm against the current service catalogue (Chapter 10) before purchasing |
| J15 | Hair | Storage | Tool trolley + organiser | N/A | 4 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Priced | A$150-300 each |
| J16 | Hair | Waste | Hair waste bin | Lidded | 1-2 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| J17 | Hair | PPE | Disposable gloves | N/A | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Product safety | Possible | Either | No | No | Open | |
| J18 | Hair | Electrical | GPO nearby each chair | N/A | 4 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed electrician | No | Yes | No | Yes | Open | |

---

## K. Hair Wash

**Current model:** 2 hair wash stations.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K01 | Hair Wash | Equipment | Backwash basin + client chair | Plumbed hot/cold, neck rest | 2 (day-one), 3rd optional | each | LOCKED (2), OPTIONAL (3rd) | No | No | HY | Electrical (if electric recline) | Possible | Either | No | Yes | Priced | A$1,000-2,500 each; +A$1,000-2,500 if 3rd added |
| K02 | Hair Wash | Plumbing | Hot water supply, drainage per basin | N/A | 2 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed plumber | No | Yes | No | Yes | Open | |
| K03 | Hair Wash | Linen | Towels (hair-wash-specific) | N/A | 8-12 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| K04 | Hair Wash | Hot Water | Hot water system capacity | N/A | 1 | system | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed plumber, hot-water system sizing | No | Yes | No | Yes | Open | Venue-dependent, verify against existing plant |

---

## L. Staff Area

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L01 | Staff Area | Furniture | Lockers | Per employed headcount | Not itemised at unit level yet | each | STAFF-DEPENDENT | No | No | HY | None | Possible | Either | No | No | Open | Genuine gap: no unit count/price researched yet; calculate against the full employment pool (VM01, PHL01-04, MB01-06, NAIL01-03, HAIR01-03, PMM01/PMB01/PMN01/PMH01) once final pool sizes are confirmed |
| L02 | Staff Area | Furniture | Staff table | Break facilities | 1 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |
| L03 | Staff Area | Equipment | Kettle | Break facilities | 1 | each | LOCKED | No | No | CN | Electrical safety mark | Yes | Yes | No | No | Open | |
| L04 | Staff Area | Plumbing | Staff sink | Break facilities | 1 | each | PROFESSIONAL-VERIFICATION | No | No | SITE | Licensed plumber | No | Yes | No | Yes | Open | |
| L05 | Staff Area | Furniture | Chairs (staff break) | N/A | 4-6 | each | STAFF-DEPENDENT | No | No | HY | None | Possible | Either | No | No | Open | |
| L06 | Staff Area | Amenity | Small fridge (staff use) | N/A | 1 | each | LOCKED | No | No | HY | Electrical safety mark | Possible | Either | No | No | Open | Separate from the Cafe's client-facing fridges |
| L07 | Staff Area | Amenity | Microwave (staff use) | N/A | 1 | each | LOCKED | No | No | HY | Electrical safety mark | Possible | Either | No | No | Open | |

---

## M. Storage

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M01 | Storage | BOH | Clean linen storage shelving/cabinet | Lockable consumable cabinet | 1 | each | LOCKED | No | No | CN | None | Yes, strong candidate, non-client-facing | Also available | No | No | Open | |
| M02 | Storage | BOH | Dirty linen/biohazard storage | Separate from clean linen | 1 | each | LOCKED | No | No | HY | Clinical waste handling standard | Possible | Either | No | No | Open | |
| M03 | Storage | BOH | General retail/product storage shelving | N/A | 1-2 | each | SITE-DEPENDENT | No | No | CN | None | Yes | Yes | No | Yes | Open | |
| M04 | Storage | BOH | Consumables stockroom shelving (nail/hair/beauty products) | N/A | 1 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |

---

## N. Toilets

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N01 | Toilets | Consumables | Toilet paper | Commercial-grade, per toilet count | To be determined | roll | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | Yes | Open | Quantity depends on final toilet count (patient WC accessible, patient WC standard, staff WC per the venue program) |
| N02 | Toilets | Consumables | Paper towel (hand-drying) | N/A | To be determined | box | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | Yes | Open | |
| N03 | Toilets | Consumables | Hand soap | Dispenser refill | To be determined | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | Yes | Open | |
| N04 | Toilets | Fixtures | Soap dispenser | Wall-mounted | Per toilet count | each | SITE-DEPENDENT | No | No | HY | None | Possible | Either | No | Yes | Open | |
| N05 | Toilets | Fixtures | Paper towel dispenser | Wall-mounted | Per toilet count | each | SITE-DEPENDENT | No | No | HY | None | Possible | Either | No | Yes | Open | |
| N06 | Toilets | Fixtures | Sanitary disposal unit | N/A | Per toilet count | each | SITE-DEPENDENT | No | No | AU | Waste-management standard | No | Yes | No | Yes | Open | |
| N07 | Toilets | Consumables | Sanitary products (complimentary) | If offered as a client amenity | Optional | lot | OPTIONAL | Yes | Yes | AU | None | No | Yes | No | No | Open | Genuine amenity decision, not confirmed either way |
| N08 | Toilets | Fixtures | Hand dryer (if selected instead of paper towel) | N/A | Per toilet count | each | FOUNDER-DECISION | No | No | AU | Electrical safety mark | No | Yes | No | Yes | Open | Paper towel vs hand dryer not yet decided |
| N09 | Toilets | Waste | Bin (general) | Lidded | Per toilet count | each | SITE-DEPENDENT | No | No | CN | None | Yes | Yes | No | Yes | Open | |
| N10 | Toilets | Cleaning | Toilet brush | N/A | Per toilet count | each | SITE-DEPENDENT | No | No | CN | None | Yes | Yes | No | Yes | Open | |
| N11 | Toilets | Cleaning | Plunger | N/A | 1-2 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| N12 | Toilets | Ambience | Air freshener (if appropriate to the brand) | Subtle, unscented preferred given pregnancy sensitivity | Optional | each | OPTIONAL | Yes | Yes | AU | None | No | Yes | No | No | Open | Scent sensitivity in pregnancy is a real consideration; not confirmed either way |
| N13 | Toilets | Accessibility | Accessibility grab rails, accessible WC fittings | AS 1428.1 | Per accessible toilet | each | PROFESSIONAL-VERIFICATION | No | No | SITE | AS 1428.1 accessibility clearances | No | Yes | No | Yes | Open | **Australian accessibility verification required** |
| N14 | Toilets | Signage | Toilet signage (including accessibility symbol) | N/A | Per toilet count | each | SITE-DEPENDENT | No | No | AU | AS 1428.1 signage requirement | No | Yes | No | Yes | Open | |
| N15 | Toilets | Cleaning | Cleaning chemicals (bathroom-specific) | See Section O for the full cleaning inventory | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference Section O, not double-counted here | |
| N16 | Toilets | Consumables | Spare stock (toilet paper, soap, paper towel reserve) | N/A | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | Quantity to be determined from opening-stock policy/supplier recommendation |

---

## O. Cleaning / Housekeeping

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| O01 | Cleaning | General | Commercial vacuum | N/A | 1-2 | each | LOCKED | No | No | HY | Electrical safety mark | Possible | Either | No | No | Open | |
| O02 | Cleaning | General | Mop system (bucket + wringer) | N/A | 2 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | One general, one clinical, kept separate |
| O03 | Cleaning | General | Buckets | N/A | 2-4 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| O04 | Cleaning | General | Dustpans/brooms | N/A | 2-3 sets | set | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| O05 | Cleaning | General | Microfibre cloths | Colour-coded by area (clinical vs general) | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | Infection control colour-coding standard | Yes | Yes | No | No | Open | |
| O06 | Cleaning | General | General-purpose disinfectant | Non-clinical areas (Lounge, Reception, BOH) | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | Kept separate from the clinical-grade disinfectant in Section E |
| O07 | Cleaning | Bathroom | Bathroom cleaner | N/A | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| O08 | Cleaning | General | Glass cleaner | N/A | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| O09 | Cleaning | General | Floor cleaner | Appropriate to the venue's actual flooring once confirmed | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| O10 | Cleaning | Waste | Bin liners (general) | Various sizes per bin type | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| O11 | Cleaning | Clinical | Clinical-grade cleaning products (TGA-listed) | Kept entirely separate from general cleaning products, see Section E for the full clinical list | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference Section E4, not double-counted here | |
| O12 | Cleaning | PPE | Cleaning gloves (heavy-duty) | N/A | Ongoing | pair | CONSUMPTION-DEPENDENT | Yes | Yes | CN | None | Yes | Yes | No | No | Open | |
| O13 | Cleaning | Equipment | Cleaning caddies | For staff to carry supplies between rooms | 2-3 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| O14 | Cleaning | Signage | Wet floor warning signs | N/A | 2-3 | each | LOCKED | No | No | CN | AS/NZS signage standard | Yes | Yes | No | No | Open | |
| O15 | Cleaning | Consumables | Paper products (general-area hand towel, tissues) | N/A | Ongoing | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| O16 | Cleaning | Emergency | Spill kit (general, non-biohazard) | N/A | 1-2 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Open | Separate from the clinical blood spill kit in Section E |
| O17 | Cleaning | Storage | Cleaning products storage (lockable) | Separate from clinical and general retail stock | 1 | each | LOCKED | No | No | HY | Chemical storage safety standard | Possible | Either | No | No | Open | |

---

## P. Laundry

**Current model:** researched against current source documents; no in-house commercial washer/dryer is confirmed as decided anywhere in this repository, and no outsourced laundry contract is confirmed either. This is a genuine, disclosed gap, not invented here.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Laundry | Linen | Towels (general/hand) | N/A | 20-30 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| P02 | Laundry | Linen | Face towels | N/A | 12-20 | each | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| P03 | Laundry | Linen | Massage/treatment linen | See Section F06/G09 for room-specific quantities, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference F/G, not double-counted | |
| P04 | Laundry | Linen | Hair towels | See Section J09/K03 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference J/K, not double-counted | |
| P05 | Laundry | Linen | Pedicure/foot towels | See Section I04 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference I, not double-counted | |
| P06 | Laundry | Equipment | Laundry bags/hampers | Segregated clean vs dirty | 4-6 | each | LOCKED | No | No | HY | Clinical/general segregation standard | Possible | Either | No | No | Open | |
| P07 | Laundry | Consumables | Detergent | N/A | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | Model (in-house wash vs outsourced) not yet decided |
| P08 | Laundry | Consumables | Stain remover | N/A | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| P09 | Laundry | Consumables | Disinfecting laundry additive (for clinical/treatment linen) | N/A | Ongoing | bottle | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Infection control standard | No | Yes | No | No | Open | |
| P10 | Laundry | Equipment | Commercial washer/dryer | Only if in-house laundry model is adopted | 0-2 | each | FOUNDER-DECISION | No | No | AU | Electrical/plumbing, commercial appliance standard | No | Yes | No | Yes | Open | **Genuine, unresolved: in-house vs outsourced laundry model not confirmed anywhere in this repository, not invented here** |
| P11 | Laundry | Service | Outsourced commercial laundry contract | Only if outsourced model is adopted | 0-1 | contract | FOUNDER-DECISION | No | Yes | AU | None | No | Yes | No | No | Open | Alternative to P10, mutually exclusive |

---

## Q. Clinical Consumables (Venue-Wide, Beyond Blood Collection)

**Note:** the core clinical consumables specific to venepuncture are itemised in full in Section E. This section covers clinical-adjacent consumables not specific to the Blood Collection Room itself.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q01 | Clinical Consumables | Venue-wide | Consent/intake forms (printed) | N/A | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | Privacy Act, patient record-keeping | No | Yes | No | No | Priced | A$150-250 |
| Q02 | Clinical Consumables | Venue-wide | Referral cards (printed) | For referring practices | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| Q03 | Clinical Consumables | Venue-wide | Digital thermometer (general use, non-cold-chain) | For any general first-aid need | 1-2 | each | LOCKED | No | No | HY | None | Possible | Either | No | No | Open | |

---

## R. First Aid / CPR / Emergency

**Protected: no reduction.** All staff receive first aid/CPR training with explicit emphasis on incidents associated with blood collection (fainting, vasovagal response, bleeding, bruising, difficult venepuncture complications, client distress), not a generic first aid course, per `docs/architecture/STAFF-PROFILES-COMPLETE.md`. Exact accredited-course requirement (HLTAID011 Provide First Aid or equivalent) still needs direct confirmation from a registered training organisation before being written into an employment contract.

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | First Aid | Venue-wide | AED (Automated External Defibrillator) | ARTG-registered | 1 | each | LOCKED | No | No | PRO | ARTG registration mandatory | No | Yes, named brands (HeartSine, Zoll, Philips) | No | No | Open | Leasing option exists, ~A$40-60/month; purchase vs lease not yet compared |
| R02 | First Aid | Venue-wide | First aid kit (comprehensive) | WorkSafe-compliant | 2 | each | LOCKED | Yes | Yes | AU | WorkSafe-compliant | No | Yes | No | No | Priced | A$100-200 each |
| R03 | First Aid | Venue-wide | Panic buttons | Wired circuit to reception | Per current room count | each | SITE-DEPENDENT | No | No | AU | WorkSafe-compliant, electrical | No | Yes | No | Yes | Open | |
| R04 | First Aid | Venue-wide | Emergency exit signage | See Section A02, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference A, not double-counted | |
| R05 | First Aid | Blood Collection | Blood spill kit | See Section E29, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference E, not double-counted | |
| R06 | First Aid | Training | First Aid/CPR accredited course (per staff member) | HLTAID011 Provide First Aid or equivalent, emphasis on venepuncture-related incidents | Full employment pool | course | STAFF-DEPENDENT | No | Yes, renewal cycle | AU | Registered training organisation, exact course requirement to be confirmed | No | Yes | No | No | Open | Not a physical purchase, a training/service line; recurring renewal cost |
| R07 | First Aid | Emergency | EpiPen (anaphylaxis) | Held by the Venue Manager, trained first aider | 1-2 | each | LOCKED | Yes | Yes, expiry-driven | AU | TGA-registered, prescription item | No | Yes | No | No | Open | Expiry-driven reorder, not a standard consumable |

---

## S. PPE / Infection Control (Venue-Wide Summary)

**This section cross-references, does not duplicate, the PPE items already itemised in Sections E (Blood Collection), G (Beauty), H (Nail), J (Hair), and C (Cafe).**

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | PPE | Venue-wide | Disposable gloves (general, non-clinical, non-nail) | For general cleaning/housekeeping use | Ongoing | box | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | Distinct from the clinical-grade gloves in Section E |
| S02 | PPE | Venue-wide | Hand sanitiser (public-facing, Reception/Lounge/Cafe) | Alcohol-based | 3-4 dispensers | each | LOCKED | Yes | Yes | AU | None | No | Yes | No | No | Open | |

---

## T. IT / Technology (Venue-Wide)

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes | Required at Opening / Optional / Future |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | IT | Venue-wide | WiFi router (commercial grade) | Ubiquiti/TP-Link business range | 1 | each | LOCKED | No | No | AU | None | No | Yes | No | No | Priced | A$200-500 | Required at Opening |
| T02 | IT | Venue-wide | Network switches | To distribute wired connections | 1-2 | each | SITE-DEPENDENT | No | No | AU | None | No | Yes | No | Yes | Open | | Required at Opening |
| T03 | IT | Venue-wide | Access points (WiFi coverage across the full floor plate) | N/A | 1-2 | each | SITE-DEPENDENT | No | No | AU | None | No | Yes | No | Yes | Open | | Required at Opening |
| T04 | IT | Venue-wide | Cabling (Cat6) | See Section A06, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference A, not double-counted | | |
| T05 | IT | Reception | Computer/laptop | See Section B03, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference B, not double-counted | | |
| T06 | IT | Reception/Lounge | Charging stations | See Sections B17/D02 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference B/D, not double-counted | | |
| T07 | IT | Lounge | Tablet mounts | See Section D06 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference D, not double-counted | | |
| T08 | IT | Venue-wide | Security cameras | Optional, not yet confirmed as required | 0-4 | each | OPTIONAL | No | No | HY | Privacy Act, CCTV signage requirement | Possible | Either | No | No | Open | | Optional |
| T09 | IT | Venue-wide | Access control (e.g. keypad/fob entry) | Optional | 0-1 | system | OPTIONAL | No | No | AU | None | No | Yes | No | Yes | Open | | Optional |
| T10 | IT | Venue-wide | UPS (uninterruptible power supply) | For POS/booking system continuity during a power blip | 1 | each | OPTIONAL | No | No | AU | Electrical safety mark | No | Yes | No | No | Open | | Optional |
| T11 | IT | Venue-wide | Backup device/cloud backup subscription | For Fresha/patient data | 1 | subscription | LOCKED | No | Yes | AU | Privacy Act data-retention requirement | No | Yes | No | No | Open | | Required at Opening |
| T12 | IT | Reception | Phone/VoIP system | See Section B06 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference B, not double-counted | | |
| T13 | IT | Venue-wide | Small TV/display | Optional (Lounge, see Section D12 future-use note) | 0-1 | each | OPTIONAL | No | No | HY | Electrical safety mark | Possible | Either | No | No | Open | | Optional/Future |

---

## U. POS / Booking / Admin (Cross-Referenced)

All POS, booking, and admin equipment is itemised under Reception (Section B) and Cafe (Section C18, which explicitly shares Reception's POS, not a separate purchase). This section exists per the requested category structure but does not duplicate those line items.

---

## V. Security

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V01 | Security | Venue-wide | Security cameras | See Section T08, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference T, not double-counted | |
| V02 | Security | Venue-wide | Access control | See Section T09, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference T, not double-counted | |
| V03 | Security | Venue-wide | Alarm system | Optional, not yet confirmed | 0-1 | system | OPTIONAL | No | No | AU | None | No | Yes | No | Yes | Open | |
| V04 | Security | Blood Collection | Lockable medical consumables cabinet | See Section E07, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference E, not double-counted | |
| V05 | Security | Reception | Lockable filing storage | See Section B16, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference B, not double-counted | |

---

## W. Signage / Branding

**Uses the locked brand direction: warm, natural, earthy, calm premium/luxury positioning, current approved 7-colour palette (`outputs/brand/warm-stone-tokens.css`). No new brand colours invented here.**

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W01 | Branding | External | External signage (business name/logo) | Design-dependent, gated on final naming decision | 1 | each | FOUNDER-DECISION | No | No | HY | Local council signage permit | Possible | Either | No | Yes | Open | Cannot be finalised until SOLENA/ELOWEN is decided |
| W02 | Branding | Internal | Internal wayfinding signage | Per venue layout | 1 lot | lot | SITE-DEPENDENT | No | No | HY | None | Possible | Either | No | Yes | Open | |
| W03 | Branding | Cafe | Menu | See Section C17, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference C, not double-counted | |
| W04 | Branding | Venue-wide | Printed materials (brochures, referral cards) | See Q02 for referral cards specifically | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | AU | None | No | Yes | No | No | Open | |
| W05 | Branding | Staff | Uniforms | See Sections E39/F12/G15, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference E/F/G, not double-counted | |
| W06 | Branding | Staff | Name badges | Per employed headcount | Full employment pool | each | STAFF-DEPENDENT | No | No | HY | None | Possible | Either | No | No | Open | |
| W07 | Branding | Reception | Branded stationery | N/A | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | None | Possible | Either | No | No | Open | |
| W08 | Branding | Venue-wide | Decor/artwork | Warm, natural, earthy, matches the locked palette | 1 lot | lot | SITE-DEPENDENT | No | No | HY | None | Possible | Either | No | Yes | Open | |
| W09 | Branding | Venue-wide | Mirrors (decorative, beyond the functional Hair mirror in J02) | Optional | 0-2 | each | OPTIONAL | No | No | HY | None | Possible | Either | No | No | Open | |
| W10 | Branding | Venue-wide | Planters (if appropriate) | Optional, real or artificial plants matching the palette | 2-4 | each | OPTIONAL | No | No | CN | None | Yes | Yes | No | No | Open | |
| W11 | Branding | Venue-wide | Scent/ambience diffuser | Only if appropriate and safe given pregnancy scent-sensitivity | 0-1 | each | FOUNDER-DECISION | No | No | HY | Pregnancy-safe fragrance-free or low-scent formulation if adopted | Possible | Either | No | No | Open | Genuine, unresolved: not confirmed appropriate given pregnancy sensitivity |

---

## X. Lighting (Dedicated Section)

**No lux levels are fabricated below. Where Australian standards/professional lighting design are required, the verification requirement is identified, not a number invented.**

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X01 | Lighting | Reception | General ambient lighting | Warm, matches palette | Per venue layout | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Australian lighting designer/electrician | Possible | Either | No | Yes | Open | |
| X02 | Lighting | Cafe | Task + ambient lighting | Warm, food-safe fixture ratings where applicable | Per venue layout | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Australian lighting designer/electrician | Possible | Either | No | Yes | Open | |
| X03 | Lighting | Lounge | Ambient + floor lamps | See Section D04, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference D, not double-counted | |
| X04 | Lighting | Blood Collection | Clinical-standard lighting | Adequate for venepuncture precision work | Per room | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Australian clinical lighting standard, electrician | No | Yes | No | Yes | Open | |
| X05 | Lighting | Nail | Task lighting per station | See Section H (implied in station equipment), dedicated fixture if not built into the nail lamp | Per station | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X06 | Lighting | Pedicure | Task lighting per chair | N/A | Per chair | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X07 | Lighting | Massage | Task/ambient lighting per station | Warm, dimmable | Per station | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X08 | Lighting | Beauty | Magnifying/task lighting | See Section G03, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference G, not double-counted | |
| X09 | Lighting | Hair Styling | Mirror-integrated lighting | See Section J02, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference J, not double-counted | |
| X10 | Lighting | Hair Wash | General ambient lighting | N/A | Per venue layout | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X11 | Lighting | Toilets | General ambient lighting | N/A | Per toilet count | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X12 | Lighting | Staff Areas | General ambient lighting | N/A | Per venue layout | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X13 | Lighting | Storage | Basic utility lighting | N/A | Per venue layout | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Electrician | Possible | Either | No | Yes | Open | |
| X14 | Lighting | Venue-wide | Emergency lighting | Building-code compliant, exit-path illumination | Per venue layout | fixture | PROFESSIONAL-VERIFICATION | No | No | SITE | Building surveyor, AS 2293 | No | Yes | No | Yes | Open | |
| X15 | Lighting | Venue-wide | Feature/decorative lighting | Optional, brand-reinforcing | Optional | fixture | OPTIONAL | No | No | HY | Electrician | Possible | Either | No | No | Open | |
| X16 | Lighting | External | Signage lighting | Gated on naming decision | 1 | fixture | FOUNDER-DECISION | No | No | HY | Electrician, council signage permit | Possible | Either | No | Yes | Open | |

---

## Y. Furniture Register (Cross-Referenced Summary)

Every chair, table, cabinet, shelf, trolley, sofa, stool, desk, and bench above is individually itemised within its own functional area (Sections B through N). This section is a navigation aid, not a duplicate list: Reception (B01, B02), Cafe (C19, seating), Lounge (D01-D03), Blood Collection (E01-E06), Massage (F01a/b, F05), Beauty (G01, G02, G07), Nail (H01-H03, H07), Pedicure (I01), Hair (J01, J15), Hair Wash (K01), Staff Area (L01, L02, L05), Storage (M01-M04).

---

## Z. Decor / Client Experience

Covered under Branding (Section W) and Lounge (Section D). Not duplicated here.

---

## AA. Waste Management

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA01 | Waste | Blood Collection | Biohazard/clinical waste | See Sections E12/E13/E14, not double-counted here | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference E, not double-counted | |
| AA02 | Waste | Venue-wide | General waste bins | Per area, see individual sections | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference C21/D11/J16/N09, not double-counted | |
| AA03 | Waste | Venue-wide | General waste collection contract | Council or private contractor | 1 | contract | SITE-DEPENDENT | No | Yes | AU | Council waste-management requirement | No | Yes | No | Yes | Open | |
| AA04 | Waste | Cafe | Food waste/recycling separation | See Section C21 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Cross-reference C, not double-counted | |

---

## AB. Maintenance / Tooling

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AB01 | Maintenance | Venue-wide | Basic tool kit (screwdrivers, allen keys for furniture assembly/maintenance) | N/A | 1 | each | LOCKED | No | No | CN | None | Yes | Yes | No | No | Open | |
| AB02 | Maintenance | Venue-wide | Spare lightbulbs/fixtures | Matching the installed fixture types | 1 lot | lot | CONSUMPTION-DEPENDENT | Yes | Yes | HY | Electrical safety mark | Possible | Either | No | No | Open | |
| AB03 | Maintenance | Equipment | Equipment service/maintenance contracts (centrifuge, LEV units, coffee machine) | Manufacturer or third-party servicing | 3+ | contract | LOCKED | No | Yes | HY | Manufacturer warranty terms | Possible | Either | No | No | Open | |

---

## AC. Opening Stock / Consumables (Cross-Referenced Summary)

All opening-stock consumables are itemised within their own functional area throughout this document (marked "Opening Stock?: Yes" in each relevant row). This section exists as the requested category but is a navigation aid, not a duplicate register. See the Opening Day Checklist below for the practical, must-have-before-first-client view.

---

## AD. Backup / Replacement Stock

| ID | Category | Area | Item | Description / Specification | Quantity | Unit | Quantity Basis | Opening Stock? | Reorderable? | Sourcing | Compliance / Verification | China Candidate? | Australian Source? | WDP Supplied? | Venue Dependent? | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AD01 | Backup | Blood Collection | Spare phlebotomy chair componentry (armrests, wipe-clean covers) | In case of damage | Quantity to be determined from opening-stock policy | each | CONSUMPTION-DEPENDENT | No | Yes | PRO | Same as E01/E02 | No | Yes | No | No | Open | |
| AD02 | Backup | Venue-wide | Spare GPO adaptors/power boards | N/A | Small lot | each | LOCKED | Yes | Yes | CN | Electrical safety mark | Yes | Yes | No | No | Open | |
| AD03 | Backup | Venue-wide | Spare AED pads/battery | Expiry-driven replacement | 1 set | set | CONSUMPTION-DEPENDENT | Yes | Yes, expiry-driven | PRO | ARTG registration | No | Yes | No | No | Open | |
| AD04 | Backup | Blood Collection | Spare sharps containers, biohazard bags | See Section E, additional buffer stock | Quantity to be determined from opening-stock policy | each | CONSUMPTION-DEPENDENT | Yes | Yes | AU | AS/NZS 23907:2023 | No | Yes | No | No | Open | |

---

## Procurement Packages

Each package groups the relevant line items above by supplier-facing bundle, for RFQ/quoting purposes.

**Package 01: Blood Collection.** Items E01-E40. Major equipment: phlebotomy chairs (2), vasovagal recliner, refrigerated centrifuge, specimen refrigerator, thermal label printer. Consumables: sharps containers, biohazard bags, PPE, TGA-listed disinfectant. China candidates: none recommended, this package is Category C throughout (clinical, protected, Australian-sourced). Australian purchases: all furniture, all clinical consumables. Dependencies: WDP's final commercial arrangement (pathology equipment split, medical waste contract), an Australian building/compliance professional for the clinical sink fitout and room ventilation. Information still required: whether WDP covers medical waste disposal.

**Package 02: Hair.** Items J01-J18, K01-K04. Major equipment: 4 styling chairs, 2 backwash basins, named-brand dryers/straighteners. Consumables: shampoo/conditioner/treatment/styling products (pregnancy-safe), capes, towels. China candidates: styling chairs, tool trolleys, brushes/combs (Category A/B). Australian purchases: named-brand hair dryers and straighteners (poor import candidates on warranty grounds). Dependencies: licensed plumber for backwash basins, confirmation of whether colour services are in the current catalogue before purchasing colour equipment. Information still required: colour service confirmation (J14).

**Package 03: Nail.** Items H01-H21. Major equipment: 4 nail tables, 4 UV/LED lamps, LEV extraction unit. Consumables: gel/regular polish, files, buffers, acetone, disinfection solution. China candidates: nail tables, tool trolleys, files/buffers/cuticle tools (Category A). Australian purchases: N95 dust masks, disinfection solution. Dependencies: WorkSafe-WA-familiar LEV contractor (not yet identified). Information still required: LEV contractor identification (H06).

**Package 04: Pedicure.** Items I01-I06. Major equipment: 4 pipeless spa chairs (same zone as Nail, not an additional 8-station expansion). China candidates: pipeless spa chairs, the single highest-confidence quantified saving in this whole register. Australian purchases: plumbing/install (local trade). Dependencies: licensed plumber for chair plumbing.

**Package 05: Massage.** Items F01a-F12. Major equipment: 2-3 pregnancy massage tables (format pending founder decision) or massage station chairs (unlocked, no existing spec if chair-based is adopted). Consumables: pregnancy-safe oil, linen, heated blankets. China candidates: massage tables (with a mandatory Australian reference unit), trolleys. Dependencies: **founder decision on table vs chair format, unresolved, shown with both options' procurement implications rather than silently resolved.**

**Package 06: Beauty.** Items G01-G15. Major equipment: 2-3 facial/beauty treatment beds (recommended count pending sign-off), magnifying lamps, wax heater. Consumables: PPD-free brow tint, pregnancy-safe wax, facial products. China candidates: treatment beds, trolleys (hybrid). Dependencies: Australian hydraulic trade for the 2-sink fitout, founder confirmation of the Beauty station count recommendation (3, matching Massage) and whether deeper facials (steamer) are offered.

**Package 07: Cafe.** Items C01-C26. Major equipment: full-size beverage fridge, display fridge, coffee machine, chilled/boiling water tap, toastie press. Consumables: crockery, takeaway items, food/beverage stock. China candidates: takeaway cups/lids/napkins, some crockery. Australian purchases: refrigeration, coffee machine, water tap (food-safety/plumbing-linked equipment). Dependencies: **external food supplier not yet identified**, local council Food Business Notification, WA food business classification (already scored Low risk band, final confirmation still needed post-menu-lock).

**Package 08: Reception.** Items B01-B18. Major equipment: reception counter (custom, site-installed), 2 iPads, 2 POS terminals, computer, printer. China candidates: cable management, charging stations. Australian purchases: reception counter (structural build), computer/printer (business-grade). Dependencies: none beyond standard IT/IT-account setup; explicitly does not include a dedicated PM Reception workstation (Model C confirmed).

**Package 09: Lounge.** Items D01-D12. Major equipment: 3-4 three-seat couches (site-dependent final count), tablets, side tables. China candidates: side tables, coffee tables, floor lamps, tablet mounts. Australian purchases/hybrid: couches (need in-person testing before bulk purchase). Dependencies: venue floor area (final couch count), tablet content licensing not yet finalised.

**Package 10: Staff/BOH.** Items L01-L07, M01-M04. Major equipment: lockers (count pending final employment pool sizes), staff table, storage shelving. China candidates: clean linen storage, general shelving. Dependencies: final treatment/phlebotomist employment pool size decisions (Chapter 34) before locker/uniform counts can be finalised.

**Package 11: Toilets.** Items N01-N16. Consumables-heavy: toilet paper, paper towel, hand soap, sanitary disposal. Fixtures: dispensers, accessibility grab rails (AS 1428.1). China candidates: bins, toilet brushes, plungers. Dependencies: final toilet count (site-dependent), Australian accessibility verification, paper towel vs hand dryer founder decision.

**Package 12: Cleaning.** Items O01-O17. General and clinical cleaning kept explicitly separate (clinical items live in Package 01). China candidates: mop systems, buckets, microfibre cloths, bin liners. Australian purchases: all disinfectants (general and clinical-grade). Dependencies: none beyond standard supplier selection.

**Package 13: IT.** Items T01-T13. Major equipment: WiFi router, network switches, access points. Optional: security cameras, access control, UPS. Australian purchases: all networking hardware (warranty/support reasons). Dependencies: none beyond standard IT supplier selection; separates required-at-opening from optional/future items explicitly.

**Package 14: Branding.** Items W01-W11. Major items: external signage, internal wayfinding, name badges, uniforms (cross-referenced to their functional areas). Dependencies: **final naming decision (SOLENA vs ELOWEN)** gates external signage, menu, and any name-bearing item; not finalised here.

**Package 15: Opening Consumables.** Cross-references every "Opening Stock?: Yes" row across every section above (approximately 60 line items). See the Opening Day Checklist immediately below for the practical, must-have-before-first-client view rather than a duplicate list here.

---

## Opening Day Procurement Checklist

Practical checklist of what must physically be present before the first client arrives. Organised by area, cross-referencing the ID numbers above rather than restating full specifications.

**Toilets:** toilet paper (N01), paper towel (N02), hand soap (N03), sanitary disposal unit stocked and installed (N06), spare stock (N16).

**Cleaning:** general disinfectant (O06), bathroom cleaner (O07), floor cleaner (O09), bin liners (O10), cleaning gloves (O12), wet floor signs (O14).

**Blood Collection:** phlebotomy chairs installed (E01/E02), centrifuge installed and tested (E15), sharps containers mounted (E09-E11), biohazard bins in place (E12), TGA-listed disinfectant stocked (E28), blood spill kit accessible (E29), glucose solution stocked and refrigerated (E21), collection log/dispatch log/adverse event register printed and ready (E40).

**PPE:** disposable gloves stocked across every area that uses them (E22, H18, J17, S01), N95 masks for Nail (H19), face masks for Blood Collection (E23).

**Towels/Linen:** massage linen (F06), beauty treatment bed linen (G09), hair towels (J09, K03), pedicure/foot towels (I04), general towels (P01), face towels (P02).

**Nail/Hair/Massage/Beauty supplies:** gel and regular polish stocked (H14/H15), base/top coat (H12/H13), files/buffers/cuticle tools (H08-H11), pregnancy-safe massage oil (F07), pregnancy-safe hair products (J10-J13), pregnancy-safe brow tint and wax (G10/G11), facial products (G12).

**Cafe stock:** coffee beans/milk (C23), herbal tea (C24), bottled/canned drinks (C25), pre-made food stock from the confirmed external supplier (C22, still a genuine dependency), crockery and takeaway items (C10-C15).

**POS/Booking/Technology:** POS terminals live and tested (B07), EFTPOS connected, Fresha booking system configured (B13), iPads charged and kiosk-mounted (B08/B09), WiFi router live (T01), backup/cloud backup configured (T11).

**Tablets/Chargers:** Lounge tablets loaded with curated content (D05), tablet mounts secured (D06), charging cables/stations tested (D02).

**Uniforms:** confirmed for every employed staff member rostered for opening week (E39, F12, G15, W05).

**Bins/Waste arrangements:** general waste bins placed in every area (C21, D11, J16, N09), biohazard waste collection arranged (E14, confirm WDP dependency status before opening), general waste collection contract active (AA03).

**Emergency equipment:** AED installed and checked (R01), first aid kits stocked (R02), panic buttons tested (R03), EpiPen in date (R07), fire extinguishers in place (A01).

**Signage:** biohazard/hand-hygiene/no-entry signage in the Blood Collection Room (E33-E35), toilet signage (N14), external signage (gated on naming decision, W01), wet floor signs (O14).

---

## Costing Summary

**Known priced items (from existing repository research, not re-estimated):** approximately 90 of the ~230 line items above carry a real market-range price sourced from `docs/equipment-costs.md` and `docs/architecture/ITEMISED-PURCHASE-LIST.md`'s own MEDIUM/LOW-confidence research, primarily in Blood Collection, Massage, Nail, Hair, Beauty, Lounge, and Cafe equipment. These are existing repository figures, not newly invented for this document.

**Items requiring quotes:** the majority of consumables (CONSUMPTION-DEPENDENT quantity basis) do not carry a priced total in this document, since opening-stock quantity itself is not yet fixed (see the Quantity Basis key). Items marked PROFESSIONAL-VERIFICATION (electrical, plumbing, HVAC, accessibility) require AU RFQ REQUIRED from a licensed trade, not a shopping-list price. Items marked SITE-DEPENDENT (toilet fixtures, exact GPO counts, Lounge couch final quantity) require SITE QUOTE REQUIRED once a venue is confirmed. The genuinely unresolved China-candidate items (pipeless pedicure chairs, LEV unit, some furniture) would need CHINA RFQ REQUIRED once a sourcing-agent engagement begins.

**This document does not present a complete fit-out cost total.** The existing `docs/equipment-costs.md` Summary Budget (day-one equipment only, excluding fit-out construction) remains the closest existing aggregate figure (approximately A$43,190-97,430 before this round's Cafe correction added it to the day-one total; the Cafe correction adds a further A$5,000-12,650). Construction/fit-out costs, exact GPO/lighting-fixture counts, toilet-count-dependent consumable volumes, and the external Cafe food supplier's own pricing are all explicitly not included in any total, since they are genuinely not known yet, not because they were overlooked.

---

## Research Performed This Round (Not Left as "Needs Research")

1. **WA Skin Penetration Code:** the Code of Practice for Skin Penetration Procedures 1998, under the Health (Skin Penetration Procedures) Regulations 1998, applies to waxing, tweezing, electrolysis, and manicure/pedicure work; massage is confirmed non-invasive and outside its scope. A hands-free handwash basin (hot/cold water, soap, paper towel) is required in the immediate treatment area for skin-penetration procedures. This directly informs the Beauty (Section G08) and Nail hygiene requirements above. Final sign-off on the specific venue's compliance still requires a WA building/compliance professional once a site is confirmed (a genuine, disclosed remaining step, not a gap in the research itself).
2. **WA Food Business Risk Classification System (Department of Health, 2024):** applied to the current Cafe model (pre-made, externally-supplied, on-site toasting only) and scored at the Low risk band (approximately 36 of a possible 7-39), informing Section C's compliance column directly.
3. **Nail ventilation (LEV):** researched that local exhaust ventilation via per-station downdraft/capture-hood systems is the standard compliance method for open-plan nail-station layouts, distinct from full room enclosure. The remaining gap is a named WorkSafe-WA-familiar contractor, not the compliance method itself (Section H06).
4. **Cleaning/infection-control product categories:** researched to distinguish clinical-grade (TGA-listed) products required for the Blood Collection Room from general-purpose cleaning products used elsewhere in the venue, avoiding a single "cleaning supplies" catch-all line.

## Genuine Remaining Gaps (Not Disguised as Research, Not Papered Over)

- **External Cafe food supplier:** not yet identified (Section C22). This is a real procurement dependency, not invented.
- **LEV contractor (Nail Station):** no WorkSafe-WA-familiar contractor identified yet (Section H06).
- **Laundry model:** in-house wash vs outsourced contract is not confirmed anywhere in this repository (Sections P10/P11).
- **Massage station format (table/bed vs chair-based):** a genuine, unresolved founder decision (Section F01a/F01b).
- **Staff lockers, uniform, and name-badge exact unit counts:** depend on the final employment pool sizes (12 vs 11 treatment, 4 vs 3 phlebotomists), themselves still open founder decisions (Chapter 34).
- **Toilet-count-dependent items:** cannot be finalised until a venue is confirmed (Section N throughout).
- **Medical waste disposal:** whether WDP's own collection-centre arrangement already covers this is a genuine, unresolved dependency (Section E14).

---

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the single authoritative, itemised procurement register for opening GTT Center Perth, superseding `docs/equipment-costs.md` and `docs/architecture/FIT-OUT-EQUIPMENT-SCHEDULE.md`'s role as the primary procurement source. Every quantity is classified against a real basis (LOCKED/CALCULATED/SITE-DEPENDENT/STAFF-DEPENDENT/CONSUMPTION-DEPENDENT/OPTIONAL/PROFESSIONAL-VERIFICATION/FOUNDER-DECISION/WDP-DEPENDENT), not an invented number. Genuine research was performed this round on WA Skin Penetration Code, WA Food Business Risk Classification, and nail ventilation methods, rather than left as "needs research." No spray tan, GDM snack pack, post-blood-draw snack, landlord contribution, old property listings, or superseded staffing/pricing/break-even figures appear anywhere in this document.
