---
title: "Deepgram LLMs overview"
source: https://developers.deepgram.com/docs/llm.md
path: docs/llm
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deepgram LLMs overview

Deepgram LLMs are language models that Deepgram hosts for voice workloads. You send a conversation to `POST https://agent.deepgram.com/v1/think` and get the next assistant message back, either as a single JSON response or as a stream of server-sent events. They are in Early Access; read the terms below before you build.

Think-Fast is also available inside the Voice Agent API: select it with the `deepgram` think provider, or call it directly to use it in your own pipeline.

## Models

| Model         | `model` value               | Use it for                                                                             |
| ------------- | --------------------------- | -------------------------------------------------------------------------------------- |
| Think-Fast    | `think-fast`                | The LLM in a cascaded voice agent. Follows a system prompt and calls tools on its own. |
| phoneLLM mini | `phonellm-mini-alpha-2-fp8` | Voice agent pipelines where speed and size come first.                                 |

See [Models overview](/docs/llm/models) for how the models compare. To send your first request, see [Getting started](/docs/llm/getting-started).

## Early Access

> **Warning**
>
> **Deepgram LLMs are in Early Access.** Before you build on them, know what that means:
>
> * **Who can use them:** current Deepgram contract customers whose projects are enrolled in the Early Access program. [Talk to sales](https://deepgram.com/contact-us) for access.
> * **What can change:** request fields, response details, model IDs, and limits can change before general availability (GA), with little notice. Do not run production traffic on these models.
> * **Where they run:** the global endpoint only. Regional endpoints are coming soon.
> * **SDKs:** Deepgram SDKs do not support these models yet. SDK support is planned for GA. Call the endpoint with any HTTP client.
> * **Data:** Think-Fast can only be used with the Model Improvement Program, so every Think-Fast request is stored for model training and abuse monitoring. phoneLLM mini requests can opt out. See [Data retention and MIP](/docs/llm/data-retention).
> * **Price:** free during Early Access.

## Features

* **Streaming and non-streaming responses.** Set `stream: true` to receive tokens as server-sent events.
* **Function calling.** Define function tools and pass tool-call history back across turns.
* **Generation controls.** Tune `temperature` and `reasoning_effort` per request.
* **Voice Agent and custom pipelines.** Use the models inside the Voice Agent API or in your own STT, LLM, and TTS loop.

## Next steps

* [Getting started](/docs/llm/getting-started): send your first request
* [Request and response format](/docs/llm/request-response-format): every field the endpoint accepts and returns
* [Build a cascaded agent](/docs/llm/cascaded-agent): wire Think-Fast between Flux STT and Flux TTS
* [Data retention and MIP](/docs/llm/data-retention): what Deepgram stores, and which models can opt out of MIP
