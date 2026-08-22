"""Shared shell for all Apolaki pages: head, nav, footer, schema."""

NAV_ITEMS = [
    ("/homeowners", "Solar Adopters", "homeowners"),
    ("/installers", "Installers", "installers"),
    ("/financing-partners", "Financing", "financing"),
    ("/blog", "Blog", "blog"),
    ("/about", "About", "about"),
    ("/faqs", "FAQ", "faq"),
    ("/contact", "Contact us", "contact"),
]

AR = ('<svg class="ar" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
      'stroke-width="2.2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
CHEV = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2"><path d="M9 6l6 6-6 6"/></svg>')
CK = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
      'stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>')
XX = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
      'stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>')



# ---------- section breathers: give the eye a rest between dense sections ----------


FACTS = [
    "&#8369;14.78 per kWh in Metro Manila, August 2026",
    "Electricity up 27&#37; in two years",
    "1,298 kWh a year from every kW installed, measured on 103 Philippine roofs",
    "Net metering approvals now capped at 10 working days",
    "No pre-installation permits for own-use rooftop solar since July 2026",
    "&#8369;12.5 billion in the new GSIS solar loan",
    "100 kW is the net metering ceiling, and no home needs half of it",
]



DEFAULT_CLOSE = {"band": "fade", "split": "fade", "numeric": "none",
                 "immersive": "arc", "compact": "none", "bare": "none"}

GROUND = {"th-sun": "#FCF2D3", "th-sky": "#E8F1F9",
          "th-white": "#FFFFFF", "": "#FCF2D3"}

WAVE_ACCENT = {"th-sun": "#F1C84B", "th-sky": "#0E6BBD",
               "th-white": "#0E6BBD", "": "#F1C84B"}

# One smooth sweep, the same curve used on every Apolaki cover. The accent is
# the identical path nudged upward, so a constant sliver of gold or blue shows
# along the edge instead of two curves crossing each other.
WAVE_PATH = ("M0,86 C300,4 540,140 810,92 C1030,53 1240,0 1440,44 "
             "L1440,160 L0,160 Z")


def wave(top, bottom, accent=None, flip=False):
    """Curve from `top` colour into `bottom` colour, with an optional sliver."""
    acc = ('<path d="%s" fill="%s" transform="translate(0,-19)"/>' % (WAVE_PATH, accent)) if accent else ""
    style = 'background:%s;' % top
    if flip:
        style += 'transform:scaleY(-1);'
    return ('<div class="wave" style="%s" aria-hidden="true">'
            '<svg viewBox="0 0 1440 160" preserveAspectRatio="none">'
            '%s<path d="%s" fill="%s"/>'
            '</svg></div>\n' % (style, acc, WAVE_PATH, bottom))


def stamp(line1, line2=""):
    """The rough SOLAR SIMPLIFIED badge, reused as a section mark."""
    txt = line1 if not line2 else "%s<br>%s" % (line1, line2)
    return ('<span class="stamp" aria-hidden="true">'
            '<svg viewBox="0 0 100 100" fill="none">'
            '<circle cx="50" cy="50" r="45" stroke="currentColor" stroke-width="3.4" '
            'stroke-dasharray="7 4.5" stroke-linecap="round"/>'
            '<circle cx="50" cy="50" r="36" stroke="currentColor" stroke-width="2" opacity=".55"/>'
            '</svg><b>%s</b></span>\n' % txt)


def closer(kind, top="#FCF2D3", bottom="#FFFFFF", accent="#F1C84B"):
    """G5: 'now everyone have this squiggly line.' One device per page, not one for all."""
    if kind == "fade":
        return ('<div class="fadeout" style="background:linear-gradient(180deg,%s,%s)"'
                ' aria-hidden="true"></div>\n' % (top, bottom))
    if kind == "wave":
        return wave(top, bottom, accent)
    if kind == "slant":
        return ('<div class="cut" style="background:%s" aria-hidden="true">'
                '<svg viewBox="0 0 1440 90" preserveAspectRatio="none">'
                '<path d="M0,90 L1440,0 L1440,90 Z" fill="%s"/>'
                '<path d="M0,90 L1440,0" stroke="%s" stroke-width="9"/>'
                '</svg></div>\n' % (top, bottom, accent))
    if kind == "arc":
        return ('<div class="cut arc" style="background:%s" aria-hidden="true">'
                '<svg viewBox="0 0 1440 110" preserveAspectRatio="none">'
                '<path d="M0,110 C420,6 1020,6 1440,110 Z" fill="%s"/>'
                '<path d="M0,110 C420,6 1020,6 1440,110" stroke="%s" stroke-width="8" fill="none"/>'
                '</svg></div>\n' % (top, bottom, accent))
    if kind == "rule":
        return ('<div class="cut rule" style="background:%s" aria-hidden="true">'
                '<span style="background:%s"></span></div>\n' % (top, accent))
    return ""



