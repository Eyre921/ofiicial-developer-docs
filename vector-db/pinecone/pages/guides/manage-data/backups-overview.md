---
title: "Backups overview"
source: https://docs.pinecone.io/guides/manage-data/backups-overview
path: guides/manage-data/backups-overview
---

Learn how serverless index backups work in Pinecone, including scheduled backups, retention policies, and use cases for restoring or copying data.

A backup is a static copy of a serverless [index](/guides/index-data/indexing-overview) that only consumes storage. It is a non-queryable representation of a set of records. You can [create a backup](/guides/manage-data/back-up-an-index) of a serverless index, and you can [create a new serverless index from a backup](/guides/manage-data/restore-an-index). This allows you to restore the index with the same or different configurations.

## Use cases

Creating a backup is useful when performing tasks like the following:

* Protecting an index from manual or system failures.
* Temporarily shutting down an index.
* Copying the data from one index into a different index.
* Making a backup of your index.
* Experimenting with different index configurations.

## Scheduled backups

Instead of creating backups manually, you can define a recurring backup schedule that runs automatically. Each schedule includes:

* **Frequency**: Backups can run daily, weekly, or monthly.
* **Retention**: A required expiration policy that automatically deletes old backups, keeping storage costs predictable.

Each index supports one active schedule at a time. Backups created by a schedule are automatically named `{name}-{ISO8601_timestamp}`.

You can create and manage backup schedules in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups) or with the API. For step-by-step instructions, see [Schedule automated backups](/guides/manage-data/back-up-an-index#schedule-automated-backups).

<Note>
  The scheduled backups API requires `X-Pinecone-API-Version: unstable`.
</Note>

For example, to create a daily backup that expires after 7 days:

```bash theme={null}
curl -sS -X POST "https://api.pinecone.io/indexes/${INDEX_NAME}/backup-schedules" \
  -H "api-key: ${PINECONE_API_KEY}" \
  -H "X-Pinecone-API-Version: unstable" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-nightly-backup",
    "schedule": {
      "type": "time-based",
      "frequency": "daily"
    },
    "retention": {
      "expire_after_days": 7
    }
  }'
```

Deleting a schedule does not delete any backups that were previously created by it. If you delete an index, all associated schedules are automatically deleted.

For more details, see the API reference:

* [Create backup schedule](/reference/api/2026-04/control-plane/create_backup_schedule)
* [List backup schedules](/reference/api/2026-04/control-plane/list_backup_schedules)
* [Describe backup schedule](/reference/api/2026-04/control-plane/describe_backup_schedule)
* [Update backup schedule](/reference/api/2026-04/control-plane/update_backup_schedule)
* [Delete backup schedule](/reference/api/2026-04/control-plane/delete_backup_schedule)
* [List schedule history](/reference/api/2026-04/control-plane/list_backup_schedule_history)

## Performance

Backup and restore times depend upon the size of the index and number of namespaces:

* For less than 1M vectors in a namespace, backups and restores take approximately 10 minutes.
* For 100,000,000 vectors, backups and restores can take up to 5 hours.

## Quotas

| Metric              | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :------------------ | :----------- | :----------- | :------------ | :-------------- |
| Backups per project | N/A          | N/A          | 500           | 1000            |

<Note>
  Backups are not available on the Starter or Builder plans. To create backups, [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

## Limitations

Backup limitations are as follows:

* Backups are stored in the same project, cloud provider, and region as the source index.
* You can only restore an index to the same project and cloud provider as the source index. Restoring to a different region on the same cloud provider is supported using the `unstable` API version. For details, see [Restore to a different region](/guides/manage-data/restore-an-index#restore-to-a-different-region).
* Backups only include vectors that were in the index at least 15 minutes prior to the backup time. This means that if a vector was inserted into an index and a backup was immediately taken after, the recently inserted vector may not be backed up. More specifically, if a backup is created only a few minutes after the source index was created, the backup may have 0 vectors.
* You can only perform operations on backups in the current Pinecone project.
* Backups are supported for indexes without a schema definition and for integrated embedding indexes that use the records API. They are not supported for full-text search indexes with document schemas that include `full_text_search` string fields, `dense_vector` fields, or `sparse_vector` fields. Indexes with document schemas also do not support `semantic_text` fields.

## Backup and restore cost

* To understand how cost is calculated for backups and restores, see [Understanding cost](/guides/manage-cost/understanding-cost#backups-and-restores).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).
