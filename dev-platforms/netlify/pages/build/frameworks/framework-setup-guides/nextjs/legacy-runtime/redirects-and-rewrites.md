---
title: "Next.js Redirects & Rewrites (Legacy v4)"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/redirects-and-rewrites.md
path: build/frameworks/framework-setup-guides/nextjs/legacy-runtime/redirects-and-rewrites
---

---
title: "Next.js redirects and rewrites on Netlify"
description: "Implement redirects and rewrites to control routing in your Next.js 10-13.4 application. Learn when to use Next.js or our platform's redirects and rewrites."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

> **Note - Legacy Next.js Runtime:** The information on this page applies to Next.js version 10-13.4 and Netlify Next.js Runtime v4, which is currently in maintenance support.

[Visit our Next.js adapter docs](/build/frameworks/framework-setup-guides/nextjs/overview/) for info on newer versions of Next.js.

Netlify's Next.js Runtime supports Next.js [rewrites](https://nextjs.org/docs/api-reference/next.config.js/rewrites) and [redirects](https://nextjs.org/docs/api-reference/next.config.js/redirects). These are defined in your `next.config.js` file and have some features that are not included in Netlify redirects and rewrites.

## Use Netlify redirects and rewrites on a Next.js site

Every site on Netlify supports [redirects and rewrites](/manage/routing/redirects/overview), which are defined in a `_redirects` or `netlify.toml` file. Sites that use Next.js Runtime are no exception.

However, there are some things to keep in mind when you use Netlify redirects and rewrites on a Next.js site. Next.js Runtime generates several rewrites on its own, which are used to map paths from your site to different Netlify Functions. The functions handle SSR, preview mode, and images, as well as assets in `/_next/static`. 

Any Netlify redirects or rewrites that you create [take precedence](#redirect-and-rewrite-precedence) over those created by Next.js Runtime. 

### Danger

**Avoid root-level rewrite**

Do not add a rewrite from the site root (such as `from = "/"`) in `netlify.toml` or `_redirects`. Your root-level rewrite would take precedence over Next.js Runtime's generated rewrites and break routing on your site.

## Redirect and rewrite precedence

Redirects and rewrites are processed in the following order:

1. Redirects and rewrites in the `_redirects` file. These are read in order until a match is found, then processing stops.
2. Redirects and rewrites in the `netlify.toml` file. None of these are read if one previous rule has already matched.
3. At this point, if the request targets a static file, then the static file returns without further evaluation of Next.js redirects or rewrites.
4. Any request that does not target a static file will then be passed to Next.js, which will then evaluate redirects and rewrites (defined in the `next.config.js` file).

## General principles

Netlify and Next.js redirects support different features and are evaluated at different points in the request lifecycle. To determine which one to use with your site, consider the following:

### When to use Netlify redirects or rewrites

- Generally, if your redirect can be handled with Netlify redirects, this is the preferred option because they are faster to evaluate.
- [Identity](/manage/security/secure-access-to-sites/identity/overview), [proxying](/manage/routing/redirects/rewrites-proxies/), and [country-based redirects](/manage/routing/redirects/overview) are Netlify-specific features and must use Netlify redirects.
- If you need redirects or rewrites to be applied before loading static files, you must use Netlify redirects and rewrites.

### When to use Next.js redirects or rewrites

- If you are using a _rewrite_ that points to a dynamic Next.js page, you must use Next.js rewrites. Next.js has no way of knowing what the rewritten page is when using Netlify rewrites, so the wrong page is likely to be rendered. Note that this only applies to rewrites, not redirects.
- If you need Next.js-specific features, such as regex path or header matching, you must use Next.js rewrites.

### Use `_redirects` and `_headers` files

If you use [`_redirects`](/manage/routing/redirects/overview#syntax-for-the-redirects-file) or [`_headers`](/manage/routing/headers/#syntax-for-the-headers-file) files rather than a `netlify.toml` file, be aware that these files must be in the published directory of your site, not the root of your repo. 

To do this, put them in `public` and they will be moved into `.next` at build time. Do not put them directly into `.next`, because it is emptied at build time. Any `_redirects` or `_headers` files in the root of the repo will not be found when deployed.

