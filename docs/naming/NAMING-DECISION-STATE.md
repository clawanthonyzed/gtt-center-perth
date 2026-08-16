# Naming Decision State — Shared Source of Truth

**Purpose:** single place both Claude Cowork and Grace check before touching naming or brand-identity work, so neither environment independently invents a conflicting decision. Update this file, don't recreate it, whenever naming status changes.

**Last updated:** 2026-08-14

---

## CURRENT STATUS

**Conditional naming decision. Not locked. Legal clearance and one founder decision are still outstanding gates.**

## CURRENT LEADER

**SOLENA — conditional, strengthened 2026-08-14.** Leads the updated three-way weighted comparison (`docs/naming/NAMING-FINAL-COMPARISON.md`, 71.6%) on strategic-fit grounds (repeat-visit desirability, execution cost, non-pregnancy lifestyle fit). The founder has now confirmed directly (2026-08-14) that a name-branded retail/product line is **not a strategic priority** — third-party resale (Gaia, Weleda, Mustela) remains the retail model. This resolves the one open founder-decision blocker and confirms the Class 3 trademark finding should carry strategic weight only on the services-use question, not on a product-line ambition that doesn't exist. The trademark finding itself remains real, unresolved, and undocumented-as-cleared — that is still the reason this is conditional, not final. Legal risk status: **KNOWN RISK — NOT YET PROFESSIONALLY CLEARED**, attorney engagement deliberately deferred to a later venture stage per founder instruction.

## SECOND

**ELOWEN — conditional.** 68.8% on the same matrix. Strongest on clinical credibility and multi-venue scalability. Its own conflict (an unregistered WA counselling business, same state, occupied domain) is real but lower-severity than Solena's registered mark.

## THIRD / RULED OUT ON EVIDENCE, NOT DISMISSED WITHOUT A FAIR HEARING

**ELOWYN — 65.9%.** Given a full Phase 2 treatment (`docs/naming/NAMING-FINAL-COMPARISON.md` §1) specifically because it was dropped after Phase 1 without one. Confirmed the cleanest of the three on trademark grounds by a clear margin, and confirmed — independently, by two separate design passes — to carry a severe, structural referral/spelling weakness ("must be spelled out on every phone call and referral pad") that a warmer visual treatment does not fix. Evaluated fairly, not chosen, and not eliminated on Phase 1's word alone either.

## DECISION BLOCKERS

- **Trademark attorney clearance — deliberately deferred, not a current action item.** `docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md` is written and ready for all three names, including a specific question on whether AU 2202790 (SOLENA, Class 3) blocks Class 44 services use. Per explicit founder instruction (2026-08-14), no attorney is being engaged or paid at this venture stage — the brief is prepared and held for a later validation/funding milestone. Legal status remains **"KNOWN RISK — NOT YET PROFESSIONALLY CLEARED,"** not "clear," "safe," or "registrable," and should not be represented as anything more than that in any document.
- ~~Founder decision: is a name-branded retail/product line a real 1–3 year ambition?~~ **ANSWERED 2026-08-14: NO / not a priority.** Third-party resale (Gaia, Weleda, Mustela) remains the retail strategy. Per the founder's own instruction, this question is not to be reopened unless the business model changes. See `docs/naming/NAMING-FINAL-COMPARISON.md` §0 for the updated weighting this produces.
- **Git/repository access** — see §Environment Note below. New naming and strategy documents exist locally and are not yet committed/pushed.

## CONFIRMATIONS — I5/I6, 2026-08-16 (simple confirmations, not new work)

- **I5 — name-agnostic strategy is the actual approach, confirmed.** Brand/experience work (`docs/strategy/`, `docs/experience/`) is genuinely built to apply to either SOLENA or ELOWEN unchanged — it is not being quietly rebuilt around one name. Naming itself is narrowed to these two finalists (ELOWYN evaluated fairly and set aside, per §3/§THIRD above), not reopened.
- **I6 — reaffirmed:** any local working material belongs in this repository — already the standing rule (see the Environment Note below for the one historical exception, now resolved).
- **I3 answered separately, in full:** `docs/naming/NAMING-SCORE-IMPROVEMENT-ANALYSIS.md` — how the current percentages could move, whether a stronger already-investigated name exists (yes, SOLENNE, correctly excluded for a real Adelaide conflict), whether higher-scoring uninvestigated names exist (not evaluated, no basis to reopen the search).
- **G9/I1/I2/I4 answered together:** `docs/naming/TRADEMARK-ATTORNEY-DECISION-BRIEF.md` — what the existing research establishes, what genuinely remains uncertain, the actual SOLENA risk level in plain terms, and the useful-certainty-vs-mandatory-requirement distinction, left for the founder to decide.

## COMPLETED

- Naming exploration (frozen seven-candidate shortlist)
- Phase 1 design exploration ("Brand Worlds — Elowen vs Elowyn vs Solena")
- Phase 2 design exploration ("Elowen vs Solena — Decision Board")
- Strategic Handover & Decision Audit (`docs/naming/SOLENA-ELOWEN-STRATEGIC-HANDOVER-DECISION-AUDIT.md`)
- Elowyn Phase 2 written evaluation and fair three-way comparison (`docs/naming/NAMING-FINAL-COMPARISON.md`)
- Trademark clearance brief, sharpened with explicit Class 44/Class 3 questions (`docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md`)
- Retail/product-line strategy check against source documents (finding: not currently a confirmed business commitment)

## NEXT

1. **Not yet** — sending `AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md` to an attorney. Deliberately deferred per founder instruction (2026-08-14) to a later validation/funding milestone; no money authorised for professional trademark clearance at this venture stage. The brief remains fully prepared for that point.
2. ~~Founder decision on the retail/product-line question~~ — answered (NO / not a priority), see above.
3. Proceed into name-agnostic brand strategy and customer-experience development (`docs/strategy/`, `docs/experience/`) — this can and should continue while the name stays conditionally open, since it's built to work for either Solena or Elowen.
4. Final naming decision — held until (a) an attorney engagement is authorised and completed at the appropriate venture stage, or (b) the founder decides the residual documented risk is acceptable to proceed on before then. Not decided in this document.

## DO NOT START YET

- Final identity lock (logo, palette, type system) for any of the three names
- Extensive brand guidelines
- Final signage
- Final packaging
- Production website
- Large-scale visual implementation of any kind

Exploratory/comparative work (like the Phase 1/Phase 2 boards and the Elowyn Phase 2 write-up) is fine and has been done. Production-level commitment to any single name is not yet justified.

---

## Environment Note

The repository mount used by Claude Cowork in this session has a recurring, unresolved filesystem-level permission restriction preventing git commits/pushes (a `.git/index.lock` file that cannot be deleted or cleared from this side, even moments after appearing cleared). This is not a normal repository-state issue and has not been resolved by retrying. **No destructive git operations have been attempted, and none are planned.** The following files exist, complete, in the local working folder and are not yet committed:

- `docs/naming/NAME-INVESTIGATION-REPORT.md` (previously committed — unaffected)
- `docs/naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md` (updated 2026-08-14, not yet committed)
- `docs/naming/SOLENA-ELOWEN-STRATEGIC-HANDOVER-DECISION-AUDIT.md` (new, not yet committed)
- `docs/naming/NAMING-FINAL-COMPARISON.md` (new, not yet committed)
- `docs/naming/NAMING-DECISION-STATE.md` (this file, new, not yet committed)

Grace, working from a separate VSCode/SSH session on the server, does not share this mount's restriction and should commit these files (or their equivalent content, cross-checked against this list) the next time she has write access, per her role as implementation/repository owner.
