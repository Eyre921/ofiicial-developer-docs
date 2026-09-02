---
title: "Punctuation"
source: https://developers.deepgram.com/docs/punctuation.md
path: docs/punctuation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Punctuation

* [Try Punctuation in the Playground](https://playground.deepgram.com/?endpoint=listen\&punctuate=true\&language=en\&model=nova-3)

`punctuate` *boolean* Default: `false`

Pre-recorded  Streaming:Nova Streaming: Flux  All available languages

## Enable Feature

To enable punctuation, use the following parameter in the query string when you call Deepgram’s `/listen` endpoint :

`punctuate=true`

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?punctuate=true'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## Results

Once applied, results will appear in the transcript.

| Source                                                                                                                                                                          | Before punctuate                                                                                                                                                                | After punctuate                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| hello and thank you for calling premier services please be aware that this call may be recorded for quality training purposes my name is beth and i will be assisting you today | hello and thank you for calling premier services please be aware that this call may be recorded for quality training purposes my name is beth and i will be assisting you today | Hello, and thank you for calling Premier Services. Please be aware that this call may be recorded for quality training purposes. My name is Beth, and I will be assisting you today. |

---
