# Entity Recommendation Memo for the Accountant (P1b, C4)

**This is general knowledge, not your personal documents. Verify with your accountant before acting.**

Prepared 2026-10-16 by Grace for Theodore (CFO), Catherine (legal and lease), the accountant and the solicitor. Builds on docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md (2026-09-04), which set out the options without recommending.

## 1. What is verified and what is assumed

| Fact | Status | Source |
|---|---|---|
| YETI Holding Trust is a discretionary trust; corporate trustee is YETI Tipi Holdings PTY LTD | Verified in repo | ENTITY-STRUCTURE-INVESTIGATION.md, financial-setup.md |
| Cudan Studio Pty Ltd exists as a company; used as publisher entity for another venture because revenue must stay outside Anthony's personal income | Verified in Cudan and DataForge records. Its ownership and trading scope are NOT in the GTT repo. | data-forge publisher file |
| Withers property is held in the Holding Trust | Stated by Anthony; appears in the second-brain financial files. Not re-verified against title or deed. | second-brain financial docs |
| "Operational Trust" | **Could not be identified.** Searched the GTT repo, the Second Brain and Cudan files for "operational trust" and "operating trust": no entity of that name. The only trust named is YETI Holding Trust. Anthony to say whether this is a separate trust, a nickname for the Holding Trust, or something yet to be set up. | search 2026-10-16 |
| Anthony receives a TPI Disability Compensation Payment; business income must stay outside his personal income | Verified as instruction | CLAUDE.md, dva-tpi-research.md |
| Repo research says trust income has zero effect on TPI; Anthony's brief says trust distributions or dividends to him "would count as income" | **CONFLICT.** Not resolved here. Accountant and DVA-qualified adviser to confirm for each option. | dva-tpi-research.md vs P1b brief |
| Draft 30 per cent minimum tax on discretionary trusts from 1 July 2028 | Verified as exposure draft only (released 2026-09-03). Check status of the final law. | ATO page, ENTITY-STRUCTURE-INVESTIGATION.md |
| Imara holds no role in GTT | Rule. She is not a director, officer or approver in any option below. | CLAUDE.md |
| Any ownership of Cudan Studio Pty Ltd shares, director names, who is a beneficiary | Not in repo. Assumed unknown. | |

## 2. The options

**(a) Anthony's "Operational Trust"**: not identifiable (see above). If it is a new or separate trust, treat it like a discretionary trust option (b2 below). We cannot assess it until it is identified.

**(b) A new dedicated Pty Ltd ("GTT Pty Ltd")**, with sub-options: b1 shares held by the trustee of YETI Holding Trust; b2 shares held by a new separate trust with its own trustee; b3 shares held in some other way.

**(c) Cudan Studio Pty Ltd** trades GTT as a second business line.

| Factor | (a) Operational Trust | (b) New Pty Ltd | (c) Cudan Studio Pty Ltd |
|---|---|---|---|
| Clinical and public liability ring-fence (pregnant clients, blood collection on premises) | Unknown. A trust trading directly exposes the trustee and trust assets | Best: liability sits in a company that carries only the GTT insurance, lease and staff | Weak: a GTT claim reaches Cudan's studio assets and photography business |
| Protecting Cudan | n/a | Strong: Cudan unaffected | Weak: shared liability |
| Protecting Withers (in Holding Trust) | Depends on identity of trust | Good if shares sit under a different trust (b2) or if the company, not the trust, signs everything. In b1 the shares are trust assets but the company's debts are not the trust's, unless the trust or Anthony guarantees the lease | Moderate: Cudan owner structure not in repo |
| TPI: business income outside Anthony's personal income | Unknown | Company profit is taxed in the company. Dividends to the trust, then distributions to beneficiaries, may still reach Anthony: accountant to ensure he is not the recipient | Same issue |
| Lease, lab contracts, employer registration, GST, payroll tax, workers compensation | Possible but a trust trades through its trustee | Clean: one entity with its own ABN, GST registration, payroll registration, insurance, bank | Mixed with Cudan's books, GST and payroll |
| Pathology partner and landlord preference | Often prefer a company | Preferred. Personal guarantees are likely requested by the landlord: TO CONFIRM who gives them | Acceptable |
| Investors and a later sale | Hard (trust) | Easy: sell shares or the business; a clear cap table | Hard: need to carve out GTT |
| 2028 trust minimum tax | Depends on trust type | Company is not a discretionary trust, so outside the draft minimum tax | Same as (b) |
| Cost and admin | Low | Incorporation, ASIC fees, company tax return, Division 7A on loans between company and trust: not quantified (PLACEHOLDER in the earlier memo) | Lowest |

## 3. Recommendation (for the accountant to confirm)

**Trade GTT through a new dedicated Pty Ltd (option b), kept separate from Cudan Studio Pty Ltd, with its shares held in a way the accountant confirms keeps income out of Anthony's personal hands.**

Reasons: the clinical and public liability exposure of blood collection and pregnant clients is the strongest argument in the file; it should not touch Cudan or the Withers property; the lease, lab contract, staff and insurance all need one clean legal person; and it is the easiest to sell or bring investors into. Option (c) is not recommended because it mixes a clinical-risk venture with a working photography studio. Option (a) cannot be assessed until the "Operational Trust" is identified.

Share holding (b1 versus b2) is the accountant's call. A separate trust (b2) gives better asset separation from Withers but more admin. The earlier memo's fixed-distribution election for YETI Holding Trust is a separate decision about the Holding Trust and can run in parallel.

Cautions the accountant must address: who is director and shareholder (Anthony's role, given his stated "cannot work" position and the repo's "non-operational, administrative only" note; Imara cannot hold a role); personal guarantees for the lease and for the loans; Division 7A if funds move between trust and company; the timing of GST registration and an ATO private ruling, which needs the entity first.

## 4. Five questions for the accountant

1. Which entity structure do you recommend for GTT (new Pty Ltd under the YETI Holding Trust, a Pty Ltd under a new separate trust, Cudan Studio Pty Ltd, or something else) and why? What is "Operational Trust", and is it relevant?
2. How do we make sure no profit, dividend or distribution reaches Anthony personally, and what does that mean for his TPI? (Resolve the conflict between the repo research, which says trust income has no effect, and the working assumption that dividends and distributions count as income.)
3. What happens to the 2028 minimum tax on discretionary trusts if we use the Holding Trust as shareholder, and should the trust elect fixed distributions?
4. What are the incorporation, ongoing and Division 7A costs, and can the lease, lab agreement, employment contracts and Fresha set-up all start in the new entity (so nothing has to be transferred later)? Who gives personal guarantees?
5. How should GST registration, the ATO private ruling and payroll or workers compensation registration be sequenced against the entity set-up and first booking?

## 5. Not decided here
This memo does not decide anything. A decision by Anthony should be logged in DECISION-LOG.md with its date.
