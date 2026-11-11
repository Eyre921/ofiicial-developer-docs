---
title: "OpenAI SDK"
source: https://langfuse.com/integrations/model-providers/openai-gateway.md
path: integrations/model-providers/openai-gateway
---

---
title: "OpenAI SDK with the Langfuse AI Gateway"
sidebarTitle: OpenAI SDK (gateway)
seoTitle: "Use the OpenAI SDK with the Langfuse AI Gateway (beta)"
description: Call OpenAI models through the Langfuse AI Gateway with the official OpenAI SDKs for Python and TypeScript, using the Responses or Chat Completions API.
logo: /images/integrations/openai_icon.svg
logoAppearance: dark
category: Integrations
---

# OpenAI SDK with the Langfuse AI Gateway

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

Use the official [OpenAI SDKs](https://developers.openai.com/api/docs/libraries) for Python and TypeScript with the gateway by changing the base URL and the API key. Requests need an `OPENAI` provider connection in your organization.

  For tracing the OpenAI SDK without the gateway, see the [OpenAI (Python)](/integrations/model-providers/openai-py) and [OpenAI (JS/TS)](/integrations/model-providers/openai-js) integrations.

Before you start, create a gateway key and export `LANGFUSE_GATEWAY_HOST` and `LANGFUSE_GATEWAY_KEY` as in [Send your first request](/docs/gateway/get-started/first-request). Replace `<model-id>` with an ID from the [models endpoint](/docs/gateway/features/rest-api#routes).

**Start with Langfuse** [Sign up](/cloud)

## Configure the client [#configure-the-client]

Set the base URL to the gateway's OpenAI route, `/openai/v1`, and pass the gateway key as the API key. The SDK sends it as `Authorization: Bearer`.

**Python**

```bash
pip install openai
```

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.environ["LANGFUSE_GATEWAY_HOST"] + "/openai/v1",
    api_key=os.environ["LANGFUSE_GATEWAY_KEY"],
)
```

**TypeScript**

```bash
npm install openai
```

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/openai/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
});
```

## Responses API [#responses]

**Python**

```python
response = client.responses.create(
    model="<model-id>",
    input="Say hello",
)
print(response.output_text)
```

**TypeScript**

```ts
const response = await client.responses.create({
  model: "<model-id>",
  input: "Say hello",
});
console.log(response.output_text);
```

## Chat Completions [#chat-completions]

**Python**

```python
completion = client.chat.completions.create(
    model="<model-id>",
    messages=[{"role": "user", "content": "Say hello"}],
)
print(completion.choices[0].message.content)
```

**TypeScript**

```ts
const completion = await client.chat.completions.create({
  model: "<model-id>",
  messages: [{ role: "user", content: "Say hello" }],
});
console.log(completion.choices[0].message.content);
```

  Streamed Chat Completions end with a usage chunk whose `choices` array is
  empty, even if you didn't ask for usage. Skip chunks without choices. See
  [streaming usage](/docs/gateway/features/rest-api#streaming-usage).

## Add request headers [#request-headers]

Set [request headers](/docs/gateway/features/tracing#request-headers) on the client for every call, or per call for values such as a session ID.

**Python**

```python
client = OpenAI(
    base_url=os.environ["LANGFUSE_GATEWAY_HOST"] + "/openai/v1",
    api_key=os.environ["LANGFUSE_GATEWAY_KEY"],
    default_headers={"langfuse-tags": "checkout,production"},
)

response = client.responses.create(
    model="<model-id>",
    input="Say hello",
    extra_headers={"langfuse-session-id": "<session-id>"},
)

completion = client.chat.completions.create(
    model="<model-id>",
    messages=[{"role": "user", "content": "Say hello"}],
    extra_headers={"langfuse-session-id": "<session-id>"},
)
```

**TypeScript**

```ts
const client = new OpenAI({
  baseURL: `${process.env.LANGFUSE_GATEWAY_HOST}/openai/v1`,
  apiKey: process.env.LANGFUSE_GATEWAY_KEY,
  defaultHeaders: { "langfuse-tags": "checkout,production" },
});

const response = await client.responses.create(
  { model: "<model-id>", input: "Say hello" },
  { headers: { "langfuse-session-id": "<session-id>" } },
);

const completion = await client.chat.completions.create(
  {
    model: "<model-id>",
    messages: [{ role: "user", content: "Say hello" }],
  },
  { headers: { "langfuse-session-id": "<session-id>" } },
);
```

  The gateway already records every call. Don't also trace the same client with
  the [Langfuse OpenAI integration](/integrations/model-providers/openai-py), or
  each call is recorded twice.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/integrations/model-providers/openai-gateway.md`.

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

