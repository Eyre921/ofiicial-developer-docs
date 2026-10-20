---
title: "OpenAI Realtime API compatibility"
source: https://elevenlabs.io/docs/eleven-agents/guides/openai-realtime-compatibility.md
path: docs/eleven-agents/guides/openai-realtime-compatibility
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# OpenAI Realtime API compatibility

ElevenLabs Realtime speaks the same wire protocol as OpenAI's Realtime API: the same client and server events, over the same WebSocket transport. If you already have an app built with OpenAI's Realtime SDK, you can point it at ElevenLabs Realtime instead of `api.openai.com` without switching SDKs.

> **Info**
>
> This guide covers the browser-based flow, where a small server-side step mints a short-lived
> credential and the browser connects directly to ElevenLabs Realtime.

## Available models

| Name                    | Optimized for             |
| ----------------------- | ------------------------- |
| Eleven Realtime v1 mini | Price and speed           |
| Eleven Realtime v1 max  | Quality and complex tasks |

## How it works

1. Your backend requests a short-lived client secret from ElevenLabs, scoped to a specific session configuration.
2. Your frontend passes that client secret to OpenAI's Realtime SDK in place of an OpenAI API key.
3. The SDK connects over WebSocket to ElevenLabs Realtime, and the conversation proceeds using the same client and server events as OpenAI's Realtime API.

## Mint a client secret

Request the client secret from your backend, not the browser, so your ElevenLabs API key never reaches the client.

[Create an API key in the dashboard here](https://elevenlabs.io/app/api/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

Store the key as a managed secret and pass it to the SDKs either as an environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

**`.env`**

```js title=".env"
ELEVENLABS_API_KEY=<your_api_key_here>
```

```python
import os

from dotenv import load_dotenv
from elevenlabs import (
    CreateClientSecretRequest,
    ExpiresAfter,
    OpenAiAudioConfigInput,
    OpenAiAudioInputConfigInput,
    OpenAiAudioInputFormat,
    OpenAiAudioOutputConfigInput,
    OpenAiAudioOutputFormat,
    OpenAiSessionConfigInput,
    OpenAiTurnDetection,
)
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

client_secret = elevenlabs.conversational_ai.realtime.create_client_secret(
    request=CreateClientSecretRequest(
        session=OpenAiSessionConfigInput(
            type="realtime",
            model="eleven_realtime_v1_mini",
            instructions="You are a helpful, friendly voice assistant. Keep replies concise.",
            output_modalities=["audio"],
            audio=OpenAiAudioConfigInput(
                input=OpenAiAudioInputConfigInput(
                    format=OpenAiAudioInputFormat(type="audio/pcm", rate=24000),
                    turn_detection=OpenAiTurnDetection(type="semantic_vad", eagerness="medium"),
                ),
                output=OpenAiAudioOutputConfigInput(
                    format=OpenAiAudioOutputFormat(type="audio/pcm"),
                    voice="brian",
                ),
            ),
        ),
        expires_after=ExpiresAfter(anchor="created_at", seconds=600),
    ),
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

process.loadEnvFile();

const elevenlabs = new ElevenLabsClient();

const clientSecret = await elevenlabs.conversationalAi.realtime.createClientSecret({
  session: {
    type: "realtime",
    model: "eleven_realtime_v1_mini",
    instructions: "You are a helpful, friendly voice assistant. Keep replies concise.",
    outputModalities: ["audio"],
    audio: {
      input: {
        format: { type: "audio/pcm", rate: 24000 },
        turnDetection: { type: "semantic_vad", eagerness: "medium" },
      },
      output: {
        format: { type: "audio/pcm" },
        voice: "brian",
      },
    },
  },
  expiresAfter: { anchor: "created_at", seconds: 600 },
});
```

The response contains `value` (the ephemeral credential your frontend will use), its expiry time, and the negotiated `session`. Return only `value` to the browser.

> **Note**
>
> A `model` string selects the agent's behavior directly, rather than referencing an `agent_id` from
> the dashboard. The session configuration you send when minting the client secret is the
> authoritative initial session for that credential.

## Connect from the browser

Pass the client secret to OpenAI's Realtime SDK (`@openai/agents-realtime`) as the API key, and point the WebSocket transport at the ElevenLabs endpoint instead of the default OpenAI one.

```typescript
import { OpenAIRealtimeWebSocket, RealtimeAgent, RealtimeSession } from "@openai/agents-realtime";

const { value: clientSecret } = await fetch("/api/token").then((res) => res.json());

const agent = new RealtimeAgent({
  name: "ElevenLabs agent",
  instructions: "You are a helpful, friendly voice assistant. Keep replies concise.",
});

const transport = new OpenAIRealtimeWebSocket({
  url: "wss://api.elevenlabs.io/v1/convai/realtime",
});

const session = new RealtimeSession(agent, {
  transport,
  model: "eleven_realtime_v1_mini",
  config: {
    outputModalities: ["audio"],
    audio: { output: { voice: "brian" } },
  },
});

await session.connect({ apiKey: clientSecret });
```

The SDK only wires audio automatically for its WebRTC transport. Over WebSocket, capture and play PCM16 audio at 24kHz yourself, for example with [`wavtools`](https://www.npmjs.com/package/wavtools), the same helper OpenAI uses in its own WebSocket examples.

> **Note**
>
> For a complete app that mints the client secret and wires up audio, see the [Next.js example on GitHub](https://github.com/elevenlabs/examples/tree/main/agents/nextjs/openai-realtime).

## Limitations

This guide covers connecting directly from a browser. Documentation for connecting from server-side OpenAI Realtime SDKs isn't published yet.

## FAQ

#### When should I use Realtime models?

Realtime models are the fastest way to start building voice into a product. Eleven Realtime v1
mini is optimized for price and speed; Eleven Realtime v1 max is optimized for quality and more
complex tasks.

#### What is the architecture underlying Realtime models?

Eleven Realtime v1 mini and max use a cascaded architecture, optimized end-to-end so each
component works best as part of a single system.

#### How do they compare to selecting the component models in ElevenAgents?

The specifics of the underlying models aren't public. Each component uses ElevenLabs' latest
research and is optimized to work best together within Realtime models.

#### Are Realtime models fused models?

No. Realtime models use a cascaded architecture: each component is a distinct model, built with
ElevenLabs' latest research and optimized to work best together.
