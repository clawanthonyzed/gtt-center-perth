# Minimum Viable Brand Launch Package

**Phase:** Market Validation Preparation. Objective: identify the smallest professional asset package capable of validating demand (hitting the 500-700 waitlist go/no-go threshold, `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md`) before signing a lease — not the full brand/launch build-out. **No name selected, no final branding created, no financial/canonical model touched.** No WDP communication drafted or sent — tracker item 50 untouched, still awaiting Carole's reply.

**Date:** 2026-08-10
**Reviewed before writing, per instruction:** `docs/architecture/BRAND-IDENTITY-FRAMEWORK.md`, `docs/architecture/BRAND-CUSTOMER-LAUNCH-ROADMAP.md`, `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md`, `docs/architecture/CONCEPT-VISUALISATION-BRIEF.md`.

---

## 1. Customer-Facing Assets Required to Hit 500-700 Waitlist Signups

### 1.1 Landing Page

**Minimum requirements**, reusing `docs/poppy-marketing.md` §6's existing brief where it already applies:
- Single, lean, mobile-first page (no full website build required at this stage — see §3)
- Placeholder-brand visual treatment (`docs/brand-guide.md`'s own colour palette, typography, and logo mark — explicitly usable as working material, not a final identity)
- Positioning statement and customer promise, verbatim from `docs/architecture/BRAND-IDENTITY-FRAMEWORK.md` §2/§5, not rewritten
- A short "how it works" explainer in plain language (GTT wait, reframed) — 2-3 sentences, not a full service menu (nothing is bookable yet)
- Waitlist signup form (see §1.4)

### 1.2 Brand Messaging — Using What's Already Established, Nothing New Invented

Directly reused, not created fresh:
- **Positioning statement** (`docs/architecture/BRAND-IDENTITY-FRAMEWORK.md` §2): "Western Australia's first venue built specifically around the mandatory GTT wait..."
- **Differentiators** (§4 of the same document): no direct WA competitor, multi-client concurrent capacity, full-service breadth, clinical credibility without clinical coldness.
- **Tone of voice** (`docs/brand-guide.md` §1, confirmed unchanged): calm, confident, warm, never alarming, no "amazing/incredible/game-changer/journey."
- **No name is used as a locked identity anywhere in this package** — the working placeholder ("GTT Center Perth") is used exactly as `docs/brand-guide.md` itself already sanctions, with no implication it is final.

### 1.3 Customer Value Proposition

Restated once, for direct landing-page use, from `docs/architecture/BRAND-IDENTITY-FRAMEWORK.md` §5's customer promise: **"You're growing a human. Your GTT morning deserves to be calm, cared for, and genuinely yours — not just endured."** Paired with the plain-language "how it works" explainer (§1.1) so the value proposition is immediately followed by a concrete picture of what it means in practice.

### 1.4 Waitlist Signup Flow

**Kept deliberately lean for conversion — validation depth moved to an optional follow-up, not the primary form (see §1.8):**
- First name
- Email
- Suburb (validates the Perth-metro/drive-time assumption, and is a genuine, real data point for future venue-site selection)
- Due date or weeks pregnant (validates whether real signups sit in the 24-28-week GTT window this venture is built around, or skew outside it)
- How did you hear about us (validates which acquisition channel is actually working, directly informing `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md`'s own channel-weighting assumption)

**One correction carried forward from the prior phase, applied here:** the service-interest checkboxes must list only current launch-scope services (massage, nails, brows, hair) — `docs/poppy-marketing.md` §6's own existing brief still lists "3D scan, dietitian," both out of scope, already flagged in `docs/architecture/BRAND-CUSTOMER-LAUNCH-ROADMAP.md` §3 and not repeated as new here.

### 1.5 Referral Partner Information Pack

A single-page, professional overview for the 22 named practices (`docs/poppy-marketing.md` §1: 12 midwifery, 10 OB/GYN) — needed to START outreach, per `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md`'s own recommendation that this begin early even though it is a Month 2+ contributor, not a Month 1 lever. Contents: the positioning statement (§1.2), a plain description of the model (pathology partner handles collection, wellness happens alongside), and a simple referral mechanism (a QR code or short URL to the same waitlist landing page — not a separate referral-specific system). **No pricing commitment or formal partnership terms in this pack** — that remains a separate, not-yet-drafted step once real relationships exist.

### 1.6 Social Media Launch Requirements

Minimum, not the full `docs/brand-guide.md` §10 Week-7 asset set: an Instagram account using the placeholder brand, profile image (leaf mark, already spec'd), and a reduced-cadence content presence — `docs/poppy-marketing.md` §5's full 12-week content calendar can wait (see §3); a lighter, honest "we're building this" cadence is sufficient for the pre-lease validation window, consistent with `docs/architecture/BRAND-CUSTOMER-LAUNCH-ROADMAP.md` §4's own recommendation to bring forward a lightweight presence, not the full build-out.

### 1.7 Email Capture Strategy

Resend (free tier, 3,000 emails/month, already identified in `docs/poppy-marketing.md` §7) for a single welcome email confirming signup and setting expectations ("we'll contact you first when bookings open") — the full multi-email nurture sequence can wait until closer to a confirmed opening date, since promising specific timing this early risks over-committing before a lease is even signed.

### 1.8 Customer Survey/Questions — Validating the Model, Not Just Counting Heads

**This is the part of the package that does more than measure demand volume — it is a genuine opportunity to sanity-check assumptions already disclosed as unresolved elsewhere in this repo.** Kept as an **optional, short follow-up** (sent after signup, not blocking the lean primary form in §1.4, to protect conversion) — 4-5 questions, each tied to a specific, named model assumption:

| Question | What it validates |
|---|---|
| "Which package sounds right for you — a focused 2×30-min visit, or a longer, more flexible session?" (described in plain language, not by package name/price) | Tests real interest distribution between AM Package 1 (A$250) and Package 2 (A$300) — the model currently uses A$250 as a deliberate conservative safety price for every revenue calculation (`data/canonical/pricing.yml#am_price_used_for_revenue`), not a blended average; real signal on actual package preference is a genuine, currently-absent data point. |
| "Which afternoon services would you be most interested in — massage, nails, hair, or brows?" | Tests the PM service-mix assumption embedded in the current 1-per-line PM staffing structure (`data/canonical/staffing.yml`) — a real, lopsided demand signal (e.g. heavy skew to one service) would be a genuine, actionable finding against the current evenly-split staffing plan, not something this repo has any evidence on today. |
| "If you were booking an afternoon service, roughly what would you expect it to cost?" | A very rough, directional check against the PM a-la-carte average (A$95/session, `data/canonical/pricing.yml#pm_alacarte_average`) — explicitly not a substitute for real pricing research, but a first, cheap data point where none currently exists. |
| "Have you already had your GTT test, or is it still coming up?" | Tests a genuine timing-urgency risk not previously flagged anywhere in this repo: if a meaningful share of engaged signups have already completed their test elsewhere by the time this venue could realistically open, that is a real signal about the achievable conversion window, distinct from the conversion-rate assumptions already flagged as unevidenced in `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md` §2. |
| "Would a discount for booking an afternoon service at the same time as your GTT appointment make you more likely to book both?" | Directly tests `docs/VERIFICATION-TRACKER.md` item 39 (the 10% PM pre-booking discount, never applied to any current revenue figure) — a genuine, cheap way to gather real evidence on an already-flagged open question, rather than leaving it permanently unevidenced. |

**None of these questions' answers are wired into the financial model by this document** — they are identified as valuable data collection points; acting on the results (e.g. adjusting the PM staffing mix, or revisiting the pre-booking discount question) would be a separate, future, evidence-based phase, not something this document does.

---

## 2. Minimum Viable Asset List

| Asset | Required to hit 500-700 waitlist | Status |
|---|---|---|
| Lean landing page (placeholder brand) | **Yes — true minimum** | Not yet built |
| Positioning/value-prop copy | **Yes — true minimum** | Already written (§1.2/1.3), ready to use |
| Lean waitlist signup form | **Yes — true minimum** | Field list defined (§1.4), not yet built |
| Optional validation follow-up survey | **Yes, as a post-signup add-on** | Question set defined (§1.8), not yet built |
| Basic Instagram presence (placeholder brand, reduced cadence) | **Yes — true minimum** | Account not yet created |
| Email welcome message (Resend) | **Yes — true minimum** | Not yet built |
| Referral partner info pack | **Yes, for the outreach track specifically (not the landing page)** | Not yet built |
| Stock photography (brand-guide-approved sources) | **Yes, as a substitute for commissioned imagery at this stage** | Not yet sourced |
| Full custom concept illustrations (`docs/architecture/CONCEPT-VISUALISATION-BRIEF.md`) | No — can wait | Brief exists, illustrations not commissioned |
| Full website (service menu, FAQ, About, Fresha booking widget) | No — can wait | Platform recommendation exists (`docs/poppy-marketing.md` §4), not built |
| Full 12-week content calendar cadence | No — can wait | Calendar exists (`docs/poppy-marketing.md` §5), not yet executed at full cadence |
| Physical print (business cards, referral cards, menu cards, price display) | No — can wait | Specs exist (`docs/brand-guide.md` §7), nothing printed |
| Final logo/full brand identity | No — cannot be built until naming is decided | Explicitly Anthony's own process, not this repo's to build |
| Signage/wayfinding | No — needs a confirmed venue | Specs exist (`docs/brand-guide.md` §9), not actionable yet |

---

## 3. What Can Wait Until After Venue Confirmation

- Full custom concept illustrations — commission once approaching a landlord specifically, or once the pre-lease waitlist signal justifies the investment (a `docs/architecture/CONCEPT-VISUALISATION-BRIEF.md`-ready brief already exists, no further preparation needed to commission it when the time comes).
- Full photography shoot — genuinely cannot happen without a real venue to photograph, per `docs/brand-guide.md` §5's own Week 14 shoot timing.
- Full website build beyond the lean landing page — nothing is bookable before a venue and booking system exist; a full site with an embedded Fresha widget would be built against a booking system that isn't live yet.
- Print collateral (business cards, referral cards, menu cards, price display) — premature without a confirmed venue address, and `docs/brand-guide.md` §7 itself notes the referral card's back content includes "Address (once known)."
- Signage and wayfinding — inherently venue-dependent.
- The full 12-week content calendar's complete cadence — a lighter, honest pre-venue presence (§1.6) is the right scale for this stage; the full cadence is better spent once there is a real fit-out story and, eventually, a real opening date to build toward.

---

## 4. What Should NOT Be Built Yet — Explicit, Protecting Against Over-Investment

Consistent with the MVP-cost-discipline thread already established across this whole effort (`docs/architecture/STARTUP-COST-OPTIMISATION.md`, `docs/architecture/MVP-OPENING-DECISION-REVIEW.md`):

- **No final brand name, logo, or full identity system.** Explicitly out of scope this phase and every phase before it — `docs/brand-guide.md`'s placeholder system is the correct, already-sanctioned tool for this entire validation window.
- **No paid advertising spend beyond the already-approved trigger.** `docs/architecture/MVP-OPENING-DECISION-REVIEW.md` §2.3 already established a A$1,000 marketing contingency reserve, held not spent, released only on a real booking-vs-ramp trigger — that trigger has not fired, and this document does not propose spending it now.
- **No physical print collateral.** Building 500 business cards or 200 referral cards against a venue address that doesn't exist yet is a genuine waste risk, not a hypothetical one.
- **No booking-system integration (Fresha).** There is nothing to book yet — integrating a live booking system this early would create a false impression of operational readiness to a waitlist audience.
- **No full custom photography shoot.** No venue exists to photograph; brand-guide-approved stock photography (§1, already an approved source per `docs/brand-guide.md` §5) is the correct substitute until one does.
- **No specific opening-date commitment communicated to the waitlist.** Consistent with `docs/business-plan.md` §8's own standing instruction that no calendar launch date is set — the welcome email and landing page should promise "we'll contact you first when bookings open," not a date.
- **No commissioned custom concept illustrations yet**, even though the brief is ready — this is a real, disclosed judgment call: stock photography is a genuine, brand-guide-approved substitute for the pre-lease validation window specifically, and commissioning custom illustration work before demand is validated (or before a landlord conversation specifically needs it) would be spending ahead of evidence, the exact pattern this whole effort has consistently avoided elsewhere.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. No brand name was selected, no final branding was created — every asset recommendation above uses the existing placeholder system or explicitly-approved stock-photography fallback (see full validation summary in this phase's combined report-back).
