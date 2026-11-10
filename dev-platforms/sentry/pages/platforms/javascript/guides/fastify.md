---
title: "Fastify"
source: https://docs.sentry.io/platforms/javascript/guides/fastify.md
path: platforms/javascript/guides/fastify
---

---
title: "Fastify"
description: "Learn how to set up Sentry in your Fastify app on Node.js, Bun, or Deno."
url: https://docs.sentry.io/platforms/javascript/guides/fastify/
---

# Sentry for Fastify

[Fastify](https://fastify.dev/) doesn't need its own Sentry SDK. Set up Sentry for the runtime your app runs on, and the SDK instruments Fastify automatically: `fastifyIntegration` captures errors from your routes and hooks, and creates spans for incoming requests when tracing is enabled.

## [Set Up Sentry for Your Runtime](https://docs.sentry.io/platforms/javascript/guides/fastify.md#set-up-sentry-for-your-runtime)

* [![javascript.node icon](https://docs.sentry.io/_next/static/media/nodejs.79546009.svg)Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md?framework=fastify)
* [![javascript.bun icon](https://docs.sentry.io/_next/static/media/bun.64e0abda.svg)Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md?framework=fastify)
* [![javascript.deno icon](https://docs.sentry.io/_next/static/media/deno.0ad064af.svg)Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md?framework=fastify)

## [Customize Error Capturing](https://docs.sentry.io/platforms/javascript/guides/fastify.md#customize-error-capturing)

Errors with a 3xx or 4xx status code are skipped. To change which errors are captured, pass a `shouldHandleError` callback to `fastifyIntegration()`. See the [Fastify integration](https://docs.sentry.io/platforms/javascript/guides/node/configuration/integrations/fastify.md#shouldhandleerror) for all options.

