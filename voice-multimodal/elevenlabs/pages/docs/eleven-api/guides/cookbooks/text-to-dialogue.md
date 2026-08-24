---
title: "Text to Dialogue quickstart"
source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue.md
path: docs/eleven-api/guides/cookbooks/text-to-dialogue
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Text to Dialogue quickstart

This guide will show you how to generate immersive, natural-sounding dialogue from text using the Text to Dialogue API.

Keep the total length of all `inputs[].text` values at or below 2,000 characters per request for
reliable generation. Split longer scripts into chunks and stitch the audio client-side.

## Using the Text to Dialogue API

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

Create a new file named `example.py` or `example.mts`, depending on your language of choice, and add the following code.
Add audio tags inside each `text` value to guide that speaker's delivery. The `voice_id`
selects the speaker voice for the same input item.

```python focus={12-21} maxLines=0
# example.py
import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_dialogue.convert(
    inputs=[
        {
            "text": "[cheerfully] Hello, how are you?",
            "voice_id": "9BWtsMINqrJLrRacOk9x",
        },
        {
            "text": "[stuttering] I'm... I'm doing well, thank you.",
            "voice_id": "IKne3meq5aSn9XLyUdCD",
        }
    ]
)

play(audio)
```

```typescript focus={7-17} maxLines=0
// example.mts
import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const audio = await elevenlabs.textToDialogue.convert({
    inputs: [
        {
            text: "[cheerfully] Hello, how are you?",
            voiceId: "9BWtsMINqrJLrRacOk9x",
        },
        {
            text: "[stuttering] I'm... I'm doing well, thank you.",
            voiceId: "IKne3meq5aSn9XLyUdCD",
        },
    ],
});

play(audio);
```

Then run it:

```python
python example.py
```

```typescript
npx tsx example.mts
```

You should hear the dialogue audio play.

#### CLI

Pass the dialogue inputs as a JSON array and save the audio to a file:

```bash
elevenlabs text-to-dialogue convert \
  --output dialogue.mp3 \
  --inputs '[
    { "text": "[cheerfully] Hello, how are you?", "voice_id": "9BWtsMINqrJLrRacOk9x" },
    { "text": "[stuttering] I... I am doing well, thank you.", "voice_id": "IKne3meq5aSn9XLyUdCD" }
  ]'
```

Open `dialogue.mp3` to hear the result.

## WebSocket streaming

For incremental dialogue over a long-lived connection with **Eleven v3** models, follow [Realtime Text to Dialogue](/docs/eleven-api/guides/how-to/websockets/realtime-tdd). To compare this WebSocket with the standard TTS WebSocket, see [Text to Speech vs Text to Dialogue WebSockets](/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets).

## Next steps

#### [Browse voices](https://elevenlabs.io/app/voice-library)

Explore 10,000+ voices to assign to each dialogue speaker

#### [Text to Speech](/docs/eleven-api/guides/cookbooks/text-to-speech)

Generate speech from a single voice with the Text to Speech API

#### [API reference](/docs/api-reference/text-to-dialogue/convert)

Explore all Text to Dialogue parameters and response formats
