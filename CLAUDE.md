# GTT Center Perth — Agent Context (Grace)

This repo is the central, single source of truth for GTT Center Perth. Read/write/commit/push to GitHub throughout the session — don't batch everything into one commit at the end. `git pull` before starting, `git push` after every file or small group of files.

## Skills Activated for This Venture (2026-07-19)

Copied from the empire shared skill library (`/opt/openclaw/shared/skills/` on server) into `.claude/skills/` here — auto-available via the Skill tool:

- **australian-tax-accounting** — use for the open Imara salary-vs-trust-distribution split question, GST treatment of GTT services, any tax classification question in `financial-model.md`/`financial-setup.md`.
- **business-advisory-australia** — use when validating business-plan.md structure, competitive positioning, or general small-business strategy questions.
- **financial-planning-australia** — use for trust distribution strategy, YETI Holding Trust income-splitting questions, anything touching Anthony's personal financial position via the trust.
- **property-investment-australia** — use for site/lease decisions (`location-scouting.md`, `floor-plan-concept.md`) — lease terms, site suitability criteria.
- **stop-slop** — run on every doc before finalizing. Empire QC minimum is 9.5/10 — use this to strip AI writing tells (filler phrases, formulaic structure, passive voice) before a doc is considered done.

**Considered, not activated:** `gh-cli` (source repo, not a skill — you already have the real `gh`/`git` CLI installed, use those directly); `context-mode` (requires an MCP server not set up locally — its benefit is for huge raw-data analysis, not relevant to editing ~60 markdown files); `memory-sync` (cross-session memory sync, not needed for a single continuous run).

**Skills activation verified 2026-07-19:** All 5 skills above confirmed present in `.claude/skills/` locally with content matching the server source byte-for-byte (md5 checksum verified via SSH against `/opt/openclaw/shared/skills/`) — no re-copy needed, activation was already correctly completed. Also scanned the full shared skill library (357+ repos) for anything else relevant to GTT specifically (health/medical compliance, WA retail/health regulation, HR/award interpretation, real-estate/lease analysis) not already listed — **none found.** The library has no dedicated Fair Work/modern-award-interpretation skill, no NATA/ACSQHC/pathology-compliance skill, and no additional lease/commercial-property skill beyond `property-investment-australia` (already activated). Candidates considered and rejected as not GTT-relevant: `maternity-aid-skill`, `dva-navigator-skill`, `ai-doula-skill` (all scoped to other ventures — Maternity Aid/Neve, DVA Navigator/Cipher — not GTT Center Perth).

## Working Principles (from andrej-karpathy-skills, inlined — no separate skill needed)

- **Don't assume, don't hide confusion.** If a doc's meaning is ambiguous or two docs disagree, surface it — don't silently pick one. Add genuinely unresolved items to a running founder-decision list rather than guessing.
- **Simplicity first.** Fix what's asked. No speculative features, no reformatting docs beyond what the task requires.
- **Surgical changes.** Touch only what you must. Don't "improve" unrelated sections while you're in a file. Match existing doc style/voice.

## Standing Facts (don't re-litigate these)

- Venture is NOT blank-slate — 60+ docs exist, several current as of 2026-07-17/18.
- Imara has zero operational involvement (confirmed 2026-07-18) — a Venue Manager (new hire, not yet recruited) covers every on-site duty previously attributed to her. Anthony/Imara retain ownership + financial oversight only.
- Funding: self-funded via Anthony's partner's ~A$200K savings, no external investor.
- Launch date: not set — sequence roadmap by dependency only.
- AM model: Scenario C, 10 clients/day, 07:00 start. Packages: only A$250/A$300 (Package 1 dropped). Saturday reuses AM + PM standalone. Sunday closed.
