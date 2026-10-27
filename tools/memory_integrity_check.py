#!/usr/bin/env python3
"""GTT memory integrity check (standard library only).

Reads docs/GTT-READ-FIRST.md and docs/FINANCIAL-CENTER-OF-TRUTH.md and checks that the headline
numbers and key locks are still there and still say what Anthony locked. It does no maths.
Exit 0 = all good. Exit 1 = something went missing or changed (each failure is printed in plain words).
Exit 2 = a rulebook file could not be found.

Usage: python tools/memory_integrity_check.py [--repo path/to/gtt-center-perth]
Run it before handing over work, and after anyone edits GTT-READ-FIRST.md or the Center of Truth.
"""
import os
import re
import sys

I = re.I | re.S
# (label, file key, regex). file key: "rf" = GTT-READ-FIRST.md, "cot" = FINANCIAL-CENTER-OF-TRUTH.md
CHECKS = [
    ("Profit before company tax A$26,631.97", "rf", r"A\$26,631\.97"),
    ("Profit before company tax A$26,631.97 (Center of Truth)", "cot", r"26,631\.97"),
    ("Profit after company tax A$19,973.98", "rf", r"A\$19,973\.98"),
    ("Profit after company tax A$19,973.98 (Center of Truth)", "cot", r"19,973\.98"),
    ("Path A package 1 GTT charge A$292.15", "rf", r"A\$292\.15"),
    ("Path A package 2 GTT charge A$342.15", "rf", r"A\$342\.15"),
    ("Path B package 1 GTT charge A$272.15", "rf", r"A\$272\.15"),
    ("Path B package 2 GTT charge A$322.15", "rf", r"A\$322\.15"),
    ("Venue manager starts 06:30", "rf", r"venue manager starts 06:30"),
    ("Venue manager 06:30 (Center of Truth)", "cot", r"venue manager[^|\n]{0,80}06:30|06:30[^|\n]{0,80}venue manager"),
    ("Midwives work 08:00 to 16:00", "rf", r"midwives work 08:00 to 16:00"),
    ("18 clients a morning", "rf", r"18 clients a (?:morning|day)"),
    ("Path A means the package WITH the GTT midwife consult, preferred", "rf", r"Path A = PREFERRED:[^\n]{0,40}WITH the GTT midwife consult"),
    ("Path B means an OUTSIDE referral, no GTT consult, not preferred", "rf", r"Path B = NOT preferred:[^\n]{0,60}OUTSIDE referral[^\n]{0,30}no GTT consult"),
    ("Path B is not limited", "rf", r"PATH B IS NOT LIMITED"),
    ("Lab request window 8 weeks", "rf", r"Lab request validity window:\s*8 weeks"),
    ("Consult late grace 10 minutes", "rf", r"10 minute grace"),
    ("Blood draws have no wiggle room", "rf", r"no wiggle room"),
    ("Phlebotomists employed by GTT Medical", "rf", r"Phlebotomists are employed by GTT MEDICAL"),
    ("Anthony is owner and director, 0 operational hours", "rf", r"OWNER and DIRECTOR[^\n]{0,200}0 operational hours"),
    ("Three companies, not a trust", "rf", r"Three companies: Holdings, Medical, Lounge\. Not a trust"),
    ("No revenue ramp", "rf", r"No revenue ramp-up"),
    ("Midwives are never recalled from a break", "rf", r"Midwives are NEVER recalled"),
    ("Rebates A$55.00 (consult A$32.95 + lab A$22.05)", "rf", r"A\$32\.95[^\n]{0,120}A\$22\.05[^\n]{0,60}A\$55\.00"),
    ("Government emails: Draft D retired", "rf", r"Draft D is RETIRED"),
]


def main(argv):
    repo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    if "--repo" in argv:
        repo = argv[argv.index("--repo") + 1]
    paths = {
        "rf": os.path.join(repo, "docs", "GTT-READ-FIRST.md"),
        "cot": os.path.join(repo, "docs", "FINANCIAL-CENTER-OF-TRUTH.md"),
    }
    texts = {}
    for key, p in paths.items():
        if not os.path.isfile(p):
            print("memory_integrity_check: cannot find " + p)
            return 2
        with open(p, encoding="utf-8", errors="replace") as fh:
            texts[key] = fh.read()
    failed = []
    for label, key, rx in CHECKS:
        if not re.search(rx, texts[key], I):
            failed.append((label, os.path.basename(paths[key])))
    if failed:
        print("MEMORY INTEGRITY CHECK FAILED: %d of %d locked facts are missing or changed." % (len(failed), len(CHECKS)))
        for label, fn in failed:
            print("  MISSING in %s: %s" % (fn, label))
        print("Fix: restore the fact from git history (git log -p docs/GTT-READ-FIRST.md). Do not rewrite a locked fact without Anthony's say.")
        return 1
    print("memory integrity OK: %d of %d locked facts present in GTT-READ-FIRST.md and FINANCIAL-CENTER-OF-TRUTH.md." % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
