import _shell as S

CK, XX, AR = S.CK, S.XX, S.AR

def li_x(t): return f'      <li>{XX}<span>{t}</span></li>'
def li_c(t): return f'      <li>{CK}<span>{t}</span></li>'

WITHOUT = [
    "Underwriting against stated income",
    "No idea who installed the equipment",
    "Nothing visible after the money goes out",
    "Every project specified differently",
    "You source and chase borrowers yourself",
]
WITH = [
    "Twelve months of real bills behind every borrower",
    "Only verified installers touch a financed system",
    "Output monitored after the panels go up",
    "The same specs across the whole portfolio",
    "Borrowers arrive already assessed",
]

FEATURES = [
    ('<path d="M3 10l9-7 9 7v10a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M12 22V12"/>',
     "The asset repays the loan",
     "The savings on the borrower's bill are the repayment source. The collateral pays you back."),
    ('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6M9 15h6M9 11h3"/>',
     "Affordability from bills, not claims",
     "Twelve months of real consumption. Not stated income."),
    ('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16"/>',
     "The same specs on every project",
     "Sizing, equipment and standards are consistent, so one loan compares to the next."),
    ('<path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/>',
     "Performance you can check",
     "If a system underperforms, you find out early, not when a repayment is missed."),
    ('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
     "Installed by verified partners",
     "Only checked installers touch a financed system, which protects your collateral."),
    ('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
     "Cash from month one",
     "Principal and interest every month from the first. No waiting for maturity."),
]

STEPS = [
    ("Tell us your mandate",
     "Ticket size, tenor, target return, and any limits on borrower profile or region.",
     ["Individual or institutional", "Your tenor and ticket size", "Your risk appetite"]),
    ("We match you to a loan pool",
     "Your capital sits across many bill-verified loans, not one borrower.",
     ["Bill-verified borrowers", "Spread across many loans", "Regions you choose"]),
    ("Repayments land monthly",
     "Withdraw as it arrives, or roll it into the next cohort.",
     ["Monthly principal and interest", "Withdraw or reinvest", "Performance reporting"]),
]

FAQ = [
    ("Is this an investment offer?",
     "No. The figures on this page are illustrative modelling based on published Philippine lending rates, and nothing here is an offer to sell a security or a promise of return. Our financing structures are being finalised with counsel and will operate under the relevant SEC registration before any capital is accepted."),
    ("What happens if a borrower stops paying?",
     "Some will, and the modelling above does not deduct losses, so treat it as a gross figure. Recovery on solar loans is helped by the fact that the equipment is on the roof and the savings are visible, but no consumer lending book has a zero default rate. We will publish our actual loss assumptions once the pilot has a track record worth quoting."),
    ("Why is the total interest lower than the rate times the years?",
     "Because the loan pays down every month. On a 36 month loan at 12 percent, your money is not all working for 36 months, so total interest lands near 19 percent of the original capital rather than 36 percent. Reinvesting each monthly repayment is how lenders close that gap."),
    ("Who can lend, individuals or institutions only?",
     "Both. Individual lenders come in at smaller tickets through a peer-to-peer structure. Banks, cooperatives, NGOs and family offices come in at portfolio level with their own terms. Use the tabs above to model whichever applies to you."),
]

