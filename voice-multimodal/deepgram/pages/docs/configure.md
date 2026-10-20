---
title: "Configure"
source: https://developers.deepgram.com/docs/configure.md
path: docs/configure
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Configure

Streaming:Nova

Use the `Configure` message to change settings on an open `/v1/listen` WebSocket stream. The stream keeps running whether the update succeeds or fails, so you don't drop audio or rebuild state to change what Deepgram listens for.

## Purpose

What a voice application needs from speech recognition changes during a call. A caller confirms their name, then reads out an order number, then asks about a specific product. With `Configure`, you can:

* **Load the vocabulary for the current step.** Add the caller's name to [keyterms](/docs/keyterm) right before you ask for it, or swap in product names when the conversation moves to a product inquiry. You don't have to load every term you might need at the start of the call.
* **Switch formatting per step.** Turn on [Numerals](/docs/numerals) before you ask for a PIN or phone number, then turn it off for free-form speech.

## Configurable Fields

| Field      | Type             | Description                                                                                                                                                                                                                                               |
| ---------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keyterms` | array of strings | Replaces the stream's [keyterms](/docs/keyterm). Works on Nova-3 models only, including monolingual, multilingual, and Nova-3 Medical models. An empty array `[]` clears all keyterms. Omit the field, or set it to `null`, to keep the current keyterms. |
| `features` | object           | Turns formatting features on or off. Each key is a feature name and each value is a boolean, for example `{"numerals": true}`. See [Numerals](/docs/numerals#toggling-numerals-during-a-real-time-stream).                                                |

Both fields are optional, and you can send them in the same message. A field you omit keeps its current value.

## Example Payloads

**`Update keyterms`**

```json Update keyterms
{
  "type": "Configure",
  "keyterms": ["Deepgram", "Nova-3", "customer service"]
}
```

**`Clear keyterms`**

```json Clear keyterms
{
  "type": "Configure",
  "keyterms": []
}
```

**`Keyterms and numerals together`**

```json Keyterms and numerals together
{
  "type": "Configure",
  "keyterms": ["account number", "routing number"],
  "features": {
    "numerals": true
  }
}
```

## Behavior

### Each Keyterms Array Replaces the List

Each `keyterms` array replaces the whole list, including any keyterms you set with the `keyterm` query parameter when you opened the stream. To add a term, send the existing terms plus the new one.

| Initial keyterms      | Configure message                                                 | Active keyterms afterward         |
| --------------------- | ----------------------------------------------------------------- | --------------------------------- |
| `["apple", "banana"]` | `{"type": "Configure", "keyterms": ["grape"]}`                    | `["grape"]`                       |
| `["apple", "banana"]` | `{"type": "Configure", "keyterms": ["apple", "banana", "grape"]}` | `["apple", "banana", "grape"]`    |
| `["apple", "banana"]` | `{"type": "Configure", "keyterms": []}`                           | none                              |
| `["apple", "banana"]` | `{"type": "Configure", "features": {"numerals": true}}`           | `["apple", "banana"]` (unchanged) |

### Timing

Deepgram processes `Configure` in order with your audio. The new settings apply to audio it hasn't transcribed yet when it processes the message. That can include audio you sent shortly before the message, but transcripts it has already returned aren't revised. Updates stay in effect until the stream ends or you send another `Configure`.

### Same Behavior as Connection-Time Keyterms

Keyterms set with `Configure` behave exactly like keyterms set with the `keyterm` query parameter when you open the stream. This holds on every Nova-3 streaming model, monolingual or multilingual. How much keyterms improve recognition depends on the language and the terms, and that's the same whichever way you set them.

### Keyterm Syntax and Limits

Each array entry is a plain term or phrase. Pass a multi-word phrase as a single entry, for example `["customer service"]`. Like the `keyterm` query parameter, entries don't support the weight syntax from the legacy [Keywords](/docs/keywords) feature, so don't append a weight such as `"term:0.15"`.

The 500-token [keyterm limit](/docs/keyterm#key-term-limits) that applies to the `keyterm` query parameter also applies to each `Configure` message. Keep each list to the terms that matter for the current step of the conversation instead of sending everything you might need. An over-limit update returns a `ConfigureFailure` with code `CONFIGURE_KEYTERM_LIMIT_EXCEEDED`.

## Responses

Deepgram answers every `Configure` with exactly one `ConfigureSuccess` or `ConfigureFailure` message. Both include the stream's `request_id`.

### ConfigureSuccess

`ConfigureSuccess` confirms that the update took effect. When the message replaced the keyterms, `keyterms` lists the keyterms now in effect. Fields the message didn't change are omitted.

**`JSON`**

```json JSON
{
  "type": "ConfigureSuccess",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "keyterms": ["Deepgram", "Nova-3", "customer service"]
}
```

### ConfigureFailure

`ConfigureFailure` means Deepgram rejected the whole message and applied none of it, including any `features` sent alongside `keyterms`. The stream stays open with its previous settings.

**`JSON`**

```json JSON
{
  "type": "ConfigureFailure",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "code": "CONFIGURE_KEYTERMS_NOT_SUPPORTED",
  "description": "`keyterms` are not supported by this model."
}
```

| Code                               | Cause                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------- |
| `CONFIGURE_KEYTERMS_NOT_SUPPORTED` | The stream's model isn't Nova-3, such as Nova-2.                                  |
| `CONFIGURE_KEYTERM_LIMIT_EXCEEDED` | The keyterms exceed the 500-token [keyterm limit](/docs/keyterm#key-term-limits). |
| `CONFIGURE_ALREADY_PENDING`        | You sent a `Configure` before the previous one received its response.             |
| `CONFIGURE_INTERNAL_ERROR`         | Deepgram failed to apply the update.                                              |

### One Update at a Time

Deepgram processes one `Configure` at a time. Wait for `ConfigureSuccess` or `ConfigureFailure` before sending the next one; a `Configure` sent while another is pending returns `CONFIGURE_ALREADY_PENDING`.

`/v1/listen` responses carry no `sequence_id`, unlike [Flux STT](/docs/flux/configure) responses.

## Errors

Sending a field the message doesn't support, for example `keyterm` instead of `keyterms`, returns an `Error` message. The stream stays open with its previous settings.

**`JSON`**

```json JSON
{
  "type": "Error",
  "variant": "SchemaError",
  "description": "Could not deserialize last text message: unknown field `keyterm`, expected one of `features`, `keyterms`",
  "message": "{\"type\": \"Configure\", \"keyterm\": [\"Deepgram\"]}"
}
```

## Language-Specific Implementations

These examples open a Nova-3 stream, update its keyterms partway through, and handle the response.

**`Python`**

```python Python
import asyncio
import json
import os

