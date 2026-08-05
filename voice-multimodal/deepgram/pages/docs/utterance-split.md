---
title: "Utterance Split"
source: https://developers.deepgram.com/docs/utterance-split.md
path: docs/utterance-split
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Utterance Split

`utt_split` *float* Default: `0.8`

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming: Flux

&#x20;All available languages

Deepgram’s Utterance Split feature monitors incoming audio and detects when a sufficiently long pause is detected between words. By default, the length of time Deepgram uses for Utterance Split is 0.8 seconds, but you can configure this value using the `utt_split` parameter.

## Enable Feature

To enable Utterance Split, when you call Deepgram’s API, add an `utt_split` parameter in the query string and set it to the length of time (in seconds) of silence between words after which Deepgram will decide that a new utterance should begin. The default values is 0.8 s.

`utt_split=LENGTH-OF-TIME-IN-SECONDS`

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client and define the utterance split value you'd wish to use:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?utterances=true&utt_split=LENGTH-OF-TIME-IN-SECONDS'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## Results

To learn about the results, see [Utterances](/docs/utterances#analyze-response).

***
