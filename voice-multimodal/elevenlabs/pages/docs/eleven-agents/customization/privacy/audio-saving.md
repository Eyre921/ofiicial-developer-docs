---
title: "Audio saving"
source: https://elevenlabs.io/docs/eleven-agents/customization/privacy/audio-saving.md
path: docs/eleven-agents/customization/privacy/audio-saving
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Audio saving

**Audio Saving** settings allow you to choose whether recordings of your calls are retained in your call history, on a per-agent basis. This control gives you flexibility over data storage and privacy.

## Overview

By default, audio recordings are enabled. You can modify this setting to:

* **Enable audio saving**: Save call audio for later review.
* **Disable audio saving**: Omit audio recordings from your call history.

Disabling audio saving enhances privacy but limits the ability to review calls. However,
transcripts can still be viewed. To modify transcript retention settings, please refer to the
[retention](/docs/eleven-agents/customization/privacy/retention) documentation.

## Modifying Audio Saving Settings

### Prerequisites

* A configured [ElevenLabs Conversational Agent](/docs/eleven-agents/quickstart)

#### Update via the dashboard

#### Access audio saving settings

Find your agent in the ElevenAgents [page](https://elevenlabs.io/app/agents/agents) and select
the "Advanced" tab. The audio saving control is located in the "Privacy Settings" section.

![Disable audio saving option](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e2f7d92f9128bace5d992e76aa500da7e1bc62d22d423841b774c1e20fcaf891/assets/images/conversational-ai/no-audio-setting.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260726%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260726T233154Z&X-Amz-Expires=604800&X-Amz-Signature=055882f564b4a886877b62f8d6f9f6c5043fdd3cd703feccdda8a2706967f515&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Choose saving option

Toggle the control to enable or disable audio saving and click save to confirm your selection.

#### Review call history

When audio saving is enabled, calls in the call history allow you to review the audio.

![Call with audio saved](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/871a28d699f54774c3e2695091e9af04948e236afded7807c27ea73bc2a8f71f/assets/images/conversational-ai/audio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260726%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260726T233154Z&X-Amz-Expires=604800&X-Amz-Signature=64fbd88ba4c1eee8b9009a63c169c7f71de9bd7c51cc2b645c59db14cc347fbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When audio saving is disabled, calls in the call history do not include audio.

![Call without audio saved](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/5dffbe46545eda166d48328b21f63ff0a6d3a0a8b05224213307da426ba6e47e/assets/images/conversational-ai/no-audio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260726%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260726T233154Z&X-Amz-Expires=604800&X-Amz-Signature=7f413b53498514ae806b65f5588483c861699f1881bfb40a76864feafb52cd9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `platform_settings.privacy.record_voice`:

```json
{
  "platform_settings": {
    "privacy": {
      "record_voice": false
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
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    platform_settings={
        "privacy": {"record_voice": False},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  platformSettings: {
    privacy: { recordVoice: false },
  },
});
```

Disabling audio saving will prevent new call audio recordings from being stored. Existing
recordings will remain until deleted via [retention
settings](/docs/eleven-agents/customization/privacy/retention).
