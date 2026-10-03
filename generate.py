#!/usr/bin/env python3
"""Generate the static Distinct Designs Construction website.

Run from the repository root:
    python3 generate.py

Output is plain HTML. Vercel does not need this script.
"""

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PHONE_DISPLAY = "(760) 221-4290"
PHONE_TEL = "+17602214290"
# TODO(v2): Email must reach Nick directly and sync into GHL. Nick to decide:
# keep this Gmail or switch to nick@distinctdesignspro.com.
EMAIL = "distinctdesigns360@gmail.com"

# Production origin for canonicals, OG and the sitemap. Previews stay noindexed.
SITE_URL = "https://distinctdesignsconstruction.com"
LICENSE = "#1145786"
LOCATION = "Yucca Valley, CA"  # matches the Google Business Profile
# Step 1 footer line, exactly as written in the brief.
COMPANY_LINE = "Distinct Designs Construction · CA Lic. #1145786 · General liability &amp; workers' comp insured"
LICENSE_EYEBROW = "CA Lic. #1145786 · Coachella Valley &amp; High Desert"
EXPERIENCE = "18 years building in the desert. 100+ years of combined experience on our crew."
CREW_LINE = "Our in-house crew and the same vetted trade partners on every job."

# "Where we build" (Step 3). Each town with a city page is linked.
WHERE_WE_BUILD = [
    "Palm Springs",
    "Rancho Mirage",
    "Palm Desert",
    "Indian Wells",
    "La Quinta",
    "Yucca Valley",
    "Joshua Tree",
    "Pioneertown",
]
AREAS = WHERE_WE_BUILD

GUIDE_FORM = "YQYYVz28qqwYJWbc8ZUw"
CONTACT_FORM = "IbFWLZlZNETBrImKFVjN"
REFERRAL_FORM = "MyS2TrJSOhTn1mitpihf"

JOURNEY = "start-your-journey"
JOURNEY_LABEL = "Start Your Journey"

# Header (Step 3): the two things we sell and how we work. Nothing else.
NAV_DROPDOWN_LABEL = "Luxury Custom Homes"
NAV_DROPDOWN = [
    ("Custom Homes", "services/custom-home-build"),
    ("Guest Houses &amp; ADUs", "services/custom-adu"),
]
NAV = [
    ("Luxury Remodels", "services/whole-home-remodel"),
    ("Portfolio", "projects"),
    ("Our Process", "our-process"),
    ("About", "about"),
]
AREA_LINKS = [
    ("Palm Springs", "service-areas/palm-springs"),
    ("Rancho Mirage", "service-areas/rancho-mirage"),
    ("Palm Desert", "service-areas/palm-desert"),
    ("Indian Wells", "service-areas/indian-wells"),
    ("La Quinta", "service-areas/la-quinta"),
    ("Yucca Valley", "service-areas/yucca-valley"),
    ("Joshua Tree", "service-areas/joshua-tree"),
]
AREA_TARGET = dict(AREA_LINKS)

# Google rating badge (Step 12).
# TODO(v2): confirm the Google Business Profile URL and the current rating.
# 4.9 / 15+ reviews is the figure already published on the guide pages.
GBP_URL = "https://www.google.com/maps/search/?api=1&amp;query=Distinct+Designs+Construction+Yucca+Valley+CA"
GBP_RATING = "4.9"


def prefix(slug: str) -> str:
    depth = len([p for p in slug.split("/") if p])
    return "../" * depth


def href(slug: str, target: str) -> str:
    pre = prefix(slug)
    target = target.strip("/")
    if not target:
        return pre or "./"
    return f"{pre}{target}/"


def asset(slug: str, path: str) -> str:
    return prefix(slug) + path


def canonical(slug):
    path = "/" + (slug.strip("/") + "/" if slug.strip("/") else "")
    return SITE_URL + path


