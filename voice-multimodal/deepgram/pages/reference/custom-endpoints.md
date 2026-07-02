---
title: "Configuring Custom Endpoints"
source: https://developers.deepgram.com/reference/custom-endpoints.md
path: reference/custom-endpoints
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Configuring Custom Endpoints

This guide provides instructions for configuring your applications to use Deepgram's regional endpoints, Deepgram Dedicated endpoints, or self-hosted endpoints.

## Regional Endpoints

Deepgram offers regional endpoints for customers who need data processing within a specific geography. Regional endpoints use the same API keys and SDKs as the default global endpoint — you only need to change the base URL.

**EU Endpoint URL**: `api.eu.deepgram.com`

The EU endpoint supports Speech-to-Text, Text-to-Speech, Voice Agent, and Text Intelligence APIs. Replace `api.deepgram.com` with `api.eu.deepgram.com` in any SDK or API request to route traffic through the EU.

**AU Endpoint URL**: `api.au.deepgram.com`

The AU endpoint supports Speech-to-Text, Text-to-Speech, Voice Agent, and Text Intelligence APIs. Replace `api.deepgram.com` with `api.au.deepgram.com` in any SDK or API request to route traffic through Australia.

For full configuration details, SDK examples, WebSocket URLs, known limitations, and information about managed LLM/TTS provider regional routing, see [Regional Endpoints](/reference/regional-endpoints).

## Deepgram Dedicated Endpoints

