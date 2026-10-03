"""Page bodies for the Distinct Designs website (v2, Oct 2026 change brief).

Imported by generate.py. Every "TODO(v2)" marks an open item from the brief:
placeholder photos, DRAFT copy for Nick to approve, and facts still to confirm.
"""

import re

import generate as g

H = g.hero
PH = g.page_hero
F = g.form_embed
Q = g.quotes_html
P = g.project_tiles
W = g.write_page
S = g.page_shell
R = g.related
FAQ = g.faq_html
STEPS = g.steps
WHY = g.why_cards
GAL = g.gallery
HREF = g.href
LD = g.faq_ld
TOWNS = g.town_links
REVIEWS = g.reviews_section
PHONE = g.PHONE_DISPLAY
TEL = g.PHONE_TEL
EMAIL = g.EMAIL
GUIDE = g.GUIDE_FORM
CONTACT = g.CONTACT_FORM
JOURNEY = g.JOURNEY
JL = g.JOURNEY_LABEL
LIC = g.LICENSE_EYEBROW

COVER_ALT = "The Ultimate Planning Guide: What It Really Takes to Build a $1M+ Custom Home in the Desert, by Nicholas Aguilar"

HOME_DESCRIPTION = "Luxury custom homes from $1M and whole-home remodels from $250K across the Coachella Valley and High Desert. Third-generation builder. CA Lic. #1145786."


def book(slug):
    return f"""<figure class="book">
  <img src="{g.prefix(slug)}images/site/planning-guide-cover.jpg" alt="{COVER_ALT}" width="1082" height="1400" loading="lazy">
</figure>"""


def journey_cta(slug, heading, text, image=None, guide=False):
    """Closing call to action: Start Your Journey button (plus the guide form on service pages)."""
    p = g.prefix(slug)
    if image:
        src, alt, w, h = image
        media = f'<div class="lead-section__media"><img src="{p}{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></div>'
    else:
        media = f'<div class="lead-section__media lead-section__media--book">{book(slug)}</div>'
    form = F(GUIDE, "Get the free planning guide") if guide else ""
    guide_line = '<p class="lead-section__note">Not ready to talk yet? Get the free Ultimate Planning Guide below.</p>' if guide else ""
    return f"""<section class="lead-section" id="form">
  {media}
  <div class="lead-section__content">
    <h2>{heading}</h2>
    <p>{text}</p>
    <div class="link-row" style="margin-top:1rem"><a class="btn btn--primary" href="{HREF(slug, JOURNEY)}">{JL}</a> <a class="btn btn--secondary" href="tel:{TEL}">Call {PHONE}</a></div>
    {guide_line}
    {form}
  </div>
</section>"""


def build_all():
    home()
    about()
    service_build()
    service_remodel()
    service_adu()
    our_process()
    projects()
    project_pages()
    start_your_journey()
    privacy()
    optout()
    planning()
    thanks()
    partners()
    referral()
    guides()
    service_areas()
    not_found()


SERVICE_CARDS = [
    ("Custom Homes", "services/custom-home-build",
     "Ground-up custom homes from $1M to $5M+. One team from design to handing you the keys, planned and priced before groundbreaking.",
     "View custom homes"),
    ("Luxury Remodels", "services/whole-home-remodel",
     "Whole-home remodels from $250K, planned and priced as one project and built by one crew.",
     "View luxury remodels"),
    ("Guest Houses &amp; ADUs", "services/custom-adu",
     "For properties that already have a home. Built to the standard of the house beside it.",
     "View guest houses"),
]


def service_cards(slug):
    bits = []
    for title, target, text, more in SERVICE_CARDS:
        bits.append(f"""<a class="service-card" href="{HREF(slug, target)}">
      <h3>{title}</h3>
      <p>{text}</p>
      <span class="service-card__more">{more}</span>
    </a>""")
    return '<div class="service-grid service-grid--three">' + "".join(bits) + "</div>"


CASE_LABELS = {
    "alturas": ("&ldquo;$200,000+ error caught before groundbreaking&rdquo;", "Alturas · Ground-up custom home"),
    "cubero": ("&ldquo;$177,000+ net savings in pre-construction&rdquo;", "Cubero · Ground-up custom home"),
    "hilltop": ("&ldquo;Their contractor vanished with $70,000. We finished it right.&rdquo;", "Hilltop · Rescue and completion"),
}


def home():
    slug = ""
    p = g.prefix(slug)
    guide_link = f'\n    <p class="hero__guide-link"><a href="#guide">Not ready to talk yet? Get the free Ultimate Planning Guide &rarr;</a></p>'
    body = H(
        slug,
        "images/site/Custom-Desert-Home.webp",
        "Cubero, a finished ground-up custom home by Distinct Designs, seen from above with its pool and desert landscape",
        1536, 1024, "",
        "Coachella Valley · High Desert",
        "Luxury Custom Homes &amp; Whole-Home Remodels",
        "Custom luxury homes from $1M to $5M+. Whole-home remodels from $250K. We don't build homes for everyone. We build signature homes for clients who refuse to settle.",
        HREF(slug, JOURNEY), JL,
        placeholder="Homepage hero: swap in the finished Cubero drone shot (current image is the existing Cubero aerial).",
        extra=guide_link,
    )
    body += f"""
<section class="section section--tinted" id="guide">
  <!-- Step 4: the guide link opens this GHL capture form, never the PDF. -->
  <div class="guide-layout">
    {book(slug)}
    <div class="guide-layout__copy">
      <p class="eyebrow">Free guide</p>
      <h2>Get your free guide. Know before you hire.</h2>
      <p class="page-intro">Two homes can be the same size, yet one costs $900K and the other $2.5M. Most builders never explain why.</p>
    </div>
    <div class="guide-layout__form reveal">{F(GUIDE, "Get your free planning guide")}</div>
  </div>
</section>
<section class="section" id="services">
  <div class="section__header"><h2>What we build</h2></div>
  {service_cards(slug)}
</section>
<section class="section section--tinted" id="who-we-build-for">
  <h2>Who we build for</h2>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>The right fit</h3><ul class="check-list">
      <li>New custom homes from $1M to $5M+.</li>
      <li>Whole-home remodels from $250K+.</li>
      <li>Guest houses and ADUs on established properties.</li>
      <li>Clients who want one team accountable from design to keys.</li>
    </ul></article>
    <article class="info-card"><h3>Not the right fit</h3><ul class="check-list check-list--muted">
      <li>Repairs, handyman work, or projects decided on the lowest bid.</li>
    </ul></article>
  </div>
</section>
<section class="section" id="case-studies">
  <div class="section__header">
    <h2>What the right builder catches</h2>
    <p>Three projects, three problems found before they became expensive.</p>
  </div>
  {P(slug, ["alturas", "cubero", "hilltop"], CASE_LABELS)}
</section>
<section class="section section--split section--tinted" id="now-building">
  <div>
    <p class="eyebrow">Now building</p>
    <h2>Alturas</h2>
    <p class="page-intro">A ground-up custom home, framed and moving.</p>
    <!-- TODO(v2): optional line "Ask us about walking an active build." Add only if Nick wants to offer tours. -->
    <div class="link-row"><a class="btn btn--nav" href="{HREF(slug, "projects/alturas")}">Read the Alturas story</a><a class="btn btn--primary" href="{HREF(slug, JOURNEY)}">{JL}</a></div>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/site/Alturas-build.jpg" alt="Alturas custom home under construction: framed and sheathed walls against a blue desert sky" width="800" height="533" loading="lazy">
  </div>
</section>
<section class="section" id="process">
  <div class="section__header">
    <h2>Our process</h2>
    <p>One team from first conversation to keys.</p>
  </div>
  {STEPS(g.PROCESS_SHORT)}
  <div class="link-row"><a class="btn btn--nav" href="{HREF(slug, "our-process")}">See the full process</a></div>
</section>
<section class="section section--split section--tinted" id="owner">
  <div>
    <p class="eyebrow">Owner</p>
    <h2>Nick Aguilar</h2>
    <!-- TODO(v2) DRAFT for Nick to approve: first-person owner note, written only from facts already on the site (third generation, Mario Trujillo, 18 years in the desert). -->
    <div class="prose" data-draft="owner-note">
      <p>I'm a third-generation builder. My grandfather, Mario Trujillo, a decorated Marine Corps Master Gunnery Sergeant, put me to work at 11 and taught me discipline, pride in craftsmanship, and to treat every project like it's my own.</p>
      <p>I've spent 18 years building in the desert, and those standards still guide every home we take on. We take on a limited number of projects each year, so you have direct access to me and our leadership from the first conversation to the day we hand you the keys.</p>
      <p><strong>Nick Aguilar</strong><br>Owner, Distinct Designs Construction</p>
    </div>
    <div class="link-row"><a class="btn btn--nav" href="{HREF(slug, "about")}">Meet the team</a></div>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/site/Nick-DD.jpg" alt="Nick Aguilar, owner of Distinct Designs Construction" width="800" height="1000" loading="lazy">
  </div>
</section>
{REVIEWS(g.HOME_QUOTES, tinted=False)}
<section class="section section--tinted" id="faq">
  <h2>Frequently asked questions</h2>
  {g.TIMELINE_TODO}
  {FAQ("home", g.HOME_FAQ)}
</section>
<section class="section" id="where-we-build">
  <h2>Where we build</h2>
  {TOWNS(slug)}
</section>
<section class="lead-section" id="form">
  <div class="lead-section__media">
    <img src="{p}images/process-crew-remodel.webp" alt="The Distinct Designs crew standing in front of a completed desert home under a clear blue sky" width="1200" height="1600" loading="lazy">
  </div>
  <div class="lead-section__content">
    <h2>Start your journey.</h2>
    <p>Tell us about your project. Every inquiry is reviewed personally, and you'll hear back the same day.</p>
    <!-- TODO(v2) GHL form builder (out of scope here): new fields per Step 11. See start-your-journey page for the full list. -->
    {F(CONTACT, "Start your journey")}
    <p class="lead-section__note">We'll be in touch the same day.</p>
  </div>
</section>
"""
    W(slug, S(slug,
              "Distinct Designs Construction · Luxury Custom Homes &amp; Remodels · Coachella Valley &amp; High Desert",
              HOME_DESCRIPTION,
              body, LD(g.HOME_FAQ)))


