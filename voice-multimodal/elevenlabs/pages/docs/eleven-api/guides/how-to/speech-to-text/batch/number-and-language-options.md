---
title: "Number and language options"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/number-and-language-options.md
path: docs/eleven-api/guides/how-to/speech-to-text/batch/number-and-language-options
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Number and language options

> **Note**
>
> **How-to guide** · Assumes you have completed the [Speech to Text quickstart](/docs/eleven-api/guides/cookbooks/speech-to-text).

## Overview

[Scribe v3](/docs/overview/models#scribe-v3) adds two optional parameters to the batch Speech to Text API:

* `numbers_format` sets whether numbers in the transcript are written as digits (`42`) or as words (`forty-two`).
* `secondary_language_codes` lists other languages that may be spoken in the audio alongside `language_code`. This improves accuracy on audio where speakers switch between languages.

Both parameters are only supported by `scribe_v3`. Sending either one with another model returns an `invalid_parameters` error.

> **Note**
>
> The SDKs don't have typed arguments for these parameters yet. In Python, pass them through
> `request_options`. In TypeScript, send the request with `fetch`.

## Format numbers

Set `numbers_format` to `digits` or `words`. When the parameter is omitted, the model chooses the format.

| Value     | Example output      |
| --------- | ------------------- |
| `digits`  | `42`                |
| `words`   | `forty-two`         |
| (omitted) | Chosen by the model |

```python maxLines=0 {19-24}
import os
from io import BytesIO

import requests
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_url = "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
audio_data = BytesIO(requests.get(audio_url).content)

transcription = elevenlabs.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v3",
    request_options={
        "additional_body_parameters": {
            "numbers_format": "digits",
        },
    },
)

print(transcription.text)
```

```typescript maxLines=0 {10-11}
import "dotenv/config";

const audio = await fetch(
  "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
);
const audioBlob = new Blob([await audio.arrayBuffer()], { type: "audio/mp3" });

const form = new FormData();
form.append("file", audioBlob, "nicole.mp3");
form.append("model_id", "scribe_v3");
form.append("numbers_format", "digits");

const response = await fetch("https://api.elevenlabs.io/v1/speech-to-text", {
  method: "POST",
  headers: { "xi-api-key": process.env.ELEVENLABS_API_KEY! },
  body: form,
});

const transcription = await response.json();
console.log(transcription.text);
```

`numbers_format` controls how the model transcribes numbers. For other changes to how dates, times or units are written, use [transcript editing](/docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing).

## Declare secondary languages

Set `language_code` to the main language of the audio and `secondary_language_codes` to the other languages you expect. Both accept ISO-639-1 or ISO-639-3 codes.

`secondary_language_codes` is a list. Repeat the form field once per language. A JSON array sent as a single string is not accepted.

The following example transcribes English audio that also contains Spanish and French:

```python maxLines=0 {4-9}
transcription = elevenlabs.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v3",
    language_code="en",
    request_options={
        "additional_body_parameters": {
            "secondary_language_codes": ["es", "fr"],
        },
    },
)
```

```typescript maxLines=0 {4-7}
const form = new FormData();
form.append("file", audioBlob, "recording.mp3");
form.append("model_id", "scribe_v3");
form.append("language_code", "en");
for (const code of ["es", "fr"]) {
  form.append("secondary_language_codes", code);
}

const response = await fetch("https://api.elevenlabs.io/v1/speech-to-text", {
  method: "POST",
  headers: { "xi-api-key": process.env.ELEVENLABS_API_KEY! },
  body: form,
});
```

> **Warning**
>
> Unrecognized codes in `secondary_language_codes` are skipped without an error. Check the codes
> against the [supported languages](/docs/overview/capabilities/speech-to-text#supported-languages)
> before sending the request.

Scribe v3 transcribes speech in the language it is spoken in. It does not translate between the main and secondary languages.

## Combine with other parameters

Both parameters can be used together and with other batch parameters, such as `keyterms`, `diarize` and `no_verbatim`. See [keyterm prompting](/docs/eleven-api/guides/how-to/speech-to-text/batch/keyterm-prompting) to bias transcription towards specific terms.

## Next steps

#### [Models](/docs/overview/models#scribe-v3)

Scribe v3 features and how to upgrade from Scribe v2.

#### [Realtime language options](/docs/eleven-api/guides/how-to/speech-to-text/realtime/language-options)

Transcribe live audio in more than one language with Scribe v3 Live.
