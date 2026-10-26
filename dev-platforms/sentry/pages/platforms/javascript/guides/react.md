---
title: "React"
source: https://docs.sentry.io/platforms/javascript/guides/react.md
path: platforms/javascript/guides/react
---

---
title: "React"
description: "Learn how to set up Sentry in your React application and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/react/
---

# Sentry for React

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/react.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

##### Using React Server Components or a React framework?

If you're using Next.js, Remix, or another framework with server-side rendering, use the dedicated SDK instead:

* [Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)
* [Remix](https://docs.sentry.io/platforms/javascript/guides/remix.md)
* [Gatsby](https://docs.sentry.io/platforms/javascript/guides/gatsby.md)

This guide is for client-side React applications (SPAs) built with tools like Vite or custom bundler configurations.

## [Install](https://docs.sentry.io/platforms/javascript/guides/react.md#install)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/react --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/react.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/react.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/react.md#send-application-metrics-). This guide also enables **Tracing**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay/web.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what was happening in the user's browser before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

### [Initialize the SDK](https://docs.sentry.io/platforms/javascript/guides/react.md#initialize-the-sdk)

Create a file in your project's root directory (for example, `instrument.js`) and add your Sentry configuration. Import this file **before** any other imports in your application entry point.

The snippet also turns on:

* Tracing: via `browserTracingIntegration()` and [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#tracesSampleRate); [`tracePropagationTargets`](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#tracePropagationTargets) controls which API requests receive trace headers
* Session Replay: via `replayIntegration()`, sampled with [`replaysSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#replaysSessionSampleRate) and [`replaysOnErrorSampleRate`](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#replaysOnErrorSampleRate)
* User Feedback: via [`feedbackIntegration()`](https://docs.sentry.io/platforms/javascript/guides/react/user-feedback/configuration.md)

Don't need a feature? Remove its integration and options from the snippet.

```javascript
import * as Sentry from "@sentry/react";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
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

  // Set trace propagation targets for your API requests
  tracePropagationTargets: [/^\//, /^https:\/\/yourserver\.io\/api/],

  // Capture replays for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Requires Sentry.replayIntegration()
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

### [Apply Instrumentation to Your App](https://docs.sentry.io/platforms/javascript/guides/react.md#apply-instrumentation-to-your-app)

Import your Sentry configuration as the **first import** in your application entry point, then render your app.

```javascript
import "./instrument";
import App from "./App";
import { createRoot } from "react-dom/client";

const container = document.getElementById("app");
const root = createRoot(container);
root.render(<App />);
```

### [Capture React Errors (React 19+)](https://docs.sentry.io/platforms/javascript/guides/react.md#capture-react-errors-react-19)

React 19 introduced error hooks that integrate directly with Sentry. Configure `createRoot` or `hydrateRoot` with error handlers using `reactErrorHandler` for comprehensive error capture.

```javascript
import "./instrument";
import App from "./App";
import { createRoot } from "react-dom/client";
import * as Sentry from "@sentry/react";

const container = document.getElementById("app");
const root = createRoot(container, {
  // Called when an error is thrown and not caught by an ErrorBoundary.
  onUncaughtError: Sentry.reactErrorHandler((error, errorInfo) => {
    console.warn("Uncaught error", error, errorInfo.componentStack);
  }),
  // Called when React catches an error in an ErrorBoundary.
  onCaughtError: Sentry.reactErrorHandler(),
  // Called when React automatically recovers from errors.
  onRecoverableError: Sentry.reactErrorHandler(),
});
root.render(<App />);
```

Using React 18 or below?

Use the `ErrorBoundary` component to capture rendering errors and display a fallback UI.

```javascript
import React from "react";
import * as Sentry from "@sentry/react";

function App() {
  return (
    <Sentry.ErrorBoundary fallback={<p>An error has occurred</p>}>
      <YourAppContent />
    </Sentry.ErrorBoundary>
  );
}
```

Learn more about [ErrorBoundary options](https://docs.sentry.io/platforms/javascript/guides/react/features/error-boundary.md).

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/react.md#add-readable-stack-traces-with-source-maps)

Source maps are **essential for debugging production errors**. Without them, stack traces point to minified code.

Run the Sentry wizard to configure source map uploads for your bundler:

* **[Vite](https://docs.sentry.io/platforms/javascript/guides/react/sourcemaps/uploading/vite.md)** — Recommended for new projects
* **[Webpack](https://docs.sentry.io/platforms/javascript/guides/react/sourcemaps/uploading/webpack.md)** — Common in existing projects
* **[Rollup](https://docs.sentry.io/platforms/javascript/guides/react/sourcemaps/uploading/rollup.md)** or **[esbuild](https://docs.sentry.io/platforms/javascript/guides/react/sourcemaps/uploading/esbuild.md)** — For custom setups

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Set Up Routing](https://docs.sentry.io/platforms/javascript/guides/react.md#set-up-routing)

If you're using client-side routing, configure Sentry to capture navigation events for better performance insights.

* [React Router v7](https://docs.sentry.io/platforms/javascript/guides/react/features/react-router/v7.md)
* [React Router v6](https://docs.sentry.io/platforms/javascript/guides/react/features/react-router/v6.md)
* [Older versions](https://docs.sentry.io/platforms/javascript/guides/react/features/react-router.md)
* [TanStack Router](https://docs.sentry.io/platforms/javascript/guides/react/features/tanstack-router.md)

When using React Router, replace `browserTracingIntegration()` with the integration for your router version. For example:

```javascript
import React from "react";
import * as Sentry from "@sentry/react";
import {
  useLocation,
  useNavigationType,
  createRoutesFromChildren,
  matchRoutes,
} from "react-router";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  integrations: [
    // enables automatic instrumentation for React Router v7
    Sentry.reactRouterV7BrowserTracingIntegration({
      useEffect: React.useEffect,
      useLocation,
      useNavigationType,
      createRoutesFromChildren,
      matchRoutes,
    }),
    // enables Session Replay
    Sentry.replayIntegration(),
    // enables User Feedback
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
  ],

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
  tracePropagationTargets: [/^\\//, /^https:\\/\\/yourserver\\.io\\/api/],

  // Capture replays for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Requires Sentry.replayIntegration()
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

### [Capture Redux State Data](https://docs.sentry.io/platforms/javascript/guides/react.md#capture-redux-state-data)

Capture Redux state and actions with your errors using `Sentry.createReduxEnhancer`. Learn more about [Redux integration options](https://docs.sentry.io/platforms/javascript/guides/react/features/redux.md).

```javascript
import { createStore, compose } from "redux";
import * as Sentry from "@sentry/react";

const sentryEnhancer = Sentry.createReduxEnhancer();
const store = createStore(rootReducer, compose(sentryEnhancer));
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/react.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/react.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/react/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you're already logging with `console` or Consola, you can capture those logs with [our console integrations](https://docs.sentry.io/platforms/javascript/guides/react/logs.md#console-integration).

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/react.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/react/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/react.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test button to one of your components. Clicking it will trigger an error for Sentry to capture.

```javascript
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Test Sentry Error
</button>;
```

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/react.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/react.md#next-steps)

At this point, you should have integrated Sentry into your React application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up tunneling](https://docs.sentry.io/platforms/javascript/guides/react/troubleshooting.md#dealing-with-ad-blockers) to avoid ad blockers from blocking Sentry events
* Explore [React-specific features](https://docs.sentry.io/platforms/javascript/guides/react/features.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/react/troubleshooting.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/react/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/react/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/react/logs.md)
- [React Features](https://docs.sentry.io/platforms/javascript/guides/react/features.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/react/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/react/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/react/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/react/profiling.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/react/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/react/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/react/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/react/configuration.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/react/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/react/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/react/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/react/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/react/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/react/troubleshooting.md)