def service_build():
    slug = "services/custom-home-build"
    p = g.prefix(slug)
    body = H(
        slug, "images/site/Custom-Desert-Home.webp",
        "Cubero, a ground-up custom home by Distinct Designs Construction, seen from above",
        1536, 1024, "",
        LIC,
        "Luxury Custom Homes",
        "Ground-up custom homes from $1M to $5M+. One team from design to keys, a plan and price you can trust before you sign, and daily progress you can see, even from out of state.",
        HREF(slug, JOURNEY), JL, page=True,
    )
    body += f"""
<!-- Step 5: headline is "Luxury Custom Homes"; the town keywords live in the page title (Step 14). Revisit if SEO needs a town in the H1. -->
<section class="section">
  <h2>Two homes, same size, very different price tags</h2>
  <div class="prose">
    <p>Two custom homes can be nearly identical in square footage, and a million dollars apart in cost. Most builders never explain why until you're already committed.</p>
    <p>The difference isn't luck. It's decisions made months before the first shovel breaks ground, decisions most buyers never get to see until it's too late to change course.</p>
    <p>That's exactly what our <a href="{HREF(slug, "planning-guide")}">free planning guide</a> walks you through, before you ever sign with a builder.</p>
  </div>
</section>
<section class="section section--split section--tinted" id="process">
  <div>
    <h2>Planned and priced before groundbreaking</h2>
    <p>Every material, design detail, and architectural decision is priced against your budget before construction begins. The decisions that move cost get made on paper, not on the job site.</p>
    <h3 class="section--split__subhead">How it works</h3>
    {STEPS(g.PROCESS)}
    <p class="pull-line">You'll always know where your project stands, what it costs, and why, even if you're managing it from out of state.</p>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/process-crew-home.webp" alt="The Distinct Designs crew inside a completed custom home, desert mountains beyond the open sliders" width="1200" height="900" loading="lazy">
  </div>
</section>
<figure class="image-break"><img src="{p}images/process-break-terrace.webp" alt="Desert terrace at dusk with a fire bowl, string lights and a spa, valley lights beyond" width="1920" height="1081" loading="lazy"></figure>
<section class="section" id="projects">
  <div class="section__header">
    <h2>Signature homes we've built</h2>
    <p>Two ground-up custom homes, and what pre-construction caught on each.</p>
  </div>
  {P(slug, ["cubero", "alturas"])}
</section>
<section class="section section--tinted" id="why-us">
  <h2>Why serious buyers choose Distinct Designs</h2>
  {WHY(g.WHY_BUILD)}
</section>
<!-- TODO(v2): swap in custom-home reviews as they come in (Step 12). Homepage reviews used for now. -->
{REVIEWS(g.HOME_QUOTES, tinted=False)}
<section class="section section--tinted" id="faq">
  <h2>Custom home questions</h2>
  {g.TIMELINE_TODO}
  {FAQ("build", g.BUILD_FAQ)}
</section>
<section class="section" id="areas-served">
  <h2>Where we build custom homes</h2>
  {TOWNS(slug)}
  <p class="page-intro" style="margin-top:1.5rem">Adding a guest house to a property you already own? See <a href="{HREF(slug, "services/custom-adu")}">Guest Houses &amp; ADUs</a>.</p>
</section>
{journey_cta(slug, "Start your custom home journey", f"Building at this level is about trust, not the lowest bid. Talk to Nick directly about your project. No call center, no sales script.", guide=True)}
"""
    W(slug, S(slug,
              "Luxury Custom Home Builder · Coachella Valley &amp; High Desert · Distinct Designs",
              "Ground-up luxury custom homes from $1M to $5M+ across the Coachella Valley and High Desert. One team from design to keys, planned and priced before groundbreaking.",
              body, LD(g.BUILD_FAQ)))


def service_remodel():
    slug = "services/whole-home-remodel"
    p = g.prefix(slug)
    body = H(
        slug, "images/process-break-bath.webp",
        "Finished spa-level bathroom with a freestanding soaking tub, white tile and desert views",
        1920, 960, "",
        LIC,
        "Luxury Whole-Home Remodels",
        "Whole-home remodels from $250K, planned and priced as one project, built by one crew, with photo updates you can see from anywhere.",
        HREF(slug, JOURNEY), JL, page=True,
        placeholder="Luxury Remodels hero: a finished high-end remodel interior (replaces the kitchen with the mini-split).",
    )
    body += f"""
<section class="section">
  <h2>Most remodel budgets don't break. They get broken.</h2>
  <div class="prose">
    <p>Luxury remodels rarely blow up because of one big mistake. They blow up from dozens of small decisions nobody priced before demo started: a selection here, a structural surprise there, until the number you signed up for doesn't mean much anymore.</p>
    <p>That's the part most contractors never walk you through before you commit.</p>
    <p>Our <a href="{HREF(slug, "planning-guide")}">free planning guide</a> shows you exactly what separates a remodel that stays on budget from one that doesn't, before you sign with anyone.</p>
  </div>
</section>
<section class="section section--split section--tinted" id="process">
  <div>
    <h2>Every decision priced before the first wall comes down</h2>
    <p>Before a single wall comes down, we run a full design-to-budget process: every material, every design detail, and every structural question we can reasonably anticipate, priced against your budget in advance.</p>
    <h3 class="section--split__subhead">How it works</h3>
    {STEPS(g.PROCESS_REMODEL)}
    <p class="pull-line">You always know what's happening, what it costs, and why, even managing it from out of state.</p>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/process-crew-remodel.webp" alt="The Distinct Designs crew standing in front of a completed desert home under a clear blue sky" width="1200" height="1600" loading="lazy">
  </div>
</section>
<figure class="image-break"><img src="{p}images/process-break-terrace.webp" alt="Desert terrace at dusk with a fire bowl, string lights and a spa, valley lights beyond" width="1920" height="1081" loading="lazy"></figure>
<section class="section" id="scope">
  <h2>What a whole-home remodel covers</h2>
  <div class="prose">
    <p>The whole house, planned as one project: layout, structure, electrical and plumbing systems, finishes, kitchens, and primary suites. Every room is designed together, so the house reads as one home when we're done.</p>
    <p>We also take on a limited number of kitchen and primary-bath remodels each year when the scope and finish level are the right fit.</p>
  </div>
</section>
<section class="section section--tinted" id="projects">
  <div class="section__header"><h2>Signature remodels we've delivered</h2></div>
  {P(slug, ["la-mirada"], placeholders={"la-mirada": "La Mirada tile: reshoot pending (Step 13)."})}
</section>
<section class="section" id="why-us">
  <h2>Why serious homeowners choose Distinct Designs</h2>
  {WHY(g.WHY_REMODEL)}
</section>
{REVIEWS([g.Q_VICTORIA])}
<section class="section" id="faq">
  <h2>Remodel questions</h2>
  {FAQ("remodel", g.REMODEL_FAQ)}
</section>
<section class="section section--tinted" id="areas-served">
  <h2>Where we remodel</h2>
  {TOWNS(slug)}
</section>
{journey_cta(slug, "Start your remodel the right way", "A remodel at this level is about trust, not the lowest bid. Talk to Nick directly about your project.", guide=True)}
"""
    W(slug, S(slug,
              "Luxury Whole-Home Remodels · General Contractor · Distinct Designs",
              "Luxury whole-home remodels from $250K across the Coachella Valley and High Desert, planned and priced as one project and built by one in-house crew.",
              body, LD(g.REMODEL_FAQ)))


