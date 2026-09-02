---
title: "Encoding"
source: https://developers.deepgram.com/docs/tts-encoding.md
path: docs/tts-encoding
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Encoding

`encoding` *string*Default: `mp3`

Text to Speech Request  Text to Speech Stream  English Only

The Encoding feature gives users the ability to specify the desired format of the resulting text-to-speech audio output.

| Encoding     | Description                                 | Availability        |
| ------------ | ------------------------------------------- | ------------------- |
| **linear16** | 16-bit, little-endian, signed PCM WAV data. | `REST` ,`Streaming` |
| **mulaw**    | Mu-law encoded WAV data.                    | `REST` ,`Streaming` |
| **alaw**     | A-law encoded WAV data.                     | `REST` ,`Streaming` |
| **mp3**      | MP3 audio compression format.               | `REST`              |
| **opus**     | Ogg Opus codec.                             | `REST`              |
| **flac**     | Free Lossless Audio Codec (FLAC).           | `REST`              |
| **aac**      | Advanced Audio Coding format.               | `REST`              |

The streaming WebSocket emits raw audio only: `linear16` (the streaming default), `mulaw`, or `alaw`. Compressed and containerized encodings (`mp3`, `opus`, `flac`, `aac`) are available on the REST endpoint only, where `mp3` is the default.

## Enable Feature

To enable Encoding, include the `encoding` parameter in the query string with the desired encoding option.

**Example**:

```text Text
https://api.deepgram.com/v1/speak?encoding=linear16
```

### CURL Examples

You can use the following cURL command in a terminal or your favorite API client to synthesize text into speech with a specific encoding.

**Linear16 encoding**:

```bash cURL
curl --request POST \
     --url "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&encoding=linear16&container=wav" \
     --header "Authorization: Token DEEPGRAM_API_KEY" \
     --header 'Content-Type: application/json' \
     --data '{"text": "Hello, how can I help you today?"}' \
     --output outputfile_Linear16.wav \
     --fail-with-body \
     --silent || echo "Request failed"
```

**MP3 encoding with bitrate of 32 kbits/second**:

```bash cURL
curl --request POST \
     --url "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&encoding=mp3&bit_rate=32000" \
     --header "Authorization: Token DEEPGRAM_API_KEY" \
     --header 'Content-Type: application/json' \
     --data '{"text": "Hello, how can I help you today?"}' \
     --output outputfile_mp3_32000.mp3 \
     --fail-with-body \
     --silent || echo "Request failed"
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

### Query Parameters

| Parameter  | Value                                                        | Type     | Description                                      |
| ---------- | ------------------------------------------------------------ | -------- | ------------------------------------------------ |
| `encoding` | `linear16` `mulaw` `alaw` `mp3`(default) `opus` `flac` `aac` | `string` | The chosen encoding format for the output audio. |

## Analyze Response

Upon successful processing of the request, you will receive an audio file containing the synthesized text-to-speech output, along with response headers providing additional information.

The audio file is streamed back to you, so you may begin playback as soon as the first byte arrives. Read the guide [Streaming Audio Outputs](/docs/streaming-the-audio-output) to learn how to begin playing the stream immediately versus waiting for the entire file to arrive.

### Response Headers Example

```text http
HTTP/1.1 200 OK
< content-type: audio/mpeg
< dg-model-name: aura-2-thalia-en
< dg-model-uuid: e4979ab0-8475-4901-9d66-0a562a4949bb
< dg-char-count: 32
< dg-request-id: bf6fc5c7-8f84-479f-b70a-602cf5bf18f3
< transfer-encoding: chunked
< date: Thu, 29 Feb 2024 19:20:48 GMT
```

To see these response headers when making a CURL request, add `-v` or `--verbose` to your request.

This includes:

* `content-type`: Specifies the media type of the resource, in this case, `audio/mpeg`, indicating the format of the audio file returned.
* `dg-request-id`: A unique identifier for the request, useful for debugging and tracking purposes.
* `dg-model-uuid`: The unique identifier of the model that processed the request.
* `dg-char-count`: Indicates the number of characters that were in the input text for the text-to-speech process.
* `dg-model-name`: The name of the model used to process the request.
* `transfer-encoding`: Specifies the form of encoding used to safely transfer the payload to the recipient.
* `date`: The date and time the response was sent.
