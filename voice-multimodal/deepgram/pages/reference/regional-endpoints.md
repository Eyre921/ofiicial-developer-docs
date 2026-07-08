---
title: "Regional Endpoints"
source: https://developers.deepgram.com/reference/regional-endpoints.md
path: reference/regional-endpoints
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Regional Endpoints

Deepgram offers regional endpoints so you can process audio, text, and voice agent traffic within a specific geography. Regional endpoints use the same API keys and SDKs as the default global endpoint — you only need to change the base URL.

## EU Endpoint

For customers requiring data processing within the EU, Deepgram provides an EU-specific endpoint at `api.eu.deepgram.com`. While Deepgram guarantees the service will be hosted within the EU, the specific country location may change over time. If you require hosting in a specific EU country, consider [Deepgram Dedicated](https://deepgram.com/dedicated) (see also our [technical documentation](/reference/custom-endpoints#deepgram-dedicated-endpoints)).

**Endpoint URL**: `api.eu.deepgram.com`

### How to Configure

1. **Replace the base URL**: In any SDK or API request, replace `api.deepgram.com` with `api.eu.deepgram.com`.
2. **Use your existing credentials**: Your existing API keys and tokens work on the EU endpoint.

### Feature Compatibility

The EU endpoint supports the following Deepgram APIs:

* Speech-to-Text: `/v1/listen` and `/v2/listen` (excluding Whisper models)
* Text-to-Speech: `/v1/speak`
* Voice Agent: `/v1/agent/converse`
* Text Intelligence: `/v1/read`

See our [API Documentation](/reference/deepgram-api-overview) for more information.

### Known Limitations

* **Whisper models are not available in the EU region.** Use Flux or Nova STT models instead.

### WebSocket Connections

For streaming features on the EU endpoint, use the following URLs:

| API            | URL                                           |
| -------------- | --------------------------------------------- |
| Speech-to-Text | `wss://api.eu.deepgram.com/v1/listen`         |
| Text-to-Speech | `wss://api.eu.deepgram.com/v1/speak`          |
| Voice Agent    | `wss://api.eu.deepgram.com/v1/agent/converse` |

### SDK Configuration Examples

```python
from deepgram import DeepgramClient
from deepgram.environment import DeepgramClientEnvironment

eu_env = DeepgramClientEnvironment(
    base="https://api.eu.deepgram.com",        # REST APIs
    production="wss://api.eu.deepgram.com",     # STT/TTS WebSocket
    agent="wss://api.eu.deepgram.com",          # Agent WebSocket
    agent_rest="https://api.eu.deepgram.com",   # Agent REST
)
client = DeepgramClient(api_key="YOUR_API_KEY", environment=eu_env)
```

```javascript
import { DeepgramClient } from "@deepgram/sdk";

const deepgram = new DeepgramClient({
  apiKey: "YOUR_API_KEY",
  baseUrl: "https://api.eu.deepgram.com",
});
```

```csharp
using Deepgram;
using Deepgram.Models.Authenticate.v1;

var client = new AnalyzeClient("YOUR_API_KEY",
    new DeepgramHttpClientOptions("YOUR_API_KEY", "https://api.eu.deepgram.com"));
```

```go
import "github.com/deepgram/deepgram-go-sdk/pkg/client/interfaces"

client := client.New("YOUR_API_KEY", &interfaces.ClientOptions{
    Host: "api.eu.deepgram.com",
})
```

```java
import com.deepgram.DeepgramClient;
import com.deepgram.core.Environment;

Environment euEnv = Environment.custom()
    .base("https://api.eu.deepgram.com")
    .agent("wss://api.eu.deepgram.com")
    .production("wss://api.eu.deepgram.com")
    .build();
DeepgramClient client = DeepgramClient.builder()
    .apiKey("YOUR_API_KEY")
    .environment(euEnv)
    .build();
```

```bash
curl -X POST "https://api.eu.deepgram.com/v1/listen" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

## AU Endpoint

For customers requiring data processing within Australia, Deepgram provides an AU-specific endpoint at `api.au.deepgram.com`. Deepgram guarantees the service will be hosted within Australia.

**Endpoint URL**: `api.au.deepgram.com`

### How to Configure

1. **Replace the base URL**: In any SDK or API request, replace `api.deepgram.com` with `api.au.deepgram.com`.
2. **Use your existing credentials**: Your existing API keys and tokens work on the AU endpoint.

### Feature Compatibility

The AU endpoint supports the following Deepgram APIs:

* Speech-to-Text: `/v1/listen` and `/v2/listen` (excluding Whisper models)
* Text-to-Speech: `/v1/speak`
* Voice Agent: `/v1/agent/converse`
* Text Intelligence: `/v1/read`

See our [API Documentation](/reference/deepgram-api-overview) for more information.

### Known Limitations

* **Whisper models are not available in the AU region.** Use Flux or Nova STT models instead.

### WebSocket Connections

For streaming features on the AU endpoint, use the following URLs:

| API            | URL                                           |
| -------------- | --------------------------------------------- |
| Speech-to-Text | `wss://api.au.deepgram.com/v1/listen`         |
| Text-to-Speech | `wss://api.au.deepgram.com/v1/speak`          |
| Voice Agent    | `wss://api.au.deepgram.com/v1/agent/converse` |

### SDK Configuration Examples

```python
from deepgram import DeepgramClient
from deepgram.environment import DeepgramClientEnvironment

au_env = DeepgramClientEnvironment(
    base="https://api.au.deepgram.com",        # REST APIs
    production="wss://api.au.deepgram.com",     # STT/TTS WebSocket
    agent="wss://api.au.deepgram.com",          # Agent WebSocket
    agent_rest="https://api.au.deepgram.com",   # Agent REST
)
client = DeepgramClient(api_key="YOUR_API_KEY", environment=au_env)
```

```javascript
import { DeepgramClient } from "@deepgram/sdk";

const deepgram = new DeepgramClient({
  apiKey: "YOUR_API_KEY",
  baseUrl: "https://api.au.deepgram.com",
});
```

```csharp
using Deepgram;
using Deepgram.Models.Authenticate.v1;

var client = new AnalyzeClient("YOUR_API_KEY",
    new DeepgramHttpClientOptions("YOUR_API_KEY", "https://api.au.deepgram.com"));
```

```go
import "github.com/deepgram/deepgram-go-sdk/pkg/client/interfaces"

client := client.New("YOUR_API_KEY", &interfaces.ClientOptions{
    Host: "api.au.deepgram.com",
})
```

```java
import com.deepgram.DeepgramClient;
import com.deepgram.core.Environment;

Environment auEnv = Environment.custom()
    .base("https://api.au.deepgram.com")
    .agent("wss://api.au.deepgram.com")
    .production("wss://api.au.deepgram.com")
    .build();
DeepgramClient client = DeepgramClient.builder()
    .apiKey("YOUR_API_KEY")
    .environment(auEnv)
    .build();
```

```bash
curl -X POST "https://api.au.deepgram.com/v1/listen" \
  -H "Authorization: Token YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

## Voice Agent Managed LLM and TTS Providers

When you use Deepgram's [managed LLM](/docs/voice-agent-llm-models) or [managed TTS](/docs/voice-agent-tts-models) providers with the Voice Agent API, Deepgram routes requests to those providers on your behalf. Where possible, Deepgram leverages regional endpoints for these managed providers to keep traffic within the same region as your Deepgram endpoint.

### EU Regional Support

Today, Deepgram routes managed provider traffic through EU endpoints for **OpenAI**. When you connect to `api.eu.deepgram.com` and use a managed OpenAI LLM or TTS model, the underlying requests to OpenAI are routed through OpenAI's EU infrastructure.

Other managed providers do not yet offer EU-specific endpoints. As providers expand their regional availability, Deepgram will adopt those endpoints automatically — no configuration change required on your side.

### AU Regional Support

When you connect to `api.au.deepgram.com` and use Deepgram managed models for speech-to-text (`listen`) and text-to-speech (`speak`) — for example, `nova-3` and `aura-2` — Deepgram processes that audio within Australia.

The voice agent LLM (`think`) runs on a third-party provider, where data residency and processing location are distinct. OpenAI, for example, offers Australian data residency — your content is stored at rest in Australia — but performs inference outside Australia. No managed in-region LLM is available today, so the `think` step is processed outside Australia even when residency applies. See [OpenAI's data residency guide](https://developers.openai.com/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency) for provider specifics.

### How to Use

No additional configuration is needed. Connect to your regional endpoint and select a managed provider as you normally would:

```json
{
  "agent": {
    "listen": {
      "provider": {
        "type": "deepgram",
        "model": "nova-3"
      }
    },
    "think": {
      "provider": {
        "type": "open_ai",
        "model": "gpt-4o-mini"
      }
    },
    "speak": {
      "provider": {
        "type": "deepgram",
        "model": "aura-2-zeus-en"
      }
    }
  }
}
```

When this configuration is sent to `wss://api.eu.deepgram.com/v1/agent/converse`, Deepgram processes speech-to-text and text-to-speech within the EU, and routes the managed OpenAI LLM call through OpenAI's EU endpoint. When sent to `wss://api.au.deepgram.com/v1/agent/converse`, Deepgram processes speech-to-text and text-to-speech within Australia; as noted above, the managed LLM (`think`) call is processed outside Australia.
