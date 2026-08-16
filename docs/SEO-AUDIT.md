# Apolaki.ai — SEO Audit & Roast

**Date:** 16 August 2026 · **Scope:** apolaki.ai (37 URLs), apolaki-478302.web.app, competitive landscape

---

## Verdict in one paragraph

The site is *well written and badly built*. The copy is honest, the Tagalog instinct is genuinely smart, and the information architecture is better than most Philippine solar sites. But it has zero structured data, a self-inflicted duplicate-URL problem across every page, thin hub pages competing against 3,000-word rivals, no named installers on a site whose entire pitch is "verified installers," and it appears nowhere in search. You built a brochure and called it a marketplace. Fix the ten Tier-0 items and you go from invisible to competitive in a quarter.

---

## THE ROAST

### 1. You are not in the index
`site:apolaki.ai` returns nothing. 37 URLs, all with `lastmod: 2026-07-06`, and no visible presence. Every other problem below is downstream of this one. Search Console first, everything else second.

### 2. The `.html` civil war
- Sitemap says: `https://apolaki.ai/about.html`
- Your navigation links to: `https://apolaki.ai/about`
- Canonical on the page says: `.../about.html`

Every internal link on your site points at a URL that declares itself non-canonical. That's 37 duplicate pairs Google has to reconcile, and 37 opportunities to split link equity. **Pick extensionless. 301 the `.html` versions. Update the sitemap.**

### 3. Zero structured data. On any page.
No `Organization`, no `WebSite`, no `LocalBusiness`, no `FAQPage`, no `Article`, no `BreadcrumbList`, no `HowTo`.

You have a **23-question FAQ page** with no `FAQPage` markup. You have **16 articles** with no `Article` schema, no author entity, no `datePublished`. In 2026 — with AI Overviews and LLM retrieval deciding who gets cited — schema is how a machine decides you're a real entity worth quoting. This is the single highest-ROI fix on the list and it's a weekend of work.

### 4. Your installer pages contain no installers
`/solar-installer-philippines` is ~700 words explaining what "trusted" means. Not one named company. Your eight city pages — "Solar installers in Makati," "Solar installers in Cebu" — name zero installers in Makati or Cebu.

Someone searching "solar installer Philippines" wants a list. You gave them a manifesto. Meanwhile Solaren, PHILERGY, UNISOLAR and pinas.solar all publish "Top 10 Solar Companies Philippines" and own that SERP.

Harsher point: your entire differentiation is *"verified installers, no pay-to-rank."* You display zero verified installers. The claim is unfalsifiable, which means it's unbelievable — to Google and to a homeowner about to spend ₱250,000.

### 5. Your money pages are stubs
`/net-metering-philippines` — **~450–500 words.**

The page beating you (pinas.solar) has **~3,000 words**, three comparison tables, a working ROI calculator, separate MERALCO / VECO / DLPC / MORE breakdowns, interconnection fee ranges (₱7,000–12,000), a Meralco-vs-VECO timeline table, a named author with a profile page, explicit ERC and DOE citations, and a visible "Updated April 10, 2026."

You are not outranking that with 450 words and no sources.

### 6. Keyword cannibalization you built on purpose
- `/solar-financing-philippines` **and** `/blog/solar-financing-philippines`
- `/net-metering-philippines` **and** `/blog/how-net-metering-works-philippines` **and** `/blog/ano-ang-net-metering`
- `/solar-assessment-philippines` **and** `/blog/how-apolaki-assessment-works`

Same intent, same keyword, two or three URLs. You're competing against yourself and splitting the signal three ways.

### 7. Zero external citations
You reference NASA POWER and Google Solar in prose but link to neither. No links to DOE, ERC, RA 9513, or MERALCO's rate archive anywhere on the site. For a financial-decision topic, that's an E-E-A-T failure. You're asking for trust while showing none of your work.

