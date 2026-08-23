# Venture Opening Readiness Audit

Status: current as of 2026-08-23. A decision-oriented audit, not a new business-plan chapter. Built from the current source-of-truth hierarchy (`docs/architecture/SOURCE-OF-TRUTH-TIERS.md`) and current-state documents only; no superseded figure, old property information, old pricing, old staffing assumption, spray tan, or GDM snack pack is treated as current anywhere below. Property search, WDP correspondence, settled pricing, the venue program, the China/Australia procurement model, the procurement register structure, and the Master Dossier structure are not touched here, per direct instruction, since no genuine contradiction was found in any of them during this audit.

## Executive Summary: If Anthony Secured the Venue Tomorrow, What Would Stop Us Opening?

**Nothing structural would stop the venture from eventually opening, but 6 things would genuinely block the first client-facing day if not actioned in parallel with fit-out:**

1. **Massage table-vs-chair format is still undecided**, and it is the only remaining founder decision that blocks an equipment order already sitting ready to send.
2. **No insurance has actually been quoted or bound.** The current financial model runs on a A$400/month placeholder against a real itemised estimate of A$975-1,583/month; a broker has not even been contacted (`docs/insurance-broker-quote-request-draft.md`, status: Not Sent). A venue cannot legally trade without public liability and professional indemnity in place.
3. **No employment contract template exists.** Job postings exist for all 4 roles (phlebotomist, PM casual, receptionist, Venue Manager), but there is no actual employment agreement to sign anyone with.
4. **No business-continuity/emergency-closure plan exists**, distinct from the physical Emergency Response Plan (fire, medical incident). Nothing currently answers "what do we do if the Venue Manager is sick on a rostered day" or "how do we communicate an unplanned closure."
5. **The HVAC/LEV contractor, external Cafe food supplier, and coffee/beverage supplier remain unidentified**, all genuine, disclosed external dependencies that cannot be resolved by more internal research.
6. **WDP has not yet confirmed the 3 clinical dependencies** (centrifuge sourcing, medical waste contract overlap, glucose solution supply); a reply to Anthony's 2026-08-21 follow-up is still outstanding.

**Everything else audited below (venue program, procurement system, staffing model, client/staff journey, clinical protocol) is genuinely ready or correctly classified as venue-dependent, not a hidden gap.**

## 1. Opening-Readiness Matrix