def business_ld() -> str:
    data = {
        "@context": "https://schema.org",
        "@type": ["HomeAndConstructionBusiness", "GeneralContractor"],
        "@id": SITE_URL + "/#business",
        "name": "Distinct Designs Construction",
        "url": SITE_URL + "/",
        "description": (
            "Luxury custom homes, whole-home remodels, and guest houses and ADUs "
            "across the Coachella Valley and High Desert. CA Lic. #1145786."
        ),
        "telephone": "+1-760-221-4290",
        "email": EMAIL,
        "logo": SITE_URL + "/images/site/DD-logo-full.webp",
        "image": SITE_URL + "/images/site/Custom-Desert-Home.webp",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Yucca Valley",
            "addressRegion": "CA",
            "addressCountry": "US",
        },
        "areaServed": [{"@type": "City", "name": c} for c in WHERE_WE_BUILD]
        + [{"@type": "Place", "name": "Coachella Valley"}, {"@type": "Place", "name": "High Desert"}],
        "sameAs": [
            "https://www.instagram.com/distinctdesignsconst/",
            "https://www.facebook.com/profile.php?id=61561101665757",
            "https://www.yelp.com/biz/distinct-designs-yucca-valley-6",
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def faq_ld(items):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": re.sub(r"<[^>]+>", "", q),
                "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)},
            }
            for q, a in items
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def head(slug, title, description, extra_ld=""):
    p = prefix(slug)
    extra = ""
    if extra_ld:
        extra = f'\n<script type="application/ld+json">{extra_ld}</script>'
    can = canonical(slug)
    og_img = SITE_URL + "/images/site/Custom-Desert-Home.webp"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Distinct Designs Construction">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}favicon.jpg" type="image/jpeg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400&amp;family=Manrope:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}styles.css">
<script>document.documentElement.classList.add("js-reveal");</script>
<script type="application/ld+json">{business_ld()}</script>{extra}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def current(slug, target):
    if slug == target or slug.startswith(target + "/"):
        return ' aria-current="page"'
    return ""


def dropdown_menu(slug, label, links, menu_id, start_open=False):
    active = any(slug == t for _, t in links)
    current_attr = ' aria-current="true"' if active else ""
    expanded = "true" if start_open else "false"
    open_class = " is-open" if start_open else ""
    items = []
    for item_label, target in links:
        items.append(
            f'<a class="nav-subitem" role="menuitem" href="{href(slug, target)}"{current(slug, target)}>{item_label}</a>'
        )
    return f"""<div class="nav-dropdown{open_class}">
      <button type="button" class="nav-item nav-dropdown__toggle" aria-expanded="{expanded}" aria-haspopup="true" aria-controls="{menu_id}"{current_attr}>{label}</button>
      <div class="nav-dropdown__panel" id="{menu_id}" role="menu" aria-label="{label}">
        {"".join(items)}
      </div>
    </div>"""


def nav(slug):
    p = prefix(slug)
    links = [dropdown_menu(slug, NAV_DROPDOWN_LABEL, NAV_DROPDOWN, "homes-menu")]
    mobile = [dropdown_menu(slug, NAV_DROPDOWN_LABEL, NAV_DROPDOWN, "homes-menu-mobile", start_open=True)]
    for label, target in NAV:
        item = f'<a class="nav-item" href="{href(slug, target)}"{current(slug, target)}>{label}</a>'
        links.append(item)
        mobile.append(item)
    mobile.append(f'<a class="btn btn--nav" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>')
    mobile.append(f'<a class="btn btn--primary" href="{href(slug, JOURNEY)}">{JOURNEY_LABEL}</a>')
    return f"""<header class="site-nav" id="site-nav">
  <div class="site-nav__inner">
    <a href="{href(slug, "")}" class="site-nav__logo">
      <img src="{p}images/logo-distinct-designs.webp" alt="Distinct Designs Construction" width="350" height="128">
    </a>
    <a class="btn btn--nav-primary site-nav__call" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">
      <svg class="site-nav__call-icon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.25 1.02l-2.2 2.2z"/></svg>
      <span>Call</span>
    </a>
    <nav class="site-nav__links" aria-label="Primary">
      {"".join(links)}
    </nav>
    <div class="site-nav__actions">
      <a class="btn btn--nav" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a class="btn btn--nav-primary" href="{href(slug, JOURNEY)}">{JOURNEY_LABEL}</a>
    </div>
    <button class="site-nav__toggle" id="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav__mobile">
      <span class="site-nav__toggle-icon" aria-hidden="true"><span></span><span></span><span></span></span>
      <span class="site-nav__toggle-label">Menu</span>
    </button>
  </div>
  <nav class="site-nav__mobile" id="site-nav__mobile" aria-label="Mobile">
    {"".join(mobile)}
  </nav>
</header>
<div class="sticky-cta" id="sticky-cta">
  <p>Ready to talk about your project?</p>
  <div class="sticky-cta__actions">
    <a href="tel:{PHONE_TEL}" class="btn btn--sticky-call">Call</a>
    <a href="{href(slug, JOURNEY)}" class="btn btn--sticky">{JOURNEY_LABEL}</a>
  </div>
</div>
"""


