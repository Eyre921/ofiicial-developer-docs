---
title: "Pi Durable"
source: https://docs.sentry.io/platforms/javascript/guides/pi-durable.md
path: platforms/javascript/guides/pi-durable
---

---
title: "Pi Durable"
description: "Learn how to send Pi Durable agent runs, model requests, tool calls, and errors to Sentry with the Sentry SDK."
url: https://docs.sentry.io/platforms/javascript/guides/pi-durable/
---

# Sentry for Pi Durable

[Pi Durable](https://earendil.com/posts/pi-durable/) is Earendil's durable agent harness, built on the same foundations as the Pi coding agent. It runs many conversations at once and survives crashes, picking each run up from its last checkpoint. This guide sets up the Sentry SDK in a Pi Durable app so agent runs, model requests, tool calls, and errors flow into [Sentry Agent Tracing](https://docs.sentry.io/product/agents.md).

Pi Durable is experimental, and its API can change between releases. The Sentry integration supports `@earendil-works/pi-durable` `>=1.0.0 <2.0.0` and requires JavaScript SDK version `11.6.0` or later.

Running Pi Durable in a Cloudflare Durable Object? Follow the [Cloudflare Quick Start](https://docs.sentry.io/platforms/javascript/guides/pi-durable/cloudflare.md) instead.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#prerequisites)

Before you begin, you need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md). The project's DSN tells the SDK where to send data.
* A Node.js application using `@earendil-works/pi-durable` version `1.0.0` or later.
* `@sentry/node` version `11.6.0` or later, or [`@sentry/cloudflare@^11.6.0` when running on Cloudflare](https://docs.sentry.io/platforms/javascript/guides/pi-durable/cloudflare.md). Browser runtimes are not supported.

## [Install](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#install)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing\[ ]Profiling

Install the Sentry Node SDK:

```bash
npm install @sentry/node@^11.6.0
```

*Other available variations of the above snippet: yarn, pnpm*

```bash
npm install @sentry/node@^11.6.0 @sentry/profiling-node@^11.6.0
```

*Other available variations of the above snippet: yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#configure)

Create an instrument file that calls `Sentry.init()`. The Pi Durable integration is enabled by default, so you don't add it to `integrations`:

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

Preload the instrument file with the `--import` flag when you start your app:

```json
{
  "scripts": {
    "start": "node --import ./instrument.mjs server.mjs"
  }
}
```

The SDK instruments `Harness.open()` while Node.js loads `@earendil-works/pi-durable`, so Sentry has to start before your app imports it. If you import the instrument file from your app instead of preloading it, the SDK can't instrument Pi Durable. If you bundle your server and can't pass `--import`, use the [bundler plugin](https://docs.sentry.io/platforms/javascript/guides/pi-durable/install/bundler.md) instead.

Your Pi Durable code doesn't change. Every Harness your app opens is traced, whichever storage and execution environment it uses:

```javascript
import { BACKGROUND_CONTEXT } from "@earendil-works/chord/context";
import { createModels } from "@earendil-works/pi-ai/models";
import { openaiProvider } from "@earendil-works/pi-ai/providers/openai";
import { createRegistry, Harness } from "@earendil-works/pi-durable";
import { openNodeSqliteStorage } from "@earendil-works/pi-durable/storage/sqlite/node";

const context = BACKGROUND_CONTEXT;
const models = createModels();
models.setProvider(openaiProvider());

const harness = await Harness.open(
  await openNodeSqliteStorage("./agent.sqlite"),
  { models, registry: createRegistry() },
  context,
);
harness.resume();
```

With this setup, Sentry captures errors thrown by your tools and extensions, and AI spans for every run (agent runs, model requests, tool calls, token usage, and latency). Manual spans you start inside a tool nest under that tool's span. Prompts and model outputs are recorded on your AI spans by default.

To review what's captured and turn recording of prompts and responses off, see [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#control-the-data-you-send-to-sentry-optional) below.

### [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/pi-durable/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

To change recording for Pi Durable only, pass `recordInputs` and `recordOutputs` to the integration. They take precedence over `dataCollection`:

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  integrations: [
    Sentry.piDurableIntegration({
      recordInputs: false,
      recordOutputs: false,
    }),
  ],
});
```

### [Link Conversations](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#link-conversations)

Sentry groups the runs of a Pi Durable conversation into a single [Conversation](https://docs.sentry.io/product/agents/conversations.md) automatically — there's no Sentry-specific setup. The SDK sets `gen_ai.conversation.id` on the agent, model, and tool spans of every run to `<harness id>:<conversation id>`.

Pi Durable numbers conversations per storage, starting from 1, so the SDK prefixes a random id for each opened Harness to keep root conversations from different storages apart. This id changes when the Harness reopens, for example after a process restart or after a Durable Object restarts. Runs from before and after a restart then show up as separate conversations in Sentry.

A subagent runs in a conversation of its own. Its first run nests under the tool call that created it, so the subagent shows up inside the parent's trace.

## [Verify](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#verify)

Submit a message to one of your conversations, ideally one that calls a tool. Then open [**Explore → Agents**](https://sentry.io/orgredirect/organizations/:orgslug/explore/agents/) in Sentry. Select the conversation to open its detail. The timeline shows the agent run, model requests, tool calls, token usage, latency, and any errors your tools threw.

If no data appears, confirm that:

* The `dsn` belongs to the Sentry project you're viewing.
* `tracesSampleRate` is greater than `0`.
* Your app completed at least one run after you added the setup.

## [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#troubleshooting)

* **No AI spans at all.** Confirm the instrument file is preloaded with `--import`, or that your bundle is built with the Sentry bundler plugin. Importing it at the top of your entry file runs too late, because `@earendil-works/pi-durable` is already loaded by then.
* **OpenAI, Anthropic, or Google Gen AI calls outside Pi Durable stopped showing up.** Once a Pi Durable run starts, the SDK turns off these provider integrations for the whole process, so Pi Durable's model requests aren't counted twice. See *What gets captured?* below.

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#next-steps)

* [Track AI agent spend with dashboards and alerts](https://sentry.io/cookbook/monitor-ai-agent-spend-with-dashboards-and-alerts/): build a dashboard for cost, tokens, models, and conversations.
* [Pi Durable's README](https://github.com/earendil-works/pi/tree/main/packages/durable): conversations, tasks, extensions, and storage, from the Pi side.
* Use the appropriate [JavaScript framework guide](https://docs.sentry.io/platforms/javascript.md) for application monitoring in a separate frontend or service.

What gets captured?

Sentry's Pi Durable integration maps Pi Durable's runtime operations to Sentry operations for the Agents dashboards:

| Pi Durable Operation            | Sentry Operation      |
| ------------------------------- | --------------------- |
| Run of a conversation           | `gen_ai.invoke_agent` |
| Model request (`pi.generation`) | `gen_ai.chat`         |
| Tool call (`pi.tool`)           | `gen_ai.execute_tool` |

Spans are tagged with `sentry.origin: auto.ai.pi_durable` and carry the model, token usage, and finish reasons for each request. Each run starts a trace of its own, separate from the request that submitted it, so concurrent runs never end up in each other's traces.

**Crash recovery.** When the process dies during a run, the spans that were open in that process are lost. Once a new process resumes the run, its spans arrive in a new trace that starts with the resumed step, such as the rerun of a tool call.

**Tool results.** A tool span records the result the model receives, including output streamed with `api.output()` and results an `afterTool` hook rewrote.

**Errors.** A tool that throws is captured as an error, and its span is marked failed. Pi Durable hands the throw back to the model as a tool result, so your app never sees it.

The built-in coding tools (`bash`, `read`, `edit`, `write`) are the exception: they throw to report expected failures, such as a command that exits with a non-zero code, so their span is marked failed but no error is captured.

Failures Pi Durable only passes to `onReport`, such as a hook or system prompt section that throws, are captured too. A failed model request isn't captured as an error; its `chat` span carries the error status.

**Provider SDKs.** Pi Durable sends model requests through `@earendil-works/pi-ai`, which calls the `openai`, `@anthropic-ai/sdk`, and `@google/genai` clients, or the Workers AI binding. From the first run on, the SDK turns off its OpenAI, Anthropic, Google Gen AI, and Workers AI integrations for the whole process, so these requests aren't counted twice. Calls your app makes with those clients outside Pi Durable aren't traced either. Amazon Bedrock requests are still reported a second time by the AWS integration.

**Not captured yet.** Tool calls that Pi Durable answers without running the tool, custom tasks you define with `defineTask`, agent names (Pi Durable has none), a link between a run and the request that submitted it, and a marker for compaction requests.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md#supported-versions)

* `@sentry/node`: `>=11.6.0`
* `@sentry/cloudflare`: `>=11.6.0`
* `@earendil-works/pi-durable`: `>=1.0.0 <2.0.0`

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

- [Cloudflare Quick Start](https://docs.sentry.io/platforms/javascript/guides/pi-durable/cloudflare.md)
- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/pi-durable/install.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/pi-durable/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/pi-durable/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/pi-durable/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/pi-durable/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/pi-durable/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/pi-durable/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/pi-durable/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/pi-durable/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/pi-durable/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/pi-durable/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/pi-durable/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/pi-durable/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/pi-durable/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/pi-durable/opentelemetry.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/pi-durable/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/pi-durable/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/pi-durable/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/pi-durable/troubleshooting.md)

