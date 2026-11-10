---
title: "Speaker diarization"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/diarization.md
path: docs/eleven-api/guides/how-to/speech-to-text/realtime/diarization
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Speaker diarization

> **Note**
>
> **How-to guide** · Assumes you have completed the
> [client-side](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming) or
> [server-side streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming) guide.

## Overview

Speaker diarization assigns speaker IDs to words so you can distinguish who said what. With diarization enabled, partial transcripts include draft speaker labels, and each committed transcript is followed by a separate `diarized_transcript` event. Speaker labels can change as more audio arrives.

## Enabling diarization

Set the boolean query parameter `diarize=true` when opening a WebSocket connection with `model_id=scribe_v3_live`. Diarization defaults to `false`.

The following server-side examples open a connection and receive events. Install `websockets` for Python, or `ws` and the development dependency `@types/ws` for TypeScript. Set `ELEVENLABS_API_KEY` in your server's environment; the examples send it in the `xi-api-key` header. Keep this key on the server, not in browser code.

These examples do not send audio. Integrate them with your audio producer from the [server-side streaming guide](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming): send `input_audio_chunk` messages on the same connection while receiving events. The examples select `pcm_16000`, so use matching audio. In Python, run the audio-sending task concurrently with the receive loop; in TypeScript, send audio after the connection opens.

```python
import asyncio
import json
import os

from websockets.asyncio.client import connect


async def main():
    url = (
        "wss://api.elevenlabs.io/v1/speech-to-text/realtime"
        "?model_id=scribe_v3_live&audio_format=pcm_16000&diarize=true"
    )
    headers = {"xi-api-key": os.environ["ELEVENLABS_API_KEY"]}

    async with connect(url, additional_headers=headers) as websocket:
        async for message in websocket:
            event = json.loads(message)
            print(event)


if __name__ == "__main__":
    asyncio.run(main())
```

```typescript
import WebSocket from "ws";

const apiKey = process.env.ELEVENLABS_API_KEY;
if (!apiKey) {
  throw new Error("Set ELEVENLABS_API_KEY in your server environment.");
}

const websocket = new WebSocket(
  "wss://api.elevenlabs.io/v1/speech-to-text/realtime" +
    "?model_id=scribe_v3_live&audio_format=pcm_16000&diarize=true",
  { headers: { "xi-api-key": apiKey } }
);

websocket.on("message", (message) => {
  const event = JSON.parse(message.toString());
  console.log(event);
});

websocket.on("error", (error) => {
  console.error(error);
});
```

## Handling events

### Partial transcripts

With diarization enabled, each `partial_transcript` includes draft `words` in the same word shape as batch transcription. Each word's `speaker_id` is `speaker_0`, `speaker_1`, and so on once a speaker is identified, or `null` while unresolved.

Treat these words as provisional: speaker IDs and timestamps can change with more audio. Words that have not yet been aligned have no timestamps (`start` and `end` are `null` or absent).

### Committed and diarized transcripts

Diarization does not delay `committed_transcript`. With diarization enabled, this event adds a zero-based integer `segment_index`:

```json
{
  "message_type": "committed_transcript",
  "segment_index": 0,
  "text": "Hello."
}
```

Every commit is followed by a separate `diarized_transcript` event with the matching `segment_index`, `text`, and `words`:

```json
{
  "message_type": "diarized_transcript",
  "segment_index": 0,
  "text": "Hello.",
  "words": [
    {
      "text": "Hello.",
      "speaker_id": "speaker_0"
    }
  ]
}
```

The word above shows only the text and speaker label. The full word shape uses the same `start`, `end`, `type`, `logprob`, and `characters` fields as batch transcription, alongside `speaker_id`. An unresolved speaker has a `null` speaker ID.

Diarized transcripts are sent in commit order. Correlate them with committed transcripts using `segment_index`, rather than text or the next received event. A `diarized_transcript` is always sent for each commit, even if speaker identification fails; in that case, unresolved speaker IDs are `null`.

### Speaker merges

A `speakers_merged` event means two speaker IDs refer to the same person:

```json
{
  "message_type": "speakers_merged",
  "from_speaker_id": "speaker_1",
  "to_speaker_id": "speaker_0"
}
```

Replace every earlier use of `from_speaker_id` with `to_speaker_id` in both partial and diarized transcripts. Speaker IDs are never reused. Merges can chain, so apply them in receive order: if `speaker_2` merges into `speaker_1` and then `speaker_1` merges into `speaker_0`, all earlier words from both IDs must end up labeled `speaker_0`.

For example, call this handler for each received event. Here, `transcript_history` stores every partial and diarized transcript retained by the application, including earlier partial snapshots. Each merge updates all stored words in place, so chained merges also update previously merged words. Render speaker labels from this updated storage; `null` labels remain `null`.

```python
transcript_history = []


def handle_event(event):
    if event["message_type"] in ("partial_transcript", "diarized_transcript"):
        transcript_history.append(event)
    elif event["message_type"] == "speakers_merged":
        for transcript in transcript_history:
            for word in transcript.get("words") or []:
                if word.get("speaker_id") == event["from_speaker_id"]:
                    word["speaker_id"] = event["to_speaker_id"]
```

## Limitations

* Diarization is supported only by `scribe_v3_live`. Other models return an `invalid_request` error with the message `"The 'diarize' parameter is only supported by scribe_v3_live."`, then close the connection.
* Diarization cannot be combined with `filter_background_audio`. This combination returns an `invalid_request` error whose message contains `"cannot be combined with filter_background_audio"`, then closes the connection.
* Speaker labels may remain unresolved (`null`), and later `speakers_merged` events can revise earlier labels. These merge events are sent only when diarization is enabled.
