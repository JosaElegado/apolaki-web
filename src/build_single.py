"""Build ONE self-contained apolaki.html: 4 pages, inlined CSS/font/logos, hash routing."""
import re, base64, os

ROUTE_MAP = []
for _slug, _route in [('homeowners','homeowners'),('installers','installers'),
                      ('financing-partners','financing'),('blog','blog'),('about','about'),
                      ('faqs','faqs'),('contact','contact')]:
    ROUTE_MAP.append(('href="/%s"' % _slug, 'href="#/%s"' % _route))
    ROUTE_MAP.append(('href="%s.html"' % _slug, 'href="#/%s"' % _route))
    ROUTE_MAP.append(('href="/%s?' % _slug, 'href="#/%s?' % _route))
    ROUTE_MAP.append(('href="%s.html?' % _slug, 'href="#/%s?' % _route))
ROUTE_MAP.append(('href="index.html"', 'href="#/home"'))
ROUTE_MAP.append(('href="privacy.html"', 'href="#/privacy"'))
ROUTE_MAP.append(('href="terms.html"', 'href="#/terms"'))

def b64(path, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())

FONT = b64('assets/fonts/figtree.woff2', 'font/woff2')
LOGO = b64('assets/img/logo-lockup.png', 'image/png')
LOGO_W = b64('assets/img/logo-lockup-white.png', 'image/png')
ICON = b64('assets/img/favicon.png', 'image/png')

css = open('assets/css/apolaki.css').read()
css = css.replace("src:url('../fonts/figtree.woff2') format('woff2')", "src:url(%s) format('woff2')" % FONT)
css += """
/* ---- single-file router ---- */
.pg[hidden]{display:none}
.nv-links a.active{color:var(--gold)}
.nv.solid .nv-links a.active{color:var(--blue)}
"""

PAGES = [
    ('home',        'index.html',              'Home'),
    ('homeowners',  'homeowners.html',         'Solar Adopters'),
    ('installers',  'installers.html',         'Installers'),
    ('financing',   'financing-partners.html', 'Financing'),
    ('blog',        'blog.html',               'Blog'),
    ('about',       'about.html',              'About'),
    ('faqs',        'faqs.html',               'FAQ'),
    ('contact',     'contact.html',            'Contact'),
]

def grab_main(fn):
    h = open(fn).read()
    m = re.search(r'<main>(.*?)</main>', h, re.S)
    body = m.group(1)
    # inline the logo/icon references that lived in assets/
    body = body.replace('src="assets/img/logo-lockup-white.png"', 'src="%s"' % LOGO_W)
    body = body.replace('src="assets/img/logo-lockup.png"', 'src="%s"' % LOGO)
    # testimonial placeholders have no file; strip the img so the monogram shows
    body = re.sub(r'<img src="assets/img/tst-\d\.jpg"[^>]*>', '', body)
    for a, bb in ROUTE_MAP:
        body = body.replace(a, bb)
    return body

# page-specific extra <script> blocks (the financing calculator)
def grab_extra_js(fn):
    h = open(fn).read()
    blocks = re.findall(r'<script>\n\(function\(\)\{\n?\'use strict\';\n?(.*?)</script>', h, re.S)
    return blocks

fin = open('financing-partners.html').read()
# the calculator is the LAST <script> block on that page
calc = re.findall(r'<script>(.*?)</script>', fin, re.S)[-1]

nav_links = "".join(
    '      <a href="#/%s" data-pg="%s"%s>%s</a>\n'
    % (key, key, ' class="active"' if key == 'home' else '', label)
    for key, _, label in PAGES)
mob_links = "".join(
    '  <a class="ml" href="#/%s" data-pg="%s">%s <svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></a>\n' % (key, key, label)
    for key, _, label in PAGES)

THEME = {'home':'th-white','homeowners':'th-sun','installers':'th-sky','financing':'th-white',
         'blog':'th-sun','about':'th-sky','faqs':'th-white','contact':'th-sun',
         'privacy':'th-white','terms':'th-white'}
ALL_PAGES = PAGES + [('privacy','privacy.html','Privacy'), ('terms','terms.html','Terms')]
pages_html = "".join(
    '<div class="pg %s" id="pg-%s"%s>\n%s\n</div>\n'
    % (THEME[key], key, '' if key == 'home' else ' hidden', grab_main(fn))
    for key, fn, _ in ALL_PAGES)

# footer from the built index, with logo inlined and links rewritten to hashes
idx = open('index.html').read()
footer = re.search(r'<footer>.*?</footer>', idx, re.S).group(0)
footer = footer.replace('src="assets/img/logo-lockup-white.png"', 'src="%s"' % LOGO_W)
for _a, _b in ROUTE_MAP:
    footer = footer.replace(_a, _b)

