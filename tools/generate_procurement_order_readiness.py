"""
Generates docs/architecture/PROCUREMENT-ORDER-READINESS-CHECKLIST.md: the
"can we actually buy this today" view (Part 4), splitting all 281 items into
the 8 Readiness categories (A-H, already assigned in the master register)
and showing, per item: ID, item, quantity, supplier route, specification
completeness, blocking issue, next action, person responsible, and a plain
Y/N on whether it can be purchased right now. Reuses the same parser and
derivation rules as the full item specification (Part 1), no second,
conflicting status system is introduced.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from procurement_register_parser import parse_register
from procurement_derivations import derive, readiness_letter

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "architecture" / "PROCUREMENT-ORDER-READINESS-CHECKLIST.md"

READINESS_SECTION_TITLES = {
    "A": "A. Order Now",
    "B": "B. Request Quote Now",
    "C": "C. Wait For Venue",
    "D": "D. Professional Verification Required",
    "E": "E. WDP Confirmation Required",
    "F": "F. Founder Decision Required",
    "G": "G. Information Required",
    "H": "H. Future/Optional",
}

SPEC_COMPLETENESS = {
    "LOCKED": "Complete: quantity and specification are locked",
    "CALCULATED": "Complete: quantity and specification are locked",
    "CONSUMPTION-DEPENDENT": "Complete: specification locked, quantity is an ongoing consumable figure",
    "SITE-DEPENDENT": "Partial: specification exists, exact quantity/dimensions pending a confirmed site",
    "PROFESSIONAL-VERIFICATION": "Partial: specification exists, pending professional sign-off",
    "WDP-DEPENDENT": "Partial: specification exists, pending WDP confirmation",
    "FOUNDER-DECISION": "Incomplete: pending a founder decision",
    "STAFF-DEPENDENT": "Partial: specification exists, exact quantity pending confirmed headcount",
    "OPTIONAL": "Complete but deferred: this is an optional item, not being actioned now",
}


def main():
    items, cross_refs, headings = parse_register()

    by_letter = {k: [] for k in READINESS_SECTION_TITLES}
    for item in items:
        letter = readiness_letter(item.get("readiness", ""))
        if letter in by_letter:
            by_letter[letter].append(derive(item))

    out = []
    out.append("# Procurement Order Readiness Checklist")
    out.append("")
    out.append(
        "Status: current as of 2026-08-23. Answers \"what can we actually buy "
        "today\" for all 281 distinct items, generated mechanically by "
        "`tools/generate_procurement_order_readiness.py` from "
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`'s own existing "
        "Readiness classification (A-H). This is not a second, conflicting "
        "status system, it is the same classification already assigned in "
        "the master register, presented as a purchasing decision view. "
        "Re-run the generator if the register changes; do not hand-edit this "
        "file directly."
    )
    out.append("")
    out.append(
        "**No purchase, RFQ, or supplier/agent contact has been made.** This "
        "document states what is ready, not what has been ordered."
    )
    out.append("")

    total = 0
    counts = {}
    for letter, title in READINESS_SECTION_TITLES.items():
        section_items = by_letter[letter]
        counts[letter] = len(section_items)
        total += len(section_items)
        out.append(f"## {title} ({len(section_items)} items)")
        out.append("")
        out.append("| Item ID | Item | Quantity | Supplier route | Specification completeness | Blocking issue | Next action | Person responsible | Can purchase now? |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        can_purchase = "Yes" if letter == "A" else "No"
        for full in section_items:
            spec_completeness = SPEC_COMPLETENESS.get(full.get("quantity_basis", ""), "Not yet determined")
            quantity_text = (full.get("quantity") or "").lower()
            if "to be determined" in quantity_text or "depends on" in quantity_text:
                spec_completeness = "Partial: item and unit price can be quoted, but the exact quantity itself is not yet fixed (see the Quantity column)"
            row = [
                full["id"],
                full["item"],
                full.get("quantity", "N/A"),
                full.get("preferred_channel", "Not yet determined"),
                spec_completeness,
                full.get("still_required", "Not yet determined"),
                full.get("final_instruction", "Not yet determined"),
                full.get("who_confirms", "Not yet determined"),
                can_purchase,
            ]
            # Escape pipe characters defensively so the table never breaks
            row = [str(c).replace("|", "/") for c in row]
            out.append("| " + " | ".join(row) + " |")
        out.append("")

    out.append("## Summary Counts")
    out.append("")
    out.append("| Category | Count |")
    out.append("|---|---|")
    for letter, title in READINESS_SECTION_TITLES.items():
        out.append(f"| {title} | {counts[letter]} |")
    out.append(f"| **Total distinct items** | **{total}** |")
    out.append("")
    if total != 281:
        out.append(f"**WARNING: total does not equal 281 (got {total}). Investigate before relying on this document.**")
        out.append("")

    out.append("## Sourcing")
    out.append("")
    out.append(
        "`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (authoritative "
        "Readiness classification), `docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md` "
        "(full per-item detail), `tools/generate_procurement_order_readiness.py`."
    )
    out.append("")
    out.append("## Changelog")
    out.append("")
    out.append(
        "**2026-08-23 (created):** Built per direct founder instruction (Part 4) "
        "as the \"can I order this\" purchasing decision view, generated "
        "mechanically from the master register's own existing Readiness "
        "classification, not a new or conflicting status system."
    )
    out.append("")

    OUTPUT_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}. Total items: {total}. Counts: {counts}")


if __name__ == "__main__":
    main()