FOOTER_LINKS = [
    ("Custom Homes", "services/custom-home-build"),
    ("Guest Houses &amp; ADUs", "services/custom-adu"),
    ("Luxury Remodels", "services/whole-home-remodel"),
    ("Portfolio", "projects"),
    ("Our Process", "our-process"),
    ("About", "about"),
    ("Planning Guide", "planning-guide"),
    ("Partners", "partners"),
    ("Start Your Journey", JOURNEY),
    ("Privacy", "privacy-policy"),
    ("Opt-out preferences", "opt-out-preferences"),
]


def where_we_build_html(slug, sep=" · "):
    named = [city_anchor(slug, name) for name in WHERE_WE_BUILD]
    return sep.join(named) + ", and across the Coachella Valley and High Desert."


def footer(slug):
    p = prefix(slug)
    links = "".join(f'<a href="{href(slug, t)}">{label}</a>' for label, t in FOOTER_LINKS)
    return f"""<footer class="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__cols">
      <div>
        <img class="site-footer__logo" src="{p}images/site/distinct-web-white-300x112.png" alt="Distinct Designs Construction" width="300" height="112" loading="lazy">
        <p class="site-footer__brand site-footer__company">{COMPANY_LINE}</p>
        <p>{LOCATION} · <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><a href="https://www.instagram.com/distinctdesignsconst/">Instagram</a> · <a href="https://www.facebook.com/profile.php?id=61561101665757">Facebook</a> · <a href="https://www.yelp.com/biz/distinct-designs-yucca-valley-6">Yelp</a></p>
      </div>
      <div>
        <h2>Explore</h2>
        <nav aria-label="Footer">{links}</nav>
      </div>
      <div>
        <h2>Where we build</h2>
        <p>{where_we_build_html(slug)}</p>
      </div>
    </div>
  </div>
  <p class="site-footer__legal">&copy; <span id="year"></span> Distinct Designs Construction. All rights reserved. CA Lic. #1145786.</p>
</footer>
<dialog class="lightbox" id="lightbox" aria-label="Enlarged project photograph">
  <button class="lightbox__close" id="lightbox-close" type="button" aria-label="Close">&times;</button>
  <figure class="lightbox__figure">
    <img class="lightbox__img" id="lightbox-img" alt="" width="1200" height="900">
    <figcaption class="lightbox__caption" id="lightbox-caption"></figcaption>
  </figure>
</dialog>
<script src="{p}script.js"></script>
</body>
</html>
"""


def ph(note):
    """Placeholder-photo marker. Renders a tiny corner tag via one CSS rule
    ([data-placeholder-photo]::before). Remove the attribute, or that rule,
    to turn the tags off. The note says what the final photo should be."""
    return f' data-placeholder-photo="{note}"' if note else ""


def ph_comment(note):
    return f"\n<!-- TODO(v2) PLACEHOLDER PHOTO: {note} -->" if note else ""


def hero(slug, image, alt, width, height, srcset, eyebrow, h1, sub, primary_href, primary_label, page=False, placeholder="", extra=""):
    p = prefix(slug)
    klass = "hero hero--page" if page else "hero"
    srcset_attr = f'\n      srcset="{srcset}"\n      sizes="100vw"' if srcset else ""
    sub_html = f'\n    <p class="subhead">{sub}</p>' if sub else ""
    return f"""{ph_comment(placeholder)}
<header class="{klass}"{ph(placeholder)}>
  <img class="hero__image" src="{p}{image}"{srcset_attr} alt="{alt}" width="{width}" height="{height}" fetchpriority="high" loading="eager">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>{sub_html}
    <nav class="hero-cta" aria-label="Hero">
      <a href="tel:{PHONE_TEL}" class="btn btn--secondary">Call {PHONE_DISPLAY}</a>
      <a href="{primary_href}" class="btn btn--primary">{primary_label}</a>
    </nav>{extra}
  </div>
</header>
"""


def page_hero(slug, image, alt, width, height, eyebrow, h1, sub="", placeholder="", klass=""):
    """Inner-page hero without buttons."""
    p = prefix(slug)
    sub_html = f'\n    <p class="subhead">{sub}</p>' if sub else ""
    return f"""{ph_comment(placeholder)}
<header class="hero hero--page{(" " + klass) if klass else ""}"{ph(placeholder)}>
  <img class="hero__image" src="{p}{image}" alt="{alt}" width="{width}" height="{height}" fetchpriority="high" loading="eager">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>{sub_html}
  </div>
</header>
"""


