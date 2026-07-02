---
title: "Welcome"
source: https://developers.deepgram.com/docs/voice-agent-welcome-message.md
path: docs/voice-agent-welcome-message
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Welcome

&#x20;Voice Agent

The welcome message confirms there has been a successful connection to the websocket.

## Purpose

The `Welcome` message serves as the initial handshake between a voice agent and the server, signaling that the websocket connection is successfully established. By including a unique `request_id`, it ensures that each interaction is traceable and distinct. This message is critical for synchronizing the client and server, enabling a voice agent to proceed with further actions.

## Example Payload

The server will immediately send a `Welcome` message as soon as the websocket opens.

```json JSON
{
  "type": "Welcome",
  "request_id": "fc553ec9-5874-49ca-a47c-b670d525a4b1"
}
```
