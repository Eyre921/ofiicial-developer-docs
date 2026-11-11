---
title: "REST API"
source: https://langfuse.com/docs/gateway/features/rest-api.md
path: docs/gateway/features/rest-api
---

---
title: REST API
seoTitle: "Langfuse AI Gateway REST API: models, Responses, Chat Completions, Messages (beta)"
description: Base URLs, authentication, and endpoints of the Langfuse AI Gateway, including the models endpoints and the OpenAI Responses, OpenAI Chat Completions, and Anthropic Messages APIs.
---

# REST API

  **Beta.** The Langfuse AI Gateway is in public beta and can still change.

You can call the gateway directly over HTTP, for example from a language without an SDK or from a script. Request and response bodies are the model provider's own, so for parameters and fields, see the provider's API reference linked in the [endpoints](#routes) table. This page covers what's specific to the gateway: base URLs, authentication, and endpoints.

## Base URLs [#base-urls]

| Route     | Base URL                                          |
| --------- | ------------------------------------------------- |
| OpenAI    | `https://gateway.cloud.langfuse.com/openai/v1`    |
| Anthropic | `https://gateway.cloud.langfuse.com/anthropic/v1` |

These are the EU URLs. For other regions, replace the host with your [gateway host](#gateway-hosts).

### Gateway hosts [#gateway-hosts]

| Region | Gateway host                               |
| ------ | ------------------------------------------ |
| EU     | `https://gateway.cloud.langfuse.com`       |
| US     | `https://gateway.us.cloud.langfuse.com`    |
| JP     | `https://gateway.jp.cloud.langfuse.com`    |
| HIPAA  | `https://gateway.hipaa.cloud.langfuse.com` |

A gateway key only works on its own region's host. On self-hosted Langfuse, use the gateway URL your deployment configured (`LANGFUSE_AI_GATEWAY_PUBLIC_URL`, see [Self-hosting the AI Gateway](/self-hosting/configuration/ai-gateway)).

## Authentication [#authentication]

Every endpoint requires a [gateway API key](/docs/gateway/features/api-keys):

- **OpenAI route:** `Authorization: Bearer <gateway key>`
- **Anthropic route:** `x-api-key: <gateway key>`, or a Bearer token. If you send both, they must have the same value.

## Endpoints [#routes]

| Endpoint                                   | Provider reference                                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `GET /openai/v1/models`                    | [List models](https://developers.openai.com/api/reference/resources/models/methods/list)                                       |
| `GET /anthropic/v1/models`                 | [List models](https://platform.claude.com/docs/en/api/models/list)                                                             |
| `POST /openai/v1/responses`                | [Create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)                            |
| `POST /openai/v1/responses/compact`        | [Compact a response](https://developers.openai.com/api/reference/resources/responses/methods/compact)                          |
| `POST /openai/v1/chat/completions`         | [Create a chat completion](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create) |
| `POST /anthropic/v1/messages`              | [Create a message](https://platform.claude.com/docs/en/api/messages/create)                                                    |
| `POST /anthropic/v1/messages/count_tokens` | [Count tokens](https://platform.claude.com/docs/en/api/messages/count_tokens)                                                  |

The models endpoints return the models your key can call, with IDs in the form `<connection>:<model>` (see [model IDs](/docs/gateway/features/models#model-ids)). The gateway doesn't translate between formats, so each endpoint needs a connection to a provider that supports its API format.

  Other paths return `404`, including websockets and realtime APIs. Request
  bodies must be uncompressed: a `Content-Encoding` other than `identity` fails
  with `415`.

## Streaming usage [#streaming-usage]

On streamed Chat Completions requests, the gateway sets `stream_options.include_usage` so that every call gets token usage and cost.

  Your client receives a final chunk with an **empty `choices` array** and a
  `usage` object, just before `data: [DONE]`. Code that reads
  `chunk.choices[0]` on every chunk needs a guard.

<!-- agent-instructions -->

---

## Agent Instructions

This page is part of the [Langfuse](https://langfuse.com) documentation, published as plain Markdown for AI agents. Every page is available as Markdown by appending `.md` to its URL, or by sending an `Accept: text/markdown` header. This page: `https://langfuse.com/docs/gateway/features/rest-api.md`.

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

