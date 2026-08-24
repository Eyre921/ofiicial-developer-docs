---
title: "Speech to Text quickstart"
source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/speech-to-text.md
path: docs/eleven-api/guides/cookbooks/speech-to-text
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Speech to Text quickstart

This guide will show you how to convert spoken audio into text using the Speech to Text API.

Use the [ElevenLabs speech-to-text skill](https://github.com/elevenlabs/skills/tree/main/speech-to-text) to transcribe audio from your AI coding assistant:

```bash
npx skills add elevenlabs/skills --skill speech-to-text
```

This tutorial will demonstrate how to use the Batch Speech to Text API. For a guide on how to use
the Realtime Speech to Text API, see the [Client-side
streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming) or
[Server-side
streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming) guides.

## Using the Speech to Text API

#### Create an API key

[Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

```js title=".env"
ELEVENLABS_API_KEY=<your_api_key_here>
```

#### Install the SDK

#### SDK

We'll also use the `dotenv` library to load our API key from an environment variable.

```python
pip install elevenlabs
pip install python-dotenv
```

```typescript
npm install @elevenlabs/elevenlabs-js
npm install dotenv
```

#### CLI

Install the ElevenLabs CLI. Homebrew (macOS) and Scoop (Windows) are recommended.

```bash title="Homebrew (macOS)"
brew install elevenlabs/tap/elevenlabs
```

```powershell title="Scoop (Windows)"
scoop bucket add elevenlabs https://github.com/elevenlabs/scoop-bucket
scoop install elevenlabs
```

```bash title="curl"
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/elevenlabs/cli/releases/latest/download/elevenlabs-cli-installer.sh | sh
```

Working with an AI coding assistant? Run `elevenlabs generate-skills` in your project to write a
`SKILL.md` for every command group into `skills/`, so your assistant knows the CLI's full surface
without you pasting docs. Use `--output-dir` to put them elsewhere. This reads the CLI's own
embedded API definition, so it needs no API key and works offline — and it stays in step with
whichever CLI version you have installed.

Then authenticate — this opens your browser to authorize the CLI:

```bash
elevenlabs auth login
```

#### Make the API request

#### SDK

Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

```python maxLines=0
# example.py
import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_url = (
    "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
)
response = requests.get(audio_url)
audio_data = BytesIO(response.content)

transcription = elevenlabs.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v2", # Model to use
    tag_audio_events=True, # Tag audio events like laughter, applause, etc.
    language_code="eng", # Language of the audio file. If set to None, the model will detect the language automatically.
    diarize=True, # Whether to annotate who is speaking
)

print(transcription)
```

```typescript maxLines=0
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const response = await fetch(
  "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
);
const audioBlob = new Blob([await response.arrayBuffer()], { type: "audio/mp3" });

const transcription = await elevenlabs.speechToText.convert({
  file: audioBlob,
  modelId: "scribe_v2", // Model to use
  tagAudioEvents: true, // Tag audio events like laughter, applause, etc.
  languageCode: "eng", // Language of the audio file. If set to null, the model will detect the language automatically.
  diarize: true, // Whether to annotate who is speaking
});

console.log(transcription);
```

Then run it:

```python
python example.py
```

```typescript
npx tsx example.mts
```

You should see the transcription of the audio file printed to the console.

#### CLI

Download the sample audio, then transcribe it:

```bash
curl -O https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3

elevenlabs speech-to-text convert \
  --file nicole.mp3 \
  --model-id scribe_v2 \
  --tag-audio-events true \
  --language-code eng \
  --diarize true
```

The transcription is printed to your terminal.

## Next steps

#### [Batch transcription](/docs/eleven-api/guides/how-to/speech-to-text/batch)

Transcribe pre-recorded audio files with speaker diarization and event tagging

#### [Realtime transcription](/docs/eleven-api/guides/how-to/speech-to-text/realtime)

Stream audio and receive transcriptions in real time

#### [API reference](/docs/api-reference/speech-to-text/convert)

Explore all Speech to Text parameters and response formats
