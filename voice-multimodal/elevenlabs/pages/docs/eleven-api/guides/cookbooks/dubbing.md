---
title: "Dubbing quickstart"
source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/dubbing.md
path: docs/eleven-api/guides/cookbooks/dubbing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dubbing quickstart

This guide shows you how to dub a media file into another language with the Dubbing API. In this example you create a dubbing project from an English audio file and generate a Spanish dub.

A dubbing project has two parts: a **project**, which holds one source of media and its transcript, and one or more **language targets**, each producing a dubbed output in a single language. You create a project, wait for its source to be transcribed, add a language, then download the finished dub.

## Using the Dubbing API

#### Create an API key

[Create an API key in the dashboard here](https://elevenlabs.io/app/settings/api-keys), which you’ll use to securely [access the API](/docs/api-reference/authentication).

Store the key as a managed secret and pass it to the SDKs either as a environment variable via an `.env` file, or directly in your app’s configuration depending on your preference.

```js title=".env"
ELEVENLABS_API_KEY=<your_api_key_here>
```

#### Install the SDK

We'll also use the `dotenv` library to load our API key from an environment variable.

```python
pip install elevenlabs
pip install python-dotenv
```

```typescript
npm install @elevenlabs/elevenlabs-js
npm install dotenv
```

The Python example uses the `requests` library to download the dubbed audio. Install it
with `pip install requests`.

#### Make the API request

Create a new file named `example.py` or `example.mts`, depending on your language of choice, and add the following code:

```python maxLines=0
# example.py
import os
import time
import requests
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

# 1. Create a project from a source URL
project = elevenlabs.dubbing.project.create(
    source_url="https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3",
    source_language="en",
    reference="Quickstart dub",
)

# 2. Wait for the source media to be transcribed
while True:
    project = elevenlabs.dubbing.project.get(project.project_id)
    if project.status == "ready":
        break
    if project.status == "failed":
        raise RuntimeError("Project preparation failed")
    print("Preparing project...")
    time.sleep(5)

# 3. Add a Spanish language target
language = elevenlabs.dubbing.project.language.create(
    project.project_id,
    target_language="es",
)

# 4. Wait for the dub to finish generating
while True:
    language = elevenlabs.dubbing.project.language.get(
        project.project_id, language.language_id
    )
    if language.status == "completed":
        break
    if language.status == "failed":
        raise RuntimeError("Dub generation failed")
    print("Generating dub...")
    time.sleep(5)

# 5. Download the dubbed audio from the signed URL
audio = requests.get(language.outputs.lossless_audio)
with open("dubbed.wav", "wb") as f:
    f.write(audio.content)

print("Saved dubbed audio to dubbed.wav")
```

```typescript maxLines=0
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import { writeFile } from "fs/promises";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

// 1. Create a project from a source URL
let project = await elevenlabs.dubbing.project.create({
  sourceUrl:
    "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3",
  sourceLanguage: "en",
  reference: "Quickstart dub",
});

// 2. Wait for the source media to be transcribed
while (true) {
  project = await elevenlabs.dubbing.project.get(project.projectId);
  if (project.status === "ready") break;
  if (project.status === "failed") throw new Error("Project preparation failed");
  console.log("Preparing project...");
  await new Promise((resolve) => setTimeout(resolve, 5000));
}

// 3. Add a Spanish language target
let language = await elevenlabs.dubbing.project.language.create(project.projectId, {
  targetLanguage: "es",
});

// 4. Wait for the dub to finish generating
while (true) {
  language = await elevenlabs.dubbing.project.language.get(
    project.projectId,
    language.languageId
  );
  if (language.status === "completed") break;
  if (language.status === "failed") throw new Error("Dub generation failed");
  console.log("Generating dub...");
  await new Promise((resolve) => setTimeout(resolve, 5000));
}

// 5. Download the dubbed audio from the signed URL
const response = await fetch(language.outputs!.losslessAudio!);
const buffer = Buffer.from(await response.arrayBuffer());
await writeFile("dubbed.wav", buffer);

console.log("Saved dubbed audio to dubbed.wav");
```

The download URL in `outputs.lossless_audio` is signed and expires about an hour after it
is issued. Fetch the language again to get a fresh URL if it has expired.

#### Execute the code

```python
python example.py
```

```typescript
npx tsx example.mts
```

The dubbed audio is saved to `dubbed.wav` in your working directory.

Enterprise workspaces can review and correct the source transcript before adding a language, which
produces more accurate translations. See [Refine and regenerate a
dub](/docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate).

## Next steps

#### [Refine and regenerate a dub](/docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate)

Edit the source transcript and translations, then regenerate the dub

#### [Dub into multiple languages](/docs/eleven-api/guides/how-to/dubbing/multiple-languages)

Add several target languages to a single project

#### [API reference](/docs/api-reference/dubbing/create-project)

Explore all Dubbing API parameters and response formats
