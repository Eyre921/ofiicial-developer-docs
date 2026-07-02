---
title: "Build a Voice Agent with Pipecat and Deepgram"
source: https://developers.deepgram.com/docs/build-voice-agent-with-pipecat-and-deepgram.md
path: docs/build-voice-agent-with-pipecat-and-deepgram
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with Pipecat and Deepgram

> Build a real-time voice agent with Pipecat for pipeline orchestration, Deepgram Nova-3 for speech-to-text, and Deepgram Aura for text-to-speech.

If you already use [Pipecat](https://pipecat.ai/) for voice AI pipelines, you can add Deepgram's speech-to-text and text-to-speech models to your Pipecat agent. Pipecat's pipeline architecture connects separate STT, LLM, and TTS services, so this guide pairs Deepgram's audio models with OpenAI for language understanding — though any Pipecat-compatible LLM works.

For a standalone voice agent without Pipecat or an external LLM, see the [Deepgram Voice Agent API](/docs/voice-agent), which bundles STT, LLM routing, and TTS in a single WebSocket connection.

For a CLI-scaffolded approach using `pipecat init`, see the [Pipecat and Deepgram integration guide](/docs/pipecat-integration).

## Before You Begin

This guide assumes you are familiar with Python and have a basic understanding of how voice agents work.

You'll need a [Deepgram account](https://console.deepgram.com/signup?jump=keys) and an API key. Signup is free and includes **\$200** in credit.

### Get OpenAI Credentials

This tutorial uses OpenAI for its LLM. You'll need to [sign up for an OpenAI account](https://platform.openai.com/signup/) and obtain an [API key](https://platform.openai.com/api-keys).

### Requirements

* Python 3.11+

## Set Up Your Project

This implementation is a starting reference for building your own voice agent with Pipecat and Deepgram. It is not designed for production deployments.

Create a new directory, set up a virtual environment, and install Pipecat with the Deepgram, OpenAI, and runner extras:

```bash
mkdir deepgram-pipecat-agent
cd deepgram-pipecat-agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install "pipecat-ai[deepgram,openai,silero,webrtc]" python-dotenv
```

The `runner` extra includes a built-in WebRTC transport with a browser-based test client — no external account needed.

## Set Environment Variables

Create a `.env` file in your project root with the credentials you collected earlier. The agent reads these at startup to authenticate with each service:

```
DEEPGRAM_API_KEY=your_deepgram_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Build the Agent

The agent creates a pipeline that connects audio input to Deepgram for transcription, OpenAI for a response, and Deepgram again for speech synthesis. Pipecat handles the audio transport, turn-taking, and interruption detection.

The key components are:

* **`Pipeline`** — connects frame processors in sequence: transport input, STT, context aggregation, LLM, TTS, and transport output.
* **`LLMContextAggregatorPair`** — manages conversation context and uses Silero VAD to detect when the user starts and stops speaking.
* **`LLMRunFrame`** — triggers the LLM to generate a response. Used here to make the agent greet the user on connect.

Create `bot.py`:

```python
# bot.py

import os

from dotenv import load_dotenv

from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.frames.frames import LLMRunFrame
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask
from pipecat.processors.aggregators.llm_context import LLMContext
from pipecat.processors.aggregators.llm_response_universal import (
    LLMContextAggregatorPair,
    LLMUserAggregatorParams,
)
from pipecat.runner.types import RunnerArguments
from pipecat.runner.utils import create_transport
from pipecat.services.deepgram.stt import DeepgramSTTService
from pipecat.services.deepgram.tts import DeepgramTTSService
from pipecat.services.openai.llm import OpenAILLMService
from pipecat.transports.base_transport import BaseTransport, TransportParams

load_dotenv(override=True)

transport_params = {
    "webrtc": lambda: TransportParams(
        audio_in_enabled=True,
        audio_out_enabled=True,
    ),
}


async def run_bot(transport: BaseTransport, runner_args: RunnerArguments):
    stt = DeepgramSTTService(
        api_key=os.getenv("DEEPGRAM_API_KEY"),
        settings=DeepgramSTTService.Settings(
            model="nova-3-general",
            language="en",
            punctuate=True,
            smart_format=True,
        ),
    )

    llm = OpenAILLMService(
        api_key=os.getenv("OPENAI_API_KEY"),
        settings=OpenAILLMService.Settings(
            model="gpt-4o",
            system_instruction=(
                "You are a friendly, helpful voice assistant. "
                "Keep your responses concise — aim for 1-3 sentences "
                "unless the user asks for detail. "
                "Your responses will be spoken aloud, so avoid emojis, "
                "bullet points, or other formatting that can't be spoken."
            ),
        ),
    )

    tts = DeepgramTTSService(
        api_key=os.getenv("DEEPGRAM_API_KEY"),
        settings=DeepgramTTSService.Settings(
            voice="aura-2-thalia-en",
        ),
    )

    context = LLMContext()

    user_aggregator, assistant_aggregator = LLMContextAggregatorPair(
        context,
        user_params=LLMUserAggregatorParams(
            vad_analyzer=SileroVADAnalyzer(),
        ),
    )

    pipeline = Pipeline([
        transport.input(),
        stt,
        user_aggregator,
        llm,
        tts,
        transport.output(),
        assistant_aggregator,
    ])

    task = PipelineTask(
        pipeline,
        params=PipelineParams(
            enable_metrics=True,
            enable_usage_metrics=True,
        ),
    )

    @transport.event_handler("on_client_connected")
    async def on_client_connected(transport, client):
        context.add_message(
            {"role": "developer", "content": "Greet the user and ask how you can help."}
        )
        await task.queue_frames([LLMRunFrame()])

    @transport.event_handler("on_client_disconnected")
    async def on_client_disconnected(transport, client):
        await task.cancel()

    runner = PipelineRunner(handle_sigint=runner_args.handle_sigint)
    await runner.run(task)


async def bot(runner_args: RunnerArguments):
    transport = await create_transport(runner_args, transport_params)
    await run_bot(transport, runner_args)


if __name__ == "__main__":
    from pipecat.runner.run import main

    main()
```

### How the pipeline works

Audio flows through the pipeline from left to right:

1. **`transport.input()`** captures microphone audio from the browser.
2. **`stt`** (Deepgram Nova-3) transcribes audio into text in real-time.
3. **`user_aggregator`** collects transcription frames and uses Silero VAD to detect when the user finishes speaking, then adds the complete utterance to the conversation context.
4. **`llm`** (OpenAI GPT-4o) generates a text response based on the conversation context.
5. **`tts`** (Deepgram Aura) converts the response text to speech.
6. **`transport.output()`** sends the audio back to the browser.
7. **`assistant_aggregator`** records the assistant's response in the conversation context for future turns.

When a user speaks over the agent, Silero VAD detects the interruption and cancels the current TTS output so the agent stops and listens.

## Run the Agent

Start the agent with the WebRTC transport. The `-t webrtc` flag launches a built-in browser client for testing:

```bash
python bot.py -t webrtc
```

The first run takes about 20 seconds to download the Silero VAD model. Subsequent starts are faster.

## Test the Agent

Once the agent is running, open [http://localhost:7860/client](http://localhost:7860/client) in your browser.

1. Allow microphone access when prompted
2. Click to connect — the agent greets you automatically
3. Start talking — the agent responds in real time

Try interrupting the agent mid-sentence. Silero VAD detects your speech and cancels the current response so the agent listens to you instead.

## Further Reading

* [Deepgram Voice Agent API](/docs/voice-agent) — build voice agents without an external LLM or transport layer
* [Pipecat and Deepgram Integration Guide](/docs/pipecat-integration) — scaffold a project with the Pipecat CLI
* [Pipecat Documentation](https://docs.pipecat.ai) — Pipecat's framework reference
