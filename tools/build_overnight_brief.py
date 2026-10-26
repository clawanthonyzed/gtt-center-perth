#!/usr/bin/env python3
"""Assemble overnight briefs from JSON specs (stdlib only). Not a calculator.

HARD RULE: a brief is at most 8,000 characters. The builder refuses to write one that is longer.

Spec keys: slug, agent, role, facts [topic ids] (or "all"), inputs [{label, path, start, end}],
           inline_inputs [{label, text}], deliverable {part, format, length, write_only, do_not_write},
           extra_checks [str], parts [part spec, ...]
Facts: playbooks/GTT-LOCKED-FACTS-PREAMBLE.md tags every line "@topic-id text". Every "@core-*" line goes into every
       brief (the builder fails if the core is over 1,200 characters). A spec adds only the topic ids it lists in
       "facts". Omitting "facts" pastes every line (the whole brief must still fit in 8,000 characters).
Parts: "parts" is a list of part specs. Each part inherits slug (as <slug>-p1, <slug>-p2), agent, role, facts and
       extra_checks from the parent unless it sets its own; deliverable, inputs and inline_inputs are the part's own.
       Every part is a complete brief and is checked on its own.
Usage:
  build_overnight_brief.py spec.json [--repo <repo root>] [--out brief.txt]   one spec (parts become brief-p1.txt ...)
  build_overnight_brief.py --specs <dir> --outdir <dir> [--repo <repo root>]  every *.json in the dir; prints a table
Exit: 0 all briefs built, 1 a brief or the core is over its limit (nothing is written for that spec), 2 usage or setup error.
Template and rules: playbooks/BRIEF-TEMPLATE.md
"""
import glob
import json
import os
import re
import sys

MAX_BRIEF_CHARS = 8000   # Anthony's rule: any task over 8,000 characters must be split into parts
MAX_CORE_CHARS = 1200    # all @core-* lines together
MAX_INPUT_CHARS = 8000   # a ceiling for pasted inputs alone; the brief limit is the real constraint
PART_KEYS_INHERITED = ("agent", "role", "facts", "extra_checks")


class BriefError(Exception):
    pass


def load_preamble(repo):
    """Return an ordered list of (id, text) from the BEGIN/END block."""
    t = open(os.path.join(repo, "playbooks", "GTT-LOCKED-FACTS-PREAMBLE.md"), encoding="utf-8").read()
    m = re.search(r"--- BEGIN PREAMBLE ---\r?\n(.*?)\r?\n--- END PREAMBLE ---", t, re.S)
    if not m:
        raise BriefError("preamble markers not found")
    out = []
    for n, line in enumerate(m.group(1).splitlines(), 1):
        if not line.strip():
            continue
        mm = re.match(r"^@([a-z0-9-]+) (.+)$", line.strip())
        if not mm:
            raise BriefError(f"preamble line {n} has no @topic-id tag: {line[:60]}")
        out.append((mm.group(1), mm.group(2).strip()))
    ids = [i for i, _ in out]
    if len(ids) != len(set(ids)):
        raise BriefError("duplicate topic id in the preamble")
    return out


def facts_block(spec, repo):
    pre = load_preamble(repo)
    core = [t for i, t in pre if i.startswith("core-")]
    core_len = len("\n".join(core))
    if core_len > MAX_CORE_CHARS:
        raise BriefError(f"core is {core_len} characters, over the {MAX_CORE_CHARS} limit: shorten the @core-* lines")
    want = spec.get("facts", "all")
    known = {i for i, _ in pre}
    if want == "all":
        return "\n".join(t for _, t in pre)
    bad = [w for w in want if w not in known or w.startswith("core-")]
    if bad:
        raise BriefError(f"unknown or core fact ids in {spec.get('slug')}: {bad}")
    keep = [t for i, t in pre if i.startswith("core-") or i in want]
    return "\n".join(keep)


