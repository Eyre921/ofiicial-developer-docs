---
title: "Tool interruptions"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/tool-configuration/tool-interruptions.md
path: docs/eleven-agents/customization/tools/tool-configuration/tool-interruptions
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Tool interruptions

## Overview

By default a user can interrupt the agent at any point, including while a tool is executing. For
some tools this is undesirable: a payment confirmation or a compliance disclaimer read out after a
lookup should be delivered in full.

The `interruption_mode` field controls this per tool. It is available on webhook tools, client
tools, system tools, and MCP servers.

## Interruption modes

| Value                          | Dashboard label           | Behavior                                                                                                   |
| ------------------------------ | ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `allow`                        | Allow                     | The user can interrupt the agent at any time. This is the default.                                         |
| `disable_during_tool`          | Disable during execution  | Interruptions are suppressed only while the tool runs. The agent response that follows can be interrupted. |
| `disable_during_tool_and_turn` | Disable during whole turn | Interruptions are suppressed while the tool runs and for the agent response that follows it.               |

When several tools run in parallel, the strictest mode among them applies for that turn.

The boolean `disable_interruptions` field is deprecated. Use `interruption_mode` instead. The two
fields are kept in sync, so `disable_interruptions: true` is equivalent to `interruption_mode:
  "disable_during_tool_and_turn"` and existing integrations continue to work unchanged.

## Configuration

#### Update via the dashboard

#### Navigate to tool configuration

Select the tool you want to configure in the **Tools** tab.

#### Set the interruption mode

Open **Advanced settings** and choose an option under **Interruptions**.

#### Save your configuration

Click **Save** to apply the change.

#### Update via the CLI

#### Pull the tool configuration

```bash
elevenlabs tools pull
```

#### Edit \`tool\_configs/\<tool-name>.json\`

Set `interruption_mode` on the tool:

```json
{
  "type": "webhook",
  "name": "confirm_payment",
  "description": "Confirms a pending payment",
  "interruption_mode": "disable_during_tool_and_turn"
}
```

#### Push your changes

```bash
elevenlabs tools push
```

#### Update via the API

```python
from elevenlabs import ElevenLabs, ToolRequestModel

elevenlabs = ElevenLabs()

elevenlabs.conversational_ai.tools.update(
    tool_id="tool_7101k5zvyjhmfg983brhmhkd98n6",
    request=ToolRequestModel(
        tool_config={
            "type": "webhook",
            "name": "confirm_payment",
            "description": "Confirms a pending payment",
            "interruption_mode": "disable_during_tool_and_turn",
            "api_schema": {
                "url": "https://api.example.com/payments/confirm",
                "method": "POST",
            },
        },
    ),
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.tools.update("tool_7101k5zvyjhmfg983brhmhkd98n6", {
  toolConfig: {
    type: "webhook",
    name: "confirm_payment",
    description: "Confirms a pending payment",
    interruptionMode: "disable_during_tool_and_turn",
    apiSchema: {
      url: "https://api.example.com/payments/confirm",
      method: "POST",
    },
  },
});
```

## MCP servers

An [MCP server](/docs/eleven-agents/customization/tools/mcp) carries its own `interruption_mode`,
which applies to every tool it exposes. Individual tools can override it through the server's
`tool_config_overrides`, where the value set on a tool takes precedence over the server default.

## Best practices

* Use `disable_during_tool` when the tool call itself must complete, such as a transfer or a keypad
  sequence, but the user should be able to interrupt the response afterwards.
* Use `disable_during_tool_and_turn` when the response that follows the tool must be heard in full,
  such as a disclaimer or a confirmation read-back.
* Leave the default `allow` in place elsewhere, since suppressing interruptions makes the
  conversation feel less responsive.
