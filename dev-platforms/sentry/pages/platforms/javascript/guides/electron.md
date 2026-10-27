---
title: "Electron"
source: https://docs.sentry.io/platforms/javascript/guides/electron.md
path: platforms/javascript/guides/electron
---

---
title: "Electron"
description: "Learn how to manually set up Sentry in your Electron app and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/electron/
---

# Sentry for Electron

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/electron.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Electron version `35.0.0` or above

## [Install](https://docs.sentry.io/platforms/javascript/guides/electron.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/electron.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/electron --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/electron.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/electron.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/electron.md#send-application-metrics-). This guide also enables **Tracing**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

You should initialize the SDK in both the `main` process and every `renderer` process you spawn. Don't need a feature? Remove its integration and options from the respective snippet.

### [Configure the Main Process](https://docs.sentry.io/platforms/javascript/guides/electron.md#configure-the-main-process)

Initialize the SDK in your Electron `main` process as early as possible.

The main process snippets also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/electron/configuration/options.md#tracesSampleRate) and `startupTracingIntegration()`

```javascript
import * as Sentry from "@sentry/electron/main";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
  integrations: [
    // Enables startup tracing in the main process
    Sentry.startupTracingIntegration(),
  ],
});
```

### [Configure the Renderer Process](https://docs.sentry.io/platforms/javascript/guides/electron.md#configure-the-renderer-process)

Initialize the SDK in your Electron renderer processes as early as possible. All renderer events are sent through the main process so passing `dsn`, `release` or `environment` to renderer `init` will have no effect.

The renderer process snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/electron/configuration/options.md#tracesSampleRate) and `browserTracingIntegration()`
* Session Replay: via `replayIntegration()`, sampled with [`replaysSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/electron/configuration/options.md#replaysSessionSampleRate) and [`replaysOnErrorSampleRate`](https://docs.sentry.io/platforms/javascript/guides/electron/configuration/options.md#replaysOnErrorSampleRate)
* User Feedback: via [`feedbackIntegration()`](https://docs.sentry.io/platforms/javascript/guides/electron/user-feedback/configuration.md)

```javascript
import * as Sentry from "@sentry/electron/renderer";

Sentry.init({
  integrations: [
    // enables automatic instrumentation
    Sentry.browserTracingIntegration(),
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

  // Capture replays for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Requires Sentry.replayIntegration()
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

### [Configure Any Utility Processes](https://docs.sentry.io/platforms/javascript/guides/electron.md#configure-any-utility-processes)

If your app uses utility processes, initialize Sentry in each one.

```javascript
import * as Sentry from "@sentry/electron/utility";

Sentry.init();
```

##### Capturing errors in the preload context

If your app uses a preload script and `contextIsolation: true`, Sentry can't automatically capture errors that occur in the preload context. To include those, initialize Sentry in your preload script as well:

```javascript
import * as Sentry from "@sentry/electron/renderer";

Sentry.init(); // don't forget to add your configuration options
```

Did you change the userData directory?

If you change the `userData` directory used by your app, ensure this change is made before you configure the SDK as this path is used to cache scope and events between application restarts.

```javascript
import { app } from "electron";
import * as Sentry from "@sentry/electron/main";

app.setPath("userData", "~/.config/my-app");
Sentry.init({ dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>" });
```

### [Using Framework-Specific SDKs](https://docs.sentry.io/platforms/javascript/guides/electron.md#using-framework-specific-sdks)

If you're using a framework in your renderers, you can combine the Electron SDK with the framework SDK:

```javascript
import { init } from "@sentry/electron/renderer";
import { init as reactInit } from "@sentry/react";

init(
  {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    integrations: [
      /* integrations */
    ],
    /* Other Electron and React SDK config */
  },
  reactInit,
);
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/electron.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/electron/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/electron.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. The `userInfo` value set in the `main` process controls IP address inference for events from all processes. The other categories apply to the process where they are set. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/electron/configuration/options.md#dataCollection).

```javascript
import * as Sentry from "@sentry/electron/main";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/electron.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/electron/logs.md) for all available logging methods and the syntax for formatting messages.

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

* [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/electron/logs.md#console-integration) for `console` calls
* [Consola](https://docs.sentry.io/platforms/javascript/guides/electron/logs.md#console-integration)
* [Pino](https://docs.sentry.io/platforms/javascript/guides/electron/configuration/integrations/pino.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/electron.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/electron/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/electron.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test button to one of your renderer pages. Clicking it throws an error that Sentry captures:

```javascript
document.getElementById("testError").addEventListener("click", () => {
  throw new Error("Sentry Test Error");
});
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/electron.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/electron.md#next-steps)

At this point, you should have integrated Sentry into your Electron application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Explore Electron-specific features](https://docs.sentry.io/platforms/javascript/guides/electron/features.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/electron/troubleshooting.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/electron/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/electron/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/electron/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/electron/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/electron/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/electron/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/electron/profiling.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/electron/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/electron/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/electron/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/electron/configuration.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/electron/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/electron/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/electron/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/electron/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/electron/troubleshooting.md)
- [Electron Features](https://docs.sentry.io/platforms/javascript/guides/electron/features.md)

