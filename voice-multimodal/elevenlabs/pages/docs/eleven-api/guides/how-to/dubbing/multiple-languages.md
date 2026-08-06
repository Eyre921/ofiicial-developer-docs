---
title: "Dub into multiple languages"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/multiple-languages.md
path: docs/eleven-api/guides/how-to/dubbing/multiple-languages
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dub into multiple languages

**How-to guide** · Assumes you have created a dubbing project, as shown in the [Dubbing
quickstart](/docs/eleven-api/guides/cookbooks/dubbing).

A single project holds one source transcript, and you can add as many language targets as you need. Each language is generated independently and carries its own status and output, so you translate the source once and produce every dub from it.

## Add several languages

Add one language target per language you want to dub into. Each starts in `queued` and begins generating once the project is `ready`.

```python
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

project_id = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3"
target_languages = ["es", "fr", "de", "ja"]

languages = [
    elevenlabs.dubbing.project.language.create(project_id, target_language=lang)
    for lang in target_languages
]
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const projectId = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3";
const targetLanguages = ["es", "fr", "de", "ja"];

const languages = await Promise.all(
  targetLanguages.map((lang) =>
    elevenlabs.dubbing.project.language.create(projectId, { targetLanguage: lang })
  )
);
```

You can also queue the first language when you create the project by passing `target_language` to `project.create`. Add any further languages with `language.create` as shown above.

## Track each language independently

Languages generate in parallel and finish at different times. List the project's languages to check the status of each, rather than polling them one by one.

```python
import time

while True:
    result = elevenlabs.dubbing.project.language.list(project_id)
    pending = [l for l in result.languages if l.status in ("queued", "processing")]
    if not pending:
        break
    print(f"{len(pending)} language(s) still generating...")
    time.sleep(5)
```

```typescript
while (true) {
  const result = await elevenlabs.dubbing.project.language.list(projectId);
  const pending = result.languages.filter(
    (l) => l.status === "queued" || l.status === "processing"
  );
  if (pending.length === 0) break;
  console.log(`${pending.length} language(s) still generating...`);
  await new Promise((resolve) => setTimeout(resolve, 5000));
}
```

## Download every completed dub

Once a language reaches `completed`, its `outputs.lossless_audio` holds a signed download URL. Download each one, skipping any language that failed.

```python
import requests

result = elevenlabs.dubbing.project.language.list(project_id)
for language in result.languages:
    if language.status != "completed":
        print(f"Skipping {language.target_language}: {language.status}")
        continue
    audio = requests.get(language.outputs.lossless_audio)
    with open(f"dubbed_{language.target_language}.wav", "wb") as f:
        f.write(audio.content)
    print(f"Saved dubbed_{language.target_language}.wav")
```

```typescript
import { writeFile } from "fs/promises";

const result = await elevenlabs.dubbing.project.language.list(projectId);
for (const language of result.languages) {
  if (language.status !== "completed") {
    console.log(`Skipping ${language.targetLanguage}: ${language.status}`);
    continue;
  }
  const response = await fetch(language.outputs!.losslessAudio!);
  const buffer = Buffer.from(await response.arrayBuffer());
  await writeFile(`dubbed_${language.targetLanguage}.wav`, buffer);
  console.log(`Saved dubbed_${language.targetLanguage}.wav`);
}
```

Signed URLs expire about an hour after they are issued. If a download fails because the URL has expired, fetch the language again with `language.get` to obtain a fresh URL.
