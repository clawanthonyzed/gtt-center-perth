# Commercial Lease Red-Flag Checklist

**Date:** 2026-08-27. **Purpose:** a genuine, previously missing document, checked for before creating (see `docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md` §2's Venue Data Capture Template, which records lease facts, and `docs/architecture/VENUE-FIRST-VISIT-CHECKLIST.md`, which is an on-site physical inspection checklist). Neither existing document teaches what a *bad* answer looks like in a commercial lease offer; this one does. It does not replace a solicitor, and does not duplicate the data-capture template's fields, it flags the clauses worth raising with a solicitor before signing anything, so a first read of any Heads of Agreement or lease draft can happen without waiting for paid solicitor time.

**When to use:** the moment a landlord or agent provides a Heads of Agreement or draft lease, before it goes to the commercial lease solicitor (`docs/external-resources-and-advisors.md` §3) for formal review. Not a substitute for that review, a triage step before it.

---

## 1. Term, Renewal, and Exit

- **Demolition or redevelopment clause** allowing the landlord to terminate early for redevelopment, with little or no compensation: a real risk for a fit-out-heavy tenancy (blood collection room, treatment rooms) where GTT Center Perth would lose its fit-out investment.
- **Assignment/subletting restrictions** that are absolute (landlord can refuse for any reason) rather than "reasonable consent not to be unreasonably withheld": limits the ability to sell or restructure the business later.
- **Option-to-renew terms** that reset rent to full market rate with no cap, rather than a defined formula (CPI, fixed percentage, or a capped market review): removes the predictability the financial model currently assumes.
- **No genuine option period at all** (lease length offered is shorter than the 3+3 year target in `docs/location-scouting.md` with no renewal right): forces an early re-negotiation from a position of no leverage once fit-out is sunk.

## 2. Rent, Outgoings, and Reviews

- **Ratchet rent review clause** (rent can only go up at review, never down, even if market rent falls): a genuine one-way risk, worth raising even though common in WA commercial leases.
- **Uncapped or "as determined by the landlord" outgoings**, rather than a stated estimate with a cap or a right to audit: this venture's financial model (`docs/CURRENT-STATE.md`) assumes a bounded occupancy cost; an open-ended outgoings clause breaks that assumption.
- **Rent review mechanism left blank or "market review" with no independent-valuation mechanism specified**: means the landlord effectively sets the number at review with no objective check.
- **No rent-free or incentive period offered at all** on a tenancy requiring the kind of fit-out this venue needs (blood collection room, plumbed wet areas, multiple treatment rooms): worth treating as a negotiation point, not just accepting the first offer.

## 3. Permitted Use and Exclusivity

- **Permitted-use clause narrower than "health, beauty, and wellness services"**: could technically prevent operating the blood collection component, the hairdressing component, or the cafe/retail component if drafted too narrowly. Needs to explicitly cover the mixed clinical/beauty/hospitality model this venture actually runs, not a generic "beauty salon" use clause.
- **No exclusivity of use** in a multi-tenancy building (e.g. a shopping centre) where a competing beauty/wellness tenant could be let into an adjacent tenancy: worth asking for, not assuming.
- **Landlord silent on medical waste and clinical-collection activity** in the permitted-use description: given the Blood Collection Room is a genuinely unusual use for a commercial tenancy, an explicit, written landlord acknowledgment of this specific activity (not just "health services" generally) closes a real ambiguity before it becomes a dispute.

## 4. Guarantees and Financial Exposure

- **Open-ended personal guarantee** (uncapped, for the full lease term) rather than a capped guarantee (e.g. limited to 6-12 months' rent, or reducing over the lease term): the Venue Data Capture Template already asks whether a personal guarantee is required and at what cap, this section is the reason that field matters, an open-ended guarantee against YETI Tipi Holdings PTY LTD as trustee (or any personal guarantee from Anthony directly) is a genuine asset-protection question, worth raising with both the lease solicitor and, if the entity-structure decision (`docs/business-plan.md` §11, currently open per `docs/DECISION-LOG.md`) is still unresolved at the time, the accountant as well.
- **Bank guarantee sized well above the stated bond** (some landlords ask for a bank guarantee in addition to, or instead of, a cash bond, at a materially higher figure): confirm which is being asked for and reconcile against the bond figure already captured in the Venue Data Capture Template.
- **GST treatment left ambiguous** ("plus GST" vs "GST inclusive" not stated): a small but real cost-model input already flagged as a field to confirm in the Venue Data Capture Template, this section is why it matters (a 10% swing on a six-figure annual rent line).

## 5. Fit-Out and Make-Good

- **Make-good clause requiring full reinstatement to base building condition** at the tenant's cost at lease end, with no negotiated exclusion for landlord-retained improvements (e.g. plumbing, HVAC upgrades installed for the Blood Collection Room that the landlord may actually want to keep): a genuinely costly clause if not negotiated, worth raising explicitly given how much of this venture's fit-out is plumbing/wet-area/compliance-driven, not cosmetic.
- **No landlord consent process defined for fit-out works** (silent on approval timelines, plans required, contractor licensing requirements): can materially delay the fit-out timeline this venture's roadmap depends on.
- **Landlord retains approval rights over signage with no defined turnaround time**: can delay opening if not addressed up front.

## 6. Compliance and Risk Allocation

- **No landlord warranty on the premises' compliance with the Skin Penetration Code, disability access, or fire safety** at handover: the Venue Data Capture Template already asks whether these are confirmed, this section flags that an *unconfirmed* answer at lease-signing stage, with the compliance risk left entirely on the tenant, is a red flag worth pushing back on, not just noting.
- **Insurance clauses requiring cover types or limits inconsistent with what's actually available** for this hybrid clinical/beauty venue (see the insurance broker draft at `docs/insurance-broker-quote-request-draft.md`, still pending broker selection): confirm the lease's required limits are realistic before signing, not after the broker quote arrives.

---

## What This Document Deliberately Does Not Do

It does not replace solicitor review, every item above is a "raise this with the solicitor" flag, not a legal opinion. It does not repeat the Venue Data Capture Template's fields, it explains why several of those fields matter. It does not assume any of these red flags will actually appear in any specific lease offer, it is a pattern-matching tool for whichever offer eventually arrives. It does not commit to engaging a solicitor now, solicitor engagement remains correctly gated on a shortlisted venue per `docs/architecture/WDP-PARTNERSHIP-ACTIVATION-PLAN.md`.

## Sourcing

`docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md` §2/§3, `docs/architecture/VENUE-ACQUISITION-READINESS-PACKAGE.md`, `docs/location-scouting.md`, `docs/external-resources-and-advisors.md` §3, `docs/CURRENT-STATE.md`, general Australian commercial-leasing risk categories (standard practice, not sourced to a specific WA statute in this document, a solicitor confirms the current legal position on any specific clause).

## Changelog

**2026-08-27 (created):** Built after confirming this specific gap did not already exist anywhere in the repository (checked `VENUE-ACQUISITION-DUE-DILIGENCE.md`, `VENUE-ACQUISITION-READINESS-PACKAGE.md`, `VENUE-FIRST-VISIT-CHECKLIST.md`, and a direct grep for make-good/ratchet/demolition-clause/exclusivity/bank-guarantee language across the full repository, zero matches). A genuinely new, bounded document, not a duplicate of the existing data-capture or on-site checklists.