def gallery(items, cols=3):
    """White ground, photo on top, blue card body. The gallery layout Josa asked
    for twice: value proposition shown as pictures, not icon cards."""
    cards = ""
    for img, alt, title, copy in items:
        cards += ('      <figure class="gcard r">\n'
                  '        <div class="gc-img"><img src="%s" alt="%s" loading="lazy" onerror="this.remove()"></div>\n'
                  '        <figcaption class="gc-b"><h3>%s</h3><p>%s</p></figcaption>\n'
                  '      </figure>\n' % (img, alt, title, copy))
    return '    <div class="gallery g%d">\n%s    </div>\n' % (cols, cards)

def phero(kicker, h1, sub, ctas, img, alt, rail=None, theme="", variant="band",
          figure=None, fignote=None, close=None):
    """One brand, five compositions. Every page shares the kicker rule, the type
    scale, the palette and the rail; the arrangement changes with the page's job.

      band      wide cinematic photo under the headline   (adopters)
      split     headline left, tall blue-washed photo right (installers)
      numeric   no photo, one oversized figure carries it   (financing)
      immersive photo behind the headline, light scrim      (about)
      compact   type only, tight, gets you to the content   (blog, faq, contact)
    """
    rails = ""
    if rail:
        rails = ('  <div class="w">\n    <div class="prail r">\n'
                 + "".join('      <div><div class="pn">%s</div><div class="pl">%s</div></div>\n' % (n, l)
                           for n, l in rail)
                 + '    </div>\n  </div>\n')

    head = ('    <div class="pkick r"><span class="pill">%s</span></div>\n'
            '    <h1 class="r">%s</h1>\n' % (kicker, h1))
    if sub:
        head += '    <p class="psub r">%s</p>\n' % sub
    if ctas:
        head += '    <div class="pcta r">%s</div>\n' % ctas

    sun = '  <div class="sunmark" aria-hidden="true"></div>\n'
    cls = "phero v-%s%s" % (variant, (" " + theme) if theme else "")

    if variant == "split":
        return ('<header class="%s">\n%s  <div class="w psplit">\n'
                '    <div class="psplit-t">\n%s    </div>\n'
                '    <div class="psplit-i r"><img src="%s" alt="%s" fetchpriority="high" onerror="this.remove()"></div>\n'
                '  </div>\n%s</header>\n' % (cls, sun, head, img, alt, rails) + closer(close or DEFAULT_CLOSE.get(variant, "wave"),
                     GROUND.get(theme, "#FCF2D3"), "#FFFFFF",
                     WAVE_ACCENT.get(theme, "#F1C84B")))

    if variant == "numeric":
        fig = ('    <div class="pfig r"><div class="pfig-n">%s</div><div class="pfig-l">%s</div></div>\n'
               % (figure or "", fignote or ""))
        return ('<header class="%s">\n%s  <div class="w pnum">\n'
                '    <div>\n%s    </div>\n%s  </div>\n%s</header>\n'
                % (cls, sun, head, fig, rails) + closer(close or DEFAULT_CLOSE.get(variant, "wave"),
                     GROUND.get(theme, "#FCF2D3"), "#FFFFFF",
                     WAVE_ACCENT.get(theme, "#F1C84B")))

    if variant == "immersive":
        return ('<header class="%s">\n'
                '  <div class="pimm-bg"><img src="%s" alt="%s" fetchpriority="high" onerror="this.remove()"></div>\n'
                '  <div class="w">\n%s  </div>\n%s</header>\n' % (cls, img, alt, head, rails) + closer(close or DEFAULT_CLOSE.get(variant, "wave"),
                     GROUND.get(theme, "#FCF2D3"), "#FFFFFF",
                     WAVE_ACCENT.get(theme, "#F1C84B")))

    if variant == "bare":
        sub_html = ('    <p class="psub r">%s</p>\n' % sub) if sub else ''
        return ('<header class="%s">\n  <div class="w">\n'
                '    <h1 class="r vh-lite">%s</h1>\n%s'
                '  </div>\n</header>\n' % (cls, h1, sub_html))

    if variant == "compact":
        return ('<header class="%s">\n%s  <div class="w">\n%s  </div>\n%s</header>\n'
                % (cls, sun, head, rails) + closer(close or DEFAULT_CLOSE.get(variant, "wave"),
                     GROUND.get(theme, "#FCF2D3"), "#FFFFFF",
                     WAVE_ACCENT.get(theme, "#F1C84B")))

    return ('<header class="%s">\n%s  <div class="w">\n%s  </div>\n'
            '  <div class="pband r"><div class="pband-in">'
            '<img src="%s" alt="%s" fetchpriority="high" onerror="this.remove()">'
            '</div></div>\n%s</header>\n' % (cls, sun, head, img, alt, rails) + closer(close or DEFAULT_CLOSE.get(variant, "wave"),
                     GROUND.get(theme, "#FCF2D3"), "#FFFFFF",
                     WAVE_ACCENT.get(theme, "#F1C84B")))


