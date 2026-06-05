# GTT Center Perth — Website Specification
## Version 1.0 | June 2026
## Owner: Poppy (Marketing) | Developer required by Week 7

---

## 1. OVERVIEW

**Purpose:** Generate 300+ waitlist signups before soft open. Support SEO. Enable GTT bookings with timing constraint.

**Timeline:**
| Phase | Content | Deadline |
|---|---|---|
| Phase 1 — Waitlist landing page | Single page: hero, value prop, waitlist form | Week 7 (before Instagram launch) |
| Phase 2 — Full website | All pages, booking widget, SEO content | Week 16 (before soft open) |

**Platform recommendation:** Squarespace (no-code, fast to launch, Fresha widget compatible)  
**Alternative:** WordPress (more SEO control, higher dev cost)  
**Decision required by:** Week 5

**Domain:** Register `gttcenterperth.com.au` AND `gttcentreperth.com.au` immediately (US vs AU spelling). Both for A$20/year each.

---

## 2. PHASE 1 — WAITLIST LANDING PAGE (Week 7)

### Required elements

**Hero section:**
- Headline: "Perth's First GTT Wellness Lounge — Opening [Month] 2026"
- Subheadline: "Transform your 2.5-hour GTT wait into a premium self-care morning. Massage, nails, brows, and more — while you wait for your test results."
- Background: high-quality pregnancy wellness imagery (sourced from Unsplash or professional shoot)
- CTA button: "Join the Waitlist"

**Value proposition (3 bullets):**
- ✓ Your GTT blood draws — on-site, by a qualified phlebotomist
- ✓ Premium wellness services during your 2.5-hour wait
- ✓ Perth's first dedicated GTT wellness venue

**Waitlist form (MANDATORY fields):**
- First name
- Last name
- Email address
- Mobile number
- Suburb
- Due date (month + year — not exact date)
- Which services are you interested in? (checkboxes: Massage / Nails / Brows / 3D Scan / Dietitian)
- How did you hear about us? (dropdown: Midwife / OB/GYN / Instagram / Google / Friend/Family / Other)
- Privacy Collection Notice (visible text): "GTT Center Perth collects this information to notify you when bookings open. See our Privacy Policy [link]."
- Checkbox: "I agree to the Privacy Policy and consent to GTT Center Perth contacting me about my booking."
- Submit button: "Join the Waitlist"

**Post-submission:**
- Thank you page: "You're on the list! We'll email you as soon as bookings open. Follow us on Instagram for behind-the-scenes updates."
- Automated email (via Resend): "You're on the GTT Center Perth waitlist. We're opening [Month] 2026 in [suburb area]. First on the list gets first pick of opening day bookings."

**Footer (Phase 1 minimum):**
- "GTT Center Perth | YETI Holding Trust | [Phone] | [Email]"
- Privacy Policy link (must be live)
- Instagram link

**Privacy Policy page:** Must be live before the waitlist form goes live (see docs/privacy-policy.md).

---

## 3. PHASE 2 — FULL WEBSITE (Week 16)

### Site map

```
Home
├── About GTT Center Perth
├── Services
│   ├── GTT Morning Experience
│   ├── Afternoon Wellness
│   ├── 3D Keepsake Scan (Bloom Baby)
│   └── Dietitian Consultation
├── Book Now (Fresha widget — see §4)
├── Packages & Pricing
├── FAQ
├── Contact
├── Blog (SEO content — see §5)
│   ├── What is the GTT test?
│   ├── How to prepare for your GTT test
│   ├── GTT test Perth — what are your options?
│   ├── What if I test positive for GDM?
│   ├── Pregnancy massage Perth — safe services
│   ├── Safe nail services during pregnancy
│   ├── Gestational diabetes diet
│   ├── GTT Center Perth vs standard pathology
│   ├── Is the GTT test painful?
│   └── GDM diagnosis in Perth — your complete guide
└── Privacy Policy
```

---

### Home page (Phase 2)

**Hero:** Full-width video or image — pregnant woman in a premium lounge, peaceful. Not clinical.

**Problem/solution hook:**
> "The GTT test is mandatory. The 2.5-hour wait doesn't have to be miserable."

**How it works (3 steps):**
1. Book your GTT slot online (choose start time 7:30am–9:30am)
2. Arrive fasting — we handle everything
3. Enjoy massage, nails, and more while your test runs

**Services section:** Visual grid. Photography-led.

**Social proof (once reviews exist):** Google review carousel.

**Waitlist/Book CTA:** "Join the Waitlist" (pre-open) → "Book Now" (post-open).

---

### Services pages

**GTT Morning Experience page:**
- What is the GTT (brief, reassuring — not clinical)
- What is included in each package tier (pricing table)
- Step-by-step morning timeline (arrive 7:30am → T=0 draw → massage/nails/brows → T=60 → T=120 → snacks and done)
- FAQ: "Do I still get Medicare bulk billing?" "Who gets my results?" "Can I leave during the test?" "What if I feel sick?"

**Afternoon Wellness page:**
- Standalone pregnancy wellness, no GTT required
- Services: massage, nails, brows, scan, dietitian
- Pricing (same afternoon packages)
- "You don't need a GTT appointment to enjoy our afternoon sessions"

---

## 4. BOOKING WIDGET — GTT TIMING CONSTRAINT

**Problem:** Fresha cannot natively enforce: GTT start time must be selected first → only services within the 2.5hr window display → services cannot overlap T=60 and T=120 draw times.

**Solution architecture (two options):**

