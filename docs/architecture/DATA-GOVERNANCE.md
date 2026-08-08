# GTT Center Perth — Data Governance

**Purpose:** define the extended status vocabulary for `data/canonical/*.yml` (see `CANONICAL-DATA-SCHEMA.md`), and reconcile it explicitly against the existing 3-status system already in force via `rules/CLAUDE.md` and `docs/CURRENT-STATE.md`. **This document extends the existing system — it does not replace it, and `rules/CLAUDE.md` is not modified by this phase.**

---

## 1. The Existing System (unchanged, still in force)

`rules/CLAUDE.md`'s "Hard Rule — No Figure Without a Tag" defines three statuses, in force today across every `docs/*.md` file:

| Existing tag | Meaning |
|---|---|
| `[VERIFIED — source, date]` | Confirmed by an external party (a real WDP/PathWest/Clinipath reply, a signed quote, an accountant/solicitor confirmation, or a programmatic scheduling simulation that is itself the primary source) |
| `[MODELED — assumption: <name it>]` | Internally calculated from other modeled or verified inputs |
| `[PLACEHOLDER — not yet known]` | A genuine unknown, or a fact that conflicts across this repo's own documents and has not been reconciled |

This system is working and is not being replaced. It stays exactly as-is for every existing `docs/*.md` file.

---

## 2. The Problem This Document Solves

Reading `docs/CURRENT-STATE.md` closely (see `REPOSITORY-AUDIT.md`) shows `[MODELED]` is currently doing four genuinely different jobs at once:

1. **A plain, undisputed arithmetic step** — e.g. "Quarterly = Monthly × 3" (`CURRENT-STATE.md` §5). Nothing modeled here in the colloquial sense; it's just multiplication of already-settled numbers.
2. **A founder decision that isn't a calculation or an external fact at all** — e.g. "no price increase until 12+ months' trading" (item 36), "full prepayment, no deposit" (item 39). These are choices Anthony made, not things that were computed or externally confirmed.
3. **A genuine assumption-based estimate** — e.g. "~50% utilisation of theoretical 4-line capacity ... no real demand data exists yet" (§3). This is the sense `rules/CLAUDE.md`'s own definition describes.
4. **A clearly-labelled alternative that was never adopted as the committed baseline** — e.g. Table 2 (12-client/08:00) sits right alongside Table 1 (18-client/07:00) in `CURRENT-STATE.md` §1, both tagged effectively the same way, even though Table 2 is explicitly "SECONDARY reference," not the committed figure.

