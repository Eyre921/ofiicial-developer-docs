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

Anthropic compatibility is supported for serverless and on-demand deployments. Requests must go through `api.fireworks.ai/inference` (direct route endpoints are not supported for this surface).

### Differences from Anthropic

The following parameters and fields are handled differently or are not supported:

* **`model`**: Must be a Fireworks model identifier (for example, `accounts/fireworks/models/deepseek-v3p2`) instead of an Anthropic model name. See the [Fireworks Model Library](https://app.fireworks.ai/models) for available models.
* **`max_tokens`**: Optional on Fireworks (required on Anthropic).
* **`anthropic-version` header**: Not required. Fireworks ignores this header.
* **`usage` field**: Included in both non-streaming and streaming responses. See [Token usage](#token-usage) for details.
* **`service_tier`**: Supported. Set `service_tier: "priority"` to opt into [Priority tier](/serverless/serving-paths).
* **`inference_geo`**: Not supported.

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

### Unsupported features

The following Anthropic features are not available on Fireworks:

* **Server tools**: Server-side tool families (for example, code execution, memory, web fetch, tool search, and web search) are not supported.
* **Server-tool metadata**: Fields such as `caller` and `container` are not supported.
* **Tool schema fields**: `eager_input_streaming`, `cache_control`, `allowed_callers`, `defer_loading`, and `input_examples` are not supported.
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
