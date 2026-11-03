---
title: "Overview"
source: https://developers.notion.com/guides/notion-agent-apis/overview
path: guides/notion-agent-apis/overview
---

Power apps and integrations with Custom Agents and the personal agent.

Build apps and integrations that bring Custom Agents and the personal agent (Notion AI) into the tools and workflows your team already uses. With the Notion Agent APIs, you can power chat experiences outside Notion and manage agents programmatically.

## Chat with agents

Use sessions to start a chat, stream the agent's reply, submit an action when needed, and read its event history. These endpoints let you bring Custom Agents or the personal agent into a Slack bot, internal tool, or mobile client.

> [card] [Create or update a session](/reference/notion-agent-apis/update-session)
>
> Start a session, send a message, submit an action, or stream a turn.

> [card] [Retrieve a session](/reference/notion-agent-apis/retrieve-session)
>
> Read the current state of a session.

> [card] [Query sessions](/reference/notion-agent-apis/query-sessions)
>
> Find accessible sessions.

> [card] [Query session events](/reference/notion-agent-apis/query-session-events)
>
> Page through a session's event history.

> [card] [Cancel a session](/reference/notion-agent-apis/cancel-session)
>
> Stop an in-progress session.

## Manage agents

Find the agents your token can access, track their usage, and change their settings, status, and credit limits. Use these endpoints to build a usage dashboard or an administrative console for Custom Agents.

> [card] [Query agents](/reference/notion-agent-apis/query-agents)
>
> Find the agents the integration can access.

> [card] [Retrieve an agent](/reference/notion-agent-apis/retrieve-agent)
>
> Get one agent's metadata.

> [card] [Retrieve agent insights](/reference/notion-agent-apis/retrieve-agent-insights)
>
> Read credits used and runs completed for a Custom Agent or your personal agent.

> [card] [Update an agent](/reference/notion-agent-apis/update-agent)
>
> Change an agent's name, model, status, or favorite state.

> [card] [Update an agent credit limit](/reference/notion-agent-apis/update-agent-credit-limit)
>
> Set or clear a Custom Agent's credit limit.

> [card] [Batch manage agent](/reference/notion-agent-apis/batch-manage-agent)
>
> Apply several agent management operations asynchronously.

> [card] [Delete an agent](/reference/notion-agent-apis/delete-agent)
>
> Soft-delete a Custom Agent you no longer need.

## Authentication and access

You can authenticate API requests with either a personal access token or a [connection token](/guides/authorization/overview):

* A **[personal access token](/guides/connections-and-tokens/personal-access-tokens)** acts as you and uses your existing access to Custom Agents.
* A **connection token** can access Custom Agents shared with its connection. To read agents and start or read sessions, it needs the **View sessions and interact with agents** capability. To update an agent or change its status, it needs the **Edit selected agents** capability. A connection can't delete an agent or change a credit limit. A connection with only Edit selected agents gets a `403` from the read and session endpoints. See [Connection capabilities](/reference/capabilities#agent-capabilities) for details.

**The personal agent**

Each user's personal agent (Notion AI) has the agent ID `notion_ai`. Only a personal access token can use it, and it always means the personal agent of the user the token acts as. A connection token receives a `404` `object_not_found` for `notion_ai`. You can chat with the personal agent, read its insights, and change its name and model. It has no status control or credit limit, and you can't delete it. Sessions you start with it belong to you, like any session you start with a personal access token.

**Access requirements**

Access to a Custom Agent is evaluated per agent, using the same permissions that apply in Notion:

* **Read access** lets you read a Custom Agent. Session access has its own rules, described below.
* **Edit access** lets you [update](/reference/notion-agent-apis/update-agent) a Custom Agent's name, description, model, or status. With a personal access token, it also lets you [delete](/reference/notion-agent-apis/delete-agent) the agent. Workspace admins can also delete agents with the [Admin API](/reference/admin/delete-agent).
* **Full access** lets you read a Custom Agent's credit limit. Otherwise, the limit is `hidden`. Only a personal access token for a user with full access can change it through this API. Workspace admins can also change it with the [Admin API](/reference/admin/update-agent-credit-limit).

**Session access**

Session access also depends on who created the session:

* A connection token can read only the sessions its connection created. This holds even when the connection can view or edit the Custom Agent. It can't read chats in the Notion app, trigger runs, or sessions from other connections.
* A personal access token can read the sessions you created, in Notion or with any of your personal access tokens in that workspace. Replacing or revoking a token doesn't hide its sessions from your other tokens. It can read other sessions on a Custom Agent if you can comment on or edit that Custom Agent in Notion.
* Wider read access does not extend to writes. A connection token can send messages to, update, or cancel only the sessions its connection created. A personal access token can do so only for sessions you created.
* Retrieving a session you can't read, or its events, returns `404` `object_not_found`. Query sessions leaves it out of the results instead.

Sessions created with a personal access token belong to that user, who can also continue them in the Notion app. Sessions created with a connection token have no user, so nobody can reply to them in Notion; continue them through the API. To share one conversation between Notion and the API, start the session with a personal access token for the user who will reply in Notion.
