---
title: "Mastra"
source: https://docs.sentry.io/platforms/javascript/guides/mastra.md
path: platforms/javascript/guides/mastra
---

---
title: "Mastra"
description: "Learn how to send Mastra agent traces, model calls, tool executions, and errors to Sentry using the Sentry CLI."
url: https://docs.sentry.io/platforms/javascript/guides/mastra/
---

# Sentry for Mastra

[Mastra](https://mastra.ai/) is a TypeScript framework for building AI applications and agents. This guide uses the Sentry CLI to set up the Sentry SDK in a Mastra app so agent runs, model generations, tool calls, workflows, and errors flow into [Sentry Agent Tracing](https://docs.sentry.io/product/agents.md).

This guide covers the Sentry SDK-based setup, which replaces the earlier `@mastra/sentry` exporter. It requires JavaScript SDK version `11.0.0` or later. If you previously used the `@mastra/sentry` exporter, remove it from your Mastra `exporters` — it calls `Sentry.init()` itself and conflicts with the built-in integration.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/mastra.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* A Mastra application using `@mastra/core` version `1.63.2` or later.

## [Install](https://docs.sentry.io/platforms/javascript/guides/mastra.md#install)

The AI-powered `sentry init` flow is currently experimental. If you run into any issues, check out the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/mastra/manual-setup.md) guide.

Run the Sentry init command in your project directory to automatically configure Sentry in your Mastra application.

The command guides you through setup and asks which optional Sentry features you want to enable beyond error monitoring.

```bash
npx sentry@latest init
```

When the command asks which features to enable, include **Agent Tracing** so your agent runs show up in Sentry.

How does sentry init work?

The `sentry init` command is AI-powered. It analyzes your project and generates a tailored integration, rather than applying a fixed template. Here's what it does:

* **Analyzes your project** — reads project files and manifests to understand your Mastra app structure, including monorepos. It also respects AI instruction files such as `CLAUDE.md`, `AGENTS.md`, and `.cursorrules`.
* **Detects your framework** — identifies Mastra and selects the `@sentry/node` SDK.
* **Fetches official Sentry docs** — uses the current Sentry documentation as the source of truth when generating integration code.
* **Installs dependencies** — adds `@sentry/node` and Mastra's `@mastra/observability` package using your project's package manager.
* **Creates and modifies files** — sets up initialization with agent tracing for your Mastra agents, and other selected features based on your existing project structure.
* **Verifies the integration** — re-reads modified files after writing to confirm Sentry was integrated.

For full details on what each file does, see the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/mastra/manual-setup.md) guide.

## [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/mastra.md#control-the-data-you-send-to-sentry)

By default, the SDK sends the inputs and outputs of your LLM and tool calls, such as prompts, responses, and tool arguments. This will give you rich debugging context. Review the data your agent handles before you deploy to production.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/mastra/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    genAI: { inputs: false, outputs: false },
  },
});
```

## [Verify](https://docs.sentry.io/platforms/javascript/guides/mastra.md#verify)

Run one of your Mastra agents, then open [**Explore → Agents**](https://sentry.io/orgredirect/organizations/:orgslug/explore/agents/) in Sentry. Select the trace to open its detail. The timeline shows the model generations, tool calls, token usage, latency, and any errors your agent threw.

If no data appears, confirm that:

* The `dsn` belongs to the Sentry project you're viewing.
* `tracesSampleRate` is greater than `0`.
* `@mastra/observability` is installed, so the integration can attach to Mastra's telemetry.
* Your application completed at least one agent run after you added the setup.

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/mastra.md#next-steps)

* [Name your agents](https://docs.sentry.io/product/agents/naming.md) so you can identify them in the Agents Dashboard.
* [Track AI agent spend with dashboards and alerts](https://sentry.io/cookbook/monitor-ai-agent-spend-with-dashboards-and-alerts/): build a dashboard for cost, tokens, models, and conversations.
* Use the appropriate [JavaScript framework guide](https://docs.sentry.io/platforms/javascript.md) for application monitoring in a separate frontend or service.

To learn what each file does and how to configure Sentry yourself, read the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/mastra/manual-setup.md) guide.

Are you having problems setting up the SDK?

* If you encountered issues with `sentry init`, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/mastra/manual-setup.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/mastra/troubleshooting.md)
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

- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/mastra/manual-setup.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/mastra/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/mastra/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/mastra/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/mastra/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/mastra/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/mastra/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/mastra/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/mastra/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/mastra/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/mastra/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/mastra/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/mastra/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/mastra/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/mastra/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/mastra/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/mastra/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/mastra/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/mastra/troubleshooting.md)

