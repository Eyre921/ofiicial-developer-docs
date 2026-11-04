---
title: "Redact usage"
source: https://developers.deepgram.com/docs/redact-usage.md
path: docs/redact-usage
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Redact usage

`redact_usage` *boolean*

Pre-recorded  Streaming:Nova Streaming:Flux

We record the parameters of each request in your usage records, which you can view in the [Console](https://console.deepgram.com/usage/logs) and through the [Management API](/reference/manage/requests/get). Some parameters carry text you supply, such as keyterms, find-and-replace terms, or search terms. If that text contains names, account details, or other sensitive data, set `redact_usage=true` and we'll store `[REDACTED]` in place of those values.

Redact usage changes only what we record about the request. It doesn't change transcription, and the response you receive is identical.

## Enable the feature

Add `redact_usage=true` to the query string:

**`cURL`**

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?model=nova-3&keyterm=Acme&keyterm=Jane%20Doe&redact_usage=true'
```

The usage record for this request shows:

```
/v1/listen?model=nova-3&keyterm=[REDACTED]&keyterm=[REDACTED]
```

The parameter works the same way on pre-recorded (`/v1/listen`), streaming (`wss://api.deepgram.com/v1/listen`), and Flux STT (`wss://api.deepgram.com/v2/listen`) requests.

### Flux STT Configure messages

On Flux STT, you can also turn on redact usage mid-stream by sending `"redact_usage": true` in a [Configure](/docs/flux/configure) message. We then redact keyterms you send in that and later Configure messages.

A Configure message can't redact the connection URL, which we record when the connection opens. Keyterms you pass as query parameters stay visible unless you also set `redact_usage=true` on the URL. To redact everything, set it on the URL.

Once on, redact usage stays on for the rest of the connection. Sending `"redact_usage": false` doesn't turn it off.

## What we redact

When `redact_usage=true`, we replace the values of these parameters with `[REDACTED]`:

| Parameter       | Feature                                        | Available on                      |
| --------------- | ---------------------------------------------- | --------------------------------- |
| `keyterm`       | [Keyterm prompting](/docs/keyterm)             | Pre-recorded, streaming, Flux STT |
| `keywords`      | [Keywords](/docs/keywords)                     | Pre-recorded, streaming           |
| `replace`       | [Find and replace](/docs/find-and-replace)     | Pre-recorded, streaming           |
| `search`        | [Search](/docs/search)                         | Pre-recorded, streaming           |
| `extra`         | [Extra metadata](/docs/extra-metadata)         | Pre-recorded, streaming           |
| `custom_topic`  | [Topic detection](/docs/topic-detection)       | Pre-recorded                      |
| `custom_intent` | [Intent recognition](/docs/intent-recognition) | Pre-recorded                      |

Other parameters keep their values. These include [`tag`](/docs/stt-tagging) and [`callback`](/docs/callback), so don't put sensitive data in tags or callback URLs. Request metadata such as the request ID, timestamps, audio duration, and model also stay visible.

## Redact usage, redaction, and the Model Improvement Program

Redact usage is independent of two related features:

* **[Redaction](/docs/redaction)** (`redact`) removes sensitive entities such as PII from the transcript we return. Redact usage doesn't touch the transcript.
* **[Model Improvement Program](/docs/the-deepgram-model-improvement-partnership-program)** (`mip_opt_out`) controls whether we may use your request data to improve our models. Setting `mip_opt_out=true` doesn't redact your usage records, and setting `redact_usage=true` doesn't opt you out of the program. Set both if you need both.

## Troubleshooting

Redacted values aren't in your usage records, so support can't use those records to diagnose a problem that depends on them. If an issue may depend on a keyterm or other redacted value, share the request ID and the relevant values with support directly.

## Self-hosted deployments

Self-hosted deployments control the same redaction with the `redact_usage` setting in `api.toml`, which defaults to on. See [Self-hosted redact usage](/docs/self-hosted-redact-usage).
