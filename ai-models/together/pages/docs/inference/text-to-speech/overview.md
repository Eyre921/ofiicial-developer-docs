---
title: "Generate speech"
source: https://docs.together.ai/docs/inference/text-to-speech/overview
path: docs/inference/text-to-speech/overview
---

Generate speech audio from text with Together AI text-to-speech models.

<Tip>
  Using a coding agent? Install the [together-audio](https://github.com/togethercomputer/skills/tree/main/skills/together-audio) skill to let your agent write correct text-to-speech code automatically. See [agent skills](/docs/agent-skills) for details.
</Tip>

Together AI hosts text-to-speech models with multiple delivery methods. Use this page for the basics: making a request, picking a model, and configuring parameters. For real-time delivery, see [Streaming](/docs/inference/text-to-speech/streaming) and [WebSocket](/docs/inference/text-to-speech/websocket).

<Tip>
  Read the [end-to-end guide](/docs/how-to-build-phone-voice-agent) to build a live voice agent powered by Together AI's real-time STT and TTS pipeline.
</Tip>

## Quickstart

Basic text-to-speech request:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  speech_file_path = "speech.mp3"

  with client.audio.speech.with_streaming_response.create(
      model="canopylabs/orpheus-3b-0.1-ft",
      input="Today is a wonderful day to build something people love!",
      voice="tara",
      response_format="mp3",
  ) as response:
      response.stream_to_file(speech_file_path)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function generateAudio() {
    const res = await together.audio.speech.create({
      input: 'Hello, how are you today?',
      voice: 'tara',
      response_format: 'mp3',
      sample_rate: 24000,
      stream: false,
      model: 'canopylabs/orpheus-3b-0.1-ft',
    });

    if (res.body) {
      console.log(res.body);
      const nodeStream = Readable.from(res.body as ReadableStream);
      const fileStream = createWriteStream('./speech.mp3');

      nodeStream.pipe(fileStream);
    }
  }

  generateAudio();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/audio/speech" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "canopylabs/orpheus-3b-0.1-ft",
         "input": "The quick brown fox jumps over the lazy dog",
         "voice": "tara",
         "response_format": "mp3"
       }' \
       --output speech.mp3
  ```
</CodeGroup>

Outputs a `speech.mp3` file.

## Available models

For the current list of text-to-speech models, see the [serverless catalog](/docs/serverless/models) or the [dedicated model inference catalog](/docs/dedicated-endpoints/models).

## Parameters

| Parameter            | Type    | Required | Description                                                                                                                                                                                               |
| :------------------- | :------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model                | string  | Yes      | The TTS model to use                                                                                                                                                                                      |
| input                | string  | Yes      | The text to generate audio for                                                                                                                                                                            |
| voice                | string  | Yes      | The voice to use for generation. See [Voices](#supported-voices) section                                                                                                                                  |
| response\_format     | string  | No       | Output format: `mp3`, `wav`, `raw` (PCM), `mulaw` (μ-law). Minimax model also supports `opus`, `aac`, and `flac`. Default: `wav`                                                                          |
| sample\_rate         | integer | No       | The sample rate of the output audio in Hz (e.g., `24000`, `44100`)                                                                                                                                        |
| bit\_rate            | integer | No       | MP3 bitrate in bits per second. Only applies when `response_format` is `mp3`. Valid values: `32000`, `64000`, `96000`, `128000`, `192000`. Default: `128000`. Currently supported on Cartesia models.     |
| language             | string  | No       | The language or locale code for speech synthesis (e.g., `en`, `fr`, `es`). Locales are supported and must be lowercase (e.g., `zh-hk` for Cantonese)                                                      |
| alignment            | string  | No       | Controls word-level timestamp generation. Set to `word` to receive word timestamps, or `none` to disable (default: `none`)                                                                                |
| segment              | string  | No       | Controls how text is segmented before synthesis. Options: `sentence` (default), `immediate`, `never`                                                                                                      |
| extra\_params        | object  | No       | Additional model-specific parameters. Supported fields:                                                                                                                                                   |
| `pronunciation_dict` | array   | No       | A list of pronunciation rules for specific characters or symbols. Each entry uses the format `"<source>/<replacement>"` (e.g., `["omg/oh my god"]`) to override how the model pronounces matching tokens. |

<Note>
  Word alignment (`alignment=word`) is only supported for streaming requests.
</Note>

For the full set of parameters refer to the API reference for [/audio/speech](/reference/audio-speech).

## Response formats

Together AI supports multiple audio formats:

| Format | Extension | Description                                                           | Streaming Support |
| :----- | :-------- | :-------------------------------------------------------------------- | :---------------- |
| wav    | .wav      | Uncompressed audio (larger file size)                                 | No                |
| mp3    | .mp3      | Compressed audio (smaller file size)                                  | No                |
| raw    | .pcm      | Raw PCM audio data                                                    | Yes               |
| mulaw  | .ulaw     | Uses logarithmic compression to optimize speech quality for telephony | Yes               |

## Best practices

### Choose the right delivery method

* **Basic HTTP API:** Best for batch processing or when you need complete audio files.
* **Streaming HTTP API:** Best for real-time applications where TTFB matters. See [Streaming](/docs/inference/text-to-speech/streaming).
* **WebSocket API:** Best for interactive applications requiring lowest latency (chatbots, live assistants). See [WebSocket](/docs/inference/text-to-speech/websocket).

### Performance tips

* Use streaming when you need the fastest time-to-first-byte.
* Use the WebSocket API for conversational applications.
* Buffer text appropriately. Sentence boundaries work best for natural speech.
* Use the `max_partial_length` parameter in WebSocket to control buffer behavior.
* Consider using `raw` (PCM) format for lowest latency, then encode client-side if needed.

### Voice selection

* Test different voices to find the best match for your application.
* Some voices are better suited for specific content types (narration vs conversation).
* Use the Voices API to discover all available options.

## Supported voices

Some of the supported voices for each model are shown below. For the full list of available voices, query the `/v1/voices` endpoint.

### Voices API

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # List all available voices
  response = client.audio.voices.list()

  for model_voices in response.data:
      print(f"Model: {model_voices.model}")
      for voice in model_voices.voices:
          print(f"  - Voice: {voice.name}")
  ```

  ```typescript TypeScript theme={null}
  import fetch from 'node-fetch';

  async function getVoices() {
    const apiKey = process.env.TOGETHER_API_KEY;
    const model = 'canopylabs/orpheus-3b-0.1-ft';
    const url = `https://api.together.ai/v1/voices?model=${model}`;

    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });

    const data = await response.json();
    
    console.log(`Available voices for ${model}:`);
    console.log('='.repeat(50));
    
    // List available voices
    for (const voice of data.voices || []) {
      console.log(voice.name || 'Unknown voice');
    }
  }

  getVoices();
  ```

  ```bash cURL theme={null}
  curl -X GET "https://api.together.ai/v1/voices?model=canopylabs/orpheus-3b-0.1-ft" \
       -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

