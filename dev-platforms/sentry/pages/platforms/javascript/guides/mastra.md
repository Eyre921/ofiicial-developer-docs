---
title: "Mastra"
source: https://docs.sentry.io/platforms/javascript/guides/mastra.md
path: platforms/javascript/guides/mastra
---

---
title: "Mastra"
description: "Learn how to send Mastra agent traces, model calls, tool executions, and errors to Sentry with the Sentry SDK."
url: https://docs.sentry.io/platforms/javascript/guides/mastra/
---

# Sentry for Mastra

[Mastra](https://mastra.ai/) is a TypeScript framework for building AI applications and agents. This guide sets up the Sentry SDK in a Mastra app so agent runs, model generations, tool calls, workflows, and errors flow into [Sentry Agent Tracing](https://docs.sentry.io/product/agents.md).

This guide covers the Sentry SDK-based setup, which replaces the earlier `@mastra/sentry` exporter. It requires JavaScript SDK version `11.0.0` or later. If you previously used the `@mastra/sentry` exporter, remove it from your Mastra `exporters` — it calls `Sentry.init()` itself and conflicts with the built-in integration.

Running Mastra on Cloudflare Workers? Follow the [Cloudflare Quick Start](https://docs.sentry.io/platforms/javascript/guides/mastra/cloudflare.md) instead.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/mastra.md#prerequisites)

Before you begin, you need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md). The project's DSN tells the SDK where to send data.
* A Mastra application using `@mastra/core` version `1.63.2` or later.
* `@mastra/observability`. Sentry's Mastra integration needs it to attach to Mastra's telemetry pipeline.
* `@sentry/node` version `11.0.0` or later, or [`@sentry/cloudflare@^11.0.0` when running on Cloudflare](https://docs.sentry.io/platforms/javascript/guides/mastra/cloudflare.md). Browser runtimes are not supported.

## [Install](https://docs.sentry.io/platforms/javascript/guides/mastra.md#install)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing\[ ]Profiling

Install the Sentry Node SDK and Mastra's observability package:

```bash
npm install @sentry/node@^11.0.0 @mastra/observability@latest
```

*Other available variations of the above snippet: yarn, pnpm*

```bash
npm install @sentry/node@^11.0.0 @sentry/profiling-node@^11.0.0 @mastra/observability@latest
```

*Other available variations of the above snippet: yarn, pnpm*

If Mastra can't load `@mastra/observability`, the integration warns and creates no spans.

## [Configure](https://docs.sentry.io/platforms/javascript/guides/mastra.md#configure)

Create an instrument file that calls `Sentry.init()`, and preload it so Sentry starts before Mastra and the AI SDK load.

Place the file in your Mastra `public/` directory. `mastra build` and `mastra dev` copy `public/` into the build output, so the file lands next to the compiled server as `instrument.mjs`, where `--import=./instrument.mjs` can resolve it:

```javascript
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
});
```

Preload the instrument file when you start Mastra by passing it through `--custom-args`:

```json
{
  "scripts": {
    "dev": "mastra dev --custom-args=\"--import=./instrument.mjs\"",
    "start": "mastra start --custom-args=\"--import=./instrument.mjs\""
  }
}
```

With this setup, Sentry captures errors thrown by your agents and AI spans for every run (agent runs, model generations, tool calls, workflows, token usage, and latency) along with outgoing HTTP and `fetch` requests. Prompts and model outputs are recorded on your AI spans by default.

To review what's captured and turn recording of prompts and responses off, see [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/mastra.md#control-the-data-you-send-to-sentry-optional) below.

### [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/mastra.md#control-the-data-you-send-to-sentry-optional)

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

### [Link Conversations](https://docs.sentry.io/platforms/javascript/guides/mastra.md#link-conversations)

Sentry groups a multi-turn chat into a single [Conversation](https://docs.sentry.io/product/agents/conversations.md) automatically — there's no Sentry-specific setup. Mastra maps its memory thread id to `gen_ai.conversation.id`, so agent runs that share a thread id are grouped into one conversation.

Threads come from Mastra's own memory feature. If your app already passes a thread when it calls an agent — as multi-turn chat apps do — Sentry picks it up as the conversation id with no extra work:

```typescript
const result = await agent.generate(message, {
  memory: {
    thread: "session-123",
    resource: "user-456",
  },
});
```

Your agent needs a storage provider configured before Mastra accepts the `memory` option. Reuse the same thread id across the messages in a session.

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

What gets captured?

Sentry's Mastra integration maps Mastra's span types to Sentry operations for the Agents dashboards:

| Mastra Span Type        | Sentry Operation      |
| ----------------------- | --------------------- |
| `AGENT_RUN`             | `gen_ai.invoke_agent` |
| `WORKFLOW_RUN`          | `gen_ai.invoke_agent` |
| `MODEL_GENERATION`      | `gen_ai.chat`         |
| `TOOL_CALL`             | `gen_ai.execute_tool` |
| `MCP_TOOL_CALL`         | `gen_ai.execute_tool` |
| `PROVIDER_TOOL_CALL`    | `gen_ai.execute_tool` |
| `CLIENT_TOOL_CALL`      | `gen_ai.execute_tool` |
| `RAG_EMBEDDING`         | `gen_ai.embeddings`   |
| `CLASSIFIER_EVALUATION` | `gen_ai.decide`       |

Spans are tagged with `sentry.origin: auto.ai.mastra`.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/mastra.md#supported-versions)

* `@sentry/node`: `>=11.0.0`
* `@sentry/cloudflare`: `>=11.0.0`
* `@mastra/core`: `>=1.63.2`
* `@mastra/observability`: required for the integration to create spans

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

- [Cloudflare Quick Start](https://docs.sentry.io/platforms/javascript/guides/mastra/cloudflare.md)
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

