---
title: "SolidStart"
source: https://docs.sentry.io/platforms/javascript/guides/solidstart.md
path: platforms/javascript/guides/solidstart
---

---
title: "SolidStart"
description: "Learn how to set up Sentry in your SolidStart application and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/solidstart/
---

# Sentry for SolidStart

##### Important

This SDK is currently in **beta**. Beta features are still in progress and may have bugs. Please reach out on [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if you have any feedback or concerns.

This SDK guide is specifically for SolidStart. For instrumenting your Solid app, see our [Solid SDK](https://docs.sentry.io/platforms/javascript/guides/solid.md).

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* SolidStart version `1.0.0`+ or `2.0.0`+

Are you using SolidStart 1?

SolidStart 2 dropped vinxi and `app.config.ts`, so the two versions are set up differently. Check the `@solidjs/start` version in your `package.json`; a new project installs SolidStart 2.

Where this guide shows **SolidStart 2** and **SolidStart 1** tabs, pick the one that matches your version. The [installation methods](https://docs.sentry.io/platforms/javascript/guides/solidstart/install.md) apply to SolidStart 1 only.

## [Install](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
npm install @sentry/solidstart --save
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#send-application-metrics-). This guide also enables **Tracing**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay/web.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what was happening in the user's browser before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

You need to initialize and configure the Sentry SDK in two places: the client side and the server side.

The examples in this guide will use TypeScript with a `src` folder structure. Make sure to adjust the file paths and extensions (`.js`, `.jsx`, `.ts`, `.tsx`) to match your project setup.

### [Configure Client-Side Sentry](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#configure-client-side-sentry)

Import and initialize the Sentry SDK in your `/src/entry-client.tsx` file. If you use Solid Router, add its tracing integration as shown below and wrap your router in the next step.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options.md#tracesSampleRate) and `solidRouterBrowserTracingIntegration()` if you're using Solid Router
* Session Replay: via `replayIntegration()`, sampled with [`replaysSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options.md#replaysSessionSampleRate) and [`replaysOnErrorSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options.md#replaysOnErrorSampleRate)
* User Feedback: via [`feedbackIntegration()`](https://docs.sentry.io/platforms/javascript/guides/solidstart/user-feedback/configuration.md)

Don't need a feature? Remove its integration and options from the snippet.

```jsx
import * as Sentry from "@sentry/solidstart";
// import solidRouterBrowserTracingIntegration if you're using Solid Router
import { solidRouterBrowserTracingIntegration } from "@sentry/solidstart/solidrouter";
import { mount, StartClient } from "@solidjs/start/client";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  integrations: [
    // add solidRouterBrowserTracingIntegration if you're using Solid Router
    // enables automatic instrumentation
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

  // Capture replays for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Requires Sentry.replayIntegration()
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});

mount(() => <StartClient />, document.getElementById("app"));
```

### [Configure Server-Side Sentry](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#configure-server-side-sentry)

Initialize Sentry on the server. On SolidStart 2, do this in a Nitro startup plugin, which runs once when the server starts. On SolidStart 1, create an `instrument.server.ts` file in your `src` folder.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options.md#tracesSampleRate)

**\[SolidStart 2] server/plugins/sentry.ts**

```typescript
import * as Sentry from "@sentry/solidstart";
import { definePlugin } from "nitro";

export default definePlugin(() => {
  Sentry.init({
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,
  });
});
```

**\[SolidStart 1] src/instrument.server.ts**

```javascript
import * as Sentry from "@sentry/solidstart";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
});
```

### [Server Instrumentation](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#server-instrumentation)

The Sentry SDK provides [middleware lifecycle](https://docs.solidjs.com/solid-start/advanced/middleware) handlers that enhance the data collected by Sentry on the server side, enabling distributed tracing between the client and server.

Create or update your `src/middleware.ts` file and add the `sentryBeforeResponseMiddleware` handler:

```typescript
import { sentryBeforeResponseMiddleware } from "@sentry/solidstart";
import { createMiddleware } from "@solidjs/start/middleware";

export default createMiddleware({
  onBeforeResponse: [
    sentryBeforeResponseMiddleware(),
    // Add your other middleware handlers after `sentryBeforeResponseMiddleware`
  ],
});
```

Add the Sentry plugin to your build config and register the middleware you just created. On SolidStart 2, add `sentrySolidStart` to `vite.config.ts`. On SolidStart 1, wrap your `app.config.ts` with `withSentry` so that the instrumentation file gets included in your build output.

**\[SolidStart 2] vite.config.ts**

```typescript
import { sentrySolidStart } from "@sentry/solidstart/vite";
import { solidStart } from "@solidjs/start/config";
import { nitro } from "nitro/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    solidStart({
      middleware: "./src/middleware.ts",
    }),
    sentrySolidStart(),
    nitro(),
  ],
});
```

**\[SolidStart 1] app.config.ts**

```javascript
import { withSentry } from "@sentry/solidstart";
import { defineConfig } from "@solidjs/start/config";

export default defineConfig(
  withSentry(
    {
      // other SolidStart config options...
      middleware: "./src/middleware.ts",
    },
    {
      // Your Sentry build-time config (such as source map upload options)
      // optional: if your `instrument.server.ts` file is not located inside `src`
      instrumentation: "./mypath/instrument.server.ts",
    },
  ),
);
```

### [Configure Solid Router](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#configure-solid-router)

If you're using Solid Router and the Sentry `solidRouterBrowserTracingIntegration` integration, wrap your Solid Router with `withSentryRouterRouting` to enable Sentry to collect navigation spans:

```tsx
import { Router } from "@solidjs/router";
import { FileRoutes } from "@solidjs/start/router";
import { withSentryRouterRouting } from "@sentry/solidstart/solidrouter";

const SentryRouter = withSentryRouterRouting(Router);

export default function App() {
  return (
    <SentryRouter>
      <FileRoutes />
    </SentryRouter>
  );
}
```

### [Run Your Application](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#run-your-application)

On SolidStart 2, the Vite plugin instruments your dependencies at build time, so the server needs no preload flag. Build with `vite build` and start the output directly.

On SolidStart 1, instrumentation has to happen as early as possible, so add an `--import` flag pointing at the instrumentation file that the build output creates: `.output/server/instrument.server.mjs`.

On SolidStart 1, run your build command to generate the `instrument.server.mjs` file before running your app. Depending on your build preset, the location of the file can differ. To find out where the file is located, monitor the build log output for:

`[Sentry SolidStart withSentry] Successfully created /my/project/path/.output/server/instrument.server.mjs.`

If you're not able to use the `--import` flag on SolidStart 1, check the alternative [installation methods](https://docs.sentry.io/platforms/javascript/guides/solidstart/install.md).

For example, update your scripts in `package.json`:

**\[SolidStart 2] package.json**

```json
{
  "scripts": {
    "build": "vite build",
    "start": "node .output/server/index.mjs"
  }
}
```

**\[SolidStart 1] package.json**

```json
{
  "scripts": {
    "start:vinxi": "NODE_OPTIONS='--import ./.output/server/instrument.server.mjs ' vinxi start",
    "start:node": "node --import ./.output/server/instrument.server.mjs .output/server/index.mjs"
  }
}
```

### [Capture Solid Errors](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#capture-solid-errors)

To automatically report exceptions from inside a component tree to Sentry, wrap Solid's `ErrorBoundary` with Sentry's helper function:

```jsx
import * as Sentry from "@sentry/solidstart";
import { ErrorBoundary } from "solid-js";

// Wrap Solid"s ErrorBoundary to automatically capture exceptions
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

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#add-readable-stack-traces-with-source-maps)

To upload source maps for clear error stack traces, add your Sentry auth token, organization, and project slug to the Sentry plugin in your build config:

**\[SolidStart 2] vite.config.ts**

```typescript
import { sentrySolidStart } from "@sentry/solidstart/vite";
import { solidStart } from "@solidjs/start/config";
import { nitro } from "nitro/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    solidStart(),
    sentrySolidStart({
      org: "<your-org-slug>",
      project: "<your-project-slug>",
      // store your auth token in an environment variable
      authToken: process.env.SENTRY_AUTH_TOKEN,
    }),
    nitro(),
  ],
});
```

**\[SolidStart 1] app.config.ts**

```TypeScript
import { withSentry } from '@sentry/solidstart';
import { defineConfig } from '@solidjs/start/config';

export default defineConfig(
  withSentry(
    {
      /* Your SolidStart config */
    },
    {
      org: "<your-org-slug>",
      project: "<your-project-slug>",
      // store your auth token in an environment variable
      authToken: process.env.SENTRY_AUTH_TOKEN,
    }
  ),
);
```

To keep your auth token secure, always store it in an environment variable instead of directly in your files:

```bash
SENTRY_AUTH_TOKEN=<your-sentry-auth-token>
```

Alternatively, you can create a `.env.sentry-build-plugin` file:

```bash
SENTRY_ORG="<your-org-slug>"
SENTRY_PROJECT="<your-project-slug>"
SENTRY_AUTH_TOKEN="<your-sentry-auth-token>"
```

Using environment variables in Vite configs

Vite doesn't automatically load `.env` files into `process.env` when evaluating the config file. If you store your auth token in a `.env` file and want to access it via `process.env.SENTRY_AUTH_TOKEN`, use Vite's [`loadEnv`](https://vite.dev/guide/api-javascript#loadenv) helper.

Alternatively, use a `.env.sentry-build-plugin` file, which the Sentry plugin reads automatically.

```javascript
import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");

  return {
    plugins: [
      sentryVitePlugin({
        authToken: env.SENTRY_AUTH_TOKEN,
        // ...
      }),
    ],
  };
});
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/solidstart/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you already use `console`, capture those calls as Sentry Logs with [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/solidstart/logs.md#console-integration). We also provide integrations for:

* [Consola](https://docs.sentry.io/platforms/javascript/guides/solidstart/logs.md#console-integration)
* [Pino](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/integrations/pino.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/solidstart/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

On Node.js, [`nodeRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/integrations/noderuntimemetrics.md) also collects runtime health metrics automatically.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test button to an existing page. Clicking it throws an error that Sentry captures:

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

```jsx
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Test Sentry Error
</button>;
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/solidstart.md#next-steps)

At this point, you should have integrated Sentry into your SolidStart application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/solidstart/agent-tracing.md) to monitor your AI systems
* [Set up tunneling](https://docs.sentry.io/platforms/javascript/guides/solidstart/troubleshooting.md#dealing-with-ad-blockers) to avoid ad blockers blocking Sentry events

Are you having problems setting up the SDK?

* If you encountered issues with setting up Sentry, [review alternative installation methods](https://docs.sentry.io/platforms/javascript/guides/solidstart/install.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/solidstart/troubleshooting.md)
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
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/solidstart/install.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/solidstart/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/solidstart/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/solidstart/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/solidstart/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/solidstart/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/solidstart/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/solidstart/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/solidstart/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/solidstart/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/solidstart/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/solidstart/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/solidstart/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/solidstart/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/solidstart/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/solidstart/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/solidstart/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/solidstart/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/solidstart/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/solidstart/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/solidstart/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/solidstart/troubleshooting.md)
- [SolidStart Features](https://docs.sentry.io/platforms/javascript/guides/solidstart/features.md)