def lines_of(repo, path, start, end):
    ls = open(os.path.join(repo, path), encoding="utf-8").read().splitlines()
    body = "\n".join(ls[start - 1:end])
    body = re.sub(r"\s*\[S\d+[^\]]*\]", "", body)  # repo source tags such as [S12 section 3]
    return re.sub("[✅\U0001F7E1\U0001F534]\\s*", "", body)  # status emoji


def build(spec, repo):
    """Return one brief (text) for a spec that has no parts. Raises BriefError if over 8,000 characters."""
    out = ["OVERNIGHT_SLUG: " + spec["slug"], "", "ROLE", spec["role"], "", facts_block(spec, repo), "",
           "INPUTS (pasted from the repo; use only these and the locked facts)"]
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
        raise BriefError(f"{spec['slug']}: inputs are {total} characters, over the {MAX_INPUT_CHARS} limit: trim them")
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
    text = "\n".join(out) + "\n"
    if len(text) > MAX_BRIEF_CHARS:
        raise BriefError(f"{spec['slug']}: brief is {len(text)} characters, over the {MAX_BRIEF_CHARS} limit: "
                         f"trim facts or inputs, or split the spec into parts")
    return text


def expand(spec):
    """Return [(slug, spec)] : one entry, or one per part (slug-p1, slug-p2 ...)."""
    parts = spec.get("parts")
    if not parts:
        return [(spec["slug"], spec)]
    out = []
    for k, p in enumerate(parts, 1):
        ps = {key: spec[key] for key in PART_KEYS_INHERITED if key in spec}
        ps.update(p)
        ps["slug"] = f"{spec['slug']}-p{k}"
        ps["deliverable"] = dict(ps["deliverable"])
        ps["deliverable"].setdefault("part", f"{k} of {len(parts)}")
        out.append((ps["slug"], ps))
    return out


def build_all(spec, repo):
    """Return [(slug, text)] for a spec, with or without parts."""
    return [(slug, build(ps, repo)) for slug, ps in expand(spec)]


def insert_suffix(path, k):
    base, ext = os.path.splitext(path)
    return f"{base}-p{k}{ext}"


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def run_dir(specdir, outdir, repo):
    rows = []
    failed = False
    os.makedirs(outdir, exist_ok=True)
    for sp in sorted(glob.glob(os.path.join(specdir, "*.json"))):
        stem = os.path.splitext(os.path.basename(sp))[0]
        spec = json.load(open(sp, encoding="utf-8"))
        try:
            briefs = build_all(spec, repo)
        except BriefError as e:
            print(f"FAIL {stem}: {e}")
            failed = True
            continue
        for k, (slug, text) in enumerate(briefs, 1):
            name = stem + (f"-p{k}" if len(briefs) > 1 else "") + ".txt"
            write(os.path.join(outdir, name), text)
            rows.append((slug, name, len(text), f"{k} of {len(briefs)}"))
    print(f"{'slug':50} {'file':16} {'characters':>10}  part")
    for slug, name, n, part in rows:
        print(f"{slug:50} {name:16} {n:>10}  {part}")
    print(f"{len(rows)} brief file(s); limit {MAX_BRIEF_CHARS} characters each; core limit {MAX_CORE_CHARS}")
    return 1 if failed else 0


def main(a):
    if not a:
        print(__doc__)
        return 2
    repo = a[a.index("--repo") + 1] if "--repo" in a else os.getcwd()
    try:
        if "--specs" in a:
            outdir = a[a.index("--outdir") + 1] if "--outdir" in a else None
            if not outdir:
                print("--specs needs --outdir")
                return 2
            return run_dir(a[a.index("--specs") + 1], outdir, repo)
        spec = json.load(open(a[0], encoding="utf-8"))
        briefs = build_all(spec, repo)
    except BriefError as e:
        print("FAIL: " + str(e))
        return 1
    outp = a[a.index("--out") + 1] if "--out" in a else None
    for k, (slug, text) in enumerate(briefs, 1):
        if outp:
            p = outp if len(briefs) == 1 else insert_suffix(outp, k)
            write(p, text)
            print(f"wrote {p} ({len(text)} characters)")
        else:
            sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
