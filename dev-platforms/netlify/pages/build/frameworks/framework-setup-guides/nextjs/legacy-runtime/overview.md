---
title: "Next.js Legacy Runtime Overview (v4)"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/overview.md
path: build/frameworks/framework-setup-guides/nextjs/legacy-runtime/overview
---

---
title: Legacy Runtime Overview
description: Overview of Next.js Legacy Runtime on Netlify
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

> **Note - Legacy Next.js Runtime:** The information on this page applies to Next.js version 10-13.4 and Netlify Next.js Runtime v4, which is currently in maintenance support.

[Visit our Next.js adapter docs](/build/frameworks/framework-setup-guides/nextjs/overview/) for info on newer versions of Next.js.

## Key features of the legacy runtime

Here are notable features of the v4 runtime and the main differences compared to the current adapter:

### Supported router types

Next.js Runtime v4 supports Next.js [Pages Router](https://nextjs.org/docs/pages). For full support of [App Router](https://nextjs.org/docs/app), upgrade to the [latest adapter.](/build/frameworks/framework-setup-guides/nextjs/overview/)

### Incremental Static Regeneration (ISR)

On Runtime v4, ISR on Netlify works with [On-demand Builders](/build/configure-builds/on-demand-builders/) to revalidate pages as needed without rebuilding your entire site. Runtime v4 does not support tag or path based revalidation. [Upgrade to the current adapter](/build/frameworks/framework-setup-guides/nextjs/overview/) to use that functionality.

You can enable ISR for a page by returning a value for `revalidate` from the `getStaticProps` function. The minimum value for `revalidate` is 60 seconds. Any value less than that will default to 60 seconds.

ISR uses a "stale while revalidate" strategy, meaning that the visitor still receives the stale content, but it is regenerated in the background and becomes ready for the next request.

### Static site export

You can use [`next export`](https://nextjs.org/docs/advanced-features/static-html-export) to generate a completely static site, if you have no need for any of the dynamic features that Next.js offers.

### Image optimization

The `next/image` component allows you to automatically optimize images for your site on-demand, as they're requested by users. On Runtime v4, `next/image` uses [ipx](https://github.com/unjs/ipx/) and [On-demand Builders](/build/configure-builds/on-demand-builders/) by default. With the current adapter, [Netlify Image CDN](/build/image-cdn/overview/) is used instead to simplify the setup of your site.

### Edge middleware

Next.js middleware is supported via an automatically-installed [Edge Function](/build/edge-functions/overview/).

### Redirects and rewrites

Next.js Runtime supports Next.js [rewrites](https://nextjs.org/docs/api-reference/next.config.js/rewrites) and [redirects](https://nextjs.org/docs/api-reference/next.config.js/redirects). These are defined in your `next.config.js` file and support some features that are not included in Netlify redirects and rewrites.

For redirects, we recommend using Netlify redirects when possible because they are faster to evaluate. Learn more about [Next.js redirects and rewrites on Netlify.](/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/redirects-and-rewrites/)

## Suggested configuration values

When you [link a repository](/manage/projects/add-new-project/#import-from-an-existing-repository) for a Next.js project, Netlify provides a suggested build command and publish directory: `next build` and `.next`.

If you're using the CLI to run [Netlify Dev](/api-and-cli-guides/cli-guides/local-development/) for a local development environment, Netlify suggests a dev command and port: `next` and `3000`.

You can override suggested values or set them in a configuration file instead, but suggested values from automatic framework detection may help simplify the process of setting up a Next.js site on Netlify.

For manual configuration, check out the [typical build settings](/build/frameworks/framework-setup-guides/nextjs/overview/) for Next.js.

## pnpm support

If you're planning to use pnpm with Next.js to manage dependencies, you must do one of the following:

- Set a `PNPM_FLAGS` [environment variable](/build/environment-variables/get-started/#create-environment-variables) with a value of `--shamefully-hoist`. This appends a `--shamefully-hoist` argument to the `pnpm install` command that Netlify runs.
- [Enable public hoisting](https://pnpm.io/npmrc#public-hoist-pattern) by adding an `.npmrc` file in the root of your project with this content:

  ```ini
  public-hoist-pattern[]=*
  ```

Learn more about using [pnpm on Netlify](/build/configure-builds/manage-dependencies/#pnpm).

## Troubleshooting

If you run into issues running a Next.js app on Netlify, check out our [troubleshooting page](/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/troubleshooting/). You can also visit the [Netlify Support Forums](https://answers.netlify.com/categories/) to see if others have encountered similar issues.

## More resources

- [Next.js documentation](https://nextjs.org/docs/getting-started)
- [Posts about Next.js in our blog](https://www.netlify.com/tags/nextjs/)