| Area | Classification | Basis |
|---|---|---|
| Corporate/business setup (YETI Holding Trust, ABN, GST registration) | READY | Established, per `docs/financial-setup.md` |
| Venue | VENUE-DEPENDENT | Anthony handling property search directly, not touched here |
| Planning/building requirements | VENUE-DEPENDENT | Cannot finalise before a site is measured, per `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md` |
| Accessibility (AS 1428.1) | PROFESSIONAL-VERIFICATION | Access consultant/building surveyor sign-off required once venue confirmed |
| Clinical/pathology operations | READY (protocol exists) / WDP-DEPENDENT (final sign-off) | `docs/gtt-clinical-protocol.md` v1.0 exists; WDP's own Licensed Collection Centre sign-off on the specific room is outstanding |
| WDP relationship | EXTERNAL-DEPENDENT | Active, responsive correspondence; 3 procurement items and the collection-room sign-off await a reply |
| Blood collection | READY (workflow) / VENUE-DEPENDENT (room) | Workflow and equipment specified; room construction and WDP room sign-off pending venue |
| Medical waste | EXTERNAL-DEPENDENT | Whether WDP's own arrangement covers it is genuinely unconfirmed (E14) |
| Infection control | READY | TGA-listed disinfectant, hand hygiene, PPE all specified in the procurement register |
| Emergency response | READY | `docs/emergency-plan.md` v1.0, WorkSafe WA compliance document, exists |
| First aid/CPR | FOUNDER-DECISION (minor) / READY (policy) | All staff trained with blood-collection-specific emphasis; exact accredited course (HLTAID011 or equivalent) needs confirmation from a registered training organisation, not yet done |
| WHS | NOT YET BUILT | No standalone WHS policy document exists; WHS obligations are referenced piecemeal (LEV/WorkSafe, emergency plan) but not consolidated |
| Skin penetration (WA Skin Penetration Code) | READY (researched) / PROFESSIONAL-VERIFICATION (site-specific) | Code requirements researched and built into Beauty/Nail procurement (2-sink fitout, G08); final site-specific compliance confirmed once venue exists |
| Massage | FOUNDER-DECISION | Table vs chair format, the single unresolved procurement-blocking decision, see Section 7 |
| Beauty | READY | 3 stations recommended and carried forward, service scope, equipment, hygiene all specified |
| Nails/pedicure | READY | 4 stations, equipment, hygiene, LEV requirement all specified |
| Hair | READY | 4 stations, equipment, colour/clippers correctly gated as founder decisions since not in the current confirmed service list |
| Cafe/food | EXTERNAL-DEPENDENT | Model confirmed; external food supplier and coffee/beverage supplier genuinely not yet identified |
| Privacy | READY | `docs/privacy-policy.md` exists |
| Consent | READY | `docs/consent-form.md` exists |
| Client records | READY | `docs/patient-intake-form.md` exists; 7-year retention requirement built into procurement (E40) |
| Booking/payment systems | READY | Fresha selected and modelled, POS terminal specified |
| IT | READY | Router, network, backup all specified in the procurement register |
| Security | READY (as future/optional) | Cameras/access control correctly classified Future/Optional, not required at opening |
| Insurance | EXTERNAL-DEPENDENT | Not sent, no broker selected, real quote outstanding (see Executive Summary item 2) |
| Staffing (model) | READY | Solver-verified 18-client/day model, 8 treatment staff + 2 phlebotomists |
| Recruitment | READY (postings) / NOT YET BUILT (contracts) | All 4 job postings exist; no employment contract template exists |
| Training | READY | `docs/onboarding.md` v2.0, Day 1 through Week 1 schedule, Fern (existing named staff resource) plus Venue Manager as owners |
| Payroll | READY | Modelled in the financial system |
| Rostering | READY | Fresha-based, roster built by Venue Manager |
| Relief coverage | READY | Relief pool modelled for phlebotomists and treatment staff |
| Supplier setup | EXTERNAL-DEPENDENT | 5 Australian salon/spa suppliers named, none contacted; China sourcing agent enquiry ready, not sent |
| Procurement | READY | Full execution system built this session (matrix, queues, packages) |
| Stock | READY | Opening-stock schedule with disclosed reorder methodology |
| Laundry | FOUNDER-DECISION | In-house vs outsourced, genuinely unconfirmed |
| Cleaning | READY | Cleaning consumables and schedule basis itemised in procurement |
| Waste | READY (general) / EXTERNAL-DEPENDENT (medical) | General waste council/contractor engagement standard; medical waste awaits WDP |
| Opening/closing procedures | NOT YET BUILT | No daily opening/closing checklist SOP exists yet |
| Customer policies (cancellation, no-show) | READY (partial) | Booking policy and T&Cs exist in `docs/onboarding.md` B0; a dedicated refund/complaints policy is thinner, see SOP register |
| Complaints | NOT YET BUILT | No standalone complaints-handling SOP exists |
| Marketing | READY | `docs/afternoon-marketing-plan.md`, `docs/poppy-marketing.md` exist |
| Launch/soft opening | NOT YET BUILT | No soft-opening plan exists yet; a genuine, necessary pre-opening step |

## 2. Client Journey (Authoritative Flow)

Booking (Fresha, online) -> pre-arrival (confirmation email, 48hr/24hr/1hr SMS reminders, per `docs/onboarding.md` B2-B5) -> arrival T-10/15 (check-in at Reception) -> GTT (glucose drink administered by phlebotomist) -> blood draws (Draw 1, wait, Draw 2 at T=60, wait, Draw 3 at T=120, per `docs/gtt-clinical-protocol.md`) -> treatment/cafe/lounge (client moves between Massage/Beauty/Nail/Hair/Cafe/Lounge during the wait window, coordinated by the AM/GTT scheduling model) -> final draw -> specimen handling (label, cold-chain storage, courier dispatch to WDP) -> departure -> post-visit (results pathway is WDP's own, not GTT Center's).

**Every handoff has an owner already established in existing documents:** Reception owns check-in; phlebotomists own the draw sequence and specimen handling; treatment staff own their own service delivery; the Venue Manager owns the overall AM schedule. **Genuine gap:** there is no single consolidated "Day-in-the-life" SOP walking a new staff member through this exact sequence end to end; the information exists across `docs/gtt-clinical-protocol.md`, `docs/onboarding.md`, and the scheduling documents, not in one operational document. This is listed in the SOP register (Section 4) as required before staff training, not before opening.