def faq_html(slug_prefix, items):
    blocks = []
    for i, (q, a) in enumerate(items, 1):
        fid = f"{slug_prefix}-faq-{i}"
        blocks.append(f"""<div class="accordion__item">
  <h3><button class="accordion__trigger" aria-expanded="false" aria-controls="{fid}">{q}</button></h3>
  <div class="accordion__panel" id="{fid}"><p>{a}</p></div>
</div>""")
    return '<div class="accordion">' + "".join(blocks) + "</div>"


def quotes_html(items):
    blocks = []
    for quote, cite in items:
        blocks.append(f"<blockquote><p>&ldquo;{quote}&rdquo;</p><cite>{cite}</cite></blockquote>")
    return '<div class="testimonial-stack reveal">' + "".join(blocks) + "</div>"


def google_badge():
    return f"""<!-- TODO(v2): confirm the Google Business Profile link and the live rating before launch. -->
<p class="google-badge"><a href="{GBP_URL}" rel="noopener" target="_blank"><span class="google-badge__stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span> {GBP_RATING} on Google · Read every review</a></p>"""


def reviews_section(items, tinted=True, section_id="testimonials"):
    """Step 12: "What clients and partners say", three reviews at most."""
    assert len(items) <= 3
    klass = "section section--tinted" if tinted else "section"
    return f"""<section class="{klass}" id="{section_id}">
  <h2>What clients and partners say</h2>
  {quotes_html(items)}
  {google_badge()}
</section>"""


# Reviews (Step 12). Kept verbatim. Troy Gatchell's review stays on Google only.
Q_MYERS = ("Nick and team went above and beyond! Great attention to detail and excellent communication.", "Jessica &amp; Laura Myers")
Q_KATIE = ("Nick and his crew were by far the best contractors I have worked with out here in Yucca Valley/Landers.", "Katie Lee")
Q_VICTORIA = ("Nick and everyone on his team are just simply the best. He gave us a magical bathroom and also helped out with new wood-trimmed windows and doors. Everyone was super kind, super fast, and really skilled. Nick's passion for his job shows, and it made the process really personal and fun. So happy with the results!", "Victoria Lynn Carroll")
Q_BENOIT = ("A complete remodel in Joshua Tree. Professional, detail-oriented, delivered on time and on budget.", "Benoit R. · Joshua Tree")

HOME_QUOTES = [Q_MYERS, Q_KATIE]

GUIDE_QUOTES = [
    ("A full down to the studs remodel finished on time and on budget, accessible the whole way, prompt with every update.", "Ken Z. · Whole-Home Remodel"),
    ("A complete remodel in Joshua Tree. Professional, detail-oriented, delivered on time and on budget.", "Benoit R. · Joshua Tree"),
    ("Called about our remodel and Nick came to the house the same day and communicated with us every step.", "Hannah S. · Remodel"),
]

INSURED_ANSWER = "Yes, we carry general liability and workers' comp insurance. Distinct Designs Construction is a licensed California contractor, CA Lic. #1145786."

# TODO(v2): build timeline. Kept at 10 to 18 months for now. The brief says to
# match the Planning Guide; the guide landing pages describe "the real 18-27
# month timeline" from first conversation to move-in. Confirm with Nick.
TIMELINE_TODO = "<!-- TODO(v2): match the custom-home timeline to the Planning Guide (guide pages say 18 to 27 months, first conversation to move-in). -->"
# TODO(v2): out-of-state answer. "We do it regularly" and "many of our most
# celebrated projects" are left off until Nick confirms they are literally true.

