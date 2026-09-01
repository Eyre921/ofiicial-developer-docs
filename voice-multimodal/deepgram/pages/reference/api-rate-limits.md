---
title: "API Rate Limits"
source: https://developers.deepgram.com/reference/api-rate-limits.md
path: reference/api-rate-limits
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# API Rate Limits

Rate limits vary by region. North America, Europe, and Australia limits are shown separately for each service.

* **North America:** `api.deepgram.com`
* **Europe:** `api.eu.deepgram.com`
* **Australia:** `api.au.deepgram.com`

## Pay as You Go

Limits to consider if you use the Pay as You Go plan with Deepgram.

#### Rate limits apply per project

Rate limits apply per project, not per account or API key. Creating additional projects under the same account will not grant you additional concurrency. Secondary projects created on a self-serve account are limited to a single concurrent stream by design. Bypassing rate limits by spreading traffic across multiple projects violates our Terms of Service.

If you need higher concurrency, [contact sales](https://deepgram.com/contact-us) about a growth or enterprise agreement.

### Voice Agent

| API                                                   | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`)  | Australia (`api.au.deepgram.com`) |
| :---------------------------------------------------- | :--------------------------------- | :------------------------------ | :-------------------------------- |
| [Voice Agent API](/reference/voice-agent/voice-agent) | Up to 45 concurrent connections    | Up to 45 concurrent connections | Up to 45 concurrent connections   |

### Speech to Text

If multiple services are used in one API call (e.g Speech to Text + Sentiment Analysis), the lower of the rate limits is applied.

| Model                                                                   | North America (`api.deepgram.com`)                                                    | Europe (`api.eu.deepgram.com`)                                                        | Australia (`api.au.deepgram.com`)                                                     |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| [Flux STT](/docs/models-languages-overview#flux)                        | `Streaming` Up to 150 concurrent requests                                             | `Streaming` Up to 150 concurrent requests                                             | `Streaming` Up to 150 concurrent requests                                             |
| [Nova-3](/docs/models-languages-overview#nova-3)                        | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Nova-2](/docs/models-languages-overview#nova-2)                        | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Nova](/docs/models-languages-overview#nova)                            | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Enhanced](/docs/models-languages-overview#enhanced)                    | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Base](/docs/models-languages-overview#base)                            | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Whisper Cloud](/docs/models-languages-overview#deepgram-whisper-cloud) | `Pre-Recorded` Up to 3 concurrent requests                                            | Not available                                                                         | Not available                                                                         |

If you include Speaker Diarization features in requests to `/listen`, you will be subject to the service limits noted in the table below.

| Model                                    | North America (`api.deepgram.com`)                                                   | Europe (`api.eu.deepgram.com`)                                                       | Australia (`api.au.deepgram.com`)                                                    |
| :--------------------------------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| [Speaker Diarization](/docs/diarization) | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 50 concurrent requests | `Pre-Recorded` Up to 25 concurrent requests `Streaming` Up to 25 concurrent requests | `Pre-Recorded` Up to 25 concurrent requests `Streaming` Up to 25 concurrent requests |

### Text to Speech REST

| Model                                       | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :------------------------------------------ | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Aura](/docs/text-to-speech)                | Up to 15 concurrent requests       | Up to 15 concurrent requests   | Up to 15 concurrent requests      |
| [Aura-2](/docs/text-to-speech)              | Up to 15 concurrent requests       | Up to 15 concurrent requests   | Up to 15 concurrent requests      |
| [Flux TTS](/docs/flux-tts/feature-overview) | Up to 15 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |

### Text to Speech Streaming

| Model                                       | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :------------------------------------------ | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Aura](/docs/streaming-text-to-speech)      | Up to 45 concurrent requests       | Up to 45 concurrent requests   | Up to 45 concurrent requests      |
| [Aura-2](/docs/streaming-text-to-speech)    | Up to 45 concurrent requests       | Up to 45 concurrent requests   | Up to 45 concurrent requests      |
| [Flux TTS](/docs/flux-tts/feature-overview) | Up to 45 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |

### Audio Intelligence

If you include Audio Intelligence features in requests to `/listen`, you will be subject to the service limits noted in the table below.

| Model                                          | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :--------------------------------------------- | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Intent Recognition](/docs/intent-recognition) | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Entity Detection](/docs/detect-entities)      | Up to 5 concurrent requests        | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Sentiment Analysis](/docs/sentiment-analysis) | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Summarization](/docs/summarization)           | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |
| [Topic Detection](/docs/topic-detection)       | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |

### Text Intelligence

| Model                                                  | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :----------------------------------------------------- | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Intent Recognition](/docs/text-intention-recognition) | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Sentiment Analysis](/docs/text-sentiment-analysis)    | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Summarization](/docs/text-summarization)              | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |
| [Topic Detection](/docs/text-topic-detection)          | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |

## Growth

Limits to consider if you use the Growth plan with Deepgram.

### Voice Agent

| API                                                   | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`)  | Australia (`api.au.deepgram.com`) |
| :---------------------------------------------------- | :--------------------------------- | :------------------------------ | :-------------------------------- |
| [Voice Agent API](/reference/voice-agent/voice-agent) | Up to 60 concurrent connections    | Up to 45 concurrent connections | Up to 45 concurrent connections   |

