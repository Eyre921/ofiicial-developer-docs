---
title: "Settings Applied"
source: https://developers.deepgram.com/docs/voice-agent-setting-applied-message.md
path: docs/voice-agent-setting-applied-message
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Settings Applied

&#x20;Voice Agent

The `SettingsApplied` message is a JSON message that confirms the server has successfully received and applied the `Settings` message.

## Purpose

The `SettingsApplied` message confirms that the server has successfully received and applied the `Settings` message. This ensures synchronization between the client and server, providing assurance that the desired settings are now in effect. By sending this message, the server enables the voice agent to proceed with operations based on the updated configuration.

## Example Payload

The server will send a `SettingsApplied` message as confirmation that the server received the [Settings](/docs/voice-agent-settings) message.

```json JSON
{
  "type": "SettingsApplied"
}
```
