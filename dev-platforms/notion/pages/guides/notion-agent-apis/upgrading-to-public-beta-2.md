---
title: "Upgrading to public beta"
source: https://developers.notion.com/guides/notion-agent-apis/upgrading-to-public-beta
path: guides/notion-agent-apis/upgrading-to-public-beta
---

Migrate your private alpha integration to the public beta.

This guide is only for customers who had early access to the private alpha of the Notion Agent APIs. If you're new to the APIs, start with the [Quickstart](/guides/notion-agent-apis/quickstart).

The public beta renames the alpha's threads-and-messages routes to sessions and events, and adds routes for agent insights and controls.

<Warning>
  **Move off alpha routes by September 30, 2026**

  If you use the alpha routes for listing agents, threads, messages, or chat, migrate to their public-beta replacements by that date. The new routes use JSON request bodies instead of query parameters and return sessions and events instead of threads and messages.
</Warning>

## What's changing

| Route description          | Alpha route                            | Public beta route                                                                                   |
| :------------------------- | :------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| Get agents                 | `GET /v1/agents`                       | [`POST /v1/agents/query`](/reference/notion-agent-apis/query-agents)                                |
| Get sessions               | `GET /v1/agents/:agent_id/threads`     | [`POST /v1/sessions/query`](/reference/notion-agent-apis/query-sessions)                            |
| Get session events         | `GET /v1/threads/:thread_id/messages`  | [`POST /v1/sessions/:session_id/events/query`](/reference/notion-agent-apis/query-session-events)   |
| Create or update a session | `POST /v1/agents/:agent_id/chat`       | [`POST /v1/sessions`](/reference/notion-agent-apis/update-session)                                  |
| Stream a session turn      | `POST /v1/agents/:agent_id/chatStream` | [`POST /v1/sessions`](/reference/notion-agent-apis/update-session) with `Accept: text/event-stream` |

You only need to migrate the routes listed above. The public beta also adds optional endpoints to retrieve or cancel sessions, view Custom Agent metadata and insights, set credit limits, enable, disable, or delete Custom Agents, and make those changes in bulk. See the [Overview](/guides/notion-agent-apis/overview) for the full set.

## Upgrade checklist

<Steps>
  <Step>
    Replace `GET /v1/agents` with `POST /v1/agents/query`, moving your query parameters into a `filter` object.
  </Step>

  <Step>
    Replace `GET /v1/agents/:agent_id/threads` with `POST /v1/sessions/query`, filtering on `agent_id`.
  </Step>

  <Step>
    Replace `GET /v1/threads/:thread_id/messages` with `POST /v1/sessions/:session_id/events/query`, and read agent replies from `agent.message` events.
  </Step>

  <Step>
    Replace `POST /v1/agents/:agent_id/chat` with `POST /v1/sessions`, moving `agent_id` into the request body.
  </Step>

  <Step>
    Replace `POST /v1/agents/:agent_id/chatStream` with `POST /v1/sessions` and `Accept: text/event-stream`, and parse server-sent events instead of NDJSON lines.
  </Step>

  <Step>
    Rename `thread_id` to `session_id` throughout your code. Handle `queued`, `in_progress`, and `terminated` in addition to the alpha statuses.
  </Step>
</Steps>

## Step-by-step guide

### Step 1: Query agents instead of listing them

[Query agents](/reference/notion-agent-apis/query-agents) is a `POST` that takes a JSON body. The alpha's query parameters become filters, each naming a `property` and pairing it with a condition object, and `name` becomes the free-text `query` field. Combine several filters with `and` or `or`.

<CodeGroup>
  ```bash Public beta theme={null}
  curl -X POST https://api.notion.com/v1/agents/query \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11" \
    -H "Content-Type: application/json" \
    -d '{
      "query": "research",
      "filter": { "property": "agent_type", "string": { "equals": "custom_agent" } },
      "page_size": 25
    }'
  ```

  ```bash Alpha (deprecated) theme={null}
  curl "https://api.notion.com/v1/agents?name=research&agent_type=custom_agent&page_size=25" \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11"
  ```
