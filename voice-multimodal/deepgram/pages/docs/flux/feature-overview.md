---
title: "Flux Feature Overview"
source: https://developers.deepgram.com/docs/flux/feature-overview.md
path: docs/flux/feature-overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux Feature Overview

## Model Selection

| Feature                  | Language(s)                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| [Model](/docs/model)     | `flux-general-en` (English), `flux-general-multi` (10 languages — [Language Prompting](/docs/flux/language-prompting)) |
| [Version](/docs/version) | [All available](/docs/model#flux)                                                                                      |

## Language Configuration

| Feature                                             | Model                     | Description                                                     |
| --------------------------------------------------- | ------------------------- | --------------------------------------------------------------- |
| [Language Prompting](/docs/flux/language-prompting) | `flux-general-multi` only | Bias output toward specific languages with `language_hint`      |
| Language Detection                                  | `flux-general-multi` only | `languages` field on TurnInfo events reports detected languages |

## Formatting

| Feature                                    | Language(s)                                                                      |
| ------------------------------------------ | -------------------------------------------------------------------------------- |
| [Profanity Filter](/docs/profanity-filter) | [All available](/docs/model#flux)                                                |
| [Numerals](/docs/numerals)                 | English + Multilingual (excludes Hindi & Japanese)                               |
| [Redaction](/docs/redaction)               | Number redaction only (`numbers`, `aggressive_numbers`) — English + Multilingual |

## Transcription

| Feature               | Language(s)                       |
| --------------------- | --------------------------------- |
| Word-level Timestamps | [All available](/docs/model#flux) |

## Custom Vocabulary

| Feature                            | Language(s)                                      |
| ---------------------------------- | ------------------------------------------------ |
| [Keyterm Prompting](/docs/keyterm) | [All available](/docs/models-languages-overview) |

## Media Input Settings

| Feature                          | Language(s)                                      |
| -------------------------------- | ------------------------------------------------ |
| [Sample rate](/docs/sample-rate) | [All available](/docs/models-languages-overview) |
| [Encoding](/docs/encoding)       | [All available](/docs/model#flux)                |

## End-of-Turn Configuration

| Feature                                             | Description                                                                                  |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [Configurable Parameters](/docs/flux/configuration) | Tune `eot_threshold`, `eager_eot_threshold`, and `eot_timeout_ms` for optimal turn detection |

Flux's end-of-turn detection is configurable to match your use case. Use `eot_threshold` for standard turn detection, or enable `eager_eot_threshold` for ultra-low latency response generation. See the [End-of-Turn Configuration](/docs/flux/configuration) for detailed configuration guidance.

## Control Messages

| Feature                                 | Description                                  |
| --------------------------------------- | -------------------------------------------- |
| [Configure](/docs/flux/configure)       | Update keyterms and thresholds mid-stream    |
| [Close Stream](/docs/flux/close-stream) | Force stream closure and final transcription |

## Rate Limits

For information on Deepgram's Concurrency Rate Limits, refer to our [API Rate Limits Documentation](/reference/api-rate-limits).

## Deepgram Self-Hosted

Flux is now available for self-hosted deployments!

For setup instructions, see [Using the Flux Model](/docs/flux-self-hosted). For more information about Deepgram's self-hosted solution, visit our [Self-Hosted Introduction](/docs/self-hosted-introduction).

---
