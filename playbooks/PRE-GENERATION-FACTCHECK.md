# Pre-generation fact check

Anthony asked on 2026-10-26: "Why are mistakes still being made? Implement a pre-generation fact-check step." Mistakes kept happening because facts were checked after writing, by memory, and each new draft started from whatever the model or the session remembered. This routine checks before and after. It applies to Idea Lobster, every consultant and every subagent working on GTT.

## The routine (8 steps)

1. Read docs/FINANCIAL-CENTER-OF-TRUTH.md (all of it) and docs/CURRENT-STATE.md section 000 before writing anything. Do not work from memory or from an earlier round's file.
2. Note which round the facts are from. If Anthony decided something after the Center of Truth date, add it to the repo first (DECISION-LOG, then the preamble), then continue.
3. Paste the block from playbooks/GTT-LOCKED-FACTS-PREAMBLE.md at the top of every subagent brief. Use tools/build_overnight_brief.py for free-route tasks.
4. Give each subagent the exact repo lines it needs, pasted in. Never write "see the repo" to an agent that cannot read it.
5. Draft. Where a fact is missing, write NOT IN REPO. Never fill the gap.
6. Run `python3 tools/factcheck_locked_facts.py <draft>`. It reads the banned stale values from section 8 of the Center of Truth, adds a few known stale patterns, and fails on em dashes. Exit 1 means fix and run again. It does no arithmetic: for numbers, compare to the Center of Truth by eye or run Theodore's `theodore_r19.py --check`.
7. Put every genuine question (money, accounts, legal, a fact only Anthony holds) in the artifact's Questions card, at most 3 per draft. A question already answered in the Center of Truth is never asked again.
8. Only then send to Anthony: link the draft, state that the check passed, and list anything marked NOT IN REPO.

## Keeping the check current

Theodore's script regenerates the Center of Truth, including its banned list. When it changes, the checker picks it up on the next run (no code change). New stale patterns found in a draft go into the EXTRA list in tools/factcheck_locked_facts.py, with the date.