def service_adu():
    slug = "services/custom-adu"
    p = g.prefix(slug)
    body = H(
        slug, "images/project-cubero.webp",
        "Cubero, a ground-up custom home built by the same Distinct Designs team that builds guest houses and ADUs",
        900, 675, "",
        LIC,
        "Custom Guest Houses &amp; ADUs",
        "For properties that already have a home. A guest house or ADU built to the standard of the house beside it, by one crew, planned and priced before we start.",
        HREF(slug, JOURNEY), JL, page=True,
        placeholder="Guest Houses &amp; ADUs hero: a guest house or ADU we built (Cubero stands in; the garage photo stays off until confirmed).",
    )
    body += f"""
<section class="section">
  <h2>A guest house should look like it was always there.</h2>
  <div class="prose">
    <p>The difference between a guest house that belongs on the property and one that looks added on is planning: siting, utilities, permits, and matching the main home's materials. That's the part most builders skip.</p>
    <p>Our <a href="{HREF(slug, "planning-guide")}">free planning guide</a> shows you what to get right before you break ground.</p>
  </div>
</section>
<section class="section section--split section--tinted" id="process">
  <div>
    <h2>Planned and priced before we start</h2>
    <p>Before construction begins, every material, finish, and utility connection is priced against your budget, with the same discipline we bring to a full custom home. Built to the same standard as our custom homes.</p>
    <h3 class="section--split__subhead">How it works</h3>
    {STEPS(g.PROCESS_ADU)}
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/process-crew-adu.webp" alt="The Distinct Designs crew together inside a finished build, Joshua trees and desert mountains through the open sliders" width="1200" height="1600" loading="lazy">
  </div>
</section>
<section class="section" id="projects">
  <div class="section__header">
    <h2>Recent custom builds</h2>
    <p>Built by the same team.</p>
  </div>
  <!-- TODO(v2): show real guest house or ADU work when available. Cubero stands in, "Built by the same team" (Step 5). -->
  {P(slug, ["cubero"], {"cubero": ("Cubero", "Built by the same team")}, placeholders={"cubero": "ADU section: real guest house or ADU work when available."})}
</section>
<section class="section section--tinted" id="why-us">
  <h2>Why homeowners trust us with their guest house</h2>
  {WHY(g.WHY_ADU)}
</section>
<!-- TODO(v2): swap in a guest house or ADU review when one comes in. -->
{REVIEWS([g.Q_MYERS], tinted=False)}
<section class="section section--tinted" id="faq">
  <h2>Guest house and ADU questions</h2>
  {FAQ("adu", g.ADU_FAQ)}
</section>
<section class="section" id="areas-served">
  <h2>Where we build guest houses and ADUs</h2>
  {TOWNS(slug)}
</section>
{journey_cta(slug, "Plan your guest house the right way", "Talk to Nick directly about a guest house or ADU for the home you already love.", guide=True)}
"""
    W(slug, S(slug,
              "Custom Guest Houses &amp; ADUs · Distinct Designs",
              "Custom guest houses and ADUs for properties that already have a home, built to the standard of the house beside it, planned and priced before we start.",
              body, LD(g.ADU_FAQ)))


def our_process():
    slug = "our-process"
    p = g.prefix(slug)
    body = PH(slug, "images/site/dsc01975.jpg",
              "Alturas custom home under construction: framed and sheathed walls with arched openings under a clear desert sky",
              800, 533,
              LIC, "Our Process",
              "One team from first conversation to keys. Most of what protects your budget happens before the first shovel.")
    body += f"""
<section class="section">
  <div class="section__header">
    <h2>What Start Your Journey leads to</h2>
    <p>Six steps, the same on every project. The Design &amp; Pre-Construction Agreement is where the budget is protected.</p>
  </div>
  {STEPS(g.PROCESS)}
</section>
<section class="section section--tinted">
  <h2>How the work is done</h2>
  {WHY(g.WHY_BUILD)}
</section>
<section class="section">
  <h2>Ready when you are</h2>
  <p class="page-intro">Tell us about your project. Every inquiry is reviewed personally, and you'll hear back the same day.</p>
  {R(slug, [("Portfolio", "projects"), (JL, JOURNEY)])}
</section>
"""
    W(slug, S(slug,
              "Our Process: Design to Keys | Distinct Designs Construction",
              "How a Distinct Designs project runs: phone consultation, site visit, Design &amp; Pre-Construction Agreement, one-price proposal, build, and keys.",
              body))
LA_MIRADA_IMGS = [
    ("img_8659.jpg", 1200, 900),
    ("img_8662.jpg", 1200, 900),
    ("20231227_131415.jpg", 1200, 900),
    ("20231227_131555.jpg", 1200, 900),
    ("20231227_131611.jpg", 1200, 900),
    ("20231227_131709.jpg", 1200, 900),
    ("img_8658.jpg", 1200, 900),
]
HILLTOP_IMGS = [
    ("hilltop-01-7.webp", 1440, 1080),
    ("hilltop-01-6.webp", 1440, 1080),
    ("hilltop-01-4.webp", 1440, 1080),
    ("hilltop-01-5.webp", 1440, 1080),
    ("hilltop-01-3.webp", 1440, 1080),
    ("hilltop-01-1-2.webp", 1440, 1080),
    ("hilltop-01-2.webp", 1440, 1080),
]
CUBERO_IMGS = [
    ("Custom-Desert-Home.webp", 1536, 1024),
    ("living-room.jpg", 1200, 800),
    ("kitchen.jpg", 1200, 800),
    ("DSC00366-HDR-scaled.jpg", 1600, 1066),
    ("cubero-bathroom.jpg", 1200, 800),
    ("Garage.jpg", 1200, 800),
]
ALTURAS_IMGS = [
    ("Alturas-build.jpg", 1400, 900),
    ("dsc01975.jpg", 1200, 800),
    ("dsc01973.webp", 800, 1200),
    ("dsc01970.jpg", 1200, 800),
    ("dsc01971.jpg", 1200, 800),
    ("dsc02051.jpg", 1200, 800),
    ("dsc02013.jpg", 1200, 800),
    ("dsc02002.jpg", 1200, 800),
]


# TODO(v2): living-room.jpg (wood beams, desert view) is off the Cubero gallery
# until Nick confirms it is a home we built (if it is a rendering, label it).
# TODO(v2): Garage.jpg (the garage with the car) is off until Nick confirms we built it (Step 5).
CUBERO_IMGS = [im for im in CUBERO_IMGS if im[0] not in ("living-room.jpg", "Garage.jpg")]


def projects():
    slug = "projects"
    body = PH(slug, "images/site/Custom-Desert-Home.webp",
              "Cubero, a ground-up custom home by Distinct Designs Construction, seen from above",
              1536, 1024, "Portfolio", "Portfolio", "Signature builds and remodels.")
    body += f"""
<section class="section">
  <h2>Signature builds and remodels</h2>
  {P(slug, ["cubero", "alturas", "hilltop"])}
  <!-- TODO(v2): add La Mirada back after the reshoot. Sun Mesa stays off until it has real photos (its page redirects here for now). -->
</section>
<section class="section section--tinted">
  <h2>Start your project</h2>
  <p class="page-intro">Every project here started with a conversation. Tell us about yours.</p>
  {R(slug, [("Our Process", "our-process"), (JL, JOURNEY)])}
</section>
"""
    W(slug, S(slug,
              "Portfolio: Custom Homes &amp; Remodels | Distinct Designs",
              "Signature builds and remodels by Distinct Designs Construction: the Cubero custom home, Alturas (now building), and the Hilltop rescue and completion.",
              body))


def case_study(slug, title, meta, h1, h2, kicker, headline, place, stat_label, stat, stage_label, stage, paragraphs, lesson, images, image_prefix, hero_img=None, placeholder="", gallery_note=""):
    p = g.prefix(slug)
    paras = "".join(f"<p>{t}</p>" for t in paragraphs)
    himg = hero_img or (f"images/site/{images[0][0]}", images[0][1], images[0][2], f"{image_prefix}, photograph 1")
    body = PH(slug, himg[0], himg[3], himg[1], himg[2], "Portfolio", h1, placeholder=placeholder)
    body += f"""
<section class="section">
  <p class="eyebrow">{kicker}</p>
  <h2>{headline}</h2>
  <p class="page-intro">{place}</p>
  <div class="stat-row" style="margin-top:1.5rem">
    <article class="stat-card"><small>{stat_label}</small><span>{stat}</span></article>
    <article class="stat-card"><small>{stage_label}</small><span>{stage}</span></article>
  </div>
  <div class="prose" style="margin-top:2rem">{paras}<h3>The lesson</h3><blockquote><p>{lesson}</p></blockquote></div>
</section>
<section class="section section--tinted">
  <h2>{h2}</h2>
  {GAL(slug, images, image_prefix, gallery_note)}
  {R(slug, [("Portfolio", "projects"), ("Custom Homes", "services/custom-home-build"), ("Luxury Remodels", "services/whole-home-remodel"), (JL, JOURNEY)])}
</section>
"""
    W(slug, S(slug, title, meta, body))


