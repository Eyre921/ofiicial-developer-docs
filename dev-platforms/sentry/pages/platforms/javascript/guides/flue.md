---
title: "Flue"
source: https://docs.sentry.io/platforms/javascript/guides/flue.md
path: platforms/javascript/guides/flue
---

---
title: "Flue"
description: "Learn how to send Flue agent traces, model calls, tool executions, and errors to Sentry with the Sentry SDK."
url: https://docs.sentry.io/platforms/javascript/guides/flue/
---

# Sentry for Flue

[Flue](https://flueframework.com/) is an open TypeScript framework for building AI agents, made by the Astro team. This guide sets up the Sentry SDK in a Flue app so agent turns, model calls, tool executions, and errors flow into [Sentry Agent Tracing](https://docs.sentry.io/product/agents.md).

This guide covers the Sentry SDK-based setup, which replaces the `flue add tooling sentry` blueprint. If you previously ran the blueprint, remove its `createOpenTelemetryInstrumentation` call — otherwise, you will get duplicate spans.

Deploying Flue agents to Cloudflare Workers? Follow the [Cloudflare Quick Start](https://docs.sentry.io/platforms/javascript/guides/flue/cloudflare.md) instead.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/flue.md#prerequisites)

Before you begin, you need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md). The project's DSN tells the SDK where to send data.
* A Flue application using `@flue/runtime` version `2.0.0` or later. Flue requires Node.js `22.19` or later.
* `@sentry/node` or `@sentry/cloudflare` version `11.0.0` or later. Browser runtimes are not supported.

## [Install](https://docs.sentry.io/platforms/javascript/guides/flue.md#install)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing\[ ]Profiling

Install the Sentry Node SDK:

```bash
npm install @sentry/node@^11.0.0
```

*Other available variations of the above snippet: yarn, pnpm*

```bash
npm install @sentry/node@^11.0.0 @sentry/profiling-node@^11.0.0
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/flue.md#configure)

Create a file that calls `Sentry.init()` and registers the Flue instrumentation. Flue is instrumented by registering with it rather than by patching, so this `instrument()` call is what connects the two:

```typescript
import { instrument } from "@flue/runtime";
import * as Sentry from "@sentry/node";
// ___PRODUCT_OPTION_START___ profiling
import { nodeProfilingIntegration } from "@sentry/profiling-node";
// ___PRODUCT_OPTION_END___ profiling

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // ___PRODUCT_OPTION_START___ profiling

  integrations: [
    // Add our Profiling integration
    nodeProfilingIntegration(),
  ],
  // ___PRODUCT_OPTION_END___ profiling
  // ___PRODUCT_OPTION_START___ performance

  // Set tracesSampleRate to 1.0 to capture 100%
  // of spans for tracing.
  // We recommend adjusting this value in production.
  tracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ profiling

  // Set profileSessionSampleRate to 1.0 to profile every session.
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#profileSessionSampleRate
  profileSessionSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ profiling
});

