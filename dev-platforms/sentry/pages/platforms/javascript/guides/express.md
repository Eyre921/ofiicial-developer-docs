---
title: "Express"
source: https://docs.sentry.io/platforms/javascript/guides/express.md
path: platforms/javascript/guides/express
---

---
title: "Express"
description: "Learn how to set up Sentry in your Express app on Node.js, Bun, or Deno."
url: https://docs.sentry.io/platforms/javascript/guides/express/
---

# Sentry for Express

[Express](https://expressjs.com/) doesn't need its own Sentry SDK. Set up Sentry for the runtime your app runs on, and the SDK instruments Express automatically: `expressIntegration` captures errors from your routes and middleware, and creates spans for incoming requests when tracing is enabled.

## [Set Up Sentry for Your Runtime](https://docs.sentry.io/platforms/javascript/guides/express.md#set-up-sentry-for-your-runtime)

* [![javascript.node icon](https://docs.sentry.io/_next/static/media/nodejs.79546009.svg)Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md?framework=express)
* [![javascript.bun icon](https://docs.sentry.io/_next/static/media/bun.64e0abda.svg)Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md?framework=express)
* [![javascript.deno icon](https://docs.sentry.io/_next/static/media/deno.0ad064af.svg)Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md?framework=express)

## [Customize Error Capturing](https://docs.sentry.io/platforms/javascript/guides/express.md#customize-error-capturing)

Errors with a 3xx or 4xx status code are skipped, since they're usually expected redirects or client errors. To change which errors are captured, pass a `shouldHandleError` callback to `expressIntegration()`:

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  integrations: [
    Sentry.expressIntegration({
      shouldHandleError(error) {
        const status = Number(error.status ?? error.statusCode ?? 500);
        // Capture 401/403 in addition to the default 5xx errors
        return status === 401 || status === 403 || status >= 500;
      },
    }),
  ],
});
```

If you capture errors yourself in your own error-handling middleware, set `shouldHandleError: false` to avoid duplicate events.

