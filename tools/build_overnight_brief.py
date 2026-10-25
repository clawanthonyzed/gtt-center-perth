#!/usr/bin/env python3
"""Assemble one overnight brief from a JSON spec (stdlib only). Not a calculator.

Spec keys: slug, agent, role, inputs [{label, path, start, end}], inline_inputs [{label, text}],
           deliverable {part, format, length, write_only, do_not_write}, extra_checks [str]
Usage: build_overnight_brief.py spec.json [--repo <repo root>] [--out brief.txt]
The preamble is pulled from playbooks/GTT-LOCKED-FACTS-PREAMBLE.md every time (between the BEGIN/END lines).
Template and rules: playbooks/BRIEF-TEMPLATE.md
"""
import json
import os
import re
import sys

MAX_INPUT_CHARS = 8000


def preamble(repo):
    t = open(os.path.join(repo, "playbooks", "GTT-LOCKED-FACTS-PREAMBLE.md"), encoding="utf-8").read()
    m = re.search(r"--- BEGIN PREAMBLE ---\n(.*?)\n--- END PREAMBLE ---", t, re.S)
    if not m:
        sys.exit("preamble markers not found")
    return m.group(1).strip()


def lines_of(repo, path, start, end):
    ls = open(os.path.join(repo, path), encoding="utf-8").read().splitlines()
    body = "\n".join(ls[start - 1:end])
    body = re.sub(r"\s*\[S\d+[^\]]*\]", "", body)  # repo source tags such as [S12 section 3]
    return re.sub("[✅\U0001F7E1\U0001F534]\\s*", "", body)  # status emoji


def build(spec, repo):
    out = ["OVERNIGHT_SLUG: " + spec["slug"], "", "ROLE", spec["role"], "", preamble(repo), "", "INPUTS (pasted from the repo; use only these and the locked facts)"]
    total = 0
    n = 0
    for i in spec.get("inputs", []):
        n += 1
        body = lines_of(repo, i["path"], i["start"], i["end"])
        total += len(body)
        out += [f"Input {n}: {i['label']} ({i['path']}, lines {i['start']} to {i['end']})", body, ""]
    for i in spec.get("inline_inputs", []):
        n += 1
        total += len(i["text"])
        out += [f"Input {n}: {i['label']}", i["text"], ""]
    if total > MAX_INPUT_CHARS:
        sys.exit(f"inputs are {total} characters, over the {MAX_INPUT_CHARS} limit: trim them")
    d = spec["deliverable"]
    out += ["DELIVERABLE", "Part: " + d["part"], "Format: " + d["format"], "Length: " + d["length"],
            "Write only: " + d["write_only"], "Do not write: " + d["do_not_write"], "",
            "ACCEPTANCE CHECKLIST (the draft is rejected if any is false)",
            "1. Every number comes from the locked facts or the inputs.",
            "2. No em dashes, no square brackets, no TBD, no TO CONFIRM.",
            "3. A missing fact is written as NOT IN REPO and listed once under Questions for Anthony (at most 3).",
            "4. Nothing is addressed to a real person or sent anywhere. Legal points say lawyer to check.",
            "5. The reply has the sections Summary, Deliverable and Next step for Anthony."]
    for k, c in enumerate(spec.get("extra_checks", []), 6):
        out.append(f"{k}. {c}")
    out += ["", "WHEN A FACT IS MISSING", "Write NOT IN REPO, say what is needed and who holds it, and carry on. Never guess."]
    return "\n".join(out) + "\n"


def main(a):
    if not a:
        print(__doc__)
        return 2
    repo = os.getcwd()
    outp = None
    if "--repo" in a:
        repo = a[a.index("--repo") + 1]
    if "--out" in a:
        outp = a[a.index("--out") + 1]
    spec = json.load(open(a[0], encoding="utf-8"))
    text = build(spec, repo)
    if outp:
        open(outp, "w", encoding="utf-8", newline="\n").write(text)
        print(f"wrote {outp} ({len(text)} characters)")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
