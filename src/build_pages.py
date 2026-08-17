import _shell as S
AR = S.AR
PX = "https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg?auto=compress&cs=tinysrgb&w=%s&h=%s&fit=crop"
def px(i, w=900, h=560): return PX % (i, i, w, h)

def hero(h1, sub, ctas, img, alt):
    return f"""<header class="phero">
  <div class="w phero-in">
    <div>
      <h1 class="r">{h1}</h1>
      <p class="psub r">{sub}</p>
      <div class="pcta r">{ctas}</div>
    </div>
    <div class="phero-shot r"><img src="{img}" alt="{alt}" fetchpriority="high" width="1400" height="1050" onerror="this.remove()"></div>
  </div>
</header>
"""

def faq_block(items, gid):
    return "".join(
        f'        <div class="fi">\n          <button class="fq-q" aria-expanded="false">{q}<span class="fic"></span></button>\n'
        f'          <div class="fq-a"><p>{a}</p></div>\n        </div>\n' for q, a in items)

def bc(name, path):
    return ('{"@type":"BreadcrumbList","@id":"https://apolaki.ai%s#bc","itemListElement":['
            '{"@type":"ListItem","position":1,"name":"Home","item":"https://apolaki.ai/"},'
            '{"@type":"ListItem","position":2,"name":"%s","item":"https://apolaki.ai%s"}]}' % (path, name, path))

# ============================== ABOUT ==============================
JOURNEY = [
    ("The beginning", "April 2025", "Three of us met through the Asian Institute of Management's Master in Innovation and Business programme.", False),
    ("The idea", "June 2025", "We went looking at carbon markets and clean energy. CarbonConnect was born.", False),
    ("The validation", "July 2025", "We stopped guessing and went and asked. Dozens of conversations confirmed the same thing: going solar in the Philippines is confusing, and nobody trusts the quotes.", False),
    ("The prototype", "September 2025", "First working prototype. Rough, but it read a bill and produced a number.", False),
    ("The evolution", "January to March 2026", "CarbonConnect became Apolaki, and we were selected for the UNLEASH Prototyping Programme.", False),
    ("The first installation", "March 2026", "We onboarded our first verified installer partner and completed our first solar installation. The idea stopped being an idea.", False),
    ("The soft launch", "April to July 2026", "Soft launched the platform, expanded what it could do, and put up our website and Facebook page.", False),
    ("Demo day", "29 August 2026", "Presenting Apolaki at the AIM MIB Demo Day.", True),
]

VALUES = [
    ('<path d="M12 2v6M12 16v6M2 12h6M16 12h6"/><circle cx="12" cy="12" r="4"/>', "Clarity",
     "We make a complicated decision simple with clear, honest, practical information."),
    ('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>', "Trust",
     "Transparency, integrity and accountability. We would rather lose a sale than a reputation."),
    ('<path d="M13 2L3 14h8l-1 8 10-12h-8z"/>', "Impact",
     "Every decision should create real value for homeowners, partners, and the wider shift to clean energy."),
]