schema = re.search(r'<script type="application/ld\+json">.*?</script>', idx, re.S).group(0)

HTML = """<!DOCTYPE html>
<html lang="en-PH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Apolaki | Trusted Solar Installers Near You</title>
<meta name="description" content="Apolaki takes you from start to finish. What size system your home needs, what you would save, and solar installers you can trust. Free, no sales calls.">
<meta name="theme-color" content="#0A2247">
<link rel="icon" href="%s" sizes="32x32">
<meta property="og:type" content="website">
<meta property="og:title" content="Apolaki | Trusted Solar Installers Near You">
<meta property="og:description" content="What size system your home needs, what you would save, and installers you can trust.">
<link rel="preconnect" href="https://images.pexels.com" crossorigin>
<style>
%s
</style>
</head>
<body>

<nav class="nv" id="nv">
  <div class="nv-in">
    <a href="#/home" data-pg="home" aria-label="Apolaki home">
      <img class="nv-lg" src="%s" alt="Apolaki" width="664" height="160">
      <img class="nv-lg dark" src="%s" alt="Apolaki" width="664" height="160">
    </a>
    <div class="nv-links">
%s      <a href="#/home" style="pointer-events:none;opacity:0;width:0;padding:0"></a>
    </div>
    <div class="nv-act">
      <a href="https://app.apolaki.ai/login" class="lgin">Log in</a>
      <a href="https://app.apolaki.ai/signup" class="b b-glass b-sm">Sign up</a>
      <button class="bg" id="bg" aria-label="Menu" aria-expanded="false" aria-controls="mm"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>

<div class="mm" id="mm">
%s  <div class="mm-b">
    <a href="https://app.apolaki.ai/assessment" class="b b-blue">See my free estimate</a>
    <a href="https://app.apolaki.ai/login" class="b b-line">Log in</a>
  </div>
</div>

<main>
%s</main>

%s

%s

<script>
(function(){'use strict';
var RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
var nv=document.getElementById('nv');
var bg=document.getElementById('bg'), mm=document.getElementById('mm');

/* ---------- router ---------- */
var PAGES=['home','homeowners','installers','financing','blog','about','faqs','contact','privacy','terms'];
function route(){
  var raw=(location.hash||'#/home').replace('#/','');
  var k=raw.split('?')[0], q=raw.split('?')[1]||'';
  if(PAGES.indexOf(k)<0) k='home';
  PAGES.forEach(function(p){
    var el=document.getElementById('pg-'+p);
    if(el) el.hidden = (p!==k);
  });
  if(k==='contact'&&q){var t=(q.split('type=')[1]||'').split('&')[0],sel=document.getElementById('ct'),
      m={installer:1,financing:2,call:0,onboarding:2};
    if(sel&&t in m) sel.selectedIndex=m[t];}
  document.querySelectorAll('[data-pg]').forEach(function(a){
    a.classList.toggle('active', a.dataset.pg===k && a.classList.contains('ml')===false);
  });
  window.scrollTo(0,0);
  reveal(); watchHero(); steps(); if(window.__apolakiCalc) window.__apolakiCalc();
  var T={home:'Apolaki | Trusted Solar Installers Near You',homeowners:'Solar for Your Home | Apolaki',
    installers:'Become a Trusted Installer | Apolaki',financing:'Financing Partners | Apolaki',
    blog:'Solar Guides | Apolaki',about:'About Apolaki',faqs:'FAQ | Apolaki',contact:'Contact | Apolaki'};
  document.title = T[k]||T.home;
}
addEventListener('hashchange',route);
document.addEventListener('click',function(e){
  var a=e.target.closest('a[href^="#/"]'); if(!a) return;
  if(mm.classList.contains('on')) shut();
});

/* ---------- nav ---------- */
var heroIO=null;
function watchHero(){
  if(heroIO){ heroIO.disconnect(); heroIO=null; }
  var vis=document.querySelector('.pg:not([hidden])');
  var anchor=vis && vis.querySelector('.hero');
  if(!anchor){ nv.classList.add('solid'); return; }
  nv.classList.remove('solid');
  heroIO=new IntersectionObserver(function(e){ nv.classList.toggle('solid', !e[0].isIntersecting); },
    {rootMargin:'-64px 0px 0px 0px',threshold:0});
  heroIO.observe(anchor);
}
function shut(){mm.classList.remove('on');bg.classList.remove('on');bg.setAttribute('aria-expanded','false');
  document.body.style.overflow='';}
bg.addEventListener('click',function(){
  var o=mm.classList.toggle('on'); bg.classList.toggle('on',o);
  bg.setAttribute('aria-expanded',String(o)); document.body.style.overflow=o?'hidden':'';
  if(o) nv.classList.add('solid');
});
document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&mm.classList.contains('on')) shut(); });

/* ---------- faq ---------- */
document.addEventListener('click',function(e){
  var b=e.target.closest('.fq-q'); if(!b) return;
  var it=b.parentElement, pa=it.querySelector('.fq-a'), open=it.classList.contains('on');
  it.parentElement.querySelectorAll('.fi.on').forEach(function(o){
    o.classList.remove('on'); o.querySelector('.fq-a').style.maxHeight=null;
    o.querySelector('.fq-q').setAttribute('aria-expanded','false');
  });
  if(!open){ it.classList.add('on'); pa.style.maxHeight=pa.scrollHeight+'px'; b.setAttribute('aria-expanded','true'); }
});

/* ---------- reveal ---------- */
var rio=null;
function reveal(){
  if(rio) rio.disconnect();
  var vis=document.querySelector('.pg:not([hidden])'); if(!vis) return;
  var els=vis.querySelectorAll('.r');
  if(RM||!('IntersectionObserver' in window)){ els.forEach(function(e){e.classList.add('in');}); return; }
  rio=new IntersectionObserver(function(en){
    en.forEach(function(e){
      if(!e.isIntersecting) return;
      var sibs=Array.prototype.slice.call(e.target.parentElement.children).filter(function(c){return c.classList.contains('r');});
      e.target.style.transitionDelay=Math.min(Math.max(0,sibs.indexOf(e.target)),4)*80+'ms';
      e.target.classList.add('in'); rio.unobserve(e.target);
    });
  },{threshold:.12,rootMargin:'0px 0px -8%% 0px'});
  els.forEach(function(e){ e.classList.remove('in'); rio.observe(e); });
}

/* ---------- counters ---------- */
function fmt(v,d){ return v.toLocaleString('en-PH',{minimumFractionDigits:d,maximumFractionDigits:d}); }
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
document.querySelectorAll('[data-c]').forEach(function(n){
  if(RM) n.textContent=fmt(parseFloat(n.dataset.c),+n.dataset.d); else nio.observe(n);
});

/* ---------- sticky step sequence ---------- */
var sCur=0, sTick=false, sList=[], pList=[];
function steps(){
  var vis=document.querySelector('.pg:not([hidden])'); if(!vis) return;
  sList=vis.querySelectorAll('.hstep'); pList=vis.querySelectorAll('.pane'); sCur=0;
  if(sList.length) pickStep();
}
function pickStep(){
  if(!sList.length) return;
  var line=innerHeight*0.5, n=1;
  for(var i=0;i<sList.length;i++){ if(sList[i].getBoundingClientRect().top<=line) n=+sList[i].dataset.i; }
  if(n!==sCur){
    sCur=n;
    sList.forEach(function(s){ s.classList.toggle('on', s.dataset.i===String(n)); });
    pList.forEach(function(p){ p.classList.toggle('on', p.dataset.p===String(n)); });
  }
}
addEventListener('scroll',function(){ if(sTick) return; sTick=true;
  requestAnimationFrame(function(){ pickStep(); sTick=false; }); },{passive:true});

/* ---------- hero parallax (home only) ---------- */
var hi=document.getElementById('heroImg');
if(hi && !RM){
  var t2=false;
  addEventListener('scroll',function(){
    if(t2)return; t2=true;
    requestAnimationFrame(function(){
      var y=Math.min(window.scrollY,window.innerHeight);
      hi.style.transform='translate3d(0,'+(y*.22)+'px,0) scale('+(1+y/window.innerHeight*.07)+')';
      t2=false;
    });
  },{passive:true});
}

/* ---------- waitlist ---------- */
document.addEventListener('submit',function(e){
  var f=e.target.closest('form[data-wait]'); if(!f) return;
  e.preventDefault();
  var inp=f.querySelector('input'); if(!inp.value) return;
  var ok=f.parentElement.querySelector('.wait-ok');
  f.style.display='none'; if(ok){ ok.classList.add('on'); ok.textContent='Thanks. '+inp.value+' is on the list.'; }
});

document.addEventListener('submit',function(e){
  var f=e.target.closest('form[data-contact]'); if(!f) return;
  e.preventDefault();
  var ok=f.parentElement.querySelector('.cform-ok');
  f.style.display='none'; if(ok) ok.classList.add('on');
});

route();
})();
</script>

<script>
%s
</script>
</body>
</html>
""" % (ICON, css, LOGO_W, LOGO, nav_links, mob_links, pages_html, footer, schema, calc)

open('apolaki.html', 'w').write(HTML)
print('apolaki.html', round(os.path.getsize('apolaki.html') / 1024, 1), 'KB')
