---
title: "Quickstart"
source: https://developers.notion.com/guides/notion-agent-apis/quickstart
path: guides/notion-agent-apis/quickstart
---

Pick a Custom Agent, start a chat, and read its reply through the API.

<Note>
  This API is in public beta
</Note>

## Prerequisites

**A Custom Agent to chat with**

You need an existing Custom Agent because it's the Agent you'll chat with in this quickstart. In step 1, you'll use the API to choose the Agent, then use its ID to start a chat in step 2. The API works with Custom Agents that already exist in the Notion app; it does not create them.

To create a new Custom Agent, see [Build a Custom Agent](https://www.notion.com/help/custom-agents#build-a-custom-agent).

**A personal access token to authenticate requests**

This quickstart sends API requests on your behalf, so each request needs a [personal access token](/guides/get-started/personal-access-tokens) (PAT). It lets you authenticate as yourself without setting up OAuth and carries your own access, so it can reach exactly the Custom Agents you can reach in Notion.

<Steps>
  <Step>
    Open <a href={personalAccessTokensUrl}>Personal access tokens</a> in the Developer portal.
  </Step>

  <Step>
    Select **New token**.
  </Step>

  <Step>
    Enter a name, select the **Notion API** capability, and then select **Create token**. That capability covers the Agents API — there is nothing else to enable.
  </Step>

  <Step>
    Copy the token and save it somewhere secure. You won't be able to see it again.
  </Step>
</Steps>

Set the token as an environment variable so you can use it in the examples below. This lasts for your current terminal session — run it again if you open a new window.

<CodeGroup>
  ```bash macOS / Linux theme={null}
  export NOTION_API_KEY=ntn_***
  ```

  ```powershell Windows (PowerShell) theme={null}
  $env:NOTION_API_KEY = "ntn_***"
  ```
</CodeGroup>

## Step 1: Pick a Custom Agent

Pick the Custom Agent you want to chat with. It can be the Custom Agent you created for this quickstart or an existing Custom Agent in your workspace that you can access. Use [Query agents](/reference/notion-agent-apis/query-agents) to find it.

The example below narrows results to Custom Agents you created. Remove the `created_by` filter to choose another Custom Agent you can access.

```bash curl theme={null}
curl -X POST https://api.notion.com/v1/agents/query \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {
      "property": "created_by",
      "people": { "contains": "me" }
    },
    "sorts": [{ "property": "created_time", "direction": "descending" }],
    "page_size": 10
  }'
```

You get back a list of your Custom Agents, most recently created first:

```json Response theme={null}
{
  "object": "list",
  "type": "agent",
  "results": [
    {
      "object": "agent",
      "id": "1f0c7c06-781b-4987-9986-5c8dd3028013",
      "agent_type": "custom_agent",
      "name": "Quickstart agent",
      "description": "Answers questions concisely.",
      "instructions_page_id": "1f0c7c06-781b-4987-9986-5c8dd3028020",
      "icon": { "type": "emoji", "emoji": "🤖" },
      "model": { "mode": "pinned", "id": "claude-sonnet-5" },
      "connections": [],
      "status": "active",
      "pause_reason": null,
      "created_by": {
        "type": "user",
        "id": "9f7dd486-3431-4f8b-b8bf-491287953a01"
      },
      "agent_version": {
        "id": "1f0c7c06-781b-4987-9986-5c8dd3028021",
        "number": 1,
        "published_at": "2026-08-14T12:04:11.000Z"
      },
      "created_time": "2026-08-14T12:00:00.000Z",
      "last_edited_time": "2026-08-14T12:04:11.000Z",
      "last_run_at": null,
      "credit_limit": null,
      "triggers": []
    }
  ],
  "has_more": false,
  "next_cursor": null
}
```

Copy the `id` of the Custom Agent you chose — that's what you'll chat with. Save it as an environment variable too:

<CodeGroup>
  ```bash macOS / Linux theme={null}
  export AGENT_ID=1f0c7c06-781b-4987-9986-5c8dd3028013
  ```

  ```powershell Windows (PowerShell) theme={null}
  $env:AGENT_ID = "1f0c7c06-781b-4987-9986-5c8dd3028013"
  ```
</CodeGroup>

## Step 2: Start a new Agent chat

Send your agent a message by creating a session with [Create or update a session](/reference/notion-agent-apis/update-session). A session is one conversation: you create it with the first message, then keep sending to the same `session_id` to continue.

```bash curl theme={null}
curl -X POST https://api.notion.com/v1/sessions \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11" \
  -H "Content-Type: application/json" \
  -d "{
    \"agent_id\": \"$AGENT_ID\",
    \"message\": \"What can you help me with?\"
  }"
```

The response is the new session:

```json Response theme={null}
{
  "object": "session",
  "id": "2a1c7c06-781b-4987-9986-5c8dd3028014",
  "agent_id": "1f0c7c06-781b-4987-9986-5c8dd3028013",
  "title": "Capabilities question",
  "status": "queued",
  "created_at": "2026-08-14T12:10:00.000Z",
  "updated_at": "2026-08-14T12:10:00.000Z"
}
```

Save the session ID so the follow-up requests can use it:

<CodeGroup>
  ```bash macOS / Linux theme={null}
  export SESSION_ID=2a1c7c06-781b-4987-9986-5c8dd3028014
  ```

  ```powershell Windows (PowerShell) theme={null}
  $env:SESSION_ID = "2a1c7c06-781b-4987-9986-5c8dd3028014"
  ```
</CodeGroup>

## Step 3: Read the Agent reply

The agent works asynchronously, so the session comes back as `queued`. Poll [Retrieve a session](/reference/notion-agent-apis/retrieve-session) until the status leaves `queued` and `in_progress`:

```bash curl theme={null}
curl https://api.notion.com/v1/sessions/$SESSION_ID \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11"
```

**Stream the response instead.**

To watch the turn as it happens instead of polling, send the same create request with `Accept: text/event-stream`. See [Create or update a session](/reference/notion-agent-apis/update-session).

Once the status is `completed`, read the Agent reply from the session's event history with [Query session events](/reference/notion-agent-apis/query-session-events):

```bash curl theme={null}
curl -X POST https://api.notion.com/v1/sessions/$SESSION_ID/events/query \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11" \
  -H "Content-Type: application/json" \
  -d '{ "filter": { "property": "type", "event_type": { "equals": "agent.message" } } }'
```

The agent's answer comes back as an `agent.message` event:

```json Response theme={null}
{
  "object": "list",
  "type": "session_event",
  "session_event": {},
  "results": [
    {
      "object": "session_event",
      "id": "3b2c7c06-781b-4987-9986-5c8dd3028015",
      "session_id": "2a1c7c06-781b-4987-9986-5c8dd3028014",
      "sequence": 102,
      "created_at": "2026-08-14T12:10:04.000Z",
      "type": "agent.message",
      "content": [
        { "type": "text", "text": "I can help you draft and summarize documents." }
      ],
      "created_by": {
        "id": "1f0c7c06-781b-4987-9986-5c8dd3028013",
        "type": "bot"
      },
      "metadata": { "model": "claude-sonnet-5" }
    }
  ],
  "has_more": false,
  "next_cursor": null
}
```

That's a full round trip: you sent a message to a Custom Agent and read its response from the session events.

## Common questions

<AccordionGroup>
  <Accordion title="I don't see Agents in the sidebar">
    Custom Agents are available on Business and Enterprise plans. Ask a workspace owner whether your workspace is on an eligible plan.
  </Accordion>

  <Accordion title="I don't see the option to create a token">
    On Business and Enterprise plans, PAT creation is restricted by default. Ask a workspace owner to enable it in **Settings → Connections**.

    See [Who can create PATs](/guides/get-started/personal-access-tokens#who-can-create-pats).
  </Accordion>

  <Accordion title="How do I use the examples in PowerShell?">
    The `curl` examples are written for a Unix shell. In PowerShell, refer to the variables as `$env:NOTION_API_KEY`, `$env:AGENT_ID`, and `$env:SESSION_ID`.
  </Accordion>

  <Accordion title="How else can I find a Custom Agent?">
    [Query agents](/reference/notion-agent-apis/query-agents) also takes a free-text `query` that matches names and descriptions, along with filters on fields like `id`, `agent_type`, `created_time`, and `connections`. Sorting is available on `created_time` and `last_run_at`.
  </Accordion>
</AccordionGroup>

## Next steps

You've found a Custom Agent through the API and started a chat. From here you can:

* **Keep the conversation going.** Send another message to the same `session_id` for a follow-up, or [submit an action](/reference/notion-agent-apis/update-session) the agent is waiting on.
* **Track what your agents cost.** Read [agent insights](/reference/notion-agent-apis/retrieve-agent-insights) for credits used and runs completed per agent to build a usage dashboard.
* **Set guardrails.** Give an agent a [credit limit](/reference/notion-agent-apis/update-agent-credit-limit), or [disable it](/reference/notion-agent-apis/update-agent-status) when something looks wrong.
* **Batch manage agent.** Apply status, credit-limit, and delete operations in a single [asynchronous batch](/reference/notion-agent-apis/batch-manage-agent).

See the [Overview](/guides/notion-agent-apis/overview) for the full set of endpoints.
