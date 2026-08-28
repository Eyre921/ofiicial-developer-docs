---
title: "Inputs: Client Messages"
source: https://developers.deepgram.com/docs/voice-agent-inputs.md
path: docs/voice-agent-inputs
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Inputs: Client Messages

Client Messages are JSON-formatted commands that the client sends to the Deepgram server over the WebSocket connection during a voice agent interaction. These messages allow the client to control various aspects of the conversation, configure the agent, and provide necessary information.

## List of Client Messages

* [`Settings`](/docs/voice-agent-settings): Initializes the voice agent, sets up audio transmission formats, and optionally provides conversation history context before any voice data is exchanged.
* [`Update Listen`](/docs/voice-agent-update-listen): Updates the Listen configuration on the fly — adjust EOT thresholds, keyterms, and language hints without restarting the session.
* [`Update Think`](/docs/voice-agent-update-think): Replaces the entire Think provider configuration, including the model, prompt, endpoint, and functions.
* [`Update Speak`](/docs/voice-agent-update-speak): Enables changing the Speak model during the conversation.
* [`Inject Agent Message`](/docs/voice-agent-inject-agent-message): Triggers an immediate statement from the agent.
* [`Inject User Message`](/docs/voice-agent-inject-user-message): Sends a text-based message to the agent as if the user had spoken it.
* [`Update Prompt`](/docs/voice-agent-update-prompt): Updates the system prompt of the agent during the conversation.
* [`Force End Turn`](/docs/voice-agent-force-end-turn): Ends the current user turn immediately. Requires a Deepgram V2 (Flux) listen provider.
* [`Function Call Response`](/docs/voice-agent-function-call-response): Sends the result of a function call back to the server.
* [`Agent Keep Alive`](/docs/agent-keep-alive): Maintains the connection to prevent timeouts.

For more detailed information on the format and usage of each message, refer to the individual documentation pages for each message.
