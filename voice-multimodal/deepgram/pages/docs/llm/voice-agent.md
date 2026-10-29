---
title: "Use in the Voice Agent"
source: https://developers.deepgram.com/docs/llm/voice-agent.md
path: docs/llm/voice-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Use in the Voice Agent

> **Warning**
>
> **Early Access.** Deepgram LLMs are available only to current Deepgram contract customers enrolled in the Early Access program ([talk to sales](https://deepgram.com/contact-us) for access). Usage is free during Early Access, requests run on the global endpoint only, SDKs do not support the endpoint yet, and the API can change before general availability. Do not run production traffic on it.

Use the Voice Agent API when you want Deepgram to run the full pipeline (listen, think, and speak) over one WebSocket. To use a Deepgram LLM as the agent's LLM, set the think provider `type` to `deepgram`.

## Configure the think stage

Set `agent.think.provider` in your [Settings message](/docs/configure-voice-agent):

```json
{
  "type": "Settings",
  "agent": {
    "think": {
      "provider": {
        "type": "deepgram",
        "model": "think-fast",
        "temperature": 0.7
      },
      "prompt": "You are a friendly voice agent. Reply in one or two short sentences."
    }
  }
}
```

| Field                                       | Value                                                                                                                                                                                         |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent.think.provider.type`                 | `deepgram`                                                                                                                                                                                    |
| `agent.think.provider.model`                | `think-fast` or `phonellm-mini-alpha-2-fp8`                                                                                                                                                   |
| `agent.think.provider.temperature`          | Optional. From `0` to `2`. Pipecat recommends `0.0` for phoneLLM mini.                                                                                                                        |
| `agent.think.provider.reasoning_mode`       | Optional. One of `none`, `minimal`, `low`, `medium`, or `high`. For voice, leave it unset or set it to `none`. With phoneLLM mini, `low` and higher make the agent speak its reasoning aloud. |
| `agent.think.provider.voice_prompt_opt_out` | Optional Boolean, default `false`. Think-Fast only. Set to `true` to send your prompt unchanged. See [Voice style instructions](#voice-style-instructions).                                   |
| `agent.think.endpoint`                      | Omit. Deepgram hosts these models.                                                                                                                                                            |

`/v1/think` calls the same control `reasoning_effort`. In the Voice Agent, use `reasoning_mode`: a `Settings` message with `reasoning_effort` is rejected with `UNPARSABLE_CLIENT_MESSAGE`.

Think-Fast can only be used with the Model Improvement Program. A `Settings` message that selects `think-fast` in a session opted out of MIP (`mip_opt_out: true` at the top level of `Settings`, or a project that requires opt-out) is rejected with `INVALID_SETTINGS`. Use `phonellm-mini-alpha-2-fp8` for sessions that opt out. See [Data retention and MIP](/docs/llm/data-retention).

## Voice style instructions

With `think-fast`, Deepgram places instructions on spoken response style ahead of your prompt and sends a `Warning` with code `VOICE_PROMPT_ADDED` after `Settings`:

`The think model think-fast is tuned for voice, so Deepgram places instructions on spoken response style ahead of your prompt. Set agent.think.provider.voice_prompt_opt_out to true to send your prompt unchanged.`

Set `agent.think.provider.voice_prompt_opt_out` to `true` to send your prompt unchanged. phoneLLM mini sessions do not get these instructions.

## SDK support

Typed SDK support for the `deepgram` think provider is coming. The Voice Agent works with Think-Fast and phoneLLM mini from every Deepgram SDK today:

| SDK        | What to do                                                                                                     |
| ---------- | -------------------------------------------------------------------------------------------------------------- |
| Go         | Set the provider type to `deepgram` as usual. The provider is a map, so it passes through.                     |
| .NET       | Set `Provider.Type = "deepgram"` as usual.                                                                     |
| JavaScript | Cast the provider to `Deepgram.ThinkSettingsV1Provider`, because strict TypeScript rejects `type: "deepgram"`. |
| Python     | Send the settings as a plain dict with `send_raw`.                                                             |
| Java       | Leave `.think()` unset and pass the think block as a map with `additionalProperty("think", ...)`.              |

> **Warning**
>
> In Python, do not build typed settings with `model_construct` to get around validation. It sends `"provider": null`, and the server rejects the message with `UNPARSABLE_CLIENT_MESSAGE` and no hint about why. Send a plain dict instead.

**`TypeScript`**

```typescript TypeScript
import { Deepgram } from "@deepgram/sdk";

connection.sendSettings({
  type: "Settings",
  audio: {
    input: { encoding: "linear16", sample_rate: 24000 },
    output: { encoding: "linear16", sample_rate: 24000, container: "wav" },
  },
  agent: {
    listen: { provider: { type: "deepgram", version: "v1", model: "nova-3" } },
    think: {
      // The SDK types don't list the deepgram provider yet, so cast it.
      provider: { type: "deepgram", model: "think-fast" } as unknown as Deepgram.ThinkSettingsV1Provider,
      prompt: "You are a friendly voice agent. Reply in one or two short sentences.",
    },
    speak: { provider: { type: "deepgram", model: "aura-2-thalia-en" } },
  },
});
```

**`Python`**

```python Python
# Typed settings reject the deepgram provider, so send a plain dict.
settings = {
    "type": "Settings",
    "audio": {
        "input": {"encoding": "linear16", "sample_rate": 24000},
        "output": {"encoding": "linear16", "sample_rate": 24000, "container": "wav"},
    },
    "agent": {
        "listen": {"provider": {"type": "deepgram", "model": "nova-3"}},
        "think": {
            "provider": {"type": "deepgram", "model": "think-fast"},
            "prompt": "You are a friendly voice agent. Reply in one or two short sentences.",
        },
        "speak": {"provider": {"type": "deepgram", "model": "aura-2-thalia-en"}},
    },
}
connection.send_raw(settings)
```

**`Java`**

```java Java
// The SDK has no deepgram think provider yet: leave .think() unset
// and pass the think block as a map.
Map<String, Object> think = Map.of(
    "provider", Map.of("type", "deepgram", "model", "think-fast"),
    "prompt", "You are a friendly voice agent. Reply in one or two short sentences.");

AgentV1SettingsAgentContext agent = AgentV1SettingsAgentContext.builder()
    // Set listen, speak, and the rest of the agent as usual.
    .additionalProperty("think", think)
    .build();
```

`voice_prompt_opt_out` reaches the server the same way: add it to the provider object.

## Related pages

Function calls and context work the same way as with the other Voice Agent LLM providers:

* [LLM Models](/docs/voice-agent-llm-models)
* [Function Calling](/docs/voice-agents-function-calling)
* [Prompting Voice Agents](/docs/prompting-voice-agents)
* [Maintaining Context](/docs/voice-agent-conversation-context)

## When to call /v1/think directly instead

Use the Voice Agent API when you want Deepgram to manage turn-taking, barge-in, and audio. Call `/v1/think` directly when you run your own orchestration, such as a custom STT, LLM, and TTS loop. See [Build a cascaded agent](/docs/llm/cascaded-agent).
