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
* **`max_tokens`**: Optional on Fireworks (required on Anthropic).
* **`anthropic-version` header**: Not required. Fireworks ignores this header.
* **`usage` field**: Included in both non-streaming and streaming responses. See [Token usage](#token-usage) for details.
* **`service_tier`**: Supported. Set `service_tier: "priority"` to opt into [Priority tier](/serverless/serving-paths).
* **`inference_geo`**: Deprecated in favor of [data residency](/accounts/data-residency). Remove it from request bodies and headers.

### Reasoning effort mapping

When you use the `thinking` parameter with `output_config.effort`, Anthropic effort values map to Fireworks [`reasoning_effort`](/api-reference/post-chatcompletions#body-reasoning-effort-one-of-0):

| Anthropic effort | Fireworks mapping |
| ---------------- | ----------------- |
| `low`            | `low`             |
| `medium`         | `medium`          |
| `high`           | `high`            |
| `max`            | `high`            |

<Note>
  The `adaptive` thinking type is not supported yet.
</Note>

For more details on reasoning, including interleaved thinking with tool use, see the [Reasoning guide](/guides/reasoning).

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

* **Server tools**: Server-side execution of tool families such as code execution, memory, web fetch, and web search is not supported. Tool search discovery and deferred tool loading are supported — see [Tool search and deferred tool loading](#tool-search-and-deferred-tool-loading).
* **Server-tool metadata**: Fields such as `caller` and `container` are not supported.
* **Tool schema fields**: `eager_input_streaming`, `cache_control`, `allowed_callers`, and `input_examples` are not supported.
* **`server_tool_use`**: Not included in usage tracking.
* **`speed`**: The `output_config.speed` option is not supported yet.

### Fireworks extensions

The following Fireworks-specific extension is available on the Anthropic-compatible endpoint:

* **`raw_output`**: A request parameter (boolean) that returns low-level details of what the model sees, including formatted prompts and function call data.

## Token usage

Token usage (`input_tokens` and `output_tokens`) is included in both non-streaming and streaming responses.

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
