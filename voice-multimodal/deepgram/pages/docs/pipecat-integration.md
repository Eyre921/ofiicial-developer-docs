---
title: "Pipecat and Deepgram"
source: https://developers.deepgram.com/docs/pipecat-integration.md
path: docs/pipecat-integration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Pipecat and Deepgram

This guide walks you through building a voice AI agent that uses [Pipecat](https://pipecat.ai) for pipeline orchestration and Deepgram for speech-to-text (STT) and text-to-speech (TTS). By the end, you have a working voice agent that listens to a user, generates a response with an LLM, and speaks back in real-time.

Pipecat is an open-source Python framework for building voice and multimodal AI agents. It connects STT, LLM, and TTS services into a real-time pipeline and handles audio transport, turn-taking, and interruption detection.

## Before you begin

Before you can use Deepgram, you need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes \$200 in credit.

Daily is the WebRTC transport layer that handles audio between the browser and your agent. See the [Pipecat Daily transport guide](https://docs.pipecat.ai/server/services/transport/daily) for more.

You need:

* A [Deepgram API key](https://console.deepgram.com/)
* A [Daily API key](https://docs.pipecat.ai/api-reference/server/services/transport/daily#prerequisites)
* An LLM API key — this guide uses [OpenAI](https://platform.openai.com/api-keys), but Pipecat supports [other providers](https://docs.pipecat.ai/pipecat/learn/llm#supported-llm-services) including Anthropic, Google, and Groq
* [uv](https://docs.astral.sh/uv/) installed (for dependency management)
* The [Pipecat CLI](https://docs.pipecat.ai/cli/overview) installed
* Python 3.11+
* Node.js 18+ (only if you add a JavaScript or React Pipecat client later)

Install or update the Pipecat CLI:

```bash
uv tool install pipecat-ai-cli
```

To update the CLI use:

```bash
uv tool update pipecat-ai-cli
```

### Choose your developer experience

Creating a Pipecat + Deepgram integration can be accomplished by using several approaches. Choose the developer experience from the guides below that best fits your style. Note that all paths share the same prerequisite: the Pipecat CLI.

1. [Build with a Coding Agent](#build-with-a-coding-agent)
2. [Use the quickstart CLI command](#use-the-quickstart-cli-command)
3. [Scaffold a new Pipecat project with the CLI](#scaffold-a-new-pipecat-project-with-the-cli)

## Build with a Coding Agent

You can use AI coding tools like Claude Code or Codex to generate your Pipecat agent code. Rather than relying on the tool's training data, you give it live context from the Pipecat documentation.

1. Follow the [Pipecat getting started guide](https://docs.pipecat.ai/pipecat/get-started/ai-tools) to set up AI tools, connect the Pipecat Context Hub, and initialize a project.
2. Start a coding session with a prompt like the example below.

```text
I'm building a phone assistant for my flower shop, Field & Flower, that
takes customer orders.

The bot should be able to:
  - list the available bouquets
  - check if a specific flower is in stock
  - add a flower to the order
  - get a summary of the order
  - set the delivery details
  - place the order
  - end the call

When the call starts, the bot greets the caller with exactly:
"This is Field & Flower, your local flower shop. How can I help you today?"

Services:
  - Twilio for phone calls
  - STT: Deepgram
  - LLM: OpenAI
  - TTS: Deepgram Flux
  - Deploy to Pipecat Cloud

This is a demo: use a mock backend for the flower data, and "place the
order" only needs to log the order.
```

The `init` command creates a **GETTING\_STARTED.md** file with additional guidance for your coding agent.

## Use the quickstart CLI command

The quickstart uses Deepgram for STT but Cartesia for TTS. Follow the instruction from the [Pipecat Quickstart documentation](https://docs.pipecat.ai/pipecat/get-started/quickstart), then switch to Deepgram using the steps below.

To switch TTS to Deepgram, open `bot.py` and find the Cartesia TTS setup:

```python
# Remove this:
from pipecat.services.cartesia.tts import CartesiaTTSService

tts = CartesiaTTSService(
    api_key=os.getenv("CARTESIA_API_KEY"),
    settings=CartesiaTTSService.Settings(
        voice="71a7ad14-091c-4e8e-a314-022ece01c121",
    ),
)
```

Replace it with:

```python
from pipecat.services.deepgram.tts import DeepgramTTSService

tts = DeepgramTTSService(
    api_key=os.getenv("DEEPGRAM_API_KEY"),
    settings=DeepgramTTSService.Settings(
        voice="aura-2-helena-en",
    ),
)
```

You can also remove `CARTESIA_API_KEY` from your `.env` file since it is no longer needed. No other changes are required. The STT service already uses Deepgram and the rest of the pipeline stays the same.

Continue building by adding a [Pipecat Client](#next-steps)

### Use Flux for turn detection

[Flux](/docs/flux/quickstart) is Deepgram's conversational STT model with built-in turn detection. It uses acoustic and semantic cues to determine when a speaker has finished their turn, resulting in more natural conversations.

To use Flux, replace `DeepgramSTTService` with `DeepgramFluxSTTService` in your `bot.py`:

```python
import os

from pipecat.services.deepgram.flux.stt import DeepgramFluxSTTService

stt = DeepgramFluxSTTService(
    api_key=os.getenv("DEEPGRAM_API_KEY"),
    settings=DeepgramFluxSTTService.Settings(
        min_confidence=0.3,
    ),
)
```

Since Deepgram Flux provides its own user turn start and end detection, you should use ExternalUserTurnStrategies to let Flux handle turn management. See [User Turn Strategies](https://docs.pipecat.ai/api-reference/server/utilities/turn-management/user-turn-strategies) for configuration details.

```python
from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.turns.user_turn_strategies import ExternalUserTurnStrategies
from pipecat.processors.aggregators.llm_response_universal import (
    LLMContextAggregatorPair,
    LLMUserAggregatorParams,
)

user_aggregator, assistant_aggregator = LLMContextAggregatorPair(
    context,  # the existing LLMContext from your bot.py
    user_params=LLMUserAggregatorParams(
        user_turn_strategies=ExternalUserTurnStrategies(),
        vad_analyzer=SileroVADAnalyzer(),
    ),
)
```

## Scaffold a new Pipecat project with the CLI

### Step 1: Create the project

Scaffold a new project using the Pipecat CLI.

```bash
pipecat init

Project directory [pipecat-bot]: [enter]
✔ Wrote pipecat-bot/AGENTS.md
✔ Wrote pipecat-bot/GETTING_STARTED.md
✔ Wrote pipecat-bot/CLAUDE.md
```

```bash
cd pipecat-bot

pipecat create --name pipecat-deepgram --bot-type web --transport daily --mode cascade --stt deepgram_flux_stt --llm openai_llm --tts deepgram_tts --no-deploy-to-cloud
```

### Step 2: Install dependencies

Navigate to the `server` directory inside your new project, create a virtual environment, and install the dependencies:

```bash
cd pipecat-deepgram/server
uv sync
```

### Step 3: Configure your environment

Copy the example environment file and fill in your API keys and set the default Deepgram voice:

```bash
cp .env.example .env
```

Replace the placeholder values with your API keys:

* **DEEPGRAM\_API\_KEY** — from your [Deepgram Console](https://console.deepgram.com/)
* **DEEPGRAM\_VOICE\_ID**=aura-2-thalia-en — See: [Deepgram Voices & Languages](https://developers.deepgram.com/docs/tts-models) for a full list of options. **Leaving this value empty may result in a 400 error.**
* **OPENAI\_API\_KEY** — from your [OpenAI dashboard](https://platform.openai.com/api-keys)
* **DAILY\_API\_KEY** — from your [Daily dashboard](https://dashboard.daily.co/u/signup). Daily is the WebRTC transport layer that handles audio between the browser and your agent. See the [Pipecat Daily transport guide](https://docs.pipecat.ai/server/services/transport/daily) for more.

The remaining values are defaults you can change later.

### Step 4: Run the agent

Start the bot from the `server` directory:

```bash
uv run python bot.py --transport daily
```

### Step 5: Test the conversation

Open the local URL printed in your terminal, then:

1. Select **Daily** from the Transport list and click **Connect**.
2. Allow microphone access and speak to your agent.
3. Ask a question and confirm the agent responds with speech.
4. Speak while the agent is talking — it should stop and listen.
5. Pause after speaking — the agent should detect the end of your turn and respond.

Continue building by adding a [Pipecat Client](#next-steps)

## Next Steps

Continue building with an agent.

Follow the [Pipecat getting started guide](https://docs.pipecat.ai/pipecat/get-started/ai-tools) and ready the Pipecat Context Hub.

Prompt your agent to add a [Pipecat client framework](https://docs.pipecat.ai/client/introduction).

Example prompt:

```text
Add a pipecat client for React
```

## Go further with Deepgram

* **Voices** — Deepgram offers 60+ voices across seven languages. Browse the [voice library](/docs/tts-models) and update `DEEPGRAM_VOICE_ID` in your `.env` file.
* **Keyterm prompting** — Improve recognition of domain-specific vocabulary by passing [keyterms](/docs/keyterm) to Nova-3 via the STT service settings.
* **Speaker diarization** — Assign a speaker identifier to each word in the transcript using [diarization](/docs/diarization) via the STT service settings.
* **Dynamic STT settings** — Pipecat supports updating Deepgram STT settings without reconnecting. See the [Pipecat Deepgram STT guide](https://docs.pipecat.ai/server/services/stt/deepgram) for details.

## Resources

* [Deepgram Models & Languages](/docs/models-languages-overview)
* [Deepgram TTS Voices](/docs/tts-models)
* [Pipecat Documentation](https://docs.pipecat.ai)
* [Pipecat Deepgram STT Guide](https://docs.pipecat.ai/server/services/stt/deepgram)
* [Pipecat Deepgram TTS Guide](https://docs.pipecat.ai/server/services/tts/deepgram)
* [pipecat-ai on PyPI](https://pypi.org/project/pipecat-ai/)
