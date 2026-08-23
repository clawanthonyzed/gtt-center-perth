"""
GTT Center Perth -- Procurement field derivation rules.

Turns the 19 raw register columns (see procurement_register_parser.py) into
the ~42 fields the founder's specification requires, by mechanical rule
only. Nothing here invents a specification, quantity, price, dimension,
material, or supplier name that is not already present somewhere in the
register row's own text. Where no repository basis exists, the derivation
returns an explicit "Not yet determined" (or the item-specific reason why),
never a plausible-looking guess.
"""

import re

KNOWN_SUPPLIER_BRANDS = [
    "Sunflower Medical", "Alphatec Australia", "Ultramedic", "Daniels Health",
    "Cleanaway Medical", "Stericycle", "Hettich Universal 320R",
    "Thermo Scientific CL10", "Thermo Scientific", "Hettich", "Dyson", "GHD",
    "Cloud Nine", "Zebra ZD420", "Zebra", "Ubiquiti", "TP-Link",
    "National Salon Supplies", "Salon Supply Australia", "Diamond Nail Supplies",
    "American Beauty Supply", "The Salon Furniture Hub", "St John Ambulance WA",
]

MATERIAL_KEYWORDS = [
    "vinyl", "stainless", "ceramic", "timber", "laminate", "glass", "fabric",
    "nitrile", "cotton",
]

FINISH_KEYWORDS = [
    "wipe-clean", "matte", "gloss", "lighted", "LED", "brushed", "powder-free",
]

DIMENSION_RE = re.compile(r'\d[\d,]*\s?(mm|cm)\b', re.IGNORECASE)

SOURCING_LABELS = {
    "CN": "China",
    "AU": "Australia only",
    "HY": "Hybrid (China or Australia, either works)",
    "PRO": "Professional/clinical procurement channel",
    "WDP": "WDP relationship, not general retail",
    "SITE": "Site-dependent, not a shippable product",
}

PREFERRED_CHANNEL = {
    "CN": "China sourcing group, see PROCUREMENT-CHINA-PACKAGE.md",
    "AU": "Australian retail/commercial supplier, see PROCUREMENT-AUSTRALIA-PACKAGE.md",
    "HY": "Either Australian or China sourcing group, whichever quote is better once both exist",
    "PRO": "Named professional/clinical equipment channel, see PROCUREMENT-AUSTRALIA-PACKAGE.md Specialist Clinical Suppliers",
    "WDP": "Pathology partner (WDP) arranged, not an open-market purchase",
    "SITE": "Licensed trade/contractor, engaged once the venue is confirmed",
}

READINESS_TEMPLATES = {
    "A": {
        "still_required": "Nothing outstanding. Specification and quantity are locked and a price has already been researched.",
        "who_confirms": "No further confirmation needed. Venue Manager (once hired) or Anthony can place the order.",
        "instruction": "Order now from the recommended sourcing route.",
    },
    "B": {
        "still_required": "A real supplier quote (RFQ). Specification and quantity are locked but no price/quote has been obtained yet.",
        "who_confirms": "Venue Manager (once hired) or Anthony, to request and compare quotes.",
        "instruction": "Do not order yet. Request quotes from the recommended sourcing route, compare them, then order.",
    },
    "C": {
        "still_required": "Site measurement and confirmation once a venue is secured. Exact dimensions/installation cannot be finalised before then.",
        "who_confirms": "Whoever measures the confirmed site (Venue Manager, builder, or Anthony), per PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md.",
        "instruction": "Do not order yet. Wait until the venue is secured and measured, then proceed to RFQ.",
    },
    "D": {
        "still_required": "Sign-off from the relevant licensed Australian professional named in the Compliance/Verification field.",
        "who_confirms": "The specific licensed professional named in the Compliance/Verification field, engaged once the venue is confirmed.",
        "instruction": "Do not order yet. Obtain the required professional verification, then proceed to RFQ or order.",
    },
    "E": {
        "still_required": "Confirmation from the pathology partner (WDP) on their own supply/commercial arrangement for this item.",
        "who_confirms": "WDP, via Reed's partnership channel, not this venture directly.",
        "instruction": "Do not order yet. Wait for WDP's confirmation before taking any procurement action on this item.",
    },
    "F": {
        "still_required": "A specific founder decision. See PROCUREMENT-FOUNDER-DECISIONS.md for the exact decision this item depends on.",
        "who_confirms": "Anthony.",
        "instruction": "Do not order yet. This item is blocked on a founder decision, not a supplier or site issue.",
    },
    "G": {
        "still_required": "A specific, named information gap (see the item's own register note), not a vague research task.",
        "who_confirms": "Depends on the specific gap; usually the Venue Manager once hired, or Anthony in the interim.",
        "instruction": "Do not order yet. Resolve the specific information gap noted in the register first.",
    },
    "H": {
        "still_required": "Nothing required now. This item is deferred until after opening and revisited against actual trading performance.",
        "who_confirms": "Anthony, if and when reconsidered post-opening.",
        "instruction": "Do not order now. Revisit after opening if actual demand supports it.",
    },
}


