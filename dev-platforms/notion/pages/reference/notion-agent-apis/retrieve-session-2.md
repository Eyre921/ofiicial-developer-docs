---
title: "Retrieve a session"
source: https://developers.notion.com/reference/notion-agent-apis/retrieve-session
path: reference/notion-agent-apis/retrieve-session
---

get /v1/sessions/{session_id}
Retrieve the status, metadata, and required actions for a session.

The response carries the session's status and metadata, including any actions waiting on you. To read a session's messages and agent thinking, use [Query session events](/reference/notion-agent-apis/query-session-events).
