import _shell as S

CK, XX, AR = S.CK, S.XX, S.AR

def li_x(t): return f'      <li>{XX}<span>{t}</span></li>'
def li_c(t): return f'      <li>{CK}<span>{t}</span></li>'

WITHOUT = [
    "Boosted posts, and hope the right person sees them",
    "Leads who know nothing and were only curious",
    "Site visits burned on homes that never proceed",
    "Competing on price against corner-cutters",
    "They have already been called by six others",
]
WITH = [
    "They arrive having run their own numbers",
    "Size, roof and budget on screen before you quote",
    "Every introduction is one they asked for",
    "You compete on your work, not your ad spend",
    "You are the only installer they approved",
]

STEPS = [
    ("Apply and get verified",
     "Registration, your licensed electrician, and a few finished projects. We check them against public records before you go live.",
     ["SEC or DTI registration", "Licensed electrician on record", "Completed project history"]),
    ("Get matched with homeowners who are ready",
     "When a homeowner in your area approves an introduction, the whole brief comes with it.",
     ["You pick your service areas", "Full brief, not a phone number", "Only consented introductions"]),
    ("Quote, install and get paid",
     "Fewer wasted site visits, fewer cold quotes. Good work moves you up the list.",
     ["Fewer wasted site visits", "Ranked on finished work", "Feedback builds your profile"]),
]

FEATURES = [
    ('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6M9 15h6M9 11h3"/>',
     "Customers who did the homework",
     "System size, budget and savings, already worked out from a real bill."),
    ('<path d="M12 1v22"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>',
     "You know they can pay",
     "Bill range and financing status on the brief, before you price the job."),
    ('<path d="M18.4 5.6a9 9 0 11-12.8 0"/><path d="M2 2l20 20"/>',
     "Far less spent on marketing",
     "No boosted posts, no lead brokers, no one cold-calling all afternoon."),
    ('<path d="M16 3h5v5"/><path d="M8 3H3v5"/><path d="M21 3l-7 7"/><path d="M3 3l7 7"/><rect x="7" y="13" width="10" height="8" rx="2"/>',
     "Get your supplies through us",
     "Panels, inverters and mounting at platform pricing. No single-distributor lock-in."),
    ('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
     "Ranked on your work, not your budget",
     "Your place on the shortlist comes from finished projects. It cannot be bought."),
    ('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0116 0"/>',
     "A profile homeowners actually read",
     "Portfolio, certifications and service areas, inside the decision rather than on Facebook."),
]

SOON = [
    ('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/>', "Quote generator",
     "Build a branded quote from the homeowner's brief in a couple of minutes."),
    ('<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>', "Project tracker",
     "Every job from deposit to handover, with the homeowner watching the same timeline."),
    ('<circle cx="9" cy="7" r="3"/><path d="M2 21a7 7 0 0114 0"/><path d="M16 3.1a4 4 0 010 7.8M22 21a7 7 0 00-5-6.7"/>', "Team workspace",
     "Assign crews, share site photos and keep your paperwork in one place."),
    ('<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>', "Payment gateway",
     "Take deposits and staged payments without chasing bank transfers."),
]

FAQ = [
    ("What does it cost to join?",
     "We are still finalising the commercial model. Right now we are piloting per-lead fees, a monthly subscription and success-based pricing with our first partners, and those partners help us decide which one is fair. Talk to us and we will be straight about where that stands."),
    ("How do you verify installers?",
     "We confirm your SEC or DTI registration against public records, check that you have a licensed electrical practitioner on record, and review completed projects including net metering approvals where they apply. Verification happens before you receive a single homeowner."),
    ("Can I choose which areas I serve?",
     "Yes. You set your service areas and the system sizes you want to take on. You will only be shown to homeowners who match."),
    ("Do I get the homeowner's contact details?",
     "Only after they approve an introduction. Before that you see the brief without the name, number or exact address. It sounds restrictive, but it is the reason homeowners trust the platform enough to be there in the first place."),
]

