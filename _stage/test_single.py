from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':950})
    errs=[]
    pg.on('pageerror',lambda x:errs.append('JS:'+str(x)))
    pg.on('console',lambda m:(errs.append('C:'+m.text) if m.type=='error' and 'TUNNEL' not in m.text and 'pexels' not in m.text.lower() else None))
    pg.goto('file:///home/claude/apolaki/site/apolaki.html'); pg.wait_for_timeout(2000)
    print('load errors:', errs or 'none')
    for k in ['home','homeowners','installers','financing']:
        pg.evaluate(f"location.hash='#/{k}'"); pg.wait_for_timeout(600)
        vis=pg.eval_on_selector_all('.pg','e=>e.filter(x=>!x.hidden).map(x=>x.id)')
        kick=pg.eval_on_selector_all('.pg:not([hidden]) .pkicker','e=>e.filter(x=>getComputedStyle(x).display!=="none").length')
        print(f'  {k:<11} {vis} kickers-visible={kick}')
    pg.evaluate("location.hash='#/financing'"); pg.wait_for_timeout(600)
    print('calc:', pg.inner_text('#kMonthly'), pg.inner_text('#tBm'))
    pg.click('.seg button[data-term="60"]'); pg.wait_for_timeout(300)
    print('60mo:', pg.inner_text('#kMonthly'), pg.inner_text('#tBm'))
    pg.click('#tab-inst'); pg.wait_for_timeout(350); print('inst:', pg.inner_text('#kMonthly'))
    # waitlist
    pg.evaluate("location.hash='#/homeowners'"); pg.wait_for_timeout(600)
    pg.fill('form[data-wait] input','josa@apolaki.ai')
    pg.click('form[data-wait] button'); pg.wait_for_timeout(400)
    print('waitlist:', pg.eval_on_selector('.pg:not([hidden]) .wait-ok','e=>e.classList.contains("on")+" | "+e.textContent'))
    # faq
    pg.evaluate("location.hash='#/home'"); pg.wait_for_timeout(500)
    pg.click('.pg:not([hidden]) .fq-q'); pg.wait_for_timeout(400)
    print('faq:', pg.eval_on_selector('.pg:not([hidden]) .fi','e=>e.classList.contains("on")'))
    # spacing: gap between a section head and the preceding section
    pg.evaluate("location.hash='#/homeowners'"); pg.wait_for_timeout(500)
    gaps=pg.evaluate("""(()=>{const s=[...document.querySelectorAll('.pg:not([hidden]) section')];const o=[];
      for(let i=1;i<s.length;i++){const a=s[i-1].getBoundingClientRect(),c=s[i].getBoundingClientRect();
      const h=s[i].querySelector('h2'); if(h) o.push(Math.round(h.getBoundingClientRect().top-a.bottom));} return o;})()""")
    print('head-to-prev-section gaps(px):', gaps)
    ov=[]
    for w in (1600,1440,1180,1024,900,768,600,480,390,360):
        pg.set_viewport_size({'width':w,'height':820}); pg.wait_for_timeout(160)
        if pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth+1"): ov.append(w)
    print('overflow:', ov or 'none')
    pg.set_viewport_size({'width':390,'height':844}); pg.wait_for_timeout(250)
    pg.click('#bg'); pg.wait_for_timeout(400)
    pg.click('.mm a[data-pg="installers"]'); pg.wait_for_timeout(600)
    print('mobile nav ->', pg.eval_on_selector_all('.pg','e=>e.filter(x=>!x.hidden).map(x=>x.id)'))
    print('final errors:', errs or 'none')
    b.close()
