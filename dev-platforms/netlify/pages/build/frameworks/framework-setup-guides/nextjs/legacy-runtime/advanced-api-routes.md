---
title: "Next.js Advanced API Routes (Legacy v4)"
source: https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/legacy-runtime/advanced-api-routes.md
path: build/frameworks/framework-setup-guides/nextjs/legacy-runtime/advanced-api-routes
---

---
title: "Next.js advanced API routes"
description: "Use background API routes and scheduled API routes with your Next.js 10-13.4 project to handle long-running or scheduled processes."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

> **Note - Legacy Next.js Runtime:** The information on this page applies to Next.js version 10-13.4 and Netlify Next.js Runtime v4, which is currently in maintenance support.

[Visit our Next.js adapter docs](/build/frameworks/framework-setup-guides/nextjs/overview/) for info on newer versions of Next.js.

Next.js sites on Netlify can take advantage of advanced API route capabilities in addition to support for basic and dynamic [API routes](https://nextjs.org/docs/api-routes/introduction). These enhancements include running a process in the background for a long-running task and scheduling a process to run at a regular interval. They are available for Next.js 12.2 and later.

## Background API routes

> **Pricing Information:** This feature is available on all [Pro](https://www.netlify.com/pricing/?category=developer) and [Enterprise](https://www.netlify.com/pricing/?category=enterprise) plans.

With background API routes, you can invoke an API route and instead of instantly returning the data, the function can return a `HTTP 202 Accepted` response, allowing it to process the request in the background for up to 15 minutes. You can read more about this functionality in the [Netlify Background Functions](/build/functions/background-functions/) documentation.

The background function can be called on the following endpoint for Next.js sites: `/api/function-name`.

To enable a background API route in your Next.js project, add a TypeScript or JavaScript file inside the folder `pages/api` and export the following `config` object:

```ts
export default async (req, res) => {
  // Do something slow
};

export const config = {
  type: "experimental-background",
};
```

Check out a more extensive [background API route code example](https://github.com/netlify/next-background-api-route) for details.

## Scheduled API routes

> **Pricing Information:** This feature is available on all pricing plans.

Scheduled API routes are triggered on a schedule rather than in response to an HTTP request. This functionality is powered by [Netlify Scheduled Functions](/build/functions/scheduled-functions/).

To enable a scheduled API route in your Next.js project, add a TypeScript or JavaScript file inside the folder `pages/api` and export the following `config` object:

```ts
export default (req, res) => {
  // Do something scheduled
};

export const config = {
  type: "experimental-scheduled",
  schedule: "@hourly",
};
```

Scheduled functions use the ["cron expression" format used by tools like crontab](https://man7.org/linux/man-pages/man5/crontab.5.html) and are executed according to the UTC timezone.
For example, the cron expression `0 0 * * *` will run a scheduled function every day at midnight UTC. We also support the [extensions](https://man7.org/linux/man-pages/man5/crontab.5.html#EXTENSIONS) in the RFC, except for the `@reboot` and `@annually` specifications.
With extensions, the expression `0 0 * * *` can be written as `@daily`.

## Test locally

Follow these steps to test a background API route or scheduled API route during development. A scheduled API route will only run on a schedule once deployed to production.

1. Run your Next.js project locally in development mode with `next dev`.
2. Trigger the route by invoking the URL path.

### Note

**Testing with Netlify Dev isn't supported**

[Netlify Dev](/api-and-cli-guides/cli-guides/local-development/) doesn't currently support serving background and schedule API routes for local testing. Instead, we recommend that you test with `next dev`.


