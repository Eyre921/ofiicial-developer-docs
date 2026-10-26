---
title: "Elysia"
source: https://docs.sentry.io/platforms/javascript/guides/elysia.md
path: platforms/javascript/guides/elysia
---

---
title: "Elysia"
description: "Learn how to set up Sentry in your Elysia app and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/elysia/
---

# Sentry for Elysia

This SDK is currently in **ALPHA**. Alpha features are still in progress, may have bugs, and might include breaking changes. Please reach out on [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if you have any feedback or concerns.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/elysia.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* An Elysia application (`v1.4.0+`)
* Bun or Node.js 20.19.0+ (with [@elysiajs/node](https://elysiajs.com/integrations/node) adapter)

## [Install](https://docs.sentry.io/platforms/javascript/guides/elysia.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/elysia.md#install-the-sentry-sdk)

Run the command for your runtime and preferred package manager to add the Sentry SDK to your application:

**Bun**

```bash
bun add @sentry/elysia
```

**Node.js**

```bash
npm install @sentry/elysia @elysiajs/node
# or
yarn add @sentry/elysia @elysiajs/node
# or
pnpm add @sentry/elysia @elysiajs/node
```

You do **not** need `@elysiajs/opentelemetry`. The `@sentry/elysia` SDK handles all instrumentation natively.

## [Configure](https://docs.sentry.io/platforms/javascript/guides/elysia.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/elysia.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/elysia.md#send-application-metrics-). This guide also enables **Tracing**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

Call `Sentry.init()` before creating your Elysia app, then wrap the app with `Sentry.withElysia()` before defining routes.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/elysia/configuration/options.md#tracesSampleRate)

Don't need a feature? Remove its integration and options from the snippet.

**\[Bun] index.ts**

```javascript
import * as Sentry from "@sentry/elysia";
import { Elysia } from "elysia";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
});

// withElysia returns the app instance, so you can chain routes directly
const app = Sentry.withElysia(new Elysia())
  .get("/", () => "Hello World")
  .listen(3000);
```

**\[Node.js] index.ts**

```javascript
import * as Sentry from "@sentry/elysia";
import { Elysia } from "elysia";
import { node } from "@elysiajs/node";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
});

// withElysia returns the app instance, so you can chain routes directly
const app = Sentry.withElysia(new Elysia({ adapter: node() }))
  .get("/", () => "Hello World")
  .listen(3000);
```

### [Customize Automatic Error Capturing](https://docs.sentry.io/platforms/javascript/guides/elysia.md#customize-automatic-error-capturing)

The SDK captures 5xx errors automatically via a global `onError` hook. Client errors (3xx/4xx) are not captured by default. You can customize which errors are captured using the `shouldHandleError` option.

```javascript
const app = Sentry.withElysia(new Elysia(), {
  shouldHandleError: (context) => {
    const status = context.set.status;
    return status === 500 || status === 503;
  },
});
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/elysia.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/elysia/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/elysia.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/elysia/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/elysia.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/elysia/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you're already logging with `console` or Consola, you can capture those logs with [our console integrations](https://docs.sentry.io/platforms/javascript/guides/elysia/logs.md#console-integration).

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/elysia.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/elysia/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/elysia.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a route to your app that throws an error:

```javascript
app.get("/debug-sentry", () => {
  throw new Error("Sentry Test Error");
});
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/elysia.md#view-captured-data-in-sentry)

Finally, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/elysia.md#next-steps)

At this point, you should have integrated Sentry into your Elysia application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/elysia/agent-tracing.md) to monitor your AI systems

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/elysia/troubleshooting.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/elysia/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/elysia/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/elysia/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/elysia/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/elysia/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/elysia/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/elysia/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/elysia/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/elysia/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/elysia/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/elysia/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/elysia/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/elysia/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/elysia/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/elysia/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/elysia/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/elysia/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/elysia/troubleshooting.md)

