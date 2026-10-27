---
title: "Remix"
source: https://docs.sentry.io/platforms/javascript/guides/remix.md
path: platforms/javascript/guides/remix
---

---
title: "Remix"
description: "Learn how to set up and configure Sentry in your Remix application using the installation wizard, capture your first errors, and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/remix/
---

# Sentry for Remix

##### Using Remix 3?

This guide covers Remix 2. Support for [Remix 3](https://remix.run/blog/remix-3-beta-preview) is in alpha and has its own setup, see [Remix 3 (Alpha)](https://docs.sentry.io/platforms/javascript/guides/remix/remix-3.md).

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/remix.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Remix version `2.0.0`+

## [Install](https://docs.sentry.io/platforms/javascript/guides/remix.md#install)

To install Sentry using the installation wizard, run the following command within your project:

The wizard then guides you through the setup process, asking you to enable additional (optional) Sentry features for your application beyond error monitoring.

```bash
npx @sentry/wizard@latest -i remix
```

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

This guide assumes that you enable all features and allow the wizard to create an example page. You can add or remove features at any time, but setting them up now will save you the effort of configuring them manually later.

What does the installation wizard change inside your application?

* Creates or updates `entry.(client|server).tsx` to initialize the SDK
* Creates `.env.sentry-build-plugin` with an auth token to upload source maps (this file is automatically added to `.gitignore`)
* Updates your build script or Vite configuration to automatically upload source maps to Sentry
* Instruments your application to support Remix v2 features if you use [Remix future flags](https://remix.run/docs/en/main/pages/api-development-strategy#current-future-flags)
* Adds an example page to your application to help verify your Sentry setup

## [Configure Server-Side Performance Monitoring](https://docs.sentry.io/platforms/javascript/guides/remix.md#configure-server-side-performance-monitoring)

To capture performance data on the server side, wrap your Remix root component (`root.tsx`) with `withSentry`:

```tsx
import {
  Links,
  LiveReload,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";

import { withSentry } from "@sentry/remix";

function App() {
  return (
    <html>
      <head>
        <Meta />
        <Links />
      </head>
      <body>
        <Outlet />
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  );
}

export default withSentry(App);
```

## [Avoid Ad Blockers With Tunneling (Optional)](https://docs.sentry.io/platforms/javascript/guides/remix.md#avoid-ad-blockers-with-tunneling-optional)

You can prevent ad blockers from blocking Sentry events using tunneling. Use the `tunnel` option in `Sentry.init` to add an API endpoint in your application that forwards Sentry events to Sentry servers.

This will send all events to the `tunnel` endpoint. However, the events need to be parsed and redirected to Sentry, so you'll need to do additional configuration on the server. The endpoint must forward only the request body to Sentry and accept only your own DSN. You can find a detailed explanation on how to do this on our [Troubleshooting page](https://docs.sentry.io/platforms/javascript/guides/remix/troubleshooting.md#using-the-tunnel-option).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  tunnel: "/tunnel",
});
```

## [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/remix.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/remix/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/remix.md#verify-your-setup)

If you haven't tested your Sentry configuration yet, let's do it now. You can confirm that Sentry is working properly and sending data to your Sentry project by using the example page created by the installation wizard:

1. Open the example page `/sentry-example-page` in your browser. For most Remix applications, this will be at localhost.
2. Click the "Throw Sample Error" button to trigger a frontend error and trace.

##### Tip

Don't forget to explore the example page's code in your project to understand what's happening after your button click.

### [Verify Additional Features](https://docs.sentry.io/platforms/javascript/guides/remix.md#verify-additional-features)

**Logs** (enabled by default)

See structured log entries from your application. You can send logs from anywhere:

```typescript
Sentry.logger.info("User action", { userId: "123" });
Sentry.logger.warn("Slow response", { duration: 5000 });
Sentry.logger.error("Operation failed", { reason: "timeout" });
```

Learn more about [Logs configuration](https://docs.sentry.io/platforms/javascript/guides/remix/logs.md).

**Application Metrics** (enabled by default) NEW

Track and analyze custom application metrics to understand trends and patterns in your app's performance and behavior over time:

```typescript
Sentry.metrics.count("checkout.failed", 1);
Sentry.metrics.gauge("queue.depth", 42);
Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
});
```

Learn more about [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/remix/metrics.md).

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/remix.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/remix.md#next-steps)

At this point, you should have integrated Sentry into your Remix application and should already be sending error and performance data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/javascript/guides/remix/usage.md)
* Continue to [customize your configuration](https://docs.sentry.io/platforms/javascript/guides/remix/configuration.md)
* Get familiar with [Sentry's product features](https://docs.sentry.io/product.md) like tracing, insights, and alerts

Are you having problems setting up the SDK?

* If you encountered issues with our installation wizard, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/remix/manual-setup.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/remix/troubleshooting.md)
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
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/remix/manual-setup.md)
- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/remix/manual-setup__v8.x.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/remix/usage.md)
- [Remix 3 (Alpha)](https://docs.sentry.io/platforms/javascript/guides/remix/remix-3.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/remix/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/remix/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/remix/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/remix/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/remix/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/remix/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/remix/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/remix/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/remix/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/remix/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/remix/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/remix/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/remix/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/remix/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/remix/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/remix/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/remix/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/remix/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/remix/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/remix/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/remix/troubleshooting.md)
- [Cloudflare SDK Guide](https://docs.sentry.io/platforms/javascript/guides/remix/frameworks.md)

