> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

# CATHERINE R21 PART 2: Medicare pricing setup (job 1) and the outside request route (job 2)

DRAFT, 2026-10-26. Tags as in PART-1.

## Job 1 continued: compliant setup for each risk

| Risk | Compliant setup | Tag |
|---|---|---|
| Fee disclosure (informed financial consent) | Show the A$130 consult fee, the "about A$32.95" rebate and the gap on the booking page before payment, and again in the confirmation email. | V (MN note), U |
| Bundling the consult with lounge services | Lawful if the consult has its own price and its own account from **GTT Medical**, and the lounge has its own tax invoice from **GTT Lounge**. One payment screen is fine. One combined receipt with no consult line is not: s 19(6) needs "the amount charged in respect of the service". | V, U |
| Consult compulsory inside Package B | Lawful because a real alternative exists (option A, or no package). Inside B, the consult must be real care: history, risk check, glucose test counselling, the request, and written notes. If the midwife decides the test is not right for her, the lounge part is refunded (R20 section 3.3). | V (MN.13.16), U |
| Tying the lounge to a consult from a related company | Competition law (third line forcing) is a risk only where it substantially lessens competition, and related companies count as one. Low risk. **Lawyer to check.** | U |
| Itemised account timing | GTT Medical emails the itemised account on the day of the consult, after it ends, dated that day. The booking payment receipt says "consult fee paid in advance; your Medicare account follows after your consult". | V (s 49), U |
| Price above comparators | No change needed. Do not claim "best price", "lowest gap" or "Medicare price". Comparisons with named competitors are lawful only if true and like for like; I recommend none. | V (ss 18, 29), U |
| PSR protection | Notes for every consult with start and end times; never bill 82105 when a consult is cut below 10 minutes; one client per consult (MN.13.16). | V |

**Draft itemised account (GTT Medical):**
> GTT Medical Services Pty Ltd, [address], ABN [number]
> Patient: [full name]. Date of service: [date].
> MBS item 82105: short antenatal professional attendance by a participating midwife. Provided by [midwife name], provider number [number], who provided this service.
> Amount charged: A$130.00 (GST-free). Paid: A$130.00 on [date]. Outstanding: A$0.00.
> You can claim your Medicare benefit (about A$32.95) with this account.

(The square-bracket items are fields the booking system fills in, not unfinished text.)

**Draft booking-page line:**
> Midwife consult (20 minutes, with a GTT midwife): A$130.00, GST-free. Medicare benefit about A$32.95, which you claim after you pay. Your gap is about A$97.05. Our fee is set by GTT, not by Medicare.

---

## Job 2. Option A: client keeps her outside request

### 2.1 The law (L: HIA-SECTION-16A.md; V this round: s 23DNL, Compilation 136 text)

| Rule | Text | Tag |
|---|---|---|
| s 16A(5AA) | No benefit for a pathology service on a treating practitioner's request "unless the pathology specimen ... was collected" by: (c)(i) the person herself; (ii) the treating practitioner; (iii) the treating practitioner's employee or contractor; (iv) if the treating practitioner is employed by a medical entrepreneur, another employee of that entrepreneur; or (d) lab staff at an approved collection centre, her home, a hospital or a care home | L |
| s 23DNL | A person who operates a specimen collection centre that is not an approved collection centre "must cause to be taken such steps as are reasonable ... to ensure that, before a pathology specimen is collected", the client and "the approved pathology practitioner by or on behalf of whom the pathology service is to be rendered" "are informed that, if the approved pathology practitioner were to use the specimen in rendering a pathology service, a medicare benefit would not be payable in respect of the pathology service." Penalty: 20 penalty units | V |
| Penalty amount | 20 penalty units = A$7,280 | L (Catherine R15) |

### 2.2 How it applies

| Question | Answer | Tag |
|---|---|---|
| Is option A unlawful? | **No.** A private, non-Medicare blood collection is lawful. It becomes unlawful only if GTT skips the s 23DNL warning, or tells her she can claim. | V, U |
| When must the notice be given? | **Before the specimen is collected.** Best practice: at booking (so the price choice is informed) and again in writing at check-in, signed, before the draw. | V |
| Who must be told? | **Both** the client and the lab's approved pathology practitioner. A sign on the wall alone does not reach the lab. Send a written note with the request and sample (a sticker or slip). | V |
| Could the lab fee still be rebatable another way? | **Not if collected at GTT.** GTT's phlebotomists are not employed by her outside practitioner (c)(iii), she is not employed by GTT (c)(iv), and GTT's room is not an approved collection centre (d). Self-collection (c)(i) does not suit a venous draw. | L, U |
| Nearest compliant fixes | (1) She chooses option B: a GTT consult and GTT request, so the test is rebatable. (2) She takes her outside request to the lab's own collection centre and books lounge services only. (3) Later: the partner lab runs its own approved collection room at GTT (Services Australia approval; Grace's track). | L, U |
| Is A$27.85 still the lab's fee? | Not known. With no Medicare benefit the lab may charge a different private fee. Get it in writing before option A goes live. | U |
| Same net price | For an eligible client, option B is A$320 less about A$55.00 = about A$265.00, the same as option A's A$265 with no rebate. Option A is best only for a client who cannot or will not claim Medicare. Say so plainly; no false "saving" claims. | R maths, U |
| What GTT receives (raised, not decided) | Option A: A$265.00 less A$27.85 = **A$237.15** (Package 1), A$287.15 (Package 2), all GST-taxable lounge revenue. Option B: A$292.15 / A$342.15, of which A$130 is GST-free. Not "the same amount". Theodore to model. | R maths |

### 2.3 Draft wording (lawyer to check)

**Booking screen, option A:**
> You have chosen to use your own pathology request from your doctor or midwife. Because GTT is not an approved pathology collection centre, **Medicare will not pay any benefit for your glucose test** if your sample is collected here on that request. The lab bills you its full private fee. If you would like a Medicare benefit, choose a GTT midwife consult instead, or take your request to one of the lab's own collection centres.

**Written notice, signed at check-in before the draw (statutory words in bold):**
> Before we collect your sample: GTT is not an approved collection centre. **If the approved pathology practitioner were to use the specimen in rendering a pathology service, a Medicare benefit would not be payable in respect of the pathology service.**
> ☐ I have read this and I want my sample collected here.  Signed: ______  Date: ______

**Slip sent to the lab with the request and sample:**
> Notice under Health Insurance Act 1973 s 23DNL: this specimen was collected at a centre that is not an approved collection centre. If the approved pathology practitioner were to use the specimen in rendering a pathology service, a Medicare benefit would not be payable in respect of the pathology service.

Do not use the s 23DNL words for option B clients (R15 B3: for them a benefit is payable, so the words would be false).

Regards.
Catherine