### Option A (recommended): Custom form + Fresha API
- Build a custom booking form on the website
- Step 1: Patient selects GTT start time (7:30am, 8:00am, 8:30am, 9:00am, 9:30am)
- Step 2: Available services display with only time slots that fit within the patient's GTT window
- Step 3: Patient selects services and pays deposit (A$30) via Stripe
- Step 4: Booking is automatically created in Fresha via API
- Technical requirements: Squarespace custom code embed + Fresha API credentials + Stripe

**Estimated cost:** A$2,500–4,000 (developer, 15–20 hours)  
**Developer skills needed:** JavaScript, REST API integration, Stripe

### Option B (interim until custom flow built): Manual workaround
- Fresha widget handles all bookings
- Receptionist reviews every GTT booking daily and calls if pairing is wrong
- Hidden "GTT Timeslot" add-on in Fresha that patient MUST add as first item
- Known limitation: receptionist must review all bookings — budget 30 min/day

**Recommendation:** Build Option A before soft open. Use Option B as interim from Week 16 if Option A is not ready.

---

## 5. SEO CONTENT STRATEGY

Target keywords (zero commercial competition as of June 2026):
- "GTT test Perth" — primary target
- "gestational diabetes test Perth"
- "pregnancy massage Perth"
- "where to get GTT test Perth"
- "GTT test waiting time Perth"
- "gestational diabetes test what to expect"
- "GTT test fasting requirements"

**10 blog posts (800–1,200 words each):**

| Page | Primary keyword | Intent |
|---|---|---|
| What is the GTT test? | GTT test explained | Informational — early funnel |
| How to prepare for your GTT test | GTT test preparation | Pre-appointment — high intent |
| GTT test Perth — your options | GTT test Perth | Decision stage — highest conversion |
| What if I test positive for GDM? | GDM diagnosis Perth | Post-diagnosis — dietitian funnel |
| Pregnancy massage Perth — safe services | Pregnancy massage Perth | Afternoon wellness acquisition |
| Safe nail services during pregnancy | Safe nail polish pregnancy | Afternoon wellness acquisition |
| Gestational diabetes diet | Gestational diabetes diet Australia | Dietitian funnel |
| GTT Center Perth vs PathWest | Comparison page | Decision stage — conversion |
| Is the GTT test painful? | GTT test painful | Fear/anxiety — high search volume |
| GDM diagnosis Perth — your guide | GDM support Perth | Post-diagnosis long-term |

**SEO setup:**
- Google Search Console: verify site ownership, submit sitemap
- Meta descriptions and H1 tags for every page
- Schema markup: LocalBusiness (address, hours, phone), FAQ schema on FAQ page
- Google Business Profile: create and verify BEFORE soft open (takes 1–2 weeks for verification)
- Internal linking: every blog post links to "Book Now" CTA

---

## 6. TRACKING AND ANALYTICS

| Tool | Purpose | Setup |
|---|---|---|
| Google Analytics 4 | Traffic, conversion tracking | Week 7 (with Phase 1) |
| Google Search Console | SEO performance | Week 7 |
| Fresha analytics | Booking conversion | Fresha built-in |
| Resend analytics | Email open/click rates | Resend built-in |

**Key tracking events:**
- Waitlist form submission (Phase 1)
- "Book Now" click (Phase 2)
- Fresha booking completion
- Package selection (which packages are most popular)

---

## 7. CONTENT REQUIREMENTS

**Photography needed BEFORE website launch:**
- Venue photography (lounge, treatment rooms, collection room exterior view only — no clinical detail)
- Product/service photography (massage hands, nail polish, brow treatment)
- Brand photography (minimal, premium, pregnancy-safe aesthetic)
- Stock photography approved: Unsplash, Getty (search: "pregnancy wellness", "pregnancy spa", "prenatal massage")

**Photography brief:**
- Colour palette: warm whites, sage green, terracotta accents (see docs/brand-guide.md)
- Tone: calm, premium, maternal — not clinical
- Models: visibly pregnant women (24–32 weeks), diverse ethnicities
- Format: landscape for hero, square for social repurposing

**Budget for professional photography shoot:** A$800–1,500 (1 half-day shoot at venue during fit-out phase 2 when venue looks premium)

---

## 8. TECHNICAL REQUIREMENTS

| Requirement | Specification |
|---|---|
| Mobile-responsive | Yes — primary usage is mobile (pregnant women searching on phones) |
| Page speed | Target < 3 seconds on 4G mobile (Google Core Web Vitals) |
| SSL certificate | Yes — required for form data collection |
| Booking widget | Fresha widget embedded on /book page |
| Privacy Policy | Required page before waitlist launch |
| Contact form | Yes — general enquiries, routed to Imara email |
| Email integration | Resend connected to waitlist form (automatic confirmation email) |
| Domain email | [email]@gttcenterperth.com.au for professional appearance |

---

## 9. ACCEPTANCE CRITERIA

Phase 1 (Week 7) is DONE when:
- [ ] Landing page live at gttcenterperth.com.au
- [ ] Waitlist form functional and collecting submissions to Fresha/Resend
- [ ] Privacy Policy page live and linked from form
- [ ] Automatic confirmation email sends on form submission
- [ ] Instagram account bio links to landing page
- [ ] Page loads in < 3 seconds on mobile

Phase 2 (Week 16) is DONE when:
- [ ] All pages in site map are live
- [ ] Fresha booking widget functional on /book page
- [ ] GTT booking constraint logic working (Option A) OR manual workaround documented and receptionist trained (Option B)
- [ ] All 10 SEO content pages published
- [ ] Google Business Profile live and verified
- [ ] Google Analytics and Search Console connected
- [ ] "Book Now" CTA links to correct booking flow

---

*Owner: Poppy (Marketing agent) + assigned developer*  
*Review: Grace (Operations), Jade (CX), Ivy (Booking)*
