# Apolaki Website

Marketing site for [apolaki.ai](https://apolaki.ai). Built for VESS Corp.

Four pages, one shared stylesheet, no build step and no dependencies.

---

## Preview locally

```bash
git clone <repo-url>
cd apolaki-web
python3 -m http.server 8000
```

Open `http://localhost:8000`. Serving it (rather than double-clicking the files) means the links between pages work the same way they will in production.

---

## Pages

| File | URL | Who it's for |
|---|---|---|
| `index.html` | `/` | Everyone. Trusted installers near you. |
| `homeowners.html` | `/homeowners` | Solar adopters |
| `installers.html` | `/installers` | Solar installation companies |
| `financing-partners.html` | `/financing-partners` | Individual and institutional lenders |

Each page follows the same shape, adapted from the HomePay layout: hero, a before-and-after comparison, numbered steps, a feature grid, what's coming next, FAQ, then a closing CTA.

---

## H1s

| Page | H1 |
|---|---|
| Home | Trusted solar installers near you. |
| Solar adopters | Know what solar costs for your home **before you spend a peso.** |
| Installers | Spend less time chasing leads. **More time on roofs.** |
| Financing | Put your money into **Filipino rooftops.** |

---

## The financing calculator

The interactive model on `/financing-partners` is the most complex piece on the site. It runs a standard amortising loan schedule in the browser:

```
M = P × r / (1 − (1+r)^−n)        r = annual rate / 12
```

**Two modes.** Individual lender (₱25k to ₱5M, 8–16% p.a.) and Institution (₱1M to ₱50M, 7–14% p.a.). The tabs reset the slider ranges and defaults.

**Outputs.** Monthly payment, total interest, interest as a percentage of capital, and the month your capital is fully recovered. Plus a chart of cumulative cash returned against a dashed capital line, with the crossing point marked, a hover tooltip, and the full schedule as a table.

**Worked example.** ₱1,000,000 at 12% over 36 months returns ₱33,214 a month, ₱195,715 total interest, capital back by month 31. Verified against hand calculation.

### The rates behind it

Sliders are bounded by what Philippine lenders actually charge and pay today:

| Source | Rate |
|---|---|
| GSIS Ginhawa Solar Loan | 5.0% p.a., 5 years, up to ₱500k |
| Pag-IBIG Home Improvement | 5.75–6.25% p.a., 5 years, max ₱300k |
| Bank solar lending (BPI, BDO, Security Bank) | ~7.5% p.a. |
| Rent-to-own solar | ~15% effective |
| SeedIn (P2P investor return) | from 7% annualised |
| Vidalia (P2P investor return) | 1–1.5% monthly, ~18% p.a. |
| Blend.PH (P2P investor return) | 6–30% p.a. |

Solar loans through a platform sit between bank secured lending and rent-to-own, which is why the individual slider defaults to 12%.

### One thing worth reading before your CEO does

The page says this plainly, and it matters: **total interest is not the rate times the years.** On a 36-month loan at 12%, total interest is about 19.6% of the original capital, not 36%, because the loan amortises and your money is not all working for the full term. Lenders close that gap by reinvesting each monthly repayment.

Better to have that in your own copy than to have a bank point it out in a meeting.

### Disclaimer

There is a prominent disclaimer under the calculator stating that the figures are illustrative, deduct no losses, fees or taxes, and are not an offer, forecast or promise of return. **Do not remove it.** Publishing modelled investment returns without one is a real regulatory exposure, and the FAQ reinforces it. Replace the assumptions with your actual terms once the structure is registered.

---

## Editing

`assets/css/apolaki.css` is the whole design system, shared by all four pages. Design tokens sit in the `:root` block at the top:

```css
--night:  #0A2247   /* dark sections, from brand navy */
--blue:   #0E6CBD   /* brand primary, all actions */
--gold:   #F2C94C   /* accent, used sparingly */
--ink:    #0A1729   /* body text */
```

Change the palette in four lines. Change the typeface in one `@font-face`.

Typeface is **Figtree**, self-hosted and subset to the glyphs in use (11KB), loaded once and cached across all four pages.

---

## SEO

Every page has canonical, `lang="en-PH"`, geo tags, Open Graph and Twitter cards, one H1, correct heading order, alt text on every image, and lazy loading below the fold.

**Structured data.** Every page carries `Organization`. Sub-pages add `BreadcrumbList`, a page-specific `Service`, and `FAQPage`. All FAQ answers in the markup match the visible copy word for word, which Google requires.

Run each URL through the [Rich Results Test](https://search.google.com/test/rich-results) after deploying.

---

## Before production

| # | Item | Where |
|---|---|---|
| 1 | Replace the three testimonial placeholders | `index.html`, search `TESTIMONIAL` |
| 2 | Swap stock photos for our own installation shots | `<img>` tags on all pages, Pexels URLs |
| 3 | Stand up `app.apolaki.ai` and redirect the Firebase URL | every CTA |
| 4 | Create the Facebook and LinkedIn pages | footer and JSON-LD `sameAs` |
| 5 | Build `/terms` | linked in the footer |
| 6 | Confirm the financing figures with counsel | `/financing-partners` |
| 7 | Set up extensionless URLs on the host | `/homeowners` not `/homeowners.html` |

### On the photos

All photos come from one shoot by a Vietnamese photographer on Pexels, free for commercial use with no attribution required. They show a Southeast Asian crew, which is closer than the Western stock we started with, but they are **not Filipino**. There is effectively no stock photography of Filipino solar crews.

Photographing one of your own installations remains the highest-value change available on this site.

### Extensionless URLs

Internal links point at `/homeowners`, not `/homeowners.html`. Most static hosts handle this automatically. On GitHub Pages, rename the files into folders (`homeowners/index.html`) or keep the `.html` links and update them. Netlify and Cloudflare Pages do it out of the box.

---

© 2026 Apolaki · VESS Corp. · Mandaluyong City, Metro Manila