def project_pages():
    case_study(
        "projects/la-mirada",
        "La Mirada Luxury Renovation | Distinct Designs Construction",
        "La Mirada luxury renovation by Distinct Designs Construction. A hidden cloth-wiring fire risk was replaced with a full rewire before the finishes went in.",
        "La Mirada – Luxury Renovation",
        "La Mirada photographs",
        "Luxury renovation | Electrical safety",
        "The previous owner's electrical system was a fire waiting to happen. We caught it before it did.",
        "La Mirada project · Southern California",
        "Risk eliminated", "Fire hazard",
        "System replaced", "Full rewire",
        [
            "These clients hired us for a high-end renovation. Before we touched a single finish, our preconstruction walkthrough revealed something that no amount of beautiful tile or custom cabinetry could fix: the home was running on cloth wiring, an aging electrical system that presents a hidden and serious fire risk.",
            "Unlike a modern breaker that trips when it is overloaded, cloth wiring deteriorates silently. The insulation degrades from the inside out through a process called thermal degradation, overheating repeatedly over years without triggering any warning. There is no alarm, no tripped breaker, no early sign until there is a fire.",
            "It is not a question of if. It is a question of when.",
            "We removed the system entirely and rewired the home to current code, protecting our clients' investment, their property, and most importantly, their family. The renovation they came to us for was delivered in full, with the peace of mind that comes from knowing the home beneath the finishes is as sound as everything visible in it.",
        ],
        "A renovation that looks exceptional but hides a compromised system is not a finished home. It is a liability waiting to surface. We don't just build beautiful spaces. We make sure everything behind the walls earns the same standard as what's in front of them.",
        LA_MIRADA_IMGS, "La Mirada renovation",
        hero_img=("images/project-la-mirada.webp", 900, 1200, "La Mirada renovation: open-plan kitchen and living area with marble island, brass pendants and oak floors"),
        placeholder="La Mirada hero: reshoot pending (current photos are phone shots).",
        gallery_note="La Mirada gallery: replace the phone shots after the reshoot (Step 13).",
    )
    case_study(
        "projects/hilltop",
        "Hilltop Rescue and Completion | Distinct Designs",
        "Hilltop build in the High Desert. Distinct Designs replaced out-of-code electrical and underspanned structural framing after another contractor left with $70,000.",
        "Hilltop – Rescue and Completion",
        "Hilltop photographs",
        "Rescue and completion | Structural and electrical",
        "Their contractor vanished with $70,000. We came in, made it safe, and finished it right.",
        "Hilltop build · High Desert, CA",
        "Contractor fraud", "$70,000",
        "Hazards remediated", "Structural + fire",
        [
            "These clients called us after their contractor had all but disappeared, showing up one week a month for two months while collecting payments in full. By the time they reached us, they had already lost $70,000 and had no idea what, if anything, had been done correctly.",
            "Our on-site assessment revealed two serious and interconnected problems. The first was the electrical: a significant portion of it had been installed out of compliance with code standards and had to be fully removed and rerun. The second was more alarming: the load-bearing framing and structural beams had been installed incorrectly relative to the engineering specifications. They were underspanned for the load they were meant to carry, a condition that, left unaddressed, creates real risk of roof failure over time.",
            "We remediated both issues completely, brought every system into full compliance, and delivered the finished home our clients had originally envisioned, but now built to the standard that actually keeps a family safe. The decision to stop and call us, rather than continue with a contractor who had already proven he couldn't be trusted, saved them from a far more costly outcome down the road.",
            "We never want to be your second call. But if you need one, we will not leave until it is right.",
        ],
        "A low bid doesn't protect your investment. It shifts the risk onto you. When a contractor disappears or cuts corners, the liability stays with the homeowner. The right builder is the one who isn't trying to win your project on price.",
        HILLTOP_IMGS, "Hilltop build",
        hero_img=("images/site/hilltop-01-2.webp", 1440, 1080, "Hilltop terrace at dusk with a fire bowl, string lights and a spa, valley lights beyond"),
        placeholder="Hilltop hero: confirm the strongest finished Hilltop photo (the kitchen with the mini-split is off the hero).",
    )
    case_study(
        "projects/cubero",
        "Cubero Ground-Up Custom Home | Distinct Designs Construction",
        "Cubero ground-up custom home in the High Desert. Pre-construction site analysis avoided Joshua tree relocation, major regrading, and a $58,000 well.",
        "Cubero – Ground-Up Custom Home",
        "Cubero photographs",
        "Ground-up new build | Site analysis and planning",
        "They thought they needed a well. We found a better path and saved them $177,000.",
        "Cubero build · High Desert, CA",
        "Net savings", "$177,000+",
        "Stage", "Pre-construction",
        [
            "These clients had already purchased their land and were ready to build. They came to us with a site plan, a vision, and the assumption that the heavy decisions had already been made. Within the first phase of our preconstruction process, we identified three costly assumptions that would have derailed the project, before a single permit had been filed.",
            "The planned building location required the relocation of protected Joshua trees, a process that would have cost over $90,000 alone, and necessitated regrading more than half of the five-acre parcel to accommodate the natural water channels running through the property. That regrading cost: over $150,000.",
            "Neither had been factored into the budget. Neither had been caught by anyone prior to our involvement. By conducting a comprehensive site analysis, we identified an alternate building location that offered superior views, eliminated the need for any tree relocation, and worked with the natural topography of the land rather than against it. The project moved forward on schedule and within budget, because the right questions were asked before the expensive decisions were locked in.",
            "We also resolved a utility challenge the clients had resigned themselves to: they believed a $58,000 well was their only option for water access. After analyzing the property and surrounding easement rights, we determined a water line connection was achievable for half that cost. No well required.",
            "After the site work the new location did require, their net savings came to more than $177,000.",
        ],
        "What you don't know before you build will cost you. Our preconstruction process exists for one reason: to ensure that every dollar you commit is being spent on the right decision, in the right location, for the right reasons.",
        CUBERO_IMGS, "Cubero build",
    )
    case_study(
        "projects/alturas",
        "Alturas Custom Home, Now Building | Distinct Designs",
        "Alturas custom home in the High Desert, now building. A pre-construction review caught a setback error and a septic conflict before demolition-level cost.",
        "Alturas – Ground-Up Custom Home",
        "Alturas photographs",
        "Now building | Design phase oversight",
        "We found a $200,000+ error before a single shovel hit the ground.",
        "Alturas build · High Desert, CA",
        "Losses prevented", "$200,000+",
        "Stage caught", "Pre-construction",
        [
            "Our clients came to us mid-process, frustrated by delays and a build that had stalled. What we uncovered when we stepped in went far beyond a scheduling problem. It was a mistake that would have eventually forced a demolition.",
            "The home had been positioned incorrectly on the architectural plans. The property lines had never been surveyed before the architect placed the structure, meaning the home as drawn was in direct violation of county setback requirements. Had this gone undetected, the building department would have eventually caught it, at whatever phase construction had reached, requiring a complete teardown and restart at devastating cost. We identified the error during our preconstruction review, corrected the placement, and kept the project moving forward without losing a dollar to avoidable demolition.",
            "We also discovered the septic tank had been positioned directly adjacent to the planned pool location. Drawing on our knowledge of how heavy equipment operates and what future site access demands, we relocated it to an optimal position, one that allowed pool construction to proceed unimpeded once the home was complete.",
            "This is precisely why involving a contractor during the design phase, before plans are finalized and submitted, is one of the highest-leverage decisions a client at this level can make. Our fee before groundbreaking is a fraction of what a single overlooked error in this phase can produce.",
        ],
        "The most expensive contractor mistake doesn't happen on the job site. It happens before anyone shows up. The right eyes in the design phase protect hundreds of thousands of dollars that most clients don't even know are at risk.",
        ALTURAS_IMGS, "Alturas build",
        hero_img=("images/site/Alturas-build.jpg", 800, 533, "Alturas custom home framed and sheathed against a blue desert sky"),
    )
    # Sun Mesa: not generated in v2 (it duplicated Hilltop's copy with La Mirada's
    # photos). /projects/sun-mesa/ redirects to /projects/ in vercel.json.


