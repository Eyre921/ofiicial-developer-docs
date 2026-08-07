---
title: "Zero Retention Mode (per-agent)"
source: https://elevenlabs.io/docs/eleven-agents/customization/privacy/zrm.md
path: docs/eleven-agents/customization/privacy/zrm
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Zero Retention Mode (per-agent)

## Overview

Zero Retention Mode (ZRM) enhances data privacy by ensuring that no Personally Identifiable Information (PII) is logged during or stored after a call. This feature can be enabled on a per-agent basis for workspaces that do not have ZRM enforced globally. For workspaces with global ZRM enabled, all agents will automatically operate in Zero Retention Mode.

When ZRM is active for an agent:

* No call recordings will be stored.
* No transcripts or call metadata containing PII will be logged or stored by our systems post-call.

For more information about setting your workspace to have Zero Retention Mode across all eligible ElevenLabs products, see our [Zero Retention Mode](/docs/eleven-api/resources/zero-retention-mode) documentation.

For workspaces where Zero Retention Mode is enforced globally, this setting will be automatically
enabled for all agents and cannot be disabled on a per-agent basis.

To retrieve information about calls made with ZRM-enabled agents, you must use [post-call webhooks](/docs/eleven-agents/workflows/post-call-webhooks).

Enabling Zero Retention Mode may impact ElevenLabs' ability to debug call-related issues for the
specific agent, as limited logs or call data will be available for review.

## How to Enable ZRM per Agent

For workspaces not operating under global Zero Retention Mode, you can enable ZRM for individual agents:

#### Update via the dashboard

Open your agent in the dashboard, navigate to the **Privacy** settings block, select the **Advanced** tab, and toggle **Zero Retention Mode** on. Save your changes.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b11c36caf8829dd90829c3b51df2be879a77f718834af8988ecd33e9ae44a071/assets/images/conversational-ai/enabled-zrm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260807T113332Z&X-Amz-Expires=604800&X-Amz-Signature=5e767eb7b74df561b6ea5e7c4c1627e5082c07d87faa76d2744bc6d67890920c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Enable Zero Retention Mode for Agent" />

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `platform_settings.privacy.zero_retention_mode`:

```json
{
  "platform_settings": {
    "privacy": {
      "zero_retention_mode": true
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
        "privacy": {"zero_retention_mode": True},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  platformSettings: {
    privacy: { zeroRetentionMode: true },
  },
});
```
