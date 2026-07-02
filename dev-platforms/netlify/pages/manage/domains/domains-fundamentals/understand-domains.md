---
title: "Netlify Custom Domains"
source: https://docs.netlify.com/manage/domains/domains-fundamentals/understand-domains.md
path: manage/domains/domains-fundamentals/understand-domains
---

---
title: "Understand domains"
description: "Learn the fundamentals of working with domains."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

Learn the fundamentals of working with domains on Netlify.

A domain name is the URL or web address where visitors find your site.

To access your deploys on Netlify, you can set up a custom domain or use the default Netlify subdomain.

## Supported custom domains

Custom domains allow you to make your sites accessible at your own domain names, such as `www.yourcustomdomain.com` or `docs.example.dev`. All top-level domains are supported for your custom domain.

Netlify supports custom domains for your production site, Deploy Previews, and branch deploys. 
  - For your production site, Netlify supports a primary site domain, [domain aliases](/manage/domains/configure-domains/add-a-domain-alias), and [domain-based redirects](/manage/domains/manage-domains/add-domain-redirect). 
  - For Deploy Previews, you can customize your domain after the Deploy Preview prefix `deploy-preview-#` with an [automatic deploy subdomain](/manage/domains/manage-domains/automatic-deploy-subdomains).  For example: `deploy-preview-123.company.com`.
  - For branch deploys, you can customize your domain after your branch name with [automatic deploy subdomains or branch subdomains](/manage/domains/manage-domains/manage-domains-for-branch-deploys).
  
 For example: `branch-name.company.com`

  For more example custom domains, check out the chart below.

## Default Netlify subdomain

Unless you've set up a basic password protection or authentication, a production site/app on Netlify is accessible from its Netlify subdomain, which takes the form `[name-of-your-site].netlify.app`. Note that you can change the name of your site to change this Netlify subdomain.

For example, if your site is named `brave-curie-12345`, then by default your site is available at `https://brave-curie-12345.netlify.app/`.

Learn more about other types of default Netlify subdomains for other types of deploys in the [chart](#netlify-subdomain-examples) below.

## Example domains for deploys

Your site deploys can have different domain patterns based on the type of site deploy. 

### Custom domain examples

| Site deploy type | Custom domain | Use case | 
|----|----|----|
| [Production deploy](/deploy/deploy-overview#definitions) | `company.com` | Can set a primary domain for your production site. | 
| [Deploy Preview](/deploy/deploy-overview#definitions) | `deploy-preview-42.early-access.company.com` | Can set a custom domain for Deploy Previews with an automatic deploy subdomain. | 
| [Branch deploy](/deploy/deploy-overview#definitions) for a branch named `staging` |   Branch subdomain: `staging.company.com` <br /> <br /> Automatic deploy subdomain: `staging.early-access.company.com` or `staging.internal-events.com` | Can set a custom domain for your branch deploys with an [automatic deploy subdomain or branch subdomains](/manage/domains/manage-domains/manage-domains-for-branch-deploys). |

### Netlify subdomain examples

By default, your site deploys are available at a URL using the Netlify subdomain `mysitename.netlify.app`. The Netlify subdomain URLs will always work even if you set up a custom domain for your site.

| Site deploy type | Netlify subdomain | Use case | 
|----|----|----|
| [Production deploy URL](/manage/domains/domains-fundamentals/domains-glossary#production-deploy-url) | `mysitename.netlify.app` | Typically a placeholder URL, ideal for internal development before assigning a custom domain for site visitors. | 
| [Deploy Preview](/manage/domains/domains-fundamentals/domains-glossary#deploy-preview) | `deploy-preview-42--mysitename.netlify.app` | Unique URL for previewing and collaborating on each pull/merge request. | 
| [Branch deploy](/manage/domains/domains-fundamentals/domains-glossary#branch-deploy) for a branch named `staging` | `staging--mysitename.netlify.app` <br /> <br /> Note: With a branch subdomain set up, the URL can be `staging.yourcustomdomain.com`. | Long-standing URL ideal for internal testing, QA teams, and ongoing development. To set up branch deploys, check out [branch deploy controls](/deploy/deploy-overview#branch-deploy-controls). |
| Atomic deploy | `1234abcd12acde000111cdef--mysitename.netlify.app` | Unique URL for a specific successful deploy. Also called [deploy permalinks](/deploy/deploy-overview#definitions) or just permalinks. Unlike the other site deploys, the web content at this URL never changes. A new deploy permalink is generated for each successful deploy of your site.
