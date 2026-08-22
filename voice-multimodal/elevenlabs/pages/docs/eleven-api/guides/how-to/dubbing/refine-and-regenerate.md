---
title: "Refine and regenerate a dub"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate.md
path: docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Refine and regenerate a dub

**How-to guide** · Assumes you have created a dubbing project and generated at least one language,
as shown in the [Dubbing quickstart](/docs/eleven-api/guides/cookbooks/dubbing).

The transcript editing and regeneration endpoints used in this guide are only available to
enterprise workspaces. Contact [sales](https://elevenlabs.io/contact-sales) for access.

A dub is only as accurate as the transcript it is built from. This guide covers the two places you can make corrections — the source transcript and a language's translation — and how to regenerate the audio once you are satisfied.

## How revisions work

Every project and every language track their own `revision` counter, both starting at `0`.

* Editing the source transcript increases the project's `revision`. Transcription itself does not.
* Editing a translation increases that language's `revision`. It does not affect the source or any other language.
* A language also reports `output_revision`: the revision its current audio was generated from. When `output_revision` is behind `revision`, the downloaded audio is out of date and the language's status becomes `stale`.

Correct the source transcript before adding languages where possible. Translations are produced from the source, so fixing the source first means every language starts from the right text. Editing the source after a language exists marks that language `stale` and requires a regeneration.

## Edit the source transcript

Read the source transcript to get each segment's stable `id`, then edit, add, or delete segments.

```python
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Replace with your project's ID
project_id = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3"

# Read the source transcript
transcript = elevenlabs.dubbing.project.transcript.get(project_id)
first_segment = transcript.segments[0]

# Correct a segment's text
elevenlabs.dubbing.project.transcript.update_segment(
    project_id,
    segment_id=first_segment.id,
    text="Welcome to our latest product demo.",
)

# Add a segment (reuse an existing speaker_id so it is dubbed with that voice)
added = elevenlabs.dubbing.project.transcript.create_segment(
    project_id,
    text="Thanks for watching.",
    speaker_id=first_segment.speaker_id,
    start_s=40.0,
    end_s=42.0,
)

# Delete the segment we just added
elevenlabs.dubbing.project.transcript.delete_segment(
    project_id,
    segment_id=added.segment.id,
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

// Replace with your project's ID
const projectId = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3";

// Read the source transcript
const transcript = await elevenlabs.dubbing.project.transcript.get(projectId);
const firstSegment = transcript.segments[0];

// Correct a segment's text
await elevenlabs.dubbing.project.transcript.updateSegment(projectId, firstSegment.id, {
  text: "Welcome to our latest product demo.",
});

// Add a segment (reuse an existing speakerId so it is dubbed with that voice)
const added = await elevenlabs.dubbing.project.transcript.createSegment(projectId, {
  text: "Thanks for watching.",
  speakerId: firstSegment.speakerId,
  startS: 40.0,
  endS: 42.0,
});

// Delete the segment we just added
await elevenlabs.dubbing.project.transcript.deleteSegment(projectId, added.segment.id);
```

When editing timing, `end_s` must be greater than `start_s`. New segments require all four fields (`text`, `speaker_id`, `start_s`, `end_s`); the server assigns the segment `id`.

## Refine a translation

A language transcript pairs each source segment with its translation. Segment `id` values match the source transcript, so you can line translations up against the original text. Edit a single segment's translation to override the machine translation. Pass `null` to clear a translation and mark that segment for re-translation.

```python
project_id = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3"
language_id = "lang_1001kwkyxp0je6ktn4knsfrasx5s"

# Read the language's translations
target = elevenlabs.dubbing.project.language.transcript.get(project_id, language_id)
first_segment = target.segments[0]

# Refine a single translation
elevenlabs.dubbing.project.language.transcript.update_segment(
    project_id,
    language_id,
    segment_id=first_segment.id,
    translation="Bienvenido a nuestra última demostración de producto.",
)
```

```typescript
const projectId = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3";
const languageId = "lang_1001kwkyxp0je6ktn4knsfrasx5s";

// Read the language's translations
const target = await elevenlabs.dubbing.project.language.transcript.get(projectId, languageId);
const firstSegment = target.segments[0];

// Refine a single translation
await elevenlabs.dubbing.project.language.transcript.updateSegment(
  projectId,
  languageId,
  firstSegment.id,
  { translation: "Bienvenido a nuestra última demostración de producto." }
);
```

Editing a translation bumps the language's `revision`. If the language had already completed, it becomes `stale` and keeps its previous audio until you regenerate.

## Regenerate the audio

After editing the source transcript or a translation, regenerate the language to produce a fresh dub from the current transcript. Regeneration is charged like a generation.

```python
import time

# Regenerate from the current transcript
elevenlabs.dubbing.project.language.transcript.regenerate(project_id, language_id)

# Poll until the new output is ready
while True:
    language = elevenlabs.dubbing.project.language.get(project_id, language_id)
    if language.status == "completed":
        break
    if language.status == "failed":
        raise RuntimeError("Regeneration failed")
    time.sleep(5)

print("Fresh output at", language.outputs.lossless_audio)
```

```typescript
// Regenerate from the current transcript
await elevenlabs.dubbing.project.language.transcript.regenerate(projectId, languageId);

// Poll until the new output is ready
let language = await elevenlabs.dubbing.project.language.get(projectId, languageId);
while (language.status !== "completed") {
  if (language.status === "failed") throw new Error("Regeneration failed");
  await new Promise((resolve) => setTimeout(resolve, 5000));
  language = await elevenlabs.dubbing.project.language.get(projectId, languageId);
}

console.log("Fresh output at", language.outputs!.losslessAudio!);
```

Regenerate returns a `409 Conflict` if the project is not `ready` or the language is not in a settled state, for example when it is already generating. Once the language reaches `completed` again, `output_revision` equals `revision` and the downloaded audio reflects your edits.

You can control how strongly the dubbed speakers clone the source voices with the
`cloning_strength` voice setting (0 to 10, default 7) when adding a language. See the [create
language target](/docs/api-reference/dubbing/language-targets/create-language-target) API
reference.
