# Apolaki Website

Landing page for [apolaki.ai](https://apolaki.ai). Built for VESS Corp.

**Live preview:** enable GitHub Pages (see below) and this deploys automatically at `https://<org>.github.io/<repo>/`

---

## Quick look

Clone and open `index.html` in any browser. No build step, no dependencies, no install.

```bash
git clone <repo-url>
cd apolaki-web
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

---

## What's here

```
index.html                  the landing page, fully self-contained
assets/
  fonts/figtree.woff2       display + body typeface, subset to 11KB
  fonts/quiapo.woff2        logo typeface, for future use
  img/og-cover.png          social share card, 1200x630
  img/logo-*.png            horizontal lockups, light and dark
  img/logo-512.png          square mark, referenced by schema
docs/
  DESIGN-NOTES.md           copy, typography and colour decisions
  SEO-AUDIT.md              audit of the previous site
  font-specimen.png         typeface comparison
```

Fonts, logos and the favicon are base64-inlined into `index.html`, so the page renders correctly even opened on its own with no `assets/` folder present. The files in `assets/` are for the social card, the schema logo reference, and future pages.

---

## Deploying

Drop `index.html` and `assets/` at your web root. That's the whole deployment.

### GitHub Pages

Settings → Pages → Source: **Deploy from a branch** → Branch: **main**, folder: **/ (root)** → Save.

Live in about a minute at `https://<org>.github.io/<repo>/`. Good enough for the team to review on real devices.

---

## Before this goes to production

| # | Item | Where |
|---|---|---|
| 1 | Replace the three testimonial placeholders | search `TESTIMONIAL` in `index.html` |
| 2 | Swap stock photos for our own installation shots | three `<img>` tags, see Photography below |
| 3 | Stand up `app.apolaki.ai` and redirect the Firebase URL | 9 CTA links |
| 4 | Create the Facebook and LinkedIn pages | footer links and JSON-LD `sameAs` |
| 5 | Build `/financing-partners` and `/terms` | linked from section 3 and the footer |

### Photography

The three photos are hotlinked from Pexels (free commercial licence, no attribution required) and show a Southeast Asian crew. They are placeholders for our own photos.

To swap: save yours under `assets/img/`, then change the `src` on each `<img>`. Every photo already has an SVG fallback and an `onerror` handler behind it, so a missing or broken file degrades to a designed graphic rather than a broken icon.

Original photography of a real Filipino crew on a real Metro Manila roof is the single highest-value change left on this page.

---

## Structure

Five sections:

1. **Hero** — H1, sub, dual CTA, three live-counting stats, full-bleed photo with parallax
2. **How Apolaki works** — three steps with a scroll-driven phone mockup that changes screen as you scroll. Works on mobile too.
3. **Who it's for** — homeowners, installers, financing partners
4. **What homeowners say** — testimonials
5. **Questions we hear a lot** — FAQ accordion, then the closing CTA

Navigation: Solar Adopters, Installers, Financing, Blog, About, FAQ, Contact, plus Log in and Sign up.

---

## SEO

**H1:** Trusted solar installers near you.
**Title:** Trusted Solar Installers Near You | Free Solar Estimate Philippines

"Solar installer near me" is the highest-frequency autocomplete result for that stem in the Philippines. Full keyword reasoning in `docs/DESIGN-NOTES.md` and `docs/SEO-AUDIT.md`.

**Structured data:** Organization, WebSite, WebPage, Service, BreadcrumbList and FAQPage, all in one JSON-LD graph. The six FAQ answers in the markup match the visible copy word for word, which is required for rich results.

Also included: canonical, `lang="en-PH"`, geo tags, full Open Graph and Twitter cards, `max-image-preview:large`, semantic heading order, alt text on every image, lazy loading below the fold.

After deploying to the real domain, run it through the [Rich Results Test](https://search.google.com/test/rich-results).

---

## Browser support and accessibility

- Verified with no horizontal overflow at 360, 390, 480, 600, 768, 900, 1024, 1180, 1440 and 1600px
- Zero console and page errors on desktop and mobile
- `prefers-reduced-motion` respected throughout: parallax, reveals and counters all disabled
- Keyboard accessible, Escape closes the mobile menu, `aria-expanded` on every toggle

---

## Editing notes

Everything lives in `index.html`. Design tokens are CSS custom properties in the `:root` block at the top:

```css
--night:  #0A2247   /* dark sections, from brand navy */
--blue:   #0E6CBD   /* brand primary, all actions */
--gold:   #F2C94C   /* accent, used sparingly */
--ink:    #0A1729   /* body text */
```

Changing the typeface is a single `@font-face` swap. Changing the palette is four lines.

---

© 2026 Apolaki · VESS Corp. · Mandaluyong City, Metro Manila
