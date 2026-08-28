---
title: "Update Listen"
source: https://developers.deepgram.com/docs/voice-agent-update-listen.md
path: docs/voice-agent-update-listen
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Update Listen

&#x20;Voice Agent

The `UpdateListen` message is a JSON message that updates the speech-to-text configuration during a conversation.

## Purpose

The `UpdateListen` message allows you to change Listen parameters on the fly without restarting the session. You can switch the speech-to-text model and language, and adjust end-of-turn thresholds and keyterms.

The payload uses the same shape as `agent.listen` in the [`Settings`](/docs/voice-agent-settings) message — every field lives under `listen.provider`.

### Tunable Parameters

| Parameter                             | Type    | Description                                                                                                                                                                                                                                             |
| ------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listen.provider.model`               | String  | Speech-to-text [model](/docs/models-languages-overview) to switch to, such as `nova-3-general` or `flux-general-multi`.                                                                                                                                 |
| `listen.provider.language`            | String  | [Language](/docs/models-languages-overview) code for transcription, such as `en` or `multi`. Supported with V1 (Nova) models.                                                                                                                           |
| `listen.provider.version`             | String  | Deepgram speech-to-text API version: `v1` for Nova models, `v2` for Flux.                                                                                                                                                                               |
| `listen.provider.eot_threshold`       | Number  | Confidence threshold for [end-of-turn detection](/docs/flux/configuration#parameter-details). Valid range: `0.5` - `1.0`. Set to `1.0` to suppress natural end-of-turn detection and end turns with [`ForceEndTurn`](/docs/voice-agent-force-end-turn). |
| `listen.provider.eager_eot_threshold` | Number  | Confidence threshold for [eager end-of-turn detection](/docs/flux/configuration#parameter-details). Valid range: `0.3` - `0.9`.                                                                                                                         |
| `listen.provider.eot_timeout_ms`      | Integer | Time in milliseconds after speech to finish a turn regardless of EOT confidence.                                                                                                                                                                        |
| `listen.provider.keyterms`            | Array   | [Keyterms](/docs/keyterm) to boost recognition for. Replaces the current keyterms list. Flux models only.                                                                                                                                               |
| `listen.provider.language_hints`      | Array   | Array of BCP-47 language codes to bias toward. Only supported with `flux-general-multi`. See [supported languages](/docs/flux/language-prompting#supported-languages).                                                                                  |

Send the fields that apply to the model you are switching to: `language` for V1 (Nova) models, and `keyterms`, the end-of-turn fields, and `language_hints` for V2 (Flux) models.

Keyterms can only be updated mid-session for Flux models. Nova-3 keyterms are fixed for the life of the session — set them in the [`Settings`](/docs/voice-agent-settings) message at the start of the session, which works for both Flux and Nova-3.

### Partial Update Semantics

`UpdateListen` is a partial update — any tunable field you omit keeps its current value, with one exception:

`language_hints` is cleared (reset to empty) when omitted. Always re-send `language_hints` if you want to preserve language biasing.

## Example Payloads

To send the `UpdateListen` message, send the following JSON message to the server:

```json Nova (V1)
{
    "type": "UpdateListen",
    "listen": {
        "provider": {
            "type": "deepgram",
            "version": "v1",
            "model": "nova-3-general",
            "language": "es"
        }
    }
}
```

```json Flux (V2)
{
    "type": "UpdateListen",
    "listen": {
        "provider": {
            "type": "deepgram",
            "version": "v2",
            "model": "flux-general-multi",
            "eot_threshold": 0.8,
            "eager_eot_threshold": 0.5,
            "eot_timeout_ms": 3000,
            "keyterms": ["Deepgram", "speech-to-text"],
            "language_hints": ["en", "es"]
        }
    }
}
```

Upon receiving the `UpdateListen` message, the server applies the changes and returns a [`ListenUpdated`](/docs/voice-agent-acknowledgements#listenupdated) message.

```json JSON
{
    "type": "ListenUpdated"
}
```
