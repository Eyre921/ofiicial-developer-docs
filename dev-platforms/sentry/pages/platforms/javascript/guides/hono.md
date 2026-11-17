---
title: "Hono"
source: https://docs.sentry.io/platforms/javascript/guides/hono.md
path: platforms/javascript/guides/hono
---

---
title: "Hono"
description: "Learn how to set up Sentry in your Hono app using the Sentry CLI, capture your first errors, logs, and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/hono/
---

# Sentry for Hono

The `@sentry/hono` SDK supports Hono 4+ across multiple runtimes: Cloudflare Workers, Node.js, Bun, and Deno. It works as Hono middleware, so you can drop it into your existing app with minimal setup.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/hono.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Hono version `4.0.0` or above

## [Install](https://docs.sentry.io/platforms/javascript/guides/hono.md#install)

The AI-powered `sentry init` flow is currently experimental. If you run into any issues, check out the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/hono/manual-setup.md) guide.

Run the Sentry init command in your project directory to automatically configure Sentry in your Hono application.

The command guides you through setup and asks which optional Sentry features you want to enable beyond error monitoring.

```bash
npx sentry@latest init
```

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back. On the server, this includes [Agent Tracing](https://docs.sentry.io/product/agents.md): supported AI libraries are instrumented automatically, so you can see model calls, tool executions, and token usage.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

How does sentry init work?

The `sentry init` command is AI-powered. It analyzes your project and generates a tailored integration, rather than applying a fixed template. Here's what it does:

* **Analyzes your project** — reads project files and manifests to understand your Hono app structure and the runtime it runs on, including monorepos. It also respects AI instruction files such as `CLAUDE.md`, `AGENTS.md`, and `.cursorrules`.
* **Detects your framework** — identifies Hono and selects the `@sentry/hono` SDK.
* **Fetches official Sentry docs** — uses the current Sentry documentation as the source of truth when generating integration code.
* **Installs dependencies** — adds `@sentry/hono` and the peer dependency for your runtime using your project's package manager.
* **Creates and modifies files** — sets up initialization and the Sentry middleware for your runtime, and other selected features based on your existing project structure.
* **Verifies the integration** — re-reads modified files after writing to confirm Sentry was integrated.

For full details on what each file does, see the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/hono/manual-setup.md) guide.

## [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/hono.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/hono/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/hono.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md) for all available logging methods and the syntax for formatting messages.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/hono.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/hono/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/hono.md#verify-your-setup)

The `sentry init` command checks the integration files it creates or modifies before it finishes. To confirm runtime events are reaching Sentry, add a test route to your Hono app that throws an error, then request `/debug-sentry` to trigger it:

```typescript
app.get("/debug-sentry", () => {
  throw new Error("Sentry Test Error");
});
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/hono.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/hono.md#next-steps)

At this point, you should have integrated Sentry into your Hono application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/hono/agent-tracing.md) to monitor your AI systems
* Explore [Hono-specific features](https://docs.sentry.io/platforms/javascript/guides/hono/features.md) like custom error filtering
* Read the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/hono/manual-setup.md) guide to learn what each file does and how to configure Sentry yourself

Are you having problems setting up the SDK?

* If you encountered issues with `sentry init`, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/hono/manual-setup.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/hono/troubleshooting.md)
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

- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/hono/install.md)
- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/hono/manual-setup.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/hono/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/hono/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/hono/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/hono/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/hono/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/hono/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/hono/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/hono/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/hono/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/hono/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/hono/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/hono/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/hono/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/hono/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/hono/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/hono/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/hono/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/hono/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/hono/troubleshooting.md)
- [Hono Features](https://docs.sentry.io/platforms/javascript/guides/hono/features.md)

