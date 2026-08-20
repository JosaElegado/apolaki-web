from playwright.sync_api import sync_playwright
import json,re
PAGES=['index.html','homeowners.html','installers.html','financing-partners.html']
JARGON=['switch-on','end to end','end-to-end','irradiance','grid-tied','photovoltaic','vetted',
        'readiness','stakeholder','seamless','robust','holistic','leverage','ecosystem','curated',
        'bespoke','empower','streamline','synerg','utilise','utilize','value proposition']
with sync_playwright() as p:
    b=p.chromium.launch()
    for f in PAGES:
        pg=b.new_page(viewport={'width':1440,'height':900})
        errs=[]
        pg.on('pageerror',lambda x:errs.append('JS:'+str(x)))
        pg.on('console',lambda m:(errs.append('C:'+m.text) if m.type=='error' and 'TUNNEL' not in m.text else None))
        pg.goto(f'http://localhost:8899/{f}'); pg.wait_for_timeout(1600)
        h1=pg.eval_on_selector_all('h1','e=>e.map(x=>x.textContent.trim())')
        h2=pg.eval_on_selector_all('h2','e=>e.length')
        noalt=pg.eval_on_selector_all('img','e=>e.filter(x=>!x.hasAttribute("alt")).length')
        # schema
        sch=pg.eval_on_selector_all('script[type="application/ld+json"]','e=>e.map(x=>x.textContent)')
        types=[]
        ok=True
        for s in sch:
            try: types+= [n['@type'] for n in json.loads(s)['@graph']]
            except Exception as ex: ok=False; types.append('PARSE-FAIL '+str(ex))
        pg.evaluate('document.querySelectorAll(".fi").forEach(e=>{e.classList.add("on");const a=e.querySelector(".fq-a"); if(a) a.style.maxHeight="999px"})')
        txt=pg.inner_text('body')
        bad=[w for w in JARGON if w.lower() in txt.lower()]
        em = '—' in txt
        ov=[]
        for w in (1600,1440,1180,1024,900,768,600,480,390,360):
            pg.set_viewport_size({'width':w,'height':820}); pg.wait_for_timeout(150)
            if pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth+1"): ov.append(w)
        print(f'\n=== {f} ===')
        print(f'  errors    : {errs or "none"}')
        print(f'  h1        : {len(h1)} -> {h1[0][:58] if h1 else "MISSING"}')
        print(f'  h2 count  : {h2} | imgs missing alt: {noalt}')
        print(f'  schema    : {types if ok else types}')
        print(f'  jargon    : {bad or "clean"} | em dash: {em}')
        print(f'  overflow  : {ov or "none"} | words: {len(txt.split())}')
        pg.close()
    b.close()
