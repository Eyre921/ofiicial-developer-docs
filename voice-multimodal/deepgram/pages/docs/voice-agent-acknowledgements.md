---
title: "Acknowledgements"
source: https://developers.deepgram.com/docs/voice-agent-acknowledgements.md
path: docs/voice-agent-acknowledgements
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Acknowledgements

&#x20;Voice Agent

When the client sends an [`UpdateListen`](/docs/voice-agent-update-listen), [`UpdateThink`](/docs/voice-agent-update-think), [`UpdateSpeak`](/docs/voice-agent-update-speak), or [`UpdatePrompt`](/docs/voice-agent-update-prompt) message, the server applies the change and replies with a corresponding acknowledgement event. The new configuration takes effect immediately and applies to every subsequent request.

You do not need to handle these events unless you want to verify that an update landed.

## `ListenUpdated`

The server sends `ListenUpdated` after applying an [`UpdateListen`](/docs/voice-agent-update-listen) message.

```json JSON
{
  "type": "ListenUpdated"
}
```

## `ThinkUpdated`

The server sends `ThinkUpdated` after applying an [`UpdateThink`](/docs/voice-agent-update-think) message. Because `UpdateThink` replaces the entire Think provider configuration (model, prompt, endpoint, and functions), `ThinkUpdated` confirms that the full replacement landed.

```json JSON
{
  "type": "ThinkUpdated"
}
```

## `SpeakUpdated`

The server sends `SpeakUpdated` after applying an [`UpdateSpeak`](/docs/voice-agent-update-speak) message.

```json JSON
{
  "type": "SpeakUpdated"
}
```

## `PromptUpdated`

The server sends `PromptUpdated` after applying an [`UpdatePrompt`](/docs/voice-agent-update-prompt) message.

```json JSON
{
  "type": "PromptUpdated"
}
```
