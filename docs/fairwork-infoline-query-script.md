# Fair Work Infoline Query Script — Saturday Ordinary-Hours Question (MA000027)

**Compiled:** 2026-08-15 | **Status: PARTIALLY RESOLVED 2026-08-23.** The general question (does MA000027 have a clause treating Saturday hours as ordinary for pathology practices) is answered: yes, clause 13.2(b)(ii), confirmed via a direct Fair Work Ombudsman award-library fetch, see `docs/hr-framework.md` §"Saturday Ordinary-Hours Question: RESOLVED 2026-08-23, Primary-Sourced". The call below is still worth making, but for the narrower remaining question in the updated script, not the original one.
**Purpose (updated 2026-08-23):** the original gap this script was written to close, whether MA000027 has a Saturday-ordinary-hours clause for pathology practices at all, is now closed via a direct fetch of `awards.fairwork.gov.au/MA000027.html`. What remains genuinely open: whether GTT Center Perth's specific setup (a co-located wellness venue with a WDP-operated collection room, not a stand-alone pathology practice) qualifies under this clause, and whether the venture's actual Saturday phlebotomist shift time falls entirely within the clause's 8:00am-4:30pm window. The call script below has been updated to ask this narrower, better-informed question.

**Why this matters financially:** every current financial model (`docs/CURRENT-STATE.md`, `data/models/master_financial_model.yml`) uses the conservative full-Saturday-penalty-rate assumption for phlebotomist wages. If the carve-out is real, Saturday phlebotomist labour cost is lower than currently modelled — **this is upside-only risk**, no model currently overstates profitability by assuming a carve-out that may not exist.

---

## Call Script

**Number:** 13 13 94 (Fair Work Infoline)
**Best time to call:** business hours, expect a queue — this is a general enquiry line, not urgent/priority.

> Hi, I'm calling about a specific classification question under the Health Professionals and Support Services Award, MA000027.
>
> I've already confirmed that clause 13.2(b)(ii) of MA000027 treats Saturday 8:00am to 4:30pm as ordinary hours, not penalty hours, for private medical, dental, pathology, physiotherapy, chiropractic and osteopathic practices.
>
> I'm setting up a wellness venue that hosts a licensed pathology partner's blood-collection service on-site, not a stand-alone pathology practice. Our phlebotomists would work within that on-site collection service.
>
> Could you help me confirm:
>
> 1. Does a wellness venue hosting a third-party pathology partner's collection service on-site (rather than operating as a stand-alone pathology practice itself) qualify for the clause 13.2(b)(ii) treatment for its phlebotomist staff?
> 2. If our Saturday phlebotomist shift starts before 8:00am, does only the portion of the shift within 8:00am-4:30pm count as ordinary hours, with the earlier portion remaining at the general penalty rate?
> 3. Is there anything else about our specific structure (the phlebotomists may ultimately be employed by us or by the pathology partner, this is not yet decided) that would change which entity's award coverage applies?
>
> I'd like to get this right before finalising employment contracts, so an exact clause reference or written confirmation I can check myself afterwards would be ideal.

---

## What To Do With the Answer

1. Record the answer (clause reference if one exists, or explicit confirmation that no such carve-out exists) directly in `docs/hr-framework.md`, replacing the "still unconfirmed" note in the Saturday Ordinary-Hours Question section — do not silently delete the existing investigation trail, add the resolution above it per this repo's own never-rewrite-history convention.
2. If a genuine carve-out is confirmed: flag it to `docs/VERIFICATION-TRACKER.md` and to whoever next updates the financial model — this would reduce modelled Saturday phlebotomist labour cost, a genuine (small) positive revision to `docs/CURRENT-STATE.md`'s net P&L figures. Do not update the financial model without this document trail existing first.
3. If no carve-out exists: mark the question definitively closed in `hr-framework.md` rather than leaving it open indefinitely — the conservative assumption already in every current model remains correct and needs no change.

---

## Sending Status

**Not called yet.** This is a phone script, not an email — "sending" means Anthony (or a delegated administrative call) actually places the call. No blocker exists beyond making the call; unlike the accountant/insurance drafts, no recipient-selection decision is outstanding.

---

## Changelog

**2026-08-15** — Created as the concrete next step for the Saturday ordinary-hours investigation already logged in `docs/hr-framework.md`, per that document's own "Recommended next step" note. Priority 3, external professional outreach round.
