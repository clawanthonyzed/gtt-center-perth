# Decision Log

**Purpose:** a running, append-only record of major project decisions, so future sessions/agents don't rediscover the same open questions or silently contradict a decision already made. Add new entries at the top. Do not delete or rewrite prior entries — correct forward, the way the rest of this repository's changelogs already work.

---

## 2026-09-04 — Entity-structure investigation write-up started (research only, no decision made)

**What happened:** `docs/FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md` row 37 flagged an "entity structure investigation write-up" as PLANNED and never actually written, and `docs/financial-setup.md` Step 1 independently flagged the trust-direct vs. PTY LTD question as a genuine open founder decision. Grace produced the write-up: `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`.

**Trigger:** on 2026-09-03 the federal Treasurer released exposure draft legislation for a 30% minimum tax on discretionary trusts from 1 July 2028, with public consultation open until approximately 18 September 2026. YETI Holding Trust (GTT Center Perth's parent structure, corporate trustee YETI Tipi Holdings PTY LTD) is a discretionary trust and falls within scope. The draft also introduces a new option — electing fixed distributions to pre-nominated beneficiaries — as an alternative to restructuring, exempting the trust from the minimum tax without stamp duty exposure but at the cost of the trust's discretionary distribution flexibility. This converts the previously two-way question (trust-direct vs. new PTY LTD) into a three-way question.

**This is NOT a decision.** The new document lays out all three options (trust-direct/current setup, new operating PTY LTD under the trust, fixed-distribution election) neutrally with tradeoffs (tax, liability, admin cost, TPI pension implications for Anthony, impact on Imara's position as beneficiary/funding partner — no operational role assigned to her), and a list of specific questions for the upcoming accountant conversation. No option is recommended or selected. The actual decision remains with Anthony and the accountant.

**Documents updated:** `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md` (new), `docs/financial-setup.md` Step 1 (added cross-reference, checklist itself not rewritten), `docs/FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md` row 37 (status PLANNED -> IN PROGRESS, dossier Ch12 rebuild itself still outstanding, consistent with the Phase L pattern already used for items 4a/6/22/23/24).

**Related documents:** `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`, `docs/financial-setup.md`, `docs/revenue-extraction-options.md`, `docs/dva-tpi-research.md`, `docs/01_conflicts_log.md` (CF-07).

---

## 2026-08-27: Blood Collection Room count: 2 rooms, one per phlebotomist, founder decision overrides evidence-based recommendation

**Decision:** Anthony has decided: **2 Blood Collection Rooms, one per phlebotomist (Chair A/Room 1, Chair B/Room 2), specifically for extra client privacy.** This overrides the evidence-based "1 room, built and serviced for 3 chairs from day one" recommendation reached in `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` Part B (Round 3, 2026-08-22) after extensive evidence review. The evidence-based recommendation was sound on its own terms and is retained in full for trace, not deleted or found to be wrong, it is simply overridden by direct founder instruction, a founder's prerogative, not to be second-guessed or reopened.

**Nature of the change:** this is a room-configuration change, not a capacity change. Total phlebotomists (2) and chairs (2) are unchanged, split across 2 separate rooms rather than sharing 1 room. The 18-clients/day AM model, staffing model, and financial figures in `docs/CURRENT-STATE.md` are unaffected.

**New open questions this decision introduces, flagged not resolved:** (1) the growth path: the single-room design's own documented 3rd-chair growth lever no longer straightforwardly applies once the room is split into 2 separate 1-chair rooms; whether growth means a 3rd room or a 2nd chair added to one of the 2 existing rooms is undecided. (2) whether the centrifuge, specimen fridge, and vasovagal recliner are shared between the 2 rooms or duplicated (a real cost question, not decided). (3) whether the per-chair curtain (previously for partitioning multiple chairs within 1 shared room) is still needed now each chair has its own solid door.

**Real consequences propagated:** floor area increases by an estimated ~18-20sqm (using the already-evidenced Option 2 minimum-floor-area estimate from the same decision-analysis document, not a newly invented figure); day-one venue footprint moves from ~239sqm to ~257-259sqm. The existing day-one fit-out dollar cost range (A$228,142-457,559) has NOT been recalculated for the larger footprint, flagged as an open item pending a confirmed venue, not invented here. Room-level fixed infrastructure (solid walls/door, biohazard/no-entry signage, emergency call button) confirmed doubled in the procurement register; several other items (centrifuge, specimen fridge, vasovagal recliner, sharps/waste bins, clinical sink, ventilation, per-chair curtain) flagged as genuinely open shared-vs-duplicated questions, not asserted either way.

**Documents updated:** `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` (Part B closure banner, Part D consolidated table, Part F gap list), `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md` (Blood Collection row, Notes, Changelog), `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` (Section E header banner plus individual line items E31/E33/E35/E36 confirmed doubled, E03/E04/E15/E16/E24/E32/E38 flagged as open questions), `docs/architecture/PROCUREMENT-CONSTRUCTION-FITOUT.md`, `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` (§3.2 contradiction resolved, §5 chair spec updated), `docs/floor-plan-concept.md` (Room Schedule split into 2 rooms, subtotals recalculated), `docs/business-plan.md` (venue footprint and room-count wording corrected, v5.2 -> v5.3), `outputs/master-dossier-v2/index.html` and `outputs/gtt-dash/index.html` (decision registers and narrative mentions updated).

**Related documents:** `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` Section E.

---

## 2026-08-14 — Naming: conditional leader is SOLENA; retail-strategy question closed

**Decision:** SOLENA is the current conditional naming leader (71.6% on the weighted three-way comparison), ahead of ELOWEN (68.8%) and ELOWYN (65.9%). Not locked.

**Reason:** Three-way comparison in `docs/naming/NAMING-FINAL-COMPARISON.md`, combined with the founder's confirmed business strategy. Elowyn was given a fair Phase 2 evaluation and its severe referral/spelling friction was independently confirmed by two separate design passes, weighing it below the other two despite the cleanest trademark position. Solena's strategic strength (repeat-visit desirability, execution cost, non-pregnancy lifestyle fit) now carries more relative weight because the one thing that most threatened it — a live Class 3 trademark blocking a future product line — has been confirmed not to threaten a business ambition that actually exists.

**Founder input received (2026-08-14):** Is a name-branded retail/product line a genuine strategic ambition? **Answer: NO / not a priority.** Third-party resale (Gaia, Weleda, Mustela) remains the retail strategy. This question is now closed and should not be reopened unless the business model itself changes — see `docs/naming/NAMING-DECISION-STATE.md`.

**Outstanding:** Trademark professional validation, deliberately deferred. Legal status is **KNOWN RISK — NOT YET PROFESSIONALLY CLEARED**, not "clear" or "safe." No attorney has been engaged and none is authorised to be paid at this venture stage. `docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md` is prepared and held for a later validation/funding milestone.

**Reversal condition:** Revisit SOLENA specifically if either (a) a future professional trademark assessment identifies a meaningful Class 44 obstacle (not just the known Class 3 conflict), or (b) a proprietary Class 3 product line later becomes a genuine strategic ambition — in which case re-run the weighting in `docs/naming/NAMING-FINAL-COMPARISON.md` §3 with that new fact, rather than assuming the current percentages still hold.

**Related documents:** `docs/naming/SOLENA-ELOWEN-STRATEGIC-HANDOVER-DECISION-AUDIT.md`, `docs/naming/NAMING-FINAL-COMPARISON.md`, `docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md`, `docs/naming/NAMING-DECISION-STATE.md`.

---

## 2026-08-14 — Brand/experience strategy work proceeds while naming stays conditionally open

**Decision:** Begin name-agnostic brand strategy and customer-experience documentation now, rather than waiting for the naming decision to lock.

**Reason:** The naming decision has two remaining, well-defined blockers (attorney clearance, deliberately deferred; and the retail-strategy question, now answered) that don't touch the underlying business/brand strategy, customer psychology, or experience design — all of which are identical regardless of whether Solena or Elowen ultimately wins. Direct founder instruction: the naming decision should not become an excuse for the rest of the venture's development to stall.

**Documents created:** `docs/strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md`, `docs/experience/CUSTOMER-JOURNEY.md`, `docs/experience/RETURN-LOOP.md`, `docs/strategy/BRAND-ARCHITECTURE.md`, `docs/strategy/PREMIUM-POSITIONING.md`.

**Explicit boundary:** none of the above lock a final logo, palette, type system, signage, packaging, uniforms, or production website for either candidate name — that remains gated on the naming decision per `docs/naming/NAMING-DECISION-STATE.md`'s "DO NOT START YET" list.