HOME_FAQ = [
    ("What do you specialize in?",
     "Luxury custom homes from $1M to $5M+, whole-home remodels from $250K, and guest houses and ADUs on properties that already have a home."),
    ("Are you licensed and insured?", INSURED_ANSWER),
    ("How do you handle budgets and prevent cost overruns?",
     "Before construction begins, every material selection, design detail, and architectural decision is priced against your budget. The decisions that move cost get made on paper, not on the job site. If an element of the design needs to be reconsidered, we identify it early and present alternatives that meet the same standard, before you have committed to it."),
    ("How do you keep clients informed throughout the build?",
     "You receive real-time photo updates through your client portal, plus detailed bi-weekly field reports, so you always know where your project stands. When you reach out, you hear back the same day, directly from leadership or your dedicated project manager, not a receptionist or voicemail box. Text, email, or phone call: we are always accessible."),
    ("Do you work with architects and interior designers?",
     "Absolutely. We have longstanding relationships with architects, designers, and realtors across the Coachella Valley and High Desert. We bring precise design visions to life without compromising the intent, and our partners refer their clients to us because they know the work will be executed with the same care they put into their own. When your architect, designer, and builder work as true partners, the vision gets built as intended."),
    ("What does your pre-construction process look like?",
     "Most of what protects your budget happens before the first shovel. After a phone consultation and a site visit, the Design &amp; Pre-Construction Agreement is a paid planning phase before any construction contract: we coordinate your architect and engineers, analyze the site, manage permitting and approvals, and price every major decision against your budget. You then receive one overall price to build, with separate allowances for the materials you select."),
    ("How long does a custom home build or full remodel typically take?",
     "Every project is unique and timelines vary based on scope, size, and complexity. A full custom home build typically ranges from 10 to 18 months depending on design, permitting, and finish selections. A full home remodel can range from 2 to 6 months. Our pre-construction process, dedicated crew, and proactive communication are all designed to prevent the delays that derail most builds, and you will always know where your project stands and why."),
    ("Can you manage my project if I live out of state or travel frequently?",
     "Yes. Your client portal provides real-time photo updates, bi-weekly field reports keep you informed, and we schedule video calls throughout the build, so you can follow every stage without needing to be on site. We act as your eyes and ears on the ground."),
    ("What makes Distinct Designs Construction different from other contractors?",
     "Our in-house crew and the same vetted trade partners work on every job, from groundbreaking to keys. Every decision is planned and priced before groundbreaking. You have direct access to leadership on every project, not an assistant or a call center. Our job sites are kept clean, organized, and protected through every phase. And when something unexpected comes up, because in construction something always does, we bring it to you early, with options. We don't just build homes. We protect your investment and deliver something you will be proud of for decades."),
    ("Do you handle permits and inspections?",
     "Yes. We manage the entire permitting and inspection process on your behalf, from plan approvals through certificates of occupancy. You never have to chase paperwork, navigate local offices, or follow up with the city on your own, which matters most for first-time builders and out-of-state clients."),
    ("How is my investment protected throughout the project?",
     "Financial transparency is a core part of how we operate. Payments are tied to project milestones, so you always know what you are paying for and why. We provide detailed documentation for every phase, we never ask for funds beyond what the current scope requires, and every major decision is priced against your budget before work begins."),
    ("Do you offer post-construction support after the project is complete?",
     "Yes. When we hand over the keys, the only thing left behind is the home itself. That includes a full deep clean, punch list management, subcontractor follow-up for warranties and certificates of occupancy, utility activation and smart home setup, appliance registration, and a complete documentation package with warranties, manuals, as-built drawings, and maintenance schedules."),
    ("What areas do you serve?",
     "The Coachella Valley and High Desert, including Palm Springs, Rancho Mirage, Palm Desert, Indian Wells, La Quinta, Yucca Valley, and Joshua Tree."),
]

BUILD_FAQ = [
    ("How long does a custom home build take?",
     "Typically 10 to 18 months, depending on design, permitting, and finish selections. Our pre-construction process and dedicated crew are built to protect that timeline, not just estimate it."),
    ("Can you manage my project if I live out of state?",
     "Yes. Your client portal gives you real-time photo updates, you get bi-weekly field reports, and we schedule video calls throughout the build."),
    ("Do you handle permits and inspections?",
     "Yes, the entire process, from plan approvals through certificates of occupancy. You never chase paperwork or navigate city offices yourself."),
    ("Are you licensed and insured?", INSURED_ANSWER),
    ("How is my investment protected?",
     "Payments are tied to project milestones, with detailed documentation at every phase. We never request funds beyond what the current scope requires, and every material, design detail, and architectural decision is priced against your budget before construction begins."),
]

REMODEL_FAQ = [
    ("How long does a full home remodel take?",
     "Typically 2 to 6 months, depending on scope and finish selections. Our pre-construction process is built to protect that timeline, not just estimate it."),
    ("Can you manage my remodel if I live out of state?",
     "Yes. Real-time photo updates through your client portal, bi-weekly field reports, and scheduled video calls keep you informed without needing to be on site."),
    ("Do you handle permits and inspections?",
     "Yes, the entire process, from plan approvals through certificates of occupancy."),
    ("Are you licensed and insured?", INSURED_ANSWER),
    ("How is my investment protected during the remodel?",
     "Payments are tied to project milestones with full documentation, and every decision is priced before the first wall comes down. We never request funds beyond what the current scope requires."),
]