def ticker(items):
    """Slow marquee of real numbers. Same band on every page, so the site reads
    as one thing. Duplicated once so the loop is seamless."""
    run = "".join('<span>%s</span><i aria-hidden="true"></i>' % t for t in items)
    return ('<section class="tick" aria-label="Philippine solar facts">\n'
            '  <div class="tick-tape"><div class="tick-run">%s</div>'
            '<div class="tick-run" aria-hidden="true">%s</div></div>\n'
            '</section>\n' % (run, run))

def strip(img_url, alt="", caption=None):
    """Full-bleed photo divider. No words unless a short caption is passed."""
    cap = ('\n  <div class="cap"><div class="w"><span>%s</span></div></div>' % caption) if caption else ""
    return ('<section class="strip pxs blued">\n'
            '  <img src="%s" alt="%s" loading="lazy" onerror="this.remove()">%s\n'
            '</section>\n' % (img_url, alt, cap))


def slimband(img_url, alt=""):
    """Thin blued photo rule that breaks up a run of white sections."""
    return ('<div class="slimband" aria-hidden="true">'
            '<img src="%s" alt="%s" loading="lazy" onerror="this.remove()">'
            '</div>\n' % (img_url, alt))


def qband(quote, cite_text, img_url, wide=False):
    """One big quote over a darkened photo."""
    return ('<section class="qband pxs%s">\n'
            '  <img src="%s" alt="" loading="lazy" onerror="this.remove()">\n'
            '  <div class="w">\n'
            '    <span class="qm" aria-hidden="true">&ldquo;</span>\n'
            '    <blockquote class="r">%s</blockquote>\n'
            '    <cite class="r">%s</cite>\n'
            '  </div>\n'
            '</section>\n' % (" wide" if wide else "", img_url, quote, cite_text))


def bigtype(line, sub=None, sky=False):
    """One oversized statement, no photo."""
    subhtml = ('\n      <p class="sub">%s</p>' % sub) if sub else ""
    return ('<section class="bigtype%s">\n'
            '  <div class="w">\n'
            '    <div class="r">\n'
            '      <p>%s</p>%s\n'
            '    </div>\n'
            '  </div>\n'
            '</section>\n' % (" sky" if sky else "", line, subhtml))


def head(title, desc, path, og_title=None, og_desc=None, extra=""):
    ogt = og_title or title
    ogd = og_desc or desc
    return f"""<!DOCTYPE html>
<html lang="en-PH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://apolaki.ai{path}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0A2247">
<meta name="geo.region" content="PH">
<meta name="geo.placename" content="Mandaluyong City, Metro Manila">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Apolaki">
<meta property="og:locale" content="en_PH">
<meta property="og:url" content="https://apolaki.ai{path}">
<meta property="og:title" content="{ogt}">
<meta property="og:description" content="{ogd}">
<meta property="og:image" content="https://apolaki.ai/assets/img/og-cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogt}">
<meta name="twitter:description" content="{ogd}">
<meta name="twitter:image" content="https://apolaki.ai/assets/img/og-cover.png">
<link rel="icon" href="/assets/img/favicon.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/apolaki-sans-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/apolaki-sans-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preconnect" href="https://images.pexels.com" crossorigin>
<link rel="stylesheet" href="/assets/css/apolaki.css">
{extra}
</head>
<body>
"""


