---
title: "Nuxt"
source: https://docs.sentry.io/platforms/javascript/guides/nuxt.md
path: platforms/javascript/guides/nuxt
---

---
title: "Nuxt"
description: "Learn how to set up and configure Sentry in your Nuxt application using the installation wizard, capture your first errors, and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/nuxt/
---

# Sentry for Nuxt

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Nuxt version `3.7.0` or above (`3.14.0`+ recommended)

Are you using Nuxt version < 3.14.0?

Add the following overrides:

```json
"overrides": {
  "ofetch": "^1.4.0",
  "@vercel/nft": "^0.27.4"
}
```

*Other available variations of the above snippet: yarn, pnpm*

## [Install](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#install)

The AI-powered `sentry init` flow is currently experimental. To use the existing framework-specific setup instead, see the option below, or check out the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup.md) guide.

Run the Sentry init command in your project directory to automatically configure Sentry in your Nuxt application.

The command guides you through setup and asks which optional Sentry features you want to enable beyond error monitoring.

```bash
npx sentry@latest init
```

How does sentry init work?

The `sentry init` command is AI-powered. It analyzes your project and generates a tailored integration, rather than applying a fixed template. Here's what it does:

* **Analyzes your project** — reads project files and manifests to understand your Nuxt app structure, including monorepos. It also respects AI instruction files such as `CLAUDE.md`, `AGENTS.md`, and `.cursorrules`.
* **Detects your framework** — identifies Nuxt and selects the `@sentry/nuxt` SDK.
* **Fetches official Sentry docs** — uses the current Sentry documentation as the source of truth when generating integration code.
* **Installs dependencies** — adds `@sentry/nuxt` using your project's package manager.
* **Creates and modifies files** — sets up client-side and server-side initialization, Nuxt module configuration, and other selected features based on your project structure.
* **Verifies the integration** — re-reads modified files after writing to confirm Sentry was integrated.

For full details on what each file does, see the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup.md) guide.

Prefer the existing Nuxt wizard?

If you don't want to use the experimental AI-powered flow, run the framework-specific installation wizard instead:

```bash
npx @sentry/wizard@latest -i nuxt
```

To configure Sentry manually, follow the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup.md) guide.

## [Avoid Ad Blockers With Tunneling (Optional)](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#avoid-ad-blockers-with-tunneling-optional)

You can prevent ad blockers from blocking Sentry events using tunneling. Use the `tunnel` option in `Sentry.init` to add an API endpoint in your application that forwards Sentry events to Sentry servers.

This will send all events to the `tunnel` endpoint. However, the events need to be parsed and redirected to Sentry, so you'll need to do additional configuration on the server. The endpoint must forward only the request body to Sentry and accept only your own DSN. You can find a detailed explanation on how to do this on our [Troubleshooting page](https://docs.sentry.io/platforms/javascript/guides/nuxt/troubleshooting.md#using-the-tunnel-option).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  tunnel: "/tunnel",
});
```

## [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#verify-your-setup)

The `sentry init` command checks the integration files it creates or modifies before it finishes. To confirm runtime events are reaching Sentry, start your Nuxt app, exercise the parts of your app that should send events, and then check your Sentry project.

If you used the Nuxt installation wizard instead, you can also verify your setup with the example page or component it creates.

The wizard created an example component instead of a page.

The wizard creates a `SentryErrorButton` component when it fails to add an example page to your project. This usually happens if you don't have a `app.vue` file or if that file does not contain the `NuxtPage` component. To verify your setup, follow these steps before continuing with the next section, "View Captured Data in Sentry":

1. Add the `SentryErrorButton` component to a page and open it in your browser. For most Nuxt applications, this will be at localhost.
2. Click the "Throw Sample Error" button, which triggers an error and starts a performance trace on the client side.

To test the server side as well, refer to the "Verify" section in the [Manual setup guide](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup.md).

To test Sentry, you can run your Nuxt application in either production or development mode. We **recommend testing in production mode** as it most closely resembles your deployed application's environment.

The SDK bundles `sentry.server.config.ts` into the Nitro server build and initializes Sentry when the server starts. To learn more, see [Server-Side Installation](https://docs.sentry.io/platforms/javascript/guides/nuxt/install.md).

### [Run in Production Mode (Recommended)](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#run-in-production-mode-recommended)

Build your project with `nuxi build`, then start the server.

```bash
# Start your app after building your project with `nuxi build`
node .output/server/index.mjs
```

### [Run in Development Mode](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#run-in-development-mode)

Sentry also monitors the server side during development. Start the dev server as usual.

Spans from some libraries, such as database clients, can be missing in development mode. Errors and request traces always work. To learn more, see [Development Mode](https://docs.sentry.io/platforms/javascript/guides/nuxt/install.md#development-mode).

```bash
nuxt dev
```

If you used the Nuxt installation wizard, after building and running your project:

1. Open the example page `/sentry-example-page` in your browser. For most Nuxt applications, this will be at localhost.

2. Click the "Throw sample error" button. This triggers two errors:

   * a frontend error
   * an error within the API route

Sentry captures both of these errors for you. Additionally, the button click starts a performance trace to measure the time it takes for the API request to complete.

### [Verify Additional Features](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#verify-additional-features)

**Logs** (enabled by default)

See structured log entries from your application. You can send logs from anywhere:

```typescript
Sentry.logger.info("User action", { userId: "123" });
Sentry.logger.warn("Slow response", { duration: 5000 });
Sentry.logger.error("Operation failed", { reason: "timeout" });
```

Learn more about [Logs configuration](https://docs.sentry.io/platforms/javascript/guides/nuxt/logs.md).

**Application Metrics** (enabled by default) NEW

Track and analyze custom application metrics to understand trends and patterns in your app's performance and behavior over time:

```typescript
Sentry.metrics.count("checkout.failed", 1);
Sentry.metrics.gauge("queue.depth", 42);
Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
});
```

Learn more about [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/nuxt/metrics.md).

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/nuxt.md#next-steps)

At this point, you should have integrated Sentry into your Nuxt application and should already be sending error and performance data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/javascript/guides/nuxt/usage.md)
* Continue to [customize your configuration](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration.md)
* Get familiar with [Sentry's product features](https://docs.sentry.io/product.md) like tracing, insights, and alerts
* Learn how to [track your Vue components or your Pinia store](https://docs.sentry.io/platforms/javascript/guides/nuxt/features.md)
* Learn how to [add support for different Nitro deployment presets](https://docs.sentry.io/platforms/javascript/guides/nuxt/features/nitro-deployment-presets.md) (like Cloudflare)

Are you having problems setting up the SDK?

* If you encountered issues with our installation wizard, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup.md)
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

- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup.md)
- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/nuxt/manual-setup__v10.x.md)
- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/nuxt/install__v10.x.md)
- [Server-Side Installation](https://docs.sentry.io/platforms/javascript/guides/nuxt/install.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/nuxt/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/nuxt/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/nuxt/logs.md)
- [Nuxt Features](https://docs.sentry.io/platforms/javascript/guides/nuxt/features.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/nuxt/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/nuxt/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/nuxt/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/nuxt/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/nuxt/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/nuxt/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/nuxt/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nuxt/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/nuxt/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/nuxt/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/nuxt/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/nuxt/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/nuxt/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/nuxt/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/nuxt/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/nuxt/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/nuxt/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nuxt/troubleshooting.md)

