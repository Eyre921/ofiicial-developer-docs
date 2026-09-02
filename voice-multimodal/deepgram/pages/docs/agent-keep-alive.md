---
title: "Agent Keep Alive"
source: https://developers.deepgram.com/docs/agent-keep-alive.md
path: docs/agent-keep-alive
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Agent Keep Alive

Voice Agent

`KeepAlive` is a JSON message you send to the server to keep an idle WebSocket open. The server closes connections that go silent, so when you stop streaming audio for an extended period, send `KeepAlive` to hold the session.

Most agent conversations do not need `KeepAlive`. You will normally stream microphone audio continuously so the user can speak at any moment.

## When to use it

Send `KeepAlive` only during a period when the client is not sending audio. While idle, send one `KeepAlive` every `8` seconds.

## Example payload

```json JSON
{
  "type": "KeepAlive"
}
```

The server does not respond to `KeepAlive`.

`KeepAlive` does not extend the [maximum session length](/docs/voice-agent-errors-warnings#maximum-session-length) of 2 hours. The server closes every session at the 2-hour mark, however much traffic it has seen.
