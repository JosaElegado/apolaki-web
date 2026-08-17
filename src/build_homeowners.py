import _shell as S

CK, XX, AR = S.CK, S.XX, S.AR

def li_x(t): return f'      <li>{XX}<span>{t}</span></li>'
def li_c(t): return f'      <li>{CK}<span>{t}</span></li>'

WITHOUT = [
    "Three companies, three very different prices",
    "No one shows the math behind the quote",
    "Your number gets passed around",
    "No way to check if they are licensed",
    "Net metering explained after it is installed",
]
WITH = [
    "One free assessment, one honest set of numbers",
    "Every assumption on screen, yours to change",
    "Your number stays private until you say so",
    "Registration and licence checked before you meet",
    "Net metering explained before you commit",
]

FEATURES = [
    ('<path d="M3 10l9-7 9 7v10a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/>',
     "A system that fits your roof", "Not the biggest anyone can sell you. The one your roof and budget can carry."),
    ('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6M9 15h6M9 11h3"/>',
     "Savings from your bill", "Your real usage and your real rate. Not a national average."),
    ('<path d="M12 1v22"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>',
     "One price, all in", "Panels, inverter, mounting, labour, permits. Nothing appears later."),
    ('<path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/>',
     "When it pays for itself", "Your payback in years, with every assumption visible."),
    ('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
     "Installers already checked", "Registration confirmed, licensed electrician on record, real projects."),
    ('<rect x="4" y="10.5" width="16" height="10.5" rx="2.4"/><path d="M8 10.5V7a4 4 0 018 0v3.5"/>',
     "Your number stays yours", "They see a city and a bill range. Nothing more, until you decide."),
]

SOON = [
    ('<path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/>', "Net metering help",
     "We handle the MERALCO paperwork with your installer."),
    ('<path d="M12 1v22"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>', "In-house financing",
     "Pay monthly through Apolaki instead of hunting for a bank."),
]

FAQ = [
    ("Is the assessment really free?",
     "Yes, and it stays free. No card, no trial, no catch. We earn from installer partners who get to meet homeowners who are genuinely ready, never from selling your contact details."),
    ("What if I do not have my bill handy?",
     "Type in roughly what you pay each month and your city. That is enough for a first estimate. Upload a bill later and the numbers get sharper."),
    ("Do I have to buy anything?",
     "No. Plenty of people run the numbers, find solar does not suit their roof yet, and leave. That is a useful answer too, and it costs nothing."),
    ("How long does the whole thing take?",
     "The assessment is about three minutes. After that it is your pace. Most homeowners take a few weeks to compare installers and sort financing."),
]

PANES = """
            <div class="pane on" data-p="1">
              <div class="pane-t">Add your bill</div>
              <div class="pane-s">Photo, PDF or type it in</div>
              <div class="pane-body">
                <div class="scan">
                  <div class="lz"></div>
                  <div class="bill"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
                  <span>Reading statement</span>
                </div>
                <div class="chips"><span class="chip b">MERALCO</span><span class="chip">712 kWh/mo</span><span class="chip">&#8369;11.80/kWh</span></div>
                <div class="outp"><div><div class="k">Read in</div></div><div class="v">2.4s</div></div>
              </div>
            </div>

            <div class="pane" data-p="2">
              <div class="pane-t">Your roof</div>
              <div class="pane-s">Quezon City &middot; 14.63&deg;N</div>
              <div class="pane-body">
                <div class="roofmap">
                  <svg width="100%" height="100%" viewBox="0 0 260 196" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
                    <rect width="260" height="196" fill="#2A3340"/>
                    <g fill="#39434F"><rect x="4" y="6" width="66" height="52" rx="3"/><rect x="80" y="14" width="52" height="40" rx="3"/>
                    <rect x="196" y="4" width="60" height="48" rx="3"/><rect x="6" y="140" width="72" height="52" rx="3"/>
                    <rect x="182" y="146" width="72" height="46" rx="3"/><rect x="146" y="72" width="40" height="34" rx="3"/></g>
                    <g stroke="#4A5563" stroke-width="5"><path d="M0 68h260M0 128h260M92 0v196M176 0v196"/></g>
                    <path d="M96 74h74v50H96z" fill="#0E6CBD" fill-opacity=".34" stroke="#F2C94C" stroke-width="2" stroke-dasharray="5 4"/>
                    <g fill="#0E6CBD" fill-opacity=".72">
                      <rect x="101" y="79" width="20" height="17" rx="1.5"/><rect x="124" y="79" width="20" height="17" rx="1.5"/><rect x="147" y="79" width="18" height="17" rx="1.5"/>
                      <rect x="101" y="100" width="20" height="17" rx="1.5"/><rect x="124" y="100" width="20" height="17" rx="1.5"/><rect x="147" y="100" width="18" height="17" rx="1.5"/>
                    </g>
                  </svg>
                </div>
                <div class="chips"><span class="chip b">28 m&sup2; usable</span><span class="chip">South-west</span><span class="chip">5.1 sun hrs</span></div>
                <div class="outp"><div><div class="k">Expected output</div></div><div class="v">6,640 kWh/yr</div></div>
              </div>
            </div>

            <div class="pane" data-p="3">
              <div class="pane-t">Your solar price</div>
              <div class="pane-s">5.2 kWp &middot; 13 panels</div>
              <div class="pane-body">
                <div class="card big">
                  <div class="ck">Installed, all in</div>
                  <div class="cv mono">&#8369;271,000</div>
                  <div class="cs">or &#8369;5,180/mo over 60 months</div>
                </div>
                <div class="row2">
                  <div class="card"><div class="ck">Saves</div><div class="cv mono">&#8369;6,340<span class="u">/mo</span></div></div>
                  <div class="card"><div class="ck">Payback</div><div class="cv mono">4.1<span class="u">yrs</span></div></div>
                </div>
                <div class="cmp">
                  <div class="cr now"><span class="cl">Now</span><span class="tr"><i></i></span><span class="cn">&#8369;8,400</span></div>
                  <div class="cr aft"><span class="cl">After</span><span class="tr"><i></i></span><span class="cn">&#8369;2,060</span></div>
                </div>
                <div class="pbtn">See 4 matched installers
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
                </div>
              </div>
            </div>
"""

