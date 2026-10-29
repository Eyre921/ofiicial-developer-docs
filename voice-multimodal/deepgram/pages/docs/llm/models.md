---
title: "Models overview"
source: https://developers.deepgram.com/docs/llm/models.md
path: docs/llm/models
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Models overview

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

Both models use the same endpoint and the same [request and response format](/docs/llm/request-response-format). To switch models, change the `model` field.

## Model comparison

|                                                       | Think-Fast                                                   | phoneLLM mini                                                                                              |
| ----------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `model` value                                         | `think-fast`                                                 | `phonellm-mini-alpha-2-fp8`                                                                                |
| Use it for                                            | The only LLM in a cascaded voice agent                       | Voice agent pipelines where speed and size come first                                                      |
| Streaming                                             | Yes                                                          | Yes                                                                                                        |
| Function calling                                      | Yes                                                          | Yes                                                                                                        |
| Reasoning                                             | Off by default. Set `reasoning_effort` to `none` or omit it. | Off by default. Set `reasoning_effort` to `none` or omit it; other values put reasoning text in the reply. |
| [Model Improvement Program](/docs/llm/data-retention) | Always included. `mip_opt_out: true` is rejected.            | Included by default. `mip_opt_out: true` is supported.                                                     |
| Voice Agent `think` provider                          | `deepgram`                                                   | `deepgram`                                                                                                 |

## Think-Fast

Think-Fast is an instruction-following model built for voice conversations. It follows a system prompt and calls your function tools, so it can be the only LLM in a cascaded voice agent. It's both fast and capable, and it writes replies meant to be spoken by a TTS provider.

It doesn't reason by default. Leave `reasoning_effort` unset or set it to `none`: other values add reasoning tokens and latency before the reply starts. Put the steps you want it to follow directly in the system prompt. See [Prompting Deepgram LLMs](/docs/llm/prompting).

## phoneLLM mini

phoneLLM mini is an open-weights text model from Pipecat, trained for voice agent pipelines. Choose it when speed and size are the top priority. It is a 30B-parameter mixture-of-experts model with 3.5B active parameters, based on NVIDIA Nemotron 3 Nano.

* **Tool calling:** supported. The model was trained on synthetic voice agent sessions, including [Pipecat Flows](https://www.pipecat.ai/labs/phonellm-alpha-2) sessions.
* **Reasoning:** off. Set `reasoning_effort` to `none` or omit it; other values put reasoning text in the reply, ending in `</think>`, which a voice app would read aloud. In the Voice Agent, the same setting is `agent.think.provider.reasoning_mode`.
* **Temperature:** Pipecat recommends `0.0`.

For model details and benchmarks, see [Pipecat's phoneLLM Alpha 2 announcement](https://www.pipecat.ai/labs/phonellm-alpha-2).

## Availability

During Early Access, both models run on the global endpoint:

```
https://agent.deepgram.com/v1/think
```

Regional endpoints are coming soon.
