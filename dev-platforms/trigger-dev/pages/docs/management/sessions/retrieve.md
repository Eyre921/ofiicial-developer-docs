---
title: "Retrieve session"
source: https://trigger.dev/docs/management/sessions/retrieve
path: docs/management/sessions/retrieve
---

v3-openapi GET /api/v1/sessions/{session}
Retrieve a single session by its friendly id (`session_…`) or your `externalId`. The response includes `triggerConfig` and the friendly `currentRunId` of the live run, if any.
