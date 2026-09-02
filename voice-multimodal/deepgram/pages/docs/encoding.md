---
title: "Encoding"
source: https://developers.deepgram.com/docs/encoding.md
path: docs/encoding
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Encoding

`encoding` *string*

Pre-recorded  Streaming:Nova Streaming:Flux  All available languages

Encoding is required when raw, headerless audio packets are sent to the streaming service. If containerized audio packets are sent to the streaming service, this feature should not be used.

If you are using the Encoding feature, the [Sample Rate](/docs/sample-rate) feature is also required.

## Enable Feature

To enable Encoding, when you call Deepgram’s API, add an `encoding` parameter in the query string and set it to the audio coding algorithm of your submitted audio:

`encoding=OPTION`

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/mp3' \
  --data-binary @youraudio.mp3 \
  --url 'https://api.deepgram.com/v1/listen?sample_rate=8000&encoding=linear16'
```

Deepgram supports the following audio coding algorithms:

Flux supports `linear16`, `linear32`, `mulaw`, `alaw`, `opus`, and `ogg-opus` for non-containerized/raw audio. Flux also supports containerized formats: `linear16` in WAV containers, `opus` in Ogg containers, and `opus` in WebM containers (omit the `encoding` parameter for containerized audio).

* `linear16`: 16-bit, little endian, signed PCM WAV data
* `linear32`: 32-bit, little endian, floating-point PCM WAV data
* `flac`: Free Lossless Audio Codec (FLAC) encoded data
* `alaw`: A-law encoded WAV data
* `mulaw`: Mu-law encoded WAV data
* `amr-nb`: Adaptive Multi-Rate (AMR) narrowband codec
* `amr-wb`: Adaptive Multi-Rate (AMR) wideband codec
* `opus`: The Opus audio codec
* `ogg-opus`: The Opus audio codec encapsulated in the Ogg container format
* `speex`: An open-source, speech-specific audio codec
* `g729`: G729 low-bandwidth (required for both raw and containerized audio)

---
