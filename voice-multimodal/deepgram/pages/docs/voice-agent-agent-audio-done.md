---
title: "Agent Audio Done"
source: https://developers.deepgram.com/docs/voice-agent-agent-audio-done.md
path: docs/voice-agent-agent-audio-done
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Agent Audio Done

Voice Agent

The server sends `AgentAudioDone` immediately after the last audio chunk for an agent utterance. Use this event to mark the end of a server-side stream so you can synchronize follow-up actions with the agent finishing.

## Client behavior

`AgentAudioDone` does not mean the user has heard the agent finish. Audio you already received may still sit in your local playback buffer. To detect end-of-playback in the user's ears, watch your audio output queue, not this event.

## Example payload

```json JSON
{
  "type": "AgentAudioDone"
}
```
