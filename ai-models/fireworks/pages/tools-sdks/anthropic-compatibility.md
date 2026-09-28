---
title: "Anthropic compatibility"
source: https://docs.fireworks.ai/tools-sdks/anthropic-compatibility
path: tools-sdks/anthropic-compatibility
---

Use Anthropic SDKs with Fireworks, and understand the supported surface for the Anthropic-compatible Messages API.

You can use the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) or [Anthropic TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript) to interact with Fireworks, making it easy to migrate applications that already use Anthropic's Messages API.

Fireworks exposes an Anthropic-compatible endpoint at `POST /v1/messages`.

## Quickstart

Install the Anthropic SDK for your language:

<Tabs>
  <Tab title="Python">
    ```bash theme={null}
    pip install anthropic
    ```
  </Tab>

  <Tab title="JavaScript / TypeScript">
    ```bash theme={null}
    npm install @anthropic-ai/sdk
    ```
  </Tab>
</Tabs>

Then make your first request:

<CodeGroup>
  ```python Python theme={null}
  import os
  import anthropic

  client = anthropic.Anthropic(
      api_key=os.environ["FIREWORKS_API_KEY"],
      base_url="https://api.fireworks.ai/inference",
  )

  response = client.messages.create(
      model="accounts/fireworks/models/kimi-k2p5",
      max_tokens=256,
      messages=[
          {"role": "user", "content": "Say hello in Spanish. Reply in one word."}
      ],
  )

  print(response.content[0].text)
  ```

  ```javascript JavaScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic({
    apiKey: process.env.FIREWORKS_API_KEY,
    baseURL: "https://api.fireworks.ai/inference",
  });

  const response = await client.messages.create({
    model: "accounts/fireworks/models/kimi-k2p5",
    max_tokens: 256,
    messages: [
      { role: "user", content: "Say hello in Spanish. Reply in one word." },
    ],
  });

  console.log(response.content[0].text);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.fireworks.ai/inference/v1/messages \
    --header "Authorization: Bearer $FIREWORKS_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "accounts/fireworks/models/kimi-k2p5",
      "max_tokens": 256,
      "messages": [
        {
          "role": "user",
          "content": "Say hello in Spanish. Reply in one word."
        }
      ]
    }'
  ```
</CodeGroup>

<Note>
  The base URL for the Anthropic SDK is `https://api.fireworks.ai/inference` (without the `/v1` suffix). The SDK appends `/v1/messages` automatically.
</Note>

## Usage

Use the Anthropic SDK as you normally would. Set `model` to a Fireworks model resource name, such as `accounts/fireworks/models/kimi-k2p5`.

The [Serverless Quickstart](/getting-started/quickstart) includes Anthropic SDK examples for common use cases:

