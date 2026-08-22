---
title: "Query sessions"
source: https://developers.notion.com/reference/notion-agent-apis/query-sessions
path: reference/notion-agent-apis/query-sessions
---

post /v1/sessions/query
Find agent sessions that an integration can access.

Use `filter`, `sorts`, and `query` to narrow the list. Follow `next_cursor` until `has_more` is `false`.
