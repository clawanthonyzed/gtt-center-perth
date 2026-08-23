# Procurement Execution Status

Status: current as of 2026-08-23. One-page operational control document. Full detail lives in the documents linked below; this page answers 7 questions at a glance and nothing else.

## 1. What can we do today?

Order 14 items directly, no blocker at all (Queue 1, Tier 1a): laptop, iPads, iPad stand, printer, WiFi router, thermal label printer, first aid kits, specimen transport bags, ice packs, blood spill kits, sharps containers (bench and room size), sharps bracket, curated reading material. 24 further items (Queue 1, Tier 1c) are structurally ready but genuinely better held until a venue exists, since they are bulky and have nowhere to be delivered or stored yet (nail/hair/pedicure station furniture, phlebotomy chairs, cafe equipment). 1 item (Fresha subscription) can be set up now but should not start paid billing yet.

**Full detail:** `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 1.

## 2. What can we quote today?

3 comparable RFQ groups, ready to send now: bulk salon/spa furniture and equipment (hair dryers, straighteners, nail lamps, manicure chairs, to 5 named Australian suppliers), Beauty treatment beds, and clinical furniture (phlebotomy chairs, exam couch). Plus the China sourcing-agent enquiry package, ready to send for an exploratory, no-commitment scoping conversation. Builder and specialist-trade quotes cannot genuinely be scoped yet, no venue exists.

**Full detail:** `docs/architecture/AUSTRALIA-RFQ-RELEASE-PACKAGE.md`, `docs/architecture/CHINA-SOURCING-AGENT-ENQUIRY-PACKAGE.md`.

## 3. What is waiting for the venue?

24 items (Readiness C), plus every builder and specialist-trade quote. Nothing here can be genuinely actioned before a lease is signed and the site is measured.

**Full detail:** `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`, `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 3.

## 4. What do I need to decide?

**Urgent, blocks a ready RFQ:** Massage table vs chair format. Every other founder decision (laundry model, hand dryer vs paper towel, facial steamer, colour hair services, hair clippers, retail brand) affects only its own single item and can wait.

**Already settled, not reopened:** Beauty station count (3, recommended), Blood Collection Room count (1 room, 3-chair-ready), China/Australia procurement model (Hybrid).

**Full detail:** `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 4.

## 5. Who do we need to contact?

**Can contact now:** 5 named Australian salon/spa suppliers (no quote yet), a China sourcing agent (exploratory only), an HVAC/LEV contractor and Cafe food/coffee suppliers (identification, not yet started). **Must wait for a reply, do not send again:** WDP (Carole Rivers), a follow-up was sent 2026-08-21 covering the medical waste question; the centrifuge and glucose-solution questions have not been asked yet and should wait for a reply, per standing instruction not to draft another follow-up without genuine reason. **Must wait for a venue:** builder, licensed electrician/plumber, freight forwarder (should follow a locked China order, not precede it).

**Full detail:** `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 5.

## 6. What happens immediately after we secure the venue?

Site measurement, then service/utility verification, electrical assessment, plumbing/hydraulic assessment, HVAC/LEV assessment, accessibility assessment, WDP sign-off on the Blood Collection Room, council Food Business Notification, furniture/layout confirmation, then 3 builder quotes, then final equipment quantities locked, then the Site-Dependent Hold List items release into the RFQ-Now queue.

**Full detail:** `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md` Queue 3, `docs/architecture/PROCUREMENT-OPENING-SEQUENCE.md` Stage 1-3.

## 7. What is the critical path to opening?

Massage format decision, then venue secured, then site measured/verified, then builder quotes and fit-out ordered, then fit-out construction, then equipment delivery and installation, then opening stock, then staff setup/training, then final compliance sign-off, then opening. No stage is skipped or run out of order; equipment is not installed before the relevant trade has finished its own work in that room.

**Full detail:** `docs/architecture/PROCUREMENT-OPENING-SEQUENCE.md` (10 stages, Stage 0 through Stage 9).

## Snapshot Counts

281 distinct items: 39 order-ready, 149 RFQ-ready, 24 site-dependent, 28 professional-verification-required, 3 WDP-dependent, 15 founder-decision-required, 9 information-required, 14 future/optional. No purchase, RFQ, or supplier/agent contact has been made against any of them.

## Sourcing

`docs/architecture/PROCUREMENT-EXECUTION-MATRIX.md`, `docs/architecture/PROCUREMENT-EXECUTION-QUEUES.md`, `docs/architecture/PROCUREMENT-OPENING-SEQUENCE.md`, `docs/architecture/AUSTRALIA-RFQ-RELEASE-PACKAGE.md`, `docs/architecture/CHINA-SOURCING-AGENT-ENQUIRY-PACKAGE.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the single, concise operational control document, answering 7 at-a-glance questions with a link out to full detail for each, rather than restating the underlying analysis. Added to the Dash, not the Master Dossier, per instruction not to bloat the business plan with procurement execution detail.
