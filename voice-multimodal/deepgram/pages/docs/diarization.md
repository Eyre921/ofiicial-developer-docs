---
title: "Speaker Diarization"
source: https://developers.deepgram.com/docs/diarization.md
path: docs/diarization
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Speaker Diarization

Deepgram API Playground
Try this feature out in our API Playground.

<br />

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming: Flux

&#x20;All available languages

## Diarization Models

Deepgram offers versioned diarization models. Use the `diarize_model` parameter to select a specific version:

| Value    | Batch                                                   | Streaming                                                   |
| -------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| `latest` | Resolves to the latest GA batch diarizer (currently v2) | Resolves to the latest GA streaming diarizer (currently v1) |
| `v2`     | Pins to the v2 diarizer                                 | Not supported — returns a validation error                  |
| `v1`     | Pins to the v1 diarizer                                 | Pins to the v1 streaming diarizer                           |

Specifying `diarize_model` both enables diarization **and** selects the model version. You do not need to also set `diarize=true`.

### Choosing a Model

* **New integrations**: Use `diarize_model=latest` to always get the newest available diarizer.
* **Pin a specific version**: Use `diarize_model=v1` or `diarize_model=v2` (batch only).
* **Streaming**: Use `diarize_model=latest` or `diarize_model=v1`. The v2 diarizer is not available for streaming and returns a validation error.

## Enable Feature

### Using `diarize_model` (recommended)

Use the `diarize_model` parameter to enable diarization and select the model version in a single parameter:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?diarize_model=latest'
```

### Using `diarize` (deprecated)

The `diarize` parameter is deprecated. Use `diarize_model` instead for both batch and streaming requests.

The boolean `diarize` parameter continues to work and always routes to the v1 diarizer:

`diarize=true`

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?diarize=true'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

**Self-hosted deployments:** `diarize=true` is pinned to the v1 batch diarizer. New self-hosted deployments provisioned at the May 2026 release (`release-260514`) or later receive only the v2 batch diarizer model by default — `diarize=true` on those deployments returns a successful response without `speaker` labels, consistent with Deepgram's longstanding behavior when a requested diarizer model is not present. To produce diarized output on a fresh deployment, specify `diarize_model=v2` or `diarize_model=latest`. See the [Self-Hosted May 2026 release notes](/changelog/self-hosted-changelog#deepgram-self-hosted-may-2026-release-260514) for details.

## Versioning Behavior

Switch your `diarize=true` requests to `diarize_model` (use `latest` for most cases). Don't set both `diarize` and `diarize_model` — requests that set both are rejected.

### Model Compatibility

Diarization is compatible with all Nova batch models (Nova-1, Nova-2, Nova-3) as well as enhanced and base. Whisper is not supported.

### Streaming

`diarize_model` is accepted on streaming requests with the following values:

* `diarize_model=v1` — uses the v1 streaming diarizer.
* `diarize_model=latest` — resolves to the latest streaming diarizer (currently v1).
* `diarize_model=v2` — **not supported** on streaming. Returns a validation error.

The deprecated `diarize=true` parameter also continues to work for streaming and routes to the v1 diarizer.

## Analyze Response

For this example, we use an MP3 audio file that contains the beginning of a customer call with Premier Phone Services. If you would like to follow along, you can [download it](https://res.cloudinary.com/deepgram/video/upload/v1680127025/dg-audio/nasa-spacewalk-interview_ljjahn.wav).

When the file is finished processing, you'll receive a JSON response. Let's look more closely at the `words` object within the `alternatives` object within this response.

### Pre-Recorded

When using diarization for pre-recorded audio, both `speaker` and `speaker_confidence` values will be returned:

```json JSON
...
"alternatives":[
  {
    ...
    "words": [
      {
        "word":"hello",
        "start":15.259043,
        "end":15.338787,
        "confidence":0.9721591,
        "speaker":0,
        "speaker_confidence":0.5853265
      },
    ...
    ]
  }
]
```

### Live Streaming

When using diarization for live streaming audio, only the `speaker` value will be returned:

```json JSON
...
"alternatives":[
  {
    ...
    "words": [
      {
        "word":"hello",
        "start":15.259043,
        "end":15.338787,
        "confidence":0.9721591,
        "speaker":0
      },
    ...
    ]
  }
]
```

### Diarizer Model Metadata

When a diarizer runs, the response `metadata` includes a `diarize_info` object that identifies the diarizer build that produced the speaker labels. It appears alongside `model_info` in both pre-recorded and streaming responses, which makes the resolved model visible when `diarize_model=latest` resolves to different versions across batch and streaming:

```json JSON
"metadata": {
  "models": ["30089e05-99d1-4376-b32e-c263170674af"],
  "model_info": {
    "30089e05-99d1-4376-b32e-c263170674af": {
      "name": "2-general-nova",
      "version": "2024-01-09.29447",
      "arch": "nova-2"
    }
  },
  "diarize_info": {
    "model_uuid": "9a1c8b3e-2f44-4c8a-b1d0-example0000",
    "arch": "v2"
  }
}
```

* `model_uuid` — the UUID of the diarizer build that ran.
* `arch` — the diarizer architecture family (`v1` or `v2`) that `diarize_model` resolved to, which makes `diarize_model=latest` resolution visible. Legacy `diarize=true` requests report `v1`.

`diarize_info` is present only when a diarizer actually ran:

| Request                                                                                                      | `diarize_info`                            |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| `diarize_model=v1`, `v2` (batch only), or `latest`                                                           | Present; `arch` shows the resolved family |
| `diarize=true` (deprecated)                                                                                  | Present; `arch: "v1"`                     |
| No diarization requested                                                                                     | Absent                                    |
| Diarization requested but no diarizer model available (for example, self-hosted v2-only with `diarize=true`) | Absent                                    |

`diarize_info` is either present with both fields or absent entirely — it is never `null` or `{}`. An absent block on a request that asked for diarization means the diarizer did not run, which is how you distinguish a missing diarizer from single-speaker audio.

## Format Response

To improve readability, you can use a JSON processor to parse the JSON. In this example, we use [JQ](https://stedolan.github.io/jq/) and further improve readability by turning on Deepgram's [punctuation](/docs/punctuation/) and [utterances](/docs/utterances/) features:

```bash cURL
curl \
  --request POST \
  --url 'https://api.deepgram.com/v1/listen?diarize_model=latest&punctuate=true&utterances=true' \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'content-type: audio/mp3' \
  --data-binary @Premier_broken-phone_numbers.mp3 | jq -r ".results.utterances[] | \"[Speaker:\(.speaker)] \(.transcript)\""
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

When the file is finished processing, you'll receive the following response:

```
[Speaker:0] Hello, and thank you for calling premier phone service. Please be aware that this call may be recorded for quality and training purposes.
[Speaker:0] My name is Beth, and I will be assisting you today. How are you doing?
[Speaker:1] Not too bad. How are you today?
[Speaker:0] I'm doing well. Thank you. May I please have your name?
[Speaker:1] My name is Blake...
```

To learn more about when to use Deepgram's Diarization or Multichannel feature, see [When to Use the Multichannel and Diarization Features](/docs/multichannel-vs-diarization).

---

What's Next

* [Understanding When to Use the Multichannel and Diarization Features](/docs/multichannel-vs-diarization)
