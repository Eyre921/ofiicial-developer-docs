---
title: "Koa"
source: https://docs.sentry.io/platforms/javascript/guides/koa.md
path: platforms/javascript/guides/koa
---

---
title: "Koa"
description: "Learn how to set up Sentry in your Koa app on Node.js, Bun, or Deno."
url: https://docs.sentry.io/platforms/javascript/guides/koa/
---

# Sentry for Koa

[Koa](https://koajs.com/) doesn't need its own Sentry SDK. Set up Sentry for the runtime your app runs on, and the SDK instruments Koa automatically: `koaIntegration` registers an error handler when your app starts, and creates spans for incoming requests and middleware when tracing is enabled.

## [Set Up Sentry for Your Runtime](https://docs.sentry.io/platforms/javascript/guides/koa.md#set-up-sentry-for-your-runtime)

* [![javascript.node icon](https://docs.sentry.io/_next/static/media/nodejs.79546009.svg)Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md?framework=koa)
* [![javascript.bun icon](https://docs.sentry.io/_next/static/media/bun.64e0abda.svg)Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md?framework=koa)
* [![javascript.deno icon](https://docs.sentry.io/_next/static/media/deno.0ad064af.svg)Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md?framework=koa)

To configure the integration, see the [Koa integration](https://docs.sentry.io/platforms/javascript/guides/node/configuration/integrations/koa.md).

