#!/usr/bin/env python3
"""Pre-generation / pre-send fact check for GTT Center Perth drafts (stdlib only).

NOT a financial calculator. It does no arithmetic. It only scans a text, markdown or HTML file for
(1) the banned stale values listed in section 8 of docs/FINANCIAL-CENTER-OF-TRUTH.md (written by
Theodore R19, theodore_r19.py), (2) a few extra stale patterns found in the overnight drafts of
2026-10-24 (old cadence, 07:00 venue manager, bulk billing talk), and (3) em dashes.

Usage:   python3 factcheck_locked_facts.py <file> [<file> ...] [--truth path/to/FINANCIAL-CENTER-OF-TRUTH.md]
Exit:    0 = clean, 1 = at least one hit (file:line and reason printed), 2 = usage or setup error.

Allowances (so the checklist files can name the banned values without failing):
  * a markdown table row whose FIRST cell is a banned value is an "error table" row and is skipped;
  * a line containing the marker  factcheck:ok  is skipped (use only on lines that quote a banned value
    on purpose, for example in a rule such as "no hosts").
Em dashes are never allowed, marker or not.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TRUTH_CANDIDATES = [
    os.path.join(HERE, "..", "docs", "FINANCIAL-CENTER-OF-TRUTH.md"),
    "/opt/openclaw/second-brain/knowledge/gtt-playbooks/FINANCIAL-CENTER-OF-TRUTH.md",
]
EM_DASH = "—"
OK_MARKER = "factcheck:ok"

# Extra patterns that are not single literal values in the Center of Truth table.
EXTRA = [
    (r"\b12[- ]?min(?:ute)?s?\b[^.\n]{0,30}(?:cadence|stagger|pair|apart|gap)|(?:cadence|stagger|pair)[^.\n]{0,30}\b12[- ]?min(?:ute)?s?\b",
     "12-minute cadence is retired. The repo cadence is 25-minute pairs"),
    (r"venue manager[^.\n|]{0,30}(?:start|arriv|open|begin|in at)\w*[^.\n|]{0,15}\b07:00\b",
     "venue manager starts 06:30; 07:00 is the first draw"),
    (r"\bbulk[- ]?bill", "no bulk billing talk (Structure B: private all-inclusive, mother claims the rebate)"),
    (r"\b82110\b(?![^.\n]{0,60}40)", "item 82110 is the 40-minute consult; GTT uses 82105 (20 minutes)"),
    (r"\bsonographer", "no sonographers in the GTT roster"),
    (r"\b21:00\b|\b2100\b|\b9 ?pm\b", "services finish and doors shut by 18:00; no 21:00 close"),
]


def find_truth(explicit):
    for p in ([explicit] if explicit else TRUTH_CANDIDATES):
        if p and os.path.isfile(p):
            return os.path.normpath(p)
    return None


def load_banned(truth_path):
    """Return list of (compiled_regex, literal_token) from the 'Banned stale values' table (first column)."""
    text = open(truth_path, encoding="utf-8").read()
    m = re.search(r"(?im)^##\s*\d*\.?\s*Banned stale values.*$", text)
    if not m:
        raise ValueError("no 'Banned stale values' heading in " + truth_path)
    section = text[m.end():]
    nxt = re.search(r"(?m)^##\s", section)
    section = section[:nxt.start()] if nxt else section
    tokens = []
    for line in section.splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*-", line) or re.match(r"^\|\s*Banned\s*\|", line):
            continue
        first = line.strip().strip("|").split("|")[0].strip()
        for tok in [t.strip() for t in first.split(" / ")]:
            if tok:
                tokens.append(tok)
    if not tokens:
        raise ValueError("banned table is empty in " + truth_path)
    out = []
    for tok in tokens:
        body = re.escape(tok)
        body = body.replace(r"\ ", r"\s+")
        if tok.startswith("A$"):
            body = r"A?\$" + body[len(re.escape("A$")):]
            pre = r"(?<![\w.,])"
        else:
            pre = r"\b" if re.match(r"\w", tok) else ""
        post = r"\b" if re.search(r"\w$", tok) else ""
        if re.search(r"\d$", tok):
            post = r"(?![\d,]*\d)"
        if tok.lower() == "hosts":
            body, post = r"hosts?", r"\b"
        out.append((re.compile(pre + body + post, re.I), tok))
    return out


def strip_html(line):
    return re.sub(r"<[^>]+>", " ", line)


def scan(path, banned):
    hits = []
    is_html = path.lower().endswith((".html", ".htm"))
    banned_firsts = {tok.lower() for _, tok in banned}
    with open(path, encoding="utf-8", errors="replace") as fh:
        for n, raw in enumerate(fh, 1):
            if EM_DASH in raw:
                hits.append((n, "em dash", raw.strip()[:110]))
            if OK_MARKER in raw:
                continue
            line = strip_html(raw) if is_html else raw
            if line.lstrip().startswith("|"):
                first = line.strip().strip("|").split("|")[0].strip().lower()
                if any(first == t or first.replace("**", "") == t for t in banned_firsts) or \
                   any(part.strip() in banned_firsts for part in first.split(" / ")):
                    continue
            if re.search(r"(?<!expecting )mothers?", line, re.I):
                hits.append((n, "terminology: say client or expecting mother", raw.strip()[:110]))
            for rx, tok in banned:
                if rx.search(line):
                    hits.append((n, "banned stale value: " + tok, raw.strip()[:110]))
            for pat, why in EXTRA:
                if re.search(pat, line, re.I):
                    hits.append((n, "stale pattern: " + why, raw.strip()[:110]))
    return hits


def main(argv):
    files, truth = [], None
    i = 0
    while i < len(argv):
        if argv[i] == "--truth" and i + 1 < len(argv):
            truth = argv[i + 1]
            i += 2
        else:
            files.append(argv[i])
            i += 1
    if not files:
        print(__doc__)
        return 2
    tp = find_truth(truth)
    if not tp:
        print("factcheck: cannot find FINANCIAL-CENTER-OF-TRUTH.md (use --truth)")
        return 2
    try:
        banned = load_banned(tp)
    except Exception as e:
        print("factcheck: " + str(e))
        return 2
    total = 0
    for f in files:
        if not os.path.isfile(f):
            print("factcheck: no such file " + f)
            return 2
        hits = scan(f, banned)
        for n, why, snip in hits:
            print(f"{f}:{n}: {why} | {snip}")
        total += len(hits)
    print(f"factcheck: {total} problem(s) in {len(files)} file(s); {len(banned)} banned values loaded from {os.path.basename(tp)}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
