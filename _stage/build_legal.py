import _shell as S

WRAP = """<section class="phero">
  <div class="w">
    <div class="ph-in">
      <h1>%s</h1>
      <p class="lead">%s</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="w">
    <div class="legal r">
%s
    </div>
  </div>
</section>"""


def sec(h, *paras):
    return "      <h2>%s</h2>\n" % h + "".join("      <p>%s</p>\n" % p for p in paras)


PRIVACY = sec(
    "What we collect",
    "When you use the free assessment we ask for your name, email or mobile number, your address or barangay, and a photo or reading of your electricity bill. If you send us a message we keep that message. That is it. We do not ask for financial account details, and we never will over email.",
) + sec(
    "Why we collect it",
    "To work out what a solar system would do for your bill, and to match you with installers who serve your area. If you ask us to introduce you to an installer, we share your name, contact details and roof information with that installer so they can quote you. We do not share your details with anyone you have not asked to be introduced to.",
) + sec(
    "Your rights",
    "Under the Data Privacy Act of 2012 (RA 10173) you can ask us what we hold about you, ask us to correct it, or ask us to delete it. Email hello@apolaki.ai and we will action it within fifteen working days.",
) + sec(
    "How long we keep it",
    "Assessment data stays for two years so you can come back to it, then it is deleted. If you ask us to delete it sooner, we do.",
) + sec(
    "Cookies",
    "We use a small number of cookies to keep the site working and to count visits. No advertising trackers.",
) + sec(
    "Who to contact",
    "VESS Corp., Mandaluyong City, Metro Manila. Email hello@apolaki.ai. If you are not happy with how we handled your data you can raise it with the National Privacy Commission.",
)

TERMS = sec(
    "What Apolaki is",
    "Apolaki is a platform run by VESS Corp. We give you an estimate of what solar could do for your electricity bill, and we connect you with installers. We are not an installer, a lender, or a licensed financial adviser.",
) + sec(
    "Estimates are estimates",
    "Every number on this site, including anything the calculators produce, is illustrative. It is based on the information you give us and on public data about rates and equipment prices. It is not a quote, not an offer, not a forecast, and not a promise of return. Your actual savings depend on your roof, your usage, your utility, the equipment installed and how rates move. Always rely on the written quote and contract from your installer, and on the terms from your lender.",
) + sec(
    "Installers",
    "We check the installers on our platform for registration, track record and workmanship, and we drop the ones that stop meeting the standard. The contract for your installation is between you and the installer. We are not a party to it and we do not warrant their work.",
) + sec(
    "Financing",
    "Any financing shown or discussed comes from third-party lenders and partners on their own terms. We do not lend, and we do not give financial advice. Read the loan documents and, if you need to, get independent advice before you sign.",
) + sec(
    "Using the site",
    "Do not scrape it, do not try to break it, and do not use it to mislead anyone. We can suspend access if you do. Everything on this site, including the Apolaki name and logo, belongs to VESS Corp.",
) + sec(
    "Changes and governing law",
    "We may update these terms. The version on this page is the one that applies. These terms are governed by the laws of the Republic of the Philippines.",
)


def build():
    for slug, title, h1, lead, body_html, mtitle, mdesc in [
        ("privacy", "Privacy", "Privacy",
         "What we collect, why we collect it, and how to get it deleted. Plain version, no legal fog.",
         PRIVACY, "Privacy Policy | Apolaki",
         "How Apolaki collects, uses and protects your data under the Philippine Data Privacy Act."),
        ("terms", "Terms", "Terms of use",
         "The short version: our estimates are estimates, your contract is with your installer, and we are not a lender.",
         TERMS, "Terms of Use | Apolaki",
         "The terms that apply when you use Apolaki, including what our estimates are and are not."),
    ]:
        html = S.page(
            title=mtitle, desc=mdesc, path="/" + slug,
            body=WRAP % (h1, lead, body_html),
            schema_nodes=['{"@type":"WebPage","@id":"https://apolaki.ai/%s#page","url":"https://apolaki.ai/%s","name":"%s","isPartOf":{"@id":"https://apolaki.ai/#website"}}' % (slug, slug, title)],
            active=None,
            primary_cta=("https://app.apolaki.ai/signup", "Sign up"))
        open("%s.html" % slug, "w").write(html)
        print("wrote", slug + ".html")


if __name__ == "__main__":
    build()
