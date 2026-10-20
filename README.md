# Distinct Designs Construction website

Static company site for Distinct Designs Construction (HTML, CSS, and vanilla JS). There is no build step. `generate.py` and `pages.py` only regenerate the HTML when the copy changes. Vercel serves this repository root as-is.

Deployed as the Vercel project **distinct-designs-website** (for example `https://distinct-designs-website.vercel.app/`). Framework preset: Other. No build command. Output directory: the repository root.

The site is **indexable** (launch, October 2026). `robots.txt` allows all crawlers and points to `sitemap.xml`. Only the confirmation pages (`/thank-you/`, `/guide-thank-you/`) and `404.html` keep `<meta name="robots" content="noindex, nofollow">`, and `vercel.json` sends `X-Robots-Tag: noindex, nofollow` on the two confirmation paths. Vercel preview URLs are noindexed by Vercel itself.

The client's live ad landing pages are not in this repository. They stay in [OWD-Organization/distinct-designs-lp](https://github.com/OWD-Organization/distinct-designs-lp).

## v3 launch candidate, branch `v3-launch-candidate`

v2 plus Nick's 8 email edits, plus the webhook contact form and `/thank-you/` from `main`. This branch matches the Oct 17 2026 Vercel preview `distinct-designs-website-m5m5v4twe` file for file.

- The contact form (`#contact-form` in `script.js`) posts JSON to the GHL inbound webhook. It is on `/start-your-journey/` and in the homepage "Start your journey" section. On success it redirects to `/thank-you/`.
- `/contact` redirects to `/start-your-journey/`. Old WordPress URLs (`/alturas`, `/sun-mesa`, `/home`, `/agent-referral-agreement`, `/agent-education-flyer`) redirect in `vercel.json`.
- **Do not run `generate.py` on this branch.** The v3 edits were made in the HTML, and `generate.py` and `pages.py` are still the v2 versions. Regenerating would overwrite the v3 pages. Port the edits into the generators first.

## v2 (October 2026 change brief), branch `v2-brief-oct-2026`

Preview only. Not merged, no domain pointed. Built from "Distinct Designs Website & Google LSA Change Brief" (Steps 1-14).

- New pages: `/our-process/`, `/start-your-journey/` (replaces `/contact/`), `/service-areas/rancho-mirage/`, root `404.html`, `sitemap.xml` (generated).
- Removed: `/services/`, `/services/remodels/`, `/remodels/`, `/contact/`, `/projects/sun-mesa/`. Redirects in `vercel.json` (Sun Mesa is a temporary redirect).
- Header: Luxury Custom Homes (Custom Homes, Guest Houses & ADUs) · Luxury Remodels · Portfolio · Our Process · About, plus phone and Start Your Journey. Every top-level item uses `.nav-item`.
- Placeholder photos carry `data-placeholder-photo="what the final photo should be"`. One CSS rule in `styles.css` (section 20) draws a tiny "PH" corner tag. Delete that rule or the attributes to turn the tags off. Each spot also has an HTML `TODO(v2) PLACEHOLDER PHOTO` comment.
- DRAFT copy for Nick: the homepage owner note (`data-draft="owner-note"`) and the city intros and "Building in" sections (`data-draft="city-intro"`, `data-draft="city-building"`).
- Search the code for `TODO(v2)` to find every open item.

### v2 open items

- **Build timeline.** FAQ still says 10 to 18 months. The Planning Guide pages say 18 to 27 months (first conversation to move-in). Match them.
- **Email.** Switched site-wide to `nick@distinctdesignspro.com` (Nick's professional email, Oct 13 2026).
- **GHL form (Step 11).** Edit in the GHL builder: new fields, investment bands (custom homes start at $1M, so the first custom-home band should start at $1M), gold submit, notify Nick, tag kitchen/bath leads, update the workflow. The embed here is unchanged.
- **Leadership.** Project manager and office leadership cards are placeholders (names, titles, headshots).
- **Google badge.** Confirm the Google Business Profile URL and the live rating.
- **Photos to confirm.** The wood-beam living room (`living-room.jpg`, `footer-cta*`) and the garage with the car (`Garage.jpg`, `hero-garage*`) stay off until Nick confirms we built them. No out-of-state project claim until confirmed.
- **New photos needed.** Cubero drone shot (home hero), finished remodel interior (Luxury Remodels hero), ADU work, Hilltop hero, Palm Springs and Yucca Valley heroes, other low-desert city heroes, La Mirada reshoot.
- **Sun Mesa.** Off the Portfolio and redirected until it has real photos and its own copy.
- **Ad pages.** `/custom-home-builder-1|2|3` redirect to `/guides/...` here. The live ad pages stay in `distinct-designs-lp`; confirm routing before launch (Step 14).

## Open client TODOs

- **No street address.** Published locality is now "Yucca Valley, CA" (matches the Google Business Profile). No street, ZIP, or postal address.
- **Cookie policy.** `/opt-out-preferences/` still contains the Complianz shortcode `[cmplz-document type="cookie-statement" region="us"]`, which does not render as a statement.