Collapsing all four into one tag makes it hard for a future automated check (`VALIDATION-ARCHITECTURE.md`) to tell "this is a safe, load-bearing number" from "this is one alternative among several, never adopted." A separate, real-world failure this conflation risks: a document quoting Table 2's +A$27,084.69/month figure without noting it's the secondary reference would currently pass `tools/check_consistency.py` (since that figure isn't itself in the stale-pattern list) even though it's not the committed headline. Splitting the tag makes that distinction checkable.

---

## 3. The Extended System (for `data/canonical/*.yml` only)

| New status | Reconciles to old tag | Meaning | Example from this repo |
|---|---|---|---|
| **`VERIFIED`** | `[VERIFIED]` — unchanged | Confirmed by an external party or a primary-source programmatic simulation | Carole Rivers' WDP email confirming the 10:30am start-time guidance |
| **`DECIDED`** | Was `[MODELED]`, now split out | A founder decision — not computed, not externally confirmed, simply chosen | "No price increase until 12+ months' trading" (item 36) |
| **`CALCULATED`** | Was `[MODELED]`, now split out | A deterministic arithmetic derivation from other `VERIFIED`/`DECIDED`/`CALCULATED` inputs, with no named assumption beyond the arithmetic itself | "Quarterly = Monthly × 3" |
| **`MODELLED`** | Was `[MODELED]`, narrowed to its original stated meaning | Calculated from other inputs **plus at least one named, not-yet-proven assumption** | "PM steady-state capacity — assumption: ~50% utilisation, no real demand data" |
| **`SCENARIO`** | New — previously unlabelled as a category, though the underlying idea ("secondary reference," "growth scenario, not committed") already appears throughout `CURRENT-STATE.md` in prose | A labelled what-if, explicitly not adopted as the committed baseline | Table 2 (12-client), Scenario D (15-client growth), the 36-client theoretical maximum |
| **`PLACEHOLDER`** | `[PLACEHOLDER]` — unchanged | A genuine unknown, or an unreconciled internal conflict | WDP commercial/rental figure (item 1c) |
| **`SUPERSEDED`** | New — previously handled by prose banners ("HISTORICAL, superseded") rather than a tag | A value that was once one of the above, but has been replaced; retained for trace only | The 12-client/23-min-cadence model and its 14-client ceiling |

**Reconciliation rule:** every `[MODELED]` tag already written into existing `docs/*.md` files stays exactly as it is — this phase does not retag any existing document. When a fact is migrated into `data/canonical/*.yml` in a future implementation phase, the migration step includes choosing which of `DECIDED`/`CALCULATED`/`MODELLED`/`SCENARIO` it actually is, using the definitions above — this is a one-time reclassification done at migration time, not a retroactive edit of `docs/CURRENT-STATE.md`'s existing prose tags.

---

## 4. What Each Status Means for Downstream Use

| Status | May a Master Financial/Operations Model (`MODEL-ARCHITECTURE.md`) use it as an input? | May a generated document (`DOCUMENT-GENERATION.md`) present it as the headline figure? | May it appear at all in a client/investor-facing output? |
|---|---|---|---|
| `VERIFIED` | Yes, always | Yes | Yes |
| `DECIDED` | Yes, always | Yes | Yes |
| `CALCULATED` | Yes, always (it's derived from the above) | Yes | Yes |
| `MODELLED` | Yes, but the model output inherits `MODELLED` status and must carry the same named-assumption disclosure forward | Yes, but must visibly disclose the assumption (footnote/inline tag) — never presented with the same confidence as `VERIFIED` | Yes, with the assumption disclosed — never silently smoothed into an unqualified number |
| `SCENARIO` | Only inside that scenario's own labelled run — never blended into the base-case model | Only inside a clearly-labelled scenario/sensitivity section, never as "the" headline figure | Yes, but only in a section explicitly labelled as a scenario/alternative, never presented as the committed plan |
| `PLACEHOLDER` | **No.** A model must either halt/flag or explicitly route around a `PLACEHOLDER` input (e.g. surface a sensitivity range instead of a point figure) | **No, never as fact.** Must render literally as `[PLACEHOLDER — not yet known]` or be omitted | No — a fabricated-but-plausible value is explicitly worse than an honest gap, per `rules/CLAUDE.md` companion rule 5 |
| `SUPERSEDED` | **No.** Must never feed a live model run | Only inside a clearly-marked "Historical" section, for trace/context — never as a current figure | Only with an explicit "historical, no longer current" label |

---

## 5. Standing Rules (extending, not duplicating, `rules/CLAUDE.md`)

1. **`rules/CLAUDE.md`'s hard rule still applies at the document level unchanged**: no figure in a `docs/*.md` file without one of the original 3 tags. This document adds a *finer-grained* internal classification for the future `data/canonical/*.yml` layer specifically — it is an elaboration for machine-readable data, not a second, competing rule for prose documents.
2. **`SCENARIO` must always be explicitly labelled as such wherever it appears**, including in generated documents — a scenario figure with the label stripped is functionally the same failure `rules/CLAUDE.md` was created to stop (a modeled number presented as settled fact), just one level more subtle (an alternative presented as *the* plan).
3. **`PLACEHOLDER` must never present as fact anywhere** — in `data/canonical/*.yml`, in a model output, or in a generated document. This is a direct carry-forward of `rules/CLAUDE.md` companion rule 5, extended explicitly to the new data/model/document layers so the same discipline holds end-to-end, not just at the hand-authored-document layer it currently governs.
4. **`SUPERSEDED` must not feed the current model.** A `models/financial/` run that includes a `SUPERSEDED`-tagged input is a bug, catchable by the schema/model validators proposed in `VALIDATION-ARCHITECTURE.md` (a model input resolver that filters to non-`SUPERSEDED` records only). `SUPERSEDED` records stay in `data/canonical/*.yml` (not deleted) purely for the historical trace `CURRENT-STATE.md` already provides in prose — the machine-readable layer keeps the same "never delete, mark superseded" convention already in force.
5. **A `DECIDED` record requires no re-justification.** Unlike `MODELLED`, a `DECIDED` fact (a founder choice) does not need an assumption disclosed — it needs only its source (who decided, when) — because it isn't a prediction subject to being wrong, it's a decision that could in principle be revisited but isn't currently in question.
6. **Every `PLACEHOLDER` record in `data/canonical/*.yml` must have a matching row in `docs/VERIFICATION-TRACKER.md`.** This is the same rule already governing `docs/*.md` files, extended to the data layer, so the single open-items ledger stays genuinely single rather than fragmenting into a docs-layer list and a separate data-layer list.

---

## 6. What This Document Does Not Do

It does not retag any existing `docs/*.md` figure, does not create `data/canonical/*.yml` files, and does not modify `rules/CLAUDE.md`. It is a forward design for how the existing, working 3-status discipline extends cleanly into the machine-readable canonical-data layer once that layer is built.