ADU_FAQ = [
    ("How long does a guest house or ADU build typically take?",
     "Timelines vary by size and scope, but our pre-construction process is designed to protect your timeline from the delays that derail most ADU projects."),
    ("Can you manage my guest house project if I live out of state?",
     "Yes. Real-time photo updates through your client portal, bi-weekly reports, and scheduled video calls keep you informed throughout."),
    ("Do you handle permits for ADUs?",
     "Yes, the full process, from plan approval through certificate of occupancy, including utility connections."),
    ("Are you licensed and insured?", INSURED_ANSWER),
    ("How is my investment protected?",
     "Payments are tied to milestones, with full documentation and no requests beyond the current scope. Every decision is planned and priced before we start."),
]


PROJECTS = {
    "cubero": ("projects/cubero", "images/project-cubero.webp", "Cubero ground-up custom home from above, with pool and desert landscape", 900, 675, "Cubero", "Ground-up custom home"),
    "alturas": ("projects/alturas", "images/project-alturas.webp", "Alturas custom home in progress: sheathed walls with a circular window opening, against the desert and mountains", 1400, 932, "Alturas", "Now building"),
    "hilltop": ("projects/hilltop", "images/site/hilltop-01-2.webp", "Hilltop terrace at dusk with a fire bowl, string lights and a spa, valley lights beyond", 1440, 1080, "Hilltop", "Rescue and completion"),
    "la-mirada": ("projects/la-mirada", "images/project-la-mirada.webp", "La Mirada renovation: open-plan kitchen and living area with marble island, brass pendants and oak floors", 900, 1200, "La Mirada", "Luxury renovation"),
}


def project_tiles(slug, keys, labels=None, placeholders=None):
    """Linked project tiles. keys picks projects; labels overrides the tile text."""
    p = prefix(slug)
    labels = labels or {}
    placeholders = placeholders or {}
    bits = []
    for key in keys:
        target, img, alt, w, h, name, note = PROJECTS[key]
        title, sub = labels.get(key, (name, note))
        bits.append(f"""<a class="project-tile project-tile--link" href="{href(slug, target)}"{ph(placeholders.get(key, ""))}>
  <img src="{p}{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
  <span class="project-tile__label">{title} <em>{sub}</em></span>
</a>""")
    count = {1: "one", 2: "two", 3: "three"}.get(len(keys), "")
    mod = f" projects-grid--{count}" if count else ""
    return f'<div class="projects-grid{mod} reveal">' + "".join(bits) + "</div>"


def town_links(slug):
    """Step 3/4/5: "Where we build" town links. No town in the heading."""
    items = "".join(f"<li>{city_anchor(slug, c)}</li>" for c in WHERE_WE_BUILD)
    return f'<ul class="town-links">{items}</ul><p class="page-intro" style="margin-top:1rem">And across the Coachella Valley and High Desert.</p>'


def city_anchor(slug, name):
    """Link a published city name when that city has a page.

    Use this for service-area lists and menus. Location and NAP lines
    stay plain text; link_cities does not wrap those.
    """
    target = AREA_TARGET.get(name)
    if not target:
        return name
    here = ' aria-current="page"' if slug == target else ""
    return f'<a class="city-link" href="{href(slug, target)}"{here}>{name}</a>'


# Longest names first. "Joshua Tree Rustic" is a finish style, not the city.
_CITY_RE = re.compile(
    r"\b(Rancho Mirage|Indian Wells|Palm Springs|Palm Desert|Yucca Valley|Joshua Tree|La Quinta)\b(?! Rustic| National Park)"
)
# A city followed by ", CA" is the business locality (eyebrow, footer,
# contact address), not a service-area mention. "serves Joshua Tree, CA"
# is still about the area, so that one stays linked.
_LOCALITY_AFTER = re.compile(r",\s*(?:CA|California)\b", re.I)
_SERVES_BEFORE = re.compile(r"\b(?:serves|serving|serve)\s+$", re.I)
_WHERE_BASED_AFTER = re.compile(r"\s+is where\b", re.I)
_WHERE_BASED_BEFORE = re.compile(
    r"\b(?:based in|located in|location as|location:)\s*$", re.I
)
_SKIP_CITY_LINK = {
    "a", "h1", "h2", "h3", "h4", "h5", "h6",
    "script", "style", "title", "textarea", "button", "option",
}


def _is_base_location(data, start, end):
    """True when the city is where the business is based, not a service area."""
    before = data[max(0, start - 80):start]
    after = data[end:end + 24]
    if _LOCALITY_AFTER.match(after) and not _SERVES_BEFORE.search(before):
        return True
    if _WHERE_BASED_AFTER.match(after):
        return True
    if _WHERE_BASED_BEFORE.search(before):
        return True
    return False


