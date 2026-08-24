---
title: "Sound Effects quickstart"
source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/sound-effects.md
path: docs/eleven-api/guides/cookbooks/sound-effects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Sound Effects quickstart

This guide will show you how to generate sound effects using the Sound Effects API.

Use the [ElevenLabs sound-effects skill](https://github.com/elevenlabs/skills/tree/main/sound-effects) to generate sound effects from your AI coding assistant:

```bash
npx skills add elevenlabs/skills --skill sound-effects
```

## Using the Sound Effects API

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

To play the audio through your speakers, you may be prompted to install [MPV](https://mpv.io/)
and/or [ffmpeg](https://ffmpeg.org/).

#### Make the API request

#### SDK

Create a new file named `example.py` or `example.mts`, depending on your language of choice and add the following code:

```python maxLines=0
# example.py
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)
audio = elevenlabs.text_to_sound_effects.convert(text="Cinematic Braam, Horror")

play(audio)
```

```typescript
// example.mts
import { ElevenLabsClient, play } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const audio = await elevenlabs.textToSoundEffects.convert({
  text: "Cinematic Braam, Horror",
});

await play(audio);
```

Then run it:

```python
python example.py
```

```typescript
npx tsx example.mts
```

You should hear your generated sound effect playing through your speakers.

#### CLI

Generate a sound effect and save it to a file:

```bash
elevenlabs text-to-sound-effects convert \
  --text "Cinematic Braam, Horror" \
  --output sound-effect.mp3
```

Open `sound-effect.mp3` to hear the result.

## Next steps

#### [Sound effects overview](/docs/overview/capabilities/sound-effects)

Learn about sound effect generation, supported formats, and use cases

#### [Text to Speech](/docs/eleven-api/quickstart)

Generate spoken audio from text with the Text to Speech API

#### [API reference](/docs/api-reference/text-to-sound-effects/convert)

Explore all Sound Effects parameters and response formats