**Staff journey:** Opening (Venue Manager/Reception arrive first, per `docs/onboarding.md` A2) -> staggered starts (per the solver-verified staffing model) -> AM service (GTT workflow, synchronized draw cadence) -> AM/PM transition (per `docs/architecture/PM-OPERATIONS-MODEL.md`) -> PM service (standalone services, service-staff Reception coverage per the RESOLVED Model C decision) -> closing. **No gap identified**; this flow is already modelled in the staffing/scheduling documents.

## 3. Operating Model Stress Test

Using the existing solver-verified AM/PM timetables (`docs/architecture/OPERATING-MODEL-18-CLIENTS.md`, `docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md`, `docs/architecture/PM-OPERATIONS-MODEL.md`):

| Scenario | 6/day | 12/day | 18/day (committed) |
|---|---|---|---|
| Baseline staffing absorbs volume | Yes, over-provisioned (same 8-staff headcount as 12/18 at the committed 25-min cadence, per `docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md`) | Yes | Yes, design case |

**Disruption stress test, real failure points identified, not assumed:**

- **Late client:** absorbed by the existing scheduling buffer; no model change required.
- **Difficult venepuncture (real rate: 1 in 10, per `docs/review-audit.md`):** genuine failure point if it pushes Draw 2 outside the T=60±5min window; the mitigation already exists (2 active phlebotomists, room built for a 3rd), but escalation beyond the 2nd on-site phlebotomist is a **genuine, unresolved dependency on WDP's own escalation protocol**, not an internal role. **Do not invent a phlebotomy supervisor role**, per standing instruction; the correct minimum action is to obtain WDP's actual escalation protocol in writing (an external-dependency item, not a staffing change).
- **Vasovagal/fainting event (5% of patients):** the vasovagal recliner (E04) and staff training already account for this; no model change required.
- **Staff absence:** relief pool already modelled for phlebotomists and treatment staff; genuine failure point only if 2+ relief staff are absent simultaneously, an acceptable residual risk at this staffing scale, not a design flaw.
- **Treatment overrun:** absorbed by curtain-partitioned rooms and the shared Massage+Beauty pool's own modelled peak concurrency; no model change required.
- **Cafe delay:** low operational risk, no clinical timing dependency; no model change required.
- **Client requiring accessibility assistance:** genuine gap, since AS 1428.1 compliance is professional-verification-dependent on the confirmed venue; not a staffing gap, a venue-dependent one.
- **Equipment failure (centrifuge specifically):** the register's own note already flags the centrifuge as "the single most critical piece of equipment in the venue"; no backup unit is currently planned, a genuine, disclosed gap (`PROCUREMENT-ITEM-SPECIFICATION-COVERAGE.md`'s E15 worked example).
- **Specimen problem (missed window, contamination):** WDP's own specimen-rejection consequence is already disclosed (`docs/review-audit.md`); the mitigation is process discipline (T=60±5min), not a staffing or equipment change.
- **Sudden PM demand:** absorbed by the service-staff PM coverage model (Model C, resolved 2026-08-21); no model change required.

**No staffing model change is recommended.** The only genuine, unresolved failure points are: (1) WDP's escalation protocol for difficult venepuncture beyond the 2nd phlebotomist, an external dependency; (2) no centrifuge backup, a procurement gap; (3) accessibility compliance, a venue-dependent professional-verification item. All 3 are already tracked in existing documents; none required a staffing change to resolve.

## 4. SOP Master Register

| SOP/Policy | Category | Owner | Dependency | Status |
|---|---|---|---|---|
| In-house GTT Clinical Protocol | Critical before opening | Clinical Coordinator + Venue Manager | None | EXISTS (`docs/gtt-clinical-protocol.md` v1.0) |
| Emergency Response Plan | Critical before opening | Venue Manager | None | EXISTS (`docs/emergency-plan.md` v1.0) |
| Consent form | Critical before opening | Clinical Coordinator | None | EXISTS |
| Privacy policy | Critical before opening | Venue Manager | None | EXISTS |
| Patient intake form | Critical before opening | Reception | None | EXISTS |
| Difficult-venepuncture escalation protocol | Critical before opening | WDP + Clinical Coordinator | WDP confirmation | NOT YET CONFIRMED (external dependency, not internally resolvable) |
| WHS policy (consolidated) | Critical before opening | Venue Manager | None | NOT YET BUILT |
| Day-in-the-life operational SOP (client + staff journey, consolidated) | Required before staff training | Venue Manager | None | NOT YET BUILT (information exists, not consolidated) |
| Employment contract template | Required before staff training | Anthony/HR | None | NOT YET BUILT |
| Opening/closing daily checklist | Required before soft opening | Venue Manager | None | NOT YET BUILT |
| Complaints-handling SOP | Required before soft opening | Venue Manager | None | NOT YET BUILT |
| Refund/cancellation policy (beyond the existing booking T&Cs) | Required before soft opening | Venue Manager | None | PARTIAL (booking policy exists in `docs/onboarding.md` B0; no dedicated refund process) |
| Business continuity/emergency closure plan | Required before soft opening | Anthony/Venue Manager | None | NOT YET BUILT |
| Equipment servicing/maintenance schedule | Can be completed after opening | Venue Manager | Equipment delivered | NOT YET BUILT (reasonable to defer, no equipment exists yet to service) |
| Soft-opening plan | Required before soft opening | Anthony/Venue Manager | Venue secured, fit-out complete | NOT YET BUILT |

