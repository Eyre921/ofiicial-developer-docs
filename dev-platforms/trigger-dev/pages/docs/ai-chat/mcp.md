---
title: "MCP Server"
source: https://trigger.dev/docs/ai-chat/mcp
path: docs/ai-chat/mcp
---

Chat with your agents from any AI coding tool using the Trigger.dev MCP server.

<Warning>
  The AI Agents and Prompts surface ships as part of the **v4.5 release candidate**. Install with `@trigger.dev/sdk@rc` (or pin `4.5.0-rc.0` or later) to use these features — they aren't yet on the latest stable, and APIs may still change before the 4.5.0 GA. See [supported AI SDK versions](/docs/ai-chat/reference#compatibility) and the [AI chat changelog](/docs/ai-chat/changelog) for details.
</Warning>

The Trigger.dev MCP server includes tools for having conversations with your chat agents directly from AI coding tools like Claude Code, Cursor, Windsurf, and others. This lets your AI assistant interact with your agents without writing any code.

## Available tools

| Tool                 | Description                           |
| -------------------- | ------------------------------------- |
| `list_agents`        | List all agents in the current worker |
| `start_agent_chat`   | Start a conversation with an agent    |
| `send_agent_message` | Send a message and get the response   |
| `close_agent_chat`   | Close a conversation                  |

See the [MCP Tools Reference](/docs/mcp-tools#agent-chat-tools) for full details on each tool.

## Typical workflow

<Steps>
  <Step title="List available agents">
    Ask your AI assistant to list agents in your project. This calls `list_agents` which returns all tasks created with [`chat.agent()`](/docs/ai-chat/backend#chat-agent) or [`chat.customAgent()`](/docs/ai-chat/custom-agents).
  </Step>

  <Step title="Start a chat">
    Start a conversation with an agent using `start_agent_chat`. This triggers a run and optionally preloads the agent so it's ready to respond immediately.

    If the agent uses `withClientData`, pass the required fields via `clientData`.
  </Step>

  <Step title="Send messages">
    Send messages with `send_agent_message`. The agent processes each message and returns the full response text, including which tools were used. The agent retains full context across messages in the same chat.
  </Step>

  <Step title="Close the chat">
    When done, close the conversation with `close_agent_chat`. This signals the agent to exit gracefully. If you skip this step, the agent will close on its own when its idle timeout expires.
  </Step>
</Steps>

## Example conversation

Here's what a typical MCP conversation with an agent looks like:

```
You: List my agents

AI: Found 3 agents in worker 20250402.12 (dev):
    - support-agent (src/trigger/support.ts)
    - pr-review (src/trigger/pr-review.ts)
    - research (src/trigger/research.ts)

You: Start a chat with the support agent

AI: Agent chat started and preloaded.
    - Chat ID: abc-123
    - Agent: support-agent
    - Run ID: run_xyz

You: Ask it to look up order #4821

AI: I found order #4821. It was placed on March 15 and shipped via
    FedEx (tracking: 7891234). Current status: In Transit, estimated
    delivery March 19.

    Tools used: lookupOrder, getShippingStatus

You: Close the chat

AI: Chat abc-123 closed.
```

## Setup

If you haven't set up the MCP server yet, see the [MCP Server introduction](/docs/mcp-introduction) for installation and client configuration.

Agent chat tools require:

* A running dev server (`trigger dev`) or a deployed worker
* At least one agent defined with [`chat.agent()`](/docs/ai-chat/backend#chat-agent) or [`chat.customAgent()`](/docs/ai-chat/custom-agents)

## How it works

Under the hood, the MCP tools use the same protocol as the [frontend transport](/docs/ai-chat/frontend) and [AgentChat SDK](/docs/ai-chat/server-chat):

1. **`start_agent_chat`** triggers a task run with the `preload` trigger and stores the session (run ID, chat ID) in memory.
2. **`send_agent_message`** sends the message via the run's input stream and subscribes to the output SSE stream to collect the agent's full response.
3. **`close_agent_chat`** sends a close signal via the input stream and removes the session.

Sessions are held in-memory within the MCP server process. If the MCP server restarts, active sessions are lost — but the underlying agent runs continue until their idle timeout.

<Note>
  The `get_current_worker` tool also labels agents with `[agent]` in its output, making it easy to identify which tasks are agents even when listing all tasks.
</Note>

## See also

* [AgentChat SDK](/docs/ai-chat/server-chat) — programmatic server-side access to agents
* [Sub-Agents](/docs/ai-chat/patterns/sub-agents) — agents calling other agents
* [MCP Tools Reference](/docs/mcp-tools#agent-chat-tools) — full tool parameter reference