def nav(active=None, primary_cta=("https://app.apolaki.ai/signup", "Sign up")):
    links = "".join(
        '      <a href="%s"%s>%s</a>\n' % (href, ' class="active"' if key == active else "", label)
        for href, label, key in NAV_ITEMS
    )
    mob = "".join(
        f'  <a class="ml" href="{href}">{label} {CHEV}</a>\n'
        for href, label, key in NAV_ITEMS
    )
    return f"""<nav class="nv" id="nv">
  <div class="nv-in">
    <a href="/" aria-label="Apolaki home">
      <img class="nv-lg" src="/assets/img/logo-lockup-white.png" alt="Apolaki" width="664" height="160">
      <img class="nv-lg dark" src="/assets/img/logo-lockup.png" alt="Apolaki" width="664" height="160">
    </a>
    <div class="nv-links">
{links}    </div>
    <div class="nv-act">
      <a href="https://app.apolaki.ai/login" class="lgin">Log in</a>
      <a href="{primary_cta[0]}" class="b b-glass b-sm">{primary_cta[1]}</a>
      <button class="bg" id="bg" aria-label="Menu" aria-expanded="false" aria-controls="mm"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>

<div class="mm" id="mm">
{mob}  <div class="mm-b">
    <a href="https://app.apolaki.ai/assessment" class="b b-blue">See my free estimate</a>
    <a href="https://app.apolaki.ai/login" class="b b-line">Log in</a>
  </div>
</div>
"""


FOOTER = """<footer>
  <div class="fbg" aria-hidden="true"><img src="/assets/img/footer-bg.jpg" alt="" loading="lazy" onerror="this.remove()"></div>
  <div class="w">
    <div class="fg">
      <div class="fb">
        <img src="/assets/img/logo-slogan-white.png" alt="Apolaki — a catalyst for solar adoption" width="1906" height="1318">
        <p>A catalyst for solar adoption. We help Filipino homeowners understand solar before they commit, and connect them with installers they can trust.</p>
        <div class="fs">
          <a href="https://www.facebook.com/apolaki.ph" aria-label="Facebook" rel="me noopener"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0022 12z"/></svg></a>
          <a href="https://www.linkedin.com/company/apolaki" aria-label="LinkedIn" rel="me noopener"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 8.98h4v12H3zM10 8.98h3.8v1.64h.06c.53-1 1.83-2.06 3.76-2.06 4.02 0 4.76 2.65 4.76 6.1v6.32h-4v-5.6c0-1.34-.02-3.06-1.86-3.06-1.87 0-2.16 1.46-2.16 2.96v5.7h-4z"/></svg></a>
          <a href="viber://chat?number=%2B639178161707" aria-label="Viber"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.4 8.4 0 01-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.4 8.4 0 013.8-.9h.5a8.5 8.5 0 018 8z"/></svg></a>
          <a href="mailto:hello@apolaki.ai" aria-label="Email"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/></svg></a>
        </div>
      </div>
      <div class="fc"><h4>Platform</h4><ul>
        <li><a href="/homeowners">Solar Adopters</a></li><li><a href="/installers">Installers</a></li>
        <li><a href="/financing-partners">Financing Partners</a></li><li><a href="/homeowners">Free Assessment</a></li>
        <li><a href="https://app.apolaki.ai/signup">Create account</a></li></ul></div>
      <div class="fc"><h4>Guides</h4><ul>
        <li><a href="/homeowners">Trusted Installers</a></li><li><a href="/faqs">Net Metering</a></li>
        <li><a href="/financing-partners">Solar Financing</a></li><li><a href="/faqs">MERALCO bill and savings</a></li>
        <li><a href="/blog">All guides</a></li></ul></div>
            <div class="fc"><h4>Company</h4><ul>
        <li><a href="/about">About</a></li><li><a href="/blog">Blog</a></li><li><a href="/faqs">FAQ</a></li>
        <li><a href="/contact">Contact us</a></li><li><a href="/contact?type=installer">Become a partner</a></li></ul></div>
    </div>
    <div class="fbot">
      <p>&copy; 2026 Apolaki &middot; VESS Energy Corp. &middot; Mandaluyong City, Metro Manila</p>
      <div class="fl"><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="mailto:hello@apolaki.ai">hello@apolaki.ai</a></div>
    </div>
  </div>
</footer>
"""