def build():
    fs = "".join(
        f'      <div class="fcard r">\n'
        f'        <div class="fi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ic}</svg></div>\n'
        f'        <h3>{t}</h3><p>{d}</p>\n      </div>\n' for ic, t, d in FEATURES)
    sc = "".join(
        f'        <div class="scard">\n'
        f'          <svg class="si" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ic}</svg>\n'
        f'          <b>{t}</b><span>{d}</span>\n        </div>\n' for ic, t, d in SOON)
    steps = "".join(
        f'      <article class="vstep r">\n        <div class="vn">{i:02d}</div>\n        <div>\n'
        f'          <h3>{t}</h3><p>{d}</p>\n'
        f'          <div class="vmeta">{"".join(f"<span>{m}</span>" for m in meta)}</div>\n'
        f'        </div>\n      </article>\n' for i, (t, d, meta) in enumerate(STEPS, 1))
    faq = "".join(
        f'        <div class="fi">\n          <button class="fq-q" aria-expanded="false">{q}<span class="fic"></span></button>\n'
        f'          <div class="fq-a"><p>{a}</p></div>\n        </div>\n' for q, a in FAQ)

    body = f"""<header class="phero">
  <div class="w phero-in">
    <div>
      <h1 class="r">Spend less time chasing leads. <em>More time on roofs.</em></h1>
      <p class="psub r">Join the Apolaki trusted installer pool and meet homeowners who already know their system size, their savings and their budget.</p>
      <div class="pcta r">
        <a href="/contact?type=installer" class="b b-blue">Become a trusted installer {AR}</a>
        <a href="#join" class="b b-glass">How to join</a>
      </div>
    </div>
    <div class="phero-shot r">
      <img src="https://images.pexels.com/photos/6961123/pexels-photo-6961123.jpeg?auto=compress&cs=tinysrgb&w=1400&h=1050&fit=crop" alt="Team of solar technicians installing panels under a clear sky" fetchpriority="high" width="1400" height="1050" onerror="this.remove()">
    </div>
  </div>
</header>

<section class="sec-tight">
  <div class="w">
    <div class="statrow r">
      <div class="stat-c"><div class="sv mono">100<span class="u">%</span></div><div class="sl">Of introductions are ones the homeowner asked for</div></div>
      <div class="stat-c"><div class="sv mono">&#8369;<span data-c="0" data-d="0">0</span></div><div class="sl">Listing fee during the pilot</div></div>
      <div class="stat-c"><div class="sv mono"><span data-c="3" data-d="0">3</span><span class="u">checks</span></div><div class="sl">Registration, licence and project history, before you go live</div></div>
    </div>
  </div>
</section>

<section class="sec-tight">
  <div class="w">
    <div class="split-2">
      <div class="split-txt r">
        <h2>This is what lands with you.</h2>
        <p class="lede" style="margin-top:18px">No name, no number, no guesswork. Just the job, so you can decide in seconds whether it is worth your van and your afternoon.</p>
      </div>
      <div class="s2-vis r">
        <div class="brief">
          <div class="brief-top"><b>New opportunity</b><span>Quezon City</span></div>
          <div class="brief-body">
            <div class="brief-hero"><b>5.2 kWp</b><span>13 panels &middot; 28 m&sup2;</span></div>
            <div class="brief-rows">
              <div class="brow"><span class="k">Budget range</span><span class="v">&#8369;250k &ndash; &#8369;325k</span></div>
              <div class="brow"><span class="k">Financing</span><span class="v ok">Pre-qualified</span></div>
              <div class="brow"><span class="k">Roof</span><span class="v">Concrete, south-west</span></div>
              <div class="brow"><span class="k">Average bill</span><span class="v">&#8369;8,400/mo</span></div>
              <div class="brow"><span class="k">Wants to start</span><span class="v">Within 30 days</span></div>
            </div>
            <div class="brief-act"><span class="ba1">Accept</span><span class="ba2">Pass</span></div>
            <div class="brief-note">Contact details unlock when you both accept</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="w">
    <div class="sh r"><h2>Getting customers should not cost this much.</h2></div>
    <div class="bafoto">
      <div class="bacard bad r">
        <div class="ph"><span class="badge">How it works now</span>
          <img src="https://images.pexels.com/photos/8853504/pexels-photo-8853504.jpeg?auto=compress&cs=tinysrgb&w=900&h=560&fit=crop" alt="Technician working alone on a rooftop solar panel" loading="lazy" width="900" height="560" onerror="this.remove()"></div>
        <div class="bd">
          <h3>Paying to be seen, then paying again to qualify</h3>
          <div class="lines">
            <p>Boosted posts, and hope the right person sees them.</p>
            <p>Site visits burned on homes that never proceed.</p>
            <p>Competing on price against corner-cutters.</p>
            <p>They have already been called by six others.</p>
          </div>
        </div>
      </div>
      <div class="bacard good r">
        <div class="ph"><span class="badge">With Apolaki</span>
          <img src="https://images.pexels.com/photos/6961088/pexels-photo-6961088.jpeg?auto=compress&cs=tinysrgb&w=900&h=560&fit=crop" alt="Installation team working together on a large rooftop" loading="lazy" width="900" height="560" onerror="this.remove()"></div>
        <div class="bd">
          <h3>They arrive knowing what they want</h3>
          <div class="lines">
            <p>Size, roof and budget on screen before you quote.</p>
            <p>Every introduction is one they asked for.</p>
            <p>You compete on your work, not your ad spend.</p>
            <p>You are the only installer they approved.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="join">
  <div class="w">
    <div class="sh r"><h2>How to join.</h2></div>
    <div class="jsteps">
      <article class="jstep r"><div class="jid">01</div><div>
        <h3>Apply</h3>
        <p>Send your registration, your licensed electrician, and a few finished projects.</p>
      </div></article>
      <article class="jstep r"><div class="jid">02</div><div>
        <h3>Get verified</h3>
        <p>We check all three against public records. A few days, and the badge means something.</p>
      </div></article>
      <article class="jstep r"><div class="jid">03</div><div>
        <h3>Pick your areas</h3>
        <p>Choose the cities and system sizes you want. You only appear to homeowners who match.</p>
      </div></article>
      <article class="jstep r"><div class="jid">04</div><div>
        <h3>Start quoting</h3>
        <p>Briefs land with size, roof, budget and timeline. Fewer wasted visits, fewer cold quotes.</p>
      </div></article>
    </div>

    <div class="callband r" style="margin-top:clamp(34px,4vw,52px)">
      <div>
        <h3>Book an onboarding call</h3>
        <p>Twenty minutes with our team. We will walk through verification, your service areas and where the commercial terms stand.</p>
      </div>
      <div class="cb-act"><a href="/contact?type=onboarding" class="b b-blue">Book an onboarding call {AR}</a></div>
    </div>
  </div>
</section>

<section class="sec tint-b">
  <div class="w">
    <div class="sh r">
      <h2>What being a trusted installer gets you.</h2>
    </div>
    <div class="feat">
{fs}    </div>

    <div class="soon r">
      <div class="soon-h"><h3>Coming soon: the installer toolkit</h3><span class="soon-badge">In development</span></div>
      <p>Built around how Philippine solar installers actually run a job.</p>
      <div class="soon-grid">
{sc}      </div>
      <form class="wait" data-wait>
        <input type="email" required placeholder="you@company.com" aria-label="Email address">
        <button type="submit" class="b b-blue">Join the waitlist</button>
      </form>
      <p class="wait-ok">Thanks. You are on the list.</p>
    </div>
  </div>
</section>

<section class="sec-tight tint">
  <div class="w">
    <div class="sh c r"><h2>Questions installers ask.</h2></div>
    <div class="fq r">
{faq}    </div>
  </div>
</section>

<section class="sec cta">
  <div class="cta-media">
    <img src="https://images.pexels.com/photos/11644973/pexels-photo-11644973.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1000&fit=crop"
         alt="Team installing solar panels on a rooftop" loading="lazy" width="1800" height="1000" onerror="this.remove()">
  </div>
  <div class="w">
    <h2 class="r">Become a trusted installer.</h2>
    <p class="r">Tell us about your company and we will walk you through verification. Pilot partners help shape the commercial terms.</p>
    <div class="b-row r">
      <a href="/contact?type=installer" class="b b-blue">Become a trusted installer {AR}</a>
      <a href="/contact?type=onboarding" class="b b-glass">Book an onboarding call</a>
    </div>
    <p class="fine r">No listing fee during the pilot.</p>
  </div>
</section>"""

    faq_schema = ('{"@type":"FAQPage","@id":"https://apolaki.ai/installers#faq","mainEntity":['
                  + ",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
                             for q, a in FAQ) + "]}")
    bc = ('{"@type":"BreadcrumbList","@id":"https://apolaki.ai/installers#bc","itemListElement":['
          '{"@type":"ListItem","position":1,"name":"Home","item":"https://apolaki.ai/"},'
          '{"@type":"ListItem","position":2,"name":"Installers","item":"https://apolaki.ai/installers"}]}')
    svc = ('{"@type":"Service","@id":"https://apolaki.ai/installers#svc","name":"Apolaki Trusted Installer Programme",'
           '"serviceType":"Verified installer network and qualified customer matching",'
           '"provider":{"@id":"https://apolaki.ai/#org"},"areaServed":{"@type":"Country","name":"Philippines"},'
           '"audience":{"@type":"Audience","audienceType":"Solar installation companies in the Philippines"}}')

    html = S.page(
        title="Become a Trusted Solar Installer | Apolaki Installer Network Philippines",
        desc="Join the Apolaki trusted installer pool and meet Philippine homeowners who already know their system size, budget and savings. Less spent on marketing, equipment supply, and software built for solar installers.",
        path="/installers",
        body=body,
        schema_nodes=[bc, svc, faq_schema],
        active="installers",
        primary_cta=("/contact?type=installer", "Apply to join"),
    )
    open("installers.html", "w").write(html)
    print("installers.html", len(html) // 1024, "KB")

if __name__ == "__main__":
    build()
