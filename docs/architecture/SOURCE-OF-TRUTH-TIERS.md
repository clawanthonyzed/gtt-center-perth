# Source-of-Truth Tier Hierarchy

Status: current as of 2026-08-22. This is deliberately one short document, not a new layer of bureaucracy: its only purpose is to state, once, which sources override which, so old information stops resurfacing as though it were current.

## The 4 tiers

**Tier 1: Founder-confirmed current decisions.** Anything Anthony has directly confirmed in the current conversation or a dated, current instruction. Overrides every other tier automatically, including this document's own defaults.

**Tier 2: Canonical/current operating and financial models.** `docs/CURRENT-STATE.md`, `data/canonical/*.yml`, `data/models/master_financial_model.yml`, and the specific architecture documents those files cite as their own current basis (for example `docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md`, `docs/architecture/STAFFING-COVERAGE-VALIDATION.md`, `docs/architecture/FIT-OUT-PROGRAM-DECISION-ANALYSIS.md`). These are authoritative for any figure, headcount, or program decision unless a Tier 1 instruction has directly superseded them.

**Tier 3: Current strategic reports.** Investigation and research documents that are dated and still current (for example this session's `docs/architecture/MARKET-RESEARCH-BIRTHS-GDM-REFERRAL-2026.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`). These inform Tier 2 documents but do not themselves override a Tier 2 figure without that figure being updated to match.

**Tier 4: Supporting research.** Everything else in `docs/` and `docs/architecture/` not listed above. Treated as historical/stale unless a specific document is explicitly revalidated and promoted into Tier 2 or Tier 3 by a dated changelog entry.

## The rule

If a Tier 4 document contradicts a Tier 2 or Tier 3 document, the Tier 4 document is stale. The correct action is to update the Tier 4 document itself (or mark it superseded in its own changelog) so it stops contradicting current truth, not to keep disclosing the contradiction every time the topic comes up in the dossier or Dash. The Master Dossier and Dash draw only from Tier 1-3; Tier 4 documents should not be cited as a current source in either.

## What this replaces

Before this document, current-state governance was implicit: `docs/CURRENT-STATE.md` was understood as authoritative but nothing stated the tier relationship for architecture-level research documents versus older strategy documents versus one-off investigation notes. This caused the same historical contradiction (old property listings, old staffing figures, old pricing methodology, spray tan, the GDM snack pack) to be re-discovered and re-disclosed in the dossier repeatedly across sessions instead of being fixed once at the source.

## Known Tier 4 documents with unresolved stale content, not yet cleaned up

This is an honest, explicit gap list, not a claim that the problem is solved. The following documents still contain spray tan and/or GDM snack pack references that have not been individually reviewed and cleaned this round (the dossier and Dash themselves are clean, verified 2026-08-22): `docs/architecture/CANONICAL-DATA-POC.md`, `docs/architecture/CANONICAL-DATA-SCHEMA.md`, `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`, `docs/architecture/DOSSIER-CURRENT-STATE-RECONCILIATION-MATRIX.md`, `docs/architecture/FINANCIAL-MODEL-DECISION-REVIEW.md`, `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md`, `docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`, `docs/architecture/MASTER-DOSSIER-ARCHITECTURE.md`, `docs/architecture/REVENUE-ASSUMPTION-AUDIT.md`, `docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md`, `docs/architecture/SERVICE-CATALOGUE-AUDIT.md`, `docs/architecture/STARTUP-COST-OPTIMISATION.md`, `docs/architecture/startup-cost-reconstruction.md`, `docs/CURRENT-STATE.md`, `docs/FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md`, `docs/VERIFICATION-TRACKER.md`, `docs/cash-flow.md`, `docs/equipment-costs.md`, `docs/extended-wellness-services.md`, `docs/financial-break-even-staff.md`, `docs/floor-plan-concept.md`, `docs/grace-startup-plan.md`, `docs/hire-purchase-china.md`, `docs/investor-memorandum.md`, `docs/market-research-findings.md`, `docs/onboarding.md`, `docs/pm-staffing-roster.md`, `docs/profit-loss-tables.md`, `docs/research.md`, `docs/services-pricing-locked.md`, `docs/swot-analysis.md`, `docs/venture-timeline.md`. Most of these already frame the item as historical/excluded rather than current, which is a materially lower-severity issue than it appearing as current, but the founder instruction is that it should not appear at all, even as history, in current planning materials. Reviewing and cleaning all of these individually is a real, bounded follow-up task, not yet done.

## Changelog

**2026-08-22 (created):** Written per direct founder instruction to establish a governance tier hierarchy that prevents old information from resurfacing as current, without creating a new layer of bureaucracy. Deliberately short. Includes an honest gap list of Tier 4 documents not yet individually cleaned of spray tan/snack pack references, rather than claiming the problem fully solved.