def build():
    fs = "".join(
        f'      <div class="fcard r">\n'
        f'        <div class="fi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ic}</svg></div>\n'
        f'        <h3>{t}</h3><p>{d}</p>\n      </div>\n' for ic, t, d in FEATURES)
    steps = "".join(
        f'      <article class="vstep r">\n        <div class="vn">{i:02d}</div>\n        <div>\n'
        f'          <h3>{t}</h3><p>{d}</p>\n'
        f'          <div class="vmeta">{"".join(f"<span>{m}</span>" for m in meta)}</div>\n'
        f'        </div>\n      </article>\n' for i, (t, d, meta) in enumerate(STEPS, 1))
    faq = "".join(
        f'        <div class="fi">\n          <button class="fq-q" aria-expanded="false">{q}<span class="fic"></span></button>\n'
        f'          <div class="fq-a"><p>{a}</p></div>\n        </div>\n' for q, a in FAQ)

    xh = S.phero(
        kicker='For financing partners',
        h1='Where to grow your money in 2026: <em>Filipino rooftops.</em>',
        sub='Solar loans backed by a real electricity bill, where the savings that repay the loan are worked out before a single peso goes out.',
        ctas=f'<a href="#model" class="b b-blue">See what you would earn {AR}</a> <a href="/contact?type=call" class="b b-glass">Book a discovery call</a>',
        img='https://images.pexels.com/photos/9875441/pexels-photo-9875441.jpeg?auto=compress&cs=tinysrgb&w=2200&h=830&fit=crop',
        alt='Rooftop solar array in bright sunlight',
        theme='th-white',
        variant='numeric',
        figure='<span data-c="9" data-d="0">9</span><span class="u wide">in 10</span>',
        fignote='Filipinos say they are considering solar at home. Only 24&#37; have done it. Everything between those two numbers is unmet demand waiting on financing.',
        rail=[('<span data-c="9" data-d="0">9</span><span class="u">in 10</span>',
               'Filipinos say they are considering solar at home'),
              ('<span data-c="24" data-d="0">24</span><span class="u">%</span>',
               'Have actually done it. The gap between those two numbers is the market.'),
              ('&#8369;<span data-c="12.5" data-d="1">12.5</span><span class="u">billion</span>',
               'Sitting in the new GSIS solar loan facility alone, waiting on providers who can issue a quote')])
    body = f"""{xh}

<!-- ============ CALCULATOR ============ -->
<section class="sec" id="model">
  <div class="w">
    <div class="sh r">
      <h2>How the cohort model works.</h2>
      <p>We pool verified homeowners into cohorts, each with a real bill behind them, and match the repayment to the saving the system actually produces. Move the sliders to see how a position behaves.</p>
    </div>

    <div class="r" style="margin-top:34px">
      <div class="tabs" role="tablist" aria-label="Lender type">
        <button role="tab" id="tab-p2p" aria-controls="panel-p2p" aria-selected="true">Individual lender</button>
        <button role="tab" id="tab-inst" aria-controls="panel-inst" aria-selected="false">Institution</button>
      </div>
      <p class="dim" id="tabNote" style="font-size:.85rem;margin-top:14px;max-width:none">
        Peer-to-peer lending for individuals. Smaller tickets, spread across many borrowers, monthly repayments.
      </p>
    </div>

    <div class="calc r">
      <div class="calc-in">
        <div class="fld">
          <div class="fld-h"><label for="amt">Amount you put in</label><output id="amtOut">&#8369;1,000,000</output></div>
          <input type="range" id="amt" min="25000" max="5000000" step="25000" value="1000000" aria-describedby="amtScale">
          <div class="fld-scale" id="amtScale"><span id="amtMin">&#8369;25k</span><span id="amtMax">&#8369;5M</span></div>
        </div>

        <div class="fld">
          <div class="fld-h"><label>Term</label><output id="termOut">36 months</output></div>
          <div class="seg" role="group" aria-label="Loan term">
            <button type="button" data-term="24" aria-pressed="false">24</button>
            <button type="button" data-term="36" aria-pressed="true">36</button>
            <button type="button" data-term="48" aria-pressed="false">48</button>
            <button type="button" data-term="60" aria-pressed="false">60</button>
          </div>
        </div>

        <div class="fld">
          <div class="fld-h"><label for="rate">Annual return to you</label><output id="rateOut">12.0%</output></div>
          <input type="range" id="rate" min="8" max="16" step="0.5" value="12" aria-describedby="rateScale">
          <div class="fld-scale" id="rateScale"><span id="rateMin">8%</span><span id="rateMax">16%</span></div>
        </div>
        <aside class="disc-card r"><p><strong>Illustrative only.</strong> Modelled on published Philippine lending rates, assuming every borrower pays on schedule. No losses, fees or taxes deducted. Not an offer, a forecast, or a promise of return. Apolaki is not a licensed financial adviser. Take independent advice before committing capital.</p></aside>
      </div>

      <div class="calc-out">
        <div class="kpi">
          <div class="tile lead">
            <div class="tk">You receive each month</div>
            <div class="tv" id="kMonthly">&#8369;33,214</div>
            <div class="ts" id="kMonthlySub">Principal and interest, from month one</div>
          </div>
          <div class="tile">
            <div class="tk">Total interest earned</div>
            <div class="tv" id="kInterest">&#8369;195,704</div>
            <div class="ts" id="kInterestSub">19.6% of your capital</div>
          </div>
          <div class="tile">
            <div class="tk">Capital back by</div>
            <div class="tv" id="kBreak">Month 31</div>
            <div class="ts">Everything after that is profit</div>
          </div>
        </div>

        <div class="tline">
          <div class="tline-t">When your money comes back</div>
          <div class="tline-s">You are repaid every month, so you are not waiting until the end to see anything.</div>
          <div class="track">
            <div class="fill" id="tFill" style="width:86%"></div>
            <div class="mk start"></div>
            <div class="mk" id="tMk" style="left:86%"></div>
            <div class="mk end"></div>
          </div>
          <div class="tmarks">
            <div><div class="tm">Month 1</div><div class="tb" id="tA">&#8369;33,214</div><div class="tsm">First payout</div></div>
            <div><div class="tm" id="tBm">Month 31</div><div class="tb hl" id="tB">&#8369;1,000,000</div><div class="tsm">Capital back</div></div>
            <div><div class="tm" id="tCm">Month 36</div><div class="tb" id="tC">&#8369;1,195,715</div><div class="tsm">Total returned</div></div>
          </div>
          <details class="tbl">
            <summary>View the month by month schedule</summary>
            <div class="scroll">
              <table id="schedTable"><thead><tr><th>Month</th><th>Payment</th><th>Interest</th><th>Principal</th><th>Cumulative</th></tr></thead><tbody></tbody></table>
            </div>
          </details>
        </div>
      </div>
    </div>

    <div class="feat two r" style="margin-top:clamp(28px,3vw,40px)">
      <div class="fcard photo"><div class="fc-img"><img src="https://images.pexels.com/photos/9875422/pexels-photo-9875422.jpeg?auto=compress&cs=tinysrgb&w=1000&h=560&fit=crop" alt="" loading="lazy" onerror="this.remove()"></div>
        <div class="fi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0116 0"/></svg></div>
        <h3>Individual lenders</h3>
        <p>Peer-to-peer, from smaller tickets, spread across many borrowers so no single household carries your outcome. Monthly repayments you can withdraw or roll forward. Comparable Philippine P2P platforms publish investor returns from about 7% to 18% a year.</p>
        </div>
      
      <div class="fcard photo"><div class="fc-img"><img src="https://images.pexels.com/photos/38171120/pexels-photo-38171120.jpeg?auto=compress&cs=tinysrgb&w=1000&h=560&fit=crop" alt="" loading="lazy" onerror="this.remove()"></div>
        <div class="fi"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="M9 21v-6h6v6"/></svg></div>
        <h3>Banks, cooperatives, NGOs</h3>
        <p>Portfolio-level participation with your own credit criteria, reporting and covenants. For context, Philippine banks currently price secured solar and home improvement lending around 7.5% a year, and government funds such as GSIS and Pag-IBIG sit between 5% and 6.25%.</p>
      </div>
    </div>
  </div>
</section>


{S.bigtype("Nobody in the Philippines offers solar with <em>no money down.</em>", "Every route to a rooftop today runs through a credit card promo or a government salary loan. That leaves out everyone who is neither. It is the widest gap in the market, and it is the one we want to close with you.")}


<section class="sec">
  <div class="w">
    <div class="ctaband r">
      <div>
        <h2>Let us walk you through the numbers.</h2>
        <p>Thirty minutes with our team. Your mandate, your ticket size, the cohorts open now, and exactly how repayment is secured against a real electricity bill.</p>
      </div>
      <div class="ctaband-act">
        <a href="/contact?type=onboarding" class="b b-blue">Book an onboarding call {AR}</a>
        <a href="/contact?type=financing" class="b b-glass">Send us a message</a>
      </div>
    </div>
  </div>
</section>

<section class="sec-tight">
  <div class="w">
    <div class="callband r">
      <div>
        <h3>Book a discovery call</h3>
        <p>Twenty minutes. We will walk through the borrower profile, the underwriting and where the structure stands with counsel.</p>
      </div>
      <div class="cb-act"><a href="/contact?type=call" class="b b-blue">Book a discovery call {AR}</a></div>
    </div>
  </div>
</section>

<section class="sec cta">
  <div class="w">
    <h2 class="r">Let us show you the book.</h2>
    <p class="r">Tell us your mandate and we will walk you through the borrower profile, the underwriting and where the structure stands with counsel.</p>
    <div class="b-row r">
      <a href="/contact?type=financing" class="b b-blue">Start a conversation {AR}</a>
      <a href="mailto:hello@apolaki.ai" class="b b-glass">hello@apolaki.ai</a>
    </div>
    <p class="fine r">Nothing on this page is an offer of securities.</p>
  </div>
</section>"""

    extra_head = ""

    extra_js = """<script>
(function(){
'use strict';
var PRESETS={
  p2p:{min:25000,max:5000000,step:25000,val:1000000,rmin:8,rmax:16,rval:12,
       lo:'\\u20B125k',hi:'\\u20B15M',
       note:'Peer-to-peer lending for individuals. Smaller tickets, spread across many borrowers, monthly repayments.'},
  inst:{min:1000000,max:50000000,step:500000,val:10000000,rmin:7,rmax:14,rval:11,
       lo:'\\u20B11M',hi:'\\u20B150M',
       note:'Portfolio-level participation for banks, cooperatives, NGOs and family offices, with your own credit criteria and reporting.'}
};
var mode='p2p', term=36;
var amt=document.getElementById('amt'), rate=document.getElementById('rate');
var amtOut=document.getElementById('amtOut'), rateOut=document.getElementById('rateOut'), termOut=document.getElementById('termOut');

function peso(n,d){ return '\\u20B1'+Number(n).toLocaleString('en-PH',{minimumFractionDigits:d||0,maximumFractionDigits:d||0}); }
function compact(n){
  if(n>=1e6) return '\\u20B1'+(n/1e6).toFixed(n%1e6===0?0:1)+'M';
  if(n>=1e3) return '\\u20B1'+Math.round(n/1e3)+'k';
  return '\\u20B1'+n;
}

function schedule(P,annual,n){
  var r=annual/100/12;
  var M = r===0 ? P/n : P*r/(1-Math.pow(1+r,-n));
  var rows=[], bal=P, cum=0;
  for(var m=1;m<=n;m++){
    var int_=bal*r, prin=M-int_; bal-=prin; cum+=M;
    rows.push({m:m,pay:M,int:int_,prin:prin,cum:cum});
  }
  return {M:M, rows:rows, total:M*n, interest:M*n-P,
          breakeven: Math.min(n, Math.ceil(P/M))};
}

function fillTable(rows){
  var tb=document.querySelector('#schedTable tbody');
  tb.innerHTML=rows.map(function(p){
    return '<tr><td>'+p.m+'</td><td>'+peso(Math.round(p.pay))+'</td><td>'+peso(Math.round(p.int))+
           '</td><td>'+peso(Math.round(p.prin))+'</td><td>'+peso(Math.round(p.cum))+'</td></tr>';
  }).join('');
}

function update(){
  var P=+amt.value, R=+rate.value;
  var s=schedule(P,R,term);
  amtOut.textContent=peso(P);
  rateOut.textContent=R.toFixed(1)+'%';
  termOut.textContent=term+' months';
  document.getElementById('kMonthly').textContent=peso(Math.round(s.M));
  document.getElementById('kInterest').textContent=peso(Math.round(s.interest));
  document.getElementById('kInterestSub').textContent=(s.interest/P*100).toFixed(1)+'% of your capital over '+term+' months';
  document.getElementById('kBreak').textContent='Month '+s.breakeven;
  var pct=Math.max(6,Math.min(100,s.breakeven/term*100));
  document.getElementById('tFill').style.width=pct+'%';
  document.getElementById('tMk').style.left=pct+'%';
  document.getElementById('tA').textContent=peso(Math.round(s.M));
  document.getElementById('tBm').textContent='Month '+s.breakeven;
  document.getElementById('tB').textContent=peso(P);
  document.getElementById('tCm').textContent='Month '+term;
  document.getElementById('tC').textContent=peso(Math.round(s.total));
  fillTable(s.rows);
}

amt.addEventListener('input',update);
rate.addEventListener('input',update);
document.querySelectorAll('.seg button').forEach(function(b){
  b.addEventListener('click',function(){
    document.querySelectorAll('.seg button').forEach(function(o){o.setAttribute('aria-pressed','false');});
    b.setAttribute('aria-pressed','true'); term=+b.dataset.term; update();
  });
});
function setMode(m){
  mode=m; var p=PRESETS[m];
  amt.min=p.min; amt.max=p.max; amt.step=p.step; amt.value=p.val;
  rate.min=p.rmin; rate.max=p.rmax; rate.value=p.rval;
  document.getElementById('amtMin').textContent=p.lo;
  document.getElementById('amtMax').textContent=p.hi;
  document.getElementById('rateMin').textContent=p.rmin+'%';
  document.getElementById('rateMax').textContent=p.rmax+'%';
  document.getElementById('tabNote').textContent=p.note;
  document.getElementById('tab-p2p').setAttribute('aria-selected',String(m==='p2p'));
  document.getElementById('tab-inst').setAttribute('aria-selected',String(m==='inst'));
  update();
}
document.getElementById('tab-p2p').addEventListener('click',function(){setMode('p2p');});
document.getElementById('tab-inst').addEventListener('click',function(){setMode('inst');});
update();
})();
</script>
"""

    faq_schema = ('{"@type":"FAQPage","@id":"https://apolaki.ai/financing-partners#faq","mainEntity":['
                  + ",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
                             for q, a in FAQ) + "]}")
    bc = ('{"@type":"BreadcrumbList","@id":"https://apolaki.ai/financing-partners#bc","itemListElement":['
          '{"@type":"ListItem","position":1,"name":"Home","item":"https://apolaki.ai/"},'
          '{"@type":"ListItem","position":2,"name":"Financing Partners","item":"https://apolaki.ai/financing-partners"}]}')
    svc = ('{"@type":"Service","@id":"https://apolaki.ai/financing-partners#svc","name":"Solar Lending Partnerships",'
           '"serviceType":"Solar loan origination and lender matching",'
           '"provider":{"@id":"https://apolaki.ai/#org"},"areaServed":{"@type":"Country","name":"Philippines"},'
           '"audience":{"@type":"Audience","audienceType":"Individual lenders, banks, cooperatives and NGOs in the Philippines"}}')

    html = S.page(
        title="Solar Financing Partners Philippines | Lend Against Real Bills | Apolaki",
        desc="Fund rooftop solar in the Philippines. Model returns on a cohort of bill-verified solar loans, for individual peer-to-peer lenders and for banks, cooperatives and NGOs. Illustrative modelling, not an offer.",
        path="/financing-partners",
        body=body,
        schema_nodes=[bc, svc, faq_schema],
        active="financing",
        extra_js=extra_js,
        primary_cta=("/contact?type=financing", "Talk to us"),
    )
    open("financing-partners.html", "w").write(html)
    print("financing-partners.html", len(html) // 1024, "KB")

if __name__ == "__main__":
    build()
