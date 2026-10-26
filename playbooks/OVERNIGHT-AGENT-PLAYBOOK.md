# GTT overnight agent playbook

Established 2026-10-26 (Autonomous Task Playbook Protocol). Owner: Grace for GTT drafts, Idea Lobster for inspection. Applies to every GTT task that runs on the free route while Anthony's laptop is shut.

## Why this exists (evidence from the 2026-10-24 and 2026-10-25 runs)

| What went wrong | Cause found | Fix in this playbook |
|---|---|---|
| 46 confirm-later slots in one draft | The plain draft path tells the model to mark anything unknown as a confirm-later slot | Every brief carries an OVERNIGHT_SLUG line: the executor then uses overnight mode (unknowns are left out, Proof-of-Done check, one automatic rework) |
| Drafts cut off or thin | Plain path caps output at 3,000 tokens; overnight mode allows 7,000 | One small deliverable per task, 70 lines or fewer |
| Stale facts (12-minute cadence, 07:00 venue manager, hosts, sonographers, A$99.40) | Briefs gave no facts; the model filled gaps from training | Locked facts pasted into every brief, now only the topic lines the task needs <!-- factcheck:ok --> |
| Briefs of 6,000 to 12,000 characters (R19) | The whole 7,000 character preamble was pasted into every brief | The 8,000 character rule: tagged preamble, per-task facts list, tiny core, parts (below) |
| "Source from the repo" ignored | The free route cannot read files or browse | Inputs are pasted into the brief with file path and lines |
| Nothing caught the errors | Proof-of-Done checks placeholders and dashes, not GTT facts | tools/factcheck_locked_facts.py on every brief and every draft |

## The 8,000 character rule (Anthony, 2026-10-26)

Any task over 8,000 characters must be split into parts. A brief file is a task, so no brief file is longer than 8,000 characters.

| Step | Rule |
|---|---|
| Size | The builder counts characters and refuses to write a brief over 8,000 (exit 1). It also fails if the always-included core is over 1,200 characters |
| Facts | Each spec lists the topic ids it needs in `facts`. The preamble file tags every line `@topic-id`; only those lines and the core are pasted |
| Split | If facts plus inputs do not fit, split the spec into `parts`. Each part is a full brief (`<slug>-p1`, `<slug>-p2`), checked on its own, queued as its own task, with a deliverable of 70 lines or fewer |
| No overlap | Each part's "Do not write" names what the other part covers |
| Queueing | One queue command per brief file. A spec with 2 parts is 2 tasks |
| Counting the night | Round 22 (Anthony, 2026-10-26) queued 28 brief files from 25 jobs because about 37 free-route calls were left. A split spec is several tasks and uses several calls. Plan 1 call a task, up to 3 with rework |

## Trigger

Anthony or Idea Lobster names work that a free-route draft can do (text only, no tools, no browsing). Work that needs file edits, calculators, live data or legal reading goes to a full-tool session (Catherine owns legal texts).

## Inputs

1. docs/FINANCIAL-CENTER-OF-TRUTH.md and docs/CURRENT-STATE.md section 000 (read first, every time).
2. playbooks/GTT-LOCKED-FACTS-PREAMBLE.md (re-check it against the two files above).
3. The exact repo lines the task needs.

## Steps

1. Read the Center of Truth. If a decision changed since the preamble date, update the preamble first.
2. Write a spec file (JSON) for the task: slug, agent (the original task's agent), role, facts (topic ids), inputs (path and line range, or condensed inline text), deliverable, extra checks, and `parts` if it will not fit. Examples: playbooks/briefs-r22/specs/. Field list: playbooks/BRIEF-TEMPLATE.md.
3. Build the brief: `python3 tools/build_overnight_brief.py spec.json --repo <repo> --out brief.txt`, or every spec in a folder with `--specs <dir> --outdir <dir>`. It pastes the core and the listed facts and the inputs, and refuses any brief over 8,000 characters (parts become brief-p1.txt, brief-p2.txt).
4. Fact-check every brief file: `python3 tools/factcheck_locked_facts.py brief.txt`. Exit 0 required (it also flags the bare word for a parent).
5. Queue it: `python3 /opt/openclaw/orchestration/queue_task.py --agent <agent> --venture "GTT Center Perth" --title "R22-<nn> <title>" --brief-file brief.txt --priority 7`. One brief file, one task, one deliverable.
6. The executor claims it (2 a minute), runs it on the free route and checks it with Proof-of-Done. The result is saved under second_brain/overnight/<slug>/. The database trigger turns the card into DRAFT (needs Anthony sign-off).
7. Inspect (Idea Lobster, no rewriting): `python3 tools/factcheck_locked_facts.py draft.md` and `python3 /opt/openclaw/toolbox/formatters/proof_of_done.py draft.md`. Read the whole draft against the brief's acceptance list.
8. Pass: link it in the report. Fail: send it back to the same agent as a rework order with the failing lines quoted (new task, same brief plus a FIX line). Two failures in a row: stop and tell Anthony what is missing.

## Acceptance checks (all must be true)

| Check | How |
|---|---|
| Proof-of-Done 0 failures | proof_of_done.py |
| 0 banned stale values, 0 em dashes | factcheck_locked_facts.py |
| Every figure is in the preamble or the inputs | read the draft against the brief |
| Missing facts are written NOT IN REPO, not guessed | search the draft for invented names, addresses, amounts |
| Length within the brief | line count |
| Every brief file is at most 8,000 characters | the builder's table of characters per file |
| Sections Summary, Deliverable, Next step for Anthony present | the executor rejects drafts without a Deliverable section |

## Limits to plan around

The free route allows about 50 calls a day (resets 08:00 AWST). Each task uses 1 call, 2 if reworked. When every free model returns 429 the work waits; the requeue cron (every 20 minutes, up to 4 tries) puts failed cards back. Queue only as many brief files as the remaining calls allow (1 to 3 calls each); split jobs count by file. Round 22 runs at priority 7, ahead of the older priority 5 and 6 backlog (the executor claims by priority, highest first). Requeue note: the cron runs 02:05 to 05:45 server time; since the clocks went back on 2026-10-25 that is 09:05 to 12:45 AWST, not 08:05. Reject llama3.2:3b drafts. Long tables get cut off: ask for 8 rows at most.

## Escalation

Only money, accounts, legal or a fact only Anthony knows. Put each in the draft's Questions for Anthony (at most 3) and in the artifact's Questions card. Everything else, fix and re-test.

## Hard stops

| Stop | Meaning |
|---|---|
| Publishing Shield | Nothing is posted, emailed or sent. Every GTT result lands as a draft for Anthony's approval |
| Legal | No legal advice. Catherine owns /opt/openclaw/second-brain/knowledge/legal/. Drafts say lawyer to check |
| Floor plans | Banned for agents. Words only; the registered architect draws |
| Billing model | Structure B only. No other billing model is discussed |
| Figures | No invented figures. The only profit figures are Theodore R21's, copied not recomputed (Theodore R22 now: A$26,631.97 before, A$19,973.98 after) |
| Style | No em dashes. AUD. Plain English |
| Roles | Only the roles in the preamble. No hosts, no sonographers <!-- factcheck:ok --> |
| Cost | Free route only. No paid model, no RunPod |
