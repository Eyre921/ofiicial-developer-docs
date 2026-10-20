---
title: "List backup schedule history"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/list_backup_schedule_history
path: reference/api/2026-07/control-plane/list_backup_schedule_history
---

GET https://api.pinecone.io/backup-schedules/{schedule_id}/history
List execution history for a Pinecone backup schedule, including scheduled runs, completed backups, statuses, and cursor-based pagination support.

> [!NOTE]
>
> This endpoint requires `X-Pinecone-Api-Version: 2026-07`.

List backups created by a specific schedule. When a backup's `status` is `Scheduled`, the `scheduled_execution_at` field indicates the planned run time. Supports pagination.

### Path parameters

**schedule\_id** `string` *required*

The ID of the backup schedule.

### Query parameters

**limit** `integer`

The maximum number of results to return.

**paginationToken** `string`

A token for fetching the next page of results.

```bash curl theme={null}
curl -sS "https://api.pinecone.io/backup-schedules/${SCHEDULE_ID}/history" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-Api-Version: 2026-07"
```
