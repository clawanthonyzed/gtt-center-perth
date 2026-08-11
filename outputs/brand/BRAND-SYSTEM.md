# Brand System — Minimum Viable Identity, Production Build

**Status: WORKING PLACEHOLDER NAME throughout ("GTT Center Perth"). Not a final business name — Anthony's own decision, on his own timeline, per `docs/brand-guide.md`'s standing governance. Every asset in this system is built so the real name can be dropped in cleanly once chosen — see §7.**

**Phase:** Market Validation Preparation — creative production. Builds directly on `docs/architecture/BRAND-IDENTITY-FRAMEWORK.md`, `docs/architecture/MINIMUM-VIABLE-BRAND-IDENTITY.md`, `docs/architecture/CONCEPT-VISUALISATION-BRIEF.md`, `docs/architecture/MVP-BRAND-LAUNCH-PACKAGE.md`, `docs/architecture/WAITLIST-VALIDATION-FRAMEWORK.md` (tracker item 53), and `docs/brand-guide.md`. No canonical financial data or business assumption changed.

**Date:** 2026-08-11

---

## 0. Capability Boundary — Read This First

**No image-generation tool is available in this toolset (no Leonardo/Higgsfield/equivalent).** Checked directly: `.claude/skills/` contains no design-relevant skill (only `handoff`, `half-clone`, `review-claudemd` — all context/workflow tools). This machine has ImageMagick (`magick`) and Python Pillow available for raster *conversion*, and Node.js/npm if needed, but nothing that generates illustration, photography, or pictorial artwork from a prompt. **Given this, everything in this system is typography, colour, and code — no illustrated mark, no photography, no AI-generated people.** This is the deliberate, disclosed scope of what was built, not a shortcut around a missing tool.

**One real, disclosed tooling limitation hit during production:** ImageMagick's built-in SVG renderer (no `rsvg-convert` delegate is installed) cannot resolve a CSS-style multi-font fallback list (`'Cormorant Garamond', Georgia, serif`) and silently substitutes a generic sans font instead — a genuine rendering defect, caught by visually inspecting the first raster output rather than assuming it worked. Worked around by rasterising with a single, ImageMagick-resolvable font name (`Georgia`, itself `docs/brand-guide.md`'s own designated fallback font) for the PNG exports specifically, while the source `.svg` files keep the full, correct CSS font stack for real browser use. **A human designer with real design software (or a proper `rsvg-convert`/headless-browser rendering pipeline) would still be needed to produce true Cormorant Garamond raster exports** — the PNGs in this folder are Georgia-rendered, not Cormorant-Garamond-rendered, and this is stated plainly, not glossed over.

---

## 1. Creative Directions Explored

Three genuinely distinct strategic directions were developed and evaluated against the target customer, positioning, and the explicit "avoid" list — not superficial colour/font variations of one idea.

### Direction 1 — Editorial Warmth
A refined serif wordmark (Cormorant Garamond, already `docs/brand-guide.md`'s established display face), no symbol at all — pure typography carrying the entire identity through spacing, weight, and colour. Feels like a boutique women's-health editorial brand: literary, calm, unhurried.
- **Strengths:** matches "premium warmth" and "maternal knowing" directly; avoids every item on the ban list by construction (nothing pictorial to go wrong); genuinely distinctive against a market where wellness brands mostly default to sans-serif-plus-icon.
- **Weaknesses:** on its own, risks reading as too soft — reinforcing the "day spa, not clinic" risk `docs/brand-guide.md` §11 and `docs/architecture/MINIMUM-VIABLE-BRAND-IDENTITY.md` §1.4 both explicitly warn against, unless executed with real typographic discipline.

### Direction 2 — Clinical-Calm Hybrid
A geometric sans-serif primary wordmark (breaking from Cormorant Garamond as the primary face), with Cormorant reduced to a secondary tagline role only. Deliberately leans more structured/clinical to maximise trust with a referring midwife or OB.
- **Strengths:** strongest direct answer to the healthcare-professionalism trust requirement.
- **Weaknesses:** weaker on emotional warmth on its own; the biggest structural departure from `docs/brand-guide.md`'s already-developed system of the three directions, carrying the most rebuild risk later.

### Direction 3 — Warm Minimal Mark
Keeps Cormorant Garamond as primary (closest continuity with the existing system), adds one small abstract graphic device — not a pictorial symbol, a restrained structural element (a horizon-line rule) — to give the mark more presence than pure type alone.
- **Strengths:** least "disconnected direction" risk against the existing brand-guide.md work; the device, if genuinely restrained, adds memorability without symbol-cliché risk.
- **Weaknesses:** any added element carries real risk of drifting into "decorative graphic without strategic purpose" (explicitly banned) if not executed with discipline.

---

## 2. Direction Selected — and Why

**A considered synthesis, not a single direction picked wholesale.** The brief's own explicit steer — "a strong wordmark-only identity is preferable to a weak symbolic logo" — is taken at face value: **no pictorial mark is used anywhere in this system.** That resolves Direction 2 out (it doesn't actually need a symbol either, but its whole rationale was a different primary typeface, a bigger, less-justified departure from the already-developed brand-guide.md system than the evidence required).

