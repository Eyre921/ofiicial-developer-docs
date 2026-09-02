---
title: "Speech Started"
source: https://developers.deepgram.com/docs/speech-started.md
path: docs/speech-started
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Speech Started

`vad_events` *boolean*.

Pre-recorded  Streaming:Nova  All available languages

Deepgram's Speech Started feature can be used for speech detection and can be used to detect the start of speech while transcribing live streaming audio.

SpeechStarted complements Voice Activity Detection (VAD) to promptly detect the start of speech post-silence. By gauging tonal nuances in human speech, the VAD can effectively differentiate between silent and non-silent audio segments, providing immediate notification of speech detection.

## Enable Feature

To enable the SpeechStarted event, include the parameter `vad_events=true` in your request:

`vad_events=true`

You'll then begin receiving messages upon speech starting.

```python Python

# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

   with client.listen.v1.connect(
            model="nova-3",
            language="en-US",
            # Apply smart formatting to the output
            smart_format=True,
            # Raw audio format details
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            # To get UtteranceEnd, the following must be set:
            interim_results=True,
            utterance_end_ms="1000",
            vad_events=True,
            # Time in milliseconds of silence to wait for before finalizing speech
            endpointing=300
   ) as connection:
```

```java Java
import com.deepgram.DeepgramClient;
import com.deepgram.resources.listen.v1.websocket.V1WebSocketClient;
import com.deepgram.resources.listen.v1.websocket.V1ConnectOptions;

DeepgramClient client = DeepgramClient.builder().build();
V1WebSocketClient wsClient = client.listen().v1().v1WebSocket();

V1ConnectOptions options = V1ConnectOptions.builder()
    .model("nova-3")
    .language("en-US")
    // Apply smart formatting to the output
    .smartFormat(true)
    // To get UtteranceEnd, the following must be set:
    .interimResults(true)
    .utteranceEndMs(1000)
    .vadEvents(true)
    // Time in milliseconds of silence to wait for before finalizing speech
    .endpointing(300)
    .build();

wsClient.connect(options).get(10, TimeUnit.SECONDS);
```

## Results

The JSON message sent when the start of speech is detected looks similar to this:

```json JSON
{
  "type": "SpeechStarted",
  "channel": [
    0,
    1
  ],
  "timestamp": 9.54
}
```

* The `type` field is always `SpeechStarted` for this event.
* The `channel` field is interpreted as `[A,B]`, where `A` is the channel index, and `B` is the total number of channels. The above example is channel 0 of single-channel audio.
* The `timestamp` field is the time at which speech was first detected.

The timestamp doesn't always match the start time of the first word in the next transcript because the systems for transcribing and timing words work independently of the speech detection system.

---