### Available voices

#### Orpheus model

Sample voices include:

```text Text theme={null}
`tara`
`leah`
`jess`
`leo`
`dan`
`mia`
`zac`
`zoe`
```

#### Kokoro model

```text Text theme={null}
af_heart
af_alloy
af_aoede
af_bella
af_jessica
af_kore
af_nicole
af_nova
af_river
af_sarah
af_sky
am_adam
am_echo
am_eric
am_fenrir
am_liam
am_michael
am_onyx
am_puck
am_santa
bf_alice
bf_emma
bf_isabella
bf_lily
bm_daniel
bm_fable
bm_george
bm_lewis
jf_alpha
jf_gongitsune
jf_nezumi
jf_tebukuro
jm_kumo
zf_xiaobei
zf_xiaoni
zf_xiaoxiao
zf_xiaoyi
zm_yunjian
zm_yunxi
zm_yunxia
zm_yunyang
ef_dora
em_alex
em_santa
ff_siwis
hf_alpha
hf_beta
hm_omega
hm_psi
if_sara
im_nicola
pf_dora
pm_alex
pm_santa
```

##### Voice mixing (Kokoro only)

Kokoro supports combining two or more voices into a single blended voice by joining their names with `+`. This can be useful for creating custom voice characteristics that aren't available from any single voice on its own.

