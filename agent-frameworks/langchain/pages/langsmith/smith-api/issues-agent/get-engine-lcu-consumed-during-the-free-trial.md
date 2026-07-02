---
title: "Get Engine LCU consumed during the free trial"
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/get-engine-lcu-consumed-during-the-free-trial
path: langsmith/smith-api/issues-agent/get-engine-lcu-consumed-during-the-free-trial
---

/langsmith/langsmith-platform-openapi.json get /v1/platform/engine/trial-lcu-total
Returns the org-wide sum of priced Engine LCU consumed strictly
before the GA cutoff (2026-06-01 UTC), i.e. all usage that was
free, plus the count of projects that had Engine configured.
Used to show admins how much they would have been billed and
across how many projects when deciding whether to continue.
The LCU value is Postgres-only (no in-flight Redis merge) since
the post-cutoff modal shows after all pre-cutoff usage is swept.
