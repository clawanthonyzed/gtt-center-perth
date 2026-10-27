# CATHERINE R23 PART 2: are "reasonably accessible to the public" and "reasonable hours" an issue? (job 2)

DRAFT, 2026-10-27. Tags as in PART-1. Not legal advice: health lawyer to check.

## READ-FIRST CHECK (docs/GTT-READ-FIRST.md, Round 23)
- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw.
- Path A = PREFERRED, package with the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult.
- Path A: A$320 / A$370 advertised, GTT charges A$292.15 / A$342.15. Path B: A$300 / A$350 all in, GTT charges A$272.15 / A$322.15. <!-- factcheck:ok -->
- Rebates "about": consult A$32.95 + lab A$22.05 = A$55.00.
- Midwives 08:00 to 16:00; first consult 08:15, 25 minute blocks to 10:30.
- Late rule: arrive at least 10 minutes early; late means from the appointment time onwards.

## Anthony's question
"We are not going down the approved collection centre route, so is 'not reasonably accessible to the public' and 'reasonable hours' actually an issue?"

## Short answer
**No. Confidence: high (about 90 percent).** Both phrases bind only an approved collection centre, which GTT will not be. The 10 percent is not about these phrases. It is about two other rules that the non-ACC route depends on (section 4).

## 1. Where the phrases come from (V, Health Insurance Act 1973, Compilation 136, read 2026-10-27 from library copy r22c/raw)
| Item | Finding |
|---|---|
| Instrument | Health Insurance Act 1973, Part IIA, **s 23DNG(1)(ba) and (bb)** |
| Exact words | "The Minister may revoke an approval (the current approval) granted for a specimen collection centre if the Minister is satisfied that: ... (ba) the centre is not reasonably accessible to the public; or (bb) the centre does not operate under reasonable hours" |
| What kind of rule | A **revocation ground**, and it is discretionary ("may"). Not a licence condition, not a criminal offence |
| What it attaches to | "an approval ... granted for a specimen collection centre", meaning an approval under s 23DNBA |
| Who holds that approval | Only an **approved pathology authority** (the lab owner), and only for an "eligible collection centre" on premises the authority owns, leases, sub-leases or "is otherwise entitled to occupy" (s 23DNBA(1); s 23DA(1) definition) |
| Who it binds | The lab, for its approved collection centre. Not the lab's laboratory (that is s 23DN), not a requester, not a lounge |
| Where else | Nowhere. The Approvals for Eligible Collection Centres Principles 2020 contain no access or hours test (full instrument read, L, APA-LAB-CATEGORIES-AND-ACC-ACCESS.md). The 13 government pages, the AskMBS advisories and the Handbook never use the words (V, 2026-10-27). The Revised Explanatory Memorandum says the change lets the Minister revoke "the Medicare approval for a pathology collection centre" (L, HIA-23DNG-1A-MINIMUM-BENEFIT.md) |

Nearest relatives (neither binds GTT): NPAAC Collection Centre Guidelines C1.1(viii) "Hours of operation should be displayed" (a "should", for approved centres; other settings use it "for guidance", L); National Pathology Standards 2027 Standard 6.04, the lab publishes its centres' "opening hours" (lab accreditation duty from July 2027, L).

## 2. Whose collection point is it? (R, repo)
| Question | Repo answer | Source |
|---|---|---|
| Who employs the midwife | GTT Medical Services Pty Ltd | R: CATHERINE-R20, R22A-PART-2 |
| Who employs the phlebotomists | GTT Medical (the 2026-09-19 decision "GTT employs both phlebotomists directly"; Catherine R16 locked Medical as employer of midwife and collectors) | R: DECISION-LOG.md 2026-10-17 entry; LAB-BILLING-WORKFLOW-R19.md; GRACE-R22-PART-6 table |
| Whose room | A GTT Medical practice collection room inside the venue. The lab owns, leases or occupies nothing at GTT | R: LAB-BILLING-WORKFLOW-R19 (question C-b) |
| Lab's role | Receives the request and samples, tests, bills the client direct. GTT never touches lab money | R: GTT-READ-FIRST.md |

