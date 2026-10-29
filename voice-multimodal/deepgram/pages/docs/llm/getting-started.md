---
title: "Get started with Deepgram LLMs"
source: https://developers.deepgram.com/docs/llm/getting-started.md
path: docs/llm/getting-started
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get started with Deepgram LLMs

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

This guide sends a single request to Think-Fast and prints the reply.

## Before you begin

* A current Deepgram contract with a project enrolled in Early Access. If you don't have one, [talk to sales](https://deepgram.com/contact-us).
* A Deepgram API key from that project. To create one, see [Creating Additional API Keys](/docs/create-additional-api-keys).
* The key exported as an environment variable:

```bash
export DEEPGRAM_API_KEY="your-api-key"
```

> **Info**
>
> **No SDK support during Early Access.** The Deepgram SDKs do not include `/v1/think` yet; SDK support is planned for general availability. The examples below call the endpoint with plain HTTP clients: `requests` for Python and the built-in `fetch` for JavaScript.

## Send a request

Send a system message and a user message to `/v1/think`. Authenticate with the `Token` scheme.

**`Python`**

```python Python
import os

import requests

# Send the conversation to /v1/think, authenticating with your API key.
response = requests.post(
    "https://agent.deepgram.com/v1/think",
    headers={"Authorization": f"Token {os.environ['DEEPGRAM_API_KEY']}"},
    json={
        "model": "think-fast",
        # The full conversation: a system prompt and the caller's first message.
        "messages": [
            {
                "role": "system",
                "content": "You are a friendly voice agent. Reply in one or two short sentences.",
            },
            {"role": "user", "content": "Hi, can you check on my order?"},
        ],
    },
)
# Raise on a 4xx or 5xx, then print the assistant's reply.
response.raise_for_status()
print(response.json()["choices"][0]["message"]["content"])
```

**`JavaScript`**

```javascript JavaScript
// Send the conversation to /v1/think, authenticating with your API key.
const response = await fetch("https://agent.deepgram.com/v1/think", {
  method: "POST",
  headers: {
    Authorization: `Token ${process.env.DEEPGRAM_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "think-fast",
    // The full conversation: a system prompt and the caller's first message.
    messages: [
      {
        role: "system",
        content: "You are a friendly voice agent. Reply in one or two short sentences.",
      },
      { role: "user", content: "Hi, can you check on my order?" },
    ],
  }),
});

// Throw on a 4xx or 5xx, then print the assistant's reply.
if (!response.ok) throw new Error(`Request failed: ${response.status}`);
const data = await response.json();
console.log(data.choices[0].message.content);
```

**`cURL`**

```bash cURL
curl https://agent.deepgram.com/v1/think \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "think-fast",
    "messages": [
      {"role": "system", "content": "You are a friendly voice agent. Reply in one or two short sentences."},
      {"role": "user", "content": "Hi, can you check on my order?"}
    ]
  }'
```

## Read the response

The endpoint returns a `chat.completion` object. The reply is in `choices[0].message.content`, and token counts are in `usage`.

```json
{
  "id": "chatcmpl-…",
  "object": "chat.completion",
  "created": 1792786932,
  "model": "think-fast",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Sure! Could you please provide your order number…",
        "refusal": null
      },
      "finish_reason": "stop",
      "logprobs": null
    }
  ],
  "usage": {
    "prompt_tokens": 32,
    "completion_tokens": 19,
    "total_tokens": 51,
    "prompt_tokens_details": { "cached_tokens": 0 },
    "completion_tokens_details": { "reasoning_tokens": 0 }
  }
}
```

## Keep the conversation going

The endpoint is stateless. To continue the conversation, append the assistant's reply and the next user message to `messages`, then send the full list again.

## Next steps

* [Request and response format](/docs/llm/request-response-format): streaming, function calling, and every supported field.
* [Models overview](/docs/llm/models): choose between Think-Fast and phoneLLM mini.
* [Build a cascaded agent](/docs/llm/cascaded-agent): use Think-Fast in a voice pipeline.
