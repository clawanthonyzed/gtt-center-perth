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
- Funding: self-funded via Anthony + Imara's joint savings (~A$200K), no external investor. **Corrected 2026-07-29 — previously miswritten as "Imara's personal savings" in several docs; Anthony confirmed directly it is joint savings, not Imara's alone.**
- Launch date: not set — sequence roadmap by dependency only.
- AM model — **REBASED 2026-08-05, per Anthony's direct instruction: the 25-min-cadence tables (previously Carole-facing only) are now the actual financial basis venture-wide.** New PRIMARY committed daily model: **18 clients/day, 07:00 start, 25-min pair cadence (Table 1)** — Monthly Net P&L +A$63,028.75, same 8 dual-qualified treatment staff + 2 phlebotomists as the old 12-client model, zero extra weekday labor cost. New SECONDARY reference: **12 clients/day, 08:00 start, same 25-min cadence (Table 2)** — Monthly Net P&L +A$27,084.69 (numerically unchanged from the old committed figure). **Framing flag, not yet confirmed by Anthony:** Table 1 was adopted as "the" committed target because it strictly dominates Table 2 (same headcount, more revenue) — if Anthony instead means keep 12/day as the daily aim and only fix the schedule shape, Table 2 is the one to use. Packages: only A$250/A$300 (Package 1 dropped). Saturday reuses the same AM volume as weekday. Sunday closed. **Treatment staff are hired dual/multi-qualified, full stop — there is no "unpooled" model.** 8 dual-qualified staff (4 Massage+Beauty pool + 2 Nails + 2 Hair) confirmed identical at BOTH 18-client and 12-client volumes under the 25-min cadence — a genuinely better finding than the old model, which needed 9 staff to serve just 14 clients. **The old 12-client/23-min-cadence committed model and its 14-client "proven ceiling" (9 staff, +A$36,726.23/month) are now HISTORICAL/superseded** — retained for trace in `docs/CURRENT-STATE.md` §1/§4/§7/§8, not deleted, no longer the committed basis. Item 1, 2026-08-05: a 7th pair CANNOT be added to Table 2 at 10:25 without breaking headcount (11, not 8) — tested and rejected. See `docs/CURRENT-STATE.md` §1/§3/§4/§5/§7/§8 for full method and figures.

## Governance — Read Before Stating Any Figure

- **`rules/CLAUDE.md`** (this repo's own governance rules, created 2026-07-29) — hard rule: no financial/regulatory figure without a `[VERIFIED]`/`[MODELED]`/`[PLACEHOLDER]` tag.
- **`docs/CURRENT-STATE.md`** — the single canonical source for package prices, client capacity, headcount, monthly net P&L, and startup capital range. Every other document defers to it.
- **`docs/VERIFICATION-TRACKER.md`** — the single running list of unconfirmed facts, who can confirm each, and status (merges the former `05_open_questions_for_founder.md`, `regulatory-accreditation-tracker.md`, `04_roadmap_next_steps.md`).
- Run `python tools/check_consistency.py` before quoting any figure externally.