def build_about():
    tl = "".join(
        f'      <div class="jrnyx{" now" if now else ""} r"><span class="dot"></span>\n'
        f'        <div class="lbl">{lbl}</div><div class="dte">{d}</div><p>{txt}</p>\n      </div>\n'
        for lbl, d, txt, now in JOURNEY)
    vals = "".join(
        f'      <div class="fcard r">\n        <div class="fi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ic}</svg></div>\n'
        f'        <h3>{t}</h3><p>{d}</p>\n      </div>\n' for ic, t, d in VALUES)

    body = hero(
        "We got tired of watching Filipinos <em>guess.</em>",
        "Apolaki is the Philippines' first solar adoption platform. We started it because everyone we spoke to wanted solar and nobody could get a straight answer about it.",
        f'<a href="#journey" class="b b-blue">Our journey {AR}</a><a href="/contact" class="b b-glass">Work with us</a>',
        px(6961123, 1400, 1050), "Solar technicians installing panels under a clear sky") + f"""
<section class="sec-tight">
  <div class="w">
    <div class="statrow r">
      <div class="stat-c"><div class="sv mono"><span data-c="2025" data-d="0">2025</span></div><div class="sl">Founded at the Asian Institute of Management</div></div>
      <div class="stat-c"><div class="sv mono"><span data-c="1" data-d="0">1</span><span class="u">st</span></div><div class="sl">Verified installer partner onboarded, March 2026</div></div>
      <div class="stat-c"><div class="sv mono">UNLEASH</div><div class="sl">Selected for the 2026 Prototyping Programme</div></div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="w">
    <div class="tlg">
      <div>
        <div class="sh r" style="margin-bottom:18px"><h2>Why we started.</h2></div>
        <p class="lede r">Filipino homes pay some of the highest electricity rates in Southeast Asia. Solar obviously makes sense here. Yet every homeowner we met was stuck at the same place: three quotes that did not agree, no way to check who was legitimate, and a phone that would not stop ringing once they asked a single question.</p>
        <p class="lede r" style="margin-top:16px">That is not a technology problem. It is a trust problem. So we built the thing we kept wishing existed: an independent first step that gives you the numbers before anyone gets your number.</p>
      </div>
      <div class="r">
        <div class="bacard good" style="max-width:none">
          <div class="ph"><span class="badge">What we believe</span>
            <img src="{px(11645008)}" alt="Installers fitting solar panels on a rooftop" loading="lazy" width="900" height="560" onerror="this.remove()"></div>
          <div class="bd">
            <h3>Solar energy, made simple</h3>
            <div class="lines">
              <p>Every Filipino deserves a simpler path to clean energy.</p>
              <p>We educate before we persuade, and guide before we sell.</p>
              <p>A future where every Filipino home can power itself.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="journey">
  <div class="w">
    <div class="sh r"><h2>How we got here.</h2><p>From a classroom in Makati to a roof in Metro Manila, in about sixteen months.</p></div>
    <div class="jrny">
{tl}    </div>
  </div>
</section>

<section class="sec tint-b">
  <div class="w">
    <div class="sh r"><h2>What we hold to.</h2></div>
    <div class="feat">
{vals}    </div>
  </div>
</section>

<section class="sec-tight">
  <div class="w">
    <div class="callband r">
      <div>
        <h3>Built by three MIB students, and still building</h3>
        <p>Apolaki is operated by VESS Corp. from Mandaluyong City. If you want to partner, invest, or just ask what we are up to, we answer our own email.</p>
      </div>
      <div class="cb-act"><a href="/contact" class="b b-blue">Get in touch {AR}</a></div>
    </div>
  </div>
</section>

<section class="sec cta">
  <div class="w">
    <h2 class="r">Our journey continues with yours.</h2>
    <p class="r">Start with your electricity bill and find out where you stand.</p>
    <div class="b-row r">
      <a href="https://app.apolaki.ai/assessment" class="b b-blue">See my free estimate {AR}</a>
      <a href="/installers" class="b b-glass">Partner with us</a>
    </div>
  </div>
</section>"""

    org = ('{"@type":"AboutPage","@id":"https://apolaki.ai/about#page","url":"https://apolaki.ai/about",'
           '"name":"About Apolaki","mainEntity":{"@id":"https://apolaki.ai/#org"},"inLanguage":"en-PH"}')
    return S.page(
        title="About Apolaki | The Philippines' First Solar Adoption Platform",
        desc="Apolaki was founded in 2025 by three Asian Institute of Management students who kept meeting Filipinos who wanted solar and could not get a straight answer. Our story, values and journey.",
        path="/about", body=body, schema_nodes=[bc("About", "/about"), org], active="about",
        primary_cta=("/contact", "Get in touch"))

