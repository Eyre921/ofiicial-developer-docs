---
title: "Hapi"
source: https://docs.sentry.io/platforms/javascript/guides/hapi.md
path: platforms/javascript/guides/hapi
---

---
title: "Hapi"
description: "Learn how to set up Sentry in your Hapi app on Node.js, Bun, or Deno."
url: https://docs.sentry.io/platforms/javascript/guides/hapi/
---

# Sentry for Hapi

[Hapi](https://hapi.dev/) doesn't need its own Sentry SDK. Set up Sentry for the runtime your app runs on, and the SDK instruments Hapi automatically: `hapiIntegration` registers an error handler when your server starts, and creates spans for incoming requests when tracing is enabled.

## [Set Up Sentry for Your Runtime](https://docs.sentry.io/platforms/javascript/guides/hapi.md#set-up-sentry-for-your-runtime)

* [![javascript.node icon](https://docs.sentry.io/_next/static/media/nodejs.79546009.svg)Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md?framework=hapi)
* [![javascript.bun icon](https://docs.sentry.io/_next/static/media/bun.64e0abda.svg)Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md?framework=hapi)
* [![javascript.deno icon](https://docs.sentry.io/_next/static/media/deno.0ad064af.svg)Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md?framework=hapi)

To configure the integration, see the [Hapi integration](https://docs.sentry.io/platforms/javascript/guides/node/configuration/integrations/hapi.md).