def readiness_letter(readiness_field):
    if not readiness_field:
        return None
    m = re.match(r'([A-H])\.', readiness_field.strip())
    return m.group(1) if m else None


def find_keyword(text, keywords):
    if not text:
        return None
    lower = text.lower()
    hits = [k for k in keywords if k.lower() in lower]
    return ", ".join(hits) if hits else None


def find_supplier_brand(*texts):
    combined = " ".join(t for t in texts if t)
    hits = [b for b in KNOWN_SUPPLIER_BRANDS if b in combined]
    return ", ".join(dict.fromkeys(hits)) if hits else None


def derive(item):
    """Takes a parsed item dict (19 register fields) and returns a dict of
    all additional derived fields, plus the raw fields passed through."""
    d = dict(item)

    letter = readiness_letter(item.get("readiness", ""))
    sourcing = (item.get("sourcing") or "").strip()
    description = item.get("description", "")
    notes = item.get("notes", "")
    compliance = item.get("compliance", "")
    category = item.get("category", "")
    venue_dependent = (item.get("venue_dependent") or "").strip().lower().startswith("yes")
    status = item.get("status", "")

    combined_text = " ".join([description, notes, compliance])

    # 11/12. Required at opening / future-optional
    if letter == "H":
        d["required_at_opening"] = "No (future/optional)"
        d["future_optional"] = "Yes"
    elif letter == "F":
        d["required_at_opening"] = "Blocked pending founder decision, see field 40 (what is still required)"
        d["future_optional"] = "No"
    else:
        d["required_at_opening"] = "Yes"
        d["future_optional"] = "No"

    # 16. China/Australia classification
    d["china_australia_classification"] = SOURCING_LABELS.get(sourcing, "Not yet determined, sourcing route not classified in the register")

    # 17. Preferred procurement channel
    d["preferred_channel"] = PREFERRED_CHANNEL.get(sourcing, "Not yet determined")

    # 18. Supplier type
    brand = find_supplier_brand(notes, compliance, description)
    d["supplier_type"] = brand if brand else f"Not yet determined. No specific supplier identified in the register for this {category} item."

    # 20. Dimensions
    dim_match = DIMENSION_RE.search(combined_text)
    d["dimensions"] = dim_match.group(0) if dim_match else "Not yet determined. Depends on the final floor plan and/or the specific product selected at quote stage."

    # 21. Material
    material = find_keyword(combined_text, MATERIAL_KEYWORDS)
    d["material"] = material if material else "Not yet determined"

    # 22. Finish
    finish = find_keyword(combined_text, FINISH_KEYWORDS)
    d["finish"] = finish if finish else "Not yet determined"

    # 23. Colour/brand
    if "palette" in combined_text.lower() or "locked palette" in combined_text.lower():
        d["colour_brand"] = "Matches the locked 7-colour palette (outputs/brand/warm-stone-tokens.css)"
    elif brand:
        d["colour_brand"] = brand
    else:
        d["colour_brand"] = "Not yet determined"

    # 24. Performance requirements
    d["performance_requirements"] = description if description else "N/A"

    # 25. Electrical
    if re.search(r'electrical|SAA|GPO|wired|electric', combined_text, re.IGNORECASE):
        d["electrical_requirements"] = compliance if compliance and re.search(r'electrical|SAA|GPO|wired', compliance, re.IGNORECASE) else "Electrical component present, confirm Australian electrical safety mark (SAA) before purchase"
    else:
        d["electrical_requirements"] = "N/A"

    # 26. Plumbing
    if re.search(r'water|drain|plumb|tap\b|basin|sink', combined_text, re.IGNORECASE):
        d["plumbing_requirements"] = "Yes, licensed plumber required" if venue_dependent else compliance if compliance else "Water supply/drainage involved, confirm exact requirement with a licensed plumber"
    else:
        d["plumbing_requirements"] = "N/A"

    # 27. HVAC/ventilation
    if re.search(r'\bACH\b|ventilation|\bLEV\b|HVAC', combined_text, re.IGNORECASE):
        d["hvac_ventilation_requirements"] = compliance if compliance else "Ventilation requirement applies, see the item's own specification"
    else:
        d["hvac_ventilation_requirements"] = "N/A"

    # 28. Clinical
    if category == "Blood Collection" or re.search(r'NATA|AS/NZS 239|clinical|phlebotom', combined_text, re.IGNORECASE):
        d["clinical_requirements"] = compliance if compliance else "Clinical requirement applies"
    else:
        d["clinical_requirements"] = "N/A"

    # 29. Food-safety
    if category == "Cafe":
        d["food_safety_requirements"] = compliance if compliance else "WA Food Business Notification and food-safety storage/handling standards apply"
    else:
        d["food_safety_requirements"] = "N/A"

    # 30. Accessibility
    if category == "Toilets" or re.search(r'AS 1428', combined_text):
        d["accessibility_requirements"] = compliance if compliance else "Accessibility compliance applies, AS 1428.1"
    else:
        d["accessibility_requirements"] = "N/A"

    # 31. Certification/compliance (reuse the register's own field, already exists)
    d["certification_compliance"] = compliance if compliance else "None identified"

    # 32. Installation
    if venue_dependent:
        d["installation_requirements"] = "Yes, site-dependent install required by a licensed trade"
    elif re.search(r'site-installed|custom|install', combined_text, re.IGNORECASE):
        d["installation_requirements"] = "Yes, installation required"
    else:
        d["installation_requirements"] = "No, freestanding/portable, no installation required"

    # 33. Delivery
    delivery_map = {
        "CN": "Container/consolidated freight from China. Delivery timing depends on production and shipping lead time, not yet quoted.",
        "AU": "Standard Australian courier/freight delivery, not yet quoted.",
        "HY": "Standard Australian courier/freight delivery if Australian-sourced, or container/consolidated freight if China-sourced, not yet quoted.",
        "PRO": "Standard Australian courier/freight delivery via the named professional channel, not yet quoted.",
        "WDP": "Arranged via WDP, not a standard commercial delivery.",
        "SITE": "Not applicable. This is a site-installed item or trade service, not a shipped product.",
    }
    d["delivery_requirements"] = delivery_map.get(sourcing, "Not yet determined")

    # 34. Assembly
    if sourcing in ("SITE", "WDP", "PRO"):
        d["assembly_requirements"] = "N/A"
    else:
        d["assembly_requirements"] = "Not yet determined. Confirm with the selected supplier at quote stage; no assembly information exists in this repository for any item."

    # 35. Warranty
    if sourcing in ("SITE", "WDP"):
        d["warranty_requirements"] = "N/A, not a standard commercial purchase"
    else:
        d["warranty_requirements"] = "Not yet determined. No warranty term has been confirmed for any item in this register; must be obtained at quote stage, per the genuine gap already disclosed in PROCUREMENT-CHINA-PACKAGE.md."

    # 36. QC requirements
    china_candidate = (item.get("china_candidate") or "").strip().lower()
    if sourcing == "CN" or china_candidate.startswith("yes") or china_candidate.startswith("possible"):
        d["qc_requirements"] = "See PROCUREMENT-CHINA-PACKAGE.md: factory specification confirmation, material/finish sample, pre-production approval, and independent pre-shipment inspection required before any order, if sourced from China."
    else:
        d["qc_requirements"] = "N/A, standard Australian retail/commercial purchase, no factory QC process required."

    # 37. Quote/RFQ requirements
    rfq_map = {
        "A": "No, already priced, ready to order.",
        "B": "Yes, RFQ/quote required.",
        "C": "Not yet. Site measurement required first, then RFQ.",
        "D": "Not yet. Professional verification required first.",
        "E": "Not yet. WDP confirmation required first.",
        "F": "Not yet. Founder decision required first.",
        "G": "Not yet. Information gap must be resolved first.",
        "H": "No, future/optional, not being actioned now.",
    }
    d["quote_rfq_required"] = rfq_map.get(letter, "Not yet determined")

    # 38. Existing price/source
    if status == "Priced" and notes:
        d["existing_price_source"] = f"{notes} (sourced from this repository's existing research, not an independently obtained quote)"
    else:
        d["existing_price_source"] = "No price researched yet"

    # 39. Cost status
    d["cost_status"] = status if status else "Not yet determined"

    # 40/41/42. Readiness-driven templates, plus the item's own literal note
    template = READINESS_TEMPLATES.get(letter, {
        "still_required": "Not yet determined, readiness classification missing.",
        "who_confirms": "Not yet determined.",
        "instruction": "Not yet determined.",
    })
    still_required = template["still_required"]

    # Genuine edge case: a small number of RFQ-ready (B) items have a
    # Quantity field that itself reads "to be determined" or "depends on"
    # something site-dependent (e.g. toilet-count-dependent consumables,
    # opening-stock-policy-dependent spares). The item and its unit price
    # can still be quoted, but the generic "B" template's "quantity are
    # locked" framing would misstate this specific item, so it is corrected
    # here rather than left inaccurate.
    quantity_text = (item.get("quantity") or "").lower()
    if letter == "B" and ("to be determined" in quantity_text or "depends on" in quantity_text):
        still_required = (
            "A real supplier quote (RFQ) for the item and unit price. The exact "
            "quantity itself is not yet fixed, it depends on a factor stated in "
            "the register's own Quantity field (see field 6 above), not just on "
            "obtaining a quote."
        )

    d["still_required"] = still_required
    d["who_confirms"] = template["who_confirms"]
    d["final_instruction"] = template["instruction"]
    d["register_note"] = notes if notes else "None"

    return d
