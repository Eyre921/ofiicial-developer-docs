---
title: "Inject User"
source: https://developers.deepgram.com/docs/voice-agent-inject-user-message.md
path: docs/voice-agent-inject-user-message
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Inject User

Voice Agent

The `InjectUserMessage` is a JSON message you can send to the agent to interact with the agent using text. This is useful when you need to trigger an agent response from text input.

## Purpose

The `InjectUserMessage` message provides a way to have the agent "hear" something without the user actually speaking it. The agent will respond as if the user had spoken the message.

## Example Payloads

To send the `InjectUserMessage` message, you need to send the following JSON message to the server:

```json JSON
{
  "type": "InjectUserMessage",
  "content": "" // The text phrase or statement the agent should listen for
}
```

## Use Cases

Some common ways to use the `InjectUserMessage` are:

* A user using a chat or text interface to interact with an agent.
* Automated testing of an agent where text is used to trigger an agent response.
