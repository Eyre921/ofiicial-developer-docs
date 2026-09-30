---
title: "Speed, Pause, Pronunciation"
source: https://developers.deepgram.com/docs/tts-voice-controls.md
path: docs/tts-voice-controls
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Speed, Pause, Pronunciation

> **Info**
>
> Pronunciation control on Flux TTS is in **Early Access**; see [Pronunciation control](#pronunciation-control). Some control combinations are invalid on Flux TTS: pronunciation cannot be combined with speed or pause. See [Combining controls](#combining-controls).

Flux TTS (`/v2/speak`) voice controls let you adjust speech output: change the speaking rate, insert silence, and override the pronunciation of specific words. They are designed for use cases that need precise delivery of industry terminology, brand names, and complex content.

Aura-2 (`/v1/speak`) supports speed and pronunciation with the same syntax. Each section calls out where Aura-2 differs.

## Availability

| Control       | [Batch (REST)](/docs/flux-tts/batch) | [Streaming (WebSocket)](/docs/flux-tts/quickstart) | Aura-2        |
| ------------- | ------------------------------------ | -------------------------------------------------- | ------------- |
| Speed         | Yes                                  | Yes, including mid-stream `Configure`              | Yes           |
| Pronunciation | Early Access                         | Early Access                                       | Yes           |
| Pause         | Yes                                  | No                                                 | Not supported |

Flux TTS controls are available in English. Aura-2 speed and pronunciation are available in English and Spanish.

## Speed control

Adjust the speaking rate of generated audio. Speed control modifies the pace of speech while maintaining natural prosody and voice quality.

### Parameters

| Parameter | Location | Type  | Default | Range                               |
| --------- | -------- | ----- | ------- | ----------------------------------- |
| `speed`   | query    | float | `1.0`   | `0.5` - `1.5`, in `0.05` increments |

On a streaming session, set `speed` as a connection parameter or change it mid-session with a [`Configure`](/docs/flux-tts/client-messages) message. The change applies at the next segment boundary.

### Example request

```bash
curl --request POST \
     --header "Content-Type: application/json" \
     --header "Authorization: Token DEEPGRAM_API_KEY" \
     --output your_output_file.mp3 \
     --data '{"text":"Hello, how can I help you today?"}' \
     --url "https://api.deepgram.com/v2/speak?model=flux-haley-en&speed=0.9"
```

### Speed values

| Value | Effect       | Use Case                                           |
| ----- | ------------ | -------------------------------------------------- |
| `0.5` | 50% slower   | Slowest supported rate                             |
| `0.7` | 30% slower   | Language learning, accessibility, legal compliance |
| `0.8` | 20% slower   | Complex instructions, elderly users                |
| `0.9` | 10% slower   | Clear explanations, training content               |
| `1.0` | Normal speed | Default conversational pace                        |
| `1.1` | 10% faster   | Efficient notifications                            |
| `1.2` | 20% faster   | Quick alerts, time-sensitive content               |
| `1.5` | 50% faster   | Rapid playback, content preview                    |

A value outside the range, or inside it but off the `0.05` increment, returns an error.

> **Note**
>
> **Aura-2:** speed runs `0.7` - `1.5`, so `0.5` and `0.6` are not supported. For Aura-2 Spanish voices, the recommended range is `0.9` - `1.5`; values below `0.9` may introduce disfluencies.

## Pause control

Insert silence at a specific point in the text. Pause control is available on Flux TTS batch requests.

> **Note**
>
> **Aura-2** does not support pause control. On Flux TTS streaming, a pause marker fails the connection with `DATA-0002`; use [batch](/docs/flux-tts/batch) for text with pauses.

### Syntax

Place an escaped pause marker where you want the silence:

```text
Your confirmation number is 4 7 2. \{pause:1s\} Is there anything else I can help with?
```

Write the duration in milliseconds (`\{pause:500\}` or `\{pause:500ms\}`) or seconds (`\{pause:1.5s\}`). A number with no unit is read as milliseconds. A structured form, `{pause:{duration_ms:500}}`, is also accepted and is easier for LLMs to generate. Write the structured form without backslashes; an escaped structured marker, or a simple marker without backslashes, is rejected with `BREAK_SYNTAX_INVALID`.

### Example request

```bash
curl --request POST \
     --header "Content-Type: application/json" \
     --header "Authorization: Token DEEPGRAM_API_KEY" \
     --output your_output_file.mp3 \
     --data '{"text":"Your confirmation number is 4 7 2. \\{pause:1s\\} Is there anything else I can help with?"}' \
     --url "https://api.deepgram.com/v2/speak?model=flux-haley-en"
```

### Validation rules

| Rule                          | Limit                                                      |
| ----------------------------- | ---------------------------------------------------------- |
| Duration range                | 500 ms to 3000 ms                                          |
| Increment                     | 100 ms. Off-grid values are rejected, never rounded.       |
| Max pause markers per request | 8                                                          |
| Adjacent pauses               | Two pauses need text between them                          |
| Delivery tolerance            | Pauses land within about ±100 ms of the requested duration |

## Pronunciation control

Override the default pronunciation of specific words using International Phonetic Alphabet (IPA) notation.

> **Warning**
>
> Pronunciation control on Flux TTS is in Early Access. The same override can come out differently from one generation to the next; some generations may not follow the IPA. Generate each term several times, on each voice you use, before you rely on it in production.

### Syntax

Pronunciation overrides are specified inline within the text using escaped JSON objects:

```text
\{"word": "dupilumab", "pronounce": "duːˈpɪljuːmæb"\}
```

Where:

* `word` is the original text (used for billing and display)
* `pronounce` is the IPA phonetic transcription
* Curly braces must be escaped with backslashes (`\{` and `\}`)

### Writing IPA for Flux TTS

Flux TTS was trained on a specific IPA style. Overrides that follow it are applied more reliably:

* **Use broad (phonemic) transcription**, for example `kˈɑpiɹˌaɪt` (copyright). Leave out narrow phonetic detail.
* **Use American pronunciations.** The model was trained mostly on American English.
* **Always mark primary stress** with `ˈ`. Nearly every word the model was trained on carries one. You can place it before the syllable (`ˈkɑpi`) or directly before the vowel (`kˈɑpi`).
* **Secondary stress is optional.** Add `ˌ` when you want more control over a long word.
* **Use `ɹ` for the English r sound**, not `r`.
* **Add length markers where the model slips.** If a vowel comes out short or swapped, mark it long: `-miːn` rather than `-min`.

### Example request

```bash
curl -X POST "https://api.deepgram.com/v2/speak?model=flux-haley-en" \
     -H "Authorization: token DEEPGRAM_API_KEY" \
     -H "Content-Type: application/json" \
     --output your_output_file.mp3 \
     -d '{"text": "Take \\{\"word\": \"Azathioprine\", \"pronounce\": \"æzəˈθaɪəpɹiːn\"\\} twice daily with \\{\"word\": \"dupilumab\", \"pronounce\": \"duːˈpɪljuːmæb\"\\}."}'
```

> **Info**
>
> The curly braces must be escaped with `\\{` and `\\}` in the cURL command.

### Common use cases

| Category      | Word         | IPA             | Spoken As              |
| ------------- | ------------ | --------------- | ---------------------- |
| Medical       | dupilumab    | `duːˈpɪljuːmæb` | "doo-PIL-yoo-mab"      |
| Medical       | azathioprine | `æzəˈθaɪəpɹiːn` | "az-uh-THIGH-oh-preen" |
| Brand         | Hermès       | `ɛəɹˈmɛz`       | "air-MEZ"              |
| Personal name | Nguyen       | `ˈwɪn`          | "win"                  |
| Technical     | SQL          | `ˈsiːkwəl`      | "sequel"               |

### Sourcing IPA transcriptions

A few rules of thumb for producing IPA for your own vocabulary:

* **Short lists (\<20 words):** generate with an LLM and validate by ear.
* **Longer lists:** use authoritative dictionaries that publish IPA directly:
  * [Cambridge Dictionary](https://dictionary.cambridge.org/)
  * [Collins Dictionary](https://www.collinsdictionary.com/)
  * [Oxford English Dictionary](https://www.oed.com/?tl=true)

**Best practices:**

* **Always validate by ear.** IPA that looks correct on the page can still sound off when synthesized — listen to the output before shipping.
* **Match the dialect.** UK and US pronunciations differ (e.g., *schedule*, *aluminum*). Make sure the IPA you choose matches the voice and audience you're targeting.

### Validation rules

| Rule                           | Limit                                                     |
| ------------------------------ | --------------------------------------------------------- |
| Max pronunciations per request | 500                                                       |
| Max IPA string length          | 128 characters                                            |
| IPA length ratio               | Cannot exceed 10x the source word length (min floor = 15) |

> **Note**
>
> **Aura-2** pronunciation control is generally available, with the same syntax and limits and a maximum input text length of 2000 characters. On Aura-2, place the stress mark directly before the vowel (`duːpˈɪljuːmæb`); a stress mark before a consonant returns a pronunciation warning.

## Combining controls

| Combination           | Flux TTS                                                                                                                      |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Speed + pause         | Allowed, with `speed` capped at `1.15` when any pause marker is present. Speed on its own keeps the full `0.5` - `1.5` range. |
| Speed + pronunciation | Rejected with `CONTROL_COMBINATION_INVALID` (a `speed` of `1.0` is exempt)                                                    |
| Pause + pronunciation | Rejected with `CONTROL_COMBINATION_INVALID`                                                                                   |
| All three             | Rejected with `CONTROL_COMBINATION_INVALID`                                                                                   |

A `speed` of exactly `1.0` does not count as a speed control, so it never triggers these rules. On a streaming session, a pronunciation control sent on a connection opened with a `speed` other than `1.0`, or after a `Configure` that set one, fails the connection with `DATA-0002`. A mid-stream `Configure` that sets `speed` while a queued turn still carries a pronunciation control is refused with a `ConfigureFailure` (`CONTROL_COMBINATION_INVALID`), and the previous speed stays in force. Pronunciations in the turn that is already playing do not block it. See [ConfigureFailure codes](/docs/flux-tts/server-messages#configurefailure-codes).

> **Note**
>
> **Aura-2** allows speed and pronunciation in the same request. Aura-2 has no pause control, so no other combinations apply.
>
> ```bash
> curl -X POST "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&speed=0.8" \
>      -H "Authorization: token DEEPGRAM_API_KEY" \
>      -H "Content-Type: application/json" \
>      --output medical_instructions.mp3 \
>      -d '{"text": "Take \\{\"word\": \"Azathioprine\", \"pronounce\": \"æzəˈθaɪəpɹiːn\"\\} twice daily."}'
> ```

### Healthcare example

This example uses pronunciation control, which is in Early Access on Flux TTS.

**`cURL`**

```curl cURL
curl -X POST "https://api.deepgram.com/v2/speak?model=flux-haley-en" \
     -H "Authorization: token DEEPGRAM_API_KEY" \
     -H "Content-Type: application/json" \
     --output medical_instructions.mp3 \
     -d '{"text": "Take \\{\"word\": \"Azathioprine\", \"pronounce\": \"æzəˈθaɪəpɹiːn\"\\} twice daily with \\{\"word\": \"dupilumab\", \"pronounce\": \"duːˈpɪljuːmæb\"\\}."}'
```

**`Python`**

```python Python
from deepgram import DeepgramClient

client = DeepgramClient(api_key="YOUR_API_KEY")

# Inline IPA replacements with escaped curly braces
text = r'Take \{"word": "Azathioprine", "pronounce": "æzəˈθaɪəpɹiːn"\} twice daily with \{"word": "dupilumab", "pronounce": "duːˈpɪljuːmæb"\}.'

response = client.speak.v2.audio.generate(
    text=text,
    model="flux-haley-en",
    encoding="mp3",
)

audio_bytes = b"".join(response)
with open("medical_instructions.mp3", "wb") as f:
    f.write(audio_bytes)
```

**`Java`**

```java Java
import com.deepgram.DeepgramClient;
import com.deepgram.resources.speak.v2.audio.requests.SpeakV2Request;
import com.deepgram.resources.speak.v2.audio.types.AudioGenerateRequestEncoding;

import java.io.InputStream;
import java.io.FileOutputStream;

DeepgramClient client = DeepgramClient.builder().build();

// Inline IPA replacements with escaped curly braces
String text = "Take \\{\"word\": \"Azathioprine\", \"pronounce\": \"æzəˈθaɪəpɹiːn\"\\} twice daily with \\{\"word\": \"dupilumab\", \"pronounce\": \"duːˈpɪljuːmæb\"\\}.";

InputStream audioStream = client.speak().v2().audio().generate(
    SpeakV2Request.builder()
        .model("flux-haley-en")
        .text(text)
        .encoding(AudioGenerateRequestEncoding.MP3)
        .build()
);

try (FileOutputStream fos = new FileOutputStream("medical_instructions.mp3")) {
    audioStream.transferTo(fos);
}
```

> **Info**
>
> Use raw string (`r'...'`) with escaped braces `\{` and `\}` for pronunciation control in Python.

### Appointment reminder example

Speed and pause can be combined as long as `speed` stays at or below `1.15`.

**`cURL`**

```curl cURL
curl -X POST "https://api.deepgram.com/v2/speak?model=flux-haley-en&speed=0.9" \
     -H "Authorization: token DEEPGRAM_API_KEY" \
     -H "Content-Type: application/json" \
     --output appointment_reminder.mp3 \
     -d '{"text": "Your appointment is on Tuesday at 3 PM. \\{pause:800ms\\} Reply YES to confirm."}'
```

**`Python`**

```python Python
from deepgram import DeepgramClient

client = DeepgramClient(api_key="YOUR_API_KEY")

text = r"Your appointment is on Tuesday at 3 PM. \{pause:800ms\} Reply YES to confirm."

response = client.speak.v2.audio.generate(
    text=text,
    model="flux-haley-en",
    encoding="mp3",
    speed=0.9,
)

audio_bytes = b"".join(response)
with open("appointment_reminder.mp3", "wb") as f:
    f.write(audio_bytes)
```

## IPA reference

### Vowels (American English)

| Symbol | Example  | As in  |
| ------ | -------- | ------ |
| `iː`   | /biːt/   | beat   |
| `ɪ`    | /bɪt/    | bit    |
| `eɪ`   | /beɪt/   | bait   |
| `ɛ`    | /bɛt/    | bet    |
| `æ`    | /bæt/    | bat    |
| `ɑː`   | /fɑːðɚ/  | father |
| `ɔː`   | /kɔːt/   | caught |
| `oʊ`   | /boʊt/   | boat   |
| `ʊ`    | /pʊt/    | put    |
| `uː`   | /buːt/   | boot   |
| `ʌ`    | /kʌt/    | cut    |
| `ə`    | /əˈbaʊt/ | about  |

### Consonants

| Symbol | Example  | As in  |
| ------ | -------- | ------ |
| `p`    | /pɪn/    | pin    |
| `b`    | /bɪn/    | bin    |
| `t`    | /tɪn/    | tin    |
| `d`    | /dɪn/    | din    |
| `k`    | /kæt/    | cat    |
| `ɡ`    | /ɡɛt/    | get    |
| `f`    | /fɪn/    | fin    |
| `v`    | /væn/    | van    |
| `θ`    | /θɪŋk/   | think  |
| `ð`    | /ðæt/    | that   |
| `s`    | /sɪt/    | sit    |
| `z`    | /zɪp/    | zip    |
| `ʃ`    | /ʃɪp/    | ship   |
| `ʒ`    | /ˈvɪʒən/ | vision |
| `h`    | /hæt/    | hat    |
| `tʃ`   | /tʃɪp/   | chip   |
| `dʒ`   | /dʒʌmp/  | jump   |
| `m`    | /mæn/    | man    |
| `n`    | /nɛt/    | net    |
| `ŋ`    | /sɪŋ/    | sing   |
| `l`    | /lɛt/    | let    |
| `ɹ`    | /ɹɛd/    | red    |
| `w`    | /wɪn/    | win    |
| `j`    | /jɛs/    | yes    |

### Stress markers

| Symbol | Meaning          | Example                      |
| ------ | ---------------- | ---------------------------- |
| `ˈ`    | Primary stress   | /ˈæp.əl/ (apple)             |
| `ˌ`    | Secondary stress | /ˌɪnfɚˈmeɪʃən/ (information) |

## Billing

| Control       | Billing behavior                                      |
| ------------- | ----------------------------------------------------- |
| Speed         | Not billed - adjusting rate doesn't affect billing    |
| Pause         | Not billed - pause markers are removed before billing |
| Pronunciation | Billed by underlying word - IPA input is not billed   |

**Example**: `Hello, \{"word": "Mr.", "pronounce": "ˈmɪstɚ"\} Bond.` is billed as `Hello, Mr. Bond.` (16 characters)

## Reporting applied controls

### Batch response headers

Batch requests report applied controls in the response headers. Flux TTS (`/v2/speak`) and Aura-2 (`/v1/speak`) return the same headers.

```text
HTTP/1.1 200 OK
content-type: audio/mpeg
dg-request-id: 3f2a9c1e-8b4d-4e2a-9f1c-7d6e5b4a3c21
dg-model-name: flux-haley-en
dg-char-count: 47
dg-pronunciations-applied: 2
dg-breaks-applied: 0
```

| Header                      | Description                                                                                                                                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dg-pronunciations-applied` | Number of pronunciation overrides applied                                                                                                                                                          |
| `dg-breaks-applied`         | Number of pause markers applied. Always `0` on Aura-2, which does not support pause.                                                                                                               |
| `dg-warnings`               | Comma-separated `PRON-NNN` codes for pronunciation overrides that triggered an IPA warning. Present only when there are warnings. See [Pronunciation warning codes](#pronunciation-warning-codes). |

The response does not echo the `speed` value; it is the value you sent in the request.

### Streaming

On a streaming session, each turn's [`SpeechMetadata`](/docs/flux-tts/server-messages) reports `controls_applied`: `pronunciations_applied`, `breaks_applied`, and `pronunciation_warnings`.

A pronunciation override that triggers an IPA warning is still applied best-effort and counted in `pronunciations_applied`; the warning is reported separately. Listen to any term that produced a warning before you ship it.

### Pronunciation warning codes

Batch requests list these codes in `dg-warnings`. On a streaming session, the same conditions produce a `PRONUNCIATION_WARNINGS` [`Warning`](/docs/flux-tts/server-messages#warning-codes).

| Code       | Condition                                                           |
| ---------- | ------------------------------------------------------------------- |
| `PRON-001` | Invalid IPA character                                               |
| `PRON-002` | Modifier (such as `ː` or `ʰ`) follows an invalid character          |
| `PRON-003` | IPA string starts with a modifier (such as `ː`)                     |
| `PRON-004` | Tie bar (`͡`) follows a non-base character                          |
| `PRON-005` | Tie bar precedes a non-base character                               |
| `PRON-006` | IPA string ends with a tie bar                                      |
| `PRON-007` | IPA string starts with a tie bar                                    |
| `PRON-008` | Stress mark precedes a non-vowel (Aura-2 only; Flux TTS accepts it) |
| `PRON-009` | IPA string ends with a stress mark                                  |

## Error handling

Batch requests return a `400` with one of these `err_code` values:

| `err_code`                    | Trigger                                                                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| `CONTROL_COMBINATION_INVALID` | Pronunciation combined with speed, pause, or both                                                     |
| `PAUSE_SPEED_CAP_EXCEEDED`    | A pause marker with `speed` above `1.15`                                                              |
| `BREAK_OUT_OF_RANGE`          | A pause shorter than 500 ms or longer than 3000 ms                                                    |
| `BREAK_INCREMENT_INVALID`     | A pause duration off the 100 ms grid                                                                  |
| `BREAKS_LIMIT_EXCEEDED`       | More than 8 pause markers, or two pauses with no text between them                                    |
| `BREAK_SYNTAX_INVALID`        | A malformed pause marker, such as `{pause:800ms}` without backslashes or an escaped structured marker |

Invalid IPA and invalid `speed` values are also rejected. On a streaming session, see the [warning](/docs/flux-tts/server-messages#warning-codes), [ConfigureFailure](/docs/flux-tts/server-messages#configurefailure-codes), and [error](/docs/flux-tts/server-messages#error-codes) codes.

> **Note**
>
> **Aura-2** returns these errors for speed and pronunciation:
>
> ```json
> {"err_code": "speed_out_of_range", "err_msg": "Speed must be between 0.7 and 1.5"}
> ```
>
> ```json
> {"err_code": "pronunciation_invalid", "err_msg": "Invalid IPA notation for 'azathioprine'"}
> ```

## Limits

| Limit                          | Flux TTS                                           | Aura-2          |
| ------------------------------ | -------------------------------------------------- | --------------- |
| Speed range                    | 0.5 - 1.5 (0.05 increments; max 1.15 with a pause) | 0.7 - 1.5       |
| Max pause markers per request  | 8                                                  | Not supported   |
| Pause duration                 | 500 - 3000 ms (100 ms increments)                  | Not supported   |
| Max pronunciations per request | 500                                                | 500             |
| Max IPA string length          | 128 characters                                     | 128 characters  |
| Max input text length          | See [Flux TTS batch](/docs/flux-tts/batch)         | 2000 characters |
