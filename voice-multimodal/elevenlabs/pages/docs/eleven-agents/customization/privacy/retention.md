---
title: "Retention"
source: https://elevenlabs.io/docs/eleven-agents/customization/privacy/retention.md
path: docs/eleven-agents/customization/privacy/retention
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Retention

**Retention** settings allow you to configure how long your conversational agent stores conversation transcripts and audio recordings. These settings help you comply with data privacy regulations.

## Overview

By default, ElevenLabs retains conversation data for 2 years. You can modify this period to:

* Any number of days (e.g., 30, 90, 365)
* Unlimited retention by setting the value to -1
* Scheduled deletion by setting the value to 0

The retention settings apply separately to:

* **Conversation transcripts**: Text records of all interactions
* **Audio recordings**: Voice recordings from both the user and agent

For GDPR compliance, we recommend setting retention periods that align with your data processing
purposes. For HIPAA compliance, retain records for a minimum of 6 years.

## Modifying retention settings

### Prerequisites

* An [ElevenLabs account](https://elevenlabs.io)
* A configured ElevenLabs Conversational Agent ([create one here](/docs/eleven-agents/quickstart))

#### Update via the dashboard

#### Access retention settings

Navigate to your agent's settings and select the "Advanced" tab. The retention settings are located in the "Data Retention" section.

![Enable overrides](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/39019a60151b8d999d5e1719e1553508a91c3bf7a34e6f5729ea2942c3dc4d57/assets/images/conversational-ai/retention.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T222210Z&X-Amz-Expires=604800&X-Amz-Signature=f0247acdb57a1ac581d06a125823897856885d1573649f405d5f148645e9ecf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Update retention period

1. Enter the desired retention period in days
2. Choose whether to apply changes to existing data
3. Click "Save" to confirm changes

![Enable overrides](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a5d069a0957ee06672aab4a8784362a72ed7d3f055d548eb54b32998ec246aad/assets/images/conversational-ai/retention-apply-existing.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T222210Z&X-Amz-Expires=604800&X-Amz-Signature=b7e21b08752bf69cf0fd08f14ebf7646ce30143c2e94b0ab7682b105f8736622&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

When modifying retention settings, you'll have the option to apply the new retention period to existing conversation data or only to new conversations going forward.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `platform_settings.privacy.retention_days`:

```json
{
  "platform_settings": {
    "privacy": {
      "retention_days": 30
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
        "privacy": {"retention_days": 30},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  platformSettings: {
    privacy: { retentionDays: 30 },
  },
});
```

Reducing the retention period may result in immediate deletion of data older than the new
retention period if you choose to apply changes to existing data.
