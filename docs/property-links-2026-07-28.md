# GTT Center Perth — Property Lead URLs, Verified 2026-07-28

**Re-verified this session per Anthony's instruction for literal clickable URLs, not "a link exists" as a concept. Correction found vs the 2026-07-27 report below — flagged explicitly, not glossed over.**

---

## 1. 2A/236 Main Street, Osborne Park — CORRECTION: NO LONGER AVAILABLE

**URL:** https://www.commercialrealestate.com.au/property/2a-236-main-street-osborne-park-wa-6017-16172595

**Status: LEASED, not available.** The listing's own page title, confirmed via live search 2026-07-28, is **"Office Leased in 2A/236 Main Street, Osborne Park WA 6017"** — this property has already been leased to someone else since it was first flagged. **This corrects the 2026-07-27 report, which presented this as an active lead** — it was checked less rigorously that session (confirmed the listing existed and had real agent/price details, but did not check current leased/available status). Do not pursue this one; remove from the active shortlist.

A second listing ID exists for the same address (18093774) — not checked this session, may be a re-listing; needs direct confirmation before treating as a replacement, not assumed.

---

## 2. 6/325 Harborne Street, Osborne Park — CONFIRMED LIVE

**URL:** https://reiwa.com.au/6-325-harborne-street-osborne-park-4941752/

**Status: Active/Live**, confirmed via direct fetch of the REIWA listing page 2026-07-28 (not just search results this time).

- **Size:** 268sqm
- **Price:** A$55,000/yr net + GST (Price on Application shown on some listing variants — the A$55,000 net figure is the specific rent quoted on the page)
- **Agents:** Shannon Swarts (0448 218 629) and Jonathan Kilborn (0404 796 137), AGORA Property Group *(phone numbers newly confirmed this session — 2026-07-27's report had Shannon Swarts named but no phone number)*
- **Description:** "Osborne Park Showroom with Excellent Exposure" — large glass frontage, open-plan, prominent signage, available immediately

**This is the one confirmed-live, confirmed-real lead with a clickable URL as of 2026-07-28.**

---

## 3. 20 Parkland Road, Osborne Park — STATUS UNCLEAR, FLAGGED

**URL:** https://www.commercialrealestate.com.au/property/20-parkland-road-osborne-park-wa-6017-16969571

**Could not directly confirm current availability this session** — direct fetch of the listing page returned HTTP 403 (blocked), same as the Main Street listing above. Search results show this address is part of a larger A-grade office building (7 floors, NABERS 5-star, per Centuria/sidespace.com.au listings for the same building) with multiple different floor spaces advertised at different times (e.g. a 770sqm Level 7 space at $350/sqm found in a different listing for the same building) — **the specific 994sqm/28-parking listing flagged last session may or may not still be the current live listing for this address; not confirmed either way.** Given this address was already flagged last session as likely oversized for GTT Center Perth's ~150-250sqm target, and its live status is now also unconfirmed, **recommend dropping this lead rather than pursuing it further.**

---

## 4. Maylands / South Perth Hardy St — STILL UNCONFIRMED, NO REPLACEMENT FOUND YET

**No real listing URL exists for either** — re-confirmed again this session. Broad category-page searches (commercialrealestate.com.au/REIWA filtered by suburb/size) return only aggregate "N properties available" pages, not a specific matching address, and attempting to pick one specific listing from those aggregate results without directly confirming it would risk presenting an unverified/possibly-stale listing as real, which is exactly the error already found with 2A/236 Main Street above.

**Flagged honestly rather than guessed:** a genuine replacement search needs either (a) direct browsing of the live filtered category pages (commercialrealestate.com.au/for-lease/maylands-wa-6051/retail/ and /for-lease/south-perth-wa-6151/retail/) by a human, since search-engine results here are proving unreliable for confirming current listing status, or (b) Quinn running this with a tool that can actually browse and filter the live site rather than relying on search snippets. **This agent's WebFetch was blocked (403) on multiple direct commercialrealestate.com.au listing pages this session** — flagging this as a tooling limitation affecting confidence in property verification generally, not specific to these two suburbs.

---

## Summary — What Anthony Can Actually Click On Right Now

| Lead | Clickable URL | Status |
|---|---|---|
| 2A/236 Main Street, Osborne Park | https://www.commercialrealestate.com.au/property/2a-236-main-street-osborne-park-wa-6017-16172595 | **LEASED — do not pursue** (correction from 2026-07-27) |
| 6/325 Harborne Street, Osborne Park | https://reiwa.com.au/6-325-harborne-street-osborne-park-4941752/ | **LIVE — only confirmed-active lead** |
| 20 Parkland Road, Osborne Park | https://www.commercialrealestate.com.au/property/20-parkland-road-osborne-park-wa-6017-16969571 | **Unconfirmed status, likely oversized — recommend dropping** |
| Maylands (160sqm, 10 parking) | **No URL exists** | Unconfirmed, no replacement found this session |
| South Perth Hardy St (216sqm, A$4,750/mo) | **No URL exists** | Unconfirmed, no replacement found this session |

**Net effect: only 1 of the original 3 Osborne Park leads is both real and currently available.** This is a materially different picture from last session's report (which presented all 3 as live) — worth surfacing to Anthony directly rather than letting the correction sit quietly in a changelog.

## Changelog

**2026-07-28** — Re-verified all property leads per Anthony's explicit instruction for literal URLs and against the stated concern that last round had false regressions. Found 2A/236 Main Street is actually leased (not available) — correcting the 2026-07-27 report, which did not check current availability status, only listing existence. 6/325 Harborne Street confirmed genuinely live via direct page fetch. 20 Parkland Road's current status could not be confirmed (fetch blocked) and is flagged for dropping given both size and status uncertainty. Maylands/Hardy St replacement search still unsuccessful — flagged as a tooling limitation (WebFetch blocked on the primary listing sites) rather than guessed at.
