from playwright.sync_api import sync_playwright
PAGES=['index.html','homeowners.html','installers.html','financing-partners.html',
       'blog.html','about.html','faqs.html','contact.html','privacy.html','terms.html']
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    errs=[]
    pg.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
    for f in PAGES:
        r=pg.goto('http://localhost:8899/'+f, wait_until='networkidle')
        pg.wait_for_timeout(400)
        ow=pg.evaluate("document.documentElement.scrollWidth>window.innerWidth+2")
        title=pg.title()[:45]
        print(f, r.status, 'overflow' if ow else 'ok', '|', title)
    # click through nav from index
    pg.goto('http://localhost:8899/index.html', wait_until='networkidle')
    for label in ['Solar Adopters','Installers','Financing','Blog','About','FAQ','Contact']:
        pg.goto('http://localhost:8899/index.html', wait_until='domcontentloaded')
        pg.click('.nv-links a:has-text("%s")'%label)
        pg.wait_for_load_state('domcontentloaded')
        print('  nav',label,'->',pg.url.split('/')[-1])
    # single file
    pg.goto('http://localhost:8899/apolaki.html', wait_until='networkidle')
    for h in ['#/homeowners','#/installers','#/financing','#/blog','#/about','#/faqs','#/contact','#/privacy','#/terms']:
        pg.evaluate("location.hash='%s'"%h); pg.wait_for_timeout(220)
        vis=pg.evaluate("[...document.querySelectorAll('.pg')].filter(e=>!e.hidden).map(e=>e.id)")
        print('  route',h,'->',vis)
    print('console errors:',errs[:5] or 'none')
    b.close()
