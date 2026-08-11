# Landing Page QA Notes

## What was tested
- Visual: desktop (1440x900) and mobile (375px, real viewport) rendering, above-the-fold and full-page.
- Responsive: mobile-first CSS reviewed; a real horizontal-overflow bug was found and fixed (see below).
- Accessibility: label/input `for`/`id` associations verified (all 5 waitlist form fields + checkbox correctly
  paired), `aria-label` on the wordmark link, `aria-hidden` on the decorative rule, skip-link present,
  `:focus-visible` styles defined globally, colour contrast computed against WCAG 2.1 AA (see
  `../brand/BRAND-SYSTEM.md` section 4 for the full ratio table and the corrected CTA colour pairing).
- Content: grepped the final HTML for testimonial/review/rating/award/partnership/accreditation/statistic
  language — none found. No fake claims, no invented credentials, no unsupported regulatory claims.

## A methodology finding worth recording
Chrome's `--headless --screenshot --window-size=W,H` CLI flag on this machine controls the OUTPUT IMAGE
dimensions but does NOT reliably control the actual CSS layout viewport used to render the page — the page
was consistently laid out at roughly 490-505px regardless of the requested window size, then the screenshot
canvas cropped that wider layout down to the requested pixel dimensions. This produced a convincing false
positive: text appeared "cut off" at the right edge in a way that looked exactly like a real responsive CSS
bug, when in fact the page was never actually rendered at the intended narrow width.

This was only caught by injecting a diagnostic script into a copy of the page that reported
`document.documentElement.clientWidth` directly, which revealed the mismatch (requested 375px, actual
~489-504px, constant regardless of the requested value).

**Fix**: switched to `npx playwright screenshot --channel=chrome --viewport-size=W,H`, which uses Playwright's
own viewport/emulation control (via CDP) against the same installed system Chrome, and does set the real CSS
viewport. Re-verified at a genuine 375px viewport — no overflow, header/wordmark/CTA all fit, all copy wraps
correctly, full-page 375px-wide capture (`qa-mobile-fullpage.png`) shows no horizontal scroll anywhere on the
page.

A real CSS fix was also applied on top of this (`styles.css` `.site-header__inner`, `.wordmark`,
`.wordmark-text`, `.site-header .btn--small`) to make the header row shrink and truncate gracefully rather
than relying on an already-wide viewport — this was the correct fix regardless of the measurement bug, since
the original flex row had no shrink/wrap handling at all. A defensive `overflow-x: hidden` was also added to
`html, body` as a safety net.

**Takeaway for future QA on this repo**: do not trust `chrome --headless --screenshot --window-size=...` alone
for responsive/viewport testing on this machine. Use `npx playwright screenshot --channel=chrome
--viewport-size=W,H` instead, and where possible verify with a `clientWidth`-reporting diagnostic rather than
assuming the requested window size was honoured.

## Evidence kept
- `qa-mobile-viewport.png` — 375x900, above the fold, real viewport.
- `qa-mobile-fullpage.png` — 375px wide, full page, confirms no horizontal overflow anywhere.
- `qa-desktop-viewport.png` — 1440x900, above the fold.

## Still recommended before public launch
- Real device testing (an actual phone, not just emulation) — one genuine gap tooling can't close.
- A screen-reader pass (VoiceOver/NVDA) — not performed in this session; the semantic/ARIA groundwork is in
  place (labels, skip-link, landmarks) but a live screen-reader run is the only way to confirm the experience
  end to end.
