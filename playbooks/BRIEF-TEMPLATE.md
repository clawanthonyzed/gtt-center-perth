# GTT overnight brief template

Use this for every task queued to the free route. It exists because the R16 briefs (2026-10-24) were short, told the model to "source from the repo" (it cannot read files), carried no acceptance test, and asked for whole documents in one go. The R19 briefs fixed that but ran 6,000 to 12,000 characters because the whole locked-facts preamble (about 7,000 characters) was pasted into each one.

## THE 8,000 CHARACTER RULE (Anthony, 2026-10-26)

**Any task over 8,000 characters must be split into parts.** The brief file itself is a task, so every brief file is at most 8,000 characters, counted as plain characters including spaces and line breaks.

| Rule | How it is kept |
|---|---|
| A brief is at most 8,000 characters | `tools/build_overnight_brief.py` refuses to write a longer brief and exits 1 with the size |
| No hand-pasting of the preamble | The preamble file tags every line `@topic-id`. A spec lists `"facts": [ids]` and the builder pastes only those lines |
| A tiny core goes in every brief | All `@core-*` lines (use-exactly rule, style, what it is, MONEY RESULT, hard stops, the word client). The builder fails if the core is over 1,200 characters |
| A big job is split | A spec has `"parts": [ ... ]`. Each part is a complete brief with its own slug (`<slug>-p1`, `<slug>-p2`), its own inputs and its own facts, and is checked on its own |
| Each part stands alone | The part names what the other part covers under "Do not write", so nothing is repeated and nothing is left out |
| Queue every part as its own task | One part, one task, one slug, one deliverable of 70 lines or fewer |

Budget for one brief (characters): core about 1,000, template wording about 1,100, role and deliverable about 800, so about 5,000 are left for facts and inputs. If the facts you need plus the inputs do not fit, split the job.

## The template (what the builder writes)

```text
OVERNIGHT_SLUG: gtt-r21-<nn>-<short-name>[-p1]

ROLE
You are <agent>, <job title> for GTT Center Perth. You write one draft, for Anthony to review. You cannot read files or browse; everything you may use is in this brief.

<the @core-* preamble lines, then only the topic lines the spec asks for in "facts">

INPUTS (pasted from the repo or condensed from it, with the source file named)
Input 1: <label and source file>
<text, trimmed to what the task needs>
Input 2: ...

DELIVERABLE
Part: <x of y>
Format: <headings, table columns, numbered steps>
Length: at most 70 lines in total; tables at most 8 rows; no filler.
Write only: <the sections for this part>
Do not write: <what belongs to another part or another task>

ACCEPTANCE CHECKLIST (the draft is rejected if any is false)
1. Every number comes from the locked facts or the inputs.
2. No em dashes, no square brackets, no placeholder words (the builder spells them out).
3. A fact that is missing is written as NOT IN REPO, and listed once under "Questions for Anthony" (at most 3).
4. Nothing is addressed to a real person or sent anywhere. Any lawyer point is marked "lawyer to check".
5. Ends with the sections the system asks for: Summary, Deliverable, Next step for Anthony.
6 and up: the spec's extra_checks

WHEN A FACT IS MISSING
Write NOT IN REPO, say what is needed and who holds it, and carry on with the rest. Never guess.
```

## Spec file (JSON)

| Key | Meaning |
|---|---|
| slug, agent, role | Required. Parts inherit them and add `-p1`, `-p2` to the slug |
| facts | List of topic ids from playbooks/GTT-LOCKED-FACTS-PREAMBLE.md (table at the top of that file). Leave it out only for a job that really needs every line, and then it must still fit in 8,000 characters |
| inputs | Repo lines to paste: `{label, path, start, end}`. Pick clean lines; the text must not contain square brackets, the bare word for a parent, or stale values |
| inline_inputs | Hand-condensed text: `{label, text}`. Name the source file in the label. Prefer this when the source lines are long or stale |
| deliverable | `{part, format, length, write_only, do_not_write}` |
| extra_checks | Task tests, numbered from 6 |
| parts | Optional list of part specs (deliverable, inputs, inline_inputs, facts, extra_checks per part) |

Build all specs in a folder: `python3 tools/build_overnight_brief.py --specs playbooks/briefs-r21/specs --outdir playbooks/briefs-r21` (prints slug, file, characters, part). Then `python3 tools/factcheck_locked_facts.py playbooks/briefs-r21/*.txt`.

## Rules for filling it

| Part | Rule |
|---|---|
| OVERNIGHT_SLUG line | Required. Without it the executor uses the plain draft path: 3,000 token cap, no Proof-of-Done check, and a system prompt that tells the model to mark anything unknown as a confirm-later slot. That is what produced the R16 confirm-later slots. |
| Core and facts | Never edited by hand in a brief. Change the preamble file (one tagged line), rebuild every brief |
| Inputs | Real text, 3 to 40 lines each. Say which file. Never write "see the repo". |
| Deliverable | One task, one document part, under 70 lines. Large documents are several parts, each its own task. |
| Checklist | Keep all five lines. Add task-specific tests as lines 6 and up (for example "exactly 14 headings"). |
| Wording | Say client. Never use the bare word for a parent. Late means from the appointment time onwards. |
| Queueing | `python3 /opt/openclaw/orchestration/queue_task.py --agent <same agent> --venture "GTT Center Perth" --title "R21-<nn> <title>" --brief-file <file>`. One command per brief file, parts included. The brief file lives on the server. |
