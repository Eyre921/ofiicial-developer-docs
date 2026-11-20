---
title: "Astro"
source: https://docs.sentry.io/platforms/javascript/guides/astro.md
path: platforms/javascript/guides/astro
---

---
title: "Astro"
description: "Learn how to set up Sentry in your Astro app using the Sentry CLI, capture your first errors, logs, and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/astro/
---

# Sentry for Astro

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/astro.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Astro `4.0.0` or above
* If you're using Astro's Netlify adapter (`@astrojs/netlify`), you need version `5.0.0` or above

##### What runtime do you use?

This SDK currently only works on Node runtimes, such as Node adapter or Vercel with Lambda functions. If you use Cloudflare Workers or Cloudflare Pages, refer to our [Astro on Cloudflare guide](https://docs.sentry.io/platforms/javascript/guides/astro/manual-setup/cloudflare.md). Other non-Node runtimes, like Vercel's Edge runtime, are currently **not supported**.

## [Install](https://docs.sentry.io/platforms/javascript/guides/astro.md#install)

The AI-powered `sentry init` flow is currently experimental. If you run into any issues, check out the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/astro/manual-setup.md) guide.

Run the Sentry init command in your project directory to automatically configure Sentry in your Astro application.

The command guides you through setup and asks which optional Sentry features you want to enable beyond error monitoring.

```bash
npx sentry@latest init
```

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back. On the server, this includes [Agent Tracing](https://docs.sentry.io/product/agents.md): supported AI libraries are instrumented automatically, so you can see model calls, tool executions, and token usage.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

How does sentry init work?

The `sentry init` command is AI-powered. It analyzes your project and generates a tailored integration, rather than applying a fixed template. Here's what it does:

* **Analyzes your project** — reads project files and manifests to understand your Astro app structure, including monorepos. It also respects AI instruction files such as `CLAUDE.md`, `AGENTS.md`, and `.cursorrules`.
* **Detects your framework** — identifies Astro and selects the `@sentry/astro` SDK.
* **Fetches official Sentry docs** — uses the current Sentry documentation as the source of truth when generating integration code.
* **Installs dependencies** — adds `@sentry/astro` using your project's package manager.
* **Creates and modifies files** — registers the Sentry integration in your Astro config, sets up client-side and server-side initialization, and other selected features based on your existing project structure.
* **Verifies the integration** — re-reads modified files after writing to confirm Sentry was integrated.

For full details on what each file does, see the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/astro/manual-setup.md) guide.

## [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/astro.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/astro/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/astro.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/astro/logs.md) for all available logging methods and the syntax for formatting messages.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/javascript/guides/astro.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app to Sentry. You can pass any attributes you want and search or filter by them later. See [Set Up Metrics](https://docs.sentry.io/platforms/javascript/guides/astro/metrics.md) for all available metric types and configuration options.

```javascript
Sentry.metrics.count("checkout.failed", 1);

Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });

Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/astro.md#verify-your-setup)

The `sentry init` command checks the integration files it creates or modifies before it finishes. To confirm runtime events are reaching Sentry, add this button to a page in your Astro app and click it to send a test error:

```astro
<button id="test-error" type="button">Test Sentry Error</button>

<script>
  document.getElementById("test-error")?.addEventListener("click", () => {
    throw new Error("Sentry Test Error");
  });
</script>
```

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/astro.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/astro.md#next-steps)

At this point, you should have integrated Sentry into your Astro application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/astro/agent-tracing.md) to follow agent runs from system prompt to final output, capturing every model call, tool execution, and handoff as a span
* [Set up tunneling](https://docs.sentry.io/platforms/javascript/guides/astro/troubleshooting.md#dealing-with-ad-blockers) to avoid ad blockers blocking Sentry events
* Read the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/astro/manual-setup.md) guide to learn what each file does and how to configure Sentry yourself

Are you having problems setting up the SDK?

* If you encountered issues with `sentry init`, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/astro/manual-setup.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/astro/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
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

- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/astro/manual-setup.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/astro/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/astro/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/astro/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/astro/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/astro/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/astro/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/astro/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/astro/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/astro/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/astro/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/astro/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/astro/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/astro/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/astro/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/astro/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/astro/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/astro/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/astro/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/astro/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/astro/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/astro/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/astro/troubleshooting.md)