[Deepgram Dedicated](https://deepgram.com/dedicated) allows you to run speech-to-text, text-to-speech, and voice agent workloads with performance, compliance, and regional control, without the complexity of managing infrastructure.

If you have a Deepgram Dedicated (DGD) endpoint, you'll receive endpoint details similar to:

**Endpoint URL**: `{SHORT_UID}.{REGION_SUBDOMAIN}.api.deepgram.com`

### How to Configure

1. **Replace the base URL**: In any SDK or API request, replace `api.deepgram.com` with your dedicated endpoint URL.
2. **Use your existing credentials**: You can use your existing API keys and tokens.

### Feature Compatibility

All Deepgram API features are available on self-hosted deployments. See our [API Documentation](/reference/deepgram-api-overview) for more information.

## Self-Hosted Endpoints

For self-hosted Deepgram deployments, you'll use your own custom domain and infrastructure.

**Common Endpoint Patterns**:

* HTTPS: `https://your-deepgram-instance.com`
* HTTP with alternate port 8080: `http://your-deepgram-instance.com:8080`
* Internal network: `http://10.0.1.100:8080`

### How to configure

For more information about self-hosted deployments, see our [Self-Hosted Documentation](/docs/self-hosted-introduction).

1. **Replace the base URL**: In any SDK or API request, replace `api.deepgram.com` with your self-hosted endpoint
2. **Use your distribution credentials**: Self-hosted deployments require specific credentials provided during setup.
3. **Configure protocol and port**: Specify HTTP/HTTPS and custom ports as needed for your deployment.

### Feature Compatibility

All Deepgram API features are available on self-hosted deployments. See our [API Documentation](/reference/deepgram-api-overview) for more information.

## WebSocket Connections

For streaming features, update WebSocket connection URLs accordingly:

### Speech-to-Text (`/v1/listen`)

* **Standard**: `wss://api.deepgram.com/v1/listen`
* **Dedicated**: `wss://{YOUR_DEDICATED_ENDPOINT}/v1/listen`
* **Self-hosted (HTTPS)**: `wss://your-deepgram-instance.com/v1/listen`
* **Self-hosted (HTTP with custom port)**: `ws://your-deepgram-instance.com:8080/v1/listen`

### Text-to-Speech (`/v1/speak`)

* **Standard**: `wss://api.deepgram.com/v1/speak`
* **Dedicated**: `wss://{YOUR_DEDICATED_ENDPOINT}/v1/speak`
* **Self-hosted (HTTPS)**: `wss://your-deepgram-instance.com/v1/speak`
* **Self-hosted (HTTP with custom port)**: `ws://your-deepgram-instance.com:8080/v1/speak`

### Voice Agent (`/v1/agent/converse`)

* **Standard**: `wss://api.deepgram.com/v1/agent/converse`
* **Dedicated**: `wss://{YOUR_DEDICATED_ENDPOINT}/v1/agent/converse`
* **Self-hosted (HTTPS)**: `wss://your-deepgram-instance.com/v1/agent/converse`
* **Self-hosted (HTTP with custom port)**: `ws://your-deepgram-instance.com:8080/v1/agent/converse`

## SDK Configuration Examples

### Python SDK

```python
# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

from deepgram import DeepgramClient
import httpx

# Standard endpoint
# client = DeepgramClient(api_key="YOUR_API_KEY")

# Dedicated endpoint
client = DeepgramClient(
    api_key="YOUR_API_KEY",
    httpx_client=httpx.Client(
        base_url="https://YOUR_DEDICATED_ENDPOINT"
    )
)

# Self-hosted endpoint (HTTPS)
client = DeepgramClient(
    api_key="YOUR_API_KEY",
    httpx_client=httpx.Client(
        base_url="https://your-deepgram-instance.com"
    )
)

# Self-hosted endpoint (HTTP with custom port)
client = DeepgramClient(
    api_key="YOUR_API_KEY",
    httpx_client=httpx.Client(
        base_url="http://your-deepgram-instance.com:8080"
    )
)
```

### JavaScript SDK

```javascript
import { DeepgramClient } from "@deepgram/sdk";

// Standard endpoint
// const deepgram = new DeepgramClient({ apiKey: "YOUR_API_KEY" });

// Dedicated endpoint
const deepgram = new DeepgramClient({
  apiKey: "YOUR_API_KEY",
  baseUrl: "https://{YOUR_DEDICATED_ENDPOINT}",
});

// Self-hosted endpoint (HTTPS)
const deepgram = new DeepgramClient({
  apiKey: "YOUR_API_KEY",
  baseUrl: "https://your-deepgram-instance.com",
});

// Self-hosted endpoint (HTTP with custom port)
const deepgram = new DeepgramClient({
  apiKey: "YOUR_API_KEY",
  baseUrl: "http://your-deepgram-instance.com:8080",
});
```

### .NET SDK

```csharp
using Deepgram;
using Deepgram.Models.Authenticate.v1;

// Standard endpoint (default)
// var client = new AnalyzeClient("YOUR_API_KEY");

// Dedicated endpoint
var client = new AnalyzeClient("YOUR_API_KEY",
    new DeepgramHttpClientOptions("YOUR_API_KEY", "https://{YOUR_DEDICATED_ENDPOINT}"));

// Self-hosted endpoint (HTTPS)
var client = new AnalyzeClient("YOUR_API_KEY",
    new DeepgramHttpClientOptions("YOUR_API_KEY", "https://your-deepgram-instance.com"));

// Self-hosted endpoint (HTTP with custom port)
var client = new AnalyzeClient("YOUR_API_KEY",
    new DeepgramHttpClientOptions("YOUR_API_KEY", "http://your-deepgram-instance.com:8080"));
```

### Go SDK

```go
import "github.com/deepgram/deepgram-go-sdk/pkg/client/interfaces"

// Standard endpoint
// client := client.NewWithDefaults()

// Dedicated endpoint
client := client.New("YOUR_API_KEY", &interfaces.ClientOptions{
    Host: "{YOUR_DEDICATED_ENDPOINT}",
})

// Self-hosted endpoint (HTTPS)
client := client.New("YOUR_API_KEY", &interfaces.ClientOptions{
    Host: "your-deepgram-instance.com",
})

// Self-hosted endpoint (HTTP with custom port)
client := client.New("YOUR_API_KEY", &interfaces.ClientOptions{
    Host: "http://your-deepgram-instance.com:8080",  // Protocol included in Host
    APIVersion: "v1",
})
```

### Java SDK

```java
import com.deepgram.DeepgramClient;
import com.deepgram.core.Environment;

// Standard endpoint (default)
// DeepgramClient client = DeepgramClient.builder().build();

// Dedicated or self-hosted endpoint
Environment customEnv = Environment.custom()
    .base("https://your-deepgram-instance.com")
    .agent("wss://your-deepgram-instance.com")
    .production("wss://your-deepgram-instance.com")
    .build();
DeepgramClient client = DeepgramClient.builder()
    .apiKey("YOUR_API_KEY")
    .environment(customEnv)
    .build();
```

## Direct API Calls

### cURL Examples

**Standard endpoint:**

```bash
curl -X POST "https://api.deepgram.com/v1/listen" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

**Dedicated endpoint:**

```bash
curl -X POST "https://{YOUR_DEDICATED_ENDPOINT}/v1/listen" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

**Self-hosted endpoint (HTTPS):**

```bash
curl -X POST "https://your-deepgram-instance.com/v1/listen" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

**Self-hosted endpoint (HTTP with custom port):**

```bash
curl -X POST "http://your-deepgram-instance.com:8080/v1/listen" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```
