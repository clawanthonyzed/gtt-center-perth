# GTT Center Perth — Project Timeline (Milestone Sequence)

**Version:** 1.0 | **Date:** 2026-07-19 (Phase 7 new deliverable)
**Purpose:** A Gantt-style relative-sequencing milestone view, reflecting `docs/04_roadmap_next_steps.md`'s dependency tiers as a visual/sequential timeline. **No calendar dates** — per standing instruction, no launch date is set; this reflects relative order and dependency, not a schedule. Distinct from `venture-timeline.md` (an earlier week-numbered phase plan that still carries some illustrative calendar dates from a prior planning pass, and from `04_roadmap_next_steps.md` (a dependency-tier action list, not a visual timeline).

---

## How to Read This

Each row is a milestone or workstream. The "Depends On" column shows what must complete first. The "Relative Position" column gives an ASCII Gantt-style bar showing roughly where each item sits relative to the others — **the horizontal position is relative sequencing, not a calendar week.** Workstreams shown on the same row-group can run in parallel.

```
Legend: [====] = duration of this workstream, relative to others
        ---->  = waiting/blocked, no active work happening
```

---

## Stage 0 — Currently In Progress (No Location Yet)

```
WDP outreach            [==================>-------------------------------------]
                         (emailed, awaiting reply — can continue indefinitely
                          in parallel with everything else in this stage)

Venue location search    [==================================>--------------------]
                         (active search — this is the actual gate for Stage 1)

King Edward guidance     [====>--------------------------------------------------]
                         source-check (low effort, can close out any time)
```

**Nothing in Stage 1 begins until "Venue location search" completes.** This is the single most consequential dependency in the entire timeline.

---

## Stage 1 — Triggered by Venue Location Confirmation

```
Depends on: Venue location search (Stage 0) = DONE

Venue Manager recruitment           ---->[=========================>-------------]
  (job posting ready in advance,          (first hire once triggered)
   docs/venue-manager-job-posting.md)

Lease signing / heads of agreement  ---->[=================>----------------------]

Fit-out planning + quotes           ---->      [===============>------------------]
  (can start once lease/HOA is in progress, doesn't need to wait for full
   lease execution)
```

---

## Stage 2 — Triggered by Venue Manager Being Hired

```
Depends on: Venue Manager recruitment (Stage 1) = DONE

Phlebotomist recruitment            ---->[==================>--------------------]
  (`phlebotomist-job-posting.md` ready in advance, same location-gating rule
   applies per that document's own sequencing update)

Other staff recruitment             ---->      [================>----------------]
  (massage, nail, hair, beauty, reception — see staff-plan.md §7 hiring order)

Employment contracts / solicitor    ---->[==================>--------------------]
engagement                              (can run in parallel with recruitment,
                                          not strictly sequential)
```

---

## Stage 3 — Triggered by Fit-Out Completion + Staff Hired

```
Depends on: Fit-out (Stage 1) = DONE, Staff hired (Stage 2) = DONE

Pathology partner site inspection   ---->[===========>---------------------------]
  (collection room compliance sign-off — depends on WDP/partner agreement
   AND physical fit-out both being complete)

Staff training / onboarding         ---->      [===========>--------------------]

Pre-launch marketing / waitlist     [==========================================>]
  (this can and should start much earlier — see note below, it is NOT
   gated the same way as the operational items above)

Test operations runs                ---->            [========>------------------]

Soft open (waitlist priority)       ---->                  [======>--------------]

Full public launch                  ---->                        [====>----------]
```

---

## Important Exception: Marketing/Waitlist-Building Does Not Wait

**Pre-launch marketing (Instagram, waitlist capture, referral card preparation) is the one workstream in this timeline that should start as early as practical, not gated on the venue/staffing chain above.** Per `business-plan.md` §8 and `docs/referral-partnership-plan.md`, building a waitlist and referral-network relationships takes time to compound — starting this only after fit-out is complete wastes the lead time available during Stages 0-2. The named referral practices in `docs/referral-partnership-plan.md` and the marketing content plan in `poppy-marketing.md` can be prepared (though outreach itself still logically needs at least a venue suburb/name to reference) well before Stage 3.

---

## Ongoing / Not Gated on the Main Chain

These can happen at any point, independent of the location/staffing dependency chain above:

- Regulatory tracker maintenance (`docs/regulatory-accreditation-tracker.md`) — update as items progress
- Documentation currency fixes (Tier 1 items in `04_roadmap_next_steps.md` — rewriting `operations-manual.md`'s scheduling section, `workflow.md`'s staffing table, etc.)
- Financial model reconciliation (CONFLICT-08/09 in `docs/01_conflicts_log.md`)
- Package price-increase timing decision (`docs/price-increase-comparison.md`) — this is a Stage-3-or-later decision in practice (no point raising prices before there's a live venue), but the analysis itself doesn't need to wait

---

## Growth-Stage Milestones (Beyond Initial Launch — Not Yet Committed)

```
Depends on: Full public launch (Stage 3) = DONE, plus a period of stable
            trading (no specific duration committed — see below)

Scenario D activation                    ---->[future — not yet triggered]
  (15-client growth model, 3rd phlebotomist — see scenario-d-investigation.md.
   Gated on demand data + resolving the King Edward guidance question for
   Scenario D specifically, and the treatment-staff-side verification caveat
   noted in am-capacity-weekend.md.)

Second venue                             ---->[future — not yet triggered]
  (Per Anthony's direct confirmation: timing is set only after Venue 1 is
   running smoothly — no earlier estimate exists, and none should be implied
   here. See docs/05_open_questions_for_founder.md Q8.)
```

---

## What This Document Deliberately Does NOT Include

- **No calendar dates.** `venture-timeline.md` still carries some illustrative Week-N/Month-N calendar references from an earlier planning pass (e.g. "Week 20, October 2026") — those are historical artifacts of an earlier draft, not a committed schedule, and are not repeated here.
- **No specific duration estimates for each stage** (e.g. "Stage 1 takes 6 weeks") — since no real venue has been selected yet, any duration estimate would be a guess dressed up as a plan. The relative bar lengths above are illustrative of sequencing, not calibrated to any specific time unit.

---

## Changelog

**2026-07-19** — Created as a new Phase 7 deliverable. Built directly from `docs/04_roadmap_next_steps.md`'s dependency tiers, translated into a Gantt-style relative-sequence view per the Phase 7 spec's request for "rough relative sequencing (not calendar dates)." Distinct from `venture-timeline.md` (earlier week-numbered plan with some legacy calendar dates) and `04_roadmap_next_steps.md` (tiered action list, not a visual timeline) — cross-references both rather than duplicating their content.
