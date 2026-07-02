---
title: "Sample Rate"
source: https://developers.deepgram.com/docs/sample-rate.md
path: docs/sample-rate
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Sample Rate

`sample_rate` *int32*

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming:Flux

&#x20;All available languages

## Enable Feature

Sample Rate is required when using the [Encoding](/docs/encoding) feature for non-containerized/raw audio. For containerized audio formats, both `sample_rate` and `encoding` should be omitted.

To enable Sample Rate, when you call Deepgram's API, add a `sample_rate` parameter in the query string and set it to the sample rate of your submitted audio.

`sample_rate=SAMPLE_RATE_VALUE`

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/mp3' \
  --data-binary @youraudio.mp3 \
  --url 'https://api.deepgram.com/v1/listen?sample_rate=8000&encoding=linear16'
```

When submitting audio encoded with the Adaptive Multi-Rate (AMR) codec, you must submit specific Sample Rate values:

* `amr-nb`: AMR narrowband codec. When using this option, you must specify `sample_rate=8000` (encoding=amr-nb\&sample\_rate=8000).
* `amr-wb`: AMR wideband codec. When using this option, you must also specify `sample_rate=16000` (encoding=amr-wb\&sample\_rate=16000).
