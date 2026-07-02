---
title: "Text-to-speech streaming"
source: https://docs.together.ai/docs/inference/text-to-speech/streaming
path: docs/inference/text-to-speech/streaming
---

Stream audio over HTTP for low time-to-first-byte and access raw PCM bytes.

For real-time applications where time-to-first-byte (TTFB) is critical, use streaming mode. Streaming returns a sequence of server-sent events containing base64-encoded audio chunks, so playback can start before generation finishes.

For the lowest possible interactive latency (and bidirectional text input), see the [WebSocket API](/docs/inference/text-to-speech/websocket).

## Streaming audio

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # Save the streamed audio to a file
  with client.audio.speech.with_streaming_response.create(
      model="canopylabs/orpheus-3b-0.1-ft",
      input="The quick brown fox jumps over the lazy dog",
      voice="tara",
      stream=True,
      response_format="raw",  # Required for streaming
      response_encoding="pcm_s16le",  # 16-bit PCM for clean audio
  ) as response:
      response.stream_to_file("speech_streaming.pcm")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function streamAudio() {
    const response = await together.audio.speech.create({
      model: 'canopylabs/orpheus-3b-0.1-ft',
      input: 'The quick brown fox jumps over the lazy dog',
      voice: 'tara',
      stream: true,
      response_format: 'raw',  // Required for streaming
      response_encoding: 'pcm_s16le'  // 16-bit PCM for clean audio
    });

    // Process streaming chunks
    const chunks = [];
    for await (const chunk of response) {
      chunks.push(chunk);
    }

    console.log('Streaming complete!');
  }

  streamAudio();
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/audio/speech" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "canopylabs/orpheus-3b-0.1-ft",
         "input": "The quick brown fox jumps over the lazy dog",
         "voice": "tara",
         "stream": true
       }'
  ```
</CodeGroup>

## Streaming response format

When `stream: true`, the API returns a stream of server-sent events.

**Audio chunk:**

```
data: {"type":"conversation.item.audio_output.delta","item_id":"tts_1","delta":"<base64_encoded_audio>"}
```

**Word timestamps** (when `alignment=word`):

```
data: {"type":"conversation.item.word_timestamps","words":["Hello","world"],"start_seconds":[0.0,0.4],"end_seconds":[0.4,0.8]}
```

**Stream end:**

```
data: [DONE]
```

<Note>
  When streaming is enabled, only `raw` (PCM) format is supported. For non-streaming requests, you can use `mp3`, `wav`, or `raw`.
</Note>

## Output raw bytes

If you want to extract raw audio bytes (for example, to feed into a custom audio pipeline), use the settings below.

<CodeGroup>
  ```python Python theme={null}
  import requests
  import os

  url = "https://api.together.ai/v1/audio/speech"
  api_key = os.environ.get("TOGETHER_API_KEY")

  headers = {"Authorization": f"Bearer {api_key}"}

  data = {
      "input": "This is a test of raw PCM audio output.",
      "voice": "tara",
      "response_format": "raw",
      "response_encoding": "pcm_s16le",
      "sample_rate": 24000,
      "stream": False,
      "model": "canopylabs/orpheus-3b-0.1-ft",
  }

  response = requests.post(url, headers=headers, json=data)

  with open("output_raw.pcm", "wb") as f:
      f.write(response.content)

  print(f"Raw PCM audio saved to output_raw.pcm")
  print(f"   Size: {len(response.content)} bytes")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function generateRawBytes() {
    const res = await together.audio.speech.create({
      input: 'Hello, how are you today?',
      voice: 'tara',
      response_format: 'raw',
      response_encoding: 'pcm_s16le',
      sample_rate: 24000,
      stream: false,
      model: 'canopylabs/orpheus-3b-0.1-ft',
    });

    console.log(res.body);
  }

  generateRawBytes();
  ```

  ```bash cURL theme={null}
  curl --location 'https://api.together.ai/v1/audio/speech' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $TOGETHER_API_KEY" \
  --output test2.pcm \
  --data '{
      "input": "Hello, this is a test of the text-to-speech system.",
      "voice": "tara",
      "response_format": "raw",
      "response_encoding": "pcm_s16le",
      "sample_rate": 24000,
      "stream": false,
      "model": "canopylabs/orpheus-3b-0.1-ft"
  }'
  ```
</CodeGroup>

This writes the raw bytes to a `test2.pcm` file.

## See also

* [Text-to-speech overview](/docs/inference/text-to-speech/overview) for parameters, response formats, voices, and pricing.
* [WebSocket API](/docs/inference/text-to-speech/websocket) for the lowest-latency, bidirectional streaming option.
