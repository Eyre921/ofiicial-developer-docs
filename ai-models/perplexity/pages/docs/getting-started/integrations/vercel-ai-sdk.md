---
title: "Perplexity with the Vercel AI SDK"
source: https://docs.perplexity.ai/docs/getting-started/integrations/vercel-ai-sdk
path: docs/getting-started/integrations/vercel-ai-sdk
---

Use Perplexity's web-grounded models with the Vercel AI SDK through the official @ai-sdk/perplexity provider.

## Overview

The [Vercel AI SDK](https://ai-sdk.dev) is a TypeScript-first toolkit for building AI-powered apps with a unified provider interface, streaming primitives, and React hooks. The official `@ai-sdk/perplexity` provider gives you full access to Perplexity's Sonar models — including streaming, citations, image results, and PDF inputs — with a one-line model identifier.

<Info>
  **Vercel AI SDK** powers `generateText`, `streamText`, `generateObject`, and React hooks like `useChat` and `useCompletion`. Learn more at [ai-sdk.dev](https://ai-sdk.dev).
</Info>

## Installation

<Tabs>
  <Tab title="pnpm">
    ```bash theme={null}
    pnpm add @ai-sdk/perplexity ai
    ```
  </Tab>

  <Tab title="npm">
    ```bash theme={null}
    npm install @ai-sdk/perplexity ai
    ```
  </Tab>

  <Tab title="yarn">
    ```bash theme={null}
    yarn add @ai-sdk/perplexity ai
    ```
  </Tab>

  <Tab title="bun">
    ```bash theme={null}
    bun add @ai-sdk/perplexity ai
    ```
  </Tab>
</Tabs>

## API Key Setup

Set your Perplexity API key:

```bash theme={null}
export PERPLEXITY_API_KEY="your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/account/api/keys">
  Generate your Perplexity API key from the API portal.
</Card>

## Quick Start

Import the default provider instance and call `generateText`:

```ts theme={null}
import { perplexity } from "@ai-sdk/perplexity";
import { generateText } from "ai";

const { text } = await generateText({
  model: perplexity("sonar-pro"),
  prompt: "What are the latest developments in quantum computing?",
});

console.log(text);
```

## Accessing Citations

Every response includes a `sources` array of the URLs Perplexity consulted:

```ts theme={null}
import { perplexity } from "@ai-sdk/perplexity";
import { generateText } from "ai";

const { text, sources } = await generateText({
  model: perplexity("sonar-pro"),
  prompt: "What are the latest developments in quantum computing?",
});

console.log(text);
console.log(sources);
```

## Provider Options

Pass Perplexity-specific parameters through `providerOptions.perplexity`:

```ts theme={null}
import { perplexity } from "@ai-sdk/perplexity";
import { generateText } from "ai";

const result = await generateText({
  model: perplexity("sonar-pro"),
  prompt: "What are the latest developments in quantum computing?",
  providerOptions: {
    perplexity: {
      return_images: true,
      search_recency_filter: "week",
    },
  },
});

console.log(result.providerMetadata);
// {
//   perplexity: {
//     usage: { citationTokens: 5286, numSearchQueries: 1 },
//     images: [{ imageUrl: "...", originUrl: "...", height: 1280, width: 720 }],
//   },
// }
```

Any other [Perplexity API parameter](/api-reference/sonar-post) can be passed the same way.

| Option                  | Type      | Description                                        |
| ----------------------- | --------- | -------------------------------------------------- |
| `return_images`         | `boolean` | Include images in the response (Tier-2+ accounts). |
| `search_recency_filter` | `string`  | One of `'hour'`, `'day'`, `'week'`, `'month'`.     |

## Custom Provider Configuration

Use `createPerplexity` when you need a custom base URL, headers, or a custom fetch implementation:

```ts theme={null}
import { createPerplexity } from "@ai-sdk/perplexity";

const perplexity = createPerplexity({
  apiKey: process.env.PERPLEXITY_API_KEY ?? "",
  baseURL: "https://api.perplexity.ai",
  headers: {
    "X-Pplx-Integration": "my-app/1.0",
  },
});
```

## PDF Inputs

Sonar models can read PDF files passed as `file` message parts:

```ts theme={null}
import { perplexity } from "@ai-sdk/perplexity";
import { generateText } from "ai";
import fs from "node:fs";

const result = await generateText({
  model: perplexity("sonar-pro"),
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What is this document about?" },
        {
          type: "file",
          data: fs.readFileSync("./data/ai.pdf"),
          mediaType: "application/pdf",
          filename: "ai.pdf",
        },
      ],
    },
  ],
});
```

You can also pass a PDF URL:

```ts theme={null}
{
  type: "file",
  data: new URL("https://example.com/document.pdf"),
  mediaType: "application/pdf",
  filename: "document.pdf",
}
```

## Supported Models

| Model                 | Image Input | Object Generation |
| --------------------- | ----------- | ----------------- |
| `sonar`               | Yes         | Yes               |
| `sonar-pro`           | Yes         | Yes               |
| `sonar-reasoning`     | Yes         | Yes               |
| `sonar-reasoning-pro` | Yes         | Yes               |
| `sonar-deep-research` | No          | Yes               |

See [all available models](/docs/sonar/models) for full capability details.

## Streaming and React Hooks

The provider works with `streamText`, `useChat`, and `useCompletion` from `ai/react`. Drop `perplexity("sonar-pro")` into any AI SDK helper that takes a model:

```ts theme={null}
import { perplexity } from "@ai-sdk/perplexity";
import { streamText } from "ai";

const result = streamText({
  model: perplexity("sonar"),
  prompt: "Give me a one-sentence summary of this week's AI news.",
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Links & Resources

<CardGroup>
  <Card title="Vercel AI SDK Provider" icon="book" href="https://ai-sdk.dev/providers/ai-sdk-providers/perplexity">
    Official `@ai-sdk/perplexity` provider docs.
  </Card>

  <Card title="Vercel AI SDK Docs" icon="globe" href="https://ai-sdk.dev/docs">
    Full Vercel AI SDK documentation.
  </Card>

  <Card title="Perplexity API Reference" icon="code" href="/api-reference/sonar-post">
    Full Perplexity API parameter reference.
  </Card>

  <Card title="Perplexity Models" icon="sparkles" href="/docs/sonar/models">
    Available Sonar models and capabilities.
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Browse the [Vercel AI SDK documentation](https://ai-sdk.dev/docs)
* Review our [FAQ](/docs/resources/faq)