* **Equal weights:** `af_bella+af_heart` blends the two voices in equal proportion.
* **Custom weights:** `af_bella(2)+af_heart(1)` weights `af_bella` twice as heavily as `af_heart`. Weights can be integers or decimals.
* **More than two voices:** `af_bella(1)+af_heart(1)+am_adam(0.5)`. Any number of components is supported.

<Note>
  Voice mixing is only supported for `hexgrad/Kokoro-82M`. Other TTS models require a single voice name.
</Note>

Example:

```bash cURL theme={null}
curl -X POST "https://api.together.ai/v1/audio/speech" \
     -H "Authorization: Bearer $TOGETHER_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "hexgrad/Kokoro-82M",
       "input": "The quick brown fox jumps over the lazy dog",
       "voice": "af_bella+af_heart",
       "response_format": "mp3"
     }' \
     --output speech.mp3
```

#### Cartesia models

All valid voices supported by Cartesia are supported.

<Note>
  You need to pass in the voice ID instead of the name. Model strings are deprecated and will not be supported in future.
</Note>

#### Rime Mist v2, v3 models

```text Text theme={null}
'cove'
'lagoon'
'mari'
'moon'
'moraine'
'peak'
'summit'
'talon'
'thunder'
'tundra'
'wildflower'
```

#### Rime Arcana v2, v3, and v3 Turbo models

<Note>
  Rime Arcana v3 and Arcana v3 Turbo are multilingual models.
</Note>

```text Text theme={null}
'albion'
'arcade'
'astra'
'atrium'
'bond'
'cupola'
'eliphas'
'estelle'
'eucalyptus'
'fern'
'lintel'
'luna'
'lyra'
'marlu'
'masonry'
'moss'
'oculus'
'parapet'
'pilaster'
'sirius'
'stucco'
'transom'
'truss'
'vashti'
'vespera'
'walnut'
```

#### Minimax Speech 2.6 Turbo model

Sample voices include:

```text Text theme={null}
'English_DeterminedMan'
'English_Diligent_Man'
'English_expressive_narrator'
'English_FriendlyNeighbor'
'English_Graceful_Lady'
'Japanese_GentleButler'
```

#### Minimax Speech 2.8 Turbo model

Sample voices include:

```text Text theme={null}
'English_CalmWoman'
'English_CaptivatingStoryteller'
'English_CharmingQueen'
'English_Comedian'
'English_ConfidentWoman'
'English_Cute_Girl'
```

## Pricing

| Model            | Price                  |
| :--------------- | :--------------------- |
| Orpheus 3B       | \$15 per 1M characters |
| Kokoro           | \$4 per 1M characters  |
| Cartesia Sonic 2 | \$65 per 1M characters |

## Next steps

* [Streaming](/docs/inference/text-to-speech/streaming): stream audio over HTTP for low time-to-first-byte, plus how to extract raw PCM bytes.
* [WebSocket API](/docs/inference/text-to-speech/websocket): stream text in and audio out over a single WebSocket for the lowest interactive latency, including multi-context support.
* [API reference](/reference/audio-speech) for detailed parameter documentation.
* [Speech-to-text](/docs/inference/transcription/overview) for the reverse operation.
* [PDF to Podcast guide](/docs/open-notebooklm-pdf-to-podcast) for a complete example.
