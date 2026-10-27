---
title: "Cloudflare"
source: https://docs.sentry.io/platforms/javascript/guides/cloudflare.md
path: platforms/javascript/guides/cloudflare
---

---
title: "Cloudflare"
description: "Learn how to manually set up Sentry for Cloudflare Workers and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/cloudflare/
---

# Sentry for Cloudflare

This guide covers Cloudflare Workers. If you're deploying a Cloudflare Pages application, see [Cloudflare Pages](https://docs.sentry.io/platforms/javascript/guides/cloudflare/features/pages.md) instead, which is set up with middleware rather than a wrapper.

If you're using any of the listed frameworks, follow their specific setup instructions:

* **[Astro](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/astro.md)**
* **[Hono](https://docs.sentry.io/platforms/javascript/guides/hono.md)** (with @sentry/hono)
* **[Hydrogen](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/hydrogen-react-router.md)**
* **[Next.js](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/nextjs.md)**
* **[Nuxt](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/nuxt.md)**
* **[Remix](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/remix.md)**
* **[SvelteKit](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/sveltekit.md)**
* **[TanStack Start](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks/tanstack-start.md)**

##### Cloudflare Workers limitations

The Cloudflare Workers runtime has some platform-specific limitations that affect tracing. See [Known Limitations](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#known-limitations) for details.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

## [Install](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/cloudflare --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#configure)

**Error Monitoring** starts working as soon as you configure Sentry. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#send-application-metrics-). This guide also enables **Tracing**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

This guide sets Sentry up through Vite, which is what we recommend for Cloudflare Workers. The plugin does the wiring at build time, so your Worker code stays untouched.

Not using Vite? See the [Wrangler setup](https://docs.sentry.io/platforms/javascript/guides/cloudflare/install/wrangler.md) for the manual instrumentation.

### [Add the Vite Plugin](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#add-the-vite-plugin)

Add the Sentry plugin to your existing `vite.config.ts`, next to `cloudflare()`. Both of its behaviors are on by default.

`autoInstrumentation` wraps your Worker entry, and any Durable Object, Workflow or Agents SDK class in your wrangler config, at build time, so you don't have to call `Sentry.withSentry()` yourself. `buildTimeInstrumentation` instruments bundled dependencies such as database clients, which is the only way to trace them in the Workers runtime, where the SDK can't patch them at runtime.

To see its options, which packages it instruments, and how to opt out of either behavior, see [Vite Plugin](https://docs.sentry.io/platforms/javascript/guides/cloudflare/install/vite-plugin.md).

```typescript
 import { cloudflare } from "@cloudflare/vite-plugin";
+import { sentryCloudflareVitePlugin } from "@sentry/cloudflare/vite";
 import { defineConfig } from "vite";

 export default defineConfig({
   plugins: [
     cloudflare(),
+    sentryCloudflareVitePlugin(),
   ],
 });
```

Run `vite build` before `wrangler deploy`, and use `vite dev` in place of `wrangler dev` for local development.

### [Wrangler Configuration](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#wrangler-configuration)

Since the SDK needs access to the `AsyncLocalStorage` API, you need to set the `nodejs_compat` compatibility flag and a `compatibility_date` of `2024-09-23` or later in your `wrangler.(jsonc|toml)` configuration file. We recommend the latest compatibility date, as some integrations depend on newer Cloudflare runtime features:

```jsonc
{
  // Set this to today's date
  "compatibility_date": "2026-10-27",
  "compatibility_flags": ["nodejs_compat"],
}
```

*Other available variations of the above snippet: Toml*

### [Release Configuration (Optional)](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#release-configuration-optional)

If you don't set the `release` option manually, the SDK automatically detects it from these sources (in order of priority):

1. The `SENTRY_RELEASE` environment variable
2. The `CF_VERSION_METADATA.id` binding (if configured)

To enable automatic release detection via Cloudflare's version metadata, add the `CF_VERSION_METADATA` binding in your wrangler configuration. This provides access to the [Cloudflare version metadata](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/).

```jsonc
{
  // ...
  "version_metadata": {
    "binding": "CF_VERSION_METADATA",
  },
}
```

*Other available variations of the above snippet: Toml*

### [Add Your Sentry Options](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#add-your-sentry-options)

Create an `instrument.server.ts` file next to your Worker entry, the file that `main` points at in your wrangler config. If `main` is `src/index.ts`, the file belongs at `src/instrument.server.ts`, not at the project root.

The name is fixed. The plugin looks for `instrument.server` with a `.ts`, `.mts`, `.js`, `.mjs` or `.cjs` extension, and passes its default export to `withSentry`. Use `defineCloudflareOptions` to get the options type-checked.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/cloudflare/configuration/options.md#tracesSampleRate)

Don't need a feature? Remove its integration and options from the snippet.

```typescript
import { defineCloudflareOptions } from "@sentry/cloudflare";

export default defineCloudflareOptions((env) => ({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
}));
```

Prefer to configure Sentry with bindings?

If you don't add an `instrument.server.*` file, the SDK reads its configuration from the Worker's `env` at runtime instead: `SENTRY_DSN`, `SENTRY_ENVIRONMENT`, `SENTRY_TRACES_SAMPLE_RATE`, `SENTRY_DEBUG`, `SENTRY_TUNNEL` and `SENTRY_TRACE_LIFECYCLE`. Set them as secrets or vars in your wrangler config.

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your [source maps](https://docs.sentry.io/platforms/javascript/guides/cloudflare/sourcemaps.md) to Sentry.

First, set the `upload_source_maps` option to `true` in your `wrangler.(jsonc|toml)` config file to enable source map uploading:

```jsonc
{
  "upload_source_maps": true,
}
```

*Other available variations of the above snippet: Toml*

Next, run the Sentry Wizard to finish your setup:

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/cloudflare/configuration/options.md#dataCollection).

```typescript
import { defineCloudflareOptions } from "@sentry/cloudflare";

export default defineCloudflareOptions((env) => ({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
}));
```

### [Known Limitations](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#known-limitations)

#### [Span Durations](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#span-durations)

Server-side spans will display `0ms` for their durations. In the Cloudflare Workers runtime, `performance.now()` and `Date.now()` only advance after I/O occurs. CPU-bound operations will show zero duration. This is a security measure Cloudflare implements to [mitigate against timing attacks](https://developers.cloudflare.com/workers/runtime-apis/performance/).

This is expected behavior in the Cloudflare Workers environment and affects all frameworks deployed to Cloudflare Workers, including Next.js, Astro, Remix, and others.

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/cloudflare/logs.md) for all available logging methods and the syntax for formatting messages.

```javascript
Sentry.logger.info("User example action completed");

Sentry.logger.warn("Slow operation detected", {
  operation: "data_fetch",
  duration: 3500,
});

Sentry.logger.error("Validation failed", {
  form_field: "email",
  reason: "Invalid email",
});
```

If you're already logging with `console` or Consola, you can capture those logs with [our console integrations](https://docs.sentry.io/platforms/javascript/guides/cloudflare/logs.md#console-integration).

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/cloudflare/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a route to your Worker that throws an error:

```javascript
export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (url.pathname === "/debug-sentry") {
      throw new Error("Sentry Test Error");
    }

    return new Response("...");
  },
};
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md#next-steps)

At this point, you should have integrated Sentry into your Cloudflare Worker. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/cloudflare/agent-tracing.md) to monitor your AI systems

Are you having problems setting up the SDK?

* Check out setup instructions for popular [frameworks on Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks.md)
* Find various support topics in [troubleshooting](https://docs.sentry.io/platforms/javascript/guides/cloudflare/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
- [Cloud Functions for Firebase](https://docs.sentry.io/platforms/javascript/guides/firebase.md)
- [Cordova](https://docs.sentry.io/platforms/javascript/guides/cordova.md)
- [Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md)
- [Effect](https://docs.sentry.io/platforms/javascript/guides/effect.md)
- [Electron](https://docs.sentry.io/platforms/javascript/guides/electron.md)
- [Elysia](https://docs.sentry.io/platforms/javascript/guides/elysia.md)
- [Ember](https://docs.sentry.io/platforms/javascript/guides/ember.md)
- [Eve](https://docs.sentry.io/platforms/javascript/guides/eve.md)
- [Express](https://docs.sentry.io/platforms/javascript/guides/express.md)
- [Fastify](https://docs.sentry.io/platforms/javascript/guides/fastify.md)
- [Flue](https://docs.sentry.io/platforms/javascript/guides/flue.md)
- [Gatsby](https://docs.sentry.io/platforms/javascript/guides/gatsby.md)
- [Google Cloud Functions](https://docs.sentry.io/platforms/javascript/guides/gcp-functions.md)
- [Hapi](https://docs.sentry.io/platforms/javascript/guides/hapi.md)
- [Hono](https://docs.sentry.io/platforms/javascript/guides/hono.md)
- [Koa](https://docs.sentry.io/platforms/javascript/guides/koa.md)
- [Mastra](https://docs.sentry.io/platforms/javascript/guides/mastra.md)
- [Nest.js](https://docs.sentry.io/platforms/javascript/guides/nestjs.md)
- [Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)
- [Nitro](https://docs.sentry.io/platforms/javascript/guides/nitro.md)
- [Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md)
- [Nuxt](https://docs.sentry.io/platforms/javascript/guides/nuxt.md)
- [Pi Durable](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md)
- [React](https://docs.sentry.io/platforms/javascript/guides/react.md)
- [React Router Framework](https://docs.sentry.io/platforms/javascript/guides/react-router.md)
- [Remix](https://docs.sentry.io/platforms/javascript/guides/remix.md)
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/cloudflare/install.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/cloudflare/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/cloudflare/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/cloudflare/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/cloudflare/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/cloudflare/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/cloudflare/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/cloudflare/mcp-monitoring.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/cloudflare/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/cloudflare/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/cloudflare/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/cloudflare/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/cloudflare/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/cloudflare/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/cloudflare/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/cloudflare/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/cloudflare/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/cloudflare/troubleshooting.md)
- [Cloudflare Features](https://docs.sentry.io/platforms/javascript/guides/cloudflare/features.md)
- [Frameworks on Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare/frameworks.md)

