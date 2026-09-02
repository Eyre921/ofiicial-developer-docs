---
title: "Update Think"
source: https://developers.deepgram.com/docs/voice-agent-update-think.md
path: docs/voice-agent-update-think
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Update Think

Voice Agent

The `UpdateThink` message is a JSON message that you can use to replace the Think provider in the middle of a conversation.

## Purpose

The `UpdateThink` message is a JSON message that allows you to replace the entire Think provider configuration during a conversation, including the model, prompt, endpoint, and functions. This flexibility enables real-time adjustments to the agent's reasoning capabilities, ensuring a more dynamic and responsive interaction tailored to the evolving needs of the conversation.

Unlike [`UpdatePrompt`](/docs/voice-agent-update-prompt), which adds to the existing prompt, `UpdateThink` replaces the entire Think provider configuration. This means you can switch to a different LLM provider, change the model, set a completely new prompt, and reconfigure functions all in a single message.

## Example Payloads

To send the `UpdateThink` message, you need to send the following JSON message to the server:

```json JSON
{
    "type": "UpdateThink",
    "think": {
        "provider": {
            "type": "open_ai",
            "model": "gpt-4o-mini"
        },
        "prompt": "You are a helpful voice assistant."
    }
}
```

Upon receiving the `UpdateThink` message, the server will process all remaining audio data and return a [`ThinkUpdated`](/docs/voice-agent-acknowledgements#thinkupdated) message.

```json JSON
{
    "type": "ThinkUpdated"
}
```