## 5. Clinical Pathway Audit

Client arrival (Reception, patient intake form) -> GTT eligibility/preparation (phlebotomist confirms fasting status, explains process) -> glucose administration (commercially prepared 75g solution, E21, administered by phlebotomist) -> blood collection (Draw 1/2/3 per the synchronized cadence) -> difficult venepuncture (escalation beyond the 2nd on-site phlebotomist is **WDP's own Licensed Collection Centre protocol, not an internal role**, per the register's own explicit, repeated statement across `MASTER-PROCUREMENT-SHOPPING-LIST.md`, `PROCUREMENT-CLINICAL-GTT-WDP-SPLIT.md`, and `gtt-clinical-protocol.md`) -> adverse event (vasovagal recliner, first-aid-trained staff, 000 escalation per the Emergency Response Plan) -> specimen handling (label, cold-chain, courier dispatch) -> dispatch -> WDP/pathology (WDP's own processing, outside GTT Center's operational control) -> results pathway (WDP/the client's own GP, not GTT Center) -> records (7-year retention, patient documentation drawer, E08/E40).

**Who performs each action:** phlebotomists (draw, glucose administration, specimen handling), Reception (intake, records administration), Clinical Coordinator (protocol ownership), WDP (specimen processing, results, escalation-protocol ownership beyond the 2nd collector).

**Investigation result on the phlebotomy supervisor question:** confirmed, again, this round: **no internal phlebotomy supervisor role is required or should be invented.** Senior clinical oversight beyond the 2nd on-site phlebotomist is WDP's own Licensed Collection Centre escalation protocol, a genuine dependency to obtain in writing from WDP directly (not yet obtained), not a gap to be filled with a new internal role or job posting.

## 6. Non-GTT Service Audit

| Service | Room/Layout | Equipment | Hygiene | Training | Compliance | Insurance Note | Cleaning/Waste | Consumables | Staffing | Client Workflow |
|---|---|---|---|---|---|---|---|---|---|---|
| Massage | Curtain-partitioned | Table (format undecided) or chair | Wipe-clean linen, table-roll barrier | Massage+Beauty shared pool | General consumer product safety | Standard professional indemnity | Standard | Oil, linen | Shared Massage+Beauty pool | Booked via Fresha, integrated into GTT wait |
| Beauty | Curtain-partitioned | Treatment bed, wax heater, tool kits | 2-sink fitout, WA Skin Penetration Code | Shared pool | WA Skin Penetration Code | Standard | Standard | Wax, brow tint, facial products | Shared pool | Same |
| Nails/pedicure | Open-plan, LEV | Nail table, dust collector, pipeless pedicure chairs | LEV extraction, disinfection solution | Nail technicians | WorkSafe WA (LEV) | Standard | Standard | Polish, files, tools | Dedicated | Same |
| Hair | Open-plan | Styling chair, backwash, named-brand tools | Standard | Hairdressers | AS/NZS 4088 | Standard | Standard | Shampoo/products | Dedicated | Same |
| Cafe | Solid-walled Cafe zone | Fridges, coffee machine, water tap | WA food-safety, TGA-listed products separate from clinical | Reception/PM staff | WA Food Business Notification | Standard, food-safety-specific coverage should be confirmed with the broker | Food-waste separated | Coffee, tea, cold drinks, pre-made food | Reception/PM coverage | Self-service purchase |

**Massage table vs chair, the requested concise recommendation:** the repository genuinely supports no evidence-based recommendation for a chair-based format (no specification, no pricing, no prior modelling exists for it anywhere in this repository, confirmed again this round). The table format has a full, existing specification and a real China/Australia price comparison already researched. **Recommendation: if a decision must be made without new external research, the table/bed format is the only one with an evidenced basis; adopting the chair-based format would require commissioning fresh product research first.** This is not a resolution of the founder decision, it is a statement of which option the existing evidence actually supports, consistent with the standing instruction to provide a recommendation only where evidence supports one.

## 7. Opening Sequence Critical Path

Venue secured -> measurement -> design (against the confirmed floor plan) -> professional verification (electrical, plumbing, HVAC/LEV, accessibility, WDP room sign-off) -> builder RFQs (3 quotes) -> procurement release (site-dependent items move to RFQ) -> construction -> equipment delivery -> installation -> staff recruitment -> training -> SOP implementation -> testing -> soft opening -> opening.

**Can begin before venue:** Massage format decision, insurance quote request, employment contract drafting, WHS policy drafting, complaints/refund policy drafting, business continuity plan drafting, soft-opening plan drafting, all of Procurement Queue 1 (Buy Now) and Queue 2 (RFQ Now), HVAC/LEV contractor and Cafe/coffee supplier identification, staff recruitment (job postings already exist).

**Cannot begin before venue:** measurement, professional verification, builder RFQs, construction, site-dependent equipment installation, final toilet-count-dependent consumable quantities.

## 8. Missing Business Infrastructure (Confirmed Gaps, Not Speculative)

Employment contract template, WHS consolidated policy, complaints-handling SOP, dedicated refund/cancellation policy beyond the existing booking T&Cs, business-continuity/emergency-closure plan, soft-opening plan, a consolidated day-in-the-life operational SOP, a real insurance quote (currently a placeholder figure only), a centrifuge backup/contingency plan. **Not a gap, already adequately covered:** privacy, consent, client records, booking/payment, IT, marketing, cleaning consumables, stock management, supplier lists (contact not yet made, but the lists themselves are complete).

## Critical Blockers (Would Genuinely Stop Opening)

Insurance not bound. No employment contract. No business-continuity plan. Massage format undecided (blocks one equipment order, not the venue itself). WDP's 3 outstanding confirmations and escalation-protocol detail.

## Founder Decisions Still Open

Massage table vs chair (urgent, blocks a ready RFQ). Laundry model (not urgent). Hand dryer vs paper towel, facial steamer, colour hair, hair clippers, retail brand (all low-value, not urgent).

## External Dependencies

WDP (centrifuge, medical waste, glucose solution, escalation protocol, room sign-off), insurance broker (not yet contacted), HVAC/LEV contractor (not identified), Cafe food supplier (not identified), coffee/beverage supplier (not identified), 5 named Australian salon/spa suppliers (not contacted), China sourcing agent (enquiry ready, not sent).

## Professional Verification Required

Electrician, plumber, HVAC/LEV contractor, access consultant, building surveyor, fire safety officer: all gated on a confirmed, measured venue.

## Pre-Venue Work That Can Start Now

Massage format decision, insurance quote request, employment contract drafting, WHS policy, complaints/refund policy, business-continuity plan, soft-opening plan, day-in-the-life SOP consolidation, Procurement Queues 1 and 2, HVAC/LEV and Cafe/coffee supplier identification, staff recruitment against existing job postings.

## First 30 Days After Venue Acquisition

Site measurement and professional verification (Week 1), builder RFQ process (Weeks 1-2), procurement release for site-dependent items (Week 2), construction start (Week 3+), staff recruitment finalised and training scheduled against the confirmed fit-out timeline.

## Critical Path to Opening

Massage decision (can happen now) -> venue secured -> measurement/verification -> builder selection -> construction -> equipment delivery/installation -> opening stock -> staff training -> SOP implementation and testing -> soft opening -> opening. Insurance, employment contracts, WHS policy, complaints/business-continuity/soft-opening plans should all be completed in parallel with construction, not treated as post-opening tasks, since none of them depend on the venue.

## Sourcing

`docs/architecture/SOURCE-OF-TRUTH-TIERS.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/architecture/PROCUREMENT-EXECUTION-STATUS.md`, `docs/gtt-clinical-protocol.md`, `docs/emergency-plan.md`, `docs/onboarding.md`, `docs/insurance-broker-quote-request-draft.md`, `docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md`, `docs/architecture/PM-OPERATIONS-MODEL.md`, `docs/review-audit.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as a concise, decision-oriented venture opening readiness audit, using only current-state and source-of-truth-tier-1-3 documents. No property search, WDP correspondence, settled pricing, venue program, procurement model, or Master Dossier structure was touched, since no genuine contradiction was found in any of them.
