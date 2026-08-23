# Insurance Broker Quote Request Email — Draft

**Compiled:** 2026-08-15 | **Status:** READY TO SEND, once a specific broker is chosen — content is complete, recipient is not.
**Purpose:** Initiate the Week 10 insurance process already specified in full in `financial-setup.md` Step 8 and cross-referenced in `docs/external-resources-and-advisors.md` §4 (broker needs health-adjacent-premises experience — a standard beauty-salon policy likely won't cover the clinical collection-room exposure, and a standard medical-clinic policy won't cover the wellness services). This is an early, no-cost quote-request enquiry, not a binding application — appropriate to send well before Week 10, since indicative quotes help firm up the startup-cost planning figures in `data/canonical/startup_costs.yml`.

**What is genuinely still open before this can be sent:** a specific broker has not yet been selected. `financial-setup.md` Step 8 names BizCover, Aon, and Gallagher as provider options and recommends getting 3 quotes — no single named recipient chosen. This draft is written generically enough to send to any of the three, or to be submitted through BizCover's online instant-quote form directly (in which case this text can be adapted to its form fields rather than sent as an email).

---

## Draft

**Subject:** Quote request — hybrid clinical/wellness venue, pre-launch, Perth

> Hi [Broker/Firm name],
>
> I'm setting up a new venue in Perth combining a licensed pathology blood-collection service with wellness services (massage, nail, hair, and brow treatments) under one roof. I'd like an indicative quote across the policy types below, ahead of finalising a lease.
>
> A brief outline of the venue and what I'd need covered:
>
> - **Nature of the business:** a wellness venue hosting a licensed third-party pathology blood-collection service on-site (we do not hold pathology accreditation ourselves — a licensed pathology partner operates the collection room), alongside wellness services (massage, nail care, hairdressing, brow treatments) for the same clients and the general public
> - **Public liability** — minimum A$20M, given the clinical collection-room exposure alongside general premises use
> - **Professional indemnity** — minimum A$5M, for the wellness-service side of the business
> - **Workers' compensation** — for approximately 10-12 employees at launch (wellness therapists, phlebotomists, reception)
> - **Commercial property/contents** — covering fit-out and equipment (specific figures to follow once a venue is confirmed)
> - **Business interruption** — optional, would like a quote for reference
> - **Cyber/data liability**: we hold client health/booking data (an online booking system and clinical intake records), would like an indicative quote for this exposure as well
>
> The venue is not yet leased or open — I'm gathering indicative quotes now to finalise the startup budget, and would follow up for a firm quote once a lease is signed.
>
> Could you let me know whether your firm has experience with health-adjacent premises (day spas, allied health, or similar), and provide an indicative annual cost range for the coverage above?
>
> Regards,
> Anthony Zed

---

## Design Notes (not for inclusion in the sent email)

- Coverage minimums and policy list match `financial-setup.md` Step 8's table exactly (public liability A$20M, professional indemnity A$5M, workers' comp, commercial property, business interruption) — no new coverage type added.
- Employee count ("approximately 10-12") reflects the confirmed core headcount (8 dual-qualified treatment staff + 2 phlebotomists) plus reception/venue-manager roles referenced elsewhere in this repo — stated as approximate since exact final headcount at launch is not yet locked.
- Explicitly discloses the clinical/wellness hybrid nature up front, since `external-resources-and-advisors.md` §4 flags this as the actual reason a generic broker may misquote or under-cover the venue — hiding it to get a cheaper indicative number would produce a useless quote.
- No venue name, no opening date, consistent with this repo's own standing outreach convention.
- The current financial model uses a **placeholder** A$400/month insurance cost (per `docs/CURRENT-STATE.md`) against an itemised estimate of A$975-1,583/month (`financial-setup.md` Step 8: A$11,700-19,000/year annualised) — this quote request is the concrete step that would close that gap with a real figure.

---

## Sending Status

**Not sent.** No broker has been selected yet. BizCover's online instant-quote tool (referenced in `financial-setup.md` Step 8 as "the fastest for public liability and PI for small health businesses") is a plausible first channel — its form fields would need this content adapted to its own structure rather than sent as a freeform email.

---

## Changelog

**2026-08-15** — Created as the first-contact insurance quote-request draft, built entirely from the existing `financial-setup.md` Step 8 checklist and `external-resources-and-advisors.md` §4 broker-selection reasoning. Priority 3, external professional outreach round.

**2026-08-23**: Added a cyber/data-liability line, per `docs/architecture/OPENING-READINESS-EXECUTION-PLAN.md` Section 2's finding that this exposure (client health/booking data, an online booking system, clinical intake records) was not covered anywhere in the existing draft. No other line changed; the draft remains READY TO SEND once a specific broker is chosen, still not sent.
