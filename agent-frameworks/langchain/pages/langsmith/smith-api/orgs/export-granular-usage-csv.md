---
title: "Export Granular Usage Csv"
source: https://docs.langchain.com/langsmith/smith-api/orgs/export-granular-usage-csv
path: langsmith/smith-api/orgs/export-granular-usage-csv
---

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing/granular-usage/export
Export granular usage data as CSV.

Same `kind` semantics as `/granular-usage`. The CSV's value columns
vary by kind:
- `traces`: single `Traces` column.
- `langsmith_deployments`: `Nodes Executed`, `Agent Runs`,
  `Agent Uptime (seconds)` columns.
Dimension columns are identical across kinds.
