#!/usr/bin/env python3
"""Check overnight GTT drafts for thin, wrong or missing output (standard library only).

Run on the server after the queue has finished:
  python3 validate_overnight_output.py --glob "/opt/openclaw/second-brain/overnight/gtt-r25-*" \
      --specs /opt/openclaw/overnight/r25/specs [--report /opt/openclaw/overnight/r25/VALIDATION.md]

For every spec (one JSON per brief) it finds the newest .md output in the matching overnight folder and checks:
  MISSING   no output file
  THIN      shorter than the minimum stated in the spec length (the first number, e.g. "2,000 to 3,000 characters")
  LONG      more than 1.6 times the maximum
  HEADINGS  fewer numbered headings found than the spec lists
  STALE     contains a known stale or banned phrase (Anthony as venue manager, DVA/SRDP, ramp, midwife chooses break,
            venue manager 07:00, square brackets, TBD, slash commands, em dash)
Exit code 0 when every draft passes, 1 when any fails. Writes a Markdown report. Nothing is changed or sent.
"""
import argparse, glob, json, os, re, sys

STALE = [
    (r"Anthony[^.\n|]{0,40}\b(?:is|as|acts as|will be)\b[^.\n|]{0,20}venue manager", "Anthony as venue manager"),
    (r"\b(?:DVA|SRDP|MRCA)\b", "DVA / SRDP / MRCA"),
    (r"revenue ramp|ramp[- ]?up", "ramp"),
    (r"midwife\s+(?:chooses|can choose)\s+(?:the |her )?(?:meal )?break", "midwife chooses break"),
    (r"venue manager[^.\n|]{0,30}(?:start|arriv|open|begin)\w*[^.\n|]{0,15}\b07:00\b", "venue manager 07:00"),
    (r"\[[^\]\n]{1,60}\]", "square brackets"),
    (r"\bTBD\b|\bTO CONFIRM\b", "placeholder"),
    (r"(?m)^\s*/[a-z][a-z-]+(?:\s|$)", "slash command"),
    (r"—", "em dash"),
    (r"(?<!expecting )\bmothers?\b", "bare word mother"),
]


def num(s):
    return int(s.replace(",", ""))


def length_bounds(text):
    m = re.search(r"([\d,]+)\s+to\s+([\d,]+)\s+characters", text or "")
    return (num(m.group(1)), num(m.group(2))) if m else (800, 9000)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", required=True, help="overnight output folder pattern, e.g. /opt/.../gtt-r25-*")
    ap.add_argument("--specs", required=True, help="folder of spec JSON files")
    ap.add_argument("--report", default="")
    a = ap.parse_args()
    folders = {os.path.basename(p): p for p in glob.glob(a.glob)}
    rows, bad = [], 0
    for sp in sorted(glob.glob(os.path.join(a.specs, "*.json"))):
        spec = json.load(open(sp, encoding="utf-8"))
        slug = spec["slug"]
        lo, hi = length_bounds(spec["deliverable"].get("length", ""))
        want_heads = len(re.findall(r"(?:^|,\s)(\d{1,2})\s", spec["deliverable"].get("write_only", "")))
        cands = [d for n, d in folders.items() if slug in n]
        files = []
        for d in cands:
            files += glob.glob(os.path.join(d, "*.md"))
        if not files:
            rows.append((slug, "MISSING", 0, "no output file")); bad += 1; continue
        f = max(files, key=os.path.getmtime)
        t = open(f, encoding="utf-8", errors="replace").read()
        body = t.split("---", 2)[-1] if t.startswith("---") else t
        n = len(body.strip())
        problems = []
        if n < lo:
            problems.append(f"THIN ({n} < {lo})")
        if n > hi * 1.6:
            problems.append(f"LONG ({n})")
        heads = len(re.findall(r"(?m)^\s*(?:#+\s*)?\**\s*\d{1,2}[.)]?\s+\S", body))
        if want_heads and heads < min(want_heads, 3):
            problems.append(f"HEADINGS ({heads})")
        for pat, why in STALE:
            if re.search(pat, body, re.I if why not in ("em dash",) else 0):
                problems.append("STALE: " + why)
        if problems:
            bad += 1
        rows.append((slug, "FAIL" if problems else "PASS", n, "; ".join(problems) or os.path.basename(f)))
    out = ["# Overnight validation", "", "| Draft | Result | Characters | Notes |", "|---|---|---|---|"]
    out += [f"| {s} | {r} | {n} | {note} |" for s, r, n, note in rows]
    out += ["", f"{len(rows) - bad} pass, {bad} fail."]
    text = "\n".join(out) + "\n"
    print(text)
    if a.report:
        open(a.report, "w", encoding="utf-8").write(text)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
