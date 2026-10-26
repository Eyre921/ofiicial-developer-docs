---
title: "TanStack Start React"
source: https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md
path: platforms/javascript/guides/tanstackstart-react
---

---
title: "TanStack Start React"
description: "Learn how to set up and configure Sentry in your TanStack Start React application using the installation wizard, capture your first errors, logs and traces and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/
---

# Sentry for TanStack Start React

##### Beta

This SDK is compatible with TanStack Start 1.0 RC and is currently in **beta**. Beta features are still in progress and may have bugs. Please reach out on [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if you have any feedback or concerns.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

## [Install](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md#install)

The AI-powered `sentry init` flow is currently experimental. If you run into any issues, check out the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/manual-setup.md) guide.

Run the Sentry init command in your project directory to automatically configure Sentry in your TanStack Start React application.

The command guides you through setup and asks which optional Sentry features you want to enable beyond error monitoring.

```bash
npx sentry@latest init
```

How does sentry init work?

The `sentry init` command is AI-powered. It analyzes your project and generates a tailored integration, rather than applying a fixed template. Here's what it does:

* **Analyzes your project** — reads project files and manifests to understand your TanStack Start React app structure, including monorepos. It also respects AI instruction files such as `CLAUDE.md`, `AGENTS.md`, and `.cursorrules`.
* **Detects your framework** — identifies TanStack Start and selects the `@sentry/tanstackstart-react` SDK.
* **Fetches official Sentry docs** — uses the current Sentry documentation as the source of truth when generating integration code.
* **Installs dependencies** — adds `@sentry/tanstackstart-react` using your project's package manager.
* **Creates and modifies files** — sets up client-side and server-side initialization, the Vite plugin for source maps, the server entry point, and middleware based on your project structure.
* **Verifies the integration** — re-reads modified files after writing to confirm Sentry was integrated.

For full details on what each file does, see the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/manual-setup.md) guide.

## [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md#verify-your-setup)

The wizard will have prompted you to select which features to enable. Select the same options here to see the relevant verification steps:

Error Monitoring\[ ]Tracing\[ ]Session Replay\[ ]User Feedback

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

Add a test button to one of your pages to trigger an error:

```tsx
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Break the world
</button>;
```

Start your dev server and click the button.

### [Check Your Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md#check-your-data-in-sentry)

**Errors** — [Open Issues](https://sentry.io/orgredirect/organizations/:orgslug/issues/)

You should see "Sentry Test Error" with a full stack trace pointing to your source code.

**Tracing** — [Open Traces](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/)

You should see page load and navigation traces. Learn more about [custom spans](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/tracing/instrumentation/custom-instrumentation.md).

**Session Replay** — [Open Replays](https://sentry.io/orgredirect/organizations/:orgslug/replays/)

Watch a video-like recording of your session, including the moment the error occurred. Learn more about [Session Replay configuration](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/session-replay.md).

**Logs** — [Open Logs](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/)

See structured log entries from your application. You can send logs from anywhere:

```typescript
Sentry.logger.info("User action", { userId: "123" });
Sentry.logger.warn("Slow response", { duration: 5000 });
Sentry.logger.error("Operation failed", { reason: "timeout" });
```

Learn more about [Logs configuration](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/logs.md).

**Application Metrics** — [Open Metrics](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics/) NEW

Track and analyze custom application metrics to understand trends and patterns in your app's performance and behavior over time:

```typescript
Sentry.metrics.count("checkout.failed", 1);
Sentry.metrics.gauge("queue.depth", 42);
Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
});
```

Learn more about [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/metrics.md).

Are you having problems setting up the SDK?

* If you encountered issues with the installation wizard, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/manual-setup.md)
* Check [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/troubleshooting.md) for common issues
* [Get support](https://www.sentry.help/en/)

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md#next-steps)

You've successfully integrated Sentry into your TanStack Start React application! Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/usage.md)
* Continue to [customize your configuration](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/configuration.md)
* Get familiar with [Sentry's product features](https://docs.sentry.io/product.md) like tracing, insights, and alerts

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
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/manual-setup.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/logs.md)
- [TanStack Start React Features](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/features.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react/troubleshooting.md)