# ============================== BLOG ==============================
POSTS = [
    ("is-solar-worth-it-philippines-2026", "Is solar worth it in the Philippines in 2026?", "Guides",
     "The honest answer depends on your bill, your roof and how long you plan to stay. Here is how to work it out.", 11645008),
    ("magkano-ang-solar-panel-pilipinas", "Magkano ang solar panel sa Pilipinas?", "Tagalog",
     "Ang totoong presyo ng solar system para sa bahay, at kung paano ito nakadepende sa kuryente mo.", 6961091),
    ("how-net-metering-works-philippines", "How net metering actually works", "Net metering",
     "Export your extra solar to the grid and get credits. What qualifies, what you get paid, and the catch.", 38171120),
    ("reading-your-meralco-bill-solar", "How to read your MERALCO bill", "MERALCO",
     "Generation charge, distribution charge, and the one number that decides whether solar makes sense for you.", 29206488),
    ("solar-financing-philippines", "Ways to pay for solar in the Philippines", "Financing",
     "Bank loans, Pag-IBIG, GSIS, rent-to-own and credit card promos, with the real rates on each.", 35454190),
    ("will-solar-work-on-my-roof", "Will solar work on my roof?", "Guides",
     "Roof space, direction, pitch and shade. What makes a roof good for solar, and what rules one out.", 6961088),
    ("solar-and-brownouts-backup", "Will solar keep my lights on during a brownout?", "Guides",
     "On its own, no. Here is why, and what a battery actually adds to the cost.", 11644973),
    ("battery-vs-net-metering-philippines", "Battery or net metering?", "Net metering",
     "Two different ways to deal with the power you do not use during the day. Which one suits your home.", 6961110),
    ("paano-pumili-ng-solar-installer", "Paano pumili ng solar installer", "Tagalog",
     "Ano ang dapat mong hanapin, at ang mga red flag na dapat mong iwasan.", 11645006),
    ("solar-for-small-business-philippines", "Solar for a small business", "Business",
     "Different usage pattern, different sizing, different payback. What changes when it is a business.", 6961215),
    ("solar-myths-philippines-debunked", "Six solar myths, checked", "Guides",
     "Panels do not work when it rains, they need constant cleaning, they damage your roof. Sorting fact from sales talk.", 8853504),
    ("solar-co2-philippines-energy-transition", "What one rooftop actually does for emissions", "Impact",
     "A typical 5 kW home system and its real carbon effect in the Philippine grid.", 35454190),
]

def build_blog():
    feat = POSTS[0]
    rest = POSTS[1:]
    featured = f"""      <div class="post wide r np">
        <div class="thumb"><span class="tag">{feat[2]}</span>
          <img src="{px(feat[4], 900, 700)}" alt="" loading="lazy" onerror="this.remove()"></div>
        <div class="pb">
          <h3 style="font-size:1.34rem">{feat[1]}</h3>
          <p>{feat[3]}</p>
          <span class="rd rd-soon">Guide coming soon</span>
        </div>
      </div>"""
    cards = "".join(
        f'      <div class="post r np">\n'
        f'        <div class="thumb"><span class="tag">{tg}</span>'
        f'<img src="{px(im)}" alt="" loading="lazy" onerror="this.remove()"></div>\n'
        f'        <div class="pb"><h3>{ti}</h3><p>{ex}</p><span class="rd rd-soon">Coming soon</span></div>\n'
        f'      </div>\n' for sl, ti, tg, ex, im in rest)

    body = hero(
        "Solar in the Philippines, <em>explained properly.</em>",
        "No sales talk. Just the numbers, the rules and the trade-offs, written for people deciding whether to spend a few hundred thousand pesos.",
        f'<a href="#all" class="b b-blue">Browse the guides {AR}</a><a href="https://app.apolaki.ai/assessment" class="b b-glass">Get my free estimate</a>',
        px(38171120, 1400, 1050), "Rooftop solar array in bright sunlight") + f"""
<section class="sec" id="all">
  <div class="w">
    <div class="sh r"><h2>Start here.</h2></div>
    <div class="postrow">
{featured}
    </div>
    <div class="posts">
{cards}    </div>
  </div>
</section>

<section class="sec-tight tint">
  <div class="w">
    <div class="callband r">
      <div>
        <h3>Reading is useful. Your own numbers are better.</h3>
        <p>Every guide here is general. Three minutes with your electricity bill gives you the version that applies to your roof.</p>
      </div>
      <div class="cb-act"><a href="https://app.apolaki.ai/assessment" class="b b-blue">See my free estimate {AR}</a></div>
    </div>
  </div>
</section>"""

    blogschema = ('{"@type":"Blog","@id":"https://apolaki.ai/blog#blog","url":"https://apolaki.ai/blog",'
                  '"name":"Apolaki Solar Guides","inLanguage":["en-PH","tl"],'
                  '"publisher":{"@id":"https://apolaki.ai/#org"}}')
    return S.page(
        title="Solar Guides Philippines | Costs, Net Metering, Financing | Apolaki",
        desc="Straight guides to going solar in the Philippines. What it costs, how net metering works, how to read your MERALCO bill, and how to pick an installer. English and Tagalog.",
        path="/blog", body=body, schema_nodes=[bc("Blog", "/blog"), blogschema], active="blog",
        primary_cta=("https://app.apolaki.ai/assessment", "Get started"))

