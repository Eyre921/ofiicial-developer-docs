---
title: "Hono"
source: https://docs.sentry.io/platforms/javascript/guides/hono.md
path: platforms/javascript/guides/hono
---

---
title: "Hono"
description: "Learn how to set up Sentry in your Hono app and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/hono/
---

# Sentry for Hono

The `@sentry/hono` SDK supports Hono 4+ across multiple runtimes: Cloudflare Workers, Node.js, Bun, and Deno. It works as Hono middleware, so you can drop it into your existing app with minimal setup.

Are you using @hono/sentry?

The community middleware `@hono/sentry` has been deprecated in favor of `@sentry/hono`, which provides better performance and more features. To migrate:

1. Uninstall `@hono/sentry` and `toucan-js`
2. Follow the install and configure steps below for your runtime
3. Replace the old middleware with the new `sentry()` middleware

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/hono.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Hono version `4.0.0` or above

## [Install](https://docs.sentry.io/platforms/javascript/guides/hono.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/hono.md#install-the-sentry-sdk)

Install the `@sentry/hono` package:

```bash
npm install @sentry/hono
```

*Other available variations of the above snippet: yarn, pnpm*

### [Install the Peer Dependency for Your Runtime](https://docs.sentry.io/platforms/javascript/guides/hono.md#install-the-peer-dependency-for-your-runtime)

The SDK needs a runtime-specific peer dependency. Install the one that matches your environment and keep its version in sync with `@sentry/hono`. You won't import it directly, but it must be present in your project.

**Cloudflare Workers**

```bash
npm install @sentry/cloudflare
```

**Node.js**

```bash
npm install @sentry/node
```

**Bun**

```bash
npm install @sentry/bun
```

**Deno**

```bash
deno add npm:@sentry/deno
```

### [Install the Profiling Package (Node.js Only)](https://docs.sentry.io/platforms/javascript/guides/hono.md#install-the-profiling-package-nodejs-only)

Profiling is only available for the Node.js runtime. Install the `@sentry/profiling-node` package:

```bash
npm install @sentry/profiling-node --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/hono.md#configure)

**Error Monitoring** starts working as soon as you configure the `sentry()` middleware or call `Sentry.init()` for Node.js. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/hono.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/hono.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**. Profiling is available only when you use the Node.js runtime.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

Cloudflare Workers: Enable Node.js Compatibility

If you're deploying to Cloudflare Workers, set the `nodejs_compat` compatibility flag. The SDK needs `AsyncLocalStorage`, which requires this flag.

```jsonc
{
  "compatibility_flags": ["nodejs_compat"],
}
```

*Other available variations of the above snippet: Toml*

Node.js: Initialize Sentry Before Your App

Node.js requires Sentry to initialize before your application loads so it can instrument third-party libraries (like database clients). Create a separate initialization file:

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/options.md#tracesSampleRate)
* Profiling: via [`profileSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/options.md#profileSessionSampleRate), [`profileLifecycle`](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/options.md#profileLifecycle), and `nodeProfilingIntegration()`

Don't need a feature? Remove its integration and options from the snippet.

```typescript
// IMPORTANT: import from `@sentry/hono/node`, not `@sentry/node`
import * as Sentry from "@sentry/hono/node";
import { nodeProfilingIntegration } from "@sentry/profiling-node";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  integrations: [
    // enables Profiling
    nodeProfilingIntegration(),
  ],

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,

  // Enables Profiling for every session.
  profileSessionSampleRate: 1.0,
  profileLifecycle: "trace",
});
```

Load this file with the `--import` flag when starting your app. You can also set this as an environment variable instead:

```bash
node --import ./instrument.mjs app.js
```

*Other available variations of the above snippet: ENV Variable*

### [Add the Sentry Middleware](https://docs.sentry.io/platforms/javascript/guides/hono.md#add-the-sentry-middleware)

Add the `sentry()` middleware as early as possible in your Hono app.

