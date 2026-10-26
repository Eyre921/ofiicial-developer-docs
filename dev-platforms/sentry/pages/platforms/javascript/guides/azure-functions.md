---
title: "Azure Functions"
source: https://docs.sentry.io/platforms/javascript/guides/azure-functions.md
path: platforms/javascript/guides/azure-functions
---

---
title: "Azure Functions"
description: "Learn how to manually set up Sentry in your Azure Functions and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/azure-functions/
---

# Sentry for Azure Functions (JavaScript)

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Node version `20.19.0` or above. Node.js 22 needs `22.12` or higher, while Node.js 23 needs `23.2` or higher (`>=20.19.0 <22.0.0 || >=22.12.0 <23.0.0 || >=23.2.0`).

## [Install](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add `@sentry/node` as a runtime dependency to your application:

```bash
npm install @sentry/node --save
```

*Other available variations of the above snippet: yarn, pnpm*

```bash
npm install @sentry/node @sentry/profiling-node --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration/options.md#tracesSampleRate)
* Profiling: via [`profileSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration/options.md#profileSessionSampleRate) and [`nodeProfilingIntegration()`](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration/integrations/nodeprofiling.md)

Don't need a feature? Remove its integration and options from the snippet.

Make sure to initialize Sentry at the top of your function file before importing any other modules:

```javascript
const Sentry = require("@sentry/node");
const { nodeProfilingIntegration } = require("@sentry/profiling-node");
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  integrations: [nodeProfilingIntegration()],
  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,

  // Enables Profiling.
  // Set to 1.0 to profile every session.
  // We recommend reducing this value in production.
  profileSessionSampleRate: 1.0,
});

// your function code
```

### [Capture Errors](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#capture-errors)

Because Azure Functions are short-lived, you have to explicitly `flush` Sentry events after calling `captureException`, or they may be lost before being sent to Sentry.

```javascript
const Sentry = require("@sentry/node");

// your Sentry init code

module.exports = async function (context, req) {
  try {
    // Your function code
  } catch (e) {
    // use Sentry.withScope to enrich the event with request data
    Sentry.withScope((scope) => {
      // Attach request context (requires dataCollection: { userInfo: true })
      scope.setSDKProcessingMetadata({ request: req });
      Sentry.captureException(e);
    });
    await Sentry.flush(2000);
  }
  // ...
};
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/azure-functions/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/azure-functions/logs.md) for all available logging methods and the syntax for formatting messages.

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

* [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/azure-functions/logs.md#console-integration) for `console` calls
* [Consola](https://docs.sentry.io/platforms/javascript/guides/azure-functions/logs.md#console-integration)
* [Pino](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration/integrations/pino.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/azure-functions/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

On Node.js, [`nodeRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration/integrations/noderuntimemetrics.md) also collects runtime health metrics automatically.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add an intentional error in your function and flush the event before the function execution ends:

```javascript
const Sentry = require("@sentry/node");

module.exports = async function (context, req) {
  try {
    throw new Error("Sentry Test Error");
  } catch (error) {
    Sentry.captureException(error);
    await Sentry.flush(2000);
  }
};
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page, select a transaction, and then a profile ID to view its flame graph. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md#next-steps)

At this point, you should have integrated Sentry into your Azure Functions application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/azure-functions/agent-tracing.md) to monitor your AI systems

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/azure-functions/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/azure-functions/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/azure-functions/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/azure-functions/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/azure-functions/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/azure-functions/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/azure-functions/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/azure-functions/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/azure-functions/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/azure-functions/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/azure-functions/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/azure-functions/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/azure-functions/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/azure-functions/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/azure-functions/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/azure-functions/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/azure-functions/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/azure-functions/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/azure-functions/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/azure-functions/troubleshooting.md)

