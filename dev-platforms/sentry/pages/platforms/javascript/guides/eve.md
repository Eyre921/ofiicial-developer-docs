---
title: "Eve"
source: https://docs.sentry.io/platforms/javascript/guides/eve.md
path: platforms/javascript/guides/eve
---

---
title: "Eve"
description: "Learn how to send Eve agent traces, conversations, and errors to Sentry with the Sentry Node SDK."
url: https://docs.sentry.io/platforms/javascript/guides/eve/
---

# Sentry for Eve

[Eve](https://eve.dev/) is Vercel's filesystem-first framework for building durable backend AI agents on top of the Vercel AI SDK. This guide sets up the `@sentry/node` SDK inside an Eve app so agent turns, model calls, tool executions, and errors flow into [Sentry Agent Tracing](https://docs.sentry.io/product/agents.md).

This guide covers the Sentry SDK-based setup for JavaScript SDK version `11.0.0` or later. If your app uses Eve's earlier OTLP instrumentation, remove it before following this guide. Both integrations produce AI spans and configure OpenTelemetry, so combining them duplicates spans, token totals, and costs.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/eve.md#prerequisites)

Before you begin, you need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md). The project's DSN tells the SDK where to send data.
* An Eve application using version `0.63.0` or later.
* `@sentry/node` version `11.0.0` or later. The SDK runs in Node.js only; it doesn't support browser or edge runtimes.

## [Install](https://docs.sentry.io/platforms/javascript/guides/eve.md#install)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing\[ ]Profiling

Then install the Sentry Node SDK:

```bash
npm install @sentry/node@^11.0.0
```

*Other available variations of the above snippet: yarn, pnpm*

```bash
npm install @sentry/node@^11.0.0 @sentry/profiling-node@^11.0.0
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/eve.md#configure)

Create `agent/instrumentation/sentry.ts` and export the Sentry instrumentation provider. Eve auto-discovers providers in `agent/instrumentation/` and runs them at server startup, before it loads your agent and the AI SDK:

```typescript
import * as Sentry from "@sentry/node";
// ___PRODUCT_OPTION_START___ profiling
import { nodeProfilingIntegration } from "@sentry/profiling-node";
// ___PRODUCT_OPTION_END___ profiling
import { defineInstrumentation } from "eve/instrumentation";

export default defineInstrumentation(
  Sentry.eveInstrumentation({
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
    // Learn more at
    // https://docs.sentry.io/platforms/javascript/guides/node/configuration/options/#tracesSampleRate
    tracesSampleRate: 1.0,
    // ___PRODUCT_OPTION_END___ performance
    // ___PRODUCT_OPTION_START___ profiling

    // Set profileSessionSampleRate to 1.0 to profile every session.
    // Learn more at
    // https://docs.sentry.io/platforms/javascript/configuration/options/#profileSessionSampleRate
    profileSessionSampleRate: 1.0,
    // ___PRODUCT_OPTION_END___ profiling
  }),
);
```

With this setup, Sentry captures errors thrown by your agent and AI spans for every turn — model calls, tool executions, token usage, and latency — along with outgoing HTTP and `fetch` requests. It also groups every turn in an Eve session into one Sentry conversation. Prompts and model outputs are recorded on your agent spans by default, so the conversation detail shows the full exchange without any extra configuration.

To also instrument the rest of your Node app, see [Instrument Other Dependencies](https://docs.sentry.io/platforms/javascript/guides/eve.md#instrument-other-dependencies) below. To review what's captured and turn recording of prompts and responses off, see [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/eve.md#control-the-data-you-send-to-sentry-optional).

## [Verify](https://docs.sentry.io/platforms/javascript/guides/eve.md#verify)

Start Eve and send a prompt that calls a tool. Then open [**Explore → Agents**](https://sentry.io/orgredirect/organizations/:orgslug/explore/agents/) in Sentry. Select the conversation to open its detail, where the timeline shows the model calls, tool calls, token usage, and latency for that turn, plus any errors your agent threw.

If no data appears, confirm that:

* The `dsn` belongs to the Sentry project you're viewing.
* `tracesSampleRate` is greater than `0`.
* Your app completed at least one agent turn after you added `agent/instrumentation/sentry.ts`.
* Eve's earlier OTLP instrumentation isn't also initialized in the agent runtime. Running both integrations duplicates AI spans, token totals, and costs.

## [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/eve.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK sends the inputs and outputs of your LLM and tool calls, such as prompts, responses, and tool arguments. This will give you rich debugging context. Review the data your agent handles before you deploy to production.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/eve/configuration/options.md#dataCollection).

```typescript
export default defineInstrumentation(
  Sentry.eveInstrumentation({
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    dataCollection: {
      genAI: { inputs: false, outputs: false },
    },
  }),
);
```

## [Customize Conversation Grouping](https://docs.sentry.io/platforms/javascript/guides/eve.md#customize-conversation-grouping)

Each Eve turn is its own durable workflow, so a session's turns land in separate traces. `eveInstrumentation` uses the durable session id (`session.id`) as the Sentry conversation id by default, which groups all turns from the session into one [Conversation](https://docs.sentry.io/product/agents/conversations.md).

To derive the conversation id yourself — for example, to group a subagent's turns under a root or parent session — pass `getConversationId` in your instrumentation provider:

```typescript
export default defineInstrumentation(
  Sentry.eveInstrumentation({
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    getConversationId: (context) => context.session.id,
  }),
);
```

## [Instrument Other Dependencies](https://docs.sentry.io/platforms/javascript/guides/eve.md#instrument-other-dependencies)

The setup above instruments the AI SDK, HTTP, and `fetch` with no bootstrapping. To also instrument the rest of your Node app — database clients like `pg` or `mysql`, and other libraries that patch themselves as they load — start Eve with Sentry's ESM loader preloaded, so it can hook those modules at load time:

```bash
NODE_OPTIONS='--import=@sentry/node/import' eve start
```

The loader can only transform modules that Eve leaves external to its server bundle. If Eve inlines a dependency, the loader can't hook it, so the module is silently never instrumented. Rather than hardcode that list, use `getInstrumentedModuleNames()` from `@sentry/node` to keep every package Sentry instruments external in `agent/agent.ts`:

```typescript
import { getInstrumentedModuleNames } from "@sentry/node";
import { defineAgent } from "eve";

export default defineAgent({
  build: {
    externalDependencies: getInstrumentedModuleNames(),
  },
});
```

`getInstrumentedModuleNames()` returns the authoritative set of packages Sentry instruments through the loader (database clients like `pg` and `mysql`, and others), so you don't have to maintain the list yourself. The AI SDK isn't part of it — it reports through a native diagnostics channel that works without the loader.

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/eve.md#next-steps)

* [Name your agents](https://docs.sentry.io/product/agents/naming.md) so you can identify them in the Agents Dashboard.
* [Track AI agent spend with dashboards and alerts](https://sentry.io/cookbook/monitor-ai-agent-spend-with-dashboards-and-alerts/): build a dashboard for cost, tokens, models, and conversations.
* Review Eve's [instrumentation guide](https://eve.dev/docs/guides/instrumentation) for the framework side of the setup.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/eve.md#supported-versions)

* `@sentry/node`: `>=11.0.0`
* `eve`: `>=0.63.0`

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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/eve/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/eve/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/eve/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/eve/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/eve/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/eve/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/eve/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/eve/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/eve/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/eve/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/eve/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/eve/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/eve/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/eve/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/eve/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/eve/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/eve/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/eve/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/eve/troubleshooting.md)