Before continuing, make sure you've completed the runtime-specific steps above: **Cloudflare Workers** users need to enable Node.js compatibility, and **Node.js** users need to create the instrument file. Since Node.js initializes Sentry in that file, the middleware doesn't take any options.

For Cloudflare Workers, Bun, and Deno, the snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/options.md#tracesSampleRate)

**\[Cloudflare Workers] index.ts**

```typescript
import { Hono } from "hono";
import { sentry } from "@sentry/hono/cloudflare";

const app = new Hono();

app.use(
  sentry(app, {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,
  }),
);

// Your routes here

export default app;
```

**\[Node.js] app.ts**

```typescript
import { Hono } from "hono";
import { serve } from "@hono/node-server";
import { sentry } from "@sentry/hono/node";

const app = new Hono();

app.use(sentry(app));

// Your routes here

serve(app);
```

**\[Bun] index.ts**

```typescript
import { Hono } from "hono";
import { sentry } from "@sentry/hono/bun";

const app = new Hono();

app.use(
  sentry(app, {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,
  }),
);

// Your routes here

export default app;
```

**\[Deno] index.ts**

```typescript
import { Hono } from "hono";
import { sentry } from "@sentry/hono/deno";

const app = new Hono();

app.use(
  sentry(app, {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,
  }),
);

// Your routes here

Deno.serve(app.fetch);
```

Cloudflare Workers: Accessing env from Worker Bindings

To access environment variables from your Cloudflare Worker bindings (for example, to store the DSN as a secret), pass a callback instead of a plain options object. The function receives the Worker `env`:

```typescript
import { Hono } from "hono";
import { sentry } from "@sentry/hono/cloudflare";

type Bindings = { SENTRY_DSN: string };

const app = new Hono<{ Bindings: Bindings }>();

app.use(sentry(app, (env) => ({ dsn: env.SENTRY_DSN })));

export default app;
```

### [Report Unhandled Exceptions](https://docs.sentry.io/platforms/javascript/guides/hono.md#report-unhandled-exceptions)

By default, Sentry captures exceptions from Hono's `onError` handler, excluding errors with 3xx or 4xx status codes. No additional configuration is needed for this.

To control which errors are captured, use the [`shouldHandleError`](https://docs.sentry.io/platforms/javascript/guides/hono/features/error-handler.md) option.

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/hono.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/hono/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/hono.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/hono.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md) for all available logging methods and the syntax for formatting messages.

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

* Node.js and Bun: [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md#console-integration) for `console` calls, [Consola](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md#console-integration), and [Pino](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/integrations/pino.md)
* Deno and Cloudflare Workers: [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md#console-integration) for `console` calls

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/hono.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/hono/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

You can also collect runtime health metrics automatically with the following integrations:

* Node.js: [`nodeRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/integrations/noderuntimemetrics.md)
* Bun: [`bunRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/bun/configuration/integrations/bunruntimemetrics.md)
* Deno: [`denoRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/deno/configuration/integrations/denoruntimemetrics.md)

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/hono.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test route to your Hono app that throws an error, then request `/debug-sentry` to trigger it:

```typescript
app.get("/debug-sentry", () => {
  throw new Error("Sentry Test Error");
});
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/hono.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/hono.md#next-steps)

At this point, you should have integrated Sentry into your Hono application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/hono/agent-tracing.md) to monitor your AI systems
* Explore [Hono-specific features](https://docs.sentry.io/platforms/javascript/guides/hono/features.md) like custom error filtering

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/hono/troubleshooting.md)
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

- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/hono/install.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/hono/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/hono/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/hono/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/hono/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/hono/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/hono/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/hono/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/hono/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/hono/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/hono/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/hono/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/hono/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/hono/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/hono/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/hono/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/hono/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/hono/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/hono/troubleshooting.md)
- [Hono Features](https://docs.sentry.io/platforms/javascript/guides/hono/features.md)

