---
title: "Feature Overview"
source: https://developers.deepgram.com/docs/stt-intelligence-feature-overview.md
path: docs/stt-intelligence-feature-overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Feature Overview

To learn how to get up and running with Speech-To-Text Intelligence, read the [Audio Intelligence](/docs/audio-intelligence) getting started guide.

## Speech-To-Text Intelligence features

| Feature                                        | Pre-recorded? | Streaming? | Language(s)                                                        |
| ---------------------------------------------- | ------------- | ---------- | ------------------------------------------------------------------ |
| [Sentiment Analysis](/docs/sentiment-analysis) | Yes           | No         | [English (all available regions)](/docs/models-languages-overview) |
| [Intent Recognition](/docs/intent-recognition) | Yes           | No         | [English (all available regions)](/docs/models-languages-overview) |
| [Topic Detection](/docs/topic-detection)       | Yes           | No         | [English (all available regions)](/docs/models-languages-overview) |
| [Summarization](/docs/summarization)           | Yes           | No         | [English (all available regions)](/docs/models-languages-overview) |
| [Entity Detection](/docs/detect-entities)      | Yes           | Yes\*      | [English (all available regions)](/docs/models-languages-overview) |

\*Entity Detection for streaming is supported on **Nova**, **Nova 2**, **Nova 3**, and **Enhanced** models. It is not available for Base models or Flux.

## Rate Limits

For information on Deepgram's Concurrency Rate Limits, refer to our [API Rate Limits Documentation](/reference/api-rate-limits).

## Deepgram Self-Hosted

Having challenges with performance and latency? Check out Deepgram's [Self-Hosted Solution](/docs/self-hosted-introduction) to get the benefits of running your own hosted instance of Deepgram.
