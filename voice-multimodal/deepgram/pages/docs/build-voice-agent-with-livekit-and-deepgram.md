---
title: "Build a Voice Agent with LiveKit and Deepgram"
source: https://developers.deepgram.com/docs/build-voice-agent-with-livekit-and-deepgram.md
path: docs/build-voice-agent-with-livekit-and-deepgram
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with LiveKit and Deepgram

> Build a real-time voice agent with LiveKit for WebRTC transport, Deepgram Nova-3 for speech-to-text, and Deepgram Aura for text-to-speech.

If you already use [LiveKit](https://livekit.io/) for WebRTC audio transport, you can add Deepgram's speech-to-text and text-to-speech models to your LiveKit agent pipeline. LiveKit's framework requires separate STT, LLM, and TTS providers, so this guide pairs Deepgram's audio models with OpenAI for language understanding — though any LiveKit-compatible LLM works.

For a standalone voice agent without LiveKit or an external LLM, see the [Deepgram Voice Agent API](/docs/voice-agent), which bundles STT, LLM routing, and TTS in a single WebSocket connection.

## Before You Begin

This guide assumes you are familiar with Python or Node.js and have a basic understanding of how voice agents work.

You'll need a [Deepgram account](https://console.deepgram.com/signup?jump=keys) and an API key. Signup is free and includes **\$200** in credit.

### Get OpenAI Credentials

This tutorial uses OpenAI for its LLM. You'll need to [sign up for an OpenAI account](https://platform.openai.com/signup/) and obtain an [API key](https://platform.openai.com/api-keys).

### Get LiveKit Credentials

You'll need a [LiveKit Cloud account](https://cloud.livekit.io) with your LiveKit URL, API Key, and API Secret.

### Requirements

* Python 3.10+ or Node.js 18+

## Set Up Your Project

This implementation is a starting reference for building your own voice agent with LiveKit and Deepgram. It is not designed for production deployments.

Create a new directory, set up your environment, and install the LiveKit agents framework along with the Deepgram and Silero plugins:

```bash title="Python"
mkdir deepgram-livekit-agent
cd deepgram-livekit-agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install "livekit-agents[openai]" livekit-plugins-deepgram livekit-plugins-silero python-dotenv
```

```bash title="Node.js"
mkdir deepgram-livekit-agent
cd deepgram-livekit-agent
npm init -y
npm pkg set type="module"
npm install @livekit/agents @livekit/agents-plugin-deepgram @livekit/agents-plugin-openai @livekit/agents-plugin-silero dotenv
npm install -D typescript @types/node
```

## Set Environment Variables

Create a `.env` file in your project root with the credentials you collected earlier. The agent reads these at startup to authenticate with each service:

```
DEEPGRAM_API_KEY=your_deepgram_api_key
OPENAI_API_KEY=your_openai_api_key
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

`LIVEKIT_URL` is the WebSocket endpoint for your LiveKit Cloud project. You can find it along with your API key and secret in the [LiveKit dashboard](https://cloud.livekit.io).

## Build the Agent

The agent connects to a LiveKit room, creates a session with Deepgram for audio processing and OpenAI for language understanding, and starts listening for speech.

The key components are:

* **`Agent`** — defines the agent's personality and instructions.
* **`AgentSession`** — wires together the STT, LLM, TTS, and VAD providers into a pipeline. When a user speaks, audio flows through Deepgram Nova-3 for transcription, OpenAI GPT-4o for a response, and Deepgram Aura for speech synthesis.
* **`generate_reply`** — triggers the agent's first message so it greets the user without waiting for input.

Create `agent.py` (Python) or `agent.ts` (Node.js):

```python title="Python"
# agent.py

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    AgentServer,
    JobContext,
    cli,
)
from livekit.plugins import deepgram, openai, silero

load_dotenv()

server = AgentServer()


class VoiceAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions=(
                "You are a friendly, helpful voice assistant. "
                "Keep your responses concise — aim for 1-3 sentences "
                "unless the user asks for detail."
            ),
        )


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(
            model="nova-3",
            language="en",
            punctuate=True,
            smart_format=True,
            interim_results=True,
        ),
        llm=openai.LLM(model="gpt-4o"),
        tts=deepgram.TTS(model="aura-2-thalia-en"),
        vad=silero.VAD.load(),
    )

    await session.start(
        agent=VoiceAssistant(),
        room=ctx.room,
    )

    await session.generate_reply(
        instructions="Greet the user and ask how you can help.",
        allow_interruptions=True,
    )


if __name__ == "__main__":
    cli.run_app(server)
```

```typescript title="Node.js"
// agent.ts

import {
  type JobContext,
  type JobProcess,
  cli,
  defineAgent,
  ServerOptions,
  voice,
} from "@livekit/agents";
import * as deepgram from "@livekit/agents-plugin-deepgram";
import * as silero from "@livekit/agents-plugin-silero";
import { LLM } from "@livekit/agents-plugin-openai";
import { fileURLToPath } from "node:url";
import "dotenv/config";

export default defineAgent({
  prewarm: async (proc: JobProcess) => {
    proc.userData.vad = await silero.VAD.load();
  },

  entry: async (ctx: JobContext) => {
    await ctx.connect();

    const agent = new voice.Agent({
      instructions:
        "You are a friendly, helpful voice assistant. " +
        "Keep your responses concise — aim for 1-3 sentences " +
        "unless the user asks for detail.",
    });

    const session = new voice.AgentSession({
      vad: ctx.proc.userData.vad as silero.VAD,
      stt: new deepgram.STT({
        model: "nova-3",
        language: "en",
        punctuate: true,
        smartFormat: true,
        interimResults: true,
      }),
      llm: new LLM({ model: "gpt-4o" }),
      tts: new deepgram.TTS({ model: "aura-2-thalia-en" }),
    });

    await session.start({ agent, room: ctx.room });

    await session.generateReply({
      instructions: "Greet the user and ask how you can help.",
    });
  },
});

cli.runApp(new ServerOptions({ agent: fileURLToPath(import.meta.url) }));
```

## Run the Agent

Start the agent in development mode. The `dev` flag connects the agent to your LiveKit Cloud project and automatically registers it to handle incoming sessions:

```bash title="Python"
python agent.py dev
```

```bash title="Node.js"
npx tsx agent.ts dev
```

## Test the Agent

LiveKit provides the [Agents Playground](https://agents-playground.livekit.io/) — a browser-based tool for testing agents. It includes video, chat, and other features, but for this tutorial you only need the microphone.

1. Go to [agents-playground.livekit.io](https://agents-playground.livekit.io/)
2. Enter your LiveKit Cloud URL and a participant token, then connect
3. Allow microphone access when prompted
4. Start talking — the agent should respond in real time

You can generate a participant token from the [LiveKit dashboard](https://cloud.livekit.io) or using the LiveKit CLI.

The agent greets you automatically on connect. Silero VAD detects when you stop speaking and triggers the STT-to-LLM-to-TTS pipeline. You can interrupt the agent mid-sentence — VAD handles barge-in automatically.

## Further Reading

* [Deepgram Voice Agent API](/docs/voice-agent) — build voice agents without an external LLM or transport layer
* [LiveKit Agents Documentation](https://docs.livekit.io/agents/) — LiveKit's agent framework reference
