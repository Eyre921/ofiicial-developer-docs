---
title: "Create or update a session"
source: https://developers.notion.com/reference/notion-agent-apis/update-session
path: reference/notion-agent-apis/update-session
---

post /v1/sessions
Start a session, send a message, submit an action, or stream a session turn.

Omit `session_id` to start a session, or provide one to add a message or submit a required action to an existing session.

### Stream a session turn

Send the same request with `Accept: text/event-stream` to receive server-sent events instead of a JSON session response. Streaming supports replaying an event with `continue_from`; that field is only valid with the SSE response.

```bash theme={null}
curl --request POST "https://api.notion.com/v1/sessions" \
  --header "Authorization: Bearer $NOTION_TOKEN" \
  --header "Notion-Version: 2026-03-11" \
  --header "Accept: text/event-stream" \
  --header "Content-Type: application/json" \
  --data '{"agent_id":"<agent-id>","message":"Summarize this week’s work."}'
```
