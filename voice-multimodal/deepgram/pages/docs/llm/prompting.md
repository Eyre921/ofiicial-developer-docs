---
title: "Prompting Deepgram LLMs"
source: https://developers.deepgram.com/docs/llm/prompting.md
path: docs/llm/prompting
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Prompting Deepgram LLMs

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

For the fundamentals of writing for voice (no formatting, short turns, data written for the ear), start with [Prompting Voice Agents](/docs/prompting-voice-agents). Those rules apply to Deepgram LLMs too. This page covers what is specific to Think-Fast and phoneLLM mini.

## Spell out the steps

Think-Fast follows instructions closely and doesn't reason by default. Leave `reasoning_effort` unset or set it to `none`, because other values add reasoning tokens and latency. Write the procedure you want into the system prompt instead of asking the model to work it out.

```text
When a caller asks about an order:
1. Ask for the order number if they have not given it.
2. Call get_order_status with the order number.
3. Read back the status in one sentence.
4. Ask if there is anything else you can help with.
```

## Put instructions in the system message

Send the prompt as a `system` message with plain-string `content`. The endpoint does not accept the array-of-content-parts form.

## Write tool descriptions for the model

`function.description` is required on every tool, and it is the main signal the model uses to decide when to call one. Say what the function does, when to call it, and when not to.

```json
{
  "type": "function",
  "function": {
    "name": "transfer_to_agent",
    "description": "Transfer the caller to a human agent. Call this only when the caller asks for a person or the issue involves a refund over $500. Do not call it for order status questions.",
    "parameters": {
      "type": "object",
      "properties": {
        "reason": { "type": "string", "description": "Why the caller needs a person." }
      },
      "required": ["reason"]
    }
  }
}
```

## Send the full history

The endpoint is stateless. Send every prior turn, including tool calls and tool results, on each request. If a reply was interrupted, store only what the caller heard. See [Handle barge-in](/docs/llm/cascaded-agent#handle-barge-in).

## phoneLLM mini settings

phoneLLM mini was trained on synthetic voice agent sessions, including Pipecat Flows. Pipecat recommends these settings:

* Set `temperature` to `0.0`.
* Leave `reasoning_effort` unset or set it to `none`. In the Voice Agent, the same setting is `agent.think.provider.reasoning_mode`.

The guidance above on spelling out steps, writing tool descriptions, and sending the full history applies to phoneLLM mini too.
