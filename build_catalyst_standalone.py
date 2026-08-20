"""Inline everything into apolaki-catalyst.html so it opens from anywhere, even Downloads."""
import base64, re


def b64(path, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())


FONT = b64('assets/fonts/figtree.woff2', 'font/woff2')
LOGO = b64('assets/img/logo-lockup.png', 'image/png')
LOGO_W = b64('assets/img/logo-lockup-white.png', 'image/png')
ICON = b64('assets/img/favicon.png', 'image/png')

css = open('assets/css/apolaki.css').read()
css = css.replace("src:url('../fonts/figtree.woff2') format('woff2')",
                  "src:url(%s) format('woff2')" % FONT)

h = open('index-catalyst.html').read()

# strip the external stylesheet, font preload and icon links, then inline
h = re.sub(r'\n?<link rel="stylesheet" href="assets/css/apolaki\.css">', '', h)
h = re.sub(r'\n?<link rel="preload" href="assets/fonts/figtree\.woff2"[^>]*>', '', h)
h = re.sub(r'\n?<link rel="icon"[^>]*>', '', h)
h = re.sub(r'\n?<link rel="apple-touch-icon"[^>]*>', '', h)

head_add = ('<link rel="icon" href="%s" sizes="32x32">\n<style>\n%s\n</style>' % (ICON, css))
h = h.replace('</head>', head_add + '\n</head>')

# inline the logos
h = h.replace('src="assets/img/logo-lockup-white.png"', 'src="%s"' % LOGO_W)
h = h.replace('src="assets/img/logo-lockup.png"', 'src="%s"' % LOGO)

# testimonial avatar placeholders do not exist yet; drop the requests so the
# file makes zero local asset calls
h = re.sub(r'<img src="assets/img/tst-\d\.jpg"[^>]*>', '', h)

# internal page links must point at the single-file build, which routes on hashes
for slug, route in [('homeowners', 'homeowners'), ('installers', 'installers'),
                    ('financing-partners', 'financing'), ('blog', 'blog'),
                    ('about', 'about'), ('faqs', 'faqs'), ('contact', 'contact'),
                    ('privacy', 'privacy'), ('terms', 'terms')]:
    h = h.replace('href="%s.html"' % slug, 'href="apolaki.html#/%s"' % route)
    h = h.replace('href="%s.html?' % slug, 'href="apolaki.html#/%s?' % route)
h = h.replace('href="index.html"', 'href="#top"')

# absolute apolaki.ai URLs in og: tags and JSON-LD are fine, they are not local loads
local = [m for m in re.findall(r'(?:src|href)="((?!https?:)[^"]*assets/[^"]*)"', h)]
assert not local, local[:5]
open('apolaki-catalyst.html', 'w').write(h)
print('apolaki-catalyst.html', round(len(h) / 1024, 1), 'KB, zero external asset calls')
