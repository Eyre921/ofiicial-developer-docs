---
title: "Get issues-agent (Engine) LCU spend per project for the calling org"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/get-issues-agent-engine-lcu-spend-per-project-for-the-calling-org
path: langsmith/smith-api/issues-agent/get-issues-agent-engine-lcu-spend-per-project-for-the-calling-org
---

/langsmith/langsmith-platform-openapi.json get /issues-agent/lcu-spend
Returns one flat row per (tenant, session) pair in the
caller's organization that has Engine spend in the
window, each carrying its workspace name, project
(session) name, and Engine LCU spend. The caller groups
rows by tenant for display and sums the `lcu_total`
field across items for the org-wide total (the UI tile
does both). The window defaults to the current calendar
month (UTC) and can be overridden with `start` and `end`
(RFC 3339, capped at 31 days). Hours where the rate card
did not price a (provider, model) pair are excluded from
each row's `lcu_total` and surfaced as
`lcu_unpriced_row_count` so callers can detect billing
coverage gaps without inflating the spend number.
