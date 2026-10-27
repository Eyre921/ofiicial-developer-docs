---
title: "Solid"
source: https://docs.sentry.io/platforms/javascript/guides/solid.md
path: platforms/javascript/guides/solid
---

---
title: "Solid"
description: "Learn how to manually set up Sentry in your Solid app and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/solid/
---

# Sentry for Solid

This SDK guide is specifically for Solid. For instrumenting your SolidStart app, see our [SolidStart guide](https://docs.sentry.io/platforms/javascript/guides/solidstart.md).

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/solid.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Solid version `1.8.4`+

## [Install](https://docs.sentry.io/platforms/javascript/guides/solid.md#install)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/solid --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/solid.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/solid.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/solid.md#send-application-metrics-). This guide also enables **Tracing**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

### [Initialize the SDK](https://docs.sentry.io/platforms/javascript/guides/solid.md#initialize-the-sdk)

Initialize Sentry as early as possible in your application, for example, in your `index.(jsx|tsx)` file.

The snippet also turns on:

* Tracing: via `solidRouterBrowserTracingIntegration()` and [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solid/configuration/options.md#tracesSampleRate)
* Session Replay: via `replayIntegration()`, sampled with [`replaysSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solid/configuration/options.md#replaysSessionSampleRate) and [`replaysOnErrorSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solid/configuration/options.md#replaysOnErrorSampleRate)
* User Feedback: via [`feedbackIntegration()`](https://docs.sentry.io/platforms/javascript/guides/solid/user-feedback/configuration.md)

Don't need a feature? Remove its integration and options from the snippet.

```javascript
import * as Sentry from "@sentry/solid";
import { solidRouterBrowserTracingIntegration } from "@sentry/solid/solidrouter";
import { render } from "solid-js/web";
import { DEV } from "solid-js";
import App from "./app";

// Initialize Sentry only in production builds.
if (!DEV) {
  Sentry.init({
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    integrations: [
      // enables automatic instrumentation for Solid Router
      solidRouterBrowserTracingIntegration(),
      // enables Session Replay
      Sentry.replayIntegration(),
      // enables User Feedback
      Sentry.feedbackIntegration({
        // Additional integration configuration goes in here
        colorScheme: "system",
      }),
    ],

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,

    // Set trace propagation targets for your API requests
    tracePropagationTargets: [
      "localhost",
      /^https:\/\/yourserver\.io\/api/,
    ],

    // Capture replays for 10% of all sessions,
    // plus for 100% of sessions with an error
    // Requires Sentry.replayIntegration()
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  });
}

const app = document.getElementById("app");

if (!app) throw new Error("No #app element found in the DOM.");

render(() => <App />, app);
```

### [Capture Solid Errors](https://docs.sentry.io/platforms/javascript/guides/solid.md#capture-solid-errors)

To automatically report exceptions from inside a component tree to Sentry, wrap Solid's `ErrorBoundary` with Sentry's helper function:

```jsx
import * as Sentry from "@sentry/solid";
import { ErrorBoundary } from "solid-js";

// Wrap Solid's ErrorBoundary to automatically capture exceptions
const SentryErrorBoundary = Sentry.withSentryErrorBoundary(ErrorBoundary);

export default function SomeComponent() {
  return (
    <SentryErrorBoundary
      fallback={(err) => <div>Error: {err.message}</div>}
    >
      <div>Some Component</div>
    </SentryErrorBoundary>
  );
}
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/solid.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/solid/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/solid.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/solid/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/solid.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/solid/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you're already logging with `console` or Consola, you can capture those logs with [our console integrations](https://docs.sentry.io/platforms/javascript/guides/solid/logs.md#console-integration).

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/solid.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/solid/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/solid.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test button to one of your components. Clicking it will trigger an error for Sentry to capture.

```javascript
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Break the world
</button>;
```

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/solid.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/solid.md#next-steps)

At this point, you should have integrated Sentry into your Solid application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up tunneling](https://docs.sentry.io/platforms/javascript/guides/solid/troubleshooting.md#dealing-with-ad-blockers) to avoid ad blockers from blocking Sentry events
* Explore [Solid-specific features](https://docs.sentry.io/platforms/javascript/guides/solid/features.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/solid/troubleshooting.md)
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
- [Nitro](https://docs.sentry.io/platforms/javascript/guides/nitro.md)
- [Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md)
- [Nuxt](https://docs.sentry.io/platforms/javascript/guides/nuxt.md)
- [Pi Durable](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md)
- [React](https://docs.sentry.io/platforms/javascript/guides/react.md)
- [React Router Framework](https://docs.sentry.io/platforms/javascript/guides/react-router.md)
- [Remix](https://docs.sentry.io/platforms/javascript/guides/remix.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/solid/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/solid/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/solid/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/solid/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/solid/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/solid/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/solid/profiling.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/solid/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/solid/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/solid/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/solid/configuration.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/solid/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/solid/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/solid/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/solid/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/solid/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/solid/troubleshooting.md)
- [Solid Features](https://docs.sentry.io/platforms/javascript/guides/solid/features.md)

