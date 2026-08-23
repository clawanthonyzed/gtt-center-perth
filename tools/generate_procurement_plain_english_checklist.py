"""
Generates docs/architecture/PROCUREMENT-SHOPPING-LIST-PLAIN-ENGLISH.md: a
teenager-proof shopping checklist covering all 281 distinct items across all
26 authoritative register categories (A through AD), organised by the
register's own category structure rather than a new taxonomy. Replaces the
earlier hand-authored version, which covered only 6 founder-named areas.

Each item gets: quantity, what it is, where it goes, what to look for, where
to buy it, China/Australia/Hybrid classification, order-ready/RFQ/blocked
status, approximate existing researched price (if one exists), and what must
be confirmed before purchase, so someone with no industry background can
walk through the venue and know exactly what to do with each item.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from procurement_register_parser import parse_register
from procurement_derivations import derive, readiness_letter

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "architecture" / "PROCUREMENT-SHOPPING-LIST-PLAIN-ENGLISH.md"

STATUS_LABEL = {
    "A": "Order-ready",
    "B": "RFQ required (quote needed before ordering)",
    "C": "Blocked: waiting on a confirmed venue to be measured",
    "D": "Blocked: waiting on professional verification",
    "E": "Blocked: waiting on WDP confirmation",
    "F": "Blocked: waiting on a founder decision",
    "G": "Blocked: waiting on a specific information gap to close",
    "H": "Future/optional, not being ordered now",
}


def render_item(full):
    lines = []
    lines.append(f"- [ ] **{full['item']}** (Item ID: {full['id']})")
    lines.append(f"    - Quantity: {full.get('quantity', 'N/A')} ({full.get('quantity_basis', 'N/A')})")
    lines.append(f"    - What it is: {full.get('description') or 'N/A'}")
    lines.append(f"    - Where it goes: {full.get('category', 'N/A')}, {full.get('area', 'N/A')}")
    lines.append(f"    - What to look for: {full.get('description') or 'N/A'}")
    lines.append(f"    - Where to buy it: {full.get('preferred_channel', 'Not yet determined')}")
    lines.append(f"    - China/Australia/Hybrid: {full.get('china_australia_classification', 'Not yet determined')}")
    letter = readiness_letter(full.get("readiness", ""))
    lines.append(f"    - Status: {STATUS_LABEL.get(letter, 'Not yet determined')}")
    lines.append(f"    - Approximate existing researched price: {full.get('existing_price_source', 'No price researched yet')}")
    lines.append(f"    - Must confirm before purchase: {full.get('still_required', 'Not yet determined')}")
    lines.append("")
    return "\n".join(lines)


def render_crossref(cr):
    return (f"- [ ] **{cr['item']}** (Item ID: {cr['id']}): cross-reference only, "
            f"already covered elsewhere in this checklist, not a second purchase. "
            f"{cr['description']}\n")


def main():
    items, cross_refs, headings = parse_register()

    section_order = list(headings.keys())
    by_section = {letter: [] for letter in section_order}
    for item in items:
        letter = item.get("section_letter")
        if letter in by_section:
            by_section[letter].append(derive(item))

    crossref_by_section = {letter: [] for letter in section_order}
    for cr in cross_refs:
        letter = cr.get("section_letter")
        if letter in crossref_by_section:
            crossref_by_section[letter].append(cr)

    out = []
    out.append("# Plain-English Shopping List")
    out.append("")
    out.append(
        "Status: current as of 2026-08-23. A teenager-proof shopping checklist "
        "covering all 281 distinct items across all 26 authoritative register "
        "categories (Section A through Section AD), organised exactly as "
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` itself is "
        "organised, generated mechanically by "
        "`tools/generate_procurement_plain_english_checklist.py` so coverage "
        "and quality are consistent across every category, not just the areas "
        "that got manual attention. Re-run the generator if the register "
        "changes; do not hand-edit this file directly."
    )
    out.append("")
    out.append(
        "**The test this checklist is built to pass:** someone with no salon, "
        "clinic, cafe, or wellness industry background should be able to read "
        "one item's entry and know what it is, how many are needed, where it "
        "goes, what to look for, where to buy it, whether it is China, "
        "Australia, or hybrid sourced, whether it can be ordered today or is "
        "blocked, roughly what it costs if that has already been researched, "
        "and exactly what still needs to happen before it can be purchased."
    )
    out.append("")
    out.append(
        "**No purchase, RFQ, or supplier/agent contact has been made.** "
        "Ticking a box here is a planning action, not a purchase confirmation."
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
        for full in section_items:
            out.append(render_item(full))
            total_rendered += 1
        if section_crossrefs:
            for cr in section_crossrefs:
                out.append(render_crossref(cr))

    out.append("## What This Checklist Deliberately Does Not Include")
    out.append("")
    out.append(
        "Any snack pack, spray tan service, or service not currently confirmed "
        "in the service catalogue. Cross-reference items (shared across "
        "multiple functional areas, e.g. staff uniforms, linen) are ticked "
        "once in their home section and pointed to elsewhere, never listed "
        "twice as independent purchases."
    )
    out.append("")
    out.append("## Generation Summary")
    out.append("")
    out.append(f"- Total distinct items covered: {total_rendered}")
    out.append(f"- Cross-reference items pointed to (not double-counted): {len(cross_refs)}")
    out.append(f"- Total register rows accounted for: {total_rendered + len(cross_refs)}")
    out.append("")
    out.append("## Sourcing")
    out.append("")
    out.append(
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, "
        "`docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md`, "
        "`docs/architecture/PROCUREMENT-ORDER-READINESS-CHECKLIST.md`, "
        "`tools/generate_procurement_plain_english_checklist.py`."
    )
    out.append("")
    out.append("## Changelog")
    out.append("")
    out.append(
        "**2026-08-23 (rebuilt):** Expanded from the original 6-founder-named-area "
        "version to all 26 authoritative register categories, generated "
        "mechanically rather than hand-authored, per direct founder instruction "
        "(Part 2) that the earlier scope-limited version did not pass the "
        "teenager-ordering test for the whole venture."
    )
    out.append("")

    OUTPUT_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {total_rendered} items and {len(cross_refs)} cross-references.")


if __name__ == "__main__":
    main()
