# Habi Digital Group

## Open the website

- **[Home page](https://amparooskar-prog.github.io/Habi-Digital-Group/)**
- **[Compact landing page & enquiry form](https://amparooskar-prog.github.io/Habi-Digital-Group/enquire/)**
- **[Roadshow conversation brief](https://amparooskar-prog.github.io/Habi-Digital-Group/roadshow/)**

These links open the public GitHub Pages website.

## Find the website files

All website files are in **[dist/](dist/)**.

| Page or asset | File |
| --- | --- |
| Home page | [dist/index.html](dist/index.html) |
| Compact landing page | [dist/enquire/index.html](dist/enquire/index.html) |
| Roadshow page | [dist/roadshow/index.html](dist/roadshow/index.html) |
| Styles | [dist/style.css](dist/style.css) |
| Form and animation code | [dist/app.js](dist/app.js) |
| Logo | [dist/logo.png](dist/logo.png) |

GitHub's Code tab displays source files, not a rendered website. Use the live links above to view the design.

Marketing website, roadshow brief, and compact enquiry landing page.

## Pages
- `/` — full company website
- `/enquire/` — concise services overview and email enquiry form
- `/roadshow/` — device-local downloadable conversation brief
- `/privacy/` — information-handling notice
- `/thank-you/` — fallback return page for native form submissions

## Enquiry delivery
The enquiry form posts to FormSubmit for delivery to **amparooskar@gmail.com**, approved by the site owner. The recipient confirmed activation on 25 October 2026. A test from the live site origin was accepted successfully by FormSubmit. New origins may require separate activation. No API keys or Gmail credentials are included. JavaScript handles accepted responses, activation messages, timeout, and errors; native HTML submission is the no-JavaScript fallback. Honeypot and provider spam protection apply. Verify recipient activation and a real test delivery before using with prospects.

The roadshow form remains a separate local download, not an email submission.

## GitHub Pages publishing

Pages publishes from `main` → `/docs`. The `dist/` folder remains the source for the original Sites host. After editing `dist/`, run `python3 scripts/build-github-pages.py` and commit the regenerated `docs/` folder. The generator adapts navigation, assets, canonical URLs, sitemap, and the form return URL for the GitHub project path.

FormSubmit may require a separate email activation for this GitHub Pages origin.

## Development and hosting
Serve `dist/` with any static HTTP server. No build step or package installation is required. Root-relative links require hosting at a domain root; for GitHub Pages, configure an appropriate custom domain or adapt asset and link paths for a project subpath. GitHub Pages is configured to publish the generated `docs/` directory.

The `.openai/hosting.json` file binds this source to the existing Sites project. The Sites source repository and this GitHub repository are separate; GitHub upload does not create an automatic deployment pipeline.

## Before public launch
- Confirm FormSubmit activation and test receipt.
- Choose the domain and update canonical URLs, sitemap and form return URL.
- Review site audience: currently owner-private on Sites.
- Supply roadshow details if needed.

Includes a generated transparent logo, responsive layouts, reduced-motion handling, metadata, structured organization data, a sitemap and source-linked research.
