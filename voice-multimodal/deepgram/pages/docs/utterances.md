---
title: "Utterances"
source: https://developers.deepgram.com/docs/utterances.md
path: docs/utterances
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Utterances

[Try Utterances in the Playground](https://playground.deepgram.com/?endpoint=listen\&utterances=true\&language=en)

`utterances` *boolean* Default: `false`

Pre-recorded  Streaming:Nova Streaming: Flux  All available languages

Deepgram’s Utterances feature allows the chosen model to interact more naturally and effectively with speakers' spontaneous speech patterns. For example, when humans speak to each other conversationally, they often pause mid-sentence to reformulate their thoughts, or stop and restart a badly-worded sentence.

## Enable Feature

To enable utterances, use the following parameter in the query string when you call Deepgram’s `/listen` endpoint :

`utterances=true`

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?utterances=true'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## Analyze Response

When the file is finished processing, you’ll receive a JSON response. Let’s look more closely at the `utterances` object:

```json JSON
...
"utterances":[
  {
    "start":0.41915998,
    "end":5.43012,
    "confidence":0.88172823,
    "channel":0,
    "transcript":"four score and seven years ago our fathers brought forth on this continent a new nation",
    "words":[
      {"word":"four","start":0.41915998,"end":0.85827994,"confidence":0.57893836},
 			...
    ],
    "id":"2d8211a4-3a5b-4053-8939-edf2b2b389fa"
  },
  ...
  }
]
...
```

In this response, we see that each utterance contains:

* `start`: Start time (in seconds) from the beginning of the audio stream.
* `end`: End time (in seconds) from the beginning of the audio stream.
* `confidence`: Floating point value between 0 and 1 that indicates overall transcript reliability. Larger values indicate higher confidence.
* `channel`: Audio channel to which the utterance belongs. When using multichannel audio, utterances are chronologically ordered by channel.
* `transcript`: Transcript for the audio segment being processed.
* `words`: Object containing each word in the transcript, along with its start time and end time (in seconds) from the beginning of the audio stream, and a confidence value.

## Advanced Processing

You may also want to enable speaker diarization, which will detect and identify speakers for utterances, and punctuation.

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @gettysburg.wav \
  --url 'https://api.deepgram.com/v1/listen?utterances=true&diarize=true&punctuate=true'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

When the file is finished processing, you’ll receive a JSON response that has the same basic structure as before. Let’s take a closer look at the new `utterances` object:

```json JSON
...
"utterances":[
  {
    "start":0.41874,
    "end":5.42518,
    "confidence":0.88211584,
    "channel":0,
    "transcript":"four score and seven years ago, our fathers brought forth on this continent a new nation",
    "words":[
      {"word":"four","start":0.41874,"end":0.85742,"confidence":0.5821198,"speaker":0,"punctuated_word":"four"},
      ...
    ],
    "speaker":0,
    "id":"ec11ce4b-2d5c-4b95-9183-ba102bea1d62"
  },
...
]
...
```

In this response, notice that the content of `transcript` in each utterance is now punctuated, and each `word` object in the `words` array contains two new parameters:

* `speaker`: Integer indicating the speaker who is saying the word being processed.
* `punctuated_word`: Word being processed with added punctuation, if any.

To improve readability, you can use a JSON processor to parse the JSON. In this example, we use [JQ](https://stedolan.github.io/jq/).

```bash cURL
curl \
--request POST \
--header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
--header "Content-Type: audio/wav" \
--data-binary @gettysburg.wav \
--url "https://api.deepgram.com/v1/listen?utterances=true&diarize=true&punctuate=true" | jq -r '.results.utterances[] | "[Speaker:\(.speaker)] \(.transcript)"'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

When the file is finished processing, you’ll receive the following response:

```
[Speaker:0] four score and seven years ago, our fathers brought forth on this continent a new nation
[Speaker:0] conceived liberty and dedicated to the proposition that all men are created equal.
[Speaker:0] Now we are engaged in a great civil war testing whether that nation or any nation so conceived and so dedicated can long endure.


```

---
