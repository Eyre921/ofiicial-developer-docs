---
title: "Transcription"
source: https://elevenlabs.io/docs/overview/capabilities/speech-to-text.md
path: docs/overview/capabilities/speech-to-text
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Transcription

## Overview

The ElevenLabs [Speech to Text (STT) API](/docs/eleven-api/guides/cookbooks/speech-to-text) turns spoken audio into text with state of the art accuracy across 90+ languages. Use [Scribe v3](/docs/overview/models#scribe-v3) for recorded audio and [Scribe v3 Live](/docs/overview/models#scribe-v3-live) for real-time audio. To try a live demo please visit our [Speech to Text](https://elevenlabs.io/speech-to-text) showcase page.

#### [Products](/docs/eleven-creative/playground/speech-to-text)

Step-by-step guide for using speech to text in ElevenLabs.

#### [Developers](/docs/eleven-api/guides/cookbooks/speech-to-text)

Learn how to integrate the speech to text API into your application.

#### [Realtime speech to text](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming)

Learn how to transcribe audio with ElevenLabs in realtime with WebSockets.

#### [API reference](/docs/api-reference/speech-to-text/convert)

Full API reference for the Speech to Text endpoint.

> **Info**
>
> Companies requiring HIPAA compliance must contact [ElevenLabs Sales](https://elevenlabs.io/contact-sales) to sign a Business Associate Agreement (BAA)
> agreement. Please ensure this step is completed before proceeding with any HIPAA-related
> integrations or deployments.

## Models

#### [Scribe v3](/docs/overview/models#scribe-v3)

Our most accurate speech recognition model for recorded audio

27% fewer word errors than Scribe v2 on FLEURS

Speaker diarization, up to 32 speakers

Numbers as digits or words

Secondary languages for mixed-language audio

Keyterm prompting, up to 1,000 terms

Entity detection and transcript editing

Precise word-level timestamps

#### [Scribe v3 Live](/docs/overview/models#scribe-v3-live)

Our most accurate real-time speech recognition model

44% lower semantic WER than Scribe v2 Realtime on FLEURS

Turn prediction from conversation context

Multilingual mode for mid-sentence language switches

Keyterm library, up to 100,000 terms

Entity detection and transcript editing

Precise word-level timestamps

Entity detection, 65 entity types

Entity redaction

Transcript editing with natural-language instructions

#### [Scribe v2 Medical](/docs/overview/models#scribe-v2-medical)

Speech recognition fine-tuned for clinical audio

35% fewer transcription errors on clinical audio than Scribe v2

Same accuracy on everyday speech as Scribe v2

Same features, languages, pricing, and API as Scribe v2

[Explore all](/docs/overview/models)

## Example API response

The following example shows the output of the Speech to Text API using the Scribe v2 model for a sample audio file.

<elevenlabs-audio-player audio-title="Nicole" audio-src="https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3" />

#### View full JSON response

```javascript
{
  "language_code": "en",
  "language_probability": 1,
  "text": "With a soft and whispery American accent, I'm the ideal choice for creating ASMR content, meditative guides, or adding an intimate feel to your narrative projects.",
  "words": [
    {
      "text": "With",
      "start": 0.119,
      "end": 0.259,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 0.239,
      "end": 0.299,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "a",
      "start": 0.279,
      "end": 0.359,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 0.339,
      "end": 0.499,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "soft",
      "start": 0.479,
      "end": 1.039,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 1.019,
      "end": 1.2,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "and",
      "start": 1.18,
      "end": 1.359,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 1.339,
      "end": 1.44,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "whispery",
      "start": 1.419,
      "end": 1.979,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 1.959,
      "end": 2.179,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "American",
      "start": 2.159,
      "end": 2.719,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 2.699,
      "end": 2.779,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "accent,",
      "start": 2.759,
      "end": 3.389,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 4.119,
      "end": 4.179,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "I'm",
      "start": 4.159,
      "end": 4.459,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 4.44,
      "end": 4.52,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "the",
      "start": 4.5,
      "end": 4.599,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 4.579,
      "end": 4.699,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "ideal",
      "start": 4.679,
      "end": 5.099,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 5.079,
      "end": 5.219,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "choice",
      "start": 5.199,
      "end": 5.719,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 5.699,
      "end": 6.099,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "for",
      "start": 6.099,
      "end": 6.199,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 6.179,
      "end": 6.279,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "creating",
      "start": 6.259,
      "end": 6.799,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 6.779,
      "end": 6.979,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "ASMR",
      "start": 6.959,
      "end": 7.739,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 7.719,
      "end": 7.859,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "content,",
      "start": 7.839,
      "end": 8.45,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 9,
      "end": 9.06,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "meditative",
      "start": 9.04,
      "end": 9.64,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 9.619,
      "end": 9.699,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "guides,",
      "start": 9.679,
      "end": 10.359,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 10.359,
      "end": 10.409,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "or",
      "start": 11.319,
      "end": 11.439,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 11.42,
      "end": 11.52,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "adding",
      "start": 11.5,
      "end": 11.879,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 11.859,
      "end": 12,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "an",
      "start": 11.979,
      "end": 12.079,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 12.059,
      "end": 12.179,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "intimate",
      "start": 12.179,
      "end": 12.579,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 12.559,
      "end": 12.699,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "feel",
      "start": 12.679,
      "end": 13.159,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 13.139,
      "end": 13.179,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "to",
      "start": 13.159,
      "end": 13.26,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 13.239,
      "end": 13.3,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "your",
      "start": 13.299,
      "end": 13.399,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 13.379,
      "end": 13.479,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "narrative",
      "start": 13.479,
      "end": 13.889,
      "type": "word",
      "speaker_id": "speaker_0"
    },
    {
      "text": " ",
      "start": 13.919,
      "end": 13.939,
      "type": "spacing",
      "speaker_id": "speaker_0"
    },
    {
      "text": "projects.",
      "start": 13.919,
      "end": 14.779,
      "type": "word",
      "speaker_id": "speaker_0"
    }
  ]
}
```

The output is classified in three category types:

* `word` - A word in the language of the audio
* `spacing` - The space between words, not applicable for languages that don't use spaces like Japanese, Mandarin, Thai, Lao, Burmese and Cantonese
* `audio_event` - Non-speech sounds like laughter or applause

## Concurrency and priority

Concurrency is the concept of how many requests can be processed at the same time.

For Speech to Text, files that are over 8 minutes long are transcribed in parallel internally in order to speed up processing. The audio is chunked into four segments to be transcribed concurrently.

You can calculate the concurrency limit with the following calculation:

$$
Concurrency = \min(4, \text{round\_up}(\frac{\text{audio\_duration\_secs}}{480}))
$$

For example, a 15 minute audio file will be transcribed with a concurrency of 2, while a 120 minute audio file will be transcribed with a concurrency of 4.

> **Info**
>
> The above calculation is only applicable to batch models such as Scribe v3, Scribe v2 and Scribe
> v2 Medical. For Scribe v3 Live and Scribe v2 Realtime, see the [concurrency limit chart](/docs/overview/models#concurrency-and-priority).

## Advanced features

> **Warning**
>
> Keyterm prompting and transcript editing come at an additional cost. See the [API pricing page](https://elevenlabs.io/pricing/api?price.section=speech_to_text\&price.sections=speech_to_text,speech_to_text#pricing-table)
> for detailed pricing information.

### Keyterm prompting

> **Info**
>
> Keyterm prompting is available with Scribe v3, Scribe v3 Live, Scribe v2, Scribe v2 Medical
> (batch), and Scribe v2 Realtime.

Highlight words or phrases to bias the model towards transcribing them. This is useful for transcribing specific words or sentences that are not common in the audio, such as product names, names, or other specific terms. Keyterms are more powerful than biased keywords or customer vocabularies offered by other models, because it relies on the context to decide whether to transcribe that term or not. Batch supports up to 1000 keyterms (50 characters each), while realtime supports up to 50 keyterms (20 characters each).

To learn more about how to use keyterm prompting, see the [keyterm prompting documentation](/docs/eleven-api/guides/how-to/speech-to-text/batch/keyterm-prompting).

### Keyterm library

> **Info**
>
> The keyterm library is available with Scribe v3 Live.

A keyterm library is a large vocabulary for a whole domain, such as a medical dictionary, legal terms or a product catalog. The model consults the library only when it hears a likely match. A library can contain up to 10,000 terms. Use it alongside keyterm prompting, which is best for the few terms you know will appear. Sessions that use a keyterm library are billed the same additional cost as keyterm prompting.

To learn more, see the [keyterm library documentation](/docs/eleven-api/guides/how-to/speech-to-text/batch/keyterm-prompting#keyterm-library).

### Turn prediction

> **Info**
>
> Turn prediction is available with Scribe v3 Live.

Silence-based voice activity detection (VAD) commits a transcript segment after a period of silence. A short silence threshold cuts speakers off when they pause, and a long one adds lag. Turn prediction uses the context of the conversation to estimate whether the speaker has finished their turn, so a caller who pauses halfway through a phone number is not cut off. This is the same turn detection that ElevenAgents uses.

To learn more, see [turn prediction](/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies#turn-prediction).

### Realtime diarization

> **Info**
>
> Realtime diarization is available with Scribe v3 Live.

Set `diarize=true` to label who is speaking in realtime transcripts. Draft speaker labels appear in partial transcripts, and each committed transcript is followed by a separate diarized transcript without delaying the committed text.

To learn more, see the [realtime speaker diarization guide](/docs/eleven-api/guides/how-to/speech-to-text/realtime/diarization).

### Number formatting

> **Info**
>
> Number formatting is available with Scribe v3.

Choose whether numbers in the transcript are written as digits (42) or as words (forty-two). If you don't set a format, the model chooses one.

To learn more, see [number and language options](/docs/eleven-api/guides/how-to/speech-to-text/batch/number-and-language-options).

### Mixed-language audio

> **Info**
>
> Secondary language codes are available with Scribe v3. Multilingual mode is available with Scribe
> v3 Live.

When speakers use more than one language, list the languages you expect so the model can transcribe each one accurately. For realtime audio, multilingual mode transcribes each language in its own script and follows switches in the middle of a sentence.

Scribe does not translate. Speech is transcribed in the language it is spoken in.

To learn more, see [number and language options](/docs/eleven-api/guides/how-to/speech-to-text/batch/number-and-language-options) for batch transcription and [realtime language options](/docs/eleven-api/guides/how-to/speech-to-text/realtime/language-options) for realtime transcription.

### No verbatim mode

> **Info**
>
> No verbatim mode is available with Scribe v3, Scribe v2, Scribe v2 Medical (batch), and Scribe v2
> Realtime.

When `no_verbatim` is enabled, the model removes filler words, false starts and disfluencies from the transcript. This produces a cleaner output suitable for subtitles, summaries, or any use case where readability is more important than capturing every spoken word.

### Entity detection

> **Info**
>
> Entity detection is available with all batch models, Scribe v3 Live, and Scribe v2 Realtime.

Batch and realtime models can detect several categories of entities in the transcript, providing their exact timestamps. This is useful to highlight credit card numbers, names, medical conditions or SSNs.

For a full list of supported entities, see the [entity detection documentation](/docs/eleven-api/guides/how-to/speech-to-text/batch/entity-detection).

### Transcript editing

> **Info**
>
> Transcript editing is an experimental feature available with all batch models, Scribe v3 Live, and
> Scribe v2 Realtime. It is not currently available in [data residency](/docs/overview/administration/data-residency) environments.

Pass a natural-language instruction with the `transcript_edit` parameter and it will be applied to the finished transcript. The edited text is returned in `edited_transcript` alongside the original transcript, so timestamps and speaker labels stay intact. This is useful for normalizing how dates, times or units are written, applying a different style, or rewriting the transcript in a single request.

To learn more, see the [transcript editing documentation](/docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing) and the [realtime transcript editing guide](/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcript-editing).

## Supported languages

Scribe v3 and Scribe v2 support 90+ languages, including:

*Afrikaans (afr), Amharic (amh), Arabic (ara), Armenian (hye), Assamese (asm), Asturian (ast), Azerbaijani (aze), Belarusian (bel), Bengali (ben), Bosnian (bos), Bulgarian (bul), Burmese (mya), Cantonese (yue), Catalan (cat), Cebuano (ceb), Chichewa (nya), Croatian (hrv), Czech (ces), Danish (dan), Dutch (nld), English (eng), Estonian (est), Filipino (fil), Finnish (fin), French (fra), Fulah (ful), Galician (glg), Ganda (lug), Georgian (kat), German (deu), Greek (ell), Gujarati (guj), Hausa (hau), Hebrew (heb), Hindi (hin), Hungarian (hun), Icelandic (isl), Igbo (ibo), Indonesian (ind), Irish (gle), Italian (ita), Japanese (jpn), Javanese (jav), Kabuverdianu (kea), Kannada (kan), Kazakh (kaz), Khmer (khm), Korean (kor), Kurdish (kur), Kyrgyz (kir), Lao (lao), Latvian (lav), Lingala (lin), Lithuanian (lit), Luo (luo), Luxembourgish (ltz), Macedonian (mkd), Malay (msa), Malayalam (mal), Maltese (mlt), Mandarin Chinese (zho), Māori (mri), Marathi (mar), Mongolian (mon), Nepali (nep), Northern Sotho (nso), Norwegian (nor), Occitan (oci), Odia (ori), Pashto (pus), Persian (fas), Polish (pol), Portuguese (por), Punjabi (pan), Romanian (ron), Russian (rus), Serbian (srp), Shona (sna), Sindhi (snd), Sinhala (sin), Slovak (slk), Slovenian (slv), Somali (som), Spanish (spa), Swahili (swa), Swedish (swe), Tamil (tam), Tajik (tgk), Telugu (tel), Thai (tha), Turkish (tur), Ukrainian (ukr), Umbundu (umb), Urdu (urd), Uzbek (uzb), Vietnamese (vie), Welsh (cym), Wolof (wol), Xhosa (xho) and Zulu (zul).*

### Breakdown of language support

Word Error Rate (WER) is a key metric used to evaluate the accuracy of transcription systems. It measures how many errors are present in a transcript compared to a reference transcript. Below is a breakdown of the WER for each language that Scribe v2 supports.

#### Excellent (≤ 5% WER)

Belarusian (bel), Bosnian (bos), Bulgarian (bul), Catalan (cat), Croatian (hrv), Czech (ces),
Danish (dan), Dutch (nld), English (eng), Estonian (est), Finnish (fin), French (fra), Galician
(glg), German (deu), Greek (ell), Hungarian (hun), Icelandic (isl), Indonesian (ind), Italian
(ita), Japanese (jpn), Kannada (kan), Latvian (lav), Macedonian (mkd), Malay (msa), Malayalam
(mal), Norwegian (nor), Polish (pol), Portuguese (por), Romanian (ron), Russian (rus), Slovak
(slk), Spanish (spa), Swedish (swe), Turkish (tur), Ukrainian (ukr) and Vietnamese (vie).

#### High Accuracy (>5% to ≤10% WER)

Armenian (hye), Azerbaijani (aze), Bengali (ben), Cantonese (yue), Filipino (fil), Georgian
(kat), Gujarati (guj), Hindi (hin), Kazakh (kaz), Lithuanian (lit), Maltese (mlt), Mandarin
(cmn), Marathi (mar), Nepali (nep), Odia (ori), Persian (fas), Serbian (srp), Slovenian (slv),
Swahili (swa), Tamil (tam) and Telugu (tel)

#### Good (>10% to ≤20% WER)

Afrikaans (afr), Arabic (ara), Assamese (asm), Asturian (ast), Burmese (mya), Hausa (hau),
Hebrew (heb), Javanese (jav), Korean (kor), Kyrgyz (kir), Luxembourgish (ltz), Māori (mri),
Occitan (oci), Punjabi (pan), Tajik (tgk), Thai (tha), Uzbek (uzb) and Welsh (cym).

#### Moderate (>25% to ≤50% WER)

Amharic (amh), Ganda (lug), Igbo (ibo), Irish (gle), Khmer (khm), Kurdish (kur), Lao (lao),
Mongolian (mon), Northern Sotho (nso), Pashto (pus), Shona (sna), Sindhi (snd), Sinhala (sin),
Somali (som), Urdu (urd), Wolof (wol), Xhosa (xho), Yoruba (yor) and Zulu (zul).

## FAQ

#### Can I use speech to text API with video files?

Yes, the API supports uploading both audio and video files for transcription.

#### What are the file size and duration limits for the Speech to Text API?

Files up to 5 GB in size are supported. Duration limits depend on the transcription mode:

* **Standard mode** (`use_multi_channel=false`): Up to 15 hours
* **Multi-channel mode** (`use_multi_channel=true`): The combined duration of all channels must be less than 15 hours

#### Which audio and video formats are supported in the API?

The API supports the following audio and video formats:

* audio/aac
* audio/x-aac
* audio/x-aiff
* audio/ogg
* audio/mpeg
* audio/mp3
* audio/mpeg3
* audio/x-mpeg-3
* audio/opus
* audio/wav
* audio/x-wav
* audio/webm
* audio/flac
* audio/x-flac
* audio/mp4
* audio/aiff
* audio/x-m4a

Supported video formats include:

* video/mp4
* video/x-msvideo
* video/x-matroska
* video/quicktime
* video/x-ms-wmv
* video/x-flv
* video/webm
* video/mpeg
* video/3gpp

#### When will you support more languages?

ElevenLabs is constantly expanding the number of languages supported by our models. Please check back frequently for updates.

#### Does speech to text API support webhooks?

Yes, asynchronous transcription results can be sent to webhooks configured in webhook settings in the UI. Learn more in the [webhooks cookbook](/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks).

#### Is a multichannel transcription mode supported in the API?

Yes, the multichannel [STT](https://elevenlabs.io/speech-to-text) feature allows you to transcribe audio where each channel is processed independently and assigned a speaker ID based on its channel number. This feature supports up to 5 channels. Learn more in the [multichannel transcription cookbook](/docs/eleven-api/guides/how-to/speech-to-text/batch/multichannel-transcription).

#### How does billing work for the speech to text API?

ElevenLabs charges for speech to text based on the duration of the audio sent for transcription. Billing is calculated per hour of audio, with rates varying by tier and model. See the [API pricing page](https://elevenlabs.io/pricing/api?price.section=speech_to_text#pricing-table) for detailed pricing information.

Silence counts toward the billed duration. Both batch and realtime transcription are metered on every second of audio you send, including pauses and silent stretches, and there is no discount for silence.

## Key facts

* **Supported input**: Both audio and video files are accepted
* **Maximum file size**: 5 GB
* **Maximum duration**: 15 hours (standard mode), 15 hours combined across all channels (multichannel mode)
* **Multichannel mode**: Up to 5 channels; each processed independently with a speaker ID assigned by channel number
* **Webhooks**: Asynchronous transcription results can be delivered to a webhook — configure in workspace settings
* **Supported audio formats**: AAC, AIFF, OGG, MP3, OPUS, WAV, FLAC, M4A, WebM
* **Supported video formats**: MP4, AVI, MKV, MOV, WMV, FLV, WebM, MPEG, 3GPP
