---
title: "Exacto Variant"
source: https://openrouter.ai/docs/guides/routing/model-variants/exacto.md
path: docs/guides/routing/model-variants/exacto
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exacto Variant

> Route requests with quality-first provider sorting

Exacto is a virtual model variant that explicitly applies quality-first provider sorting. When you add `:exacto` to a model slug, OpenRouter prefers providers with stronger tool-calling quality signals for that model instead of using the default price-weighted ordering.

## Using the Exacto variant

Add `:exacto` to the end of any supported model slug. This is a shortcut for setting the provider sort to Exacto on that model.

```typescript title="TypeScript SDK" lines theme={null}
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

const completion = await openRouter.chat.send({
  chatRequest: {
    model: "moonshotai/kimi-k2-0905:exacto",
    messages: [
      {
        role: "user",
        content: "Draft a concise changelog entry for the Exacto launch.",
      },
    ],
    stream: false,
  },
});

if (completion instanceof ReadableStream) {
  throw new Error('Expected a non-streaming response');
}

console.log(completion.choices[0].message.content);
```

```typescript title="TypeScript (OpenAI SDK)" lines theme={null}
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});

const completion = await client.chat.completions.create({
  model: "moonshotai/kimi-k2-0905:exacto",
  messages: [
    {
      role: "user",
      content: "Draft a concise changelog entry for the Exacto launch.",
    },
  ],
});
```

```shell title="cURL" lines theme={null}
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
  "model": "moonshotai/kimi-k2-0905:exacto",
  "messages": [
    {
      "role": "user",
      "content": "Summarize the latest release notes for me."
    }
  ]
}'
```

> [!TIP]
>
> You can still supply fallback models with the `models` array. Any model that carries the `:exacto` suffix will request Exacto sorting when it is selected.

## What is the Exacto variant?

Exacto is a routing shortcut for quality-first provider ordering. Unlike standard routing, which primarily favors lower-cost providers, Exacto prefers providers with stronger signals for tool-calling reliability and deprioritizes weaker performers.

## Why use Exacto?

### Why we built it

Providers serving the same model can vary meaningfully in tool-use behavior. Exacto gives you an explicit, request-level way to prefer higher-quality providers when you care more about tool-calling reliability than the default price-weighted route.

### Recommended use cases

Exacto is useful for quality-sensitive, agentic workflows where tool-calling accuracy and reliability matter more than raw cost efficiency.

## How Exacto works

Exacto uses the same provider-ranking signals as [Auto Exacto](https://openrouter.ai/docs/guides/routing/auto-exacto.md), but applies them explicitly because you chose the `:exacto` suffix.

We use three classes of signals:

* Tool-calling success and reliability from real traffic (see [How Tool-Calling Success Rate Is Measured](https://openrouter.ai/docs/guides/routing/auto-exacto.md#how-tool-calling-success-rate-is-measured) for the underlying methodology)
* Provider performance metrics such as throughput and latency
* Benchmark data from OpenRouter's benchmark harness (see [What the Benchmark Harness Runs](https://openrouter.ai/docs/guides/routing/auto-exacto.md#what-the-benchmark-harness-runs) for the benchmarks and parameters, and [Where to Find the Scores](https://openrouter.ai/docs/guides/routing/auto-exacto.md#where-to-find-the-scores) for the published results)

Providers with strong track records are moved toward the front of the list. Providers with limited data are kept behind well-established performers, and providers with poor quality signals are deprioritized further.

## Exacto vs. Auto Exacto

* **Auto Exacto** runs automatically on tool-calling requests and requires no model suffix.
* **`:exacto`** is the explicit shortcut when you want to request the Exacto sorting mode directly on a specific model slug.

If you explicitly sort by price, throughput, or latency, that explicit sort still takes precedence.

## Supported models

Exacto is a virtual variant and is not backed by a separate endpoint pool. It can be used anywhere provider sorting is meaningful, especially on models with multiple compatible providers.

In practice, Exacto is most useful on models that:

* Support tool calling
* Have multiple providers available on OpenRouter
* Show meaningful provider variance in tool-use reliability

> [!NOTE]
>
> If you have feedback on the Exacto variant, please fill out this form: [https://openrouter.notion.site/2932fd57c4dc8097ba74ffb6d27f39d1?pvs=105](https://openrouter.notion.site/2932fd57c4dc8097ba74ffb6d27f39d1?pvs=105)

