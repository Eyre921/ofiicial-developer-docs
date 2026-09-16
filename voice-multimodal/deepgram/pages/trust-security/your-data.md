---
title: "Your Data at Deepgram"
source: https://developers.deepgram.com/trust-security/your-data.md
path: trust-security/your-data
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Your Data at Deepgram

> How Deepgram handles your audio, text, and transcripts: what we store, how long we keep it, where it is processed, and the controls you have over each.

Your data is yours. This page explains what Deepgram does with the audio, text, and transcripts you send us, and the controls you have over each part of it.

Three things determine how your data is handled:

* **Where it is processed.** The endpoint you call sets the geography. The global endpoint is the default. Regional endpoints handle your request and store your data inside one region. Model improvement on retained data can happen outside that region, so processing is fully in-region only when the request is also opted out.
* **Whether it is retained and used to improve our models.** Requests participate in the [Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program) (MIP) by default, and Deepgram retains them. Retained data may be processed outside your region for model improvement. Opt out per request with `mip_opt_out=true`. Opted-out requests are not retained, and on a regional endpoint Deepgram does not send them outside the region ([third-party Voice Agent providers](#voice-agent-and-third-party-providers) are separate).
* **How it is protected.** Your data is encrypted in transit and at rest, and is processed only by Deepgram and our published sub-processors, or by providers you choose using your own keys.

The two settings are separate. The residency guarantee depends on both.

## What Deepgram stores

| API            | Data                                       | Default                                                                                                                        | With `mip_opt_out=true`                                                                                                        |
| -------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Speech-to-Text | Request audio                              | Retained to improve our models                                                                                                 | Retained only for the duration needed to process the request                                                                   |
| Speech-to-Text | Transcript                                 | Returned to you; retained to improve our models                                                                                | Retained only for the duration needed to process the request                                                                   |
| Text-to-Speech | Request text and voice parameters          | Retained to improve our models                                                                                                 | Retained only for the duration needed to process the request                                                                   |
| Text-to-Speech | Synthesized audio                          | Returned to you; retained to improve our models                                                                                | Retained only for the duration needed to process the request                                                                   |
| Voice Agent    | Request audio                              | Retained to improve our models                                                                                                 | Retained only for the duration needed to process the request                                                                   |
| Voice Agent    | Intermediate transcripts and agent context | Returned to you; retained to improve our models                                                                                | Retained only for the duration needed to process the request                                                                   |
| Voice Agent    | Synthesized audio                          | Returned to you; retained to improve our models                                                                                | Retained only for the duration needed to process the request                                                                   |
| All            | Async callback results                     | Held until delivered to your [callback URL](/docs/callback) or retries are exhausted, then deleted. Not retrievable afterward. | Held until delivered to your [callback URL](/docs/callback) or retries are exhausted, then deleted. Not retrievable afterward. |
| All            | Request metadata and usage logs            | Retrievable for 90 days; summarized usage retained beyond 90 days                                                              | Retrievable for 90 days; summarized usage retained beyond 90 days                                                              |

Request metadata and usage logs record how you used the API. They do not contain your audio, text, or transcripts. To retain usage data past 90 days, fetch it on an interval with the [Usage API](/reference/manage/requests/list) and store it yourself. See [Using Logs & Usage](/docs/using-logs-usage).

Deepgram does not sell your data, does not use it to build advertising profiles, and does not redistribute it to third parties without your permission.

## Model improvement and zero data retention

The [Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program) (MIP) is how Deepgram improves its models on real-world audio. Participation is the default, and participants receive models tuned to their domain, faster support, and early access to new models.

Data used for training is only the data included through MIP. It is never sold, never used for advertising, and never redistributed to third parties without your permission.

### Opting out

Set `mip_opt_out=true` and the request is excluded from model improvement:

| API                                         | How to set it                                   |
| ------------------------------------------- | ----------------------------------------------- |
| Speech-to-Text (pre-recorded and streaming) | `mip_opt_out=true` query parameter              |
| Text-to-Speech (REST and streaming)         | `mip_opt_out=true` query parameter              |
| Voice Agent                                 | `"mip_opt_out": true` in the `Settings` message |

For example, to opt a pre-recorded transcription request out of model improvement:

```bash
curl -X POST "https://api.deepgram.com/v1/listen?model=nova-3&mip_opt_out=true" \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @audio.wav
```

Opting out gives you zero data retention: Deepgram does not store your audio, text, transcripts, or synthesized audio after the response is returned. Request metadata and usage logs are still recorded, as described above.

For per-language and per-SDK examples, see [Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program#want-to-opt-out).

### Confirming opt-out

Check the [Deepgram Console](https://console.deepgram.com/) under **Usage > Logs**, where an opted-out request shows `mip_opt_out` as `true`. You can also read it programmatically with the [Get a Project Request](/reference/manage/usage/get) endpoint.

If you would rather not set the flag on every request, [contact us](https://deepgram.com/contact-us) about enforcing opt-out across your account or deployment.

## Data residency

Where Deepgram processes your data depends on the endpoint you call.

### The global endpoint

`api.deepgram.com` is Deepgram's global endpoint and the default for every API. It carries the broadest model and feature coverage, and it is the right choice for most applications. The Voice Agent API's global host is `agent.deepgram.com`.

Data residency guarantees come from regional endpoints. If your data must stay in a specific geography, call that region's endpoint.

A full in-region guarantee requires both a regional endpoint and `mip_opt_out=true`. See the summary at the top of this page.

### Regional endpoints are the residency boundary

Regional endpoints take the form `api.{region}.deepgram.com`. On a regional endpoint, Voice Agent traffic uses that region's host: `wss://api.{region}.deepgram.com/v1/agent/converse`.

Each regional endpoint handles your request and stores your data within its region, and does not route requests to Deepgram services outside it. If the region is unavailable, requests fail rather than fall back to another region. For what model improvement adds, see the summary at the top of this page.

Regional endpoints use your existing API keys and SDKs. You only change the base URL. For endpoint URLs, WebSocket paths, and SDK configuration, see [Regional Endpoints](/reference/regional-endpoints).

### Available regions

| Region         | Endpoint              | Where your data is processed and stored        |
| -------------- | --------------------- | ---------------------------------------------- |
| European Union | `api.eu.deepgram.com` | Within the EU; the specific country may change |
| Australia      | `api.au.deepgram.com` | Within Australia                               |
| India          | `api.in.deepgram.com` | Within India                                   |

All regional endpoints support the same APIs:

* **Speech-to-Text** — Nova and Flux models (Whisper is not supported)
* **Text-to-Speech** — Aura and Flux models
* **Voice Agent**
* **Text Intelligence**

If you need processing pinned to a specific country rather than a region, use [Deepgram Dedicated](https://deepgram.com/dedicated) or [self-hosted](/docs/self-hosted-introduction).

### Residency is not sovereignty

A regional endpoint keeps your data stored and processed in-region and stops routine offshore administrative access. It does not make Deepgram immune to foreign legal process. If your requirements go that far, deploy self-hosted or Deepgram Dedicated, where keys, logs, and retention stay in your own infrastructure.

### Voice Agent and third-party providers

Deepgram runs the `listen` and `speak` steps on Deepgram infrastructure in the region you call. If you configure a third-party LLM for the `think` step, that provider processes your data on its own infrastructure under its own residency and retention terms. Confirm those independently.

Where a managed provider offers a regional endpoint, Deepgram routes to it automatically. See [Voice Agent managed providers](/reference/regional-endpoints#voice-agent-managed-llm-and-tts-providers) for what is regionalized today.

## Encryption

Deepgram encrypts all data in transit and at rest with industry-standard encryption, including TLS 1.3 and AES-256.

## Compliance

Deepgram operates under SOC 2 Type 1 and Type 2 attestation, and supports HIPAA, PCI DSS, GDPR, CCPA, and the Australian Privacy Principles. For framework detail, regional specifics, and how to request documentation, see [Data Privacy Compliance](/trust-security/data-privacy-compliance).

Deepgram publishes its sub-processors at [deepgram.com/privacy/subprocessors](https://deepgram.com/privacy/subprocessors).

## Next steps

* [Regional Endpoints](/reference/regional-endpoints) - endpoint URLs, WebSocket paths, and SDK
  configuration. - [Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program) - how opt-out works, with
  examples for every SDK. - [Data Privacy Compliance](/trust-security/data-privacy-compliance) -
  frameworks, certifications, and how to request documentation. - [Security Policy](/trust-security/security-policy) - how Deepgram protects data and controls access.

If you have a residency or retention requirement this page does not cover, [contact us](https://deepgram.com/contact-us).
