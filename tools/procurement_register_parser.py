"""
GTT Center Perth -- Procurement register parser.

Parses docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md into structured
records, so downstream generator scripts (item specifications, plain-English
checklist, order-readiness view) derive every field mechanically from the
authoritative register rather than being hand-copied and risking drift.

The register is not a single 19-column table throughout: 8 rows in Section T
(IT) carry a 20th trailing column (a per-section "Required at Opening /
Optional" flag not used elsewhere), and 20 rows are deliberately abbreviated
cross-reference rows (18 cells) that point to an item's real home section
rather than re-itemising it. Both variants are handled explicitly below
rather than assumed away.

This script does not invent any field value. Where the register itself does
not state something, the parsed record carries None / "" and the downstream
generator is responsible for rendering that honestly (e.g. "Not yet
determined"), never silently fabricating a plausible-looking value.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTER_PATH = REPO_ROOT / "docs" / "architecture" / "MASTER-PROCUREMENT-SHOPPING-LIST.md"

COLUMNS_19 = [
    "id", "category", "area", "item", "description", "quantity", "unit",
    "quantity_basis", "readiness", "opening_stock", "reorderable", "sourcing",
    "compliance", "china_candidate", "australian_source", "wdp_supplied",
    "venue_dependent", "status", "notes",
]

ROW_RE = re.compile(r'^\|\s*([A-Z]{1,3}\d{2}[a-z]?)\s*\|')

CATEGORY_HEADING_RE = re.compile(r'^## ([A-Z]{1,2})\. (.+)$')


def _split_row(line):
    return [p.strip() for p in line.strip().strip('|').split('|')]


def parse_register(path=None):
    """Returns (items, cross_refs, category_headings).

    items: list of dicts, one per real (scored) procurement item, 19 fields
    cross_refs: list of dicts for the 25 cross-reference rows (abbreviated)
    category_headings: dict of category letter -> heading text, in document order
    """
    path = path or REGISTER_PATH
    lines = path.read_text(encoding="utf-8").splitlines()

    items = []
    cross_refs = []
    category_headings = {}
    current_category_letter = None
    current_category_heading = None

    for line in lines:
        heading_match = CATEGORY_HEADING_RE.match(line)
        if heading_match:
            current_category_letter = heading_match.group(1)
            current_category_heading = heading_match.group(2)
            category_headings[current_category_letter] = current_category_heading
            continue

        if not ROW_RE.match(line):
            continue

        parts = _split_row(line)
        is_crossref = "Cross-reference" in line or "not scored" in line

        if is_crossref:
            # Abbreviated row: ID, Category, Area, Item, Description(cross-ref
            # text), then a run of N/A cells. Only the first 5 real fields are
            # meaningful; everything else is genuinely N/A by the register's
            # own design (it is a pointer, not an independent item).
            record = {
                "id": parts[0] if len(parts) > 0 else "",
                "category": parts[1] if len(parts) > 1 else "",
                "area": parts[2] if len(parts) > 2 else "",
                "item": parts[3] if len(parts) > 3 else "",
                "description": parts[4] if len(parts) > 4 else "",
                "section_letter": current_category_letter,
                "section_heading": current_category_heading,
                "is_cross_reference": True,
            }
            cross_refs.append(record)
            continue

        # Real scored row: 19 columns normally, 20 in Section T (an extra
        # trailing "Required at Opening / Optional" flag). Never assume a
        # fixed length silently; branch on what is actually present.
        record = {"section_letter": current_category_letter,
                   "section_heading": current_category_heading,
                   "is_cross_reference": False}

        if len(parts) == 19:
            for name, value in zip(COLUMNS_19, parts):
                record[name] = value
            record["opening_optional_flag"] = None
        elif len(parts) == 20:
            for name, value in zip(COLUMNS_19, parts):
                record[name] = value
            record["opening_optional_flag"] = parts[19]
        elif len(parts) == 18:
            # Genuinely short, scored row (should not normally occur outside
            # cross-references, but handled defensively rather than crashing
            # or silently mis-aligning every subsequent field).
            for name, value in zip(COLUMNS_19, parts):
                record[name] = value
            for name in COLUMNS_19:
                record.setdefault(name, "")
            record["opening_optional_flag"] = None
            record["_short_row_warning"] = f"Row had 18 cells, expected 19: {parts[0]}"
        else:
            record["_parse_warning"] = f"Unexpected column count {len(parts)} for row {parts[0] if parts else '?'}"
            for name in COLUMNS_19:
                record.setdefault(name, "")
            record["id"] = parts[0] if parts else ""
            record["opening_optional_flag"] = None

        items.append(record)

    return items, cross_refs, category_headings


if __name__ == "__main__":
    items, cross_refs, headings = parse_register()
    print(f"Parsed {len(items)} scored items, {len(cross_refs)} cross-reference rows, "
          f"{len(headings)} category headings.")
    warnings = [i for i in items if "_parse_warning" in i or "_short_row_warning" in i]
    if warnings:
        print(f"WARNINGS on {len(warnings)} rows:")
        for w in warnings:
            print(" ", w.get("_parse_warning") or w.get("_short_row_warning"))
    else:
        print("No parse warnings.")