def about():
    slug = "about"
    p = g.prefix(slug)
    body = f"""
<header class="hero hero--page hero--team">
  <img class="hero__image" src="{p}images/process-crew-home.webp" alt="The Distinct Designs crew inside a completed custom home, desert mountains beyond the open sliders" width="1200" height="900" fetchpriority="high" loading="eager">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">About Distinct Designs</p>
    <h1>Three generations. One standard.</h1>
    <p class="subhead">18 years building in the desert. 100+ years of combined experience on our crew.</p>
  </div>
</header>
<section class="section">
  <h2>Dedication to my grandfather, Mario Trujillo</h2>
  <div class="portrait-row reveal" style="margin:1.5rem 0">
    <img src="{p}images/site/Mario-Trulillo-old-school-2.jpg" alt="Mario Trujillo, earlier in his career" width="900" height="1100" loading="lazy">
    <img src="{p}images/site/Mario-Trulillo.jpg" alt="Mario Trujillo" width="900" height="1100" loading="lazy">
  </div>
  <div class="prose">
    <p>Mario Trujillo, a decorated war veteran and Master Gunnery Sergeant of the United States Marine Corps, laid the foundation upon which Distinct Designs Construction was built. He upheld principles of hard work, diligence, adaptability, and treating every employee like family. These standards continue to guide our company today.</p>
    <p>Every one of us at Distinct Designs Construction has been shaped and influenced by Mr. Trujillo's leadership, whether through direct mentorship or through the guidance passed down from those he mentored. His values and craftsmanship became the blueprint that continues to branch throughout the company, instilling integrity, diligence, and a commitment to building quality from the ground up.</p>
    <p>Mr. Trujillo taught us the importance of working hard, taking pride in our craft, going the extra mile, and never settling for anything less than excellence. But more than that, he built a culture rooted in loyalty, mutual respect, and a shared commitment to high standards, where every project was approached with the same diligence to excellence.</p>
    <p>He didn't just take us on as employees, he mentored us as young adults and molded us into men. His dedication went beyond teaching skills; it was about building character and passing down values that would endure. His legacy of excellence continues to shape Distinct Designs Construction.</p>
    <p>Mr. Trujillo laid the concrete foundation and paved the road for Distinct Designs Construction to thrive. His mentorship, diligence, and relentless pursuit of excellence continue to be the backbone of our success. We are forever grateful for his guidance, vision, and commitment to nurturing both our skills and our character.</p>
    <p>Thank you, Mario Trujillo, for everything you have done. Your unwavering dedication and wisdom have built more than just a company, you have built a family. Distinct Designs Construction stands strong today because of the foundation you laid. We will honor you by carrying your legacy forward through the principles and values you instilled in all of us.</p>
  </div>
</section>
<section class="section section--split section--tinted">
  <div>
    <h2>What we build</h2>
    <p>We build luxury custom homes, whole-home remodels, and guest houses across the Coachella Valley and High Desert. We take on a limited number of projects each year, so every one gets our full attention.</p>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/site/Team-Distinct-Designs-768x576.jpg" alt="The Distinct Designs Construction team on a finished job site" width="768" height="576" loading="lazy">
  </div>
</section>
<section class="section">
  <div class="card-grid">
    <article class="info-card"><h3>Our team</h3><p>100+ years of combined experience, with in-house specialists from structure to custom cabinetry.</p></article>
    <article class="info-card"><h3>Our standard</h3><p>One team accountable from design to keys.</p></article>
    <article class="info-card"><h3>Our vision</h3><p>Long-lasting relationships with clients who trust us to exceed their expectations and take care of them like family.</p></article>
  </div>
</section>
<section class="section section--tinted" id="team">
  <div class="section__header"><h2>Leadership</h2></div>
  <!-- TODO(v2): leadership placeholders. Need names, titles, and headshots for the project manager and office leadership (Step 9). -->
  <div class="team-grid team-grid--leadership">
    <article class="team-card"><img src="{p}images/site/Nick-DD.jpg" alt="Nick Aguilar, owner of Distinct Designs Construction" width="600" height="700" loading="lazy"><h3>Nick Aguilar</h3><p>Owner</p></article>
    <article class="team-card team-card--placeholder"><div class="team-card__photo"{g.ph("Leadership headshot: project manager")} role="img" aria-label="Headshot coming soon"></div><h3>Project Manager</h3><p>Name and headshot to come</p></article>
    <article class="team-card team-card--placeholder"><div class="team-card__photo"{g.ph("Leadership headshot: office leadership")} role="img" aria-label="Headshot coming soon"></div><h3>Office Leadership</h3><p>Name and headshot to come</p></article>
  </div>
  <h3 class="team-subhead">In-house craftsmen</h3>
  <div class="team-grid">
    <article class="team-card"><img src="{p}images/site/eric-pancho-2-2.jpg" alt="Eric, custom cabinet and door specialist" width="600" height="700" loading="lazy"><h3>Eric</h3><p>Cabinet and door specialist</p></article>
    <article class="team-card"><img src="{p}images/site/jerry-spider-1.jpg" alt="Jerry, in-house demo and plumbing specialist" width="600" height="700" loading="lazy"><h3>Jerry</h3><p>In-house demo and plumbing specialist</p></article>
    <article class="team-card"><img src="{p}images/site/pops32.jpg" alt="Joel, tile and stone designer and installer" width="600" height="700" loading="lazy"><h3>Joel</h3><p>Tile and stone designer and installer</p></article>
    <article class="team-card"><img src="{p}images/site/randy-hoher-drywall-and-paint-specialist-02.jpg" alt="Randy, drywall and paint specialist" width="600" height="700" loading="lazy"><h3>Randy</h3><p>Drywall and paint specialist</p></article>
    <article class="team-card"><img src="{p}images/site/fredo.jpg" alt="Fredo, general lead tile and stone installer" width="600" height="700" loading="lazy"><h3>Fredo</h3><p>General lead tile and stone installer</p></article>
    <article class="team-card"><img src="{p}images/site/Travis-Vanzee.jpg" alt="Travis Vanzee, electrician" width="600" height="700" loading="lazy"><h3>Travis</h3><p>Electrician specialist</p></article>
  </div>
</section>
<section class="section">
  <h2>Our standards</h2>
  {WHY(g.WHY_BUILD)}
  {R(slug, [("Our Process", "our-process"), ("Portfolio", "projects"), (JL, JOURNEY)])}
</section>
"""
    W(slug, S(slug,
              "About Distinct Designs Construction | Three Generations",
              "Three generations, one standard. Meet Nick Aguilar and the Distinct Designs team: 18 years building in the desert, 100+ years of combined crew experience.",
              body))


def start_your_journey():
    slug = JOURNEY
    p = g.prefix(slug)
    body = PH(slug, "images/process-crew-home.webp",
              "The Distinct Designs crew inside a completed custom home, desert mountains beyond the open sliders",
              1200, 900, LIC, "Start Your Journey",
              "Tell us about your project. Every inquiry is reviewed personally, and you'll hear back the same day.")
    body += f"""
<section class="section" id="form">
  <div class="two-col journey-layout">
    <div>
      <h2>Contact details</h2>
      <h3>Phone</h3>
      <p><a href="tel:{TEL}">{PHONE}</a></p>
      <h3>Email</h3>
      <!-- TODO(v2): email must reach Nick directly and sync into GHL. Keep the Gmail or switch to nick@distinctdesignspro.com (Nick to decide). -->
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <h3>Location</h3>
      <p>{g.LOCATION}</p>
      <h3>License</h3>
      <p>CA Lic. #1145786</p>
      <p style="margin-top:1.5rem">Instagram: <a href="https://www.instagram.com/distinctdesignsconst/">@distinctdesignsconst</a><br>
      Facebook: <a href="https://www.facebook.com/profile.php?id=61561101665757">Distinct Designs</a><br>
      Yelp: <a href="https://www.yelp.com/biz/distinct-designs-yucca-valley-6">Distinct Designs, Yucca Valley</a></p>
    </div>
    <div>
      <h2>Tell us about your project</h2>
      <!--
        TODO(v2) GHL FORM BUILDER (out of scope for this repo; edit the form in GHL so it keeps feeding the CRM).
        Step 11 spec:
          - First name, last name, phone, email: required
          - Project type: New custom home ($1M+) · Whole-home remodel ($250K+) · Guest house or ADU · Kitchen or bath remodel · Other
          - Investment range: Under $250K · $250K–$800K · $800K–$1.5M · $1.5M–$3M · $3M-5M+
            (Orion, Oct 3: custom homes start at $1M, so the first custom-home band should start at $1M. Re-cut the bands in GHL.)
          - Timeline to start: 0–6 months · 6–12 months · 12–24 months · Just planning
          - Property: I own the lot · I own the home · In escrow · Still looking
          - City: text
          - How did you hear about us?: Google search · Google ad · Instagram · Facebook · Realtor · Architect or designer · Referral · Jobsite sign · Other
          - Message: text
          - Remove the current "Services Interest In" checkboxes
          - Submit button in brand gold (#c8ab72) instead of green
          - New submissions notify Nick directly
          - Tag "Kitchen or bath remodel" inquiries in GHL (take them when the crew has an opening, without advertising them)
          - If the onboarding workflow branches on the old checkboxes, update it at the same time
          - Submit a test before launch (Step 14)
      -->
      {F(CONTACT, "Start your journey with Distinct Designs Construction")}
      <p class="form-note">We'll be in touch the same day.</p>
    </div>
  </div>
</section>
"""
    W(slug, S(slug,
              "Start Your Journey | Distinct Designs Construction",
              "Start your custom home, whole-home remodel, or guest house project with Distinct Designs Construction. Every inquiry is reviewed personally. Call (760) 221-4290.",
              body))


def not_found():
    """Branded 404 (Vercel serves /404.html with HTTP 404)."""
    body = f"""
<section class="section">
  <p class="eyebrow">Page not found</p>
  <h1>This page has moved</h1>
  <p class="page-intro">The page you're looking for isn't here. Try one of these instead.</p>
  {R("", [("Custom Homes", "services/custom-home-build"), ("Luxury Remodels", "services/whole-home-remodel"), ("Portfolio", "projects"), (JL, JOURNEY)])}
</section>
"""
    html = S("", "Page Not Found | Distinct Designs Construction",
             "The page you were looking for is not on the Distinct Designs Construction site. Explore custom homes, luxury remodels, and our portfolio.", body)
    html = g.link_cities(html, "")
    # Served at any missing URL, so make every local path root-absolute and drop the canonical.
    html = re.sub(r'(href|src)="(?!https?:|tel:|mailto:|#|/|data:)(\./)?', r'\1="/', html)
    html = re.sub(r'<link rel="canonical"[^>]*>\n?', "", html)
    (g.ROOT / "404.html").write_text(html, encoding="utf-8")
    print("404.html")


