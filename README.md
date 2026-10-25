# Habi Digital Group

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

## Development and hosting
Serve `dist/` with any static HTTP server. No build step or package installation is required. Root-relative links require hosting at a domain root; for GitHub Pages, configure an appropriate custom domain or adapt asset and link paths for a project subpath. Uploading this repository does not itself enable GitHub Pages.

The `.openai/hosting.json` file binds this source to the existing Sites project. The Sites source repository and this GitHub repository are separate; GitHub upload does not create an automatic deployment pipeline.

## Before public launch
- Confirm FormSubmit activation and test receipt.
- Choose the domain and update canonical URLs, sitemap and form return URL.
- Review site audience: currently owner-private on Sites.
- Supply roadshow details if needed.

Includes a generated transparent logo, responsive layouts, reduced-motion handling, metadata, structured organization data, a sitemap and source-linked research.
