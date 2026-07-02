---
title: "Agent Thinking"
source: https://developers.deepgram.com/docs/voice-agent-agent-thinking.md
path: docs/voice-agent-agent-thinking
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Agent Thinking

&#x20;Voice Agent

The `AgentThinking` message is used to inform the client the agent is processing information.

## Purpose

The `AgentThinking` message informs the client when the agent is processing internally, without verbalizing its thoughts. This allows the system to handle non-verbalized reasoning and, in some cases, determine which functions to call, ensuring smoother and more dynamic interactions.

## Example Payload

The server will send an `AgentThinking` message to inform the client of a non-verbalized agent thought. When functions are available, some LLMs use these thoughts to decide which functions to call.

```json JSON
{
  "type": "AgentThinking",
  "content": "" // The text of the agent's thought
}
```
