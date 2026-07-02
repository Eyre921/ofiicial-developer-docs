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

The `UpdateListen` message is a JSON message that updates the speech-to-text configuration of your existing Flux model during a conversation.

## Purpose

The `UpdateListen` message allows you to change Listen parameters on the fly without restarting the session. You can adjust end-of-turn detection thresholds, keyterms, and language hints while continuing to use the same Flux model.

The payload uses the same shape as `agent.listen` in the [`Settings`](/docs/voice-agent-settings) message — tunable fields live under `listen.provider` alongside the required provider identity.

The provider identity (`type`, `version`, `model`) is required and must match the current session. You cannot change the model (e.g., switch from `flux-general-en` to `flux-general-multi`) or version mid-session. Attempting to do so is rejected with a `Warning` (code `UPDATE_LISTEN_UNSUPPORTED_FIELDS_CHANGED`) and the session keeps its existing config.

### Tunable Parameters

| Parameter                             | Type    | Description                                                                                                                                                            |
| ------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `listen.provider.eot_threshold`       | Number  | Confidence threshold for [end-of-turn detection](/docs/flux/configuration#parameter-details). Valid range: `0.5` - `0.9`.                                              |
| `listen.provider.eager_eot_threshold` | Number  | Confidence threshold for [eager end-of-turn detection](/docs/flux/configuration#parameter-details). Valid range: `0.3` - `0.9`.                                        |
| `listen.provider.eot_timeout_ms`      | Integer | Time in milliseconds after speech to finish a turn regardless of EOT confidence.                                                                                       |
| `listen.provider.keyterms`            | Array   | [Keyterms](/docs/keyterm) to boost recognition for. Replaces the current keyterms list.                                                                                |
| `listen.provider.language_hints`      | Array   | Array of BCP-47 language codes to bias toward. Only supported with `flux-general-multi`. See [supported languages](/docs/flux/language-prompting#supported-languages). |

### Partial Update Semantics

`UpdateListen` is a partial update — any tunable field you omit keeps its current value, with one exception:

`language_hints` is cleared (reset to empty) when omitted. Always re-send `language_hints` if you want to preserve language biasing.

## Example Payloads

To send the `UpdateListen` message, send the following JSON message to the server:

```json JSON
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