### Speech to Text

If multiple services are used in one API call (e.g Speech to Text + Sentiment Analysis), the lower of the rate limits is applied.

| Model                                                                   | North America (`api.deepgram.com`)                                                    | Europe (`api.eu.deepgram.com`)                                                        | Australia (`api.au.deepgram.com`)                                                     |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| [Flux STT](/docs/models-languages-overview#flux)                        | `Streaming` Up to 225 concurrent requests                                             | `Streaming` Up to 150 concurrent requests                                             | `Streaming` Up to 150 concurrent requests                                             |
| [Nova-3](/docs/models-languages-overview#nova-3)                        | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 225 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Nova-2](/docs/models-languages-overview#nova-2)                        | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 225 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Nova](/docs/models-languages-overview#nova)                            | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 225 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Enhanced](/docs/models-languages-overview#enhanced)                    | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 225 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Base](/docs/models-languages-overview#base)                            | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 225 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 150 concurrent requests |
| [Whisper Cloud](/docs/models-languages-overview#deepgram-whisper-cloud) | `Pre-Recorded` Up to 3 concurrent requests                                            | Not available                                                                         | Not available                                                                         |

If you include Speaker Diarization features in requests to `/listen`, you will be subject to the service limits noted in the table below.

| Model                                    | North America (`api.deepgram.com`)                                                   | Europe (`api.eu.deepgram.com`)                                                       | Australia (`api.au.deepgram.com`)                                                    |
| :--------------------------------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| [Speaker Diarization](/docs/diarization) | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 50 concurrent requests | `Pre-Recorded` Up to 25 concurrent requests `Streaming` Up to 25 concurrent requests | `Pre-Recorded` Up to 25 concurrent requests `Streaming` Up to 25 concurrent requests |

### Text to Speech REST

| Model                                       | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :------------------------------------------ | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Aura](/docs/text-to-speech)                | Up to 15 concurrent requests       | Up to 15 concurrent requests   | Up to 15 concurrent requests      |
| [Aura-2](/docs/text-to-speech)              | Up to 15 concurrent requests       | Up to 15 concurrent requests   | Up to 15 concurrent requests      |
| [Flux TTS](/docs/flux-tts/feature-overview) | Up to 15 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |

### Text to Speech Streaming

| Model                                       | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :------------------------------------------ | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Aura](/docs/streaming-text-to-speech)      | Up to 60 concurrent requests       | Up to 45 concurrent requests   | Up to 45 concurrent requests      |
| [Aura-2](/docs/streaming-text-to-speech)    | Up to 60 concurrent requests       | Up to 45 concurrent requests   | Up to 45 concurrent requests      |
| [Flux TTS](/docs/flux-tts/feature-overview) | Up to 60 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |

### Audio Intelligence

If you include Audio Intelligence features in requests to `/listen`, you will be subject to the service limits noted in the table below.

| Model                                          | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :--------------------------------------------- | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Intent Recognition](/docs/intent-recognition) | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Entity Detection](/docs/detect-entities)      | Up to 5 concurrent requests        | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Sentiment Analysis](/docs/sentiment-analysis) | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Summarization](/docs/summarization)           | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |
| [Topic Detection](/docs/topic-detection)       | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |

