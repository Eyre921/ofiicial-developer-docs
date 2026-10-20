---
title: "Realtime models"
source: https://elevenlabs.io/docs/eleven-agents/customization/realtime-models.md
path: docs/eleven-agents/customization/realtime-models
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Realtime models

## Overview

A Realtime model is an ElevenLabs model built for low-latency voice conversation, available to voice agents.

Every voice agent has a **Voice mode**: **Custom** or **Realtime**. In Custom mode, you choose the LLM, TTS model, and ASR settings yourself, as described in [Models](/docs/eleven-agents/customization/llm). In Realtime mode, you choose a Realtime model, and ElevenLabs manages those settings for you.

Two Realtime models are available:

| Model                       | `realtime_model` value    | Description                                                                                         |
| --------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------- |
| **Eleven Realtime v1 Mini** | `eleven_realtime_v1_mini` | The default Realtime model. Lowest latency and cost.                                                |
| **Eleven Realtime v1 Max**  | `eleven_realtime_v1_max`  | Reasons before it responds, for complex instructions and multi-step tool use. Costs more than Mini. |

The agent's system prompt, voice, tools, knowledge base, and turn settings work the same in both modes.

> **Tip**
>
> Coming from another realtime API, such as SpaceXAI or OpenAI? The [Realtime API](/docs/eleven-agents/guides/openai-realtime-compatibility) is a quicker way to try out
> Realtime models: point your existing client at ElevenLabs and keep the events you already use.

> **Note**
>
> Realtime models are rolling out gradually. If the **Voice mode** setting doesn't appear on your
> agent's **Agent** tab, Realtime models aren't available for your workspace yet, and the API
> rejects `realtime_model` with the error `Realtime models are not available for this workspace.`

## Choosing a voice mode

Keep the agent in Custom mode if any of the following apply:

