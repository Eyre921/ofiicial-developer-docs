---
title: "Languages Support"
source: https://developers.deepgram.com/docs/language.md
path: docs/language
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Languages Support

`language` *string* Default: `en`

&#x20;Pre-recorded

&#x20;Streaming:Nova

## Enable Feature

To enable Language in your API request you can add the `language` parameter in the query string and set it to the language you would like to recognize:

`language=OPTION`

For a full list of languages and compatible models see our [Model & Language Overview](/docs/models-languages-overview).

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?language=OPTION'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## Language Restriction Behavior

When a specific language is set using the `language` parameter (e.g., `language=en`), Deepgram will only attempt to transcribe speech in that specified language. Speech in other, non-specified languages will not be transcribed. If you expect your audio to contain multiple languages and want Deepgram to transcribe across them, consider using `language=multi` with one of our [multilingual models](/docs/multilingual-code-switching).

## Results

Once the language option is applied, results will appear in the transcript.

## English Dialect Spelling

Deepgram's English models are designed to handle global English audio, with strong performance across dialects and accents from across the world. Transcription outputs from the English models are provided with standardized American spelling of words.

For example, "color" will always be spelled as such with both `language=en-US` and `language=en-GB`, never using the British spelling "colour". If your use case requires a different spelling, you should perform post-processing on results in order to enforce your preferred spelling standard.

***
