---
title: "Audio environment"
source: https://elevenlabs.io/docs/eleven-agents/customization/voice/audio-environment.md
path: docs/eleven-agents/customization/voice/audio-environment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio environment

## Overview

Audio environment controls how the agent's outbound audio sounds to the caller. Two settings apply:

* **Background sound** plays a looping ambient sound under agent speech.
* **Voice filter** applies a phone-style filter to the agent's voice before that mix.

The caller hears the result. The agent does not hear the background sound, and it is not sent into speech recognition.

This is separate from [tool call sounds](/docs/eleven-agents/customization/tools/tool-configuration/tool-call-sounds), which play only while a tool runs.

## Background sound

Background sound mixes a built-in preset under agent speech for the duration of the conversation. The sound keeps looping when the user interrupts; it does not stop with the agent's turn.

Presets include office, restaurant, city, typing, and elevator music. In the dashboard, you can preview a preset before you save.

Configure background sound with `conversation_config.conversation.background_sound`.

### Configuration

#### Update via the dashboard

#### Open Audio environment

Open your agent. On the Agent page, next to **Voices**, click the **Audio environment**
button.

#### Enable background sound

Turn on **Enable background sound**. Choose a preset from **Background sound**. Use the play
control next to the dropdown to preview it.

#### Set volume and looping

Set **Volume**. Keep **Crossfade loop** enabled to avoid an audible click when the sound
repeats. Save your changes.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `conversation_config.conversation.background_sound`. Valid `source_id` values are
`office1`, `office2`, `restaurant`, `city`, `typing`, and `elevator1` through `elevator4`.

```json
{
  "conversation_config": {
    "conversation": {
      "background_sound": {
        "source_type": "preset",
        "source_id": "office2",
        "volume": 0.15,
        "crossfade_loop": true
      }
    }
  }
}
```

To disable background sound, set `source_type` and `source_id` to `null`. Do not omit
`background_sound` or set the object to `null`; an update keeps the existing setting.

#### Push the agent configuration

```bash
elevenlabs agents push --agent agent_7101k5zvyjhmfg983brhmhkd98n6
```

#### Update via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "conversation": {
            "background_sound": {
                "source_type": "preset",
                "source_id": "office2",
                "volume": 0.15,
                "crossfade_loop": True,
            }
        }
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    conversation: {
      backgroundSound: {
        sourceType: "preset",
        sourceId: "office2",
        volume: 0.15,
        crossfadeLoop: true,
      },
    },
  },
});
```

To disable, set `source_type` and `source_id` to `null`. Omitting `background_sound` on an
update does not disable it.

On very poor WebSocket connections, mixing background sound can produce choppy audio.

### Parameters

Valid `source_id` values are `office1`, `office2`, `restaurant`, `city`, `typing`, and `elevator1` through `elevator4`.

| Field            | Type    | Default | Description                                                                 |
| ---------------- | ------- | ------- | --------------------------------------------------------------------------- |
| `source_type`    | string  | unset   | Must be `preset` when a sound is enabled. Set together with `source_id`.    |
| `source_id`      | string  | unset   | Identifier for a built-in preset.                                           |
| `volume`         | number  | `0.15`  | Level relative to agent speech. Range `0.01`–`1.0`.                         |
| `crossfade_loop` | boolean | `true`  | Crossfade at the loop boundary so the sound does not click when it repeats. |

## Voice filter

Voice filter reshapes the agent's generated voice. It does not equalize or denoise the background sound. The filter runs first; background sound is mixed under the filtered speech.

Voice filter is dashboard-only. It is not part of the public agent API or CLI schema, and it may
not be available on all workspaces.

In the same **Audio environment** panel, set **Voice filter** to **Off** or a phone preset, then save.

## Limitations

* Built-in presets only. You cannot upload a custom file or point at an arbitrary URL.
* Audio environment controls are hidden when the agent is **text-only**.
* Background sound is not mixed into [WhatsApp](/docs/eleven-agents/whatsapp) voice-message replies. WhatsApp calls still include it.
* Background sound cannot be set per conversation through client [overrides](/docs/eleven-agents/customization/personalization/overrides); `conversation_config_override` does not include `background_sound`. You can still change it on a [workflow](/docs/eleven-agents/customization/agent-workflows) node.

## Related

#### [Tool call sounds](/docs/eleven-agents/customization/tools/tool-configuration/tool-call-sounds)

Play ambient audio only while a tool is running.

#### [Voice customization](/docs/eleven-agents/customization/voice)

Choose a voice, speed, and other speech settings for the agent.
