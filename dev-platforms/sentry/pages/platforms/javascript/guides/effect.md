---
title: "Effect"
source: https://docs.sentry.io/platforms/javascript/guides/effect.md
path: platforms/javascript/guides/effect
---

---
title: "Effect"
description: "Learn how to set up and configure Sentry in your Effect application, capture your first events and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/effect/
---

# Sentry for Effect

##### Important

This SDK is currently in **ALPHA**. Alpha features are still in progress, may have bugs, and might include breaking changes. Please reach out on [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if you have any feedback or concerns.

This guide will show you how to integrate Sentry into your [Effect](https://effect.website/) project using the `@sentry/effect` SDK.

`@sentry/effect` supports **Effect v3** and **Effect v4**. The integration automatically detects which version you have installed, but the `Tracer` and `Logger` layer APIs differ between major versions. Make sure to follow the correct code snippets for your version below.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/effect.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

## [Install](https://docs.sentry.io/platforms/javascript/guides/effect.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/effect.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application.

```bash
npm install @sentry/effect --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/effect.md#configure)

**Error Monitoring** starts working as soon as you provide `Sentry.effectLayer()`. **Logs** and **Application Metrics** need no extra SDK configuration. To forward Effect-native logs and metrics, use the Sentry Effect logger and metrics layers shown in this guide. You'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/effect.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/effect.md#send-application-metrics-). This guide also enables **Tracing**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

The SDK provides an `effectLayer` that initializes Sentry. You can compose it with additional Effect layers to enable tracing, logging, and metrics. The `effectLayer`, `SentryEffectTracer`, `SentryEffectLogger`, and `SentryEffectMetricsLayer` exports are the same for Effect v3 and v4. The only difference between versions is how you compose layers for tracing and logging, which is covered in the snippets below.

### [Effect v3](https://docs.sentry.io/platforms/javascript/guides/effect.md#effect-v3)

Available since: `v10.44.0`

* Node: Provide `SentryLive` before launching your HTTP layer (for example, with `NodeRuntime`).
* Browser: Provide `SentryLive` to your app layer.

In both cases, use `Layer.setTracer` to configure tracing and `Logger.replace` to configure logging.

The snippets also turn on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/effect/configuration/options.md#tracesSampleRate) and the Effect tracer layer
* Logs: via `SentryEffectLogger`
* Application Metrics: via `SentryEffectMetricsLayer`

Don't need a feature? Remove its layer and options from the snippet.

```typescript
import * as Sentry from "@sentry/effect";
import { NodeRuntime } from "@effect/platform-node";
import * as Logger from "effect/Logger";
import * as Layer from "effect/Layer";
import { HttpLive } from "./Http.js";

const SentryLive = Layer.mergeAll(
  Sentry.effectLayer({
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,
  }),

  // Enable Effect tracing
  Layer.setTracer(Sentry.SentryEffectTracer),

  // Forward Effect logs to Sentry
  Logger.replace(Logger.defaultLogger, Sentry.SentryEffectLogger),

  // Forward Effect metrics to Sentry
  Sentry.SentryEffectMetricsLayer,
);

const MainLive = HttpLive.pipe(Layer.provide(SentryLive));

MainLive.pipe(Layer.launch, NodeRuntime.runMain);
```

*Other available variations of the above snippet: Client*

### [Effect v4](https://docs.sentry.io/platforms/javascript/guides/effect.md#effect-v4)

Available since: `v10.50.0`

Effect v4 changes how you install the default `Tracer` and `Logger` services. Use `Layer.succeed(Tracer.Tracer, …)` plus `Logger.layer([…])`.

With SDK version 10.75.0 or higher, `effectLayer` also registers a Sentry `ErrorReporter`. Sentry then captures the failures that Effect reports, for example a route handler of Effect's HTTP server that fails. Learn more in [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/effect/usage.md#effect-v4).

```typescript
import * as Sentry from "@sentry/effect";
import { NodeRuntime } from "@effect/platform-node";
import * as Logger from "effect/Logger";
import * as Layer from "effect/Layer";
import * as Tracer from "effect/Tracer";
import { HttpLive } from "./Http.js";

const SentryLive = Layer.mergeAll(
  Sentry.effectLayer({
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,
  }),

  // Enable Effect tracing
  Layer.succeed(Tracer.Tracer, Sentry.SentryEffectTracer),

  // Forward Effect logs to Sentry
  Logger.layer([Sentry.SentryEffectLogger]),

  // Forward Effect metrics to Sentry
  Sentry.SentryEffectMetricsLayer,
);

const MainLive = HttpLive.pipe(Layer.provide(SentryLive));

MainLive.pipe(Layer.launch, NodeRuntime.runMain);
```

*Other available variations of the above snippet: Client*

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/effect.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/effect/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/effect.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/effect/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/effect.md#send-logs)

The Effect logger layer forwards `Effect.log` messages to Sentry. The v3 and v4 layer setup is included in the configuration snippets above.

See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/effect/logs.md) for logging methods and message formatting.

```typescript
import { Effect } from "effect";

const program = Effect.gen(function* () {
  yield* Effect.log("User example action completed");
  yield* Effect.logWarning("Slow operation detected").pipe(
    Effect.annotateLogs({ operation: "data_fetch", duration: "3500ms" }),
  );
});
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/effect.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/effect/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/effect.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Run an Effect that fails using the layer that includes `Sentry.effectLayer()`:

```typescript
import { Effect } from "effect";

const program = Effect.fail(new Error("Sentry Test Error"));

// Run with your layer that includes Sentry.effectLayer().
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/effect.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/effect.md#next-steps)

At this point, you should have integrated Sentry into your Effect application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/effect/agent-tracing.md) to monitor your AI systems

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/effect/troubleshooting.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/effect/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/effect/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/effect/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/effect/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/effect/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/effect/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/effect/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/effect/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/effect/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/effect/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/effect/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/effect/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/effect/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/effect/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/effect/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/effect/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/effect/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/effect/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/effect/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/effect/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/effect/troubleshooting.md)

