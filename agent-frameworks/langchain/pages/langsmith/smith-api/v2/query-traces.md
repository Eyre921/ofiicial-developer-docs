---
title: "Query traces"
source: https://docs.langchain.com/langsmith/smith-api/v2/query-traces
path: langsmith/smith-api/v2/query-traces
---

/langsmith/langsmith-platform-openapi.json post /v2/traces/query
Returns a paginated list of traces (root runs) for a single tracing project. Each item carries the trace's root run plus optional trace-wide aggregates (`total_tokens`, `total_cost`, `first_token_time`) under `trace_aggregates`, so clients never have to merge by `trace_id`.

Traces are scanned within a `start_time` window: `min_start_time` defaults to 24 hours before the request, `max_start_time` defaults to the request time. Set either explicitly to widen or narrow the window.

Supports filters (`trace_filter`, `tree_filter`), cursor pagination (`cursor`), and field projection (`selects`).
