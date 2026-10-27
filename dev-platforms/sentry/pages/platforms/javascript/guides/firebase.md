---
title: "Cloud Functions for Firebase"
source: https://docs.sentry.io/platforms/javascript/guides/firebase.md
path: platforms/javascript/guides/firebase
---

---
title: "Cloud Functions for Firebase"
description: "Learn how to set up Sentry in your Cloud Functions for Firebase project and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/firebase/
---

# Sentry for Cloud Functions for Firebase

[Cloud Functions for Firebase](https://firebase.google.com/docs/functions) let you automatically run backend code in response to events triggered by Firebase features and HTTPS requests. Sentry's Node SDK works out of the box with Cloud Functions for Firebase.

## [What's Instrumented](https://docs.sentry.io/platforms/javascript/guides/firebase.md#whats-instrumented)

The Sentry SDK includes a built-in [Firebase integration](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/integrations/firebase.md) that automatically instruments:

* **Cloud Functions** - HTTP functions, background functions, and event triggers
* **[Firestore](https://firebase.google.com/docs/firestore)** - Database operations like reads, writes, and queries are instrumented out of the box

This integration is enabled by default, so you get automatic performance monitoring and error tracking without any additional configuration.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/firebase.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Node version `20.19.0` or above. Node.js 22 needs `22.12` or higher, while Node.js 23 needs `23.2` or higher (`>=20.19.0 <22.0.0 || >=22.12.0 <23.0.0 || >=23.2.0`).

## [Install](https://docs.sentry.io/platforms/javascript/guides/firebase.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/firebase.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your Firebase Functions project:

```bash
npm install @sentry/node @sentry/profiling-node --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/firebase.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/firebase.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/firebase.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

Create an initialization file (for example, `instrument.js`) that imports and initializes Sentry.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/options.md#tracesSampleRate)
* Profiling: via [`profileSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/options.md#profileSessionSampleRate), [`profileLifecycle`](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/options.md#profileLifecycle), and the profiling integration

Don't need a feature? Remove its integration and options from the snippet.

```javascript
const Sentry = require("@sentry/node");
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

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

Import the initialization file at the very top of your functions entry point (for example, `index.js`), before any other imports:

It's important that you import the initialization file **before** any other `require` calls, including Firebase imports. This ensures Sentry can properly instrument all modules.

```javascript
require("./instrument"); // Require Sentry initialization first

const { onRequest } = require("firebase-functions/https");
const { onDocumentCreated } = require("firebase-functions/firestore");
const admin = require("firebase-admin");

admin.initializeApp();

// HTTP function - automatically instrumented
exports.helloWorld = onRequest(async (request, response) => {
  response.send("Hello from Firebase!");
});

// Firestore trigger - automatically instrumented
exports.onUserCreated = onDocumentCreated(
  "users/{userId}",
  async (event) => {
    const userId = event.params.userId;
    // Your logic here
  },
);
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/firebase.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/firebase/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/firebase.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/firebase.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/firebase/logs.md) for all available logging methods and the syntax for formatting messages.

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

* [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/firebase/logs.md#console-integration) for `console` calls
* [Consola](https://docs.sentry.io/platforms/javascript/guides/firebase/logs.md#console-integration)
* [Pino](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/integrations/pino.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/firebase.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/firebase/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

On Node.js, [`nodeRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration/integrations/noderuntimemetrics.md) also collects runtime health metrics automatically.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/firebase.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test function that throws an error, deploy your functions, and trigger the test endpoint:

```javascript
require("./instrument");
const { onRequest } = require("firebase-functions/https");

exports.testSentry = onRequest(async () => {
  throw new Error("Sentry Test Error");
});
```

*Other available variations of the above snippet: bash*

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/firebase.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/firebase.md#next-steps)

At this point, you should have integrated Sentry into your Cloud Functions for Firebase application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/firebase/agent-tracing.md) to monitor your AI systems
* Explore [Tracing](https://docs.sentry.io/platforms/javascript/guides/firebase/tracing.md) to learn how to inspect application performance

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/firebase/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/firebase/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/firebase/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/firebase/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/firebase/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/firebase/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/firebase/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/firebase/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/firebase/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/firebase/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/firebase/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/firebase/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/firebase/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/firebase/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/firebase/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/firebase/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/firebase/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/firebase/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/firebase/troubleshooting.md)

