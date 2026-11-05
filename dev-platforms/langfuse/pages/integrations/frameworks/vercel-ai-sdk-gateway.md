---
title: "Vercel AI SDK"
source: https://langfuse.com/integrations/frameworks/vercel-ai-sdk-gateway.md
path: integrations/frameworks/vercel-ai-sdk-gateway
---

---
title: "Vercel AI SDK with the Langfuse AI Gateway"
sidebarTitle: Vercel AI SDK (gateway)
seoTitle: "Use the Vercel AI SDK with the Langfuse AI Gateway (beta)"
description: Call OpenAI and Anthropic models through the Langfuse AI Gateway with the Vercel AI SDK by pointing its OpenAI and Anthropic providers at the gateway.
logo: /images/integrations/vercel_ai_sdk_icon.png
logoAppearance: multicolor
category: Integrations
---

# Vercel AI SDK with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

Use the [AI SDK](https://ai-sdk.dev/docs/introduction) by Vercel with the gateway by pointing its OpenAI or Anthropic provider at the gateway. Each provider needs the matching provider credential in your organization: `OPENAI` for OpenAI models, `ANTHROPIC` for Anthropic models.

  For tracing the Vercel AI SDK without the gateway, see the [Vercel AI SDK integration](/integrations/frameworks/vercel-ai-sdk).

Before you start, create a gateway key and export `LANGFUSE_GATEWAY_HOST` and `LANGFUSE_GATEWAY_KEY` as in [Send your first request](/docs/gateway/get-started/first-request). Replace `<model-id>` with an ID from the [models endpoint](/docs/gateway/features/rest-api#routes).

## Configure the provider [#configure-the-provider]

Create the provider with the gateway's route as base URL and the gateway key as API key.

**OpenAI**

Use the gateway's OpenAI route, `/openai/v1`, with the [OpenAI provider](https://ai-sdk.dev/providers/ai-sdk-providers/openai).

```bash
npm install ai @ai-sdk/openai
```

```ts
import { createOpenAI } from "@ai-sdk/openai";
import { generateText } from "ai";

const openai = createOpenAI({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/openai/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});

const { text } = await generateText({
  model: openai("<model-id>"),
  prompt: "Say hello",
});
console.log(text);
```

`openai("<model-id>")` uses the Responses API. To use Chat Completions instead, use `openai.chat("<model-id>")`.

**Anthropic**

Use the gateway's Anthropic route with the [Anthropic provider](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic). Unlike the Anthropic SDK, the AI SDK provider expects `/v1` in the base URL, so use `/anthropic/v1`.

```bash
npm install ai @ai-sdk/anthropic
```

```ts
import { createAnthropic } from "@ai-sdk/anthropic";
import { generateText } from "ai";

const anthropic = createAnthropic({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/anthropic/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});

const { text } = await generateText({
  model: anthropic("<model-id>"),
  prompt: "Say hello",
});
console.log(text);
```

## Add request headers [#request-headers]

Set [request headers](/docs/gateway/features/tracing#request-headers) on the provider for every call, or per call for values such as a session ID.

**OpenAI**

```ts
import { createOpenAI } from "@ai-sdk/openai";
import { generateText } from "ai";

const openai = createOpenAI({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/openai/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
  headers: { "langfuse-tags": "checkout,production" },
});

const { text } = await generateText({
  model: openai("<model-id>"),
  prompt: "Say hello",
  headers: { "langfuse-session-id": "<session-id>" },
});
```

**Anthropic**

```ts
import { createAnthropic } from "@ai-sdk/anthropic";
import { generateText } from "ai";

const anthropic = createAnthropic({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/anthropic/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
  headers: { "langfuse-tags": "checkout,production" },
});

const { text } = await generateText({
  model: anthropic("<model-id>"),
  prompt: "Say hello",
  headers: { "langfuse-session-id": "<session-id>" },
});
```

  The gateway already records every call. Don't also trace the same calls with
  the [Langfuse Vercel AI SDK integration](/integrations/frameworks/vercel-ai-sdk),
  or each model call is recorded twice.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/frameworks/vercel-ai-sdk-gateway.md`.

### Querying these docs

If the answer is not on this page, query the documentation instead of guessing:

- **Semantic search** across all Langfuse docs, returning an answer with the relevant pages and excerpts. Ask a specific, self-contained question:

  ```bash
  curl -sG "https://langfuse.com/api/search-docs" --data-urlencode "query=How do I trace a LangGraph agent?"
  ```

- **Index of every page**: <https://langfuse.com/llms.txt>, with per-section indexes [llms-docs.txt](https://langfuse.com/llms-docs.txt), [llms-integrations.txt](https://langfuse.com/llms-integrations.txt), and [llms-self-hosting.txt](https://langfuse.com/llms-self-hosting.txt).

### Before writing Langfuse code

- **Install the [Langfuse Agent Skill](https://langfuse.com/docs/api-and-data-platform/features/agent-skill).** It encodes Langfuse's own best practices for instrumentation, prompt management, and evaluation, and materially improves results.
- **Read [What does a good trace look like?](https://langfuse.com/docs/observability/best-practices.md)** before instrumenting an application.
- **Verify endpoints, parameters, and response fields** against the [API reference](https://api.reference.langfuse.com) instead of inferring them from code examples.
- **Use the [Langfuse CLI](https://langfuse.com/docs/api-and-data-platform/features/cli)** (`npx @langfuse/cli api <resource> <action>`) to read or write traces, prompts, datasets, and scores from the terminal.

Found an error in these docs? Please open an issue at <https://github.com/langfuse/langfuse-docs/issues>.

