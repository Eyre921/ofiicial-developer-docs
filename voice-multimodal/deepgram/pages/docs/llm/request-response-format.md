---
title: "Request and response format"
source: https://developers.deepgram.com/docs/llm/request-response-format.md
path: docs/llm/request-response-format
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Request and response format

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

This page is the reference for `/v1/think` during Early Access. Both [models](/docs/llm/models) use the same format.

The request and response follow the OpenAI Chat Completions structure, so most Chat Completions client code carries over. The differences are called out in each section below.

## Endpoint and authentication

```
POST https://agent.deepgram.com/v1/think
```

Authenticate with your Deepgram API key using the `Token` scheme:

```
Authorization: Token <DEEPGRAM_API_KEY>
```

To authenticate from a browser or other untrusted client, use a short-lived token from [token-based authentication](/guides/fundamentals/token-based-authentication) with the `Bearer` scheme: `Authorization: Bearer <token>`.

Deepgram never forwards your credentials to the model service.

## Request body

Send JSON with `Content-Type: application/json`. The endpoint accepts the eight fields below and **rejects any other top-level field**.

| Field              | Type                                | Required                | Default       | Description                                                                                                                                                                                                                                                                                                       |
| ------------------ | ----------------------------------- | ----------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`            | string                              | Yes                     |               | A model available to your project, such as `think-fast` or `phonellm-mini-alpha-2-fp8`.                                                                                                                                                                                                                           |
| `messages`         | array of [messages](#messages)      | Yes                     |               | The full conversation history.                                                                                                                                                                                                                                                                                    |
| `temperature`      | number                              | No                      | Model default | Sampling temperature, from `0` to `2`.                                                                                                                                                                                                                                                                            |
| `reasoning_effort` | string                              | No                      | Model default | One of `none`, `minimal`, `low`, `medium`, `high`, in lowercase. See [Generation controls](#generation-controls).                                                                                                                                                                                                 |
| `tools`            | array of [tools](#function-calling) | No                      | `[]`          | Function tools the model can call.                                                                                                                                                                                                                                                                                |
| `stream`           | boolean                             | No                      | `false`       | Set to `true` to receive the response as [server-sent events](#streaming).                                                                                                                                                                                                                                        |
| `stream_options`   | object                              | When `stream` is `true` |               | Must be exactly `{"include_usage": true}`.                                                                                                                                                                                                                                                                        |
| `mip_opt_out`      | boolean                             | No                      | `false`       | Opts this request out of the Model Improvement Program. phoneLLM mini only: Think-Fast can only be used with the Model Improvement Program, so `true` is rejected with `400`. Requires the MIP opt-out add-on; without it, `true` is rejected with `403`. See [Data retention and MIP](/docs/llm/data-retention). |

### Unsupported fields

These Chat Completions fields are rejected as unknown fields: `max_tokens`, `max_completion_tokens`, `top_p`, `stop`, `n`, `seed`, `tool_choice`, `response_format`, `frequency_penalty`, `presence_penalty`, `logprobs`, and `user`. Remove them before sending a request.

## Messages

`messages` is an array of message objects. The endpoint identifies each message by its shape. Use the standard roles: `system`, `user`, `assistant`, and `tool`.

> **Warning**
>
> Think-Fast does not accept the `developer` role. A `developer` message returns `400` with the body `{"message":"Invalid request","type":"Bad Request","code":400}` and no `dg-error` header. Send those instructions as a `system` message instead. Some frameworks, including Pipecat, send `developer` messages by default. phoneLLM mini accepts the `developer` role.

`content` must be a plain string. The array-of-content-parts form is not supported.

**System, user, and assistant messages**

| Field     | Type   | Required |
| --------- | ------ | -------- |
| `role`    | string | Yes      |
| `content` | string | Yes      |

**Assistant message with tool calls**

| Field        | Type                | Required |
| ------------ | ------------------- | -------- |
| `role`       | `"assistant"`       | Yes      |
| `content`    | string or null      | No       |
| `tool_calls` | array of tool calls | Yes      |

Each tool call has this shape:

```json
{
  "id": "call_123",
  "type": "function",
  "function": { "name": "get_order_status", "arguments": "{\"order_id\": \"A1234\"}" }
}
```

`function.arguments` is a JSON-encoded string.

**Tool result message**

| Field          | Type     | Required |
| -------------- | -------- | -------- |
| `role`         | `"tool"` | Yes      |
| `content`      | string   | Yes      |
| `tool_call_id` | string   | Yes      |
| `name`         | string   | No       |

### Conversation history

The endpoint is stateless. Send the full conversation, including earlier tool calls and tool results, on every request.

## Generation controls

* **`temperature`** sets sampling randomness. Lower values give more consistent replies.
* **`reasoning_effort`** sets how much the model reasons before answering. Think-Fast doesn't reason by default: leave it unset or set it to `none`, because other values add reasoning tokens and latency.

## Streaming

Set `stream` to `true` and `stream_options` to `{"include_usage": true}`. The response has `Content-Type: text/event-stream`.

```json
{
  "model": "think-fast",
  "stream": true,
  "stream_options": { "include_usage": true },
  "messages": [{ "role": "user", "content": "Hi, can you check on my order?" }]
}
```

Each event's `data:` line holds a `chat.completion.chunk` object. The stream then ends in this order:

1. A chunk whose choice has `finish_reason` set, such as `"stop"`.
2. A final chunk with an empty `choices` array and a `usage` object.
3. `data: [DONE]`

If the model service's stream breaks off, the response ends **without** `[DONE]`. Treat a missing `[DONE]` as a failed request.

```
data: {"id":"chatcmpl-…","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"role":"assistant","content":"Sure"}}]}

data: {"id":"chatcmpl-…","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"! Could you"}}]}

data: {"id":"chatcmpl-…","object":"chat.completion.chunk","choices":[{"index":0,"delta":{},"finish_reason":"stop"}]}

data: {"id":"chatcmpl-…","object":"chat.completion.chunk","choices":[],"usage":{"prompt_tokens":32,"completion_tokens":19,"total_tokens":51}}

data: [DONE]
```

For a full streaming loop, see [Build a cascaded agent](/docs/llm/cascaded-agent).

## Function calling

Pass function tools in `tools`. `function` is the only supported tool type.

| Field                  | Type   | Required | Description                                                         |
| ---------------------- | ------ | -------- | ------------------------------------------------------------------- |
| `type`                 | string | Yes      | `"function"`                                                        |
| `function.name`        | string | Yes      | The function name.                                                  |
| `function.description` | string | Yes      | What the function does and when to call it. Required on every tool. |
| `function.parameters`  | object | Yes      | A JSON Schema for the arguments.                                    |

```json
{
  "model": "think-fast",
  "messages": [
    { "role": "system", "content": "You help customers check on their orders." },
    { "role": "user", "content": "Where is order A1234?" }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_order_status",
        "description": "Look up the shipping status of an order. Call this when the customer gives an order number.",
        "parameters": {
          "type": "object",
          "properties": {
            "order_id": { "type": "string", "description": "The order number, such as A1234." }
          },
          "required": ["order_id"]
        }
      }
    }
  ]
}
```

When the model calls a tool, the response message contains `tool_calls`. To continue:

1. Run the function in your application.
2. Append the assistant message with its `tool_calls` to `messages`.
3. Append a `tool` message with the result and the matching `tool_call_id`.
4. Send the request again with the same `tools`.

The assistant message can contain `content` as well as `tool_calls`, such as "Sure, checking on that order." Speak it, and keep it in the assistant message you append.

The endpoint forwards tool-call history intact, so the model can keep calling tools across turns.

## Response format

A successful response returns the model's status code and body unchanged.

When `stream` is `false`, the response is `200` with `Content-Type: application/json` and a `chat.completion` object:

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

### Usage

| Field                                              | Description                                                                                           |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `usage.prompt_tokens`                              | Tokens in the request messages and tools.                                                             |
| `usage.completion_tokens`                          | Tokens in the generated reply.                                                                        |
| `usage.total_tokens`                               | The sum of prompt and completion tokens.                                                              |
| `usage.prompt_tokens_details.cached_tokens`        | Prompt tokens served from cache.                                                                      |
| `usage.completion_tokens_details.reasoning_tokens` | Tokens spent on reasoning. Think-Fast only: phoneLLM mini responses omit `completion_tokens_details`. |

## Errors

Errors that Deepgram returns use the standard Deepgram error body, and the same message appears in the `dg-error` response header:

```json
{
  "err_code": "Bad Request",
  "err_msg": "Model not available.",
  "request_id": "0b2f6c1e-5a7d-4c3e-9f1a-2d8e4b6a7c90"
}
```

Errors from the model service are relayed unchanged, with their own status code and error body.

| Status | `err_code`                                                                     | When it happens                                                                                                                                                                                                                                                                                               | Fix                                                                                                                       |
| ------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `400`  | `Bad Request`                                                                  | The body is not valid JSON, includes a field outside the [eight supported fields](#request-body), is missing `model` or `messages`, sends `content` as an array, or has a tool without `function.description` or `function.parameters`. `err_msg` starts with `Invalid think request:` and names the problem. | Fix the field named in `err_msg`. See [Unsupported fields](#unsupported-fields).                                          |
| `400`  | `Bad Request`                                                                  | `model` is not a model available on this endpoint. `err_msg` is `Model not available.`                                                                                                                                                                                                                        | Use `think-fast` or `phonellm-mini-alpha-2-fp8`.                                                                          |
| `400`  | `Bad Request`                                                                  | `stream` is `true` but `stream_options.include_usage` is not `true`.                                                                                                                                                                                                                                          | Send `"stream_options": {"include_usage": true}`.                                                                         |
| `400`  | `Bad Request`                                                                  | A `think-fast` request sets `mip_opt_out: true`, or the project requires MIP opt-out. `err_msg` is `The think-fast LLM model does not yet support opting out of the Model Improvement Program (mip_opt_out).`                                                                                                 | Think-Fast can only be used with the Model Improvement Program. Remove `mip_opt_out`, or use `phonellm-mini-alpha-2-fp8`. |
| `400`  | none (body is `{"message":"Invalid request","type":"Bad Request","code":400}`) | A Think-Fast request includes a message with `role: "developer"`. No `dg-error` header is sent.                                                                                                                                                                                                               | Send those instructions as a `system` message.                                                                            |
| `401`  | `INVALID_AUTH`                                                                 | The API key is missing, invalid, or expired.                                                                                                                                                                                                                                                                  | Send `Authorization: Token <DEEPGRAM_API_KEY>` with a valid key.                                                          |
| `403`  | `INSUFFICIENT_PERMISSIONS`                                                     | The key or project is not authorized for this endpoint.                                                                                                                                                                                                                                                       | Confirm the project is enrolled in Early Access and the key has the needed scope.                                         |
| `403`  | `UNAUTHORIZED_FEATURES_REQUESTED`                                              | The request sets `mip_opt_out: true` and the project lacks the MIP opt-out add-on.                                                                                                                                                                                                                            | Remove `mip_opt_out` or add the add-on to the project.                                                                    |
| `429`  | `Too Many Requests`                                                            | The project is at its concurrency limit. `err_msg` is `Please try again later.`                                                                                                                                                                                                                               | Retry with backoff, or reduce concurrent requests.                                                                        |
| `500`  | `Internal Server Error` or `INTERNAL_SERVER_ERROR`                             | Deepgram could not reach the model service.                                                                                                                                                                                                                                                                   | Retry with backoff.                                                                                                       |
| `502`  | `Bad Gateway`                                                                  | Streaming requests only: the model service failed or closed the connection before the stream opened. `err_msg` is `Could not open a stream to the LLM provider.`                                                                                                                                              | Retry with backoff.                                                                                                       |
| `503`  | `Service Unavailable`                                                          | The model service or the concurrency service is unavailable.                                                                                                                                                                                                                                                  | Retry with backoff.                                                                                                       |

A stream that ends without `data: [DONE]` also means the request failed. The model service's stream broke off after the response started, so no error status is sent. Treat the response as incomplete and retry.
