---
title: "Agents"
source: https://docs.sentry.io/product/agents.md
path: product/agents
---

---
title: "Agents"
description: "Use AI observability in Sentry to trace and debug agent workflows and conversations. Monitor agent runs, tool calls, model interactions, token usage, and errors."
url: https://docs.sentry.io/product/agents/
---

# Agents

Sentry helps you understand what's going on with your agent workflows. Using [agent tracing](https://docs.sentry.io/product/agents/getting-started.md), it automatically collects information about agent runs, tool calls, model interactions, and errors across your entire AI pipeline—from user interaction to final response. You can also replay past conversations. If you are looking for MCP monitoring, see [MCP Servers](https://docs.sentry.io/product/mcp-servers.md).

## [Get Started](https://docs.sentry.io/product/agents.md#get-started)

To start debugging agents, you must have an existing Sentry account and project set up. If you don't have one, [create an account here](https://sentry.io/signup/).

Use agent tracing by [setting up Sentry for Agents](https://docs.sentry.io/product/agents/getting-started.md) and [name your agents](https://docs.sentry.io/product/agents/naming.md) so they're identifiable in the dashboard.

## [Example Use Cases](https://docs.sentry.io/product/agents.md#example-use-cases)

* Your agent is failing silently during tool execution, and you want to trace the complete agent flow to identify where it's breaking.
* Users report that your agent is returning unexpected or malformed responses, and you need to debug the full context of prompts, model calls, and outputs.
* Your agent workflows are experiencing performance issues, and you want to identify which steps (model calls, tool usage, or custom logic) are causing bottlenecks.

## [Related Features](https://docs.sentry.io/product/agents.md#related-features)

[![](https://docs.sentry.io/ai/img/IconCompass.svg)](https://docs.sentry.io/product/agents/conversations.md)

### [Conversations](https://docs.sentry.io/product/agents/conversations.md)

[Replay past conversations with your AI assistants. See every message and tool call in a chat-like view.](https://docs.sentry.io/product/agents/conversations.md)

[![](https://docs.sentry.io/ai/img/IconStats.svg)](https://docs.sentry.io/product/agents/dashboards.md)

### [Agents Dashboards](https://docs.sentry.io/product/agents/dashboards.md)

[View agent executions, model costs, token usage, tool calls, and recent errors in the Agents Dashboards.](https://docs.sentry.io/product/agents/dashboards.md)

## Pages in this section

- [Set Up](https://docs.sentry.io/product/agents/getting-started.md)
- [Agents Dashboards](https://docs.sentry.io/product/agents/dashboards.md)
- [Conversations](https://docs.sentry.io/product/agents/conversations.md)
- [Naming Your Agents](https://docs.sentry.io/product/agents/naming.md)
- [Model Costs](https://docs.sentry.io/product/agents/costs.md)
- [Sampling Strategies](https://docs.sentry.io/product/agents/sampling.md)
- [Data Privacy](https://docs.sentry.io/product/agents/privacy.md)