</CodeGroup>

The response envelope is unchanged — `results`, `has_more`, and `next_cursor` — so your pagination loop keeps working.

One thing to watch for in the results: fields you aren't entitled to read come back as the string `"hidden"` rather than being omitted. `credit_limit` needs full access to the agent, and `last_run_at` needs edit access.

See [Query agents](/reference/notion-agent-apis/query-agents) for the full filter, sort, and option list.

### Step 2: Query sessions instead of threads

A thread is now a session. [Query sessions](/reference/notion-agent-apis/query-sessions) is workspace-wide rather than nested under an agent, so the agent moves from the path into a filter.

<CodeGroup>
  ```bash Public beta theme={null}
  curl -X POST https://api.notion.com/v1/sessions/query \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11" \
    -H "Content-Type: application/json" \
    -d "{
      \"filter\": {
        \"and\": [
          { \"property\": \"agent_id\", \"string\": { \"equals\": \"$AGENT_ID\" } },
          { \"property\": \"status\", \"status\": { \"equals\": \"completed\" } }
        ]
      },
      \"sorts\": [{ \"property\": \"updated_at\", \"direction\": \"descending\" }]
    }"
  ```

  ```bash Alpha (deprecated) theme={null}
  curl "https://api.notion.com/v1/agents/$AGENT_ID/threads?status=completed&sort_by=last_edited_time&sort_direction=descending" \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11"
  ```
</CodeGroup>

The objects changed shape along with the name:

| Thread (alpha)                                                            | Session (Public beta)                                                                                 |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------- |
| `object: "thread"`                                                        | `object: "session"`                                                                                   |
| `created_time`, `last_edited_time`                                        | `created_at`, `updated_at`                                                                            |
| `status`: `pending`, `requires_action`, `completed`, `canceled`, `failed` | `status`: `queued`, `in_progress`, `requires_action`, `completed`, `failed`, `canceled`, `terminated` |
| `error` string on failure                                                 | `error` object with `code`, `message`, and `retryable`                                                |
| `sort_by` and `sort_direction` query parameters                           | `sorts` array over `created_at` and `updated_at`                                                      |

Handle `queued` and `in_progress` as separate session statuses in place of the alpha's `pending` status. Both APIs use `canceled` for a stopped turn. If your client treated stopped turns as `completed`, update that check. Handle `terminated` separately from `failed`, and treat unknown statuses as non-terminal.

### Step 3: Read events instead of messages

Message history is now an event stream. [Query session events](/reference/notion-agent-apis/query-session-events) returns one entry per thing that happened in the session — user input, agent output, thinking, tool calls, tool results, and status transitions — each with a monotonically increasing `sequence`.

<CodeGroup>
  ```bash Public beta theme={null}
  curl -X POST https://api.notion.com/v1/sessions/$SESSION_ID/events/query \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11" \
    -H "Content-Type: application/json" \
    -d '{
      "filter": { "property": "type", "event_type": { "equals": "agent.message" } },
      "sorts": [{ "property": "sequence", "direction": "ascending" }]
    }'
  ```

  ```bash Alpha (deprecated) theme={null}
  curl "https://api.notion.com/v1/threads/$THREAD_ID/messages?role=agent" \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11"
  ```
</CodeGroup>

| Thread message (alpha)                                   | Session event (Public beta)                                                                                           |
| :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `object: "thread_message"`                               | `object: "session_event"`                                                                                             |
| `role`: `user` or `agent`                                | `type`: `user.message`, `agent.message`, `agent.thinking`, `agent.tool_use`, `agent.tool_result`, or `session.status` |
| `content` string                                         | `content` array of parts, each `text` or `file`                                                                       |
| `parent` object pointing at the thread                   | `session_id`                                                                                                          |
| `created_time`                                           | `created_at`, plus `sequence`                                                                                         |
| `verbose` query parameter for thinking and tool activity | Filter on `type` for the event kinds you want                                                                         |
| `attachments` array                                      | `file` parts inside `content`                                                                                         |

Two consequences worth handling explicitly:

* **Agent replies are `agent.message` events**, and their text lives in `content` parts rather than in a single string. Concatenate the `text` parts to reconstruct the reply.
* **Errors are no longer agent messages.** The alpha surfaced inference and tool failures as `role: "agent"` messages whose `content` described the error; read the session's `error` object and its `session.status` events instead.

### Step 4: Create sessions instead of chatting

[Create or update a session](/reference/notion-agent-apis/update-session) replaces the chat route. `agent_id` moves from the path into the body, and one route now covers all three things you do to a session: start it, add a message, and answer a required action.

<CodeGroup>
  ```bash Public beta theme={null}
  curl -X POST https://api.notion.com/v1/sessions \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11" \
    -H "Content-Type: application/json" \
    -d "{
      \"agent_id\": \"$AGENT_ID\",
      \"message\": \"Summarize this week's work.\"
    }"
  ```

  ```bash Alpha (deprecated) theme={null}
  curl -X POST https://api.notion.com/v1/agents/$AGENT_ID/chat \
    -H "Authorization: Bearer $NOTION_API_KEY" \
    -H "Notion-Version: 2026-03-11" \
    -H "Content-Type: application/json" \
    -d '{ "message": "Summarize this week'\''s work." }'
  ```
</CodeGroup>

Send `session_id` to continue an existing session, and send `session_id` with `actions` to approve or reject something the agent is waiting on.

The response is a session object rather than a `chat.invocation`:

| Chat invocation (alpha)     | Session (Public beta)                     |
| :-------------------------- | :---------------------------------------- |
| `object: "chat.invocation"` | `object: "session"`                       |
| `thread_id`                 | `id`                                      |
| `invocation_id`             | No equivalent — track the session by `id` |
| `status`: always `pending`  | `status`: the full session status set     |

Poll [Retrieve a session](/reference/notion-agent-apis/retrieve-session) for the result, which the alpha had no route for — you no longer have to re-list threads to find the one you just created.

### Step 5: Switch streaming from NDJSON to server-sent events

`POST /v1/agents/:agent_id/chatStream` is replaced by the same `POST /v1/sessions` request with `Accept: text/event-stream`. The transport changes twice over: the alpha emitted newline-delimited JSON chunks that were session objects themselves, while the Public beta emits server-sent events whose `data` is an envelope naming what arrived.

```bash Public beta theme={null}
curl -X POST https://api.notion.com/v1/sessions \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2026-03-11" \
  -H "Accept: text/event-stream" \
  -H "Content-Type: application/json" \
  -d "{
    \"agent_id\": \"$AGENT_ID\",
    \"message\": \"Summarize this week's work.\"
  }"
```

Switch on each envelope's `type` rather than decoding `data` as a session event directly:

| `type`              | Payload                 | What to do with it                                                                                                                                                                      |
| :------------------ | :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `session.snapshot`  | `session`               | The session's state at the start of the stream.                                                                                                                                         |
| `event.provisional` | `event`                 | Output the agent is still producing. Expect it to be superseded; don't persist it.                                                                                                      |
| `event.committed`   | `event`                 | A durable session event, the same shape [Query session events](/reference/notion-agent-apis/query-session-events) returns. Unwrap `event.committed.event`.                              |
| `stream.timeout`    | `session_id`, `message` | The stream ended early while the turn is still running. Reconnect.                                                                                                                      |
| `stream.end`        | `session_id`, `status`  | The current turn is over. A `status` of `requires_action` means the session is waiting on you — submit the action to the same `session_id` to continue. Any other `status` is terminal. |
| `stream.error`      | `error`, `session_id`   | The turn failed. `error` carries `code`, `message`, and `retryable`.                                                                                                                    |

A dropped connection no longer costs you the turn. Persist the `id` of the last `event.committed.event` you received, then reconnect with that exact ID as `continue_from` — along with the `session_id` — and the stream replays from there. `continue_from` takes a committed event's ID, not its `sequence` and not a provisional or stream-control record, so anything else fails to resolve. See [Create or update a session](/reference/notion-agent-apis/update-session).