### 8. Your social links go to facebook.com and linkedin.com
Not your pages. *The homepages.* Also means no LinkedIn company page — so no entity corroboration, no brand knowledge panel, no third-party signal that VESS Corp. exists.

### 9. Fake app store buttons pointing at a Firebase URL
"App Store — Soon" and "Google Play — Soon" both link to `apolaki-478302.web.app`. Two failures:
1. Non-functional store badges read as vaporware.
2. Your **entire product** lives on a URL that looks like a leaked internal project ID. Every sign-up leaves your brand domain and lands somewhere that pattern-matches to phishing.

That SPA is also indexable, has `<title>Apolaki</title>`, no canonical, and is client-rendered — so it's a thin, JS-only page competing for your own brand name.

**Move it to `app.apolaki.ai`, `noindex` it, today.** DNS record plus twenty minutes.

### 10. No local SEO infrastructure at all
You target 8 cities. You have: no Google Business Profile, no `LocalBusiness` schema, no street address (just "Mandaluyong City"), no city-level NAP, no maps. For local-intent queries this is table stakes.

### 11. Tagalog content with no language markup
Five Tagalog articles — the smartest, least contested content decision on the site. But no `lang="tl"`, no `hreflang`. Google may read them as low-quality English. Free fix, meaningful upside.

### 12. Every page has the same `lastmod`
All 37 URLs: `2026-07-06`. That reads as batch-published and abandoned. Your content is rate-sensitive (MERALCO ₱14.83/kWh) — it needs visible "Last updated" dates and actual updates, or it decays into a liability.

### 13. Your brand SERP is buried under a volcano
"Apolaki" is a Wikipedia-notable caldera that went viral as fake news, plus a mythology figure heavily tagged on DeviantArt/TikTok/Behance. You are not winning that name unqualified. Standardize on **"Apolaki Solar"** as the searchable brand token and build entity signals (Wikidata, LinkedIn, Crunchbase, consistent NAP).

### 14. Your best asset is behind a login on another domain
The bill-backed assessment is the whole product — and it's gated, off-domain, and un-indexable. Competitors put a free, ungated ROI calculator directly on the page that ranks. That's what earns dwell time and links.

**Strong opinion:** ungate a lightweight calculator on `apolaki.ai` itself. Bill in → system size, savings, payback out. No email required. *Then* offer the full readiness report for sign-up. You're currently optimizing for lead capture so hard that you never get traffic to capture.

---

## THE PLAN

### Tier 0 — this week (~1–2 days of dev)

| # | Action | Why |
|---|---|---|
| 1 | Set up Google Search Console + Bing Webmaster Tools, submit sitemap, request indexing, enable IndexNow | You can't fix what you can't see |
| 2 | 301 all `.html` → extensionless; fix canonicals; regenerate sitemap | Ends the duplicate-URL split |
| 3 | Add `Organization` + `WebSite` JSON-LD sitewide | Entity foundation |
| 4 | Add `FAQPage` JSON-LD to `/faqs` and every page with a Q&A block | FAQ rich results — free SERP real estate |
| 5 | Add `Article` + `Person` (real author) + `datePublished`/`dateModified` to all 16 posts | E-E-A-T + article rich results |
| 6 | Add `BreadcrumbList` + `Service`/`LocalBusiness` to the 8 city pages | Local relevance signals |
| 7 | Fix or remove the LinkedIn/Facebook links; create a real LinkedIn company page | Trust + entity corroboration |
| 8 | Remove the fake App Store / Google Play badges | Trust |
| 9 | Move app to `app.apolaki.ai`; add `noindex` to the SPA | Brand integrity + stop self-competition |
| 10 | `lang="tl"` + `hreflang` on Tagalog posts | Language targeting |

### Tier 1 — weeks 2–4