### Text Intelligence

| Model                                                  | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`) | Australia (`api.au.deepgram.com`) |
| :----------------------------------------------------- | :--------------------------------- | :----------------------------- | :-------------------------------- |
| [Intent Recognition](/docs/text-intention-recognition) | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Sentiment Analysis](/docs/text-sentiment-analysis)    | Up to 10 concurrent requests       | Up to 5 concurrent requests    | Up to 5 concurrent requests       |
| [Summarization](/docs/text-summarization)              | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |
| [Topic Detection](/docs/text-topic-detection)          | Up to 10 concurrent requests       | Up to 10 concurrent requests   | Up to 10 concurrent requests      |

## Enterprise

Starting limits to consider if you have an Enterprise Contract with Deepgram. Enterprise limits are the same across all regions unless a row states otherwise.

New and existing Enterprise customers can request a Service Limit increase by discussing your needs with the [Deepgram Sales Team.](mailto:sales@deepgram.com)

### Voice Agent

| API                                                   | North America (`api.deepgram.com`)     | Europe (`api.eu.deepgram.com`)         | Australia (`api.au.deepgram.com`)      |
| :---------------------------------------------------- | :------------------------------------- | :------------------------------------- | :------------------------------------- |
| [Voice Agent API](/reference/voice-agent/voice-agent) | Starting at 100 concurrent connections | Starting at 100 concurrent connections | Starting at 100 concurrent connections |

### Speech to Text

If multiple services are used in one API call (e.g Speech to Text + Sentiment Analysis), the lower of the rate limits is applied.

| Model                                                                   | North America (`api.deepgram.com`)                                                                 | Europe (`api.eu.deepgram.com`)                                                                     | Australia (`api.au.deepgram.com`)                                                                  |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [Flux STT](/docs/models-languages-overview#flux)                        | `Streaming` Up to 300 concurrent requests                                                          | `Streaming` Up to 300 concurrent requests                                                          | `Streaming` Up to 300 concurrent requests                                                          |
| [Nova-3](/docs/models-languages-overview#nova-3)                        | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests |
| [Nova-2](/docs/models-languages-overview#nova-2)                        | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests |
| [Nova](/docs/models-languages-overview#nova)                            | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests |
| [Enhanced](/docs/models-languages-overview#enhanced)                    | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests |
| [Base](/docs/models-languages-overview#base)                            | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests | `Pre-Recorded` Starting at 200 concurrent requests `Streaming` Starting at 300 concurrent requests |
| [Whisper Cloud](/docs/models-languages-overview#deepgram-whisper-cloud) | `Pre-Recorded` Starting at 15 concurrent requests                                                  | Not available                                                                                      | Not available                                                                                      |

If you include Speaker Diarization features in requests to `/listen`, you will be subject to the service limits noted in the table below.

| Model                                    | North America (`api.deepgram.com`)                                                    | Europe (`api.eu.deepgram.com`)                                                        | Australia (`api.au.deepgram.com`)                                                     |
| :--------------------------------------- | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| [Speaker Diarization](/docs/diarization) | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 100 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 100 concurrent requests | `Pre-Recorded` Up to 50 concurrent requests `Streaming` Up to 100 concurrent requests |

### Text to Speech REST

| Model                                       | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`)     | Australia (`api.au.deepgram.com`)  |
| :------------------------------------------ | :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [Aura](/docs/text-to-speech)                | Starting at 25 concurrent requests | Starting at 25 concurrent requests | Starting at 25 concurrent requests |
| [Aura-2](/docs/text-to-speech)              | Starting at 25 concurrent requests | Starting at 25 concurrent requests | Starting at 25 concurrent requests |
| [Flux TTS](/docs/flux-tts/feature-overview) | Starting at 25 concurrent requests | Starting at 25 concurrent requests | Starting at 25 concurrent requests |

