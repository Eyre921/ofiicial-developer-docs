---
title: "Get issues-agent (engine) LCU spend per project for the calling org"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/get-issues-agent-engine-lcu-spend-per-project-for-the-calling-org
path: langsmith/smith-api/issues-agent/get-issues-agent-engine-lcu-spend-per-project-for-the-calling-org
---

/langsmith/langsmith-platform-openapi.json get /issues-agent/lcu-spend
Returns the authoritative Engine LCU spend for the caller's
organization in the window (`total_lcu`, independent of
pagination). Set `group_by=tenant` for a workspace breakdown or
`group_by=session` for a (tenant, session) breakdown — each
spend-ranked and cursor-paginated (`page_size`, `cursor`); omit
`group_by` for the total only. The window defaults to the current
calendar month (UTC) and can be overridden with `start`/`end`
(RFC 3339, capped at 31 days). Hours the rate card did not price
are excluded from LCU and surfaced via the `*_unpriced_row_count`
fields so callers can detect coverage gaps without inflating spend.
