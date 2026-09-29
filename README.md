# Distinct Designs Construction website

Static company site for Distinct Designs Construction (HTML, CSS, and vanilla JS). There is no build step. `generate.py` and `pages.py` only regenerate the HTML when the copy changes. Vercel serves this repository root as-is.

Deployed as the Vercel project **distinct-designs-website** (for example `https://distinct-designs-website.vercel.app/`). Framework preset: Other. No build command. Output directory: the repository root.

The site stays **noindexed until launch**:

- `<meta name="robots" content="noindex, nofollow">` on every page
- `X-Robots-Tag: noindex, nofollow` on all paths (`vercel.json`)
- `robots.txt` with `User-agent: *` and `Disallow: /`

The client's live ad landing pages are not in this repository. They stay in [OWD-Organization/distinct-designs-lp](https://github.com/OWD-Organization/distinct-designs-lp).

## Open client TODOs

- **License number.** The homepage FAQ says License #1039394. The guide pages say License #1145786. Confirm which CSLB number should appear sitewide before launch.
- **No street address.** Published locality is "Joshua Tree, CA" only. No street, ZIP, or postal address.
- **Sun Mesa.** `/projects/sun-mesa/` duplicates the Hilltop case study (including "Hilltop build") and uses the La Mirada photo set.
- **Cookie policy.** `/opt-out-preferences/` still contains the Complianz shortcode `[cmplz-document type="cookie-statement" region="us"]`, which does not render as a statement.
- **Remodels additions.** `/services/remodels/` names additions and does not describe them. That page also has no project count, price, timeline, or testimonial for the smaller kitchens-and-baths scope.
