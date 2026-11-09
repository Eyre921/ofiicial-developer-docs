---
title: "Pi"
source: https://langfuse.com/integrations/developer-tools/pi-agent-gateway.md
path: integrations/developer-tools/pi-agent-gateway
---

---
title: "Pi with the Langfuse AI Gateway"
sidebarTitle: Pi Agent (gateway)
seoTitle: "Trace the Pi coding agent with the Langfuse AI Gateway (beta)"
description: Route the Pi coding agent through the Langfuse AI Gateway to trace every model call, tool call, token, and cost.
logo: /images/integrations/pi-agent_icon.svg
category: Integrations
---

# Pi with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

**Requires** Pi 1.5.0 or later and an `ANTHROPIC` and/or `OPENAI` provider credential.

  For tracing Pi without the gateway, see the [Pi Agent integration](/integrations/developer-tools/pi-agent).

**Start with Langfuse** [Sign up](/cloud)

## Setup [#setup]

<Steps>

### Create a gateway API key [#create-a-key]

Create a gateway API key under **AI Gateway → Gateway keys**. See [API keys](/docs/gateway/features/api-keys#create-a-key).

Export it in the shell you start Pi from:

```sh
export LANGFUSE_GATEWAY_KEY="<your-gateway-key>"
```

To keep the setup across sessions, add the `export` lines to `~/.zshrc`.

### Install Pi [#install]

Install Pi from the `@earendil-works/pi-coding-agent` package. The older `@mariozechner/…` package is deprecated.

```sh
npm install -g @earendil-works/pi-coding-agent
```

### Add the gateway providers [#add-the-providers]

Add gateway providers to `~/.pi/agent/models.json` (or `$PI_CODING_AGENT_DIR/models.json`). `$VAR` interpolation works in `apiKey` and in headers.

```json
{
  "providers": {
    "langfuse-anthropic": {
      "baseUrl": "https://gateway.cloud.langfuse.com/anthropic",
      "api": "anthropic-messages",
      "apiKey": "$LANGFUSE_GATEWAY_KEY",
      "compat": { "sendSessionAffinityHeaders": true },
      "headers": {
        "langfuse-tags": "pi,<team>",
        "langfuse-environment": "local"
      },
      "models": [
        {
          "id": "<anthropic-model-id>",
          "reasoning": true,
          "input": ["text", "image"],
          "contextWindow": 200000,
          "maxTokens": 64000
        }
      ]
    },
    "langfuse-openai": {
      "baseUrl": "https://gateway.cloud.langfuse.com/openai/v1",
      "api": "openai-responses",
      "apiKey": "$LANGFUSE_GATEWAY_KEY",
      "headers": {
        "langfuse-tags": "pi,<team>",
        "langfuse-environment": "local"
      },
      "models": [
        {
          "id": "<openai-model-id>",
          "reasoning": true,
          "input": ["text", "image"],
          "contextWindow": 400000,
          "maxTokens": 128000
        }
      ]
    }
  }
}
```

```sh
pi --provider langfuse-anthropic --model <anthropic-model-id>
pi -p --provider langfuse-openai --model <openai-model-id> "Summarize README.md"
```

- **Sessions on the Anthropic route require `"compat": { "sendSessionAffinityHeaders": true }`.** Without it, Pi sends no session ID to Anthropic and the generations have no session. The OpenAI route always sends the session ID.
- The Anthropic `baseUrl` has **no** `/v1`. The OpenAI `baseUrl` **includes** `/v1`.
- Use `"api": "openai-responses"`. `openai-completions` uses [Chat Completions](/docs/gateway/features/rest-api#routes), which the gateway serves but which has not been verified with pi.
- Replace the model IDs with IDs from [`/models`](/docs/gateway/get-started/first-request#list-models), and set `reasoning`, `contextWindow`, and `maxTokens` to the values of that model.
- List every model you use under `models`. Otherwise, Pi warns "Using custom model id" and guesses the context window and reasoning support.

### Verify [#verify]

Run a prompt:

```sh
pi -p --provider langfuse-anthropic --model <anthropic-model-id> "Reply with exactly: pong"
```

If Pi replies, it runs through the gateway.

</Steps>

## Turn grouping (experimental, optional) [#turn-grouping]

  Experimental. This extension works with the current gateway but is not an
  official, published package yet. A dedicated turn header is planned.

Pi sends no turn ID, so every model call is its own trace. A small [extension](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md) can send a W3C `traceparent` with a new trace ID per prompt, which the gateway adopts. Save it as `~/.pi/agent/extensions/langfuse-turn.ts` (or `.pi/extensions/` in a project), or load it for one run with `pi -e ./langfuse-turn.ts`:

```ts
import { randomBytes } from "node:crypto";

export default function (pi: any) {
  let traceId: string | undefined;

  // One trace per user prompt (agent run).
  pi.on("agent_start", () => {
    traceId = randomBytes(16).toString("hex");
  });

  pi.on("before_provider_headers", (event: any) => {
    if (!traceId) return;
    const spanId = randomBytes(8).toString("hex");
    event.headers["traceparent"] = `00-${traceId}-${spanId}-01`;
  });
}
```

- All model calls of a prompt, including retries and follow-up messages within the run, land in one trace. The generations appear as top-level observations, because the parent span does not exist in Langfuse.
- Calls after the run ends, such as auto-compaction, join the prompt that triggered them.

## Troubleshooting and FAQ [#troubleshooting-and-faq]

### Can headers differ per request? [#static-headers]

No. Headers are static per provider. Vary them with `$VAR`, or define several providers.

### Where are thinking tokens counted? [#thinking-tokens]

On Anthropic, thinking tokens are counted inside output tokens. OpenAI reasoning tokens are shown separately.

### Why isn't Pi's prompt cached on small models? [#cache-miss]

Pi's default prompt (about 2,000 tokens) is cached on Sonnet but is below the minimum cacheable size of Haiku 4.5.

[Ask another question](/docs/ask-ai)

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/developer-tools/pi-agent-gateway.md`.

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