- **Ship an ungated calculator** at `/solar-calculator-philippines`. Highest-leverage single page you can build. Also add `/meralco-bill-calculator`.
- **Rebuild the 4 hub pages to 2,000+ words:** net metering, financing, MERALCO savings, assessment. Include utility-by-utility tables (MERALCO, VECO, DLPC, MORE, BENECO), permit timelines, fee ranges, requirement checklists.
- **Publish the installer directory.** Even 15 named companies with real profiles. This is simultaneously your product, your SEO moat, and your credibility. Nothing else on this list matters as much strategically.
- **Fix cannibalization:** consolidate each duplicate pair — hub page becomes the ranking target, blog post 301s into it or gets rewritten to a genuinely different angle.
- **Add real author bylines and bios.** You have four founders including a mechanical engineer doing installations. That's exactly the first-hand experience Google's E-E-A-T guidelines reward. Use their names.
- **Cite sources:** DOE net-metering guidebook, ERC rate orders, MERALCO rate archive, RA 9513, NASA POWER.
- **Add visible "Last updated"** and set a monthly refresh cadence on rate-dependent pages.

### Tier 2 — months 2–3

- **Expand city pages 8 → 35**, but only with genuinely unique local data per page: utility + current rate, irradiance, typical roof construction, LGU permit office, common neighborhoods. Thin duplicates will hurt you. Priority additions: Manila, Parañaque, Las Piñas, Muntinlupa, Marikina, Antipolo, Bacoor, Dasmariñas, Sta. Rosa, Calamba, Bulacan, Pampanga/Angeles, Iloilo, Bacolod, CDO, Batangas.
- **Own the MERALCO bill cluster** — the gap nobody's working. Competitors all fight over bottom-funnel "solar panel price." Nobody owns "why is my MERALCO bill so high," "how to read MERALCO bill," "MERALCO rate today," "MERALCO bill estimator." Enormous volume, and your product literally reads bills. This is your unfair advantage and it's sitting unclaimed.
- **Scale Tagalog 5 → 25 posts.** Near-zero competition, real search volume, and it's on-brand.
- **Digital PR:** publish a quarterly **"Philippine Rooftop Solar Payback Index"** — original data, payback by city and utility. Journalists cite data, not opinions. Target BusinessWorld, Inquirer Business, Rappler, PhilStar. Also pursue the AIM `.edu` link — you're an AIM venture and you're not using it.

### Tier 3 — the moves nobody at your stage is making

1. **Optimize for AI citation, not just clicks.** "Is solar worth it in the Philippines" increasingly gets answered inside AI Overviews, ChatGPT and Perplexity. Win by being *quotable*: one clear declarative answer sentence per section, tables with explicit units, every number sourced, full schema coverage. Add an `llms.txt` at root.
2. **Build `/methodology` as the canonical machine-readable source** for Philippine solar payback math — assumptions, irradiance sources, performance ratio, degradation curve, rate escalation. Make it the page every LLM and every journalist cites when they need PH solar math. That's an authority asset competitors can't copy without admitting where it came from.
3. **Turn installers into a backlink engine.** Give every partner a profile page on apolaki.ai with a "Verified by Apolaki" badge to embed on their own site. Free, compounding, relevant backlinks — and it doubles as your partner acquisition pitch. Two-sided marketplace flywheel applied to SEO.
4. **"No cold calls" is your most quotable line.** It's a memorable, differentiating claim that LLMs and journalists can repeat verbatim. You have a whole page for it (`/no-cold-calls-solar-marketplace`) that isn't even linked from the homepage. Promote it into main navigation and build the brand around it.

---

## Priority sequence

**Week 1:** Tier 0 — indexation, URLs, schema, trust fixes.
**Weeks 2–4:** Calculator + hub page rebuilds + installer directory.
**Months 2–3:** City expansion, MERALCO cluster, Tagalog scale-up, digital PR.

If you only do three things: **(1) fix the URL/canonical split and get indexed, (2) add full schema coverage, (3) publish real named installers.** Everything else is optimization on top of a site that currently doesn't exist to Google.