* The agent uses a [custom LLM](/docs/eleven-agents/customization/llm/custom-llm), Amazon Bedrock, or [Speech Engine](/docs/eleven-api/guides/cookbooks/speech-engine).
* The agent needs a specific LLM or TTS model.
* Workflow nodes override the LLM, TTS model, or another [managed setting](#managed-settings).
* The agent transfers to or from agents in Custom mode.
* The agent is text-only. Realtime models are built for voice conversations.

Otherwise, start with Eleven Realtime v1 Mini. Choose Eleven Realtime v1 Max instead when:

* The agent follows long or complex instructions, or relies on multi-step tool calls, and Mini's responses aren't good enough.
* The agent must comply with [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm) or [HIPAA](/docs/eleven-agents/legal/hipaa) in the US or EU. Mini isn't available under either.

Max isn't available in the India and Singapore data residency environments, and it needs a token limit of at least 1,024, or no limit. See [Limitations](#limitations) and [Compliance and data residency](#compliance-and-data-residency).

## Configuration

#### Update via the dashboard

#### Open the Agent tab

Open your agent in the dashboard and go to the **Agent** tab.

#### Set the voice mode

Set **Voice mode** to **Realtime**. The agent switches to Eleven Realtime v1 Mini.

#### Choose a model

To use Eleven Realtime v1 Max instead, select it from the **Model** list.

#### Publish

Publish your changes. Publishing fails if the agent breaks one of the rules in [Limitations](#limitations).

To turn Realtime off, set **Voice mode** to **Custom** and publish. The agent goes back to the LLM, TTS model, and ASR settings stored on it.

#### Update via the CLI

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent_configs/\<agent-name>.json\`

Set `conversation_config.realtime_model`:

```json
{
  "conversation_config": {
    "realtime_model": "eleven_realtime_v1_mini"
  }
}
```

To turn Realtime off, set `realtime_model` to `null`.

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
    conversation_config={
        "realtime_model": "eleven_realtime_v1_mini",
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    realtimeModel: "eleven_realtime_v1_mini",
  },
});
```

To turn Realtime off, set `realtime_model` to `None` in Python or `realtimeModel` to `null` in TypeScript.

## Managed settings

While a Realtime model is set, ElevenLabs manages the following settings, and the agent ignores the values stored for them. The stored values come back into use when you switch to Custom.

| Setting             | Field in `conversation_config`            |
| ------------------- | ----------------------------------------- |
| LLM                 | `agent.prompt.llm`                        |
| Reasoning effort    | `agent.prompt.reasoning_effort`           |
| Thinking budget     | `agent.prompt.thinking_budget`            |
| Parallel tool calls | `agent.prompt.enable_parallel_tool_calls` |
| Cascade timeout     | `agent.prompt.cascade_timeout_seconds`    |
| TTS model           | `tts.model_id`                            |
| Expressive mode     | `tts.expressive_mode`                     |
| ASR provider        | `asr.provider`                            |

The token limit (`agent.prompt.max_tokens`) keeps its stored value, but workflow nodes can't override it, and Eleven Realtime v1 Max needs a minimum value. See [Limitations](#limitations).

To change any of these settings, switch the agent to Custom.

## Settings that still apply

All other agent settings work as they do in Custom mode, including:

* the system prompt and first message
* the voice, including [multi-voice support](/docs/eleven-agents/customization/voice/multi-voice-support)
* [languages](/docs/eleven-agents/customization/voice/customization/language)
* temperature
* [tools](/docs/eleven-agents/customization/tools) and the [knowledge base](/docs/eleven-agents/customization/knowledge-base)
* [conversation flow](/docs/eleven-agents/customization/conversation-flow) settings such as turn eagerness, timeouts, and interruptions

The dashboard hides the LLM settings, including temperature, while the agent is in Realtime mode. Use the CLI or the API to change temperature on a Realtime agent.

If the Realtime model doesn't respond in time or returns an error, the agent falls back to backup LLMs as described in [LLM cascading](/docs/eleven-agents/customization/llm/llm-cascading). The Realtime model sets how long the agent waits before falling back.

## Limitations

ElevenLabs checks these rules when you publish the agent. A draft that breaks one of them still saves, but publishing fails with an error that names the setting to change.

* **ElevenAgents agents only**: Agents created through other ElevenLabs products, such as [Speech Engine](/docs/eleven-api/guides/cookbooks/speech-engine), can't use a Realtime model.
* **No custom LLM**: Realtime mode isn't available while the agent's LLM is a custom LLM or Amazon Bedrock. Select a built-in LLM in Custom mode before switching.
* **No workflow overrides of managed settings**: A workflow node can't override any [managed setting](#managed-settings) or the token limit. Remove the override, or keep the agent in Custom mode.
* **Token limit for Max**: Eleven Realtime v1 Max needs a token limit of 1,024 or more, or no limit.
* **Transfers between modes**: An agent in Realtime mode can only [transfer](/docs/eleven-agents/customization/tools/system-tools/agent-transfer) to and from other agents in Realtime mode. Transfers between Mini and Max agents are supported.

> **Warning**
>
> Publishing checks only the transfers the published agent makes. A transfer into a Realtime agent
> from a Custom-mode agent is caught only when the Custom-mode agent is next published; until then,
> the transfer is rejected during the conversation and the current agent stays on the call.

Transfer errors read `Transfers between default and Realtime model modes are not supported.`, where "default" means Custom mode.

## Compliance and data residency

Realtime models follow the same [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm), [HIPAA](/docs/eleven-agents/legal/hipaa), and [data residency](/docs/overview/administration/data-residency) rules as other models. Availability differs between Mini and Max:

| Environment                   | Eleven Realtime v1 Mini | Eleven Realtime v1 Max     |
| ----------------------------- | ----------------------- | -------------------------- |
| US                            | Available               | Available                  |
| EU data residency             | Available               | Available                  |
| India data residency          | Available               | Not available              |
| Singapore data residency      | Available               | Not available              |
| Zero Retention Mode and HIPAA | Not available           | Available in the US and EU |

Zero Retention Mode applies whether it is enforced on the workspace or enabled on the agent.

If a Realtime model isn't available under the agent's compliance or data residency settings, ElevenLabs rejects it with an error that names the model. Choose the other Realtime model, or switch to Custom.

## Pricing

A Realtime agent is billed the standard ElevenAgents per-minute rate, plus its input, cached input, and output tokens at the Realtime model's rates. Eleven Realtime v1 Max costs more per token than Eleven Realtime v1 Mini. See [ElevenLabs pricing](https://elevenlabs.io/pricing) for current rates.

## Related resources

* [Models](/docs/eleven-agents/customization/llm)
* [LLM cascading](/docs/eleven-agents/customization/llm/llm-cascading)
* [Agent transfer](/docs/eleven-agents/customization/tools/system-tools/agent-transfer)
* [Zero Retention Mode](/docs/eleven-agents/customization/privacy/zrm)
* [HIPAA compliance](/docs/eleven-agents/legal/hipaa)
