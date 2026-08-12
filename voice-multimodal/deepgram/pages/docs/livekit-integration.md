---
title: "LiveKit and Deepgram"
source: https://developers.deepgram.com/docs/livekit-integration.md
path: docs/livekit-integration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# LiveKit and Deepgram

This guide walks you through building a voice AI agent that uses [LiveKit Agents](https://docs.livekit.io/agents/) for real-time audio transport and Deepgram for speech-to-text (STT) and text-to-speech (TTS). By the end, you will have a working voice agent that listens to a user, generates a response with an LLM, and speaks back in real time.

Deepgram is available in LiveKit Agents through two paths:

| Path              | Description                                                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LiveKit Inference | Deepgram models hosted and billed through LiveKit Cloud. Supports Nova-3, Nova-2 variants (`nova-2`, `nova-2-medical`, `nova-2-phonecall`), Flux, and Aura-2. No Deepgram API key required. |
| Deepgram Plugin   | Connects directly to Deepgram's API with your own API key. Includes diarization, keyterm prompting, and advanced parameters.                                                                |

This guide starts with LiveKit Inference for the fastest setup, then shows how to switch to the Deepgram Plugin for direct API access and advanced features.

Code samples are provided for both Python and TypeScript (Node.js). Choose one language and follow its tab in each step.

## Before you begin

Before you can use Deepgram, you need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes \$200 in credit.

You need:

* A [LiveKit Cloud](https://cloud.livekit.io) account (or a self-hosted LiveKit server)
* An LLM. The starter uses LiveKit Inference (`inference.LLM(model="openai/chat-latest")`), which runs through LiveKit Cloud and requires no separate provider key. A dedicated LLM API key is only needed if you bring your own provider, such as [OpenAI](https://platform.openai.com/api-keys); LiveKit Agents supports [other providers](https://docs.livekit.io/agents/models/) too.
* Python 3.10+ or Node.js 20+

## Step 1: Create the project

The fastest way to scaffold a new agent project is with the [LiveKit CLI](https://docs.livekit.io/intro/basics/cli/) (`lk`). Alternatively, clone a starter template from GitHub ([Python](https://github.com/livekit-examples/agent-starter-python), [Node.js](https://github.com/livekit-examples/agent-starter-node)).

```bash title="Python"
lk agent init my-agent --template agent-starter-python
cd my-agent
uv sync
```

```bash title="Node.js"
lk agent init my-agent --template agent-starter-node
cd my-agent
pnpm install
```

When the CLI finishes, your agent is registered with LiveKit Cloud. You'll test it later from the [Agent Console](https://cloud.livekit.io).

## Step 2: Configure your environment

The CLI creates a `.env.local` file during setup. Open it and confirm your API keys are set:

```bash
LIVEKIT_URL=YOUR_LIVEKIT_CLOUD_URL
LIVEKIT_API_KEY=YOUR_LIVEKIT_API_KEY
LIVEKIT_API_SECRET=YOUR_LIVEKIT_API_SECRET
# Only required if you switch the LLM to OpenAI directly instead of using LiveKit Inference:
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

If you used the CLI's guided setup, these values are already populated. If not, add them from your [LiveKit Cloud dashboard](https://cloud.livekit.io). The `OPENAI_API_KEY` is optional — the starter uses LiveKit Inference by default, so you only need it if you bring your own OpenAI key from the [OpenAI dashboard](https://platform.openai.com/api-keys).

## Step 3: Use Deepgram for TTS

At the time of writing, the starter template uses Deepgram for STT but Cartesia for TTS. These defaults change frequently and aren't guaranteed, so check the generated code. To use Deepgram for both, find the `tts` argument in the `AgentSession` constructor in `src/agent.py` (Python) or `src/main.ts` (Node.js) and replace it:

```python
# Python — src/agent.py
# Replace the existing tts line with:
tts=inference.TTS(model="deepgram/aura-2", voice="thalia"),
```

```typescript
// TypeScript — src/main.ts
// Replace the existing tts line with:
tts: new inference.TTS({
  model: 'deepgram/aura-2',
  voice: 'thalia',
}),
```

The agent now uses Deepgram for both STT and TTS. No additional dependencies or API keys are needed because both run through LiveKit Inference.

Browse available voices in the [Deepgram voice library](/docs/tts-models).

## Step 4: Run the agent

Start the agent in development mode. The required model files ([VAD](/docs/understanding-end-of-speech-detection), turn detection) are now downloaded automatically:

```bash title="Python"
uv run src/agent.py dev
```

```bash title="Node.js"
pnpm run dev
```

The `dev` command connects your agent to LiveKit Cloud. Open the [Agent Console](https://cloud.livekit.io) in your browser to talk to your agent.

## Step 5: Test the conversation

Once the agent is running, you should hear a greeting. Try these interactions to verify everything works:

1. Ask a question and confirm the agent responds with speech.
2. Start speaking while the agent is talking. It should stop and listen.
3. Pause after speaking. The agent should detect the end of your turn and respond.

If any of these fail, check your API keys and confirm the agent process is running.

## Use the Deepgram Plugin for advanced features

The steps above use LiveKit Inference, which hosts Deepgram models through LiveKit Cloud. If you need direct access to Deepgram features like [speaker diarization](/docs/diarization), [keyterm prompting](/docs/keyterm), or fine-grained parameter control, use the Deepgram Plugin instead. This connects directly to Deepgram's API with your own API key.

### Install the plugin

```bash title="Python"
uv add "livekit-agents[deepgram]~=1.4"
```

```bash title="Node.js"
pnpm add @livekit/agents-plugin-deepgram@1.x
```

### Set your Deepgram API key

Add `DEEPGRAM_API_KEY` to your `.env.local` file:

```bash
DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY
```

Replace `YOUR_DEEPGRAM_API_KEY` with the API key from your [Deepgram Console](https://console.deepgram.com/). The plugin reads this variable automatically at startup.

### Update the AgentSession

Add the Deepgram import at the top of your entrypoint file, then replace the `stt` and `tts` arguments in the `AgentSession`:

```python
# Python — src/agent.py
from livekit.plugins import deepgram

# Replace the stt and tts lines in your AgentSession:
stt=deepgram.STT(
    model="nova-3",
    language="en",
    punctuate=True,
    interim_results=True,
),
tts=deepgram.TTS(model="aura-2-thalia-en"),
```

```typescript
// TypeScript — src/main.ts
import * as deepgram from "@livekit/agents-plugin-deepgram";

// Replace the stt and tts lines in your AgentSession:
stt: new deepgram.STT({
  model: "nova-3",
  language: "en",
  punctuate: true,
  interimResults: true,
}),
tts: new deepgram.TTS({ model: "aura-2-thalia-en" }),
```

Your agent now connects directly to Deepgram's API with your own API key, instead of going through LiveKit Inference. This unlocks the advanced features covered below, such as [keyterm prompting](/docs/keyterm), [speaker diarization](/docs/diarization), and fine-grained STT/TTS parameters.

To verify the change, restart the agent as in [Step 4](#step-4-run-the-agent) (`uv run src/agent.py dev` for Python, or `pnpm run dev` for Node.js) and run through the checks in [Step 5](#step-5-test-the-conversation). The conversation should behave as before, now powered by the Deepgram plugin. If the agent fails to start, confirm `DEEPGRAM_API_KEY` is set in `.env.local`.

### Use Flux for turn detection

[Flux](/docs/flux) is Deepgram's conversational STT model with built-in turn detection. It uses acoustic and semantic cues to determine when a speaker has finished their turn, resulting in more natural conversations with fewer awkward pauses.

To use Flux, replace the `stt` configuration with `STTv2` and set turn detection to `"stt"`:

```python
# Replace the stt line and add turn_handling:
stt=deepgram.STTv2(model="flux-general-en"),
turn_handling={"turn_detection": "stt"},
```

```typescript
// TypeScript — src/main.ts
// Replace the stt line and add turnDetection:
stt: new deepgram.STTv2({ model: "flux-general-en" }),
turnHandling: { turnDetection: "stt" },
```

Even when using Flux for turn detection, a [VAD (Voice Activity Detection)](/docs/understanding-end-of-speech-detection) is required for interruption handling — without it, the agent cannot detect when a user speaks over the agent's response. If you don't specify a VAD, LiveKit auto-provisions one for you. Note that this is not the Silero plugin itself, but a bundled inference VAD that is still based on Silero. You can also add the Silero plugin explicitly if you prefer to manage it yourself.

### Choose a different voice

#### Flux

Flux is the latest conversation-native TTS model, built for real-time voice agents. It's expressive by default, consistent across turns, and responds in under 200ms with native interruption handling, real-time controls, and strong entity accuracy.

```python
# Python
tts = deepgram.TTSv2(model="flux-alexis-en")
```

```typescript
// TypeScript
const tts = new deepgram.TTSv2({ model: "flux-alexis-en" });
```

#### Aura 2

Deepgram offers 60+ voices across seven languages with Aura 2. Replace the `model` parameter in `TTS` with any supported voice:

```python
# Python
tts = deepgram.TTS(model="aura-2-andromeda-en")
```

```typescript
// TypeScript
const tts = new deepgram.TTS({ model: "aura-2-andromeda-en" });
```

Browse all available voices in the [Deepgram voice library](/docs/tts-models).

## Go further with Deepgram

* **Voices** — Deepgram offers 60+ voices across seven languages. Browse the [voice library](/docs/tts-models) and replace the `model` parameter in `TTS` with any supported voice.
* **Keyterm prompting** — Improve recognition of domain-specific vocabulary by passing [keyterms](/docs/keyterm) to Nova-3 via the STT plugin settings.
* **Speaker diarization** — Assign a speaker identifier to each word in the transcript using [diarization](/docs/diarization) via the STT plugin settings.
* **Plugin reference** — See the full list of plugin parameters in the LiveKit Deepgram reference for [Python](https://docs.livekit.io/reference/python/livekit/plugins/deepgram/index.html#livekit.plugins.deepgram.STT) and [Node.js](https://docs.livekit.io/reference/agents-js/classes/plugins_agents_plugin_deepgram.STT.html).

## Resources

* [Deepgram Models & Languages](/docs/models-languages-overview)
* [Deepgram TTS Voices](/docs/tts-models)
* [LiveKit Agents Docs](https://docs.livekit.io/agents/)
* [LiveKit Deepgram STT Guide](https://docs.livekit.io/agents/models/stt/deepgram/)
* [LiveKit Deepgram TTS Guide](https://docs.livekit.io/agents/models/tts/deepgram/)
* [livekit-plugins-deepgram on PyPI](https://pypi.org/project/livekit-plugins-deepgram/)
* [@livekit/agents-plugin-deepgram on npm](https://www.npmjs.com/package/@livekit/agents-plugin-deepgram)