The executed identity is **Direction 1's pure-typography discipline, tightened using Direction 3's single structural insight** — a restrained horizon-line rule — **without introducing Direction 3's literal graphic device as a separate "mark."** Concretely: the wordmark is set in wide-tracked, uppercase Cormorant Garamond at a light-to-regular weight (never bold, never script-like), which reads as considered and quietly confident rather than delicate — directly answering Direction 1's own weakness. The single inset horizon rule beneath it (not a symbol, not a leaf, not a flower) gives the mark a stable anchor and a genuine, statable rationale (rest, a settled horizon — echoing "the wait, reimagined") without crossing into the banned territory of generic pregnancy iconography. **This is deliberately the most restrained option available, consistent with the brief's own preference for wordmark-only over a weak symbol.**

**One explicit, disclosed deviation from `docs/brand-guide.md`'s original logo spec:** that document specifies a sage leaf motif as part of the logo mark. This system does not use it — the leaf/flower category is explicitly on this phase's "avoid" list, and the brief itself instructs preferring wordmark-only over a weak symbolic logo. The colour, typography, tone, and personality system from `docs/brand-guide.md` is otherwise fully retained; only the leaf-mark element is deliberately dropped, disclosed here rather than silently changed.

---

## 3. Wordmark & Typography System

- **Primary wordmark:** `outputs/brand/wordmark.svg` — "GTT CENTER PERTH" (placeholder), Cormorant Garamond Regular (400), uppercase, letter-spacing ~0.09em, Deep Slate on light backgrounds. A single inset Sage horizon rule beneath.
- **Secondary lockup (with descriptor):** `outputs/brand/wordmark-with-tagline.svg` — adds "Perth's first GTT wellness lounge" in DM Sans beneath the rule, for contexts needing a one-line explanation (referral documents, print).
- **Compact/square mark:** `outputs/brand/mark-square.svg` and `outputs/brand/social-avatar.svg` — "GTT" (the same letters already in the working name, and the genuine clinical abbreviation this venture is built around, not an arbitrary monogram).
- **Favicon/tiny-size mark:** `outputs/brand/favicon.svg` — a single bold "G" on Deep Slate, the same graceful-degradation logic `docs/brand-guide.md` §4 already specifies for its own smallest logo variant.
- **Typefaces (unchanged from `docs/brand-guide.md` §3):** Cormorant Garamond (display, weights 300/400/600) + DM Sans (body, weights 400/500), both free Google Fonts, loaded via `<link>` in the landing page's `<head>`.
- **On the web**, the wordmark is rendered as real, styled HTML text (see `outputs/landing-page/index.html`), not an embedded image — this is the professionally correct choice for a typography-only identity (better performance, full accessibility/screen-reader support, real SEO value) and is only possible because no custom hand-drawn letterforms are involved. The `.svg` files remain the portable asset for contexts outside the live website (print, email, social).

---

## 4. Colour System — With One Accessibility Correction

`docs/brand-guide.md` §2's full palette is retained without change (Lounge White, Sage, Terracotta as accent-only, Deep Slate; Morning Blush, Forest, Parchment, Pearl). **One genuine defect found and corrected, not previously caught anywhere in this repo:** contrast-tested every likely text/background pairing directly (WCAG 2.1 relative-luminance formula, not eyeballed):

