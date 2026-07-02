---
title: "List backup schedule history"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/list_backup_schedule_history
path: reference/api/2026-04/control-plane/list_backup_schedule_history
---

GET https://api.pinecone.io/backup-schedules/{schedule_id}/history
List the execution history for a backup schedule.

<Note>
  This endpoint requires `X-Pinecone-API-Version: unstable`.
</Note>

List backups created by a specific schedule. When a backup's `status` is `Scheduled`, the `scheduled_execution_at` field indicates the planned run time. Supports pagination.

### Path parameters

<ParamField type="string">
  The ID of the backup schedule.
</ParamField>

### Query parameters

<ParamField type="integer">
  The maximum number of results to return.
</ParamField>

<ParamField type="string">
  A token for fetching the next page of results.
</ParamField>

<RequestExample>
  ```bash curl theme={null}
  curl -sS "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}/history" \
    -H "api-key: ${PINECONE_API_KEY}" \
    -H "X-Pinecone-API-Version: unstable"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "backup_id": "16098c2f-f9ff-4db3-b8b2-4b02d119cd53",
        "source_index_id": "d40265e4-a492-402b-9cf1-973b4908b7a0",
        "source_index_name": "my-index",
        "tags": {},
        "name": "my-nightly-backup-20260424T060000Z",
        "description": null,
        "status": "Scheduled",
        "scheduled_execution_at": "2026-04-24T06:00:00.244035Z",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 2,
        "schema": null,
        "record_count": null,
        "namespace_count": null,
        "size_bytes": null,
        "created_at": "2026-04-23T16:36:51.511526Z"
      }
    ],
    "pagination": null
  }
  ```
</ResponseExample>
