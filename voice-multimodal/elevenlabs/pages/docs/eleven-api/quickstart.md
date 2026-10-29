---
title: "ElevenAPI quickstart"
source: https://elevenlabs.io/docs/eleven-api/quickstart.md
path: docs/eleven-api/quickstart
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenAPI quickstart

By the end of this guide you will have ElevenLabs set up in your project and can make your first text to speech request. There are two ways to get there: let your coding agent do the setup, or do it by hand.

For guides covering other capabilities — streaming, voice cloning, speech-to-text — see the [Tutorials](/docs/eleven-api/guides/cookbooks) section.

## Set up with your coding agent

You do not need an account or an API key before you start. Paste this into your coding agent:

```text
Add ElevenLabs to my project: run `npx -y @elevenlabs/cli@latest onboard init` and follow what it prints.
```

The ElevenLabs CLI takes it from there and tells your agent each step. Your browser opens once so you can sign in or create an account and click **Authorize**. The key is saved in your project's env file (`.env.local`, or `.env` in a Python project) and kept out of git; it is never shown in the chat. The agent then asks what you'd like to build, installs the SDK, adds the code to your app, and asks whether to send a test request.

> **Note**
>
> If your agent runs somewhere your browser cannot reach, such as a remote machine over SSH or a
> cloud sandbox, the CLI asks you to [create a key](https://elevenlabs.io/app/api/api-keys?quickstart=true) yourself and paste it into the env
> file, then continues. The command needs [Node.js](https://nodejs.org) for `npx`. Without it,
> [install the ElevenLabs CLI](https://github.com/elevenlabs/cli#installation) with Homebrew (macOS
> and Linux) or Scoop (Windows), or update it if you already have it (`brew upgrade elevenlabs`,
> `scoop update elevenlabs`), and ask your agent to run `elevenlabs onboard init` instead.

## Set up by hand

#### Create an API key

[Create an API key in the dashboard here](https://elevenlabs.io/app/api/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

Store the key as a managed secret and pass it to the SDKs either as an environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

**`.env`**

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

**`Homebrew (macOS)`**

```bash title="Homebrew (macOS)"
brew install elevenlabs/tap/elevenlabs
```

**`Scoop (Windows)`**

```powershell title="Scoop (Windows)"
scoop bucket add elevenlabs https://github.com/elevenlabs/scoop-bucket
scoop install elevenlabs
```

**`npm`**

```bash title="npm"
npm install -g @elevenlabs/cli
```

**`curl`**

```bash title="curl"
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/elevenlabs/cli/releases/latest/download/elevenlabs-cli-installer.sh | sh
```

> **Tip**
>
> Working with an AI coding assistant? Run `elevenlabs generate-skills` in your project to write a
> `SKILL.md` for every command group into `skills/`, so your assistant knows the CLI's full surface
> without you pasting docs. Use `--output-dir` to put them elsewhere. This reads the CLI's own
> embedded API definition, so it needs no API key and works offline — and it stays in step with
> whichever CLI version you have installed.

Then authenticate — this opens your browser to authorize the CLI:

```bash
elevenlabs auth login
```

> **Note**
>
> To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
> and/or [ffmpeg](https://ffmpeg.org/).

#### Make your first request

#### SDK

Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

```python
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
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

play(audio)

```

```typescript
import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();
const audio = await elevenlabs.textToSpeech.convert(
  "JBFqnCBsd6RMkjVDRZzb", // "George" - browse voices at elevenlabs.io/app/voice-library
  {
    text: "The first move is what sets everything in motion.",
    modelId: "eleven_v4",
    outputFormat: "mp3_44100_128",
  }
);

await play(audio);

```

Then run it:

```python
python example.py
```

```typescript
npx tsx example.mts
```

You should hear the audio play through your speakers.

#### CLI

Generate speech and save it to an MP3 file:

```bash
elevenlabs text-to-speech convert \
  --voice-id JBFqnCBsd6RMkjVDRZzb \
  --model-id eleven_v4 \
  --text "The first move is what sets everything in motion." \
  --output-format mp3_44100_128 \
  --output audio.mp3
```

Open `audio.mp3` to hear the result.

## Next steps

#### [Stream audio](/docs/eleven-api/guides/how-to/text-to-speech/streaming)

Reduce latency by streaming audio as it generates rather than waiting for the complete file

#### [Browse voices](https://elevenlabs.io/app/voice-library)

Explore 10,000+ voices and swap the example voice ID for one that fits your use case

#### [Clone a voice](/docs/eleven-api/guides/how-to/voices/instant-voice-cloning)

Create a custom voice from a short audio recording