instrument(Sentry.createFlueInstrumentation());
```

Import it at the top of your app entry, so it runs before your agents take a turn:

```typescript
import "./instrument.ts";
```

Call `instrument()` once, at module scope. On Cloudflare the Vite plugin registers the instrumentation at build time instead; on Node there's no equivalent, so this call is what installs it.

### [Run With the Sentry Loader](https://docs.sentry.io/platforms/javascript/guides/flue.md#run-with-the-sentry-loader)

Libraries like database drivers, caches, and `dataloader` are instrumented by a module transform that has to be installed before your app loads them. A Flue build imports your dependencies before `src/instrument.ts` runs, so start the server with the Sentry loader to catch them:

```json
{
  "scripts": {
    "dev": "NODE_OPTIONS='--import=@sentry/node/import' vite dev",
    "start": "NODE_OPTIONS='--import=@sentry/node/import' node dist/server.mjs"
  }
}
```

Agent, model, and tool spans arrive without this, as do outgoing HTTP requests. Everything instrumented through the module transform needs it.

With this setup, Sentry captures errors thrown by your agents and tools, and AI spans for every run (agent turns, model calls, tool executions, token usage, and latency). Manual spans you start inside a tool nest under that tool's span.

To review what's captured and turn recording of prompts and responses off, see [Privacy Controls](https://docs.sentry.io/platforms/javascript/guides/flue.md#privacy-controls) below.

### [Privacy Controls](https://docs.sentry.io/platforms/javascript/guides/flue.md#privacy-controls)

The SDK will record generative AI inputs and outputs (the prompts your agent sends and the model responses it receives) by default. To turn recording off, set `genAI.inputs` and `genAI.outputs` to `false` in `dataCollection`:

```typescript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    genAI: { inputs: false, outputs: false },
  },
});
```

See [`dataCollection` documentation](https://docs.sentry.io/platforms/javascript/guides/flue/configuration/options.md#dataCollection) for details on privacy control options.

### [Link Conversations](https://docs.sentry.io/platforms/javascript/guides/flue.md#link-conversations)

Sentry groups a multi-turn chat into a single [Conversation](https://docs.sentry.io/product/agents/conversations.md) automatically — there's no Sentry-specific setup. Flue already tracks a conversation id per conversation, and the SDK maps it to `gen_ai.conversation.id` on the agent, model, and tool spans of every turn.

The agent span also carries `gen_ai.agent.name`, so you can tell a lead agent's runs from its subagents'.

## [Verify](https://docs.sentry.io/platforms/javascript/guides/flue.md#verify)

Send a message to one of your agents, then open [**Explore → Agents**](https://sentry.io/orgredirect/organizations/:orgslug/explore/agents/) in Sentry. Select the conversation to open its detail. The timeline shows the agent turn, model calls, tool executions, token usage, latency, and any errors your tools threw.

If no data appears, confirm that:

* The `dsn` belongs to the Sentry project you're viewing.
* `tracesSampleRate` is greater than `0`.
* Your agent completed at least one turn after you added the setup.

## [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/flue.md#troubleshooting)

* **Token and cost values are doubled.** Remove the `createOpenTelemetryInstrumentation` call left over from the `flue add tooling sentry` blueprint. Flue emits its own model spans through it, so both it and the SDK count the same turn.
* **No AI spans at all.** Confirm `instrument(Sentry.createFlueInstrumentation())` actually runs. Importing `src/instrument.ts` at the top of `src/app.ts` runs it during app startup, before any agent takes a turn.

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/flue.md#next-steps)

* [Name your agents](https://docs.sentry.io/product/agents/naming.md) so you can identify them in the Agents Dashboard.
* [Track AI agent spend with dashboards and alerts](https://sentry.io/cookbook/monitor-ai-agent-spend-with-dashboards-and-alerts/): build a dashboard for cost, tokens, models, and conversations.
* [Flue's observability guide](https://flueframework.com/docs/guide/observability/): the event model behind the spans, from the Flue side.
* Use the appropriate [JavaScript framework guide](https://docs.sentry.io/platforms/javascript.md) for application monitoring in a separate frontend or service.

What gets captured?

Sentry's Flue integration maps Flue's runtime operations to Sentry operations for the Agents dashboards:

| Flue Operation   | Sentry Operation      |
| ---------------- | --------------------- |
| Agent submission | `gen_ai.invoke_agent` |
| Model turn       | `gen_ai.chat`         |
| Tool execution   | `gen_ai.execute_tool` |

Spans are tagged with `sentry.origin: auto.ai.flue` and carry the model, token usage, and finish reasons for the turn.

A `chat` span also carries `flue.turn.purpose`, which is how you tell a context-compaction turn from a user-facing one. There's no conventional attribute for that distinction.

A tool that throws is captured as an error and its span is marked failed. Flue catches the throw and hands it back to the model as a tool result, so the error is reported as handled.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/flue.md#supported-versions)

* `@sentry/node`: `>=11.0.0`
* `@sentry/cloudflare`: `>=11.0.0`
* `@flue/runtime`: `>=2.0.0 <3.0.0`

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

- [Cloudflare Quick Start](https://docs.sentry.io/platforms/javascript/guides/flue/cloudflare.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/flue/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/flue/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/flue/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/flue/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/flue/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/flue/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/flue/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/flue/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/flue/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/flue/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/flue/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/flue/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/flue/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/flue/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/flue/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/flue/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/flue/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/flue/troubleshooting.md)

