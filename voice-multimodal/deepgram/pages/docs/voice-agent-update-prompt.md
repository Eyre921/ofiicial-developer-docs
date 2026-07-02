---
title: "Update Prompt"
source: https://developers.deepgram.com/docs/voice-agent-update-prompt.md
path: docs/voice-agent-update-prompt
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Update Prompt

&#x20;Voice Agent

The `UpdatePrompt` message is a JSON message that you can use to update the system prompt of the agent.

## Purpose

The `UpdatePrompt` message is a JSON message that allows you to update the system prompt of the agent. `UpdatePrompt` will add to – not replace – the current prompt. This flexibility enables real-time adjustments to the agent's behavior, ensuring a more dynamic and responsive interaction tailored to the evolving needs of the conversation.

Prompt length is limited to 25,000 characters for managed LLMs and unlimited for BYO LLMs.

## Example Payloads

To send the `UpdatePrompt` message, you need to send the following JSON message to the server:

```json JSON
{
  "type": "UpdatePrompt",
  "prompt": "" // The new system prompt
}
```

Upon receiving the `UpdatePrompt` message, the server will process all remaining audio data and return a [`PromptUpdated`](/docs/voice-agent-acknowledgements#promptupdated) message.

```json JSON
{
    "type": "PromptUpdated"
}
```
