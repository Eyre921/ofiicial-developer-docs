---
title: "Using SDKs with Self-Hosted"
source: https://developers.deepgram.com/docs/using-sdks-with-self-hosted.md
path: docs/using-sdks-with-self-hosted
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Using SDKs with Self-Hosted

By default, Deepgram's SDKs hit the hosted endpoint `api.deepgram.com`. To use one of our SDKs with your self-hosted deployment, you will need to specify your own self-hosted endpoint instead.

## Determining your host URL

If running your requests locally on your server, your URL may be as simple as `http://localhost:8080` (pre-recorded) or `ws://localhost:8080` (streaming).

If running your requests on other servers, you may be using a static IP, such as `http://172.23.0.1:8080`.

If you use a multi-server or auto-scaled environment, you may configure a URL that is served by a load balancer that routes your requests across several instances.

Note that for a host that does not have TLS enabled, you will use `http` rather than `https`, and `ws` rather than `wss`.

## Python SDK

To configure the Python SDK for self-hosted deployments, create a custom `DeepgramClientEnvironment` with your self-hosted URLs and pass it to the `DeepgramClient`. This approach configures all endpoint types (REST APIs, WebSocket streaming, Agent, and Preview features).

Below is an example of how to make your first API request to your self-hosted deployment using the Python SDK. Substitute your own host address in place of `localhost` if needed.

Note that the `api_key` field cannot be a blank string as it is a required parameter for the Python SDK, but it does not need to be a valid Deepgram API key, as authorization with Deepgram for self-hosted deployments is configured through the container, not at the individual request level.

```python Python
# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

from deepgram import DeepgramClient
from deepgram.environment import DeepgramClientEnvironment

# Create a custom environment for your self-hosted deployment
self_hosted_env = DeepgramClientEnvironment(
    base="http://localhost:8080",           # HTTP endpoint for REST APIs
    production="ws://localhost:8080",       # WebSocket endpoint for streaming
    agent="ws://localhost:8080",            # WebSocket endpoint for agent
    preview="ws://localhost:8080"           # WebSocket endpoint for preview
)

# Initialize the client with your custom environment
deepgram = DeepgramClient(
    api_key="a",  # placeholder for self-hosted
    environment=self_hosted_env
)

response = deepgram.listen.v1.media.transcribe_url(
    url="https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav",
    model="nova-3",
    smart_format=True
)
print(response)

# Alternative: Use environment variables for URLs
import os

self_hosted_env = DeepgramClientEnvironment(
    base=os.getenv("DEEPGRAM_BASE_URL", "http://localhost:8080"),
    production=os.getenv("DEEPGRAM_WS_URL", "ws://localhost:8080"),
    agent=os.getenv("DEEPGRAM_AGENT_URL", "ws://localhost:8080"),
    preview=os.getenv("DEEPGRAM_PREVIEW_URL", "ws://localhost:8080")
)
```

## .NET SDK

The .NET SDK provides `DeepgramHttpClientOptions `(pre-recorded) and `DeepgramWsClientOptions` (streaming) classes, through which you can pass your host address. Below is a streaming example. Note that you should provide the `/v1` suffix to the base address.

```csharp C#
var apiKey = "<your API key>";
var options = new DeepgramWsClientOptions(){
  BaseAddress = "ws://localhost:8080/v1"
};
var liveClient = new LiveClient(apiKey, options);
```

If you encounter the following error message, note that you are receiving a 400 (bad request) when a 101 (successful stream) is expected.

```text Text
Error: "The server returned status code \u0027400\u0027 when status code \u0027101\u0027 was expected."
```

Ensure that your request parameters are specifying a model that you have available on your self-hosted instance. For example, when you intend to serve requests through a Nova-3 model, specify the following params:

```csharp C#
var liveSchema = new LiveSchema()
{
  Model = "nova-3",
  SmartFormat = true,
};
```

If that model is not present in your `models/` directory, the above error will occur.

## Go SDK

To modify the `Host` option in [type-client.go](https://github.com/deepgram/deepgram-go-sdk/blob/v1.3.6/pkg/client/interfaces/types-client.go):

```go Go
// ClientOptions defines any options for the client
type ClientOptions struct {
	...
	Host       string // override for the host endpoint
	...
	SelfHosted bool   // set to true if using self-hosted
  ...
}
```

You can create an object of type `ClientOptions` and then set the `Host` value.

```go Go
	// create a Deepgram client
	c := client.New("", interfaces.ClientOptions{
		Host: "http://localhost:8080",
    SelfHosted: true,
	})
```

## JavaScript SDK

To modify the URL, you can pass the `url` property within the global object to a new client.

```javascript JavaScript
const { DeepgramClient } = require("@deepgram/sdk");

const client = new DeepgramClient({
  apiKey: "DEEPGRAM_API_KEY",
  baseUrl: "http://localhost:8080", // Set the desired URL here
});
```

## Java SDK

Use `Environment.custom()` to point all API traffic (REST and WebSocket) to your self-hosted endpoint.

```java Java
import com.deepgram.DeepgramClient;
import com.deepgram.core.Environment;

Environment selfHostedEnv = Environment.custom()
    .base("http://localhost:8080")    // REST endpoint
    .agent("ws://localhost:8080")     // Agent WebSocket endpoint
    .production("ws://localhost:8080") // STT/TTS WebSocket endpoint
    .build();

// The api_key value is required by the SDK but is not validated
// by self-hosted deployments — use any non-empty string.
DeepgramClient client = DeepgramClient.builder()
    .apiKey("self-hosted")
    .environment(selfHostedEnv)
    .build();
```

***

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
