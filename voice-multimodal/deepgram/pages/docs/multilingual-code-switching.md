---
title: "Multilingual Codeswitching"
source: https://developers.deepgram.com/docs/multilingual-code-switching.md
path: docs/multilingual-code-switching
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Multilingual Codeswitching

`language` *string* Option: `multi`

&#x20;Pre-recorded

&#x20;Streaming:Nova

&#x20;Specific languages only

The Multilingual Codeswitching feature in Deepgram's API allows you to transcribe conversations where speakers switch between multiple languages. This guide will walk you through enabling this feature, how to use it with cURL, and how to analyze and interpret the response.

Multilingual Code Switching is available on Nova-2, Nova-3, and Flux Multilingual (`flux-general-multi`). See [the list of supported languages](/docs/models-languages-overview) for each multilingual model.

## 1. Enable Feature

### Nova-2 / Nova-3

To enable Multilingual Codeswitching on Nova-2 or Nova-3, use the following language parameter in the query string when you call Deepgram's `/listen` endpoint:

`language=multi`

### Pre-Recorded Audio

To transcribe audio from a file on your computer that contains multiple languages, run the following cURL command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?language=multi&model=nova-3
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

### Streaming Audio

To transcribe an audio stream, initiate a websocket connection, including the parameter `language=multi`. For instance:

We recommend using an endpointing value of 100 ms for code-switching, `endpointing=100`.

```
wss://api.deepgram.com/v1/listen?language=multi&model=nova-3&sample_rate=44100&encoding=linear16&endpointing=100
```

### Flux Multilingual

Flux Multilingual handles code-switching natively. Instead of `language=multi`, use `model=flux-general-multi` with optional `language_hint` parameters to bias toward expected languages.

```
wss://api.deepgram.com/v2/listen?model=flux-general-multi&language_hint=en&language_hint=es&encoding=linear16&sample_rate=16000
```

Flux returns detected languages in every `TurnInfo` event via the `languages` field. See the [Language Prompting guide](/docs/flux/language-prompting) for full details on usage scenarios and response format.

## 3. Analyze Response

### Pre-Recorded Audio

When the file is finished processing, you’ll receive a JSON response that has the following basic structure:

```json JSON

{
    "metadata": {
        "transaction_key": "deprecated",
        "request_id": "2479c8c8-8285-40ac-9ab6-f0874449f793",
        "sha256": "154e291ecfa8be6ab8343560bcc109001fa7853eb537253be8e4defc9b504c33",
        "created": "2024-06-26T19:56:16.180Z",
        "duration": 1.6,
        "channels": 1,
        "models": [
            "dc8a3fe5-a395-4b75-a8b1-71c9a5a87526"
        ],
        "model_info": {
            "dc8a3fe5-a395-4b75-a8b1-71c9a5a87526": {
                "name": "2-general-nova",
                "version": "1999-06-13.21385",
                "arch": "nova-2"
            }
        }
    },
    "results": {
        "channels": [
            {
                "alternatives": [
                    {
                        "transcript": "No recuerdo mi bank password.",
                        "confidence": 0.99902344,
                        "languages": [
                            "en",
                            "es"
                        ],
                        "words": [
                            {
                                "word": "no",
                                "start": 0.08,
                                "end": 0.32,
                                "confidence": 0.9975586,
                                "language": "es"
                            },
                            {
                                "word": "recuerdo",
                                "start": 0.32,
                                "end": 0.79999995,
                                "confidence": 0.9921875,
                                "language": "es"
                            },
                            {
                                "word": "mi",
                                "start": 0.79999995,
                                "end": 1.04,
                                "confidence": 0.96777344,
                                "language": "es"
                            },
                            {
                                "word": "bank",
                                "start": 1.04,
                                "end": 1.28,
                                "confidence": 1,
                                "language": "en"
                            },
                            {
                                "word": "password",
                                "start": 1.28,
                                "end": 1.5999999,
                                "confidence": 0.9926758,
                                "language": "en"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

In this response, we see that each channel contains:

* **alternatives** object, which contains:

  * **transcript**: Transcript for the audio being processed.
  * **confidence**: Floating point value between 0 and 1 that indicates overall transcript reliability. Larger values indicate higher confidence.
  * **languages**: Array of [BCP-47](https://tools.ietf.org/html/bcp47) language tags for all detected languages in the channel, sorted in descending order of number of words per language.
  * **words**: Object containing each word in the transcript, along with its start time and end time (in seconds) from the beginning of the audio, a word-level transcription confidence value, the language of the word, and the punctuated word if Smart Formatting is enabled.

### Streaming Audio

When streaming audio, a Results JSON message has the following structure:

```json JSON
{
    "type": "Results",
    "channel_index": [
        0,
        1
    ],
    "duration": 4.0700073,
    "start": 464.47,
    "is_final": True,
    "speech_final": False,
    "channel": {
        "alternatives": [
            {
                "transcript": "será el inglés muchos",
                "confidence": 0.937473,
                "languages": [
                    "es"
                ],
                "words": [
                    {
                        "word": "será",
                        "start": 465.43,
                        "end": 465.91,
                        "confidence": 0.9494371,
                        "language": "es"
                    },
                    {
                        "word": "el",
                        "start": 465.91,
                        "end": 466.15,
                        "confidence": 0.37035784,
                        "language": "es"
                    },
                    {
                        "word": "inglés",
                        "start": 466.15,
                        "end": 466.65,
                        "confidence": 0.416623,
                        "language": "es"
                    },
                    {
                        "word": "muchos",
                        "start": 467.75,
                        "end": 468.25,
                        "confidence": 0.937473,
                        "language": "es"
                    }
                ]
            }
        ]
    },
    "metadata": {
        "request_id": "84157495-6794-4c45-b12b-95b0aeb8793f",
        "model_info": {
            "name": "2-general-nova",
            "version": "1999-05-16.19331",
            "arch": "nova-2"
        },
        "model_uuid": "cf62fbcf-2ee4-49ff-a064-d92fc81d27f4"
    },
    "from_finalize": False
}
```

***
