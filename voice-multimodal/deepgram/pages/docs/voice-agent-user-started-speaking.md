---
title: "User Started Speaking"
source: https://developers.deepgram.com/docs/voice-agent-user-started-speaking.md
path: docs/voice-agent-user-started-speaking
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# User Started Speaking

&#x20;Voice Agent

The `userStartedSpeaking` message confirms when a user begins to speak.

## Purpose

The `UserStartedSpeaking` message is sent by the server to notify the client that the user has begun speaking, prompting the client to stop any ongoing agent audio playback and discard any buffered audio, ensuring that the user's input is prioritized and processed immediately.

## Example Payload

The server will send a `UserStartedSpeaking` message every time the user begins a new utterance. If the client is playing agent audio when this message is received, it should stop playback immediately and discard all of its buffered agent audio.

```json JSON
{
  "type": "UserStartedSpeaking"
}
```
