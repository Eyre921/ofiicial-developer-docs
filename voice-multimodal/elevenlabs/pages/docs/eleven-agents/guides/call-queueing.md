---
title: "Call queueing"
source: https://elevenlabs.io/docs/eleven-agents/guides/call-queueing.md
path: docs/eleven-agents/guides/call-queueing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Call queueing

## Overview

When an agent or workspace reaches its concurrency limit, new calls are normally rejected immediately. With call queueing enabled, callers who arrive while the agent is at capacity are held on the line with hold audio and connected automatically, in the order they arrived, as soon as a slot frees up.

Call queueing is configured per agent and is turned off by default.

Call queueing applies once all available capacity is in use, including burst capacity when [burst pricing](/docs/eleven-agents/guides/burst-pricing) is enabled for the agent.

## How call queueing works

1. **Capacity check**: When a call arrives, ElevenAgents checks whether the agent and the workspace have a free concurrency slot. If they do, the call connects immediately.
2. **Queueing**: If no slot is available, the caller is held in the agent's queue and hears hold audio. No conversation starts and nothing is charged while the caller waits.
3. **Admission**: The moment a slot frees up, the caller at the front of the queue is connected and the conversation starts as usual.
4. **Timeout**: If no slot frees up within the **Max queue wait time**, the call is disconnected. Telephony calls are hung up normally. WebSocket clients receive a `queue_status` event with status `timed_out`, followed by a close with code 4300.

Callers are connected strictly in arrival order for a given agent. When several agents share a workspace's concurrency pool, callers who have waited longer are generally connected first.

### What the caller hears

* Phone callers on Twilio and SIP trunk numbers hear the hold audio over the call.
* Widget and browser SDK users hear the hold audio in the browser. The widget (version 0.17.0 or later) also shows a waiting message and disables text input while queued.
* Direct WebSocket API clients receive the hold audio as regular `audio` events, plus `queue_status` events to drive a waiting state in your own UI. See [Handling queue events](#handling-queue-events-in-a-custom-websocket-client).

### Billing and conversation duration

Time spent in the queue is **not billed**, does not count toward the agent's **Max conversation duration**, and is not included in the conversation's reported duration. The conversation details in the dashboard show how long the caller waited before being connected.

## Supported channels

| Channel                                       | Call queueing |
| --------------------------------------------- | ------------- |
| Twilio inbound calls                          | Supported     |
| SIP trunk inbound calls                       | Supported     |
| Widget and client SDKs (WebSocket and WebRTC) | Supported     |
| Direct WebSocket API                          | Supported     |
| Outbound calls and batch calls                | Not supported |
| Text-only agents                              | Not supported |
| Genesys, AudioCodes, Exotel, WhatsApp and SMS | Not supported |

The daily call limit is not queued. A call that exceeds the agent's daily limit is rejected
immediately, because that limit does not free up until the next day.

## Configuration

Call queueing is configured per agent in the **Limits** section of the agent's **Security** tab.

| Setting                 | Description                                                                                                                                                                                         | Default                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **Enable call queuing** | Hold callers in a queue when the agent is at its concurrency limit.                                                                                                                                 | Off                     |
| **Max queue wait time** | How long a caller can wait before the call is disconnected, in seconds. Between 1 and 1,800 seconds (30 minutes).                                                                                   | 180 seconds (3 minutes) |
| **Custom hold audio**   | An MP3 or WAV file played on a loop to queued callers. Up to 40 MB and 3 minutes long. When no file is uploaded, callers hear the default hold tone. Upload it in the dashboard or through the API. | Default hold tone       |

#### Update via the dashboard

#### Open the Limits settings

Open your agent in the dashboard, navigate to the **Security** tab, and scroll to **Limits**.

#### Enable call queueing

Toggle on **Enable call queuing** and set the **Max queue wait time**.

#### Upload hold audio (optional)

Under **Custom hold audio**, upload an MP3 or WAV file. You can preview the default hold tone and your uploaded clip before publishing.

#### Publish your changes

Click **Publish** to apply the new settings.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `platform_settings.queueing_config`:

```json
{
  "platform_settings": {
    "queueing_config": {
      "enabled": true,
      "wait_timeout_seconds": 300
    }
  }
}
```

#### Push your changes

```bash
elevenlabs agents push --agent "<agent-name>"
```

#### Update via the API

```python
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
import os

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    platform_settings={
        "queueing_config": {
            "enabled": True,
            "wait_timeout_seconds": 300,
        },
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  platformSettings: {
    queueingConfig: {
      enabled: true,
      waitTimeoutSeconds: 300,
    },
  },
});
```

### Managing hold audio through the API

Upload an MP3 or WAV file to set the agent's custom hold audio. Uploading a new file replaces the previous one. The API accepts the `audio/mpeg` and `audio/wav` content types, so the examples set the type explicitly.

```python
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
import os

load_dotenv()

elevenlabs = ElevenLabs(
api_key=os.getenv("ELEVENLABS_API_KEY"),
)

elevenlabs.conversational_ai.agents.hold_audio.create(
agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
hold_audio_file=("hold-music.mp3", open("hold-music.mp3", "rb"), "audio/mpeg"),
)

```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import fs from "node:fs";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const holdAudioFile = new File([fs.readFileSync("hold-music.mp3")], "hold-music.mp3", {
  type: "audio/mpeg",
});

await elevenlabs.conversationalAi.agents.holdAudio.create("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  holdAudioFile,
});
```

Remove the custom clip to return to the default hold tone:

```python
elevenlabs.conversational_ai.agents.hold_audio.delete(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
)
```

```typescript
await elevenlabs.conversationalAi.agents.holdAudio.delete("agent_7101k5zvyjhmfg983brhmhkd98n6");
```

The current clip is returned read-only as `platform_settings.queueing_config.hold_audio` on the agent. Sending `hold_audio` in an agent create or update request has no effect.

## Handling queue events in a custom WebSocket client

Clients connected through the [WebSocket API](/docs/eleven-agents/libraries/web-sockets) receive `queue_status` events while they are queued:

```json
{
  "type": "queue_status",
  "queue_status_event": {
    "status": "waiting"
  }
}
```

* `waiting` is sent once, immediately after `conversation_initiation_metadata` and before any hold audio.
* `admitted` is sent when the caller is connected. The conversation then proceeds as usual.
* `timed_out` is sent when the wait exceeds the max queue wait time. The server then closes the connection with code 4300.

Calls that connect immediately never receive `queue_status` events. The event is always sent to queued callers and does not need to be enabled in the agent's `client_events`.

Hold audio is delivered as regular `audio` events in roughly one-second chunks, provided the agent's client events include `audio`. Use `queue_status` to show a waiting state rather than treating the hold audio as agent speech.

The `@elevenlabs/client` and `@elevenlabs/react` SDKs do not expose a dedicated callback for this
event yet. Use the `onIncomingEvent` callback to observe raw server events, including
`queue_status`.

## FAQ

#### Does a queued call count toward my concurrency limit?

No. A queued caller does not occupy a concurrency slot until they are connected to the agent.

#### Can callers hear their position in the queue or an estimated wait time?

Not currently. Queued callers hear the hold audio only. Queue position and wait-time estimates
are not announced.

#### What happens if the caller hangs up while waiting?

The caller leaves the queue immediately and everyone behind them moves up one place. No
conversation minutes are charged.

#### Does call queueing work with outbound calls?

No. Outbound and batch calls are only placed when capacity is available, so they are never
queued.