Gaps to fix (not legal changes, just records): GTT-READ-FIRST.md says "2 phlebotomists" but does not say who employs them; theodore_r22.py puts phlebotomist wages in the "morning lounge" segment. If the Lounge became the employer, Path A would break (section 3). I recommend READ-FIRST says "phlebotomists are employed by GTT Medical" (QUESTIONS FOR ANTHONY, Q1).

## 3. Why GTT does not need an approved collection centre for Path A (V, s 16A(5AA), s 3B)
A Medicare benefit for the lab test is payable only if the sample was collected in one of the listed ways (s 16A(5AA)). The approved collection centre is only one of them, para (d). GTT uses para **(c)(iv)**: if the treating practitioner (our midwife) "is employed ... by a medical entrepreneur", the sample may be collected "on behalf of the treating practitioner, by another employee of that medical entrepreneur, or by a person engaged under a contract for services by or on behalf of that medical entrepreneur".
- GTT Medical is a "medical entrepreneur": s 3B item 2 covers a business that employs a "participating midwife" to give a midwifery service (V).
- So a GTT Medical phlebotomist drawing blood on a GTT midwife's request fits (c)(iv). No collection centre approval is needed, and s 23DNG never applies.
- The Department's own page says samples can be taken by "your doctor or their practice staff" (file 08, V). Same idea.

## 4. The residual risk (the 10 percent), with the nearest compliant fix
| # | Risk | Fix | Tag |
|---|---|---|---|
| 1 | **Employer mismatch.** If the phlebotomist is employed by the Lounge, Holdings or a labour hire firm, (c)(iv) is not met and Path A loses the lab benefit | Phlebotomists on GTT Medical's payroll, or contracted to GTT Medical in writing | V law, R |
| 2 | **Lab staff drawing at GTT.** A lab employee collecting in a room that is not an approved collection centre fits neither (d) nor (c)(iv), unless engaged by GTT Medical under a contract for services. If the lab supplies collectors free or below cost, that is a benefit to a requester (Part IIBA, s 23DZZIF, L) | Do not use lab staff at GTT. If ever needed, GTT Medical pays a market rate under a written contract | V, L, U |
| 3 | **Request must come from our midwife.** (c)(iv) works only on the GTT midwife's request. Outside requests are Path B: no benefit, s 23DNL notice before the draw (locked) | Keep: Path B notice and lab standing letter (CATHERINE-R22B-PART-5) | V |
| 4 | **s 23DNL read literally.** It binds "a person who operates a specimen collection centre that is not an approved collection centre". A "specimen collection centre" is any "place for collecting pathology specimens" (s 23DA(1)), so GTT's room is one. Read literally, the no-benefit warning would be due before every draw, even Path A, where it would be untrue. Every general practice with a practice nurse taking blood is in the same position. My reading: the section targets collections where no benefit is payable. Not tested | Ask the Department in writing (PART-3, question 2). Until answered, keep the locked rule: s 23DNL words for Path B only | U |
| 5 | **Collection item.** 73928 is "collected in an approved collection centre" (R, THEODORE-R21). Without an ACC, that item does not fit on its face | Already parked for AskMBS; GTT's own money does not change (locked). Question drafted in PART-3 | R |
| 6 | **Lab acceptance.** The lab must still accept samples GTT collects (NPAAC labelling, request, transport rules, L) | The lab agreement covers its collection manual, labels and transport | L, U |

Fallback if the Department ever says an approved collection centre is needed: the lab holds the approval for a room at GTT, with public booking, published hours (for example 07:00 to 11:00 Monday to Saturday) and a listing on the lab's finder (L, APA-LAB-CATEGORIES-AND-ACC-ACCESS.md W1 to W5). Only then would (ba) and (bb) matter.

Regards.
Catherine
