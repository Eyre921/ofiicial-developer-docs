---
title: "JavaScript"
source: https://docs.sentry.io/platforms/javascript.md
path: platforms/javascript
---

---
title: "JavaScript"
description: "Learn how to manually set up Sentry in your JavaScript app and capture your first errors."
url: https://docs.sentry.io/platforms/javascript/
---

# Sentry for Browser JavaScript

##### Using a framework?

This guide focuses on plain JavaScript. If you're working with React, Next.js, or any other framework, choose the fitting SDK from the left-hand dropdown.

## [Prerequisites](https://docs.sentry.io/platforms/javascript.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

## [Install](https://docs.sentry.io/platforms/javascript.md#install)

We recommend installing Sentry via a package manager. If that isn't an option for you, you can use the [Loader Script](https://docs.sentry.io/platforms/javascript/install/loader.md) or a CDN bundle.

#### [Option 1: Package Manager (Recommended)](https://docs.sentry.io/platforms/javascript.md#option-1-package-manager-recommended)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/browser --save
```

*Other available variations of the above snippet: yarn, pnpm*

#### [Option 2: Loader Script](https://docs.sentry.io/platforms/javascript.md#option-2-loader-script)

In Sentry, go to **Settings > Projects > (select project) > SDK Setup > [Loader Script](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/loader-script/)**. Enable Tracing, Session Replay, Logs and Metrics, and User Feedback. Then, copy the script tag and place it before all other scripts in your app.

#### [Option 3: CDN Bundle](https://docs.sentry.io/platforms/javascript.md#option-3-cdn-bundle)

Sentry provides bundles with different feature combinations. In this guide, we'll use the [full bundle with all features](https://docs.sentry.io/platforms/javascript/install/loader.md#full-bundle-with-all-features). Copy the script tag and place it before all other scripts in your app.

If you're updating your Sentry SDK to the latest version, check out our [migration guide](https://docs.sentry.io/platforms/javascript/migration/v10-to-v11.md) to learn more about breaking changes.

## [Configure](https://docs.sentry.io/platforms/javascript.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript.md#send-application-metrics-). This guide also enables **Tracing**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

### [Initialize the SDK](https://docs.sentry.io/platforms/javascript.md#initialize-the-sdk)

Initialize Sentry as early as possible in your application's lifecycle. Use the tab that matches how you installed the SDK (npm, Loader, or CDN).

The snippet also turns on:

* Tracing: via `browserTracingIntegration()` and [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracesSampleRate)
* Session Replay: via `replayIntegration()`, sampled with [`replaysSessionSampleRate`](https://docs.sentry.io/platforms/javascript/configuration/options.md#replaysSessionSampleRate) and [`replaysOnErrorSampleRate`](https://docs.sentry.io/platforms/javascript/configuration/options.md#replaysOnErrorSampleRate)
* User Feedback: via [`feedbackIntegration()`](https://docs.sentry.io/platforms/javascript/user-feedback/configuration.md)

Don't need a feature?

Remove its integration and options from the `Sentry.init` snippet. Depending on how you installed the SDK, you may need one more step:

* **npm:** No additional steps.
* **Loader script:** Also turn off the feature in your Sentry project settings, then replace the loader script in your project with the updated one.
* **CDN bundle:** Also switch to a bundle that includes only the features you need. See the [list of available bundles](https://docs.sentry.io/platforms/javascript/install/loader.md#cdn).

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  // Alternatively, use `process.env.npm_package_version` for a dynamic release version
  // if your build tool supports it.
  release: "my-project-name@2.3.12",
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
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

  // Capture replays for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Requires Sentry.replayIntegration()
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

*Other available variations of the above snippet: Loader, CDN*

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you're already logging with `console` or [Consola](https://github.com/unjs/consola), you can capture those logs with [our console integrations](https://docs.sentry.io/platforms/javascript/logs.md#console-integration).

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test button to one of your pages. Open the page in a browser and click the button to trigger an error for Sentry to capture.

```html
<script>
  function triggerError() {
    throw new Error("Sentry Test Error");
  }
</script>

<button onclick="triggerError()">Break the World</button>
```

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript.md#next-steps)

At this point, you should have integrated Sentry into your JavaScript application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Extend Sentry to your backend using one of our [SDKs](https://docs.sentry.io/.md)
* [Set up tunneling](https://docs.sentry.io/platforms/javascript/troubleshooting.md#dealing-with-ad-blockers) to avoid ad blockers from blocking Sentry events

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Frameworks

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
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Installation Methods](https://docs.sentry.io/platforms/javascript/install.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/metrics.md)
- [JavaScript](https://docs.sentry.io/platforms/javascript/legacy-sdk.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/profiling.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/configuration.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/troubleshooting.md)

