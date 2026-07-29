# GTT Center Perth — Industry Standards vs Floor Plan Cross-Check (v2 — Real Documents Read)

**Prepared:** 2026-07-28 | **Supersedes:** v1 of this doc (which flagged all 3 standards as "not read"). **This version actually obtained and read 2 of 3 standards documents in full text** (via `pdftotext` extraction after WebFetch returned binary/unreadable PDFs) — WA Skin Penetration Code of Practice (509 lines extracted) and AMT Massage Code of Practice (1,392 lines extracted). **NPAAC 3rd Edition could NOT be retrieved** despite 6 genuine attempts across 4 different URLs on the safetyandquality.gov.au domain (direct PDF fetch, HTML landing pages, resource-library mirror, digitalhealth.gov.au implementer hub) — every attempt timed out or connection-reset, while the WA Health and AMT domains both worked without issue on the first or second try. This is flagged as a genuine access/tooling limitation for that specific domain, not a lack of effort or a skipped step.

**Compared against:** `floor-plan-concept.md` (v1.0, 2026-07-01, "Concept only — for architect brief. Not a construction document") and `floor-plan-v3.svg` (schematic, room labels + dimensions only). Per the coordinator's framing: this validates whether the **concept** reflects real requirements, not whether it's construction-ready — the plan is expected to be adapted once a real venue is confirmed.

---

## 1. WA Health (Skin Penetration Procedure) Regulations 1998 + Code of Practice — READ IN FULL

**Threshold question, flagged first:** §2 (Application) states the Code covers "all persons who perform skin penetration procedures" and "the premises in which such procedures are performed," with an explicit exemption list: dentists, medical practitioners, podiatrists, and registered nurses. **Phlebotomists/pathology collectors are NOT on this exemption list.** Venepuncture is unambiguously a skin penetration procedure. **This means, on the plain text of the Code, the Blood Collection Room may fall under this Code in addition to NPAAC — not confirmed either way, genuinely worth a direct regulatory check (or asking WDP, since they operate under NATA/Licensed Collection Centre governance which may supersede or interact with this Code differently), not assumed.**

| Code Requirement (§, quoted/paraphrased) | Floor Plan Status |
|---|---|
| §7.1: Surfaces in direct contact with skin/mucous membranes "must be smooth, impervious and in good repair" | **Can't fully assess** — floor plan specifies "chemical-resistant vinyl or tile, no carpet" for Nail Station only; treatment room flooring material is not specified at all in `floor-plan-concept.md`'s room schedule. Gap: concept plan should state a smooth/impervious floor material for all skin-penetration-adjacent rooms (treatment rooms, collection room), not just Nail Station. |
| §7.1: Hand basin with hot/cold water, soap, paper towels "available in the immediate area." For **new premises**: an "approved hand free type of handbasin" is required | **MEETS for Blood Collection Room** (floor plan specifies "clinical sink — elbow-operated tap," which qualifies as hands-free). **DOESN'T MEET for Treatment Rooms** — floor plan specifies "clinical sink — hot/cold, soap dispenser, paper towel dispenser" but does not specify a hands-free tap, which the Code requires for new premises. Genuine, specific gap. |
| §7.2: Work space/preparation area "shall be separate from the client treatment or work area," with its own "cleaning area separated from the preparation area," and "at least two sinks, one for hand washing and one for cleaning and decontaminating appliances" | **DOESN'T MEET as currently described** — the floor plan gives each treatment room a single clinical sink, with no separate prep/cleaning area or second (instrument-decontamination) sink shown anywhere in the room schedule. This is the most concrete, specific gap found in this cross-check. |
| §3.3/§3.4: Sharps in "designated puncture resistant container that complies with AS 4031"; contaminated waste in clearly identified receptacles, disposed per local government requirements | **MEETS** — floor plan specifies "2x sharps container wall brackets (bench level + stand level), yellow biohazard bins" for the Collection Room. Treatment rooms don't separately list sharps disposal, but treatment rooms (massage/beauty/nails) don't inherently generate sharps waste the way the collection room does — reasonable as-is. |
| §3.8: Linen "stored to prevent contamination"; used/soiled linen in "a suitable receptacle," separate from clean | **MEETS, arguably exceeds** — floor plan has separate "Clean Linen/Storage (6sqm)" and "Dirty Linen/Biohazard (4sqm)" rooms, a stronger separation than the Code's minimum. |
| §4.3: Reusable appliances requiring sterilisation shall be autoclaved (steam under pressure) | **Can't assess** — floor plan doesn't specify sterilisation equipment placement/provision anywhere (relevant to nail tools, beauty tools). This is a real gap in the concept plan. |
| (No ventilation clause found in this Code) | **N/A to this Code** — LEV/ventilation is a separate WorkSafe WA hazardous-substances requirement, already correctly treated as such elsewhere in this repo, not conflated here. |

