---
title: "ElevenLabs Documentation"
source: https://elevenlabs.io/docs/overview/intro.md
path: docs/overview/intro
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenLabs Documentation

> ElevenLabs API docs for text to speech, speech to text and voice agents, with Python and TypeScript SDKs, model guides, quickstarts and API reference.

> **Tip**
>
> Get started with your coding agent. No account or API key needed beforehand.
>
> Paste this into Claude Code, Cursor or Codex. It signs you in or creates an account, creates a key, and adds the SDK to your project.
>
> ```text
> Add ElevenLabs to my project: run `npx -y @elevenlabs/cli@latest onboard init` and follow what it prints.
> ```
>
> [See how it works](/docs/eleven-api/quickstart#set-up-with-your-coding-agent), or read the [`onboard` command's source](https://github.com/elevenlabs/cli/tree/main/cli/elevenlabs/workflow/onboard) to see exactly what it tells your agent.

## How does ElevenLabs work?

ElevenLabs provides AI voice infrastructure: text-to-speech, speech-to-text, voice cloning, voice agents, and generative audio. You can use it in four ways, suited to different audiences.

**[ElevenCreative](/docs/eleven-creative)** is a no-code web application where creators, producers, and editors generate voiceovers, music, dubs, and studio projects directly in the browser.

**[ElevenAgents](/docs/eleven-agents)** is the platform for designing and operating voice agents, with a visual builder for non-technical users and full programmatic control for developers.

**[ElevenAPI](/docs/eleven-api)** exposes every capability as a REST interface with official Python and TypeScript SDKs, so developers can embed voice into their own applications and workflows.

**[Reception.ai](/docs/reception-ai)** is a ready-to-deploy AI phone receptionist for small and medium businesses that answers calls, books appointments, and manages day-to-day operations from a single dashboard.

## Choose your path

[![](/docs/_fern-img/12097a437e55f60c199946cf59c9528eb8349d110142394833d67fe93b50e68d.webp)](/docs/eleven-creative/overview)

### ElevenCreative

Learn how to use the ElevenCreative platform with step-by-step guides

[![](/docs/_fern-img/7375358c43ac5dd1a170937123f0874e01b3d8b6cf178c282805588a11d39593.webp)](/docs/eleven-agents/overview)

### ElevenAgents

Learn how to build, launch, and scale agents with ElevenLabs

[![](/docs/_fern-img/002b2432fa6ab18befc9f1a6e7fadf348f46506a5a5a72a2358ba1e7f92d8ded.webp)](/docs/eleven-api/quickstart)

### ElevenAPI

Learn how to integrate with the ElevenLabs API with examples and tutorials

## Concepts

**Voices** are the speech persona used in audio generation. Each voice has a unique ID — for example, `JBFqnCBsd6RMkjVDRZzb` — that you select in the dashboard or pass in API requests. ElevenLabs maintains a [library of 10,000+ voices](https://elevenlabs.io/app/voice-library). You can also clone a voice from an audio recording or generate one from a text description.

**Models** control the quality, latency, and language coverage of generated audio. [`eleven_v4`](/docs/overview/models) produces the most expressive output across 90+ languages. [`eleven_v4_turbo`](/docs/overview/models) targets real-time use at median inference latency of \~100ms. Each capability — speech-to-text, music, sound effects — has its own dedicated model. See [Which model should I use?](#which-model-should-i-use) to pick one.

## How does pricing work?

**Credits** are the unit of consumption shared across every product. Text-to-speech costs one credit per character of input text. Other operations are charged per second of audio processed. Credits reset monthly and unused credits roll over for up to two months. See [pricing](https://elevenlabs.io/pricing/api) for a full breakdown.

To use the API without a monthly subscription, [Pay As You Go](/docs/overview/administration/pay-as-you-go) lets you prepay a balance that is drawn down as you use ElevenLabs, after any subscription credits are used up.

## Built for production

### How fast is ElevenLabs text to speech?

Eleven Flash v2.5 generates audio with \~75ms of model inference latency, and Eleven v4 Turbo with a median of \~100ms. Scribe v2 Realtime returns partial transcripts in \~150ms. These figures exclude application and network latency, so the time until your users hear audio is higher. [Understanding latency](/docs/eleven-api/concepts/latency) explains what the figures cover, and [Latency optimization](/docs/eleven-api/guides/how-to/best-practices/latency-optimization) covers how to reduce end-to-end latency.

### How does ElevenLabs handle scale?

Your plan sets how many requests are processed at the same time. A concurrency limit is not a cap on simultaneous conversations: as a rule of thumb, a limit of 5 can typically support around 100 simultaneous audio broadcasts, depending on the voices used and the use case. Enterprise plans have elevated limits. See [Concurrency and priority](/docs/overview/models#concurrency-and-priority) for per-plan limits and load testing guidance.

### Enterprise controls

* **[Private deployments](/docs/overview/capabilities/private-deployment)** run ElevenAgents, Text to Speech and Speech to Text inside your own cloud account, so text, audio and transcripts stay in your network.
* **[Data residency](/docs/overview/administration/data-residency)** stores your data in isolated environments in the EU, India or Singapore instead of the default U.S. location. It is an Enterprise feature.
* **[Workspaces](/docs/overview/administration/workspaces/overview)** centralize billing, shared resources, team access and API key management. Enterprise workspaces add [SSO](/docs/overview/administration/workspaces/sso) over SAML 2.0 or OIDC, and [audit logs](/docs/overview/administration/workspaces/audit-logs) of administrative actions in the OCSF schema.

## Generate your first audio

Install the SDK, set your API key as an environment variable, and convert text to an MP3 file in a single request. To have your coding agent do this setup instead, see [Set up with your coding agent](/docs/eleven-api/quickstart#set-up-with-your-coding-agent).

#### Install the SDK

**`Python`**

```bash title="Python"
pip install elevenlabs python-dotenv
```

**`TypeScript`**

```bash title="TypeScript"
npm install @elevenlabs/elevenlabs-js dotenv
```

#### Set your API key

[Create an API key](https://elevenlabs.io/app/settings/api-keys) and add it to a `.env` file in your project directory:

**`.env`**

```js title=".env"
ELEVENLABS_API_KEY=<your_api_key_here>
```

#### Generate and save audio

```python
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",  # "George" - browse voices at elevenlabs.io/app/voice-library
    model_id="eleven_v4",
    output_format="mp3_44100_128",
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import { writeFile } from "node:fs/promises";

const elevenlabs = new ElevenLabsClient();
const audio = await elevenlabs.textToSpeech.convert(
  "JBFqnCBsd6RMkjVDRZzb", // "George" - browse voices at elevenlabs.io/app/voice-library
  {
    text: "The first move is what sets everything in motion.",
    modelId: "eleven_v4",
    outputFormat: "mp3_44100_128",
  }
);

await writeFile("output.mp3", Buffer.from(await new Response(audio).arrayBuffer()));

```

Run the script with `python example.py` or `npx tsx example.mts`, then open `output.mp3`. To do the same from the terminal, use the [ElevenLabs CLI](/docs/eleven-api/quickstart):

```bash
elevenlabs text-to-speech convert \
  --voice-id JBFqnCBsd6RMkjVDRZzb \
  --model-id eleven_v4 \
  --text "The first move is what sets everything in motion." \
  --output-format mp3_44100_128 \
  --output output.mp3
```

The [ElevenAPI quickstart](/docs/eleven-api/quickstart) covers the same request in more detail, including CLI setup and playing audio through your speakers.

## What can I build with ElevenAgents?

ElevenAgents combines speech recognition, an LLM of your choice, text to speech and turn-taking into a single voice agent that you configure in the dashboard or through the SDKs.

* **Customer support**: answer questions from your own documentation by attaching a [knowledge base](/docs/eleven-agents/customization/knowledge-base) to the agent.
* **Phone lines**: connect a Twilio number with the [native integration](/docs/eleven-agents/phone-numbers/twilio-integration/native-integration) to handle inbound and outbound calls, or bring your existing phone system over SIP trunking.
* **Outbound campaigns**: place many outbound calls at once with [batch calling](/docs/eleven-agents/phone-numbers/batch-calls).
* **Websites and apps**: embed an agent that handles both voice and text with the [widget](/docs/eleven-agents/customization/widget).

The [ElevenAgents quickstart](/docs/eleven-agents/quickstart) builds a first agent end to end.

## Which model should I use?

Start from your use case. Each model ID below is the value to pass as `model_id` in API requests.

| Use case                          | Recommended model  | Model ID             | Why                                                                                                                                                                                                        |
| --------------------------------- | ------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Real-time voice agents            | Eleven v4 Turbo    | `eleven_v4_turbo`    | Median inference latency of \~100ms† with the most expressive real-time delivery. For the lowest latency, use `eleven_flash_v2_5` (\~75ms†).                                                               |
| Expressive or long-form narration | Eleven v4          | `eleven_v4`          | The most expressive model, suited to audiobooks and character voiceovers. Up to 10,000 characters (\~10 minutes of audio) per request. For the most stable long-form output, use `eleven_multilingual_v2`. |
| Multilingual content              | Eleven v4          | `eleven_v4`          | 90+ languages with consistent voice quality across language switches. `eleven_v4_turbo` covers the same languages in real time.                                                                            |
| Lowest cost                       | Eleven Flash v2.5  | `eleven_flash_v2_5`  | 50% lower price per character for API generations, 32 languages, and up to 40,000 characters per request.                                                                                                  |
| Speech to text, batch             | Scribe v2          | `scribe_v2`          | Transcription in 90+ languages with word-level timestamps, speaker diarization for up to 32 speakers, and keyterm prompting. Use `scribe_v2_medical` for clinical audio.                                   |
| Speech to text, realtime          | Scribe v2 Realtime | `scribe_v2_realtime` | Streams transcripts with \~150ms† latency in 90+ languages.                                                                                                                                                |

See [Choosing the right model](/docs/eleven-api/choosing-the-right-model) for more use cases and the [models reference](/docs/overview/models) for full specifications.

#### [Eleven v4](/docs/overview/models#eleven-v4)

Our most emotive, high quality speech synthesis model

Exceptional voice cloning capabilities

90+ languages supported

10,000 character limit

Support for natural multi-speaker dialogue

#### [Eleven v4 Turbo](/docs/overview/models#eleven-v4-turbo)

Our most emotive, real-time speech synthesis model

Ultra-low latency (median inference latency of \~100ms†)

Exceptional voice cloning capabilities

90+ languages supported

Audio tags for fine-grained control

#### [Eleven v3](/docs/overview/models#eleven-v3)

Our emotionally rich, expressive speech synthesis model

Dramatic delivery and performance

70+ languages supported

5,000 character limit

Support for natural multi-speaker dialogue

#### [Eleven v3 Conversational](/docs/overview/models#eleven-v3-conversational)

Our expressive, realtime speech synthesis model

Low latency (\~280ms)

Dramatic delivery and performance

70+ languages supported

Audio tags for fine-grained control

#### [Eleven Multilingual v2](/docs/overview/models#multilingual-v2)

Lifelike, consistent quality speech synthesis model

Natural-sounding output

29 languages supported

10,000 character limit

Most stable on long-form generations

#### [Eleven Flash v2.5](/docs/overview/models#flash-v25)

Our fast, affordable speech synthesis model

Ultra-low latency (\~75ms†)

32 languages supported

40,000 character limit

Faster model, 50% lower price per character for API generations

#### [Scribe v2](/docs/overview/models#scribe-v2)

State-of-the-art speech recognition model

Accurate transcription in 90+ languages

Keyterm prompting, up to 1000 terms

Entity detection, 65 entity types

Transcript editing with natural-language instructions

Precise word-level timestamps

Speaker diarization, up to 32 speakers

Dynamic audio tagging

Smart language detection

#### [Scribe v2 Realtime](/docs/overview/models#scribe-v2-realtime)

Real-time speech recognition model

Accurate transcription in 90+ languages

Real-time transcription

Low latency (\~150ms†)

Precise word-level timestamps

Entity detection, 65 entity types

Transcript editing with natural-language instructions

#### [Scribe v2 Medical](/docs/overview/models#scribe-v2-medical)

Speech recognition fine-tuned for clinical audio

35% fewer transcription errors on clinical audio than Scribe v2

Same accuracy on everyday speech as Scribe v2

Same features, languages, pricing, and API as Scribe v2

[Explore all](/docs/overview/models)

† Excluding application & network latency. See [Understanding latency](/docs/eleven-api/concepts/latency).

## Browse by capability

Text to Speech

Convert text into lifelike speech

Speech to Text

Transcribe spoken audio into text

Music

Generate music from text

Text to Dialogue

Create natural-sounding dialogue from text

Image & Video

Generate images and videos from text

Voice changer

Modify and transform voices

Voice isolator

Isolate voices from background noise

Dubbing

Dub audio and videos seamlessly

Sound effects

Create cinematic sound effects

Voices

Clone and design custom voices

Voice Remixing

Transform and enhance existing voices

Forced Alignment

Align text to audio

Speech Engine

Add voice to anything

ElevenAgents

Deploy intelligent voice agents

Private deployments

Run ElevenLabs in your own cloud