import websockets

# Configure keyterms work on Nova-3 models only.
URL = "wss://api.deepgram.com/v1/listen?model=nova-3&encoding=linear16&sample_rate=16000"
HEADERS = {"Authorization": f"Token {os.environ['DEEPGRAM_API_KEY']}"}

async def receive(ws):
    # ConfigureSuccess and ConfigureFailure arrive interleaved with Results.
    async for raw in ws:
        message = json.loads(raw)
        # ConfigureSuccess echoes keyterms only when the Configure replaced them.
        if message["type"] == "ConfigureSuccess":
            print("Keyterms now in effect:", message.get("keyterms"))
        # ConfigureFailure applied nothing; the stream keeps its previous settings.
        elif message["type"] == "ConfigureFailure":
            print("Configure rejected:", message["code"], message["description"])
        elif message["type"] == "Results":
            print(message["channel"]["alternatives"][0]["transcript"])

async def main():
    async with websockets.connect(URL, additional_headers=HEADERS) as ws:
        # Read server messages on a background task so sending audio isn't blocked.
        receiver = asyncio.create_task(receive(ws))

        # Stream audio with ws.send(audio_bytes) ...

        # The caller is about to give their account manager's name.
        # Wait for this Configure's response before sending another, or
        # Deepgram returns CONFIGURE_ALREADY_PENDING.
        await ws.send(json.dumps({
            "type": "Configure",
            "keyterms": ["Zyphorra Quillbeck", "Xylofex Dynamics"],
        }))

        # Keep streaming; later transcripts use the new keyterms.
        await receiver

asyncio.run(main())

```

**`JavaScript`**

```javascript JavaScript
const WebSocket = require("ws");

// Configure keyterms work on Nova-3 models only.
const ws = new WebSocket(
  "wss://api.deepgram.com/v1/listen?model=nova-3&encoding=linear16&sample_rate=16000",
  { headers: { Authorization: `Token ${process.env.DEEPGRAM_API_KEY}` } }
);

ws.on("open", () => {
  // Stream audio with ws.send(audioChunk) ...

  // The caller is about to give their account manager's name.
  // Wait for this Configure's response before sending another, or
  // Deepgram returns CONFIGURE_ALREADY_PENDING.
  ws.send(
    JSON.stringify({
      type: "Configure",
      keyterms: ["Zyphorra Quillbeck", "Xylofex Dynamics"],
    })
  );
});

// ConfigureSuccess and ConfigureFailure arrive interleaved with Results.
ws.on("message", (data) => {
  const message = JSON.parse(data);
  // ConfigureSuccess echoes keyterms only when the Configure replaced them.
  if (message.type === "ConfigureSuccess") {
    console.log("Keyterms now in effect:", message.keyterms);
  // ConfigureFailure applied nothing; the stream keeps its previous settings.
  } else if (message.type === "ConfigureFailure") {
    console.log("Configure rejected:", message.code, message.description);
  } else if (message.type === "Results") {
    console.log(message.channel.alternatives[0].transcript);
  }
});
```

## Related Resources

* [Keyterm Prompting](/docs/keyterm): choosing keyterms and setting them when you open a stream
* [Numerals](/docs/numerals): converting spoken numbers to digits
* [Flux STT Configure](/docs/flux/configure): the equivalent message for Flux STT (`/v2/listen`)
* [Finalize](/docs/finalize) and [Close Stream](/docs/close-stream): other streaming control messages