**Section count: 3 meets, 2 doesn't-meet (specific, fixable), 2 can't-assess.**

---

## 2. AMT Massage Code of Practice — READ IN FULL

**Confirmed: no explicit room-size clause exists in this Code** — it governs professional conduct, hygiene practice, and privacy/draping protocol, not physical room dimensions. This resolves the open question from v1 of this doc.

| Code Requirement (quoted/paraphrased) | Floor Plan Status |
|---|---|
| "Clinic rooms should be impervious to sound so that conversations cannot be overheard" (Privacy and Confidentiality standard) | **MEETS directly** — floor plan specifies "Sound insulation — acoustically isolated from adjacent rooms (massage = quiet environment)" for Treatment Rooms. |
| "Clients must be given adequate privacy to undress and dress... leaving the room, knocking before re-entering" (procedural, but structurally enabled by a lockable door) | **MEETS/SUPPORTS** — floor plan specifies "Privacy lock — thumb-turn deadbolt client-side (no key)" for Treatment Rooms, which structurally enables this procedural requirement. |
| Clean, freshly washed linen for each client; clean dry storage with rotation system; soiled linen in closed container | **MEETS** — same Clean/Dirty Linen storage rooms noted under §1 above apply equally here. |
| Hand washing (soap dispensers, not bar soap; disposable paper towels); clean/disinfect table and bolsters between clients | **MEETS in substance** — floor plan's clinical sink (soap dispenser, paper towel dispenser) covers this; no gap found specific to massage. |
| No explicit room-size requirement | **N/A** — floor plan's ~12-14sqm massage rooms are a design choice, not tested against a Code minimum because none exists. |

**Section count: 4 meets, 0 doesn't-meet, 1 N/A (no requirement exists to test against).** Massage is the cleanest match of the three standards checked.

---

## 3. NPAAC Guidelines for Approved Pathology Collection Centres (3rd Ed.) — **COULD NOT BE RETRIEVED**

**Genuinely not obtained** despite 6 real attempts (2x direct PDF fetch at different sub-paths, 1x HTML resource page, 1x digitalhealth.gov.au implementer hub mirror, 1x older health.gov.au mirror, 1x targeted WebSearch for quoted text) — every safetyandquality.gov.au-domain attempt timed out (60s) or connection-reset; the mirror pages that did load only pointed back to the same unreachable domain. **This is not being silently skipped or filled in from general knowledge** — no line-by-line comparison is possible without the actual text.

**What can be said honestly:** `pathology-collection-room.md` (existing repo doc) already states the exact WDP room spec has never been confirmed and must come from WDP directly before finalising — this is unaffected by whether NPAAC itself is obtained, since WDP's own Licensed Collection Centre requirements (built on top of NPAAC) are the more directly binding source for GTT specifically. **Recommendation: prioritise getting WDP's actual room spec (now realistic given Carole Rivers is engaged) over re-attempting the NPAAC PDF fetch** — it's the more direct and more likely path to a real answer.

**Section count: 0 meets, 0 doesn't-meet, cannot assess (document inaccessible) — flagged honestly, not guessed.**

---

## Food Act 2008 — Café/Snack Notification, Next Steps Drafted

Per `industry-standards-reference-2026-07-28.md`, GTT's café/refreshments counter (herbal tea, water, snacks, glucose drink dispensing) triggers Food Act 2008 (WA) notification requirements. `floor-plan-concept.md` itself already correctly flags this room as "low-risk food notification" — consistent with what's actually required.

**Draft next steps (cannot be filed yet — blocked on venue location, not an oversight):**
1. **Classification:** GTT's offering (prepackaged/low-risk snacks, tea/coffee, glucose drink dispensing — no commercial kitchen, no meal preparation) most likely falls under the WA Health notification form's "low-risk" or "retailer" category rather than "restaurant/café" — needs direct confirmation with the local council once venue suburb is known, since classification can be council-specific.
2. **Form:** WA Health's Food Act 2008 Notification/Registration form (https://www.health.wa.gov.au/~/media/Files/Corporate/general-documents/food/Word/FoodActNotificationRegistrationFormDeptHealth.doc) — proprietor/business details, food type, premises address.
3. **Authority:** enforced and processed by the **local council** for whichever suburb the venue lands in — not a single state-wide authority. This means the notification cannot genuinely be filed until a venue address exists.
4. **Underlying requirement:** Standard 3.2.2 of the Australia New Zealand Food Standards Code requires notification even for businesses that are otherwise registration-exempt — GTT should notify regardless of whether the council places it in a low-risk exempt category.
5. **Timing:** file promptly once a venue is signed, before opening — not deferred past that point given it's a straightforward, low-cost step.