BASE_JS = """<script>
(function(){'use strict';
var RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
var nv=document.getElementById('nv');
var anchor=document.querySelector('.hero,.phero');
if(anchor){
  new IntersectionObserver(function(e){ nv.classList.toggle('solid', !e[0].isIntersecting); },
    {rootMargin:'-64px 0px 0px 0px',threshold:0}).observe(anchor);
}
var bg=document.getElementById('bg'), mm=document.getElementById('mm');
function shut(){mm.classList.remove('on');bg.classList.remove('on');bg.setAttribute('aria-expanded','false');
  document.body.style.overflow='';nv.classList.toggle('solid',window.scrollY>60);}
bg.addEventListener('click',function(){
  var o=mm.classList.toggle('on'); bg.classList.toggle('on',o);
  bg.setAttribute('aria-expanded',String(o)); document.body.style.overflow=o?'hidden':'';
  if(o) nv.classList.add('solid');
});
mm.addEventListener('click',function(e){ if(e.target.closest('a')) shut(); });
document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&mm.classList.contains('on')) shut(); });

document.querySelectorAll('.fq-q').forEach(function(b){
  b.addEventListener('click',function(){
    var it=b.parentElement, pa=it.querySelector('.fq-a'), open=it.classList.contains('on');
    document.querySelectorAll('.fi.on').forEach(function(o){
      o.classList.remove('on'); o.querySelector('.fq-a').style.maxHeight=null;
      o.querySelector('.fq-q').setAttribute('aria-expanded','false');
    });
    if(!open){ it.classList.add('on'); pa.style.maxHeight=pa.scrollHeight+'px'; b.setAttribute('aria-expanded','true'); }
  });
});

var rev=document.querySelectorAll('.r');
if(RM||!('IntersectionObserver' in window)){ rev.forEach(function(e){e.classList.add('in');}); }
else{
  var seen=new WeakSet();
  var rio=new IntersectionObserver(function(en){
    en.forEach(function(e){
      if(!e.isIntersecting||seen.has(e.target))return; seen.add(e.target);
      var sibs=Array.prototype.slice.call(e.target.parentElement.children).filter(function(c){return c.classList.contains('r');});
      e.target.style.transitionDelay=Math.min(Math.max(0,sibs.indexOf(e.target)),4)*80+'ms';
      e.target.classList.add('in'); rio.unobserve(e.target);
    });
  },{threshold:.12,rootMargin:'0px 0px -8% 0px'});
  rev.forEach(function(e){rio.observe(e);});
}

/* sticky step sequence (only on pages that have it) */
var steps=document.querySelectorAll('.hstep'), panes=document.querySelectorAll('.pane');
if(steps.length){
  var cur=0, tick=false;
  function setStep(n){
    steps.forEach(function(s){ s.classList.toggle('on', s.dataset.i===String(n)); });
    panes.forEach(function(p){ p.classList.toggle('on', p.dataset.p===String(n)); });
  }
  function pick(){
    var line=innerHeight*0.5, n=1;
    for(var i=0;i<steps.length;i++){ if(steps[i].getBoundingClientRect().top<=line) n=+steps[i].dataset.i; }
    if(n!==cur){ cur=n; setStep(n); }
  }
  function onScroll(){ if(tick) return; tick=true; requestAnimationFrame(function(){ pick(); tick=false; }); }
  addEventListener('scroll',onScroll,{passive:true});
  addEventListener('resize',onScroll,{passive:true});
  pick();
}

function fmt(v,d){ return v.toLocaleString('en-PH',{minimumFractionDigits:d,maximumFractionDigits:d}); }
var nums=document.querySelectorAll('[data-c]');
if(RM||!('IntersectionObserver' in window)){ nums.forEach(function(n){ n.textContent=fmt(parseFloat(n.dataset.c),+n.dataset.d); }); }
else{
  var nio=new IntersectionObserver(function(en){
    en.forEach(function(e){
      if(!e.isIntersecting)return; nio.unobserve(e.target);
      var el=e.target, to=parseFloat(el.dataset.c), d=+el.dataset.d, t0=null;
      requestAnimationFrame(function tick(ts){
        if(!t0)t0=ts; var p=Math.min((ts-t0)/1500,1), k=1-Math.pow(1-p,4);
        el.textContent=fmt(to*k,d); if(p<1) requestAnimationFrame(tick);
      });
    });
  },{threshold:.5});
  nums.forEach(function(n){nio.observe(n);});
}
})();
(function(){var m={installer:1,financing:2,call:0,onboarding:2};
var t=(location.search.split('type=')[1]||'').split('&')[0], sel=document.getElementById('ct');
if(sel&&t in m) sel.selectedIndex=m[t];})();
(function(){
var RMx=matchMedia('(prefers-reduced-motion: reduce)').matches;
var ps=[].slice.call(document.querySelectorAll('.pxs'));
if(!ps.length||RMx) return;
var tk=false;
function d(){
  var vh=innerHeight;
  ps.forEach(function(s,i){
    var im=s.querySelector('img'); if(!im) return;
    var r=s.getBoundingClientRect();
    if(r.bottom<-200||r.top>vh+200) return;
    var mid=(r.top+r.height/2-vh/2)/vh;
    im.style.setProperty('--py',(mid*-34).toFixed(1)+'px');
  });
}
addEventListener('scroll',function(){if(tk)return;tk=true;requestAnimationFrame(function(){d();tk=false;});},{passive:true});
addEventListener('resize',d,{passive:true}); d();
})();
</script>
"""


