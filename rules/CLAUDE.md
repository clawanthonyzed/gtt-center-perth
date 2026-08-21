# GTT Center Perth — Venture Governance Rules

**Created:** 2026-07-29. No `rules/` directory or `rules/CLAUDE.md` existed in this repo before this session — this is the minimal equivalent, created per an outside review's finding that the venture had no standing rule preventing invented/false-precision figures. This file is scoped to GTT Center Perth only. It is separate from, and does not modify, the global empire `CLAUDE.md` (`C:\Users\azed9\CLAUDE.md`) — that file's rules are out of scope here and this file has no authority over them.

---

## Hard Rule — No Figure Without a Tag

**No agent may state a financial or regulatory figure as fact without a `[VERIFIED]` or `[MODELED]` tag, per `docs/CURRENT-STATE.md`'s tagging system.**

- `[VERIFIED — source, date]` — confirmed by an external party (a real WDP/PathWest/Clinipath reply, a signed quote, an accountant or solicitor confirmation, or a programmatic scheduling simulation that is itself the primary source).
- `[MODELED — assumption: <name it>]` — internally calculated from other modeled or verified inputs. Name the assumption explicitly; do not present a modeled figure as if it were verified.
- `[PLACEHOLDER — not yet known]` — a genuine unknown, or a fact that conflicts across this repo's own documents and has not been reconciled.

**If a number is needed and no source exists, write PLACEHOLDER and add it to `docs/VERIFICATION-TRACKER.md` — never invent a plausible-sounding number to fill the gap.**

---

## Why This Rule Exists

An outside review of this repo (2026-07-29) found:
- The financial model had moved 5+ times with contradicting numbers across documents, with no single canonical source.
- Profit was quoted to the cent (e.g. "+A$25,087.07/month") on a business with zero real trading data.
- `operations-manual.md` — the document staff train from — still described an abandoned 8-client scheduling model 10 days after being flagged as superseded, because the flag was added as a banner without the underlying content ever being fixed.
- `investor-memorandum.md` showed a loss in its own body table while a banner directly above it claimed the venture was profitable.
- Roughly 48 of 107 markdown files in this repo contained `[to be inserted/confirmed]` placeholders — some legitimately blank pending real information, others silently smoothed over elsewhere.
- The AM/GTT segment was modeled as losing money on its own in one document (`pm-staffing-roster.md`'s Profit Breakdown table) 9 days after the exact same figure was corrected venture-wide elsewhere (`docs/01_conflicts_log.md` CONFLICT-08) — the fix never propagated to the segment-level table.

Every one of these is a process failure, not a one-off numbers mistake: flagging a stale figure without physically fixing or moving it, and having no single canonical source for current numbers, made it inevitable that fixes in one place would leave contradictions everywhere else. This file and `docs/CURRENT-STATE.md` are the two-part fix: one canonical numbers file, and a standing rule that nothing gets stated as fact without a tag.

---

## Companion Rules

1. **Archive, don't flag.** A document (or section) marked SUPERSEDED/STALE/ARCHIVED gets physically moved to `docs/archive/` (via `git mv`, preserving history) or rewritten in place, in the same session it is identified — not left in the main `docs/` folder with a banner pointing elsewhere. A flagged-but-left-in-place file is exactly how the `operations-manual.md` problem happened.
2. **One canonical numbers file.** `docs/CURRENT-STATE.md` is the single source for package prices, client capacity, headcount, monthly net P&L, and startup capital range. Every other document points to it rather than independently restating these figures.
3. **One canonical open-items file.** `docs/VERIFICATION-TRACKER.md` is the single running list of unconfirmed facts, who can confirm each one, and current status. New unconfirmed facts get added there first, not scattered through other documents.
4. **Run the consistency checker before quoting figures externally.** `python tools/check_consistency.py` greps every `docs/*.md` file (excluding `docs/archive/`) for known-stale values of the tracked parameters in `docs/CURRENT-STATE.md`. Run it before any investor conversation, lease negotiation, or staff training session that will quote a number from this repo. It is a grep-based sweep, not a semantic parser — it will have false positives, but a false positive is a much cheaper failure mode than a silent stale figure reaching a real conversation.
5. **Never invent a placeholder value to make a document look complete.** `emergency-plan.md`, `privacy-policy.md`, `consent-form.md`, and any similar draft-with-blanks document must keep every `[to be inserted]`/`[to be confirmed]` field as an explicit blank until a real value exists. A fabricated-but-plausible placeholder (a fake phone number, a made-up address) is worse than an honest blank — it can silently pass through to a live document.
6. **3D scan framing.** Never frame the keepsake ultrasound scan as diagnostic. Keepsake/entertainment only, consistent with the empire-wide rule.
7. **No regulatory claims without a citable current WA Health/AHPRA source.** Consistent with the empire-wide rule — this venture's regulatory tracker (`docs/VERIFICATION-TRACKER.md`) exists specifically to hold every such claim that isn't yet independently sourced.
8. **Before citing anything as "open," "unresolved," or "not yet decided" — check whether it's already resolved.** This applies to operational/policy matters exactly as Rule 2/3 already apply to financial figures. The recurring failure this rule exists to stop: an older document still states the pre-resolution position (because it was disclosed with a banner, not archived, per Companion Rule 1's own exception for documents undergoing active investigation), a later document resolves it, and a still-later session cites the older document without checking whether a resolution exists — rediscovering a resolved matter as new. **Before presenting any matter as open: (a) check `docs/VERIFICATION-TRACKER.md` for that item's current status, (b) check `docs/DECISION-LOG.md` for a founder decision on it, (c) if a dossier exists (`outputs/master-dossier-v2/index.html`), check its Chapter 34 (Open Items/Decisions) — that chapter is itself required to be re-verified against current repo state before every dossier update, so it is a genuine current-status source, not just another document that might be stale.** If a resolution is found, the older document's conflicting statement gets classified HISTORICAL/SUPERSEDED in whatever you're writing now — it does not get treated as evidence the matter is still open, and the older document itself is not rewritten unless you are the one resolving it for the first time (per Companion Rule 1).

---

## Changelog

**2026-08-21 (Companion Rule 8 added)** — Added per a recurring failure pattern observed across multiple GTT dossier-build sessions: resolved matters (the WDP courier cutoff, the PM Reception coverage gap, and others) were repeatedly re-flagged as newly-discovered open issues because an older document's pre-resolution wording was cited without checking `VERIFICATION-TRACKER.md`, `DECISION-LOG.md`, or the dossier's own Chapter 34 first. This is the same class of problem Companion Rules 1-3 already solve for financial figures, extended explicitly to operational/policy resolutions. No new file created — this rule points to the three registers that already exist rather than creating a fourth.

**2026-07-29 (created)** — Created in direct response to an outside GitHub repo review that Anthony accepted in full. Companion files created the same session: `docs/CURRENT-STATE.md` (canonical numbers), `docs/VERIFICATION-TRACKER.md` (merged from `05_open_questions_for_founder.md`, `regulatory-accreditation-tracker.md`, `04_roadmap_next_steps.md`), `tools/check_consistency.py` (automated sweep).
