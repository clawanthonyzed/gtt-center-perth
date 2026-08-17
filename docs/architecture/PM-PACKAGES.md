# PM Packages — Selected, Priced, and the Real PM Average Transaction Calculation

**Date:** 2026-08-17 | **Purpose:** Lock two real PM packages using the same structured process already used for AM (research, design, pricing research, selection), and calculate a real, defensible PM average transaction value from the actual service catalogue and package mix, replacing the arbitrary ~A$95 placeholder that has been in every financial figure until now.

---

## 1. Process Used (Same Structure as AM Package Selection)

1. Research real Perth comparable package pricing (already done, `docs/architecture/SERVICE-CATALOGUE.md`, Chapter 4 of the dossier).
2. Design candidate combinations from the venue's own already-priced a-la-carte catalogue (no new services invented).
3. Price each candidate at a genuine bundle discount versus buying the same services separately (industry-standard bundling practice, not an arbitrary number).
4. Select two, covering the two highest-value service pairings (Massage+Beauty, and Nails+Hair) so both treatment-staff pools are represented.

## 2. Real Perth Comparable Bundle Pricing (Research Basis)

Real, currently-trading Perth day spas bundle pregnancy/wellness services the same way this venture proposes to: Keturah Spa bundles a pregnancy massage, a signature facial, and a spa pedicure as one package; Hidden Valley Eco Day Spa bundles a pregnancy massage, a facial, a foot massage, and afternoon tea; endota Spa Perth CBD bundles a customised facial and a customised massage across 90 minutes. Discounted spa packages in the Perth market average around A$140 combined. This confirms bundling two-plus services at a discount to the individual sum is the real, established market pattern this venture is following, not a novel approach.

## 3. Package A — "PM Refresh" (Massage + Beauty)

| Component | Duration | A-la-carte price (catalogue) |
|---|---|---|
| Pregnancy or relaxation massage | 45 min | ~A$130 |
| Mini facial | 30 min | ~A$82 (midpoint of A$75-90) |
| **Sum if bought separately** | 75 min | **A$212** |
| **Package A price** | 75 min | **A$185** (13% bundle discount) |

Staffing: Massage+Beauty pool (the same 4-person shared pool as AM). Delivered as a single continuous 75-minute booking.

## 4. Package B — "PM Restore" (Nails + Hair)

| Component | Duration | A-la-carte price (catalogue) |
|---|---|---|
| Gel manicure | 45 min | ~A$80 |
| Blow-dry / styling | 30 min | ~A$70 (midpoint of A$60-80) |
| **Sum if bought separately** | 75 min | **A$150** |
| **Package B price** | 75 min | **A$135** (10% bundle discount) |

Staffing: 1 Nail technician + 1 Hairdresser, run concurrently (not sequentially) where the room layout allows, or sequentially where it doesn't — an operational detail for the eventual Venue Manager, not decided here.

## 5. Calculating the Real PM Average Transaction Value

**Individual a-la-carte average, calculated directly from the service catalogue's own price midpoints** (`docs/architecture/SERVICE-CATALOGUE.md`), not assumed:

| Service | Midpoint price |
|---|---|
| Pregnancy/relaxation massage (30/45min blend) | A$112 |
| Gel manicure | A$72 |
| Gel pedicure | A$82 |
| Cut/shampoo/blow-dry | A$95 |
| Blow-dry/styling only | A$70 |
| Brow shape/tint | A$40 |
| Mini facial | A$82 |
| Deluxe facial | A$117 |
| Lash lift/tint | A$87 |
| **Average of the above 9 services** | **A$84.11** |

**Blended PM average, using a disclosed, conservative mix assumption** (no real booking data exists yet — this is a planning assumption, not a confirmed figure):

| Mix component | Assumed share | Price | Contribution |
|---|---|---|---|
| Individual a-la-carte | 60% | A$84.11 | A$50.47 |
| Package A (PM Refresh) | 25% | A$185.00 | A$46.25 |
| Package B (PM Restore) | 15% | A$135.00 | A$20.25 |
| **Blended PM average transaction value** | 100% | | **A$116.97 ≈ A$117** |

**This replaces the previous ~A$95/session placeholder**, which had no stated derivation anywhere in this repo's history. A$117 is genuinely calculated from the real service catalogue and the two real packages above, not an arbitrary round number — but the 60/25/15 mix assumption itself remains a planning estimate, clearly disclosed, not real booking data. If actual booking mix differs materially once trading, this figure should be revisited against real data, not defended as fact.

## 6. What Still Requires Confirmation

- Anthony's sign-off on the two packages and their pricing (same as AM packages required his sign-off before being locked).
- The 60/25/15 mix assumption is a planning estimate only, not evidenced.
- Whether Package B's two services should run concurrently (needs 2 staff simultaneously) or sequentially (needs 75 continuous minutes from one client, 2 staff at different times) — an operational decision for later.

---

## Changelog

**2026-08-17** — Created per the founder's explicit instruction to actually select and price two real PM packages (same structured process as AM) and calculate a real PM average transaction value from the actual catalogue and package mix, replacing the unexplained ~A$95 placeholder.