def org_schema():
    return """{"@type":"Organization","@id":"https://apolaki.ai/#org","name":"Apolaki","legalName":"VESS Energy Corp.","alternateName":["Apolaki Solar","Apolaki by VESS Energy"],"url":"https://apolaki.ai/","logo":{"@type":"ImageObject","url":"https://apolaki.ai/assets/img/logo-512.png","width":512,"height":512},"slogan":"A catalyst for solar adoption","email":"hello@apolaki.ai","telephone":"+63-917-816-1707","address":{"@type":"PostalAddress","addressLocality":"Mandaluyong City","addressRegion":"Metro Manila","addressCountry":"PH"},"areaServed":{"@type":"Country","name":"Philippines"},"sameAs":["https://www.facebook.com/apolaki.ph","https://www.linkedin.com/company/apolaki"]}"""


SLUGS = ["homeowners", "installers", "financing-partners", "blog", "about",
         "faqs", "contact", "privacy", "terms"]


def relativize(html):
    """GitHub Pages serves this from /apolaki-web/, so root-absolute internal
    links resolve to the domain root and 404. Emit relative links instead.
    Absolute URLs (https://, mailto:, viber:, data:) are left alone, and so is
    every og:/canonical/JSON-LD reference, which is already fully qualified."""
    for slug in SLUGS:
        html = html.replace('href="/%s"' % slug, 'href="%s.html"' % slug)
        html = html.replace('href="/%s?' % slug, 'href="%s.html?' % slug)
        html = html.replace('href="/%s#' % slug, 'href="%s.html#' % slug)
    html = html.replace('href="/assets/', 'href="assets/')
    html = html.replace('src="/assets/', 'src="assets/')
    html = html.replace('href="/"', 'href="index.html"')
    return html


def page(title, desc, path, body, schema_nodes, active=None, extra_head="", extra_js="",
         primary_cta=("https://app.apolaki.ai/signup", "Sign up")):
    graph = ",".join([org_schema()] + schema_nodes)
    schema = f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@graph":[{graph}]}}\n</script>\n'
    return relativize(head(title, desc, path, extra=extra_head)
                      + nav(active, primary_cta)
                      + "\n<main>\n" + body + "\n</main>\n\n"
                      + FOOTER + "\n") + schema + BASE_JS + extra_js + "</body>\n</html>\n"
