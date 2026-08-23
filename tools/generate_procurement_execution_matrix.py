"""
Generates docs/architecture/PROCUREMENT-EXECUTION-MATRIX.md: the single
operational matrix tracing every one of the 281 distinct items, per the
founder's execution-readiness instruction. Reuses the existing parser and
derivation pipeline (no new classification system introduced); adds only
the practical execution fields (can-action-today, exact action, dependency
type, who provides it, purchase-route type) derived by rule from data
already in the register.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from procurement_register_parser import parse_register
from procurement_derivations import derive, readiness_letter

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "architecture" / "PROCUREMENT-EXECUTION-MATRIX.md"

CAN_ACTION_TODAY = {"A": "Yes, order now", "B": "Yes, RFQ/quote now"}

DEPENDENCY_TYPE = {
    "A": "None",
    "B": "Supplier-dependent (need a quote)",
    "C": "Venue-dependent",
    "D": "Professional-verification-dependent",
    "E": "WDP-dependent",
    "F": "Internal (founder decision)",
    "G": "Internal (information gap)",
    "H": "None (deferred by choice, not a dependency)",
}

WHO_PROVIDES = {
    "A": "N/A, ready to order",
    "B": "Selected supplier (quote)",
    "C": "Venue measurement (Venue Manager/builder/Anthony)",
    "D": "Named licensed Australian professional",
    "E": "WDP (via Reed's partnership channel)",
    "F": "Anthony",
    "G": "Venue Manager once hired, or Anthony in the interim",
    "H": "Anthony, if reconsidered post-opening",
}

PURCHASE_ROUTE = {
    "CN": "Sourcing-agent/factory RFQ (China)",
    "AU": "Normal purchase or Australian supplier RFQ",
    "HY": "Normal purchase or RFQ, either route",
    "PRO": "Named professional/clinical supplier RFQ",
    "WDP": "WDP confirmation, not an open-market purchase",
    "SITE": "Builder/trade quote",
}


def main():
    items, cross_refs, headings = parse_register()

    out = []
    out.append("# Procurement Execution Matrix")
    out.append("")
    out.append(
        "Status: current as of 2026-08-23. One operational matrix tracing "
        "every one of the 281 distinct items in "
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, generated "
        "mechanically by `tools/generate_procurement_execution_matrix.py`. "
        "This reuses the register's own existing Readiness classification "
        "and Sourcing code; it does not introduce a second, conflicting "
        "system. Columns: Item ID, Item, Category, Area, Quantity, Quantity "
        "Basis, Readiness, Sourcing, Actionable Today, Exact Action "
        "Required, Dependency Type, Who Provides It, Purchase Route, Before "
        "Opening?, Opening Stock?, Future/Optional?."
    )
    out.append("")
    out.append(
        "**No information is invented to make an item appear ready.** Where "
        "an item cannot be actioned today, the matrix says so and states "
        "the real blocking dependency, per the register's own existing "
        "classification, not a re-judgement."
    )
    out.append("")

    section_order = list(headings.keys())
    by_section = {letter: [] for letter in section_order}
    for item in items:
        letter = item.get("section_letter")
        if letter in by_section:
            by_section[letter].append(item)

    total = 0
    for letter in section_order:
        section_items = by_section[letter]
        if not section_items:
            continue
        out.append(f"## Section {letter}: {headings[letter]}")
        out.append("")
        out.append("| Item ID | Item | Quantity | Qty Basis | Readiness | Sourcing | Actionable Today | Exact Action Required | Dependency Type | Who Provides It | Purchase Route | Before Opening? | Opening Stock? | Future/Optional? |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for item in section_items:
            full = derive(item)
            letter_r = readiness_letter(full.get("readiness", ""))
            actionable = CAN_ACTION_TODAY.get(letter_r, "No")
            dep_type = DEPENDENCY_TYPE.get(letter_r, "Not yet determined")
            who = WHO_PROVIDES.get(letter_r, "Not yet determined")
            sourcing = (full.get("sourcing") or "").strip()
            route = PURCHASE_ROUTE.get(sourcing, "Not yet determined")
            before_opening = full.get("required_at_opening", "Not yet determined")
            row = [
                full["id"], full["item"], full.get("quantity", "N/A"),
                full.get("quantity_basis", "N/A"), full.get("readiness", "N/A"),
                sourcing or "N/A", actionable, full.get("final_instruction", "Not yet determined"),
                dep_type, who, route, before_opening,
                full.get("opening_stock", "N/A"), full.get("future_optional", "No"),
            ]
            row = [str(c).replace("|", "/") for c in row]
            out.append("| " + " | ".join(row) + " |")
            total += 1
        out.append("")

    out.append("## Generation Summary")
    out.append("")
    out.append(f"- Total distinct items in the matrix: {total}")
    out.append(f"- Cross-reference items excluded (not independent purchasing decisions): {len(cross_refs)}")
    out.append("")
    out.append("## Sourcing")
    out.append("")
    out.append(
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (authoritative), "
        "`tools/generate_procurement_execution_matrix.py`."
    )
    out.append("")
    out.append("## Changelog")
    out.append("")
    out.append(
        "**2026-08-23 (created):** Built per direct founder instruction as the "
        "single operational execution matrix, generated mechanically from the "
        "master register's existing Readiness/Sourcing classification, no new "
        "classification system introduced."
    )
    out.append("")

    OUTPUT_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {total} items.")


if __name__ == "__main__":
    main()
