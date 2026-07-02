---
title: "SDK Feature Matrix"
source: https://developers.deepgram.com/sdks/sdk-features.md
path: sdks/sdk-features
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# SDK Feature Matrix

Below is a list of all the features supported by our SDKs. For more details on any of these SDKs or features please refer to the corresponding documentation.

If an SDK doesn't have support for an API feature please refer to our documentation for how to [use custom add on parameters with our SDKs](/guides/fundamentals/using-custom-parameters-sdks).

## Voice Agent

| API Reference                                     | Options       | Status | SDK Availability                     |
| ------------------------------------------------- | ------------- | ------ | ------------------------------------ |
| [Voice Agent](/reference/voice-agent/voice-agent) | All Available | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |

## Listen API (v2): Turn-based streaming

| API Reference                                 | Options         | Status | SDK Availability       |
| --------------------------------------------- | --------------- | ------ | ---------------------- |
| [Flux](/reference/speech-to-text/listen-flux) | All Available\* | `GA`   | `JS`, `Python`, `Java` |

* Flux Multilingual (`flux-general-multi`) is available in JS, Python, and Java. See the Flux multilingual
  guide for SDK-specific `language_hint` and `language_hints` examples.

## Listen API (v1): Streaming

| API Reference                                           | Query Options            | Status | SDK Availability                              |
| ------------------------------------------------------- | ------------------------ | ------ | --------------------------------------------- |
| [Streaming](/reference/speech-to-text/listen-streaming) | callback                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | callback\_method         | `GA`   | `JS`, `.NET`, `Python` , `Go`, `Rust`, `Java` |
| [Streaming](/reference/speech-to-text/listen-streaming) | channels                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | diarize                  | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | diarize\_version         | `GA`   | `JS`, `.NET`, `Python`,`Go` `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | encoding                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | endpointing              | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | extra                    | `GA`   | `JS`, `.NET`,`Python`, `Go`, `Rust`, `Java`   |
| [Streaming](/reference/speech-to-text/listen-streaming) | interim\_results         | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | keyterm                  | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Java`            |
| [Streaming](/reference/speech-to-text/listen-streaming) | keywords                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | language                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | model                    | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | multichannel             | `GA`   | `JS`,`.NET`, `Python`,`Go` , `Rust`, `Java`   |
| [Streaming](/reference/speech-to-text/listen-streaming) | numerals                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | punctuate                | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | profanity\_filter        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | redact                   | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | replace                  | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | sample\_rate             | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | search                   | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | smart\_format            | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | smart\_format: no\_delay | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | tag                      | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | utterance\_end\_ms       | `GA`   | `JS`, `.NET`,`Python`,`Go`, `Rust`, `Java`    |
| [Streaming](/reference/speech-to-text/listen-streaming) | vad\_events              | `Beta` | `JS`, `.NET``Python`,`Go`, `Rust`, `Java`     |
| [Streaming](/reference/speech-to-text/listen-streaming) | version                  | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`    |

## Listen API (v1): Pre-recorded

| API Reference                                                       | Query Options     | Status | SDK Availability                             |
| ------------------------------------------------------------------- | ----------------- | ------ | -------------------------------------------- |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | callback          | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | callback\_method  | `GA`   | `JS`,`.NET`,`Python`, `Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | channels          | `GA`   | `.NET`,`Python`, `Go`, `Rust`, `Java`        |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | diarize           | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | diarize\_model    | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | diarize\_version  | `GA`   | `JS`,`.NET`, `Python`, `Rust`, `Java`        |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | detect\_language  | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | dictation         | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | encoding          | `GA`   | `.NET`,`Python`, `Go`, `Rust`, `Java`        |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | extra             | `GA`   | `JS`, `Python`, `Go`, .`NET`, `Rust`, `Java` |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | filler\_words     | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | keyterm           | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Java`           |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | keywords          | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | language          | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | measurements      | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | model             | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | multichannel      | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | numerals          | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | paragraph         | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | punctuate         | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | profanity\_filter | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | redact            | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | replace           | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | sample\_rate      | `GA`   | `Python`,`Go`, `Java`                        |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | search            | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | smart\_format     | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | tag               | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | utterances        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | utt\_split        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |
| [Pre-recorded Audio](/reference/speech-to-text/listen-pre-recorded) | version           | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java`   |

## Intelligence API: Pre-recorded

| API Reference                                                       | Query Options    | Status | SDK Availability                              |
| ------------------------------------------------------------------- | ---------------- | ------ | --------------------------------------------- |
| [Intelligence Audio](/reference/speech-to-text/listen-pre-recorded) | detect\_entities | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java`  |
| [Intelligence Audio](/reference/speech-to-text/listen-pre-recorded) | intents          | `GA`   | `JS`, `.NET`,`Python` , `Go`, `Rust`, `Java`  |
| [Intelligence Audio](/reference/speech-to-text/listen-pre-recorded) | sentiment        | `GA`   | `JS`, `.NET`, `Python` , `Go`, `Rust`, `Java` |
| [Intelligence Audio](/reference/speech-to-text/listen-pre-recorded) | summarize        | `GA`   | `JS`, `.NET`, `Python` , `Go`, `Rust`, `Java` |
| [Intelligence Audio](/reference/speech-to-text/listen-pre-recorded) | topics           | `GA`   | `JS`, `.NET`,`Python` , `Go`, `Rust`, `Java`  |

## Intelligence API: Text

| API Reference                                                  | Query Options | Status | SDK Availability                     |
| -------------------------------------------------------------- | ------------- | ------ | ------------------------------------ |
| [Intelligence Text](/reference/text-intelligence/analyze-text) | intents       | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |
| [Intelligence Text](/reference/text-intelligence/analyze-text) | sentiment     | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |
| [Intelligence Text](/reference/text-intelligence/analyze-text) | summarize     | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |
| [Intelligence Text](/reference/text-intelligence/analyze-text) | topics        | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |

## Text to Speech API: Streaming

| API Reference                                               | Query Options | Status | SDK Availability                     |
| ----------------------------------------------------------- | ------------- | ------ | ------------------------------------ |
| [Text to Speech](/reference/text-to-speech/speak-streaming) | encoding      | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-streaming) | model         | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-streaming) | sample\_rate  | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Java` |

