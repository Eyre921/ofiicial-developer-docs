---
title: "Retrieve an async task"
source: https://developers.notion.com/reference/retrieve-async-task
path: reference/retrieve-async-task
---

openapi.json GET /v1/async_tasks/{task_id}
Retrieve the status and result of an async task.

Use this endpoint to poll an `async_task` returned by an operation that was accepted for background execution.

The first async-capable REST endpoints are:

| Operation                           | Async support                                                           |
| ----------------------------------- | ----------------------------------------------------------------------- |
| `POST /v1/pages`                    | Supported only when the request includes the `markdown` body parameter. |
| `PATCH /v1/pages/:page_id/markdown` | Supported for markdown update requests.                                 |

Set `allow_async: true` on a supported operation to opt into an `async_task` response. When `allow_async` is omitted or `false`, the endpoint keeps its existing synchronous response shape. `allow_async` changes response behavior only; it does not change validation, permissions, or the operation being performed.

<Note>
  Async task completion is polling-first in this version. Webhook notifications and ETA estimates are not part of the async task contract.
</Note>

### Async task response

When an operation is accepted for background execution, the supported endpoint returns HTTP `202` with an `async_task` object:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "queued",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "poll_after_seconds": 2,
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  }
}
```

Use `status_url`, or call this endpoint with the returned `id`, to check completion.

### Status values

| Status      | Meaning                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| `queued`    | The task has been accepted and persisted, but processing has not started.                                      |
| `running`   | A worker is processing the task.                                                                               |
| `retrying`  | The task hit a retryable infrastructure or downstream-service failure and is scheduled to retry.               |
| `succeeded` | The task completed successfully. The response includes a `result` object.                                      |
| `failed`    | The task failed terminally. The response includes an `error` object using the standard Public API error shape. |

For non-terminal statuses (`queued`, `running`, and `retrying`), wait at least `poll_after_seconds` before polling again.

Completed and failed task metadata is retained for a bounded period. After expiry, polling the task returns the standard not-found response, so store any final result data your application needs.

### Polling responses

An in-progress task includes the latest non-terminal status and polling guidance:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "running",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "poll_after_seconds": 2,
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  }
}
```

A successful task includes the operation result:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "succeeded",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  },
  "result": {
    "object": "page_markdown",
    "id": "page-uuid",
    "markdown": "# Updated page\n\nThe update is complete.",
    "truncated": false,
    "unknown_block_ids": []
  }
}
```

A failed task includes a standard Public API error object:

```json theme={null}
{
  "object": "async_task",
  "id": "task_abc123",
  "status": "failed",
  "status_url": "https://api.notion.com/v1/async_tasks/task_abc123",
  "created_time": "2026-06-29T12:00:00.000Z",
  "operation": {
    "surface": "rest",
    "name": "PATCH /v1/pages/:page_id/markdown"
  },
  "error": {
    "object": "error",
    "status": 400,
    "code": "validation_error",
    "message": "The request body was invalid."
  }
}
```

### Errors

Returns a 404 HTTP response if the async task does not exist, has expired, or is not visible to the current connection.

Returns a 429 HTTP response if polling exceeds [request limits](/reference/request-limits). Malformed requests can return a 400 HTTP response.

*Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*
