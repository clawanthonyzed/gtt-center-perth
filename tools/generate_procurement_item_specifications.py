"""
Generates docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md: a full
42-field procurement specification record for every one of the 281 distinct
items in MASTER-PROCUREMENT-SHOPPING-LIST.md, derived mechanically (see
procurement_register_parser.py / procurement_derivations.py) rather than
hand-authored, so quality is consistent across all 281 items and nothing is
fabricated. The 25 cross-reference rows are listed separately, pointing back
to their home item, not re-specified (avoiding double-counting).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from procurement_register_parser import parse_register
from procurement_derivations import derive

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "architecture" / "PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md"

FIELD_ORDER = [
    ("1. Procurement Item ID", "id"),
    ("2. Item name", "item"),
    ("3. Plain-English description", "description"),
    ("4. Business area", "category"),
    ("5. Sub-area/location", "area"),
    ("6. Quantity", "quantity"),
    ("7. Quantity basis", "quantity_basis"),
    ("8. Unit of measure", "unit"),
    ("9. Opening quantity (where applicable)", "opening_stock"),
    ("10. Reorder quantity (where applicable)", "reorderable"),
    ("11. Required at opening Y/N", "required_at_opening"),
    ("12. Future/optional Y/N", "future_optional"),
    ("13. Procurement readiness classification", "readiness"),
    ("14. Current status", "cost_status"),
    ("15. Source route", "sourcing"),
    ("16. China/Australia classification", "china_australia_classification"),
    ("17. Preferred procurement channel", "preferred_channel"),
    ("18. Supplier type", "supplier_type"),
    ("19. Specification", "description"),
    ("20. Dimensions if known", "dimensions"),
    ("21. Material if known", "material"),
    ("22. Finish if known", "finish"),
    ("23. Colour/brand requirements if known", "colour_brand"),
    ("24. Performance requirements", "performance_requirements"),
    ("25. Electrical requirements if applicable", "electrical_requirements"),
    ("26. Plumbing requirements if applicable", "plumbing_requirements"),
    ("27. HVAC/ventilation requirements if applicable", "hvac_ventilation_requirements"),
    ("28. Clinical requirements if applicable", "clinical_requirements"),
    ("29. Food-safety requirements if applicable", "food_safety_requirements"),
    ("30. Accessibility requirements if applicable", "accessibility_requirements"),
    ("31. Certification/compliance requirements", "certification_compliance"),
    ("32. Installation requirements", "installation_requirements"),
    ("33. Delivery requirements", "delivery_requirements"),
    ("34. Assembly requirements", "assembly_requirements"),
    ("35. Warranty requirements", "warranty_requirements"),
    ("36. Quality-control requirements", "qc_requirements"),
    ("37. Quote/RFQ requirements", "quote_rfq_required"),
    ("38. Existing price/source if already researched", "existing_price_source"),
    ("39. Cost status", "cost_status"),
    ("40. What is still required before ordering", "still_required"),
    ("41. Who must confirm it", "who_confirms"),
    ("42. Final purchasing instruction in plain English", "final_instruction"),
]


def render_item(full):
    lines = [f"### {full['id']}: {full['item']}", ""]
    seen_fields = set()
    for label, key in FIELD_ORDER:
        if key in seen_fields and key == "description":
            # field 19 (Specification) intentionally reuses field 3's source
            # data under a different label per the founder's own field list;
            # render both, they answer different questions (description vs
            # buyable spec) even though the source text is the same.
            pass
        seen_fields.add(key)
        value = full.get(key, "")
        if value in ("", None):
            value = "N/A"
        lines.append(f"- **{label}:** {value}")
    lines.append(f"- **Register note:** {full.get('register_note', 'None')}")
    lines.append("")
    return "\n".join(lines)


def render_crossref(cr):
    return (f"- **{cr['id']}** ({cr['item']}): {cr['description']} "
            f"Cross-reference only, not an independent procurement item, "
            f"see the item it points to for the real specification.")


def main():
    items, cross_refs, headings = parse_register()

    # Group items by section letter, preserving document order
    section_order = list(headings.keys())
    by_section = {letter: [] for letter in section_order}
    for item in items:
        letter = item.get("section_letter")
        if letter in by_section:
            by_section[letter].append(item)

    crossref_by_section = {letter: [] for letter in section_order}
    for cr in cross_refs:
        letter = cr.get("section_letter")
        if letter in crossref_by_section:
            crossref_by_section[letter].append(cr)

    out = []
    out.append("# Full Per-Item Procurement Specification")
    out.append("")
    out.append(
        "Status: current as of 2026-08-23. A complete 42-field specification "
        "record for every one of the 281 distinct items in "
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, generated "
        "mechanically by `tools/generate_procurement_item_specifications.py` "
        "directly from that register (see `tools/procurement_register_parser.py` "
        "and `tools/procurement_derivations.py` for the exact derivation rules), "
        "not hand-authored, so quality and field coverage are consistent across "
        "all 281 items rather than varying by which item happened to get manual "
        "attention. Re-run the generator any time the register changes; do not "
        "hand-edit this file directly, edit the register and regenerate instead."
    )
    out.append("")
    out.append(
        "**Honesty note on derived fields:** dimensions, material, finish, "
        "colour/brand, electrical, plumbing, HVAC, clinical, food-safety, and "
        "accessibility fields are derived only from each item's own row text "
        "in the register (description, compliance/verification, and notes "
        "columns). Some requirements exist at the venue-program level rather "
        "than being repeated in every relevant item's own row (for example, "
        "the Pedicure zone's water supply/drain requirement is stated once in "
        "`docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md` rather than on "
        "every individual pedicure-chair row). Where a field below reads "
        "\"N/A\", check the venue program table and the relevant procurement "
        "package documents before assuming no requirement exists at all."
    )
    out.append("")
    out.append(
        "**Cross-reference items:** 25 rows in the master register are "
        "deliberately abbreviated pointers to an item already itemised "
        "elsewhere (avoiding double-counting a shared item across multiple "
        "functional areas, e.g. staff uniforms). These are listed at the end "
        "of each section below, not given a full 42-field record, since they "
        "are not independent purchasing decisions."
    )
    out.append("")
    out.append("## How to Read Each Record")
    out.append("")
    out.append(
        "Fields 1-18 identify what the item is and where it sits in the "
        "procurement system. Fields 19-36 describe what to actually look for "
        "when sourcing it. Fields 37-42 tell you exactly what to do next. "
        "Field 19 (Specification) and field 3 (Plain-English description) "
        "share the same source text in the register; they are listed "
        "separately because the founder's own field list distinguishes "
        "\"what it is\" from \"what to buy\", even where the register itself "
        "answers both with one sentence."
    )
    out.append("")

    total_rendered = 0
    for letter in section_order:
        section_items = by_section[letter]
        section_crossrefs = crossref_by_section[letter]
        if not section_items and not section_crossrefs:
            continue
        heading_text = headings[letter]
        out.append(f"## Section {letter}: {heading_text}")
        out.append("")
        for item in section_items:
            full = derive(item)
            out.append(render_item(full))
            total_rendered += 1
        if section_crossrefs:
            out.append("**Cross-reference items in this section (not independently specified, see the target item):**")
            out.append("")
            for cr in section_crossrefs:
                out.append(render_crossref(cr))
            out.append("")
        out.append("---")
        out.append("")

    out.append("## Generation Summary")
    out.append("")
    out.append(f"- Total distinct items with a full 42-field specification record: {total_rendered}")
    out.append(f"- Cross-reference items listed (not independently specified): {len(cross_refs)}")
    out.append(f"- Total register rows accounted for: {total_rendered + len(cross_refs)}")
    out.append("")
    out.append("## Sourcing")
    out.append("")
    out.append(
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (authoritative "
        "source for every field below), `tools/generate_procurement_item_specifications.py`, "
        "`tools/procurement_register_parser.py`, `tools/procurement_derivations.py`."
    )
    out.append("")
    out.append("## Changelog")
    out.append("")
    out.append(
        "**2026-08-23 (created):** Built per direct founder instruction (Part 1) "
        "as a genuinely complete per-item specification for all 281 items, "
        "generated mechanically from the authoritative register rather than "
        "hand-authored, to guarantee consistent field coverage and eliminate "
        "fabrication risk at this scale. Supersedes the coverage-only statement "
        "in `PROCUREMENT-ITEM-SPECIFICATION-COVERAGE.md`, which remains as the "
        "record of why a generated approach was chosen over hand-authoring."
    )
    out.append("")

    OUTPUT_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {total_rendered} full item records and {len(cross_refs)} cross-reference pointers.")


if __name__ == "__main__":
    main()