## Text to Speech API: REST

| API Reference                                             | Query Options | Status | SDK Availability                             |
| --------------------------------------------------------- | ------------- | ------ | -------------------------------------------- |
| [Text to Speech](/reference/text-to-speech/speak-request) | bit\_rate     | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-request) | callback      | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-request) | container     | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-request) | encoding      | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-request) | model         | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |
| [Text to Speech](/reference/text-to-speech/speak-request) | sample\_rate  | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |

## Manage API

| API Reference                                                | Query Options                                                                                                                                                                                                              | Status | SDK Availability                           |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------ |
| [Create Key](/reference/manage/keys/create)                  | comment, scopes, tags, expiration\_date, time\_to\_live\_in\_seconds                                                                                                                                                       | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Delete Project](/reference/manage/projects/delete)          | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Delete Invites](/reference/manage/invites/delete)           | N/A                                                                                                                                                                                                                        | `GA`   | `JS`, `Python`,`Go`, `Java`                |
| [Delete Key](/reference/manage/keys/delete)                  | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Balance](/reference/manage/billing/get)                 | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get All Balances](/reference/manage/billing/list)           | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Key](/reference/manage/keys/get)                        | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Members](/reference/manage/members/list)                | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Member Scopes](/reference/manage/invites/list)          | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Project](/reference/manage/projects/get)                | start, end, limit, page                                                                                                                                                                                                    | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Projects](/reference/manage/projects/list)              | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Project Models](/reference/manage/projects/models/list) | include\_outdated                                                                                                                                                                                                          | `GA`   | `JS`, `Python`,`Go`, `.NET`, `Java`        |
| [Get Project Model](/reference/manage/projects/models/get)   | N/A                                                                                                                                                                                                                        | `GA`   | `JS`, `Python`,`Go`, `.NET`, `Java`        |
| [Leave Project](/reference/manage/projects/leave)            | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`Python`,`Go` ,`Rust` ,`.NET`, `Java` |
| [List Invites](/reference/manage/invites/list)               | N/A                                                                                                                                                                                                                        | `GA`   | `JS`, `Python`,`Go`, `.NET`, `Java`        |
| [List Keys](/reference/manage/keys/list)                     | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Get Models](/reference/manage/models/list)                  | include\_outdated                                                                                                                                                                                                          | `GA`   | `JS`, `Python`,`Go`, `.NET`, `Java`        |
| [Get Model](/reference/manage/models/get)                    | N/A                                                                                                                                                                                                                        | `GA`   | `JS`, `Python`,`Go`, `.NET`, `Java`        |
| [Remove Member](/reference/manage/members/delete)            | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Send Invites](/reference/manage/invites/create)             | email, scope                                                                                                                                                                                                               | `GA`   | `JS`, `Python`,`Go`, `Rust`, `Java`        |
| [Summarize Usage](/reference/manage/usage/get)               | start, end, accessor, tag, method, model, multichannel, interim\_results, punctuate, ner, utterances, replace, profanity\_filter, keywords, detect\_topics, diarize, search, redact, alternatives, numerals, smart\_format | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Usage Get All Requests](/reference/manage/requests/list)    | start, end, limit, status, page                                                                                                                                                                                            | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Usage Get Fields](/reference/manage/billing/fields/get)     | start, end                                                                                                                                                                                                                 | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Usage Get Request](/reference/manage/requests/get)          | N/A                                                                                                                                                                                                                        | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Update Project](/reference/manage/projects/update)          | name                                                                                                                                                                                                                       | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |
| [Update Scope](/reference/manage/invites/list)               | scope                                                                                                                                                                                                                      | `GA`   | `JS`,`.NET`, `Python`,`Go`, `Rust`, `Java` |

## Self-Hosted API

In certain cases, our SDKs can be used with Deepgram's [self-hosted](/docs/self-hosted-introduction)-specific endpoints.

For more details on sending inference requests to a self-hosted deploment, see the [Using SDKs with Self-Hosted](/docs/using-sdks-with-self-hosted) guide.

| API Reference                                                                | Query Options | Status | SDK Availability                    |
| ---------------------------------------------------------------------------- | ------------- | ------ | ----------------------------------- |
| [Create Credentials](/reference/self-hosted/distribution-credentials/create) | N/A           | `GA`   | `JS`, `.NET`,`Python`, `Go`, `Java` |
| [Delete Credentials](/reference/self-hosted/distribution-credentials/delete) | N/A           | `GA`   | `JS`,`.NET`, `Python`, `Go`, `Java` |
| [Get Credential](/reference/self-hosted/distribution-credentials/get)        | N/A           | `GA`   | `JS`, `.NET`,`Python`, `Go`, `Java` |
| [Get Credentials](/reference/self-hosted/distribution-credentials/list)      | N/A           | `GA`   | `JS`, `.NET`,`Python`, `Go`, `Java` |

## Auth API

| API Reference                                              | Query Options | Status | SDK Availability                             |
| ---------------------------------------------------------- | ------------- | ------ | -------------------------------------------- |
| [Token-Based Authentication](/reference/auth/tokens/grant) | N/A           | `GA`   | `JS`, `.NET`, `Python`, `Go`, `Rust`, `Java` |

***

What's Next

* [Deepgram SDKs](/home)
