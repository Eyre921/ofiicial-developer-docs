---
title: "Transcript editing"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing.md
path: docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Transcript editing

> **Note**
>
> **How-to guide** · Assumes you have completed the [Speech to Text quickstart](/docs/eleven-api/guides/cookbooks/speech-to-text).

## Overview

> **Warning**
>
> Transcript editing is an experimental feature and comes at an additional cost of 30% on top of the
> base transcription cost, billed for a minimum of 10 seconds of audio per request. See the [API pricing page](https://elevenlabs.io/pricing?price.section=speech_to_text\&price.sections=speech_to_text,speech_to_text#pricing-table)
> for detailed pricing information.

Transcript editing lets you attach a natural-language instruction to a transcription request. Once the audio has been transcribed, your instruction is applied to the transcript and the edited text is returned alongside the original.

This replaces a separate post-processing step in your own pipeline. Typical uses are normalizing how dates, times or units are written, expanding abbreviations, removing content you do not need, applying a different style or tone, or reformatting the transcript.

For example, transcribing a voicemail with the instruction `Write all dates in ISO 8601 format (YYYY-MM-DD)` returns both versions of the text:

```json maxLines=0
{
  "language_code": "eng",
  "language_probability": 0.9912,
  "text": "Hi, this is Jill. Your appointment is confirmed for the twelfth of July twenty twenty-six, and the follow-up is on the third of August.",
  "words": [
    { "text": "Hi,", "start": 0.12, "end": 0.38, "type": "word", "logprob": 0.0 },
    { "text": " ", "start": 0.38, "end": 0.41, "type": "spacing", "logprob": 0.0 },
    { "text": "this", "start": 0.41, "end": 0.55, "type": "word", "logprob": 0.0 },
    ...
  ],
  "transcription_id": "Y2ZX8AxHUzTPCIualYiE",
  "edited_transcript": {
    "kind": "transcript",
    "text": "Hi, this is Jill. Your appointment is confirmed for 2026-07-12, and the follow-up is on 2026-08-03."
  }
}
```

The `text` and `words` fields always describe the original transcript. The edited version is returned separately in `edited_transcript`.

## Integrating transcript editing

Transcript editing is integrated into the Speech to Text API by passing the `transcript_edit` parameter to the `convert` method. The instruction can be up to 2000 characters long.

```python maxLines=0
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

with open("voicemail.mp3", "rb") as audio_file:
    transcription = elevenlabs.speech_to_text.convert(
        file=audio_file,
        model_id="scribe_v2",
        # Natural-language instruction applied to the finished transcript.
        transcript_edit="Write all dates in ISO 8601 format (YYYY-MM-DD)",
    )

print("Original:", transcription.text)
print("Edited:", transcription.edited_transcript)
```

```typescript maxLines=0
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import { readFile } from "node:fs/promises";

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

const audioBlob = new Blob([await readFile("voicemail.mp3")], { type: "audio/mp3" });

const transcription = await elevenlabs.speechToText.convert({
  file: audioBlob,
  modelId: "scribe_v2",
  // Natural-language instruction applied to the finished transcript.
  transcriptEdit: "Write all dates in ISO 8601 format (YYYY-MM-DD)",
});

console.log("Original:", transcription.text);
console.log("Edited:", transcription.editedTranscript);
```

Transcript editing works with both synchronous requests and [webhook](/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks) requests. For webhook requests, `edited_transcript` is included in the `transcription` object of the webhook payload.

Scribe v2 Realtime supports the same instructions on each committed transcript. See the [realtime transcript editing guide](/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcript-editing).

## Writing instructions

The instruction is applied to the whole transcript wherever it is relevant, and every matching occurrence is edited, not just the first. An instruction can change specific words or phrases and leave everything else untouched, or it can rewrite or annotate the complete text. A single instruction can combine several edits.

The following examples illustrate the range of supported instructions:

| Instruction                                                                                             | Effect                                                                                   |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `Write all dates in ISO 8601 format (YYYY-MM-DD)`                                                       | `the twelfth of July twenty twenty-six` becomes `2026-07-12`                             |
| `Write times in 24-hour format`                                                                         | `half past two in the afternoon` becomes `14:30`                                         |
| `Expand abbreviations such as "ETA" and "ASAP" on first use`                                            | `ETA` becomes `estimated time of arrival (ETA)`                                          |
| `Add the sentiment of every sentence in brackets at the end. Choose from [positive, negative, neutral]` | `Thanks, that was really helpful.` becomes `Thanks, that was really helpful. [positive]` |
| `Redact every curse word with its first letter followed by stars, e.g. s***`                            | `That was a damn good call.` becomes `That was a d*** good call.`                        |
| `Format the transcript as a bulleted list, one sentence per bullet`                                     | Reformats the whole transcript                                                           |

> **Note**
>
> Some adjustments have dedicated parameters that are cheaper and more predictable than an edit
> instruction. Use [keyterm prompting](/docs/eleven-api/guides/how-to/speech-to-text/batch/keyterm-prompting) to bias
> recognition towards specific names and terms, `no_verbatim` to remove filler words and
> disfluencies, and `numbers_format` (where supported) to choose between digits and words. Reserve
> transcript editing for changes those options do not cover.

Keep the following in mind when writing instructions:

* Be explicit about the desired output. `Write all dates in ISO 8601 format (YYYY-MM-DD)` is more reliable than `fix the dates`.
* The instruction can be written in any language, although instructions written in English work best. The edited transcript stays in the language of the original.
* Only the instruction is carried out. Content spoken in the audio is treated as data and cannot change how the instruction is applied.
* If nothing in the transcript is affected by the instruction, the edited transcript is identical to the original.

## Response format

When `transcript_edit` is set, the response contains an `edited_transcript` object. Its `kind` field indicates whether the edit succeeded:

| `kind`       | Fields                                  | Description                                                                                                   |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `transcript` | `text`                                  | The edited transcript. Identical to the original `text` when no edits were made.                              |
| `error`      | `error_type` (`edit_failed`), `message` | The edit could not be produced. The transcription itself succeeded and the original `text` is still returned. |

The field is absent when no `transcript_edit` was requested.

**`Failed edit`**

```json title="Failed edit"
{
  "text": "Hi, this is Jill. Your appointment is confirmed for ...",
  "edited_transcript": {
    "kind": "error",
    "error_type": "edit_failed",
    "message": "The transcript could not be edited. Please try again."
  }
}
```

Behavior to be aware of:

* The edited transcript is plain text. Word-level timestamps, speaker labels and `additional_formats` continue to describe the original transcript.
* The edit runs after transcription has completed, so it adds latency that grows with the length of the transcript.
* The surcharge is applied to the audio duration of the request, with a minimum of 10 seconds billed per request.

> **Warning**
>
> Transcript editing cannot be combined with `entity_detection`, `entity_redaction` or
> `use_multi_channel`. Requests that combine them are rejected with an invalid parameters error.

## Next steps

#### [API reference](/docs/api-reference/speech-to-text)

Full Speech to Text API reference and parameters.

#### [Webhooks](/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks)

Receive transcripts, including the edited transcript, asynchronously via webhooks.
