---
title: "Overview"
source: https://developers.notion.com/guides/notion-agent-apis/overview
path: guides/notion-agent-apis/overview
---

Power apps and integrations with Custom Agents.

Build apps and integrations that bring Custom Agents into the tools and workflows your team already uses. With the Notion Agent APIs, you can power chat experiences outside Notion and manage Custom Agents programmatically.

> [!NOTE]
>
> This API is in public beta

## Chat with Custom Agents

Use sessions to start a chat, stream the Agent's reply, submit an action when needed, and read its event history. These endpoints let you bring Custom Agents into a Slack bot, internal tool, or mobile client.

> **[Create or update a session](/reference/notion-agent-apis/update-session)**
>
> Start a session, send a message, submit an action, or stream a turn.

> **[Retrieve a session](/reference/notion-agent-apis/retrieve-session)**
>
> Read the current state of a session.

> **[Query sessions](/reference/notion-agent-apis/query-sessions)**
>
> Find accessible sessions.

> **[Query session events](/reference/notion-agent-apis/query-session-events)**
>
> Page through a session's event history.

> **[Cancel a session](/reference/notion-agent-apis/cancel-session)**
>
> Stop an in-progress session.

## Manage Custom Agents

Find the Custom Agents your token can access, track their usage, and manage their status and credit limits. Use these endpoints to build a usage dashboard or an administrative console for Custom Agents.

> **[Query agents](/reference/notion-agent-apis/query-agents)**
>
> Find Custom Agents the integration can access.

> **[Retrieve an agent](/reference/notion-agent-apis/retrieve-agent)**
>
> Get one Custom Agent's metadata.

> **[Retrieve agent insights](/reference/notion-agent-apis/retrieve-agent-insights)**
>
> Read credits used and runs completed for a Custom Agent or your personal agent.

> **[Update agent status](/reference/notion-agent-apis/update-agent-status)**
>
> Enable or disable a Custom Agent.

> **[Update an agent credit limit](/reference/notion-agent-apis/update-agent-credit-limit)**
>
> Set or clear a Custom Agent's credit limit.

> **[Batch manage agent](/reference/notion-agent-apis/batch-manage-agent)**
>
> Apply several agent management operations asynchronously.

> **[Delete an agent](/reference/notion-agent-apis/delete-agent)**
>
> Soft-delete a Custom Agent you no longer need.

## Authentication and access

You can authenticate API requests with either a personal access token or a [connection token](/guides/get-started/authorization):

* A **[personal access token](/guides/get-started/personal-access-tokens)** acts as you and uses your existing access to Custom Agents.
* A **connection token** needs the **View sessions and interact with agents** capability and can access Custom Agents shared with its connection.

**Access requirements**

Access is evaluated per Custom Agent, using the same permissions that apply in Notion:

* **Read access** lets you read a Custom Agent. Session access has its own rules, described below.
* **Edit access** lets you change a Custom Agent's status or delete it.
* **Full access** lets you read or change a Custom Agent's credit limit. Otherwise, the limit is `hidden`.

**Session access**

Session access also depends on who created the session:

* A connection token can read the sessions its connection created. To read other sessions on a Custom Agent, such as chats in the Notion app, trigger runs, or sessions from other connections, the connection also needs the **Edit selected agents** capability for that Custom Agent. That capability also lets the connection change the Custom Agent's status and properties and delete it, so grant it only when you need it.
* A personal access token can read the sessions you created, in Notion or with any of your personal access tokens in that workspace. Replacing or revoking a token doesn't hide its sessions from your other tokens. It can read other sessions on a Custom Agent if you can comment on or edit that Custom Agent in Notion.
* Wider read access does not extend to writes. A connection token can send messages to, update, or cancel only the sessions its connection created. A personal access token can do so only for sessions you created.
* Retrieving a session you can't read, or its events, returns `404` `object_not_found`. Query sessions leaves it out of the results instead.

Sessions created with a personal access token belong to that user, who can also continue them in the Notion app. Sessions created with a connection token have no user, so nobody can reply to them in Notion; continue them through the API. To share one conversation between Notion and the API, start the session with a personal access token for the user who will reply in Notion.
