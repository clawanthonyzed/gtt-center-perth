# GTT Design Quality Standard

Status: current as of 2026-08-24. A concise working standard for all future visual output (Dash, Dossier, PDFs, procurement documents, customer-facing materials), not a brand redesign. Verified against `outputs/brand/warm-stone-tokens.css` directly, not guessed: the locked palette is 7 colours (Warm Ivory #FAF6EE, Warm Stone #E8DAC5, Deep Brown #33261E, Earthy Terracotta #A9654E, Muted Olive #5E5F45, Dusty Rose #D9A08C, Warm Brass #9C7A46), Fraunces (serif) + DM Sans (sans) typography, 8px-base spacing scale. Do not substitute, lighten, darken, or add to these values.

## Design Skills Installed This Session

1. **web-design-guidelines** (`vercel-labs/agent-skills`, installed at `.claude/skills/web-design-guidelines/SKILL.md`): fetches Vercel's own current Web Interface Guidelines and audits HTML/CSS against 100+ accessibility/UX/consistency rules, file:line format. Reputable, widely adopted (554.2k installs, 30.2k stars per its own listing), security-scanned Safe/0 alerts (Snyk flagged Medium risk, noted honestly, not a blocker for a markdown-only skill with no code execution).
2. **design-taste-frontend** (`Leonxlnx/taste-skill`, installed at `.agents/skills/design-taste-frontend`, symlinked into `.claude/skills/design-taste-frontend`): a taste-first design judgment skill, sets 3 dials (design variance, motion intensity, visual density) to gate layout/motion decisions against a declared design read, explicitly built to avoid generic "3-column, purple-gradient" AI aesthetics. Community-maintained (not an Anthropic/Vercel official repo), security-scanned Safe/0 alerts/Low risk. Chosen over installing multiple overlapping "taste" variants found in the search (e.g. other design-system-generation skills) since this one is purpose-built for judgment, not for generating a new design system from scratch, which this venture does not need (the palette/typography are already locked).
3. **"Awesome Design"**: re-confirmed 2026-08-24, resolved to a category of curated reference-list repositories (e.g. `awesome-claude-skills`), not a single installable skill or plugin. Not installed, since installing a meta-list would be redundant with the 3 skills in this section; this is documented as a conclusion, not a gap.
4. **Image-to-Code, now installed 2026-08-24:** `uxKero/anydesign`, installed at `.agents/skills/anydesign`, symlinked into `.claude/skills/anydesign`. Analyses an image, URL, or Figma file and produces a structured `design.md` (plain Markdown + W3C DTCG JSON token system, component inventory, reconstruction notes); every inference carries an explicit confidence marker and treats inventing a token as worse than reporting "not enough information," a genuinely complementary discipline to this venture's own "do not invent" governance principle. Security-scanned Safe/0 Socket alerts/Med Snyk risk (same risk band as `web-design-guidelines`, not a new concern). Complements rather than overlaps the 2 skills above: `web-design-guidelines` audits existing code against external standards, `design-taste-frontend` supplies judgment for new builds, `anydesign` reverse-engineers an existing visual reference into a usable spec, 3 distinct functions, no redundancy.
5. **Playwright**: genuinely verified working in this environment via Node/npx, not Python. `npx playwright --version` returned 1.62.1; Chromium browser binaries were already present at `C:\Users\azed9\AppData\Local\ms-playwright\`. A real functional test was run: launched Chromium via `playwright-core`, loaded `outputs/gtt-dash/index.html` from disk, retrieved its real page title ("GTT Center Perth: Dash (Prototype)"), captured zero console errors, and produced a real 149KB screenshot. **This corrects a standing assumption carried through every prior GTT checkpoint this session** ("Playwright not available"), which was based only on `python -c "import playwright"` failing; the Node/npx path was never actually tested until now.

## Design Quality Standard

**Typography hierarchy:** Fraunces serif for headings/display (restrained weight, e.g. 300-600), DM Sans for body/UI text. Never more than 3 heading levels visible on one screen/page. Body copy stays sans-serif; serif is reserved for headings, pull quotes, and cover titles.

**Spacing:** the existing 8px-base scale (8/16/24/40/64/96) only. Generous whitespace over dense information packing; the current Dash already does this reasonably well (verified via the screenshot test below).

**Colour usage:** Warm Ivory/Warm Stone dominate (85-90% of any surface, per the token file's own comment). Deep Brown for primary text, never pure black. Earthy Terracotta as an accent (labels, focus states, tags), never a large fill (contrast-checked and rejected as a CTA fill in the token file itself, for good reason, do not reintroduce it as one). Muted Olive for secondary structural accents (callout panels). Dusty Rose and Warm Brass are restrained, single-moment accents only, never a dominant block.

**Cards/tables/dashboards:** use cards for genuinely distinct metrics, not as a default container for everything; a full grid of uniform white cards (the current Dash's own dominant pattern) reads closer to a generic SaaS dashboard than an "executive console" and is the single biggest visual-quality opportunity identified this round (see audit below). Tables should prioritise scan-ability (clear column headers, restrained borders, no zebra-striping unless genuinely needed for row-tracking in a very long table).

**Charts/data visualisation:** use the locked palette only; avoid default charting-library colour schemes (blues/greens/reds that clash with the earth-tone palette).

**Document covers/page hierarchy (Dossier, PDFs):** a genuine cover treatment (title, subtitle, date, not just the first chapter starting cold) signals a "professionally produced" document rather than a repository export; this is a real, identified refinement opportunity (see audit below).

**What NOT to do:** no gradients as a default choice. No decorative icons where a text label would communicate hierarchy more clearly. No default SaaS-dashboard aesthetics (heavy card shadows, rounded pill badges everywhere, generic sans-only typography). No sacrificing table/data readability for a "luxury" treatment. Do not touch a design that already works (per the audit below, several existing surfaces are already good and should not be changed for change's sake).

**Accessibility:** contrast-check every new colour pairing against the locked palette (the token file's own CTA-button reasoning, Deep Brown fill + Warm Ivory text at 13.56:1, is the model to follow); the Vercel web-design-guidelines skill should be run against any new HTML output before it is considered final.

**Responsive/interaction:** desktop and mobile viewport checks for anything new; no motion/animation beyond restrained, purposeful transitions (consistent with the taste-skill's "motion intensity" dial set low, matching the calm/premium brand tone, not a high-energy consumer-app feel).

## Visual Audit (This Round), Classified

**A. Already premium and appropriate:** the wordmark/logo system, the 7-colour palette itself, the typography choice (Fraunces + DM Sans), the CTA-button contrast solution. None of these need touching.

**B. Good but needs refinement:** the GTT Dash. Verified via a real Playwright screenshot this session (not assumed): warm ivory background, deep brown header, restrained terracotta/olive tags, clean card grid, generous whitespace, zero console errors. This is a solid, on-brand foundation, not a failure. The refinement opportunity: the dashboard section is currently a uniform grid of white metric cards, a pattern common to generic developer/SaaS dashboards; a genuine "executive console" feel would differentiate primary metrics (larger, less boxed) from secondary ones (smaller, grouped), rather than giving every figure equal card-weight. **P1, not P0**: it is on-brand and functional as-is, this is a refinement, not damage control.

**C. Clearly below the intended brand standard:** none identified this round. No surface was found actively contradicting the locked palette, using an off-brand font, or presenting a generic AI aesthetic.

**D. Functional/internal, intentionally utilitarian:** the procurement documents, the Master Dossier's underlying markdown source, and all `docs/architecture/*.md` working documents. These are correctly plain-markdown internal artifacts, not customer-facing; no design work is warranted on them, and none was done.

**Master Dossier:** not re-audited visually this round (its HTML rendering was not re-screenshotted, given time constraints); the one identified opportunity carried over from general knowledge of its structure is a genuine cover page, listed as **P2** (optional polish, not urgent).

**Prioritised list:**
- **P0 (materially damaging):** none found. No change was automatically implemented, correctly, since nothing met this bar.
- **P1 (worthwhile refinement):** Dash dashboard-card hierarchy (differentiate primary vs secondary metrics visually, not just by grid position).
- **P2 (optional polish):** a genuine Dossier cover page.

**No change was made to any visual output this round.** Per instruction, only P0 changes were to be auto-implemented, and none were found; P1/P2 are recommendations for a future, deliberate design pass, not implemented here to avoid unbounded scope creep on a task explicitly about installing capability and establishing a standard, not executing a redesign.

## Workflow Rules for Future Design-Related Work

**For HTML/UI:** render via Playwright (now verified working, Node/npx path, not Python) at both desktop (1280x800) and mobile (375x667) viewports; capture console errors (the Dash currently has zero); check for layout overflow, contrast, and interactive-state visibility; run the `web-design-guidelines` skill against the HTML before considering it final.

**For documents:** check page hierarchy, whitespace, table readability, and visual consistency against this standard; a genuine cover/section-break treatment for anything customer-facing.

**For the Dash specifically:** every new metric/view must earn its place (decision-usefulness over completeness), avoid adding another uniform card to an already-dense grid without considering whether it should be a differentiated primary metric instead, maintain the palette exactly as locked.

**Judgment principle (from the installed Taste skill):** declare a one-line design read before making a layout/motion decision, and set variance/motion/density deliberately low for this brand (calm, restrained, premium), not high (energetic, trend-forward).

## Design References (External Inspiration, Not Adopted)

**Merse Wellness (WA-based recovery/bathhouse wellness chain, Osborne Park + Claremont + other Perth-metro/Brisbane/Gold Coast locations), flagged by Anthony as design inspiration from Instagram, 2026-08-28.** Researched via the public website (mersewellness.com.au) and search results; the specific Instagram account Anthony referenced (@merseosbornepark) could not be directly rendered by this session's tools, so this assessment rests on the public website/press material, a reasonable proxy for brand aesthetic but not a substitute for the actual feed, flagged honestly rather than claimed as verified.

**What Merse actually is:** a multi-location recovery/thermal-therapy chain (magnesium bathhouse, cold plunge, hot rock and infrared saunas, cryotherapy, hyperbaric chambers, salt rooms, compression therapy, LED light therapy), founded by the Fitness Cartel team, scaling toward 100 Australian locations by 2033. Its sites (900sqm Claremont flagship, ~750sqm newer sites) are a genuinely different scale and service category to GTT Center Perth: a bathhouse/recovery chain, not a beauty/massage/hair/nails day-spa paired with a clinical pathology test.

**Aesthetic, as far as verifiable:** premium, minimalist, neutral/earth-tone palette ("eggshell and soft earth tones"), Mediterranean-inspired interior language, clean contemporary typography, spacious high-quality photography emphasising calm and cleanliness, icon-based service navigation, generous whitespace, an "escape from daily life" positioning.

**Where this validates GTT's own locked direction:** the neutral/earth-tone palette family, premium-not-ornate minimalism, calm/escape positioning, and photography-led trust-building are directionally consistent with GTT's own locked Warm Ivory/Warm Stone/Earthy Terracotta palette and the calm/premium/restrained standard above. Useful validation that this general aesthetic direction reads as credible in the current WA wellness market, not a reason to change anything.

**Where it genuinely diverges (contrast, not a flaw either way):** Merse is a large-footprint, multi-site recovery/bathhouse chain, more resort/spa-hotel in material language (Mediterranean stone, water features), against GTT's single boutique venue pairing a clinical test with beauty/massage/hair services. Merse has no pregnancy-specific or clinical-integration positioning at all, the exact thing that differentiates GTT. Its icon-grid service menu and named "signature zone" branding (e.g. a "Rejuvenate Lounge") are layout/naming patterns, not colour or material decisions, and nothing here is being adopted.

**Concretely worth noting for a future fit-out/visual design pass, not applied now:** (1) icon-based service navigation as a way to present a multi-service menu (massage/beauty/nails/hair) scannably, a layout question this standard doesn't yet address; (2) naming functional zones as an experience-branding device worth considering at the marketing/naming stage for GTT's own Lounge/treatment areas, distinct from the physical fit-out itself. Neither changes the locked palette, typography, or brand strategy; both are noted as options for whoever does the eventual interior design brief once a venue exists.

**Ysee Coiffeur (hair salon, Mount Lawley, Perth WA) and BHO Interiors (Perth commercial interior design firm), flagged by Anthony as further design inspiration, 2026-08-28.** Same research method and same caveat: assessed via public website content (yseecoiffeur.com, bhointeriors.com) and search results, not Instagram directly.

**Genuinely important finding, not obvious from the names alone: Ysee Coiffeur and Merse Wellness Osborne Park were both designed by the same firm, BHO Interiors.** BHO's own portfolio explicitly lists both projects. This means 2 of Anthony's 3 references share a single design author, which explains the aesthetic consistency between them, not a coincidence.

**Ysee Coiffeur, what it actually is:** a premium hair salon in Mount Lawley, Perth (Instagram bio: "PERTH HAIR SALON"), positioned as "where glam meets luxury." Aesthetic: minimalist, monochromatic/neutral tones, clean white space, elegant restrained typography with uppercase emphasis for brand moments, polished professional interior and styling photography. A single boutique hair salon, not a multi-service model.

**BHO Interiors, what it actually is:** a Perth (East Perth-based) boutique commercial interior design and fit-out firm, founded 2009 by Bryan Ho, specialising in hospitality/retail/wellness/commercial fit-outs, not a wellness or salon business itself, as the coordinator's own framing anticipated. Their stated design philosophy is "purpose-driven design," restrained/understated material palettes, sustainability-conscious material selection, and photography that emphasises light, proportion, and how people use a space, rather than a decorative or trend-led aesthetic. Their portfolio includes Merse Wellness Osborne Park, Ysee Coiffeur, a retail flagship (The Furniture Gallery, Joondalup), and The Perth Mint.

**Where Ysee/BHO align with GTT's own locked direction:** both companies' stated design language, restraint, understated premium materials, calm/uncluttered photography, neutral palette, is directionally consistent with GTT's own locked Warm Ivory/Warm Stone/Deep Brown/Earthy Terracotta palette and the "premium, not ornate" standard above. Same conclusion as Merse: this validates the general aesthetic direction as credible in the current WA market, it does not license any change.

**Where they diverge:** Ysee is a monochromatic/neutral palette (Ysee's own described tones lean cooler/greyer than GTT's own warm-toned palette, which is explicitly warm ivory/terracotta/olive/brass, not monochrome), a single-service (hair-only) salon at a much smaller scale than GTT's multi-service model. BHO's portfolio, while demonstrating relevant hospitality/wellness/retail fit-out experience, is a design-firm aesthetic applied across very different client briefs (a bathhouse, a hair salon, a retail flagship, a cultural institution), not a single consistent "look" to copy wholesale.

**Concretely worth noting, not applied now:** BHO Interiors has directly relevant, demonstrated Perth experience designing both a wellness/spa venue (Merse) and a premium hair salon (Ysee), an unusually close match to GTT Center Perth's own hybrid beauty/wellness/hair/clinical model. **This is worth flagging as a genuinely relevant future fit-out/interior-design contact once a venue is secured and that stage of the project begins**, per instruction, not contacted now, and this is not a decision or commitment, simply a factual note that this firm's portfolio is unusually well-matched to this venture's brief.

**Not changed:** as above, no locked palette, typography, or brand-strategy decision is affected by this addition.

## Sourcing

`outputs/brand/warm-stone-tokens.css`, `outputs/brand/BRAND-SYSTEM.md`, `outputs/gtt-dash/index.html`.

## Changelog

**2026-08-28 (Ysee Coiffeur + BHO Interiors design references added, same day):** Anthony flagged 2 further references. Ysee Coiffeur (Mount Lawley hair salon) and BHO Interiors (Perth commercial interior design firm) researched via public website/search results. Genuine finding: BHO Interiors designed both Merse Wellness Osborne Park and Ysee Coiffeur, so 2 of Anthony's 3 references share one design author. Assessed against the locked standard: directionally aligned on restraint/premium-calm positioning, diverges on Ysee's monochromatic (not warm-toned) palette and single-service scale. Flagged BHO Interiors as a genuinely relevant future fit-out contact once a venue exists (not contacted, per instruction). No locked brand decision reopened or changed.

**2026-08-28 (Merse Wellness design reference added):** Anthony flagged Merse Wellness (a WA recovery/bathhouse wellness chain) as design inspiration from Instagram. Researched via public website and search results (Instagram itself not directly renderable, flagged not hidden). Assessed against the locked palette/typography/design standard above: genuinely aligned on neutral/earth-tone premium-calm positioning, genuinely diverges on service category, scale, and pregnancy-specific positioning. No locked brand decision reopened or changed; 2 concrete layout/naming ideas (icon-based service navigation, named functional zones) noted as future reference only, not applied.

**2026-08-24 (created):** Built per direct founder instruction. Installed and verified 2 real design skills plus genuinely tested Playwright (correcting a standing "not available" assumption carried through this entire session), established a concise working design standard, and audited existing outputs, finding no P0 issues and one genuine P1 refinement (Dash card hierarchy). No visual output was changed this round.

**2026-08-24 (follow-up, same day): installed a 3rd design skill, `anydesign` (image-to-code), after inspecting its source repository and running the same security scan used for the first 2 skills.** Re-confirmed "Awesome Design" remains a curated-list category, not installed, no change to that conclusion.
