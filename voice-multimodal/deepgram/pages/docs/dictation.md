---
title: "Dictation"
source: https://developers.deepgram.com/docs/dictation.md
path: docs/dictation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Dictation

Pre-recorded  Streaming:Nova Streaming: Flux  English (all available regions)

Dictation is a feature of Deepgram’s Speech-to-Text API that converts spoken dictation commands into their corresponding punctuation marks.

This feature enhances the readability of transcriptions by accurately representing verbal commands as punctuation. For example, saying "comma" as a word will be transcribed as the punctuation mark ",".

## Enable Feature

To enable Dictation, set the `dictation` parameter to `true` in your API request. Note that the `punctuate` parameter must also be enabled for Dictation to work.

The Punctuation feature must be enabled for Dictation to work. Be sure to add `dictation=true&punctuate=true` to your request.

### cURL Example

To transcribe audio with dictation enabled, run the following cURL command in a terminal or your favorite API client:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?dictation=true&punctuate=true'
```

### Query Parameters

| Parameter   | Value            | Data Type | Description                                                                    |
| ----------- | ---------------- | --------- | ------------------------------------------------------------------------------ |
| `dictation` | `true` / `false` | boolean   | Converts spoken dictation commands into their corresponding punctuation marks. |
| `punctuate` | `true` / `false` | boolean   | Enables punctuation in the transcriptions.                                     |

## Analyze Response

Once dictation is enabled, the results will appear in the transcript with the spoken commands converted to punctuation marks. Below is an example of what the transcript will look like when dictation is enabled.

### Response Example

#### Before Dictation

```text Text
Patient presents with a headache comma nausea comma and vomiting period They report the headache started two days ago period Vital signs are within normal limits period
```

#### After Dictation

```text Text
Patient presents with a headache, nausea, and vomiting. They report the headache started two days ago. Vital signs are within normal limits.
```

In the response example above, spoken commands such as "comma" and "period" have been converted to their corresponding punctuation marks, making the transcription more readable and easier to understand.

## Commands List

The following commands will be converted.

| Command          | Converted Text |
| ---------------- | -------------- |
| period           | `.`            |
| comma            | `,`            |
| colon            | `:`            |
| question mark    | `?`            |
| exclamation mark | `!`            |
| new line         | `<\n>`         |
| new paragraph    | `<\n\n>`       |

---