# ============================== FAQS ==============================
FAQ_HOME = [
    ("Is the assessment really free?", "Free forever, and no card is needed. We earn from installer partners who receive consented, bill-verified opportunities, never from selling your contact details."),
    ("How accurate are the numbers?", "They are built on your real electricity bill, satellite analysis of your actual roof, and sunshine data for your location. That puts them well ahead of a generic online calculator. An installer confirms the final design after a site visit."),
    ("How long does it take?", "About three minutes. Enter your city and your monthly bill, or upload a photo of a recent bill for a sharper result."),
    ("Do I need my MERALCO bill?", "It helps but it is not required. You can upload a photo or type the amount in. More bills means better accuracy."),
    ("How much does solar cost?", "Roughly &#8369;50,000 to &#8369;65,000 per kilowatt installed, so a typical 5 kW home system lands between &#8369;250,000 and &#8369;325,000. Equipment tier, roof complexity and battery storage move that range."),
    ("What is the payback period?", "Usually three to five years for a Filipino home. After that the power is close to free for another twenty years or so."),
    ("Will solar power my home during a brownout?", "Not on its own. A normal grid-tied system shuts off during an outage so it cannot send power into lines that linemen are working on. Backup needs a battery and a different kind of inverter."),
    ("Is my data private?", "Yes. Your data is encrypted, kept anonymous, and handled under the Data Privacy Act, RA 10173. You can delete it at any time."),
    ("Will I get spam calls?", "No. Installers cannot contact you directly. Introductions only happen when you approve them."),
]
FAQ_INST = [
    ("What does Apolaki give installers?", "Qualified, consented opportunity profiles rather than raw contact lists. Each one includes bill range, location, system size and how far along the homeowner is."),
    ("How is this different from buying leads?", "Lead lists are sold on volume and sold more than once. Every profile here is bill-backed, consent-driven, and shown to you because the homeowner chose you."),
    ("Do homeowners contact us directly?", "Connections stay mediated. Homeowners remain anonymous until they consent to an introduction."),
    ("What does it cost installers?", "We are still finalising the commercial model and are piloting per-lead fees, subscriptions and success-based pricing with our first partners. There is no listing fee during the pilot."),
    ("Can we list our portfolio and services?", "Yes. Partners get a profile with portfolio, certifications, warranty terms and service areas, and can bid on matching opportunities."),
    ("How do you vet installers?", "We confirm SEC or DTI registration against public records, check that a licensed electrical practitioner is on record, and review completed projects including net metering approvals."),
    ("How do I join?", "Submit your company details, then we run verification and agree pilot terms. You can also book an onboarding call and we will walk you through it."),
]
FAQ_GEN = [
    ("What is Apolaki?", "A digital solar readiness and partner-matching platform for Philippine homes and small businesses, built at the Asian Institute of Management and operated by VESS Corp."),
    ("What data sources do you use?", "Satellite rooftop analysis and location-specific solar irradiance data, anchored to your actual electricity bill."),
    ("What is net metering?", "It lets you export surplus solar to the grid in exchange for bill credits. Under RA 9513 systems up to 100 kW qualify, which covers every home installation."),
    ("Where is Apolaki available?", "Across the Philippines, with data and assumptions tuned locally. We are based in Mandaluyong City, Metro Manila."),
    ("Is there a mobile app?", "The web app is live now. Native iOS and Android apps are in development."),
    ("Who built Apolaki?", "Three students from the Master in Innovation and Business programme at the Asian Institute of Management, operating as VESS Corp."),
]

