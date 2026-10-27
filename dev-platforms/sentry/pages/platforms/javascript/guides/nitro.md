---
title: "Nitro"
source: https://docs.sentry.io/platforms/javascript/guides/nitro.md
path: platforms/javascript/guides/nitro
---

---
title: "Nitro"
description: "Learn how to set up Sentry in your Nitro app, capture your first events, and monitor performance."
url: https://docs.sentry.io/platforms/javascript/guides/nitro/
---

# Sentry for Nitro

This SDK is currently in **BETA**. Beta features are still in progress and may have bugs. Please reach out on [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if you have any feedback or concerns.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nitro.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* A Nitro application (`3.0.260415-beta` or newer)
* Node.js `20.19.0+`

## [Install](https://docs.sentry.io/platforms/javascript/guides/nitro.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nitro.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/nitro --save
```

*Other available variations of the above snippet: yarn, pnpm*

The SDK is a wrapper around `@sentry/node` and re-exports its full API. All Node.js instrumentation from `@sentry/node` (HTTP clients, databases, etc.) works out of the box, and the Nitro-specific tracing channels add parameterized routes and middleware spans on top.

## [Configure](https://docs.sentry.io/platforms/javascript/guides/nitro.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#4](https://docs.sentry.io/platforms/javascript/guides/nitro.md#send-logs) and [#5](https://docs.sentry.io/platforms/javascript/guides/nitro.md#send-application-metrics-). This guide also enables **Tracing**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

The Nitro SDK is configured in two places: a build-time wrapper that registers a Nitro module, and a runtime file that initializes the SDK before your server starts.

### [Configure the Nitro Build](https://docs.sentry.io/platforms/javascript/guides/nitro.md#configure-the-nitro-build)

Wrap your Nitro config with `withSentryConfig` so the Sentry module is registered during the build. Provide your auth token, organization, and project slugs so that source maps are automatically uploaded during production builds.

```typescript
import { defineNitroConfig } from "nitro/config";
import { withSentryConfig } from "@sentry/nitro";

const config = defineNitroConfig({
  serverDir: "./server",
  // your Nitro options...
});

export default withSentryConfig(config, {
  org: "<your-org-slug>",
  project: "<your-project-slug>",
  authToken: process.env.SENTRY_AUTH_TOKEN,
});
```

If you use Nitro as a Vite plugin, wrap the options you pass to `nitro()` instead:

```typescript
import { defineConfig } from "vite";
import { nitro } from "nitro/vite";
import { withSentryConfig } from "@sentry/nitro";

export default defineConfig({
  plugins: [
    nitro(
      withSentryConfig(
        {
          serverDir: "./server",
          // your Nitro options...
        },
        {
          org: "<your-org-slug>",
          project: "<your-project-slug>",
          authToken: process.env.SENTRY_AUTH_TOKEN,
        },
      ),
    ),
  ],
});
```

Add your auth token to your environment:

```bash
SENTRY_AUTH_TOKEN=<your-sentry-auth-token>
```

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nitro.md#initialize-the-sentry-sdk)

Create an `instrument.mjs` file in your project root:

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/nitro/configuration/options.md#tracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```javascript
import * as Sentry from "@sentry/nitro";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
});
```

### [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nitro.md#source-maps)

By default, `withSentryConfig` generates hidden source maps, uploads them to Sentry, and deletes the `.map` files after the build. This gives you readable stack traces in Sentry without shipping source maps to production. If you already set `sourcemap` in your Nitro config, the SDK respects your setting.

### [Run Your Application](https://docs.sentry.io/platforms/javascript/guides/nitro.md#run-your-application)

Load the instrumentation file with Node's `--import` flag before any Nitro command. This works for `nitro dev`, `nitro preview`, and your production start script:

```json
{
  "scripts": {
    "dev": "NODE_OPTIONS='--import ./instrument.mjs' nitro dev",
    "preview": "NODE_OPTIONS='--import ./instrument.mjs' nitro preview",
    "start": "NODE_OPTIONS='--import ./instrument.mjs' node .output/server/index.mjs"
  }
}
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/nitro.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/nitro/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Automatic Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nitro.md#automatic-instrumentation)

### [Automatic Error Capturing](https://docs.sentry.io/platforms/javascript/guides/nitro.md#automatic-error-capturing)

The SDK registers a Nitro `error` hook that captures unhandled errors from route handlers and middleware. `HTTPError`s with 3xx or 4xx status codes are skipped.

To disable the built-in error hook, set `enableNitroErrorHandler: false` in `Sentry.init`:

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  enableNitroErrorHandler: false,
});
```

### [Automatic Tracing](https://docs.sentry.io/platforms/javascript/guides/nitro.md#automatic-tracing)

The SDK creates transactions for incoming requests using Nitro's tracing channels (`h3.request` and `srvx.request`). `withSentryConfig` enables `tracingChannel: true` on your Nitro config automatically.

* Root request spans use `op: 'http.server'` with parameterized route names (e.g. `GET /users/:id`)
* Middleware spans use `op: 'middleware.nitro'`
* Path parameters are attached as `url.path.parameter.<key>` attributes
* 3xx/4xx `HTTPError`s do not mark the span as errored

### [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nitro.md#distributed-tracing)

The SDK appends `sentry-trace` and `baggage` values to `Server-Timing` response headers so the browser SDK can link pageload traces to their server trace. Incoming `sentry-trace` and `baggage` headers are honored by the underlying `@sentry/node` SDK. No additional configuration needed.

### [Manual Spans](https://docs.sentry.io/platforms/javascript/guides/nitro.md#manual-spans)

You can create manual spans inside your route handlers:

```javascript
import { defineHandler } from "nitro/h3";
import * as Sentry from "@sentry/nitro";

export default defineHandler(() => {
  return Sentry.startSpan({ name: "process-payment" }, () => {
    // ... your code
  });
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/nitro.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/nitro/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you're already logging with another library, use an integration to capture those logs as Sentry Logs automatically:

* [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nitro/logs.md#console-integration) for `console` calls
* [Consola](https://docs.sentry.io/platforms/javascript/guides/nitro/logs.md#console-integration)
* [Pino](https://docs.sentry.io/platforms/javascript/guides/nitro/configuration/integrations/pino.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/nitro.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/nitro/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

On Node.js, [`nodeRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nitro/configuration/integrations/noderuntimemetrics.md) also collects runtime health metrics automatically.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/nitro.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test route that throws an error, then open `/debug-sentry` in your browser to trigger the error:

```javascript
import { defineHandler } from "nitro/h3";

export default defineHandler(() => {
  throw new Error("Sentry Test Error");
});
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/nitro.md#view-captured-data-in-sentry)

Finally, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/nitro.md#next-steps)

At this point, you should have integrated Sentry into your Nitro application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/nitro/agent-tracing.md) to monitor your AI systems
* [Explore Tracing](https://docs.sentry.io/platforms/javascript/guides/nitro/tracing.md) to learn how to inspect application performance

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nitro/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
- [Cloud Functions for Firebase](https://docs.sentry.io/platforms/javascript/guides/firebase.md)
- [Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/nitro/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nitro/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/nitro/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/nitro/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/nitro/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/nitro/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/nitro/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/nitro/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/nitro/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nitro/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/nitro/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/nitro/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/nitro/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/nitro/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/nitro/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/nitro/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/nitro/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/nitro/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nitro/troubleshooting.md)