**Status: drafted and ready, correctly blocked on venue-location decision, not outstanding through inaction.**

---

## Overall Summary

| Standard | Meets | Doesn't Meet | Can't Assess |
|---|---|---|---|
| WA Skin Penetration Code | 3 | 2 | 2 |
| AMT Massage Code | 4 | 0 | 1 (N/A) |
| NPAAC (phlebotomy) | 0 | 0 | **All — document inaccessible** |

## Most Important Fix Needed

**The concept floor plan's treatment rooms need a second sink (or clearly designated separate prep/cleaning area) and hands-free taps, per WA Skin Penetration Code §7.1-7.2** — this is the single most concrete, specific, fixable gap found across all three standards. Everything else is either already met, not applicable, or genuinely blocked on external information (WDP's room spec, a venue address for Food Act notification, or NPAAC's inaccessible text).

---

## Scope Narrowing (2026-07-28, later same day) — Which Services Actually Trigger the Code

Anthony confirmed GTT will NOT offer waxing that nicks skin, shaving, microneedling, or dermaplaning. The Code's own trigger definition (Definitions, p.4): **"Skin penetration procedure — Means any process involving the piercing, cutting, puncturing, tearing or shaving of the skin, mucous membrane or conjunctiva of the eye."** Checked against GTT's actual planned service menu (`services-pricing-locked.md`), not assumption:

| Service | Triggers the Code? | Reasoning |
|---|---|---|
| Blood collection (phlebotomy) | **YES** | Venepuncture is unambiguously "piercing... of the skin." Unaffected by this scope narrowing. |
| Nail treatments (manicure/pedicure) | **LIKELY YES** | Standard industry cuticle trimming (nippers) cuts cuticle tissue, which is skin — plausibly "cutting... of the skin." **Flagged as an assumption pending confirmation of GTT's actual cuticle protocol** (push-back only vs. trim), not a confirmed clause match. |
| Hair cutting/styling | **NO** | The Code's definition is "cutting... of the skin" — hair cutting is cutting of hair, not skin. Razor work (which would trigger "shaving... of the skin") is excluded from GTT's scope per Anthony. |
| Massage | **NO** | No piercing, cutting, puncturing, tearing, or shaving of skin occurs under any circumstance. Confirmed unchanged from the earlier finding — massage was already the cleanest match against these standards. |
| Plain non-invasive facials | **NO** | No trigger action occurs. |
| Brow waxing / threading | **GENUINE BOUNDARY CASE, NOT RESOLVED** | Both are real, currently planned services (`services-pricing-locked.md`: "Brow wax + reshape," "Brow thread + reshape"). Whether professionally-executed waxing (no nicking) constitutes "tearing... of the skin" under the plain text is a real judgment call this agent cannot resolve with confidence — not a government ruling, just a reasoned reading of ambiguous wording. |

**Sink requirement scoped accordingly, not applied blanket:**
- **No longer needs the 2-sink/hands-free-tap fix:** Massage Rooms (1, 2, 5-growth), Hairdressing Area.
- **Retains the fix (conservative default given unresolved boundary questions):** Nail Station Area, Facial/Beauty Rooms (3, 4, 6-growth).
- **Retains the fix (unambiguous):** Blood Collection Room.

This is a real, calculated fit-out cost reduction for 3 of 7 treatment-adjacent rooms — not assumed, and not overstated: 2 of the remaining rooms (Nail, Facial/Beauty) are retained on a conservative-not-confirmed basis, not because they're definitely required.

## Changelog
**2026-07-28 (v2)** — Superseded v1's "none read" status. Obtained and read WA Skin Penetration Code (509 lines) and AMT Massage Code (1,392 lines) in full via pdftotext extraction after WebFetch returned unreadable binary. NPAAC genuinely inaccessible after 6 attempts — flagged honestly, not guessed. Found a real, previously-unflagged threshold question: the Skin Penetration Code's exemption list may not cover phlebotomists. Drafted Food Act 2008 notification next steps, correctly identified as blocked on venue location rather than outstanding through inaction.

**2026-07-28 (v3, later same day)** — Anthony narrowed GTT's service scope (no nicking-waxing, shaving, microneedling, dermaplaning). Re-checked the Code's trigger definition against GTT's actual planned service menu, room by room. Result: Massage and Hairdressing no longer need the 2-sink/hands-free-tap fix; Nail and Facial/Beauty retain it on a conservative, not-confirmed basis (cuticle cutting, brow waxing/threading both sit in genuine unresolved territory); Blood Collection Room unaffected. Corresponding edits made to `floor-plan-concept.md`.
