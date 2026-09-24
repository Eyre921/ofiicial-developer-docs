---
title: "Transcript editing"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcript-editing.md
path: docs/eleven-api/guides/how-to/speech-to-text/realtime/transcript-editing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Transcript editing

> **Note**
>
> **How-to guide** · Assumes you have completed the
> [client-side](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming) or
> [server-side streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming) guide.

## Overview

> **Warning**
>
> Transcript editing is an experimental feature and adds a 30% premium to the base transcription
> cost, billed for at least 10 seconds of audio per committed transcript. See the [API pricing page](https://elevenlabs.io/pricing?price.section=speech_to_text\&price.sections=speech_to_text,speech_to_text#pricing-table)
> for detailed pricing information.

Realtime transcription can apply a natural-language edit instruction to every committed transcript, for example to write spoken dates in a fixed format or to expand abbreviations and acronyms. The instruction is passed once when the connection is opened, and each committed transcript is followed by a separate `edited_transcript` event with the edited text.

Partial transcripts are never edited. The `committed_transcript` event is not changed either, so existing integrations keep working when you turn the feature on.

> **Warning**
>
> Transcript editing cannot be combined with `entity_detection`. Connections that set both are
> rejected with an `invalid_request` error.

## Enabling transcript editing

Pass the instruction with the `transcriptEdit` option when connecting (the `transcript_edit` query parameter of the WebSocket API). The instruction can be up to 2000 characters long. See the [batch transcript editing guide](/docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing#writing-instructions) for guidance on writing instructions.

In all SDKs the edited transcripts arrive through the `RealtimeEvents.EDITED_TRANSCRIPT` event.

### Client-side

Use `@elevenlabs/client` in the browser with a single-use token issued by your server, as described in the [client-side streaming guide](/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming).

```typescript
import { Scribe, RealtimeEvents } from "@elevenlabs/client";

// Fetch a single-use token from your server first
const response = await fetch("/scribe-token", yourAuthHeaders);
const { token } = await response.json();

const connection = Scribe.connect({
  token,
  modelId: "scribe_v2_realtime",
  transcriptEdit: "Write all dates in ISO 8601 format (YYYY-MM-DD)",
  microphone: {
    echoCancellation: true,
    noiseSuppression: true,
  },
});

connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, (data) => {
  console.log("Committed:", data.text);
});

connection.on(RealtimeEvents.EDITED_TRANSCRIPT, (data) => {
  console.log("Edited:", data.edited_text);
});
```

### Server-side

Use the official SDK on your server, as described in the [server-side streaming guide](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming#configure-the-sdk). Only the option and the event handler differ from that guide; sending audio and closing the connection work the same way.

```python
import asyncio
import os
from dotenv import load_dotenv
from elevenlabs import AudioFormat, ElevenLabs, RealtimeAudioOptions, RealtimeEvents

load_dotenv()

async def main():
    elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    connection = await elevenlabs.speech_to_text.realtime.connect(RealtimeAudioOptions(
        model_id="scribe_v2_realtime",
        audio_format=AudioFormat.PCM_16000,
        sample_rate=16000,
        transcript_edit="Write all dates in ISO 8601 format (YYYY-MM-DD)",
    ))

    def on_committed_transcript(data):
        print(f"Committed: {data.get('text', '')}")

    def on_edited_transcript(data):
        print(f"Edited: {data.get('edited_text', '')}")

    connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, on_committed_transcript)
    connection.on(RealtimeEvents.EDITED_TRANSCRIPT, on_edited_transcript)

    # Send audio chunks as shown in the server-side streaming guide, then close.
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
```

```typescript
import { ElevenLabsClient, RealtimeEvents, AudioFormat } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const connection = await elevenlabs.speechToText.realtime.connect({
  modelId: "scribe_v2_realtime",
  audioFormat: AudioFormat.PCM_16000,
  sampleRate: 16000,
  transcriptEdit: "Write all dates in ISO 8601 format (YYYY-MM-DD)",
});

connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, (data) => {
  console.log("Committed:", data.text);
});

connection.on(RealtimeEvents.EDITED_TRANSCRIPT, (data) => {
  console.log("Edited:", data.edited_text);
});

// Send audio chunks as shown in the server-side streaming guide, then close.
```

## Receiving edited transcripts

When enabled, each committed transcript is followed by an `edited_transcript` event carrying the committed text and its edited version:

```json
{
  "message_type": "edited_transcript",
  "text": "our next meeting is on the twelfth of July twenty twenty-six",
  "edited_text": "our next meeting is on 2026-07-12"
}
```

Behavior to be aware of:

* Edits are applied per committed segment. The `edited_transcript` event is emitted shortly after the corresponding `committed_transcript` event, since editing runs asynchronously. It may arrive after the next partial transcript, and edits for consecutive segments may arrive out of order. Use the `text` field to match an edit to its committed transcript.
* If no edits were made to a segment, `edited_text` is identical to `text`.
* If an edit cannot be produced for a segment, no `edited_transcript` event is sent for it. The `committed_transcript` event is not affected.
* Word-level timestamps in `committed_transcript_with_timestamps` describe the original committed text, not the edited text.

## Next steps

#### [Batch transcript editing](/docs/eleven-api/guides/how-to/speech-to-text/batch/transcript-editing)

Instruction writing guidance and the batch response format.

#### [Event reference](/docs/eleven-api/guides/how-to/speech-to-text/realtime/event-reference)

Full list of events and error types from the realtime STT API.
