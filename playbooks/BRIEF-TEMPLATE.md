# GTT overnight brief template

Use this for every task queued to the free route. It exists because the R16 briefs (2026-10-24) were short, told the model to "source from the repo" (it cannot read files), carried no acceptance test, and asked for whole documents in one go. Fill every part. Build the final brief file with `python3 tools/build_overnight_brief.py` or by hand, then run `python3 tools/factcheck_locked_facts.py <brief>` on it.

## The template

```text
OVERNIGHT_SLUG: gtt-r19-<nn>-<short-name>

ROLE
You are <agent>, <job title> for GTT Center Perth. You write one draft, for Anthony to review. You cannot read files or browse; everything you may use is in this brief.

<paste the whole block between BEGIN PREAMBLE and END PREAMBLE from playbooks/GTT-LOCKED-FACTS-PREAMBLE.md>

INPUTS (pasted from the repo, with the file path and the lines they came from)
Input 1: <repo path>, lines <a> to <b>
<pasted text, trimmed to what the task needs>
Input 2: ...

DELIVERABLE
Part: <this task is part X of Y>
Format: <headings, table columns, numbered steps>
Length: at most 70 lines in total; tables at most 8 rows; no filler.
Write only: <the sections for this part>
Do not write: <what belongs to another part or another task>

ACCEPTANCE CHECKLIST (the draft is rejected if any is false)
1. Every number comes from the preamble or the inputs.
2. No em dashes, no square brackets, no placeholder words (the builder spells them out).
3. A fact that is missing is written as NOT IN REPO, and listed once under "Questions for Anthony" (at most 3).
4. Nothing is addressed to a real person or sent anywhere. Any lawyer point is marked "lawyer to check".
5. Ends with the sections the system asks for: Summary, Deliverable, Next step for Anthony.

WHEN A FACT IS MISSING
Write NOT IN REPO, say what is needed and who holds it, and carry on with the rest. Never guess.
```

## Rules for filling it

| Part | Rule |
|---|---|
| OVERNIGHT_SLUG line | Required. Without it the executor uses the plain draft path: 3,000 token cap, no Proof-of-Done check, and a system prompt that tells the model to mark anything unknown as a confirm-later slot. That is what produced the R16 confirm-later slots. |
| Preamble | Pasted whole, unedited. Re-pull it from the repo each time. |
| Inputs | Paste the real text, 3 to 40 lines each, under 8,000 characters in total. Say which file and lines. Never write "see the repo". |
| Deliverable | One task, one document part, under 70 lines. Large documents are several tasks (part A, B, C), each with its own slug. |
| Checklist | Keep all five lines. Add task-specific tests as lines 6 and up (for example "exactly 14 headings"). |
| Queueing | `python3 /opt/openclaw/orchestration/queue_task.py --agent <same agent> --venture "GTT Center Perth" --title "R19-<nn> <title>" --brief-file <file>`. The brief file lives on the server. |