class _CityLinker(HTMLParser):
    """Wrap published city names in body text when they name a service area.

    Skip headings, titles, meta attributes, scripts, text already inside a
    link, and locality lines (a city plus ", CA", "based in", or "location as").
    """

    def __init__(self, slug):
        super().__init__(convert_charrefs=False)
        self.slug = slug
        self.stack = []
        self.out = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        self.out.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack:
                if self.stack.pop() == tag:
                    break
        self.out.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.get_starttag_text())

    def handle_data(self, data):
        if any(tag in _SKIP_CITY_LINK for tag in self.stack):
            self.out.append(data)
        else:
            self.out.append(_CITY_RE.sub(self._repl, data))

    def handle_entityref(self, name):
        self.out.append(f"&{name};")

    def handle_charref(self, name):
        self.out.append(f"&#{name};")

    def handle_comment(self, data):
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")

    def _repl(self, match):
        if _is_base_location(match.string, match.start(), match.end()):
            return match.group(0)
        if AREA_TARGET.get(match.group(1)) == self.slug:
            return match.group(0)  # no self-links in body copy on the city's own page
        return city_anchor(self.slug, match.group(1))

    def result(self):
        return "".join(self.out)


def link_cities(html, slug):
    parser = _CityLinker(slug)
    parser.feed(html)
    parser.close()
    return parser.result()


def form_embed(form_id, title):
    """Standard GoHighLevel inline embed. form_embed.js resizes the iframe.

    data-height is only the fallback if that script cannot resize. The contact
    form is the tall one (fields through Submit). Guide forms are name and email.
    """
    # Pixel fallbacks measured from the live widgets (desktop and 390px),
    # rounded up so Submit stays in view if form_embed.js cannot resize.
    if form_id == CONTACT_FORM:
        kind, fallback = "contact", "1280"
    elif form_id == REFERRAL_FORM:
        kind, fallback = "referral", "2400"
    else:
        kind, fallback = "guide", "512"
    # data-layout uses single quotes, matching GoHighLevel's snippet.
    layout = "{'id':'INLINE'}"
    return f"""<div class="form-embed form-embed--{kind}">
  <iframe src="https://api.leadconnectorhq.com/widget/form/{form_id}" title="{title}" id="inline-{form_id}" data-layout="{layout}" data-trigger-type="alwaysShow" data-trigger-value="" data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" data-deactivation-value="" data-form-name="{title}" data-height="{fallback}" data-layout-iframe-id="inline-{form_id}" data-form-id="{form_id}" scrolling="no"></iframe>
</div>"""


def gallery(slug, images, caption_prefix, placeholder=""):
    p = prefix(slug)
    bits = []
    for i, (fn, w, h) in enumerate(images, 1):
        alt = f"{caption_prefix}, photograph {i}"
        bits.append(f"""<button class="gallery-item" type="button" data-caption="{alt}">
  <img src="{p}images/site/{fn}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
</button>""")
    return ph_comment(placeholder) + f'<div class="gallery-grid reveal"{ph(placeholder)}>' + "".join(bits) + "</div>"


PAGES_WRITTEN = []
# Kept out of sitemap.xml: ad landing pages (mirrors of the LP hub), thank-you
# and agreement pages.
SITEMAP_EXCLUDE = ("guides/", "guide-thank-you", "partners/referral-agreement", "opt-out-preferences")


def write_page(slug, html):
    PAGES_WRITTEN.append(slug)
    html = link_cities(html, slug)
    if slug:
        path = ROOT.joinpath(*[p for p in slug.split("/") if p], "index.html")
    else:
        path = ROOT / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(path.relative_to(ROOT))


def page_shell(slug, title, description, body, extra_ld=""):
    html = head(slug, title, description, extra_ld) + nav(slug) + '<main id="main">' + body + "</main>" + footer(slug)
    if "api.leadconnectorhq.com/widget/form/" in html:
        html = html.replace(
            "</body>",
            '<script src="https://link.msgsndr.com/js/form_embed.js"></script>\n</body>',
            1,
        )
    return html


def why_cards(items, reveal=False):
    bits = []
    for h, text in items:
        bits.append(f'<article class="why-us-card"><h3>{h}</h3><p>{text}</p></article>')
    return f'<div class="why-us-grid{" reveal" if reveal else ""}">' + "".join(bits) + "</div>"