### Text to Speech Streaming

| Model                                       | North America (`api.deepgram.com`)  | Europe (`api.eu.deepgram.com`)      | Australia (`api.au.deepgram.com`)   |
| :------------------------------------------ | :---------------------------------- | :---------------------------------- | :---------------------------------- |
| [Aura](/docs/streaming-text-to-speech)      | Starting at 150 concurrent requests | Starting at 150 concurrent requests | Starting at 150 concurrent requests |
| [Aura-2](/docs/streaming-text-to-speech)    | Starting at 100 concurrent requests | Starting at 100 concurrent requests | Starting at 100 concurrent requests |
| [Flux TTS](/docs/flux-tts/feature-overview) | Starting at 100 concurrent requests | Starting at 50 concurrent requests  | Starting at 50 concurrent requests  |

### Audio Intelligence

If you include Audio Intelligence features in requests to `/listen`, you will be subject to the service limits noted in the table below.

| Model                                          | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`)     | Australia (`api.au.deepgram.com`)  |
| :--------------------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [Intent Recognition](/docs/intent-recognition) | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |
| [Entity Detection](/docs/detect-entities)      | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |
| [Sentiment Analysis](/docs/sentiment-analysis) | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |
| [Summarization](/docs/summarization)           | Starting at 20 concurrent requests | Starting at 20 concurrent requests | Starting at 20 concurrent requests |
| [Topic Detection](/docs/topic-detection)       | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |

### Text Intelligence

| Model                                                  | North America (`api.deepgram.com`) | Europe (`api.eu.deepgram.com`)     | Australia (`api.au.deepgram.com`)  |
| :----------------------------------------------------- | :--------------------------------- | :--------------------------------- | :--------------------------------- |
| [Intent Recognition](/docs/text-intention-recognition) | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |
| [Sentiment Analysis](/docs/text-sentiment-analysis)    | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |
| [Summarization](/docs/text-summarization)              | Starting at 20 concurrent requests | Starting at 20 concurrent requests | Starting at 20 concurrent requests |
| [Topic Detection](/docs/text-topic-detection)          | Starting at 10 concurrent requests | Starting at 10 concurrent requests | Starting at 10 concurrent requests |

## Scaling beyond default limits

Rate limits are scoped to a project. One customer maps to one project for the purposes of these limits. Multiple API keys inside a single project all draw from that project's concurrency pool. Adding more projects under the same account does not increase the concurrency available to you.

### If you are hitting your limits

Consolidate your traffic into a single project, then [contact sales](https://deepgram.com/contact-us) about moving to a Growth or Enterprise agreement with a higher concurrency allocation.

### What not to do

Do not create additional projects, additional accounts, or otherwise distribute traffic across projects to work around per-project limits. These setups are detected. Secondary projects on a self-serve account are restricted to 1 concurrent stream, and bypassing rate limits this way violates our Terms of Service.

### REST API rate limits

The concurrency limits on this page apply to inference endpoints (Speech-to-Text, Text-to-Speech, Voice Agent, Intelligence). REST endpoints for project and API key management have their own separate rate limits. See [Temporary API Key Limits](/docs/create-additional-api-keys#temporary-api-key-limits) for details.
