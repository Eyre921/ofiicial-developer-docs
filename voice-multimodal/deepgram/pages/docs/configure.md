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

Use the `Configure` message to change settings on an open `/v1/listen` WebSocket stream. The stream keeps running, so you don't drop audio or rebuild state to change what Deepgram listens for.

> **Info**
>
> Updating Nova-3 `keyterms` with `Configure` on `/v1/listen` is available on the global endpoint (`api.deepgram.com`). It isn't available yet on the EU (`api.eu.deepgram.com`), Australia (`api.au.deepgram.com`), or India (`api.in.deepgram.com`) [regional endpoints](/reference/regional-endpoints).

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

### No Acknowledgement on Success

A successful `Configure` on `/v1/listen` produces no response message; the next transcripts reflect the new settings. This differs from [Flux STT](/docs/flux/configure), which replies with `ConfigureSuccess`.

### Keyterm Syntax and Limits

Each array entry is a plain term or phrase. Pass a multi-word phrase as a single entry, for example `["customer service"]`. Like the `keyterm` query parameter, entries don't support the weight syntax from the legacy [Keywords](/docs/keywords) feature, so don't append a weight such as `"term:0.15"`.

The 500-token [keyterm limit](/docs/keyterm#key-term-limits) that applies to the `keyterm` query parameter also applies to each `Configure` message. Keep each list to the terms that matter for the current step of the conversation instead of sending everything you might need. If an update goes over the limit, Deepgram rejects it with an [error](#errors) and the stream keeps its previous keyterms.

## Errors

Rejected `Configure` messages return an `Error` message. The stream stays open with its previous settings.

Sending `keyterms` on a model other than Nova-3, such as Nova-2:

**`JSON`**

```json JSON
{
  "type": "Error",
  "variant": "InvalidConfigureMessage",
  "description": "`keyterms` are only supported for Nova-3 and Flux.",
  "code": "KeytermsNotSupported"
}
```

Sending keyterms over the 500-token [keyterm limit](/docs/keyterm#key-term-limits) returns an `InvalidConfigureMessage` error whose `description` explains the limit. The stream keeps its previous keyterms.

Sending a field the message doesn't support, for example `keyterm` instead of `keyterms`:

**`JSON`**

```json JSON
{
  "type": "Error",
  "variant": "SchemaError",
  "description": "Could not deserialize last text message: unknown field `keyterm`, expected one of `features`, `processors`, `keyterms`, `language_hints`",
  "message": "{\"type\": \"Configure\", \"keyterm\": [\"Deepgram\"]}"
}
```

## Language-Specific Implementations

These examples open a Nova-3 stream and update its keyterms partway through.

**`Python`**

```python Python
import asyncio
import json
import os

import websockets

URL = "wss://api.deepgram.com/v1/listen?model=nova-3&encoding=linear16&sample_rate=16000"
HEADERS = {"Authorization": f"Token {os.environ['DEEPGRAM_API_KEY']}"}


async def main():
    async with websockets.connect(URL, additional_headers=HEADERS) as ws:
        # Stream audio with ws.send(audio_bytes) ...

        # The caller is about to give their account manager's name.
        await ws.send(json.dumps({
            "type": "Configure",
            "keyterms": ["Zyphorra Quillbeck", "Xylofex Dynamics"],
        }))

        # Keep streaming; later transcripts use the new keyterms.


asyncio.run(main())
```

**`JavaScript`**

```javascript JavaScript
const WebSocket = require("ws");

const ws = new WebSocket(
  "wss://api.deepgram.com/v1/listen?model=nova-3&encoding=linear16&sample_rate=16000",
  { headers: { Authorization: `Token ${process.env.DEEPGRAM_API_KEY}` } }
);

ws.on("open", () => {
  // Stream audio with ws.send(audioChunk) ...

  // The caller is about to give their account manager's name.
  ws.send(
    JSON.stringify({
      type: "Configure",
      keyterms: ["Zyphorra Quillbeck", "Xylofex Dynamics"],
    })
  );
});
```

## Related Resources

* [Keyterm Prompting](/docs/keyterm): choosing keyterms and setting them when you open a stream
* [Numerals](/docs/numerals): converting spoken numbers to digits
* [Flux STT Configure](/docs/flux/configure): the equivalent message for Flux STT (`/v2/listen`)
* [Finalize](/docs/finalize) and [Close Stream](/docs/close-stream): other streaming control messages