# Step 10 city pages. Intros and "Building in" sections are DRAFT copy for Nick
# to approve. They use general, public knowledge about each town plus facts
# already on the site (Cubero, Alturas, Hilltop). They do not claim projects,
# addresses, or counts in a town that the site does not publish.
CITY_PAGES = [
    {
        "slug": "service-areas/palm-springs", "name": "Palm Springs", "region": "Coachella Valley",
        "hero": ("images/site/hilltop-01-4.webp", "Finished primary bath with a freestanding tub, sunken soaking tub, and desert light through tall windows", 1440, 1080),
        "hero_ph": "Palm Springs hero: a finished Palm Springs or low-desert home (Step 13). No Joshua trees.",
        "intro": [
            "Palm Springs homes carry a design legacy few towns can match: mid-century modern landmarks, Spanish Colonial estates in Old Las Palmas and the Movie Colony, and new builds tucked against the San Jacinto foothills. Buyers here want a home that respects that heritage and still lives like a modern house, with clean lines, indoor-outdoor living, and systems built for summer heat.",
            "Whether it's a ground-up custom home or a whole-home remodel of a classic, the work starts with a plan and a price you can trust before anything is built.",
        ],
        "building": [
            "Building at this level in Palm Springs usually means more review than buyers expect. Depending on the property, plans may go through city architectural review, historic-district or HOA design guidelines, and hillside and view rules on lots against the mountains.",
            "Remodels of older homes bring their own questions: original electrical and plumbing, single-pane glass, and additions that have to match the original architecture. We work through those items during pre-construction, so they're priced and planned before the first wall comes down.",
        ],
        "project": "cubero", "review": None,
    },
    {
        "slug": "service-areas/rancho-mirage", "name": "Rancho Mirage", "region": "Coachella Valley",
        "hero": ("images/site/hill-top-remodel-7.webp", "Spa-level bathroom with a freestanding tub, white tile walls, and open desert through floor-to-ceiling windows", 1440, 1080),
        "hero_ph": "Rancho Mirage hero: a finished Rancho Mirage or low-desert home (Step 13). No Joshua trees.",
        "intro": [
            "Rancho Mirage is country club living at its most established: gated communities around championship golf, estate lots with mountain and fairway views, and homes built for entertaining and long, quiet winters. Many buyers here are updating a 1970s or 1980s club home, or replacing it with something built for how they live now.",
            "Our role is to turn that vision into a plan and a price you can trust before anything is torn out or built.",
        ],
        "building": [
            "Most work in Rancho Mirage runs through a country club or HOA architectural committee before it reaches the city. Committees can set rules on height, rooflines, exterior colors and materials, setbacks from the course, contractor hours, and site access, and review can take weeks.",
            "We build those approvals into the schedule and the budget from day one, so a committee comment doesn't become a change order once the work has started.",
        ],
        "project": "alturas", "review": None,
    },
    {
        "slug": "service-areas/palm-desert", "name": "Palm Desert", "region": "Coachella Valley",
        "hero": ("images/site/DSC00366-HDR-scaled.jpg", "Finished walk-in shower with a stone pebble floor, floating vanity, vessel sink, and brushed-brass fixtures", 2560, 1700),
        "hero_ph": "Palm Desert hero: a finished Palm Desert or low-desert home (Step 13). No turf patio, no Joshua trees.",
        "intro": [
            "Palm Desert offers everything from hillside estates in the south foothills to gated golf communities and established neighborhoods close to El Paseo. Buyers here often want a full-time desert home with the space, finish level, and outdoor living of a resort, without the maintenance headaches.",
            "Whether you're building on a hillside lot or reworking a home you already own, we plan and price every major decision before construction begins.",
        ],
        "building": [
            "Building in Palm Desert can involve city design review, HOA or club architectural guidelines in gated communities, and hillside rules on grading, height, and views in the foothills.",
            "Desert sites also bring wind, sand, drainage, and extreme summer heat. We plan for them early: insulation, glazing, shade, and mechanical systems sized for the climate, so the home stays comfortable and the budget holds.",
        ],
        "project": "hilltop", "review": None,
    },
    {
        "slug": "service-areas/indian-wells", "name": "Indian Wells", "region": "Coachella Valley",
        "hero": ("images/site/hilltop-01-3.webp", "Finished bathroom with a freestanding tub, rattan cabinet, and desert mountains through tall windows", 1440, 1080),
        "hero_ph": "Indian Wells hero: a finished Indian Wells or low-desert home (Step 13). No Joshua trees.",
        "intro": [
            "Indian Wells is one of the most exclusive addresses in the Coachella Valley: a small city of gated communities, golf and tennis clubs, and estate homes with long mountain views. Buyers here expect a resort-level finish and a builder who handles the details without being asked.",
            "We take on a limited number of projects each year, so a custom home or remodel in Indian Wells gets our full attention from design to keys.",
        ],
        "building": [
            "Nearly every project in Indian Wells sits inside a gated community, which means club or HOA architectural review in addition to city plan review. Expect standards for massing, rooflines, materials, landscaping, and construction hours, plus coordination with the gate for every delivery and trade.",
            "We work through those requirements during pre-construction and price them in, so approvals and access are handled before the build starts.",
        ],
        "project": "cubero", "review": None,
    },
    {
        "slug": "service-areas/la-quinta", "name": "La Quinta", "region": "Coachella Valley",
        "hero": ("images/project-la-mirada.webp", "Renovated open-plan kitchen and living area with a marble island, brass pendants, and oak floors", 900, 1200),
        "hero_ph": "La Quinta hero: a finished La Quinta or low-desert home (Step 13). No Joshua trees.",
        "intro": [
            "La Quinta pairs some of the desert's most private golf communities with the Santa Rosa Mountains rising right behind them. From the Cove's hillside streets to gated club estates, buyers here want homes that frame the mountains and handle serious entertaining.",
            "Whether you're building new or remodeling a home you already own, we plan and price every decision before construction begins.",
        ],
        "building": [
            "Projects in La Quinta often need both city review and a club or HOA architectural committee. Lots near the mountains can bring hillside rules, view corridors, and rock or grading work that has to be understood before design is final.",
            "Our pre-construction process looks at the site, the approvals, and the access early, so the budget reflects what the property actually needs.",
        ],
        "project": "alturas", "review": None,
    },
    {
        "slug": "service-areas/yucca-valley", "name": "Yucca Valley", "region": "High Desert",
        "hero": ("images/project-alturas.webp", "Alturas custom home in progress: sheathed walls with a circular window opening, against the desert and mountains", 1400, 932),
        "hero_ph": "Yucca Valley hero: a finished Yucca Valley home (Step 13). Alturas, now building, stands in.",
        "intro": [
            "Yucca Valley is home base. We've spent 18 years building in the High Desert, and this is where our crew lives and works. Buyers here want room to breathe: acreage, big skies, and homes that sit naturally on the land instead of fighting it.",
            "From ground-up custom homes on raw parcels to whole-home remodels and guest houses, we know these lots and what they take.",
        ],
        "building": [
            "High Desert lots come with conditions the low desert rarely has. Protected western Joshua trees can limit where a home can go and add real cost if they need to be relocated. Many parcels need a well or a long utility run for water, a septic system sized and placed correctly, and a plan for the washes and natural water channels that cross the land.",
            "On our Cubero build, a site analysis moved the home to a better location, avoided over $90,000 in Joshua tree relocation and over $150,000 in regrading, and replaced a planned $58,000 well with a water line at half that cost. That's the kind of planning we do before anything is built.",
        ],
        "project": "cubero", "review": "katie",
    },
    {
        "slug": "service-areas/joshua-tree", "name": "Joshua Tree", "region": "High Desert",
        "hero": ("images/site/Custom-Desert-Home.webp", "Cubero, a ground-up custom home by Distinct Designs Construction, seen from above", 1536, 1024),
        "hero_ph": "",
        "intro": [
            "Joshua Tree draws people for the boulders, the dark skies, and the national park at its doorstep. Buyers here want homes that feel like part of the landscape: low profiles, big glass, and outdoor spaces made for long desert evenings.",
            "We build and remodel homes across the High Desert, and we plan and price every decision before construction begins.",
        ],
        "building": [
            "Building near the park means working with the land as it is. Western Joshua trees are protected, so where the home sits matters from the first site visit. Most parcels rely on septic, many need a well or a water line extension, and seasonal washes shape where you can build and how the site drains.",
            "Our Cubero project shows why it matters. Before a permit was filed, we found a building location that avoided relocating protected Joshua trees, worked with the natural water channels instead of regrading the parcel, and replaced a $58,000 well with a water line at half the cost.",
        ],
        "project": "alturas", "review": "benoit",
    },
]

CITY_REVIEWS = {"katie": g.Q_KATIE, "benoit": g.Q_BENOIT}


def service_areas():
    for page in CITY_PAGES:
        slug, name, region = page["slug"], page["name"], page["region"]
        img, alt, w, h = page["hero"]
        eyebrow = f"CA Lic. #1145786 · {region}"
        body = H(slug, img, alt, w, h, "", eyebrow,
                 f"Luxury Custom Homes &amp; Remodels in {name}",
                 "Custom homes from $1M and whole-home remodels from $250K. One team from design to keys.",
                 HREF(slug, JOURNEY), JL, page=True, placeholder=page["hero_ph"])
        intro = "".join(f"<p>{t}</p>" for t in page["intro"])
        building = "".join(f"<p>{t}</p>" for t in page["building"])
        key = page["project"]
        review = CITY_REVIEWS.get(page["review"])
        review_html = REVIEWS([review], tinted=False) if review else f"<!-- TODO(v2): no published review from {name} yet. Add one when it comes in (Step 10). -->"
        body += f"""
<section class="section">
  <!-- TODO(v2) DRAFT: {name} intro for Nick to approve (Step 10). -->
  <div class="prose" data-draft="city-intro">{intro}</div>
</section>
<section class="section section--tinted">
  <!-- TODO(v2) DRAFT: "Building in {name}" for Nick to approve. Confirm local review and site details. -->
  <h2>Building in {name}</h2>
  <div class="prose" data-draft="city-building">{building}</div>
</section>
<section class="section" id="services">
  <h2>What we build in {name}</h2>
  {service_cards(slug)}
</section>
<section class="section section--tinted" id="projects">
  <!-- TODO(v2): featured project. Swap in a {name} project when one is published. -->
  <div class="section__header"><h2>Featured project</h2></div>
  {P(slug, [key], {key: CASE_LABELS[key]})}
</section>
{review_html}
<section class="section{"" if review else ""}" id="why-us">
  <h2>How the work is done</h2>
  {WHY(g.WHY_BUILD)}
</section>
{journey_cta(slug, f"Start your {name} project", "Tell us about your project. Every inquiry is reviewed personally, and you'll hear back the same day.")}
"""
        W(slug, S(slug,
                  f"Luxury Custom Homes &amp; Remodels in {name} · Distinct Designs",
                  f"Luxury custom homes from $1M and whole-home remodels from $250K in {name}, CA. One team from design to keys, planned and priced before construction.",
                  body))


