---
title: "How ElevenLabs latency figures are measured"
source: https://elevenlabs.io/docs/eleven-api/concepts/latency-methodology.md
path: docs/eleven-api/concepts/latency-methodology
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How ElevenLabs latency figures are measured

The latency figures on the [models page](/docs/overview/models) are medians of the time ElevenLabs takes to respond to a request, measured on production traffic. They exclude network round-trips and the time your application spends before and after the request, so the latency your users experience is always higher.

## Published latency figures for ElevenLabs models

| Model                    | Median  | Metric                       |
| ------------------------ | ------- | ---------------------------- |
| Eleven v4 Turbo          | \~100ms | Server-side latency          |
| Eleven Flash v2.5        | \~100ms | Server-side latency          |
| Eleven Flash v2          | \~135ms | Server-side latency          |
| Eleven v3 Conversational | \~165ms | Server-side latency          |
| Scribe v2 Realtime       | \~150ms | Time to committed transcript |

Every figure is a median (p50). The text to speech figures are measured on WebSocket streaming requests with warm voices: a **warm voice** is one that has already been used for a generation.

Medians vary through the day with traffic, and are highest during peak hours. The figures on this page were last updated on October 29, 2026.

## What do the text to speech latency figures measure?

The text to speech figures are **server-side latency**: the end-to-end time from when ElevenLabs receives a request to when it sends the first audio back. Server-side latency does not include:

* The network round-trip between your application and ElevenLabs.
* Upstream steps in your application, such as waiting for an LLM response.
* Audio player buffering before playback starts.

The latency your users experience is **time-to-first-audio (TTFA)**, which adds these stages to server-side latency. [Understanding latency](/docs/eleven-api/concepts/latency#what-contributes-to-time-to-first-audio) describes each stage.

## What does the Scribe v2 Realtime latency figure measure?

The \~150ms figure for Scribe v2 Realtime is the median **time to committed transcript**, taken from production metrics. Realtime transcription returns two kinds of result: partial transcripts while a segment of speech is in progress, and a committed transcript once the segment is final. See [Realtime speech to text](/docs/eleven-api/guides/how-to/speech-to-text/realtime) for how committing works.

## Can ElevenLabs latency figures be compared with other providers?

Only when both figures measure the same thing. The ElevenLabs text to speech figures are server-side latency. They are not comparable with time-to-first-byte (TTFB) or TTFA figures measured from a client, which include the network round-trip and, for TTFA, playback buffering. To compare providers, measure TTFA for each from the same client, region and voice type.

## What makes latency higher than the published figures?

The published ElevenLabs latency figures are a reference point for comparing models, not a guarantee for every request. Server-side latency is higher than the published median with:

* Longer inputs.
* Professional Voice Clones, compared with Instant Voice Clones and default voices.
* High server load, when requests queue before generation starts.

Requests are routed to the nearest serving cluster, and the round-trip to it adds to TTFA but not to the published figures.

[Understanding latency](/docs/eleven-api/concepts/latency) explains why each of these factors matters. To measure and reduce latency in your own application, see [Latency optimization](/docs/eleven-api/guides/how-to/best-practices/latency-optimization).

## Models without a published latency figure

ElevenLabs does not publish a latency figure for Eleven v4, Eleven v3, Eleven Multilingual v2, Scribe v2 or Scribe v2 Medical. These models are designed for quality rather than real-time use. Latency figures for the real-time models above do not apply to them.

## Related

#### [Understanding latency](/docs/eleven-api/concepts/latency)

The stages that contribute to time-to-first-audio and how to reason about tradeoffs.

#### [Latency optimization](/docs/eleven-api/guides/how-to/best-practices/latency-optimization)

Techniques and configuration options that reduce end-to-end latency.