STEPS = [
    ("Send your bill", "A photo of your MERALCO, VECO or Davao Light statement. That is the whole first step."),
    ("We measure your roof", "Satellite imagery and local sunshine data give us the size your home actually needs."),
    ("Meet your installers", "Your price, your savings, your financing, and installers near you we have already checked."),
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
        f'        <article class="hstep{" on" if i==1 else ""}" data-i="{i}">\n'
        f'          <div class="k"><i></i>Step {i:02d}</div>\n'
        f'          <h3>{t}</h3><p>{d}</p>\n        </article>\n' for i, (t, d) in enumerate(STEPS, 1))
    faq = "".join(
        f'        <div class="fi">\n          <button class="fq-q" aria-expanded="false">{q}<span class="fic"></span></button>\n'
        f'          <div class="fq-a"><p>{a}</p></div>\n        </div>\n' for q, a in FAQ)

    body = f"""<header class="phero">
  <div class="w phero-in">
    <div>
      <h1 class="r">Know what solar costs for your home <em>before you spend a peso.</em></h1>
      <p class="psub r">Send us your electricity bill. We do the rest.</p>
      <div class="pcta r">
        <a href="https://app.apolaki.ai/assessment" class="b b-blue">Start my free assessment {AR}</a>
        <a href="#how" class="b b-glass">See how it works</a>
      </div>
    </div>
    <div class="phero-shot r">
      <img src="https://images.pexels.com/photos/9875422/pexels-photo-9875422.jpeg?auto=compress&cs=tinysrgb&w=1400&h=1050&fit=crop" alt="Solar technician installing panels on a house roof" fetchpriority="high" width="1400" height="1050" onerror="this.remove()">
    </div>
  </div>
</header>

<section class="sec-tight">
  <div class="w">
    <div class="statrow r">
      <div class="stat-c"><div class="sv mono">&#8369;<span data-c="6340" data-d="0">6,340</span></div><div class="sl">Typical monthly saving on a Metro Manila home</div></div>
      <div class="stat-c"><div class="sv mono"><span data-c="3.9" data-d="1">3.9</span><span class="u">years</span></div><div class="sl">Before a well-sized system pays for itself</div></div>
      <div class="stat-c"><div class="sv mono">&#8369;<span data-c="0" data-d="0">0</span></div><div class="sl">What it costs to find out where you stand</div></div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="w">
    <div class="sh r"><h2>Going solar alone is the expensive way.</h2></div>
    <div class="bafoto">
      <div class="bacard bad r">
        <div class="ph"><span class="badge">On your own</span>
          <img src="https://images.pexels.com/photos/29206488/pexels-photo-29206488.jpeg?auto=compress&cs=tinysrgb&w=900&h=560&fit=crop" alt="Solar panel being fitted on a residential roof" loading="lazy" width="900" height="560" onerror="this.remove()"></div>
        <div class="bd">
          <h3>Three quotes, no way to compare them</h3>
          <div class="lines">
            <p>Nobody shows the math behind the price.</p>
            <p>Your number gets passed around after one enquiry.</p>
            <p>No way to check who is actually licensed.</p>
            <p>Net metering explained after it is on the roof.</p>
          </div>
        </div>
      </div>
      <div class="bacard good r">
        <div class="ph"><span class="badge">With Apolaki</span>
          <img src="https://images.pexels.com/photos/6961091/pexels-photo-6961091.jpeg?auto=compress&cs=tinysrgb&w=900&h=560&fit=crop" alt="Installers fitting solar panels on a sunny rooftop" loading="lazy" width="900" height="560" onerror="this.remove()"></div>
        <div class="bd">
          <h3>One free assessment, one honest set of numbers</h3>
          <div class="lines">
            <p>Every assumption on screen, and yours to change.</p>
            <p>Your number stays private until you say so.</p>
            <p>Registration and licence checked before you meet.</p>
            <p>Net metering explained before you commit.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="how">
  <div class="w">
    <div class="sh r"><h2>Three minutes, start to finish.</h2></div>
    <div class="jsteps">
      <article class="jstep r"><div class="jid">01</div><div>
        <h3>Send your bill</h3>
        <p>A photo of your MERALCO, VECO or Davao Light statement. That is the whole first step.</p>
      </div></article>
      <article class="jstep r"><div class="jid">02</div><div>
        <h3>We measure your roof</h3>
        <p>Satellite imagery and local sunshine data give us the size your home actually needs.</p>
      </div></article>
      <article class="jstep r"><div class="jid">03</div><div>
        <h3>Meet your installers</h3>
        <p>Your price, your savings, your financing, and installers near you we have already checked.</p>
      </div></article>
    </div>
  </div>
</section>

<section class="sec tint-b">
  <div class="w">
    <div class="sh r"><h2>What is in your free report.</h2></div>
    <div class="feat">
{fs}    </div>

    <div class="soon r">
      <div class="soon-h"><h3>Coming soon</h3><span class="soon-badge">In development</span></div>
      <p>Join the waitlist and we will tell you the day they go live.</p>
      <div class="soon-grid" style="grid-template-columns:repeat(2,1fr);margin-top:18px">
{sc}      </div>
      <form class="wait" data-wait>
        <input type="email" required placeholder="you@email.com" aria-label="Email address">
        <button type="submit" class="b b-blue">Join the waitlist</button>
      </form>
      <p class="wait-ok">Thanks. You are on the list.</p>
    </div>
  </div>
</section>

<section class="sec-tight tint">
  <div class="w">
    <div class="sh c r"><h2>Questions homeowners ask.</h2></div>
    <div class="fq r">
{faq}    </div>
    <div class="center" style="margin-top:40px"><a href="/faqs" class="tl">See all questions {AR}</a></div>
  </div>
</section>

<section class="sec cta">
  <div class="cta-media">
    <img src="https://images.pexels.com/photos/11644973/pexels-photo-11644973.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1000&fit=crop"
         alt="Team installing solar panels on a rooftop" loading="lazy" width="1800" height="1000" onerror="this.remove()">
  </div>
  <div class="w">
    <h2 class="r">Switch to solar now.</h2>
    <p class="r">Grab your latest bill. Three minutes from now you will know.</p>
    <div class="b-row r">
      <a href="https://app.apolaki.ai/assessment" class="b b-blue">Start my free assessment {AR}</a>
      <a href="/installers" class="b b-glass">I am an installer</a>
    </div>
    <p class="fine r">It is free. No card, and your number stays with you.</p>
  </div>
</section>"""

    faq_schema = ('{"@type":"FAQPage","@id":"https://apolaki.ai/homeowners#faq","mainEntity":['
                  + ",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
                             for q, a in FAQ) + "]}")
    bc = ('{"@type":"BreadcrumbList","@id":"https://apolaki.ai/homeowners#bc","itemListElement":['
          '{"@type":"ListItem","position":1,"name":"Home","item":"https://apolaki.ai/"},'
          '{"@type":"ListItem","position":2,"name":"Solar Adopters","item":"https://apolaki.ai/homeowners"}]}')
    svc = ('{"@type":"Service","@id":"https://apolaki.ai/homeowners#svc","name":"Free Solar Assessment for Homeowners",'
           '"serviceType":"Solar system sizing, savings estimate and trusted installer matching",'
           '"provider":{"@id":"https://apolaki.ai/#org"},"areaServed":{"@type":"Country","name":"Philippines"},'
           '"audience":{"@type":"Audience","audienceType":"Homeowners in the Philippines"},'
           '"offers":{"@type":"Offer","price":"0","priceCurrency":"PHP","availability":"https://schema.org/InStock",'
           '"description":"Free bill-based solar assessment for Philippine homeowners"}}')

    html = S.page(
        title="Solar for Your Home | Free Assessment and Trusted Installers | Apolaki",
        desc="Find out what solar costs for your home in the Philippines. Send your electricity bill and get your system size, monthly savings, financing options and trusted installers near you. Free, no sales calls.",
        path="/homeowners", body=body, schema_nodes=[bc, svc, faq_schema], active="homeowners",
        primary_cta=("https://app.apolaki.ai/assessment", "Get started"),
    )
    open("homeowners.html", "w").write(html)
    print("homeowners.html", len(html) // 1024, "KB")

if __name__ == "__main__":
    build()