def privacy():
    slug = "privacy-policy"
    body = f"""
<section class="section prose">
  <h1>Privacy policy</h1>
  <h2>Who we are</h2>
  <p>Our website address is: https://distinctdesignsconstruction.com.</p>
  <h2>Comments</h2>
  <p>When visitors leave comments on the site we collect the data shown in the comments form, and also the visitor's IP address and browser user agent string to help spam detection.</p>
  <p>An anonymized string created from your email address (also called a hash) may be provided to the Gravatar service to see if you are using it. The Gravatar service privacy policy is available here: https://automattic.com/privacy/. After approval of your comment, your profile picture is visible to the public in the context of your comment.</p>
  <h2>Media</h2>
  <p>If you upload images to the website, you should avoid uploading images with embedded location data (EXIF GPS) included. Visitors to the website can download and extract any location data from images on the website.</p>
  <h2>Cookies</h2>
  <p>Do we use cookies and other tracking technologies?</p>
  <p>In short: we may use cookies and other tracking technologies to collect and store your information.</p>
  <p>We may use cookies and similar tracking technologies (like web beacons and pixels) to gather information when you interact with our Services. Some online tracking technologies help us maintain the security of our Services, prevent crashes, fix bugs, save your preferences, and assist with basic site functions.</p>
  <p>We also permit third parties and service providers to use online tracking technologies on our Services for analytics and advertising, including to help manage and display advertisements, to tailor advertisements to your interests, or to send abandoned shopping cart reminders (depending on your communication preferences). The third parties and service providers use their technology to provide advertising about products and services tailored to your interests which may appear either on our Services or on other websites.</p>
  <p>To the extent these online tracking technologies are deemed to be a "sale"/"sharing" (which includes targeted advertising, as defined under the applicable laws) under applicable US state laws, you can opt out of these online tracking technologies by submitting a request as described below.</p>
  <p>Specific information about how we use such technologies and how you can refuse certain cookies is set out in our Cookie Notice.</p>
  <h3>Google Analytics</h3>
  <p>We may share your information with Google Analytics to track and analyze the use of the Services.</p>
  <p>To opt out of being tracked by Google Analytics across the Services, visit <a href="https://tools.google.com/dlpage/gaoptout">https://tools.google.com/dlpage/gaoptout</a>.</p>
  <p>For more information on the privacy practices of Google, please visit the <a href="https://policies.google.com/privacy">Google Privacy &amp; Terms page</a>.</p>
  <h2>Embedded content from other websites</h2>
  <p>Articles on this site may include embedded content (e.g. videos, images, articles, etc.). Embedded content from other websites behaves in the exact same way as if the visitor has visited the other website.</p>
  <p>These websites may collect data about you, use cookies, embed additional third-party tracking, and monitor your interaction with that embedded content, including tracking your interaction with the embedded content if you have an account and are logged in to that website.</p>
  <h2>Who we share your data with</h2>
  <p>If you request a password reset, your IP address will be included in the reset email.</p>
  <h2>How long we retain your data</h2>
  <p>If you leave a comment, the comment and its metadata are retained indefinitely. This is so we can recognize and approve any follow-up comments automatically instead of holding them in a moderation queue.</p>
  <p>For users that register on our website (if any), we also store the personal information they provide in their user profile. All users can see, edit, or delete their personal information at any time (except they cannot change their username). Website administrators can also see and edit that information.</p>
  <h2>What rights you have over your data</h2>
  <p>If you have an account on this site, or have left comments, you can request to receive an exported file of the personal data we hold about you, including any data you have provided to us. You can also request that we erase any personal data we hold about you. This does not include any data we are obliged to keep for administrative, legal, or security purposes.</p>
  <h2>Where your data is sent</h2>
  <p>Visitor comments may be checked through an automated spam detection service.</p>
  <p><a href="{HREF(slug, "opt-out-preferences")}">Opt-out preferences</a></p>
</section>
"""
    W(slug, S(slug,
              "Privacy Policy | Distinct Designs Construction",
              "Privacy policy for Distinct Designs Construction, including comments, media, cookies, Google Analytics, and the rights you have over your data.",
              body))


def optout():
    slug = "opt-out-preferences"
    body = f"""
<section class="section prose">
  <h1>Opt-out preferences</h1>
  <p>The current site's opt-out page is a cookie-statement placeholder. The rendered banner says:</p>
  <blockquote><p>We use cookies to enhance your browsing experience, serve personalised ads or content, and analyse our traffic. By clicking "Accept All", you consent to our use of cookies.</p></blockquote>
  <p>We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.</p>
  <!-- TODO: The live page only contains the shortcode [cmplz-document type="cookie-statement" region="us"]. Complianz did not render a full cookie statement in the page source. Paste the real Complianz cookie statement here before launch, and wire a consent banner. -->
  <p><strong>TODO:</strong> The full cookie statement from the current site did not render (it is a Complianz shortcode). Do not treat this page as a complete cookie policy until that statement is pasted in.</p>
  <p>Cookie categories named on the current banner: necessary, analytics, and advertisement.</p>
  <p>To opt out of Google Analytics, visit <a href="https://tools.google.com/dlpage/gaoptout">https://tools.google.com/dlpage/gaoptout</a>.</p>
  <p>Read the <a href="{HREF(slug, "privacy-policy")}">privacy policy</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</section>
"""
    W(slug, S(slug,
              "Opt-out Preferences | Distinct Designs Construction",
              "Cookie and tracking opt-out preferences for Distinct Designs Construction. The full Complianz cookie statement still needs to be pasted in before launch.",
              body))


def planning():
    slug = "planning-guide"
    body = f"""
<section class="section">
  <p class="eyebrow">Free guide</p>
  <h1>Planning guide</h1>
  <p class="page-intro">To download the guide, use the reader below.</p>
  <iframe class="embed-frame" src="https://heyzine.com/flip-book/4c5f65a1bc.html" title="Distinct Designs planning guide" allowfullscreen></iframe>
  <div class="link-row">
    <a class="btn btn--nav" href="{HREF(slug, "guides/custom-home-builder-1")}">Guide landing 1</a>
    <a class="btn btn--nav" href="{HREF(slug, "guides/custom-home-builder-2")}">Guide landing 2</a>
    <a class="btn btn--nav" href="{HREF(slug, "guides/custom-home-builder-3")}">Guide landing 3</a>
  </div>
</section>
"""
    W(slug, S(slug,
              "Planning Guide | Distinct Designs Construction",
              "Read the Distinct Designs planning guide: what it takes to build a custom home in the High Desert and Coachella Valley.",
              body))


def thanks():
    slug = "guide-thank-you"
    body = """
<section class="section">
  <h1>Guide thank you</h1>
  <div class="video-frame">
    <iframe src="https://player.vimeo.com/video/1188183562?playsinline=1" title="Guide thank you video" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
  </div>
</section>
"""
    W(slug, S(slug,
              "Guide Thank You | Distinct Designs Construction",
              "Thank you for requesting the Distinct Designs planning guide.",
              body))


def partners():
    slug = "partners"
    p = g.prefix(slug)
    body = f"""
<section class="section">
  <img src="{p}images/site/DD-logo-full.webp" alt="Distinct Designs Construction" width="350" height="128">
  <p class="eyebrow" style="margin-top:1.5rem">Partners</p>
  <h1>When luxury buyers can't find it, we build it</h1>
  <h2>Custom home builds</h2>
  <p class="page-intro">6–7 figure remodels · High and Low Desert. Elite clients don't settle. When the right property doesn't exist, we create it with structured budgets, controlled timelines, and professional execution.</p>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><h3>Partnership program</h3><ul class="check-list"><li>2% on the first project</li><li>3% on the second project</li><li>4% on every project after</li></ul></article>
    <article class="info-card"><h3>Illustrative commission model</h3><ul class="check-list"><li>$2,500,000 × 4% = $100,000</li><li>$2,000,000 × 3% = $60,000</li><li>$1,000,000 × 2% = $20,000</li></ul></article>
    <article class="info-card"><h3>Volume partner incentive</h3><p>Partners referring 2+ projects annually qualify for preferred 4% tier status and priority scheduling access.</p></article>
  </div>
  <h2 style="margin-top:2.5rem">Submit a referral. Lock in your commission.</h2>
  <p>Click next to access the official referral agreement.</p>
  <p><a href="tel:{TEL}">{PHONE}</a><br>www.distinctdesignsconstruction.com</p>
  <div class="link-row"><a class="btn btn--primary" href="{HREF(slug, "partners/referral-agreement")}">Next</a></div>
</section>
"""
    W(slug, S(slug,
              "Partner Referral Program | Distinct Designs Construction",
              "Distinct Designs partner program for agents: 2% on the first referred project, 3% on the second, and 4% after that. High Desert and Coachella Valley custom homes and remodels.",
              body))


