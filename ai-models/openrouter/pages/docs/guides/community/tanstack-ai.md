---
title: "TanStack AI"
source: https://openrouter.ai/docs/guides/community/tanstack-ai.md
path: docs/guides/community/tanstack-ai
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TanStack AI

> Using OpenRouter with TanStack AI

## TanStack AI

You can use [TanStack AI](https://tanstack.com/ai) to integrate OpenRouter with your React, Solid, or Preact applications. The OpenRouter adapter provides access to 400+ AI models from various providers through a single unified API. To get started, install [@tanstack/ai-openrouter](https://www.npmjs.com/package/@tanstack/ai-openrouter):

```bash lines theme={null}
npm install @tanstack/ai @tanstack/ai-openrouter
```

### Basic Usage

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("openai/gpt-5.2"),
  messages: [{ role: "user", content: "Hello!" }],
});
```

### Configuration

You can configure the OpenRouter adapter with additional options:

```typescript title="TypeScript" lines theme={null}
import { createOpenRouter, type OpenRouterConfig } from "@tanstack/ai-openrouter";

const config: OpenRouterConfig = {
  apiKey: process.env.OPENROUTER_API_KEY!,
  baseURL: "https://openrouter.ai/api/v1", // Optional
  httpReferer: "https://your-app.com", // Optional, for rankings
  xTitle: "Your App Name", // Optional, for rankings
};

const adapter = createOpenRouter(config.apiKey, config);
```

### Available Models

OpenRouter provides access to 400+ models from various providers. Models use the format `provider/model-name`:

```typescript lines theme={null}
model: "openai/gpt-5.2"
model: "anthropic/claude-sonnet-4.5"
model: "google/gemini-3.1-pro-preview"
model: "z-ai/glm-4.7"
model: "minimax/minimax-m2.1"
```

See the full list at [openrouter.ai/models](https://openrouter.ai/models).

### Server-Side Example

```typescript title="TypeScript" lines theme={null}
import { chat, toServerSentEventsResponse } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

export async function POST(request: Request) {
  const { messages } = await request.json();

  const stream = chat({
    adapter: openRouterText("openai/gpt-5.2"),
    messages,
  });

  return toServerSentEventsResponse(stream);
}
```

### Using Tools

```typescript title="TypeScript" expandable lines theme={null}
import { chat, toolDefinition } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";
import { z } from "zod";

const getWeatherDef = toolDefinition({
  name: "get_weather",
  description: "Get the current weather",
  inputSchema: z.object({
    location: z.string(),
  }),
});

const getWeather = getWeatherDef.server(async ({ location }) => {
  return { temperature: 72, conditions: "sunny" };
});

const messages = [{ role: "user", content: "What's the weather in NYC?" }];

const stream = chat({
  adapter: openRouterText("openai/gpt-5.2"),
  messages,
  tools: [getWeather],
});
```

### Environment Variables

Set your API key in environment variables:

```bash lines theme={null}
OPENROUTER_API_KEY=sk-or-...
```

### Model Routing and Provider Preferences

TanStack AI supports OpenRouter's powerful routing features through the `modelOptions` parameter. You can configure model fallbacks, provider sorting, and data policies.

#### Model Fallbacks

Specify backup models to try if the primary model is unavailable:

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("openai/gpt-5.2"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    models: ["anthropic/claude-sonnet-4.5", "google/gemini-3.1-pro-preview"],
    route: "fallback",
  },
});
```

#### Provider Sorting

Sort providers by price, throughput, or latency instead of using default routing:

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

// Prioritize fastest providers
const stream = chat({
  adapter: openRouterText("openai/gpt-5.2"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    provider: {
      sort: "throughput",
    },
  },
});
```

#### Provider Ordering

Specify an explicit order of providers to try:

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("anthropic/claude-sonnet-4.5"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    provider: {
      order: ["anthropic", "amazon-bedrock", "google-vertex"],
      allow_fallbacks: true,
    },
  },
});
```

#### Data Privacy Controls

Control data collection and use Zero Data Retention (ZDR) providers:

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("openai/gpt-5.2"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    provider: {
      data_collection: "deny",
      zdr: true,
    },
  },
});
```

#### Filtering Providers

Include or exclude specific providers:

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("meta-llama/llama-3.3-70b-instruct"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    provider: {
      only: ["together", "fireworks"],
      ignore: ["azure"],
      quantizations: ["fp16", "bf16"],
    },
  },
});
```

#### Cost Controls

Set maximum price limits for requests:

```typescript title="TypeScript" lines theme={null}
import { chat } from "@tanstack/ai";
import { openRouterText } from "@tanstack/ai-openrouter";

const stream = chat({
  adapter: openRouterText("z-ai/glm-4.7"),
  messages: [{ role: "user", content: "Hello!" }],
  modelOptions: {
    provider: {
      max_price: {
        prompt: 0.5,
        completion: 2,
      },
    },
  },
});
```

For more advanced routing options like performance thresholds and partition-based sorting, see the [Provider Routing documentation](https://openrouter.ai/docs/guides/routing/provider-selection.md).

### Resources

For more information and detailed documentation, check out these resources:

* [TanStack AI Documentation](https://tanstack.com/ai/latest/docs/getting-started/overview) - Learn the basics of TanStack AI
* [OpenRouter Adapter Docs](https://tanstack.com/ai/latest/docs/adapters/openrouter) - Official TanStack AI OpenRouter adapter documentation
* [OpenRouter Models](https://openrouter.ai/models) - Browse available models

