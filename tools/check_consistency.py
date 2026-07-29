"""
GTT Center Perth -- Consistency checker.

Source of truth for all canonical figures: docs/CURRENT-STATE.md.
This script does NOT re-derive figures itself -- it greps every docs/*.md file
(recursively, excluding docs/archive/) for known STALE/conflicting values of
the four tracked parameters below, and flags any line that states one of
those stale values without an accompanying staleness marker nearby (words
like "superseded", "stale", "was", "corrected", "historical", etc.) -- the
same signal a human reviewer would use to tell "this line explains history"
from "this line is quietly still wrong."

This replaces manual "conflict sweeps" (see docs/01_conflicts_log.md,
docs/00_document_inventory.md) with something that can be re-run any time a
canonical figure changes in docs/CURRENT-STATE.md.

Tracked parameters (update here AND in docs/CURRENT-STATE.md together --
this script is not authoritative, CURRENT-STATE.md is):
  1. AM GTT client capacity  (canonical: 10 clients/day)
  2. Package prices          (canonical: Package 1 = A$250, Package 2 = A$300)
  3. Monthly net P&L         (canonical: +A$25,087.07/month, steady state)
  4. Startup capital range   (canonical: UNRECONCILED -- see docs/CURRENT-STATE.md
                               §6; this script flags ANY of the 3 conflicting
                               ranges being quoted as if settled)

Exit code: 0 if no findings, 1 if any findings (usable in CI / pre-commit).
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
ARCHIVE_DIR = DOCS_DIR / "archive"

# Words that, if present anywhere in the same line (or within STALENESS_WINDOW
# lines above it), mean this is a historical/explanatory mention, not a live
# unflagged restatement -- skip it.
STALENESS_MARKERS = re.compile(
    r"superseded|stale|historical|was\s|prior|previously|corrected|correction|"
    r"flagged|archive|abandoned|old model|old figure|no longer|not.{0,15}current|"
    r"CONFLICT-|changelog|deprecated",
    re.IGNORECASE,
)
STALENESS_WINDOW = 3  # lines of preceding context also checked for a marker

# (parameter_name, canonical_value_display, [stale/conflicting regex patterns])
CHECKS = [
    (
        "AM GTT client capacity (canonical: 10 clients/day, scenario-c-sync-timetables.md)",
        "10 clients/day",
        [
            re.compile(r"\b8\s*(GTT\s+)?clients?\s*/\s*day\b", re.IGNORECASE),
            re.compile(r"\b8[\s-]client\b", re.IGNORECASE),
            re.compile(r"\b8\s+GTT\s+(patients|clients)\b", re.IGNORECASE),
            re.compile(r"176\s*(GTT\s+)?visits\s*/\s*month", re.IGNORECASE),
        ],
    ),
    (
        "Package prices (canonical: Package 1 = A$250, Package 2 = A$300 -- only 2 tiers)",
        "A$250 / A$300 (2 tiers only)",
        [
            re.compile(r"Package\s*1[^.\n]{0,20}A\$\s*200\b", re.IGNORECASE),
            re.compile(r"A\$\s*200\s*(flat|package)", re.IGNORECASE),
            re.compile(r"Package\s*3\b", re.IGNORECASE),
        ],
    ),
    (
        "Monthly net P&L, steady state (canonical: +A$25,087.07/month)",
        "+A$25,087.07/month",
        [
            re.compile(r"-\s*A\$\s*9,684"),
            re.compile(r"-\s*A\$\s*4,384"),
            re.compile(r"-\s*A\$\s*4,255"),
            re.compile(r"\+\s*A\$\s*6,663"),
            re.compile(r"\+\s*A\$\s*10,232"),
        ],
    ),
    (
        "Startup capital range (canonical: UNRECONCILED -- 3 conflicting ranges, see docs/CURRENT-STATE.md §6)",
        "UNRECONCILED (do not quote any single range as settled)",
        [
            re.compile(r"A\$\s*363,000"),
            re.compile(r"A\$\s*144,500"),
            re.compile(r"A\$\s*209,000"),
            re.compile(r"A\$\s*292,000"),
        ],
    ),
]


def has_marker(lines, idx):
    """Check line idx and the STALENESS_WINDOW lines before it for a marker."""
    start = max(0, idx - STALENESS_WINDOW)
    context = "\n".join(lines[start : idx + 1])
    return bool(STALENESS_MARKERS.search(context))


def scan_file(path):
    """Return a list of (line_no, param_name, canonical, matched_text, line_text)."""
    findings = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")
    for param_name, canonical, patterns in CHECKS:
        for i, line in enumerate(lines):
            for pat in patterns:
                m = pat.search(line)
                if m and not has_marker(lines, i):
                    findings.append((i + 1, param_name, canonical, m.group(0), line.strip()))
    return findings


def iter_docs():
    for p in sorted(DOCS_DIR.rglob("*.md")):
        if ARCHIVE_DIR in p.parents:
            continue
        yield p


def main():
    # Windows consoles default to cp1252, which can't encode some characters
    # that show up in these docs (approx signs, em-dashes, etc). Force UTF-8
    # with replacement so the script never crashes on output alone.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    if not DOCS_DIR.exists():
        print(f"ERROR: {DOCS_DIR} not found -- run from repo root.")
        return 2

    total_findings = 0
    files_with_findings = 0

    for path in iter_docs():
        findings = scan_file(path)
        if not findings:
            continue
        files_with_findings += 1
        rel = path.relative_to(REPO_ROOT)
        print(f"\n{rel}")
        for line_no, param_name, canonical, matched, line_text in findings:
            total_findings += 1
            print(f"  L{line_no}: possible stale value for [{param_name}]")
            print(f"       canonical: {canonical}")
            print(f"       found:     '{matched}'  -- {line_text[:120]}")

    print("\n" + "=" * 72)
    if total_findings == 0:
        print("check_consistency: 0 findings across all docs/*.md (excluding archive/).")
        print("All tracked figures consistent with docs/CURRENT-STATE.md.")
        return 0
    else:
        print(
            f"check_consistency: {total_findings} possible stale value(s) "
            f"across {files_with_findings} file(s)."
        )
        print(
            "Each finding is a line containing a known-stale figure with no "
            "staleness marker nearby -- review manually, this is a grep-based "
            "sweep, not a semantic parser. False positives are possible "
            "(e.g. a legitimate new sentence that happens to contain '250' "
            "near unrelated text)."
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