| Pairing | Ratio | WCAG AA (normal text, 4.5:1) | WCAG AA (large text/UI, 3:1) |
|---|---|---|---|
| Deep Slate on Lounge White | 12.13 | Pass | Pass |
| Deep Slate on Parchment | 10.54 | Pass | Pass |
| Deep Slate on Morning Blush | 10.01 | Pass | Pass |
| Pearl on Sage (`docs/brand-guide.md`'s own email-button spec) | **2.31** | **FAIL** | **FAIL** |
| **Deep Slate on Sage (this system's corrected CTA)** | **5.03** | **Pass** | Pass |
| Pearl on Deep Slate | 11.61 | Pass | Pass |
| Sage text on Lounge White (e.g. as a link colour) | 2.41 | FAIL | FAIL |
| Forest (deep sage) on Lounge White | 4.52 | Pass | Pass |
| Terracotta on Lounge White | 3.15 | FAIL | Pass |

**Correction applied system-wide:** every interactive Sage surface (buttons, active states) uses **Deep Slate text**, not Pearl — `docs/brand-guide.md`'s own spec fails a real, testable accessibility standard. **Sage is never used as a text colour on light backgrounds** (only as a background, border, or the horizon-rule accent) — it fails contrast as text. **Terracotta is used only for large/bold display-scale text or non-text decorative elements**, never body copy or captions, consistent with its already-existing "accent only, one element maximum" rule in `docs/brand-guide.md` §2 — now additionally justified by a real contrast constraint, not just a stylistic preference.

---

## 5. Spacing, Layout, and Supporting Graphic Language

An 8px-base spacing scale (`outputs/brand/brand-tokens.css`) is introduced — not previously specified anywhere in `docs/brand-guide.md`, disclosed as new rather than silently added. Generous whitespace throughout, consistent with the "calm, unhurried" brand pillar — no card-heavy, gradient, or icon-dense layouts anywhere in this system (all explicitly on the ban list). The **only** supporting graphic device in this entire identity is the horizon-line rule already described in §3 — used consistently as a section-divider and mark-anchor, never duplicated into a decorative pattern or repeated motif without purpose.

---

## 6. Imagery Direction — A Brief, Not Produced Imagery

**No photography or illustration is produced by this system — that capability genuinely does not exist in this toolset (§0).** `docs/architecture/CONCEPT-VISUALISATION-BRIEF.md` already specifies the full illustration brief for when a professional illustrator/photographer is engaged. For the landing page specifically, **no placeholder photography or generic stock imagery is used either** — a genuine, deliberate design decision, not a gap: a typography-and-colour-led hero section (real content, real craft) reads as more considered and premium than an empty grey placeholder box or a generic stock photo that risks looking like template filler, and avoids any risk of the "obviously-AI-generated people" or "generic stock imagery" failure modes on the ban list entirely.

---

## 7. Application Testing

**Actually built** (real files in this repo): website header (`outputs/landing-page/index.html`, styled HTML text), mobile header (same file, responsive), favicon (`favicon.svg` + rasterised `.png`), social/Instagram avatar (`social-avatar.svg` + rasterised `.png`), email header (`email-header.html` + `email-header-wordmark.png`).

**Described, not built** (genuinely need a human designer, real photography, or a confirmed venue before they can exist for real):
- **Referral partner document:** use `wordmark-with-tagline.svg` at the header, Deep Slate/Sage/Lounge White only (no Terracotta), restrained layout per `docs/architecture/MINIMUM-VIABLE-BRAND-IDENTITY.md` §3's own healthcare-professional-audience nuance — minimal to no imagery, plain-language copy.
- **Signage:** `docs/brand-guide.md` §9 already has a full spec (etched aluminium, brushed plate) — venue-dependent, cannot be produced without a confirmed site, correctly out of scope for this phase.
- **Print collateral (business cards, referral cards):** `docs/brand-guide.md` §7 has the full spec — venue-address-dependent, correctly deferred per `docs/architecture/MVP-BRAND-LAUNCH-PACKAGE.md` §3.
- **Physical clinic environment:** the wordmark and horizon-rule motif would translate as a single, quiet reception-wall treatment (etched or painted, not a lit sign) and the same device echoed subtly in the curtain-track hardware finish (a real, low-cost way to extend the identity into the built environment without introducing a new symbol) — a direction note for the future interior designer/architect (`docs/architecture/CONCEPT-DESIGN-BRIEF.md`), not something this document builds.

---

## 8. Usage Guidance — Basics

- **Minimum clear space:** the height of the wordmark's own cap-height, on all sides — unchanged principle from `docs/brand-guide.md` §4.
- **Never** stretch, distort, recolour the horizon rule to a non-Sage colour, add a drop shadow, add a border/box around the wordmark, or place it on a busy photograph (moot for now, since no photography exists in this system yet).
- **Never** use Pearl text on Sage (§4's corrected finding) or Sage text on a light background.
- **Do not** introduce a second graphic device — the horizon rule is the only one, by design.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified. No business name was selected — every asset uses the working placeholder, structured for a clean swap (see the single `--business-name` token in `brand-tokens.css` and the header comments in every `.svg` file).
