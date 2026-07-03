---
title: "Retrieve run trace"
source: https://trigger.dev/docs/management/runs/retrieve-trace
path: docs/management/runs/retrieve-trace
---

v3-openapi GET /api/v1/runs/{runId}/trace
Returns the OTel trace subtree for the requested run — the run's span as `rootSpan`, its ancestor chain, and its descendant spans. For child or nested runs in a large trace, this is scoped to that run rather than the trace-wide root.

Returns the OpenTelemetry trace subtree for the run you request. The response `trace.rootSpan` is that run's span — not necessarily the trace-wide root — with its descendant spans nested under `children`.

For a child or nested run inside a large trace, this endpoint scopes the tree to that run so you still get a useful subtree even when the full trace has more spans than the platform can return in one response.
