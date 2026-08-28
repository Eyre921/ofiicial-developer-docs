---
title: "Overview"
source: https://developers.notion.com/guides/notion-agent-apis/overview
path: guides/notion-agent-apis/overview
---

Power apps and integrations with Custom Agents.

Build apps and integrations that bring Custom Agents into the tools and workflows your team already uses. With the Notion Agent APIs, you can power chat experiences outside Notion and manage Custom Agents programmatically.

<Note>
  This API is in public beta
</Note>

## Chat with Custom Agents

Use sessions to start a chat, stream the Agent's reply, submit an action when needed, and read its event history. These endpoints let you bring Custom Agents into a Slack bot, internal tool, or mobile client.

<CardGroup>
  <Card title="Create or update a session" icon="comments" href="/reference/notion-agent-apis/update-session">
    Start a session, send a message, submit an action, or stream a turn.
  </Card>

  <Card title="Retrieve a session" icon="message" href="/reference/notion-agent-apis/retrieve-session">
    Read the current state of a session.
  </Card>

  <Card title="Query sessions" icon="magnifying-glass" href="/reference/notion-agent-apis/query-sessions">
    Find accessible sessions.
  </Card>

  <Card title="Query session events" icon="clock-rotate-left" href="/reference/notion-agent-apis/query-session-events">
    Page through a session's event history.
  </Card>

  <Card title="Cancel a session" icon="circle-stop" href="/reference/notion-agent-apis/cancel-session">
    Stop an in-progress session.
  </Card>
</CardGroup>

## Manage Custom Agents

Find the Custom Agents your token can access, track their usage, and manage their status and credit limits. Use these endpoints to build a usage dashboard or an administrative console for Custom Agents.

<CardGroup>
  <Card title="Query agents" icon="magnifying-glass" href="/reference/notion-agent-apis/query-agents">
    Find Custom Agents the integration can access.
  </Card>

  <Card title="Retrieve an agent" icon="robot" href="/reference/notion-agent-apis/retrieve-agent">
    Get one Custom Agent's metadata.
  </Card>

  <Card title="Retrieve agent insights" icon="chart-line" href="/reference/notion-agent-apis/retrieve-agent-insights">
    Read credits used and runs completed for a Custom Agent or your personal agent.
  </Card>

  <Card title="Update agent status" icon="toggle-on" href="/reference/notion-agent-apis/update-agent-status">
    Enable or disable a Custom Agent.
  </Card>

  <Card title="Update an agent credit limit" icon="coins" href="/reference/notion-agent-apis/update-agent-credit-limit">
    Set or clear a Custom Agent's credit limit.
  </Card>

  <Card title="Batch manage agent" icon="list-check" href="/reference/notion-agent-apis/batch-manage-agent">
    Apply several agent management operations asynchronously.
  </Card>

  <Card title="Delete an agent" icon="trash" href="/reference/notion-agent-apis/delete-agent">
    Soft-delete a Custom Agent you no longer need.
  </Card>
</CardGroup>

## Authentication and access

You can authenticate API requests with either a personal access token or a [connection token](/guides/get-started/authorization):

* A **[personal access token](/guides/get-started/personal-access-tokens)** acts as you and uses your existing access to Custom Agents.
* A **connection token** needs the **Interact with agents** capability and can access Custom Agents shared with its connection.

**Access requirements**

Access is evaluated per Custom Agent, using the same permissions that apply in Notion:

* **Read access** lets you read a Custom Agent and its sessions.
* **Edit access** lets you change a Custom Agent's status or delete it.
* **Full access** lets you read or change a Custom Agent's credit limit. Otherwise, the limit is `hidden`.