def build_faqs():
    def grp(title, items):
        return f'    <div class="fgroup r">\n      <h3>{title}</h3>\n      <div class="fq">\n{faq_block(items,"")}      </div>\n    </div>\n'
    body = hero(
        "Questions, <em>answered straight.</em>",
        "The things homeowners, installers and partners ask us most. If yours is not here, email us and we will add it.",
        f'<a href="/contact" class="b b-blue">Ask us something {AR}</a><a href="https://app.apolaki.ai/assessment" class="b b-glass">Get my free estimate</a>',
        px(9875422, 1400, 1050), "Solar technician installing panels on a house roof") + f"""
<section class="sec">
  <div class="w" style="max-width:880px">
{grp("For homeowners", FAQ_HOME)}{grp("For installers", FAQ_INST)}{grp("About Apolaki", FAQ_GEN)}
  </div>
</section>

<section class="sec-tight tint">
  <div class="w">
    <div class="callband r">
      <div><h3>Still stuck on something?</h3><p>Email us and a real person answers. We are a small team, so it is usually one of the founders.</p></div>
      <div class="cb-act"><a href="mailto:hello@apolaki.ai" class="b b-blue">hello@apolaki.ai {AR}</a></div>
    </div>
  </div>
</section>"""
    allf = FAQ_HOME + FAQ_INST + FAQ_GEN
    fs = ('{"@type":"FAQPage","@id":"https://apolaki.ai/faqs#faq","mainEntity":['
          + ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                     % (q.replace('"', ''), a.replace('"', '').replace('&#8369;', 'PHP '))
                     for q, a in allf) + "]}")
    return S.page(
        title="Frequently Asked Questions | Apolaki Solar Philippines",
        desc="Answers on free solar assessments, accuracy, costs, payback, net metering, privacy, and how Apolaki connects Philippine homeowners with verified installers.",
        path="/faqs", body=body, schema_nodes=[bc("FAQ", "/faqs"), fs], active="faq",
        primary_cta=("/contact", "Contact us"))

