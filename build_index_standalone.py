"""Inline everything into apolaki-index.html so it opens from anywhere, even Downloads."""
import base64, os, re

MIME = {'.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml', '.webp': 'image/webp'}


def b64(path):
    ext = os.path.splitext(path)[1].lower()
    return 'data:%s;base64,%s' % (MIME[ext],
                                  base64.b64encode(open(path, 'rb').read()).decode())


css = open('assets/css/apolaki.css').read()

# inline every font the stylesheet asks for
for fn in sorted(set(re.findall(r"\.\./fonts/([A-Za-z0-9._-]+\.woff2)", css))):
    p = 'assets/fonts/' + fn
    if os.path.exists(p):
        css = css.replace("../fonts/" + fn, b64(p))

# inline every image the stylesheet asks for
for fn in sorted(set(re.findall(r"\.\./img/([A-Za-z0-9._-]+)", css))):
    p = 'assets/img/' + fn
    if os.path.exists(p):
        css = css.replace("../img/" + fn, b64(p))

h = open('index.html').read()

# strip external stylesheet / font preloads / icon links, then re-add inline
h = re.sub(r'\n?<link rel="stylesheet" href="assets/css/apolaki\.css">', '', h)
h = re.sub(r'\n?<link rel="preload" href="assets/fonts/[^"]*"[^>]*>', '', h)
h = re.sub(r'\n?<link rel="icon"[^>]*>', '', h)
h = re.sub(r'\n?<link rel="apple-touch-icon"[^>]*>', '', h)

h = h.replace('</head>', '<link rel="icon" href="%s" sizes="32x32">\n<style>\n%s\n</style>\n</head>'
              % (b64('assets/img/favicon.png'), css))

# inline every remaining local asset reference in the markup
for m in sorted(set(re.findall(r'(?:src|href)="((?!https?:)assets/[^"]+)"', h))):
    if os.path.exists(m):
        h = h.replace('"%s"' % m, '"%s"' % b64(m))

# placeholder testimonial avatars do not exist; drop the requests entirely
h = re.sub(r'<img src="assets/img/tst-\d\.jpg"[^>]*>', '', h)

# internal page links point at the single-file build, which routes on hashes
for slug, route in [('homeowners', 'homeowners'), ('installers', 'installers'),
                    ('financing-partners', 'financing'), ('blog', 'blog'),
                    ('about', 'about'), ('faqs', 'faqs'), ('contact', 'contact'),
                    ('privacy', 'privacy'), ('terms', 'terms')]:
    h = h.replace('href="%s.html"' % slug, 'href="apolaki.html#/%s"' % route)
    h = h.replace('href="%s.html?' % slug, 'href="apolaki.html#/%s?' % route)
h = h.replace('href="index.html"', 'href="#top"')

local = re.findall(r'(?:src|href)="((?!https?:|data:|#|mailto:|tel:)[^"]*assets/[^"]*)"', h)
assert not local, local[:5]
open('apolaki-index.html', 'w').write(h)
print('apolaki-index.html', round(len(h) / 1024, 1), 'KB, zero external asset calls')
