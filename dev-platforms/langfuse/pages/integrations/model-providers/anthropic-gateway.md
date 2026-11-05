---
title: "Anthropic SDK"
source: https://langfuse.com/integrations/model-providers/anthropic-gateway.md
path: integrations/model-providers/anthropic-gateway
---

---
title: "Anthropic SDK with the Langfuse AI Gateway"
sidebarTitle: Anthropic SDK (gateway)
seoTitle: "Use the Anthropic SDK with the Langfuse AI Gateway (beta)"
description: Call Claude models through the Langfuse AI Gateway with the official Anthropic client SDKs for Python and TypeScript, using the Messages API.
logo: /images/integrations/anthropic_icon.png
logoAppearance: dark
category: Integrations
---

# Anthropic SDK with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

Use Anthropic's official [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) for Python and TypeScript with the gateway by changing the base URL and the API key. Requests need an `ANTHROPIC` provider credential in your organization.

  For tracing the Anthropic SDK without the gateway, see the [Anthropic (Python)](/integrations/model-providers/anthropic) and [Anthropic (JS/TS)](/integrations/model-providers/anthropic-js) integrations.

Before you start, create a gateway key and export `LANGFUSE_GATEWAY_HOST` and `LANGFUSE_GATEWAY_KEY` as in [Send your first request](/docs/gateway/get-started/first-request). Replace `<model-id>` with an ID from the [models endpoint](/docs/gateway/features/rest-api#routes).

## Configure the client [#configure-the-client]

Set the base URL to the gateway's Anthropic route, `/anthropic`, without `/v1`: the SDK appends `/v1/messages` itself. Pass the gateway key as the API key. The SDK sends it as `x-api-key`.

**Python**

```bash
pip install anthropic
```

```python
import os

from anthropic import Anthropic

client = Anthropic(
    base_url=os.environ["LANGFUSE_GATEWAY_HOST"] + "/anthropic",
    api_key=os.environ["LANGFUSE_GATEWAY_KEY"],
)
```

**TypeScript**

```bash
npm install @anthropic-ai/sdk
```

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/anthropic`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});
```

## Messages API [#messages]

**Python**

```python
message = client.messages.create(
    model="<model-id>",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello"}],
)
print(message.content[0].text)
```

To stream the response:

```python
with client.messages.stream(
    model="<model-id>",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

**TypeScript**

```ts
const message = await client.messages.create({
  model: "<model-id>",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Say hello" }],
});
console.log(message.content);
```

To stream the response:

```ts
const stream = client.messages.stream({
  model: "<model-id>",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Say hello" }],
});
stream.on("text", (text) => process.stdout.write(text));
await stream.finalMessage();
```

## Add request headers [#request-headers]

Set [request headers](/docs/gateway/features/tracing#request-headers) on the client for every call, or per call for values such as a session ID.

**Python**

```python
client = Anthropic(
    base_url=os.environ["LANGFUSE_GATEWAY_HOST"] + "/anthropic",
    api_key=os.environ["LANGFUSE_GATEWAY_KEY"],
    default_headers={"langfuse-tags": "checkout,production"},
)

message = client.messages.create(
    model="<model-id>",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello"}],
    extra_headers={"langfuse-session-id": "<session-id>"},
)
```

**TypeScript**

```ts
const client = new Anthropic({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/anthropic`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
  defaultHeaders: { "langfuse-tags": "checkout,production" },
});

const message = await client.messages.create(
  {
    model: "<model-id>",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Say hello" }],
  },
  { headers: { "langfuse-session-id": "<session-id>" } },
);
```

  The gateway already records every call. Don't also trace the same client with
  the [Langfuse Anthropic integration](/integrations/model-providers/anthropic),
  or each call is recorded twice.

## Claude Agent SDK [#claude-agent-sdk]

The [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) runs Claude Code under the hood, so it is configured with the same environment variables as Claude Code, not with a client base URL. Set `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` in the environment of the agent process, as described in the [Claude Code guide](/integrations/developer-tools/claude-code-gateway#setup).

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/model-providers/anthropic-gateway.md`.

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

