# Why facts drift, and the guards now in place

## READ-FIRST CHECK
- Venue manager starts 06:30. The first draw is 07:00. Anthony is owner and director, 0 operational hours.
- Path A = with the GTT midwife consult (preferred, A$320 / A$370). Path B = outside referral (A$300 / A$350), not limited.
- Rebates A$32.95 + A$22.05 = A$55.00. Midwives 08:00 to 16:00, first consult 08:15. Draws: no wiggle room. Consults: 10 minute grace.

Anthony, here is the plain answer to "why do locked facts keep coming back wrong".

## What I found (causes)
1. The same fact lived in many files. The scan found 336 stale lines in 77 files. When a fact is changed in one place the other copies stay old, and an agent reading an old copy treats it as true.
2. Old drafts looked like truth. Round 15 to 22 files, the July and August documents and the old business plan read as confident and current. Nothing on them said "out of date".
3. Two files claimed to be the master. CLAUDE.md said CURRENT-STATE.md was the single source; the rulebook said GTT-READ-FIRST.md was. An agent obeyed whichever it read first.
4. Generated tables were not regenerated. The pricing, profit and ramp files in outputs and architecture still carried the old A$35,186.40 profit and the 43/64/79/93/100 ramp. <!-- factcheck:ok -->
5. Agents were not reading the rulebook. The agent persona files (Grace, Reed, Bruno and others) still said "trust", "Venue Manager has no operational involvement" and "MRCA permanent fact". None of them mentioned GTT-READ-FIRST.md. <!-- factcheck:ok -->
6. Council-style multi-agent runs each carry their own context. Each agent starts with only the brief it was handed, so a missing fact in the brief is a missing fact in the answer. Nobody in the room remembers last week's lock.
7. The server copy of the rulebook is old (4,612 bytes against 10,731 in the repo), so any agent that reads the server version works from Round 22 facts.

## Guards now in place
| Guard | What it does |
|---|---|
| Rulebook law | GTT-READ-FIRST.md wins over every file. It is now the first section of the repo CLAUDE.md. |
| Fact check tool | tools/factcheck_locked_facts.py flags stale values and patterns in any file. |
| Pre-commit hook | .git/hooks/pre-commit (copy at tools/pre-commit-factcheck.sh) blocks a commit if a line you ADD contradicts the rulebook. Tested: a bad file was blocked, a clean file passed. Put the marker factcheck:ok on a line that quotes a banned value on purpose. |
| Integrity check | tools/memory_integrity_check.py confirms 25 headline facts still sit in the rulebook and Center of Truth and fails loudly if one goes missing or changes. Tested with two faked changes: it failed and named both. Run it any time. |
| Persona first line | 11 GTT agents now start with "Before any GTT work read docs/GTT-READ-FIRST.md ... Never contradict them." Their trust and DVA lines were fixed. | <!-- factcheck:ok -->
| Banners | 120 repo files and 12 memory notes now say "SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md". |

## What I could not fix (honest list)
- The server copy of GTT-READ-FIRST.md and the Center of Truth (second-brain gtt-playbooks and gtt-ops/r24) is stale. Idea Lobster must copy the repo versions over.
- Idea Lobster's own memory notes, the MEMORY.md index and the global CLAUDE.md in C:\Users\azed9: I bannered 12 notes but did not rewrite them. Idea Lobster must refresh project_gtt_center_perth.md and the index lines to match the rulebook.
- Theodore and Catherine are empire-wide, so their trust and pension text stays; they only got the first line.
- Other windows and chat sessions outside this repo cannot be blocked by a hook. They only fix themselves if they read the rulebook.
- The hook guards new lines in docs/*.md and playbooks only (not outputs), and only on a machine where it is copied into .git/hooks.
- Old body text is still wrong in the bannered files. The banner warns; it does not correct the number.
- DECISION-LOG.md, operations-manual.md and GTT-READ-FIRST.md were left alone because other agents are changing them.

Regards.
