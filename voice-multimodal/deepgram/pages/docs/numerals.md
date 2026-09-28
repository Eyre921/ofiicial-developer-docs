---
title: "Numerals"
source: https://developers.deepgram.com/docs/numerals.md
path: docs/numerals
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Numerals

`numerals` *boolean* Default: `false`

Pre-recorded  Streaming:Nova Streaming:Flux  Specific languages only

Deepgram’s Numerals feature converts numbers from written format to numerical format. For example, the cardinal number "nine hundred" would appear in your transcript as "900", and the ordinal number "nine hundredth" would appear in your transcript as "900th".

Supported languages include:

* Bulgarian: `bg`
* Chinese (Cantonese, Traditional): `zh-HK`
* Danish: `da`, `da-DK`
* Dutch: `nl`
* English: `en`, `en-US`, `en-AU`, `en-GB`, `en-NZ`, `en-IN`
* French: `fr`, `fr-CA`
* German: `de`
* German (Switzerland): `de-CH`
* Italian: `it`
* Korean: `ko`, `ko-KR`
* Malay: `ms`
* Norwegian: `no`
* Polish: `pl`
* Portuguese: `pt`, `pt-BR`, `pt-PT`
* Spanish: `es`, `es-419`
* Swedish: `sv`, `sv-SE`
* Russian: `ru`
* Hebrew: `he`
* Romanian: `ro`

> **Info**
>
> When using Nova-3 Multilingual (`model=nova-3`, `language=multi`), numeral formatting is supported for: English, Spanish, French, German, Russian, Portuguese, Italian, and Dutch. Numeral formatting is not currently supported for Hindi or Japanese.

### Flux support

Numerals are supported on both Flux models:

* **Flux English** (`model=flux-general-en`) — full numeral formatting.
* **Flux Multilingual** (`model=flux-general-multi`) — numeral formatting for English, Spanish, French, German, Russian, Portuguese, Italian, and Dutch. Numeral formatting is not currently supported for Hindi or Japanese.

On Flux STT, set the initial value with the `numerals` query parameter when you open the connection. To change it mid-stream, send a [`Configure`](/docs/flux/configure) message.

**`Direct WebSocket`**

```text Direct WebSocket
wss://api.deepgram.com/v2/listen?model=flux-general-en&numerals=true&encoding=linear16&sample_rate=16000
```

## Enable Feature

To enable numerals, when you call Deepgram’s API, add a `numerals` parameter set to `true` in the query string:

`numerals=true`

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

> **Info**
>
> Be sure to replace the placeholder `YOUR_DEEPGRAM_API_KEY` with your Deepgram API Key. You can [create an API Key](/guides/fundamentals/authenticating#create-an-api-key) in the [Deepgram Console](https://console.deepgram.com).

**`cURL`**

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?numerals=true'
```

### Toggling Numerals during a real-time stream

On the streaming API (`/v1/listen`), you can turn Numerals on or off at any point during the stream. Send the following JSON message to the WebSocket:

**`JSON`**

```json JSON
{
  "type": "Configure",
  "features": {
    "numerals": true
  }
}
```

Numerals can be turned on and off multiple times during a stream if desired.

### Toggling Numerals during a Flux STT stream

On Flux STT (`/v2/listen`), send `numerals` as a top-level field in a [`Configure`](/docs/flux/configure) message, alongside `type`. Flux STT rejects the `/v1/listen` form nested under `features` and closes the connection.

**`JSON`**

```json JSON
{
  "type": "Configure",
  "numerals": true
}
```

Flux STT replies with a `ConfigureSuccess` message that echoes the full active configuration, including `numerals`. The update applies to transcripts Flux STT sends after it processes the message; it doesn't reformat transcripts it has already sent. You can toggle `numerals` as many times as needed during a stream.

> **Warning**
>
> `numerals` must be a JSON boolean. A string such as `"true"` fails schema validation: Flux STT returns a message with `type: Error` and code `UNPARSABLE_CLIENT_MESSAGE`, and closes the connection. `ConfigureFailure` can carry the same code, so check `type` to tell the two apart.

## Results

Once applied, results will appear in the transcript.

| Source                                                                                | Before numerals                                                                       | After numerals                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------- |
| My account number is nine two eight four seven three seven three nine two three seven | My account number is nine two eight four seven three seven three nine two three seven | My account number is 9 2 8 4 7 3 7 3 9 2 3 7 |

| Source                                                                                                                                                                          | Before numerals                                                                                                                                                                 | After numerals                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| My customer ID code is five one y w capital k capital p capital o six four one five lowercase d as in dog capital q lowercase p capital l z lowercase a m and then twenty three | My customer ID code is five one y w capital k capital p capital o six four one five lowercase d as in dog capital q lowercase p capital l z lowercase a m and then twenty three | My customer ID code is 5 1 y w capital k capital p capital o 6 4 1 5 lowercase d as in dog capital q lowercase p capital l z lowercase a m and then 23 |

| Source                                                                                                                                                | Before numerals                                                                                                                                       | After numerals                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| My phone number is five five five two one two four three nine four and I live at five five five main street new york new york one zero zero zero five | My phone number is five five five two one two four three nine four and I live at five five five main street new york new york one zero zero zero five | My phone number is 5 5 5 2 1 2 4 3 9 4 and I live at 5 5 5 main street new york new york 1 0 0 0 5 |

| Source                                 | Before numerals                        | After numerals                |
| -------------------------------------- | -------------------------------------- | ----------------------------- |
| My date of birth is june twenty eighth | My date of birth is june twenty eighth | My date of birth is june 28th |

> **Info**
>
> When punctuation is enabled, converted numbers do not include it. For example, 999,999 will always be transcribed as 999999.
