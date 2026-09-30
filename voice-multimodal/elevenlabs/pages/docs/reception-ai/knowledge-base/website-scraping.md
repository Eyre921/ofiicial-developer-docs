---
title: "Website scraping"
source: https://elevenlabs.io/docs/reception-ai/knowledge-base/website-scraping.md
path: docs/reception-ai/knowledge-base/website-scraping
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Website scraping

Website scraping lets your receptionist learn from your existing website: FAQs, service descriptions, policies, and anything else published on your site.

## Source types

When adding a website source, choose:

| Type               | What it does                                                             | Best for                                |
| ------------------ | ------------------------------------------------------------------------ | --------------------------------------- |
| **Single page**    | Reads one specific URL                                                   | FAQ page, pricing page, specific policy |
| **Entire website** | Finds and reads the pages on your site that contain business information | Your main website                       |

URLs must use HTTPS.

## How an entire website is read

Reception.ai reads your sitemap and homepage links, then selects the pages most likely to contain business information, such as services, pricing, team, locations, and help articles. Pages such as galleries, blog posts, and legal notices are skipped.

| Scan           | When it runs                                                  | Pages read |
| -------------- | ------------------------------------------------------------- | ---------- |
| **Quick scan** | During onboarding                                             | Up to 15   |
| **Deep scan**  | When you add an entire website, or read the rest of your site | Up to 80   |

Booking platforms and social profiles, such as Facebook, Yelp, Vagaro, Booksy, or Calendly pages, are always read as a single page.

### Reading the rest of your site

Onboarding runs a quick scan only, so it's done in under a minute. To import the remaining pages, select **Read the rest of your site** on the [Home](/docs/reception-ai/features/home) page, or **Read more pages** on the website source. A deep scan can take several minutes.

## Status

While processing, a source shows its current step, such as crawling or extracting. When done, it shows **Ready** or **Error**.

Select **Show scraped pages** on a source to see which pages were read.

If a website can't be read, check the address. Some sites block automated access, for example with anti-bot protection. In that case, add individual pages or [upload the content as a file](/docs/reception-ai/knowledge-base/file-uploads).

## Keeping content current

Websites change over time. For a single page, select **Reprocess** to read it again. For an entire website, select **Read more pages** to refresh everything. Do this after changing pricing, services, or policies on your site.