* [Messages](/getting-started/quickstart)
* [Streaming](/getting-started/quickstart#streaming-responses)
* [Function calling](/getting-started/quickstart#function-calling)
* [Structured outputs](/getting-started/quickstart#structured-outputs-json-mode)
* [Reasoning](/getting-started/quickstart#reasoning)
* [Vision](/getting-started/quickstart#vision-models)

## API compatibility

### Supported endpoint

Fireworks supports the Anthropic [`/v1/messages`](/api-reference/anthropic-messages) endpoint, including non-streaming and streaming (SSE) responses.

### Deployment support

Anthropic compatibility is supported for serverless and on-demand deployments. Requests must go through `api.fireworks.ai/inference` or [US-only Serverless](/serverless/us-only-serverless) at `us.api.fireworks.ai/inference` (direct route endpoints are not supported for this surface).

### Differences from Anthropic

The following parameters and fields are handled differently or are not supported:

* **`model`**: Must be a Fireworks model identifier (for example, `accounts/fireworks/models/deepseek-v3p2`) instead of an Anthropic model name. See the [Fireworks Model Library](https://app.fireworks.ai/models) for available models.
* **`max_tokens`**: Required and must be greater than `0`, the same as on Anthropic. Omitting it returns `400 invalid_request_error`.
* **`anthropic-version` header**: Not required. Fireworks ignores this header.
* **`usage` field**: Included in both non-streaming and streaming responses. See [Token usage](#token-usage) for details.
* **`service_tier`**: Supported. Set `service_tier: "priority"` to opt into [Priority tier](/serverless/serverless-modes).
* **`inference_geo`**: Deprecated in favor of [data residency](/accounts/data-residency). Remove it from request bodies and headers.

### Reasoning

There are two ways to control reasoning, and both resolve to Fireworks [`reasoning_effort`](/api-reference/post-chatcompletions#body-reasoning-effort-one-of-0).

**`output_config.effort`** maps directly:

| Anthropic effort | Fireworks `reasoning_effort` |
| - | - |
| `low` | `low` |
| `medium` | `medium` |
| `high` | `high` |
| `max` | `max` |
| `xhigh` | `max` |

**`thinking.budget_tokens`** is converted to an effort band, because Fireworks models take an effort level rather than a token budget:

| `budget_tokens` | Fireworks `reasoning_effort` |
| - | - |
| `>= 10000` | `high` |
| `5000`–`9999` | `medium` |
| `1024`–`4999` | `low` |

When both are present, `output_config.effort` wins. Setting `thinking.type: "disabled"` sends `reasoning_effort: "none"`.

These constraints are enforced and return `400 invalid_request_error`:

* `thinking.budget_tokens` is required when `thinking.type` is `enabled`, and must be at least `1024`.
* `max_tokens` must be greater than `thinking.budget_tokens`.
* Enabled thinking cannot be combined with a forced `tool_choice` of `any` or `tool`.
* You cannot pre-fill an assistant turn while thinking is enabled or adaptive.

Set `thinking.display: "omitted"` to run reasoning without returning `thinking` blocks. `thinking.type: "adaptive"` is accepted, but it does not by itself select an effort level — pair it with `output_config.effort`.

For more details on reasoning, including interleaved thinking with tool use, see the [Reasoning guide](/guides/reasoning).

### Thinking history and context management

Long agentic conversations accumulate `thinking` blocks that inflate the prompt. Use `context_management` to control how much of that reasoning history is replayed:

```json theme={null}
{
  "context_management": {
    "edits": [{ "type": "clear_thinking_20251015", "keep": "all" }]
  }
}
```

| `keep` | Behavior |
| - | - |
| `"all"` | Replay the full reasoning history |
| `"none"` | Drop reasoning history entirely |
| `"interleaved"` | Keep reasoning interleaved with the turns it belongs to |
| `{"type": "thinking_turns", "value": N}` | Keep reasoning for the last `N` thinking turns |

When an edit is applied, streaming responses report it on the final `message_delta` event as `context_management.applied_edits`.

### Structured output

Request JSON that conforms to a schema with `output_config.format` (or the top-level `output_format`):

```json theme={null}
{
  "output_config": {
    "format": {
      "type": "json_schema",
      "schema": {
        "type": "object",
        "properties": { "city": { "type": "string" } },
        "required": ["city"]
      }
    }
  }
}
```

Schema adherence is strict. See [Structured outputs](/structured-responses/structured-output-grammar-based) for guidance on writing schemas.

### Images and documents

Image blocks are supported with both `source.type: "base64"` and `source.type: "url"`:

```json theme={null}
{
  "type": "image",
  "source": { "type": "base64", "media_type": "image/png", "data": "<BASE64>" }
}
```

Two content shapes are rejected by the backend, and the error names the Anthropic field so it is clear what to change:

* `document` blocks (PDF and text documents).
* `image` blocks using `source.type: "file"`.

Use a vision-capable model — see [Querying vision-language models](/guides/querying-vision-language-models).

### Tool search and deferred tool loading

Tool definition schemas usually live at the top of a model's chat template, ahead of the conversation. Carrying every schema on every turn bloats that prefix and destabilizes the prompt cache for clients with large tool sets. Fireworks supports the [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) pattern for on-demand tool discovery—used by [Claude Code's MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) and the [Agent SDK's tool search](https://code.claude.com/docs/en/agent-sdk/tool-search)—to lazy-load schemas instead.

* **`defer_loading`**: Tools marked `defer_loading: true` are omitted from the request's tool definitions when a tool-search tool is present. Rather than placing every schema at the top of the template up front, the deferred schemas are loaded lazily through tool results once the model identifies which tools it needs.
* **`tool_reference` expansion**: When a tool result returns `tool_reference` blocks (the payload a tool-search call emits), each reference is expanded inline into the referenced tool's schema within the tool-result message. That makes the newly loaded schema visible to the model through the conversation, so it can produce tool calls in line with that schema—without the client re-sending the full `tools` array and shifting the prefix.

This covers both Anthropic-native `tool_search_tool_*` tool names and clients that name their discovery tool `ToolSearch` (for example, Claude Code).

<Note>
  Fireworks translates the **client-side** tool-search discovery and deferred-loading wire format only. Anthropic's **server-side** tool search and server-side tool use—where the provider executes the search and tool calls on its side—are not supported. Server-side execution of the other server tool families (web search, code execution, memory, web fetch) is likewise not supported; see [Unsupported features](#unsupported-features).
</Note>

<Note>
  An explicitly forced `tool_choice` naming a deferred tool overrides the drop: the forced tool stays callable in the request's tool definitions so the forced choice validates.
</Note>

### Unsupported features

The following Anthropic features are not available on Fireworks:

* **Other `/v1/messages` routes**: Only `POST /v1/messages` is served. `POST /v1/messages/count_tokens` returns `404`, and `/v1/messages/batches` is not available — use the Fireworks [Batch API](/guides/batch-inference) instead.
* **Server tools**: Server-side execution of tool families such as code execution, memory, web fetch, and web search is not supported. Declaring Anthropic's server-side `web_search_20250305` tool returns a `400` telling you to declare `web_search` as a client-side tool with an `input_schema` and execute it yourself. Tool search discovery and deferred tool loading are supported — see [Tool search and deferred tool loading](#tool-search-and-deferred-tool-loading).
* **Server-tool metadata**: Fields such as `caller` and `container` are not supported.
* **Tool schema fields**: `eager_input_streaming`, `cache_control`, `allowed_callers`, and `input_examples` are not supported.
* **`server_tool_use`**: Not included in usage tracking.
* **`speed`**: The `output_config.speed` option is not supported yet.

### Fireworks extensions

The following Fireworks-specific extension is available on the Anthropic-compatible endpoint:

* **`raw_output`**: A request parameter (boolean) that returns low-level details of what the model sees, including formatted prompts and function call data.

## Errors

Errors use the Anthropic error envelope, so the `APIError` subclasses in the Anthropic SDKs behave as they do against Anthropic:

```json theme={null}
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "max_tokens is required and must be > 0"
  }
}
```

`error.type` is one of `invalid_request_error`, `authentication_error`, `billing_error`, `permission_error`, `not_found_error`, `request_too_large`, `rate_limit_error`, `overloaded_error`, or `api_error`. Status codes follow Anthropic's conventions rather than the underlying Fireworks ones — a `422` is reported as `400`, a billing failure as `402`, and an oversized request as `413`.

Error messages refer to the Anthropic field you sent, not its Fireworks equivalent. If you send `stop_sequences`, a validation error names `stop_sequences` even though the field is called `stop` on the Fireworks chat completions API.

<Note>
  A few failures are raised before the request reaches the Anthropic-compatible layer — an unknown model or an unrouted path, for example. Those return the standard Fireworks error body (`{"error": {"code": "NOT_FOUND", ...}, "request_id": "..."}`) instead of the Anthropic envelope. Treat the HTTP status as authoritative and do not assume every error body has an `error.type`.
</Note>

For the shared status-code catalog, see [Inference error codes](/guides/inference-error-codes).

## Use with Claude Code

Point Claude Code at Fireworks by setting the base URL and using your Fireworks API key as the auth token:

```bash theme={null}
export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"
export ANTHROPIC_AUTH_TOKEN="$FIREWORKS_API_KEY"
export ANTHROPIC_MODEL="accounts/fireworks/models/kimi-k2p5"

claude
```

Use `ANTHROPIC_AUTH_TOKEN` (sent as a `Bearer` credential) rather than `ANTHROPIC_API_KEY`. Claude Code's login gate only recognizes OAuth, `ANTHROPIC_AUTH_TOKEN`, or an already-approved `ANTHROPIC_API_KEY`, so a Fireworks key placed in `ANTHROPIC_API_KEY` can leave the client reporting "Not logged in".

The same settings work for the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python), which reads `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` from the environment.

### Troubleshooting

| Symptom | Cause and fix |
| - | - |
| `404` with "Model not found, inaccessible, and/or not deployed" | `ANTHROPIC_MODEL` is not a Fireworks model resource name, or the model is not deployed to your account. Use the full `accounts/<account>/models/<model>` form. |
| `404` "Path not found" | The base URL includes `/v1`. Set `ANTHROPIC_BASE_URL` to `https://api.fireworks.ai/inference`; the client appends `/v1/messages`. |
| "Not logged in" | The key is in `ANTHROPIC_API_KEY`. Move it to `ANTHROPIC_AUTH_TOKEN`. |
| `400` "max\_tokens is required and must be > 0" | A client or proxy dropped `max_tokens`. It is required on every request. |
| `400` naming `web_search_20250305` | Claude Code's WebSearch tool requested server-side execution in a region where it is unavailable. Disable WebSearch, or supply your own client-side `web_search` tool. |
| Slow multi-turn responses | Prompt-cache misses. Claude Code sends a session header that Fireworks uses to route follow-up turns to the same replica; avoid stripping `X-Claude-Code-Session-Id` in an intermediate proxy. |

<Note>
  Claude Code's built-in WebSearch tool is served by Fireworks only in regions where the search backend is enabled, and only for the single-turn search shape Claude Code emits. It is not a general-purpose server-side web search tool.
</Note>

## Token usage

Token usage (`input_tokens` and `output_tokens`) is included in both non-streaming and streaming responses.

Following Anthropic's accounting, `input_tokens` **excludes** tokens served from the prompt cache; those are reported separately as `cache_read_input_tokens`. Total prompt tokens are therefore `input_tokens + cache_read_input_tokens`. This differs from the Fireworks chat completions API, where `prompt_tokens` includes cached tokens. `cache_creation_input_tokens` is always `0`.

### Non-streaming

For non-streaming requests, usage is returned on the response object:

<CodeGroup>
  ```python Python theme={null}
  response = client.messages.create(
      model="accounts/fireworks/models/kimi-k2p5",
      max_tokens=256,
      messages=[{"role": "user", "content": "Say hello"}],
  )

  print(f"Input tokens:  {response.usage.input_tokens}")
  print(f"Output tokens: {response.usage.output_tokens}")
  ```

  ```javascript JavaScript theme={null}
  const response = await client.messages.create({
    model: "accounts/fireworks/models/kimi-k2p5",
    max_tokens: 256,
    messages: [{ role: "user", content: "Say hello" }],
  });

  console.log(`Input tokens:  ${response.usage.input_tokens}`);
  console.log(`Output tokens: ${response.usage.output_tokens}`);
  ```
</CodeGroup>

### Streaming

For streaming requests, token usage is included in the final `message_delta` event:

<CodeGroup>
  ```python Python theme={null}
  stream = client.messages.create(
      model="accounts/fireworks/models/kimi-k2p5",
      max_tokens=256,
      messages=[{"role": "user", "content": "Say hello"}],
      stream=True,
  )

  for event in stream:
      if event.type == "message_delta":
          print(f"Input tokens:  {event.usage.input_tokens}")
          print(f"Output tokens: {event.usage.output_tokens}")
  ```

  ```javascript JavaScript theme={null}
  const stream = client.messages.stream({
    model: "accounts/fireworks/models/kimi-k2p5",
    max_tokens: 256,
    messages: [{ role: "user", content: "Say hello" }],
  });

  for await (const event of stream) {
    if (event.type === "message_delta") {
      console.log(`Input tokens:  ${event.usage.input_tokens}`);
      console.log(`Output tokens: ${event.usage.output_tokens}`);
    }
  }
  ```
</CodeGroup>

<Note>
  There is only one `message_delta` event per stream (the last event before `message_stop`), and it always contains the actual token counts. The `message_start` event also includes a `usage` field, but its values are always `0` and should be ignored for metering purposes.
</Note>

## Next steps

<CardGroup>
  <Card title="Quickstart" href="/getting-started/quickstart" icon="rocket">
    Get started with your first API call
  </Card>

  <Card title="Reasoning" href="/guides/reasoning" icon="brain">
    Use reasoning with thinking models
  </Card>

  <Card title="API reference" href="/api-reference/anthropic-messages" icon="brackets-curly">
    Full Anthropic Messages API reference
  </Card>
</CardGroup>
