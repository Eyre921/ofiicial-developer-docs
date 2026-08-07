---
title: "Bring your own transcript"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/bring-your-own-transcript.md
path: docs/eleven-api/guides/how-to/dubbing/bring-your-own-transcript
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Bring your own transcript

**How-to guide** · Assumes you are familiar with creating dubbing projects, as shown in the
[Dubbing quickstart](/docs/eleven-api/guides/cookbooks/dubbing).

Providing your own transcript and translations is only available to enterprise workspaces. Contact
[sales](https://elevenlabs.io/contact-sales) for access.

By default, the Dubbing API transcribes your source media and machine-translates the transcript into each target language. If you already have an accurate transcript — subtitles, a script, or professionally translated text — you can supply it instead. This guide covers the transcript file format, how to create a project from a transcript, and how to provide your own translations when adding a language.

## Transcript file format

A transcript is a JSON file with a single top-level `segments` array. Each segment is one utterance: the text spoken, when it starts and ends, and optionally who speaks it.

```json title="transcript.json"
{
  "segments": [
    {
      "external_id": "line_0",
      "speaker_id": "speaker_0",
      "start_s": 0.0,
      "end_s": 14.5,
      "text": "With my soft and whispery American accent, I'm the ideal choice for creating ASMR content, meditation guides, or adding an intimate feel to your narrative projects."
    }
  ]
}
```

| Field         | Required | Description                                                                                                                                                       |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`        | Yes      | The text spoken during the segment.                                                                                                                               |
| `start_s`     | Yes      | Start time of the segment, in seconds.                                                                                                                            |
| `end_s`       | Yes      | End time of the segment, in seconds.                                                                                                                              |
| `speaker_id`  | No       | Identifier grouping segments spoken by the same speaker, so each speaker is dubbed with a consistent voice. Segments that omit it share a single default speaker. |
| `external_id` | No       | Your own identifier for the segment, at most 128 characters and unique within the transcript. Used to key translations and echoed back on every transcript read.  |
| `translation` | No       | Translated text for the segment, used to seed the language target created via `target_language`. If any segment includes one, every segment must.                 |

### Segment rules

The transcript is validated when you create the project:

* Segments must be ordered by `start_s`.
* A segment must be between 0.1 and 25 seconds long, and `end_s` must be greater than `start_s`.
* Segments with the same `speaker_id` must not overlap, although they may touch at an endpoint. Segments from different speakers may overlap to represent simultaneous speech.
* A transcript may contain at most 20,000 segments and the file may be at most 4 MiB.

Prefer shorter segments over longer ones: break sentences wherever there is a pause of one second or longer. Segment boundaries determine how the dubbed audio is timed against the source, so a transcript with accurate, natural breaks produces a better-synchronized dub.

## Create a project from your transcript

Pass the transcript file when creating the project. `source_language` is required when providing a transcript, since the source media is not transcribed automatically. Languages are specified as BCP-47 tags, for example `es` or `fr-CA`. See the [supported languages and dialects](/docs/overview/capabilities/dubbing#supported-languages) for all accepted values.

```python
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

with open("transcript.json", "rb") as transcript:
    project = elevenlabs.dubbing.project.create(
        source_url="https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3",
        source_language="en",
        transcript=transcript,
    )

print(project.project_id)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import { createReadStream } from "fs";

const elevenlabs = new ElevenLabsClient();

const project = await elevenlabs.dubbing.project.create({
  sourceUrl: "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3",
  sourceLanguage: "en",
  transcript: createReadStream("transcript.json"),
});

console.log(project.projectId);
```

The project still ingests the source media before it can be dubbed, so poll it until its status is `ready`, as shown in the [quickstart](/docs/eleven-api/guides/cookbooks/dubbing). Your segments are used as-is; no automatic transcription runs.

## Provide your own translations

When adding a language target, pass a `translations` map to use your own translations instead of machine translation. The map is keyed by each source segment's `external_id`, or by its internal segment `id` if you did not supply one, and must cover every source segment exactly once.

```python
project_id = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3"

language = elevenlabs.dubbing.project.language.create(
    project_id,
    target_language="fr",
    translations={
        "line_0": "Avec mon accent américain doux et murmuré, je suis le choix idéal pour créer du contenu ASMR, des guides de méditation, ou pour apporter une touche d'intimité à vos projets narratifs.",
    },
)
```

```typescript
const projectId = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3";

const language = await elevenlabs.dubbing.project.language.create(projectId, {
  targetLanguage: "fr",
  translations: {
    line_0:
      "Avec mon accent américain doux et murmuré, je suis le choix idéal pour créer du contenu ASMR, des guides de méditation, ou pour apporter une touche d'intimité à vos projets narratifs.",
  },
});
```

Each language target takes one create call, so repeat this request for every language you want to dub into. A `translations` map may contain at most 20,000 entries totalling at most 4 MiB of text.

If your segments have no `external_id`, read the source transcript to obtain each segment's internal `id` and use those as keys instead:

```python
transcript = elevenlabs.dubbing.project.transcript.get(project_id)
for segment in transcript.segments:
    print(segment.id, segment.text)
```

```typescript
const transcript = await elevenlabs.dubbing.project.transcript.get(projectId);
for (const segment of transcript.segments) {
  console.log(segment.id, segment.text);
}
```

### Seed translations at project creation

For a single target language, you can skip the separate `translations` map by including a `translation` on every segment in the transcript file and passing `target_language` when creating the project. The language target is created queued with your translations and begins generating once the project is ready.

```json title="transcript.json"
{
  "segments": [
    {
      "external_id": "line_0",
      "speaker_id": "speaker_0",
      "start_s": 0.0,
      "end_s": 14.5,
      "text": "With my soft and whispery American accent, I'm the ideal choice for creating ASMR content, meditation guides, or adding an intimate feel to your narrative projects.",
      "translation": "Avec mon accent américain doux et murmuré, je suis le choix idéal pour créer du contenu ASMR, des guides de méditation, ou pour apporter une touche d'intimité à vos projets narratifs."
    }
  ]
}
```

## Quality considerations

The dub is only as good as the transcript and translations it is built from. Segment timings and text are used directly to time and voice the dubbed performance, so inaccurate timings or text degrade the output. Translations are rendered to fit their segment's time span: a translation that is much longer or shorter than the original affects the pacing of the dubbed speech, so aim for translations of comparable spoken length.

## Next steps

#### [Refine and regenerate a dub](/docs/eleven-api/guides/how-to/dubbing/refine-and-regenerate)

Edit the source transcript and translations, then regenerate the dub

#### [Dub into multiple languages](/docs/eleven-api/guides/how-to/dubbing/multiple-languages)

Add several target languages to a single project

#### [API reference](/docs/api-reference/dubbing/create-project)

Explore all Dubbing API parameters and response formats
