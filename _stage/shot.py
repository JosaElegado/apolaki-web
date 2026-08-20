import sys
from playwright.sync_api import sync_playwright
page = sys.argv[1]; out = sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1440,'height':950})
    errs=[]; pg.on('pageerror',lambda x:errs.append(str(x)))
    pg.on('console',lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
    pg.goto(f'http://localhost:8899/{page}'); pg.wait_for_timeout(2000)
    print('errors:', errs or 'none')
    pg.evaluate("document.querySelectorAll('.r').forEach(x=>x.classList.add('in'))")
    pg.wait_for_timeout(700)
    pg.screenshot(path=out, full_page=True)
    for w in (1600,1440,1180,1024,900,768,600,480,390,360):
        pg.set_viewport_size({'width':w,'height':820}); pg.wait_for_timeout(180)
        if pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth+1"):
            print(f'  OVERFLOW @{w}')
    print('responsive: checked')
    b.close()
