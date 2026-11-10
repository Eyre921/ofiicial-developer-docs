---
title: "Language options"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/language-options.md
path: docs/eleven-api/guides/how-to/speech-to-text/realtime/language-options
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Language options

> **Note**
>
> **How-to guide** · Assumes you have completed the
> [client-side](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming) or
> [server-side streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming) guide.

## Overview

By default, the realtime API detects the language of the audio automatically. You can change this behavior in three ways:

* Set `language_code` to the language of the audio.
* Add `secondary_languages` to limit language detection to a set of expected languages.
* With [Scribe v3 Live](/docs/overview/models#scribe-v3-live), set `multilang_mode=true` to follow speakers who switch languages during the session.

Scribe does not translate. Speech is transcribed in the language it is spoken in.

## Secondary languages

Pass `language_code` with the main language and repeat `secondary_languages` once per additional language in the query string. Both accept ISO-639-1 or ISO-639-3 codes.

```text
wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v3_live&language_code=en&secondary_languages=es&secondary_languages=fr
```

`secondary_languages` makes language identification more reliable by limiting it to the languages you list. To follow speakers who switch between languages during the session, use [multilingual mode](#multilingual-mode).

## Multilingual mode

> **Info**
>
> Multilingual mode is only available with Scribe v3 Live (`scribe_v3_live`). Other models reject
> `multilang_mode=true` with an `invalid_request` error and close the connection.

With `multilang_mode=true`, Scribe v3 Live transcribes each language in its own script and follows language switches, including switches in the middle of a sentence.

```text
wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v3_live&audio_format=pcm_16000&multilang_mode=true
```

Multilingual mode has the following trade-offs:

* Background speech that sounds like another language can be transcribed.
* Short phrases are more likely to be transcribed incorrectly.

> **Note**
>
> The official SDKs don't support `multilang_mode` yet. To use it, connect to the WebSocket API
> directly.

## Next steps

#### [Transcripts and commit strategies](/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies)

Commit transcripts manually, on silence, or with turn prediction.

#### [Number and language options](/docs/eleven-api/guides/how-to/speech-to-text/batch/number-and-language-options)

Format numbers and declare secondary languages for recorded audio.