# ============================== CONTACT ==============================
def build_contact():
    body = hero(
        "Talk to <em>an actual person.</em>",
        "We are a small team in Mandaluyong City. Email, Viber or the form below all reach us, usually within a working day.",
        f'<a href="#form" class="b b-blue">Send a message {AR}</a><a href="mailto:hello@apolaki.ai" class="b b-glass">hello@apolaki.ai</a>',
        px(6961123, 1400, 1050), "Solar technicians working together on a rooftop") + f"""
<section class="sec-tight">
  <div class="w">
    <div class="ccards">
      <div class="ccard r">
        <div class="ci"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/></svg></div>
        <h3>Email</h3><p>Best for anything detailed. A founder usually answers.</p>
        <a href="mailto:hello@apolaki.ai">hello@apolaki.ai</a>
      </div>
      <div class="ccard r">
        <div class="ci"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.4 8.4 0 01-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.4 8.4 0 013.8-.9h.5a8.5 8.5 0 018 8z"/></svg></div>
        <h3>Viber</h3><p>Quick questions, quick answers. Mondays to Saturdays.</p>
        <a href="viber://chat?number=%2B639178161707">+63 917 816 1707</a>
      </div>
      <div class="ccard r">
        <div class="ci"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4.5 8-11a8 8 0 10-16 0c0 6.5 8 11 8 11z"/><circle cx="12" cy="11" r="3"/></svg></div>
        <h3>Where we are</h3><p>Operated by VESS Corp. Built at the Asian Institute of Management.</p>
        <a href="/about">Mandaluyong City, Metro Manila</a>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="form">
  <div class="w">
    <div class="tlg">
      <div>
        <div class="sh r" style="margin-bottom:20px"><h2>Send us a message.</h2><p>Tell us who you are and we will point you at the right person.</p></div>
        <form class="cform r" data-contact>
          <div class="rowx">
            <div><label for="cn">Your name</label><input id="cn" required placeholder="Juan dela Cruz"></div>
            <div><label for="ce">Email</label><input id="ce" type="email" required placeholder="you@email.com"></div>
          </div>
          <div><label for="ct">I am a</label>
            <select id="ct">
              <option>Homeowner looking at solar</option>
              <option>Solar installer</option>
              <option>Financing partner or lender</option>
              <option>Press or something else</option>
            </select>
          </div>
          <div><label for="cm">Message</label><textarea id="cm" required placeholder="What can we help with?"></textarea></div>
          <button type="submit" class="b b-blue">Send message {AR}</button>
        </form>
        <div class="cform-ok r">Thanks. We have got it and will reply within a working day.</div>
      </div>
      <div class="r">
        <div class="callband" style="grid-template-columns:1fr">
          <div>
            <h3>Rather just talk?</h3>
            <p>Book a free twenty minute call. Homeowners can walk through their bill with us. Installers and lenders can go straight to onboarding.</p>
            <div class="cb-act" style="margin-top:20px">
              <a href="/contact?type=call" class="b b-blue">Book a discovery call {AR}</a>
            </div>
          </div>
        </div>
        <div class="bacard good r" style="margin-top:18px;max-width:none">
          <div class="ph"><span class="badge">Partner with us</span>
            <img src="{px(11645006)}" alt="Solar technician carrying equipment across a rooftop" loading="lazy" width="900" height="560" onerror="this.remove()"></div>
          <div class="bd">
            <h3>Installers and lenders</h3>
            <div class="lines">
              <p><a href="/installers" style="color:var(--blue);font-weight:600">Become a trusted installer</a></p>
              <p><a href="/financing-partners" style="color:var(--blue);font-weight:600">Fund solar as a financing partner</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""
    cp = ('{"@type":"ContactPage","@id":"https://apolaki.ai/contact#page","url":"https://apolaki.ai/contact",'
          '"name":"Contact Apolaki","mainEntity":{"@id":"https://apolaki.ai/#org"},"inLanguage":"en-PH"}')
    return S.page(
        title="Contact Apolaki | Solar Philippines",
        desc="Get in touch with Apolaki. Email hello@apolaki.ai, message us on Viber, or book a free discovery call. Based in Mandaluyong City, Metro Manila.",
        path="/contact", body=body, schema_nodes=[bc("Contact", "/contact"), cp], active="contact",
        primary_cta=("mailto:hello@apolaki.ai", "Email us"))

if __name__ == "__main__":
    for fn, fx in [("about.html", build_about), ("blog.html", build_blog),
                   ("faqs.html", build_faqs), ("contact.html", build_contact)]:
        h = fx().replace('href="/assets/', 'href="assets/').replace('src="/assets/', 'src="assets/')
        open(fn, "w").write(h)
        print(fn, len(h) // 1024, "KB")
