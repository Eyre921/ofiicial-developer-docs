---
title: "Read Shared Delta Stream"
source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-delta-stream
path: langsmith/smith-api/public/read-shared-delta-stream
---

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/datasets/runs/delta/stream
Stream feedback deltas for multiple feedback keys.

Returns results in chunks as they become available. Each chunk contains
results for one or more feedback keys. Errors for individual chunks are
included in the response rather than failing the entire operation.

Response format (SSE):
    event: data
    data: {"feedback_deltas": {"key1": {session_id: {...}}, ...}, "errors": null}

    event: data
    data: {"feedback_deltas": {"key2": {...}}, "errors": null}

    event: end