def referral():
    slug = "partners/referral-agreement"
    body = f"""
<section class="section">
  <h1>Referral agreement</h1>
  <p class="page-intro">Official agent referral agreement.</p>
  {F(g.REFERRAL_FORM, "Agent referral agreement")}
</section>
"""
    W(slug, S(slug,
              "Agent Referral Agreement | Distinct Designs Construction",
              "Submit the Distinct Designs Construction agent referral agreement.",
              body))


def guides():
    shared_for = [
        "You're planning a custom home or major remodel at $1M or above",
        "You want real numbers before you start designing",
        "You've been burned before, or don't want to be",
        "You're building from out of state and need it handled right",
        "You want it done once, done right",
    ]
    shared_not = [
        "You're collecting three bids to find the cheapest crew",
        "You want the lowest price over the right result",
        "You're not actually planning to build",
        "You'd rather learn the hard way, mid-construction",
    ]
    variants = [
        ("guides/custom-home-builder-1",
         "What It Really Takes to Build a Custom Home in the Desert | Distinct Designs",
         "Free guide for $1M+ custom homes in the High Desert and Coachella Valley: real costs, timelines, and the mistakes that blow budgets.",
         "Free guide · For $1M+ builds in the High Desert &amp; Coachella Valley",
         "What it really takes to build a custom home in the desert",
         "The clarity most homeowners wish they'd had before they started: real costs, real timelines, and the mistakes that quietly blow budgets. Written by a third-generation desert builder.",
         ["What a custom home actually costs here in 2026, by project level",
          "The 5 factors that really drive your budget (it isn't square footage)",
          "The 7 costly mistakes that derail builds, and how to avoid them",
          "The real 18–27 month timeline, phase by phase"],
         "d3BGxWF34ECOkqZdjpSI",
         "This guide is for you if",
         "This isn't for you if",
         "Build with clarity, not surprises"),
        ("guides/custom-home-builder-2",
         "Custom Home Guide for the High Desert | Distinct Designs",
         "Free guide for $1M+ builds in the High Desert and Coachella Valley from Distinct Designs Construction.",
         "Free guide · $1M+ builds · High Desert &amp; Coachella Valley",
         "What it really takes to build a custom home in the desert",
         "The clarity most homeowners wish they'd had before they started: real costs, real timelines, and the mistakes that quietly blow budgets. Written by a third-generation desert builder.",
         ["What a custom home actually costs here in 2026, by project level",
          "The 5 factors that really drive your budget (it isn't square footage)",
          "The 7 costly mistakes that derail builds, and how to avoid them",
          "The real 18–27 month timeline, phase by phase"],
         "BAGEhP3HzpQSiPNrrCqf",
         "This guide is for you if",
         "This isn't for you if",
         "Build with clarity, not surprises"),
        ("guides/custom-home-builder-3",
         "What It Really Costs to Build a Custom Home in the Desert | Distinct Designs",
         "Real numbers, real timelines, and the mistakes that blow custom-home budgets in the High Desert and Coachella Valley.",
         "Free guide · $1M+ builds · High Desert &amp; Coachella Valley",
         "What it really costs to build a custom home in the desert",
         "Real numbers. Real timelines. The mistakes that quietly blow budgets, and how to avoid every one. From a third-generation desert builder.",
         ["What it actually costs here in 2026, by project level",
          "The 5 factors that really drive your budget",
          "The 7 costly mistakes that derail builds",
          "The real 18–27 month timeline"],
         "9M9TcIWN7yJsuz9QWG1R",
         "For you if",
         "Not for you if",
         "Build with clarity, not surprises"),
    ]
    prices = [
        ("Major remodel", "$250K – $400K"),
        ("Large remodel / expansion", "$400K – $750K"),
        ("Custom home", "$750K – $1.35M"),
        ("Luxury custom home", "$2.2M – $3.8M+"),
        ("Luxury estate build", "$4.5M+"),
    ]
    for slug, title, meta, eyebrow, h1, sub, bullets, form_id, for_h, not_h, cta_h in variants:
        p = g.prefix(slug)
        bl = "".join(f"<li>{b}</li>" for b in bullets)
        fl = "".join(f"<li>{b}</li>" for b in shared_for)
        nl = "".join(f"<li>{b}</li>" for b in shared_not)
        cards = "".join(f'<article class="price-card"><h3>{n}</h3><strong>{v}</strong></article>' for n, v in prices)
        body = f"""
<section class="section">
  <p class="eyebrow">Distinct Designs · <a href="tel:{TEL}">760·221·4290</a></p>
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <p class="page-intro">{sub}</p>
  <ul class="check-list" style="margin-top:1.25rem">{bl}</ul>
  <div class="guide-layout guide-layout--form" style="margin-top:2rem">
    {book(slug)}
    <div class="guide-layout__form">
      <p><strong>Free · instant download</strong></p>
      {F(form_id, "Download the planning guide")}
    </div>
  </div>
  <div class="stat-row" style="margin-top:2rem">
    <article class="stat-card"><span>4.9★</span><small>15+ reviews</small></article>
    <article class="stat-card"><span>18 years</span><small>Building</small></article>
    <article class="stat-card"><span>3rd generation</span><small>Desert builder</small></article>
    <article class="stat-card"><span>#1145786</span><small>License</small></article>
  </div>
  <p class="page-intro" style="margin-top:1rem">High Desert · Coachella Valley</p>
</section>
<section class="section section--tinted">
  <p class="eyebrow">Inside the guide</p>
  <h2>The numbers most builders never put in writing</h2>
  <p>The same information we walk serious clients through before the first dollar is spent. Yours, free.</p>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><p class="eyebrow">01. Real investment levels</p><h3>What it actually costs</h3><p>Honest ranges for every project level, from a major remodel to a luxury estate, $250K to $4.5M+, plus real cost-per-square-foot for the desert market.</p></article>
    <article class="info-card"><p class="eyebrow">02. The 5 cost drivers</p><h3>What really moves the budget</h3><p>Why square footage is the smallest part of the equation, and how architecture, engineering, materials, and site conditions swing a build by six figures.</p></article>
    <article class="info-card"><p class="eyebrow">03. 7 costly mistakes</p><h3>What derails a build</h3><p>The seven mistakes that blow budgets, including why a $5,000 design change becomes $30,000+ once framing is up.</p></article>
    <article class="info-card"><p class="eyebrow">04. The real timeline</p><h3>What to actually expect</h3><p>The true 18–27 month path from first conversation to move-in, phase by phase, so nothing catches you off guard.</p></article>
  </div>
</section>
<section class="section">
  <p class="eyebrow">A preview. Know your investment.</p>
  <h2>Where projects typically land</h2>
  <p class="page-intro">Every project is priced to its site, scope, and selections. The full guide breaks down what each level includes.</p>
  <div class="price-grid" style="margin-top:1.5rem">{cards}</div>
  <p style="margin-top:1rem">Get the full breakdown, what each level includes and real cost-per-square-foot, in the free guide.</p>
</section>
<section class="section section--split section--tinted">
  <div class="section--split__media"><img src="{p}images/site/Nick-DD.jpg" alt="Nick Aguilar, owner of Distinct Designs" width="800" height="1000" loading="lazy"></div>
  <div>
    <p class="eyebrow">Who wrote this</p>
    <p>My grandfather, Mario Trujillo, a decorated Marine Corps Master Gunnery Sergeant, put me to work at 11 and taught me discipline, pride in craftsmanship, and treating every project like it's your own.</p>
    <p>I wrote this guide to give homeowners what most builders never offer: clear information before the first dollar is spent.</p>
    <p><strong>Nick Aguilar</strong><br>Third-generation builder · Distinct Designs</p>
  </div>
</section>
<section class="section">
  <p class="eyebrow">What clients say</p>
  <h2>On time. On budget. No surprises.</h2>
  {Q(g.GUIDE_QUOTES)}
</section>
<section class="section section--tinted">
  <p class="eyebrow">Is this guide for you?</p>
  <h2>Let's be honest about who this is for</h2>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>{for_h}</h3><ul class="check-list">{fl}</ul></article>
    <article class="info-card"><h3>{not_h}</h3><ul class="check-list">{nl}</ul></article>
  </div>
</section>
<section class="section" id="form">
  <div class="guide-layout guide-layout--form">
    {book(slug)}
    <div class="guide-layout__copy">
      <p class="eyebrow">Get the guide</p>
      <h2>{cta_h}</h2>
      <p>Enter your details and we'll send the full Ultimate Planning Guide straight to your inbox.</p>
      {F(GUIDE, "Get the free guide")}
    </div>
  </div>
  <p style="margin-top:2rem">Third-generation luxury custom home building and whole-home remodels across the High Desert and Coachella Valley. CA License #1145786.</p>
  <p><a href="tel:{TEL}">760·221·4290</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Yucca Valley · Joshua Tree · Palm Springs · Palm Desert · Rancho Mirage · La Quinta</p>
</section>
"""
        W(slug, S(slug, title, meta, body))