# The four standards (Step 9/10), from the Yucca Valley page, updated per Step 2.
WHY_BUILD = [
    ("One crew, start to finish.", "Our in-house crew and the same vetted trade partners on every job. The team that breaks ground is the team that hands you the keys."),
    ("One price, not a maze of line items.", "Your proposal is one overall price to build, with separate allowances for the materials you select, never a confusing trade-by-trade breakdown."),
    ("Direct access to leadership.", "When you call, you hear back the same day, from Nick or your dedicated project manager, never a receptionist or voicemail box."),
    ("Third-generation craftsmanship.", "18 years in the desert, 100+ years of combined experience on our crew, and standards passed down over three generations."),
]
WHY_REMODEL = [
    ("One crew, start to finish.", "Our in-house crew and the same vetted trade partners on every job. The team that starts your remodel finishes it."),
    ("One price, not a maze of line items.", "One overall price to build, with separate allowances for the finishes you choose, never a confusing trade-by-trade breakdown."),
    ("Direct access to leadership.", "Reach out and hear back the same day, from Nick or your dedicated project manager, never a call center."),
    ("Third-generation craftsmanship.", "18 years in the desert, 100+ years of combined experience on our crew, and standards passed down over three generations."),
]
WHY_ADU = [
    ("One crew, start to finish.", "Our in-house crew and the same vetted trade partners, from groundbreaking to final walkthrough."),
    ("One price, not a maze of line items.", "One overall price to build, with separate allowances for your material selections."),
    ("Direct access to leadership.", "Same-day responses from Nick or your dedicated project manager."),
    ("Third-generation craftsmanship.", "18 years in the desert and 100+ years of combined experience, applied to your guest house the same way we apply it to a $5M home."),
]


def steps(items):
    bits = []
    for i, (h, text) in enumerate(items, 1):
        bits.append(f"""<li class="process-steps__item">
  <span class="process-steps__index">0{i}</span>
  <div><h4>{h}</h4><p>{text}</p></div>
</li>""")
    return '<ol class="process-steps">' + "".join(bits) + "</ol>"


# Step 8: the six steps, full text (Our Process page and service pages).
PROCESS = [
    ("Phone consultation", "We talk through your vision, property, timeline, and budget. If we're not the right fit, we'll tell you."),
    ("Site visit", "We walk the lot or the home with you: access, utilities, setbacks, and anything that will drive cost."),
    ("Design &amp; Pre-Construction Agreement", "A paid planning phase before any construction contract. We coordinate your architect and engineers and design, analyze the site, and price every major decision against your budget. This is where the Alturas and Cubero savings came from."),
    ("Your proposal", "One overall price to build, with separate allowances for the materials you select."),
    ("Build", "Our in-house crew and the same vetted trade partners on every job, with real-time photo updates through your client portal and bi-weekly field reports."),
    ("Keys and after", "Punch list, final clean, warranties, manuals, and documentation handed over together."),
]
# One line each, for the homepage (Step 4).
PROCESS_SHORT = [
    ("Phone consultation", "Your vision, property, timeline, and budget, and an honest answer on fit."),
    ("Site visit", "We walk the lot or home: access, utilities, setbacks, and cost drivers."),
    ("Design &amp; Pre-Construction Agreement", "A paid planning phase that prices every major decision before any construction contract."),
    ("Your proposal", "One overall price to build, with separate allowances for your selections."),
    ("Build", "Our in-house crew and vetted trade partners, with updates through your client portal."),
    ("Keys and after", "Punch list, final clean, warranties, manuals, and documentation, handed over together."),
]
PROCESS_REMODEL = PROCESS
PROCESS_ADU = PROCESS


def related(slug, links, primary_last=True):
    bits = []
    for i, (label, target) in enumerate(links):
        klass = "btn btn--primary" if (primary_last and i == len(links) - 1 and target == JOURNEY) else "btn btn--nav"
        bits.append(f'<a class="{klass}" href="{href(slug, target)}">{label}</a>')
    return '<div class="link-row">' + "".join(bits) + "</div>"


def write_sitemap():
    urls = []
    for slug in PAGES_WRITTEN:
        if any(slug.startswith(x) for x in SITEMAP_EXCLUDE):
            continue
        urls.append(f"  <url><loc>{canonical(slug)}</loc></url>")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    print("sitemap.xml", len(urls), "urls")


def main():
    import pages
    pages.build_all()
    # pages imports this file as the module "generate" (not __main__), so the
    # list of written pages lives on that module.
    pages.g.write_sitemap()


if __name__ == "__main__":
    main()
