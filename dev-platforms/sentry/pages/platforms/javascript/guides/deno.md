---
title: "Deno"
source: https://docs.sentry.io/platforms/javascript/guides/deno.md
path: platforms/javascript/guides/deno
---

---
title: "Deno"
description: "Learn how to manually set up Sentry in your Deno app and capture your first events."
url: https://docs.sentry.io/platforms/javascript/guides/deno/
---

# Sentry for Deno

This SDK is currently in **beta**. Beta features are still in progress and may have bugs. Please reach out on [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if you have any feedback or concerns

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/deno.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Deno version >= `2.8.3`

## [Install](https://docs.sentry.io/platforms/javascript/guides/deno.md#install)

### [Import the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/deno.md#import-the-sentry-sdk)

Import the Sentry Deno SDK directly from the npm registry, before importing any other modules:

```javascript
import * as Sentry from "<sdk-package-name>";
// your other imports
```

The Sentry import hook, which you load when you [start your app](https://docs.sentry.io/platforms/javascript/guides/deno.md#start-your-app), reads your dependencies from a local `node_modules` directory, not from Deno's global npm cache. Set `nodeModulesDir` in your `deno.json`:

```json
{
  "imports": {
    "@sentry/deno": "npm:@sentry/deno"
  },
  "nodeModulesDir": "auto"
}
```

## [Configure](https://docs.sentry.io/platforms/javascript/guides/deno.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/javascript/guides/deno.md#send-logs) and [#4](https://docs.sentry.io/platforms/javascript/guides/deno.md#send-application-metrics-). This guide also enables **Tracing**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/deno.md#initialize-the-sentry-sdk)

Initialize Sentry as early as possible in your app.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/deno/configuration/options.md#tracesSampleRate)

Don't need a feature? Remove its integration and options from the snippet.

```javascript
import * as Sentry from "<sdk-package-name>";
// your other imports

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,
});
```

### [Start Your App](https://docs.sentry.io/platforms/javascript/guides/deno.md#start-your-app)

Load the Sentry import hook with the `--preload` flag. The hook instruments your database drivers, message queues, AI libraries and web frameworks. An `import` statement in your entry file is too late for packages that ship ES modules, because Deno loads every module that your entry file imports before it runs any of them.

Deno blocks access to the network, the file system and system information until you grant it. Start your app with all four permissions so that the SDK can send complete events. Add the other hosts your app talks to, separated by commas:

```bash
deno run \
  --preload=<sdk-package-name>/import \
  --allow-net=o<orgId>.ingest.sentry.io \
  --allow-env \
  --allow-read=. \
  --allow-sys=hostname,osRelease \
  main.ts
```

What each permission gives you

| Flag                             | What it gives you                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--allow-net=<host>`             | Delivery of events to Sentry. If a host is missing, Deno names it in the error.                                                                                           |
| `--allow-env`                    | The import hook. Without it, your app stops at start with `NotCapable: Requires env access`.                                                                              |
| `--allow-read=.`                 | The import hook, source code in stack traces, and `app:///` paths instead of absolute paths. Without it, your app stops at start with `NotCapable: Requires read access`. |
| `--allow-sys=hostname,osRelease` | The server name and the operating system version on events.                                                                                                               |

If you omit `--allow-sys`, the SDK sends events without that data and prints no warning.

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/deno.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/deno/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/deno.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/deno/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/deno.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/deno/logs.md) for all available logging methods and the syntax for formatting messages.

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

If you're already logging with `console` or Consola, you can capture those logs with [our console integrations](https://docs.sentry.io/platforms/javascript/guides/deno/logs.md#console-integration).

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/deno.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/deno/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

For Deno, [`denoRuntimeMetricsIntegration`](https://docs.sentry.io/platforms/javascript/guides/deno/configuration/integrations/denoruntimemetrics.md) also collects runtime health metrics automatically.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/deno.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add an intentional error to your application:

```javascript
setTimeout(() => {
  throw new Error("Sentry Test Error");
}, 0);
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/deno.md#view-captured-data-in-sentry)

Finally, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/deno.md#next-steps)

At this point, you should have integrated Sentry into your Deno application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/deno/agent-tracing.md) to monitor your AI systems

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/deno/troubleshooting.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/deno/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/deno/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/deno/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/deno/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/deno/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/deno/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/deno/mcp-monitoring.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/deno/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/deno/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/deno/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/deno/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/deno/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/deno/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/deno/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/deno/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/deno/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/deno/troubleshooting.md)

