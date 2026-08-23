"""
Generates docs/architecture/PROCUREMENT-ROOM-BY-ROOM-CHECKLIST.md (Part 3):
"what needs to exist here before we can open?" for 18 physical/functional
areas, each divided into Furniture, Equipment, Fixtures, Electrical,
Plumbing, Lighting, HVAC/ventilation, Consumables, Technology, Signage,
Safety, Cleaning, Opening Stock, Future/Optional.

This is a cross-reference view only. It lists Item IDs and item names per
bucket, tagged with the master register's own Readiness classification
(LOCKED/SITE-DEPENDENT/etc mapped from A-H); it does not restate quantities,
since MASTER-PROCUREMENT-SHOPPING-LIST.md remains the single quantity/source
of truth (per the founder's own explicit instruction).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from procurement_register_parser import parse_register
from procurement_derivations import readiness_letter

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "architecture" / "PROCUREMENT-ROOM-BY-ROOM-CHECKLIST.md"

# 18 requested areas -> the register's own Category values that belong to
# that physical/functional area. Every one of the register's 26 Category
# values is assigned to exactly one of the 18 areas (verified in Section
# "Coverage Check" at the bottom of the generated file).
AREA_MAP = [
    ("1. Blood Collection Area", ["Blood Collection"]),
    ("2. Hair Wash Area", ["Hair Wash"]),
    ("3. Hair Styling Area", ["Hair"]),
    ("4. Nail Area", ["Nail"]),
    ("5. Pedicure Area", ["Pedicure"]),
    ("6. Massage Area", ["Massage"]),
    ("7. Beauty Area", ["Beauty"]),
    ("8. Reception", ["Reception"]),
    ("9. Cafe", ["Cafe"]),
    ("10. Lounge", ["Lounge"]),
    ("11. Staff Area", ["Staff Area"]),
    ("12. Storage", ["Storage"]),
    ("13. Toilets", ["Toilets"]),
    ("14. Cleaning / Laundry", ["Cleaning", "Laundry"]),
    ("15. Clinical / Waste Area", ["Clinical Consumables", "Waste"]),
    ("16. General Venue Infrastructure", ["Venue", "Maintenance", "Backup", "Branding", "Lighting"]),
    ("17. IT / Security", ["IT", "Security"]),
    ("18. Staff / Emergency Equipment", ["First Aid", "PPE"]),
]

BUCKET_ORDER = [
    "Furniture", "Equipment", "Fixtures", "Electrical", "Plumbing", "Lighting",
    "HVAC/Ventilation", "Consumables", "Technology", "Signage", "Safety",
    "Cleaning", "Opening Stock", "Future/Optional",
]

# Sub-location (Area column) keyword to functional bucket. Checked only for
# items not already routed to Opening Stock or Future/Optional by priority.
BUCKET_KEYWORDS = [
    (["Furniture", "Furniture/Equipment", "Furniture (OPTION A: table/bed)", "Furniture (OPTION B: chair-based)"], "Furniture"),
    (["Equipment", "Beverage Equipment", "Food Service Equipment", "Heating/Toasting",
      "Colour Equipment", "Practitioner Equipment", "Staff Equipment", "Pathology Equipment",
      "Specimen Handling", "Refrigeration"], "Equipment"),
    (["Fixtures", "Storage", "Privacy", "Construction"], "Fixtures"),
    (["Electrical"], "Electrical"),
    (["Plumbing", "Hot Water"], "Plumbing"),
    (["Lighting"], "Lighting"),
    (["Ventilation"], "HVAC/Ventilation"),
    (["Consumables", "Glucose Drink", "Supplier/Food Stock", "Linen", "Takeaway Items",
      "Crockery", "Disposables", "Food Safety"], "Consumables"),
    (["Technology", "Documentation", "POS"], "Technology"),
    (["Signage"], "Signage"),
    (["PPE", "Hand Hygiene", "Sharps Disposal", "Clinical Waste", "Emergency", "Hygiene"], "Safety"),
    (["Cleaning", "Waste"], "Cleaning"),
]

READINESS_MAP = {
    "A": "ORDER-READY",
    "B": "RFQ-READY",
    "C": "SITE-DEPENDENT",
    "D": "PROFESSIONAL VERIFICATION",
    "E": "WDP-DEPENDENT",
    "F": "FOUNDER DECISION",
    "G": "INFORMATION REQUIRED",
    "H": "FUTURE/OPTIONAL",
}


def bucket_for(item):
    letter = readiness_letter(item.get("readiness", ""))
    if letter == "H":
        return "Future/Optional"
    if (item.get("opening_stock") or "").strip().lower() == "yes":
        return "Opening Stock"
    area = item.get("area", "")
    for keywords, bucket in BUCKET_KEYWORDS:
        if area in keywords:
            return bucket
    return "Fixtures"  # residual default for area values not explicitly mapped (General, Venue-wide, etc)


def main():
    items, cross_refs, headings = parse_register()

    by_category = {}
    for item in items:
        by_category.setdefault(item["category"], []).append(item)

    mapped_categories = set()
    for _, cats in AREA_MAP:
        mapped_categories.update(cats)
    all_categories = set(by_category.keys())
    unmapped = all_categories - mapped_categories
    extra_mapped = mapped_categories - all_categories

    out = []
    out.append("# Room-by-Room Procurement Checklist")
    out.append("")
    out.append(
        "Status: current as of 2026-08-23. Answers \"what needs to exist here "
        "before we can open?\" for 18 physical/functional areas, generated "
        "mechanically by `tools/generate_procurement_room_checklist.py` "
        "directly from `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`. "
        "This is a cross-reference view only: it lists Item IDs and names per "
        "area and bucket, tagged with the register's own Readiness "
        "classification. **It does not restate quantities.** "
        "`MASTER-PROCUREMENT-SHOPPING-LIST.md` remains the single "
        "quantity/source of truth; look up the Item ID there for the actual "
        "quantity, price, and full specification."
    )
    out.append("")
    out.append(
        "Each area is divided into: Furniture, Equipment, Fixtures, "
        "Electrical, Plumbing, Lighting, HVAC/Ventilation, Consumables, "
        "Technology, Signage, Safety, Cleaning, Opening Stock, "
        "Future/Optional. An item appears in exactly one bucket per area: "
        "Future/Optional items are pulled out first (Readiness H), then "
        "Opening Stock items (register's own Opening Stock? = Yes), then "
        "everything else is bucketed by its own sub-area/location field."
    )
    out.append("")

    for area_title, categories in AREA_MAP:
        out.append(f"## {area_title}")
        out.append("")
        area_items = []
        for cat in categories:
            area_items.extend(by_category.get(cat, []))
        if not area_items:
            out.append("No items in the register are assigned to this area.")
            out.append("")
            continue

        buckets = {b: [] for b in BUCKET_ORDER}
        for item in area_items:
            buckets[bucket_for(item)].append(item)

        for bucket in BUCKET_ORDER:
            bucket_items = buckets[bucket]
            if not bucket_items:
                continue
            out.append(f"**{bucket}:**")
            out.append("")
            for item in bucket_items:
                letter = readiness_letter(item.get("readiness", ""))
                tag = READINESS_MAP.get(letter, "NOT CLASSIFIED")
                out.append(f"- [{tag}] {item['id']}: {item['item']}")
            out.append("")
        out.append("---")
        out.append("")

    out.append("## Coverage Check")
    out.append("")
    out.append(
        f"All {len(all_categories)} register categories accounted for across "
        f"the 18 areas above: {'Yes' if not unmapped and not extra_mapped else 'NO, SEE WARNING BELOW'}."
    )
    out.append("")
    if unmapped:
        out.append(f"**WARNING: unmapped categories (present in the register, not assigned to any area): {sorted(unmapped)}**")
        out.append("")
    if extra_mapped:
        out.append(f"**WARNING: categories mapped above that do not exist in the register: {sorted(extra_mapped)}**")
        out.append("")

    out.append("## Sourcing")
    out.append("")
    out.append(
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (authoritative "
        "quantities, prices, and full specification for every Item ID above), "
        "`docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md`, "
        "`tools/generate_procurement_room_checklist.py`."
    )
    out.append("")
    out.append("## Changelog")
    out.append("")
    out.append(
        "**2026-08-23 (created):** Built per direct founder instruction (Part 3) "
        "as a room-by-room walk-through checklist, generated mechanically as a "
        "cross-reference view over the master register rather than a "
        "duplicated quantity table, to avoid any risk of the two documents "
        "disagreeing."
    )
    out.append("")

    OUTPUT_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}. Unmapped categories: {unmapped or 'none'}. Extra mapped: {extra_mapped or 'none'}.")


if __name__ == "__main__":
    main()
