---
title: "Convert an index to a document index"
source: https://docs.pinecone.io/guides/indexes/convert-an-index
path: guides/indexes/convert-an-index
---

Convert a Pinecone serverless legacy vector index or legacy integrated index into a new document index with full-text search, while the source keeps serving.

Converting builds a new document index from the records in a serverless legacy vector index or legacy integrated index, so you can run full-text search on that data without re-ingesting it.

> [!NOTE]
>
> This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).

## What a conversion does

* **Source**: The source index keeps serving reads and writes before, during, and after the conversion.
* **Snapshot**: The job copies the source as it stood when the job starts, as a backup does. Writes to the source after you send the request might not be in the new index.
* **IDs and fields**: Each record becomes a document with the same ID, and its fields are filled by name, as described in [Plan the schema](#plan-the-schema).
* **Namespaces**: Each source namespace becomes a namespace of the same name in the new index. Namespaces that have never held records are skipped.
* **Location**: The new index is created in the source's cloud and region, and is encrypted with the source's customer-managed encryption keys (CMEK) when it has them.
* **Billing**: A conversion is charged at the [import](/guides/cost/understand-cost#imports) rate, by the size of the source's data. A job that fails because of your data is charged for the data it read. A canceled job, or one that fails because of an internal error, isn't charged. Both indexes are billed for storage until you delete the source.

## Limitations

* Only serverless indexes in the `Ready` state can be converted, including indexes on [dedicated read nodes](/guides/optimize/dedicated-read-nodes/overview). An index in any other state, such as one that's being deleted, has failed, or is disabled, is rejected with a `412`.
* Pod-based indexes can't be converted. [Migrate the index to serverless](/guides/legacy/pod-based-indexes/migrate-a-pod-based-index-to-serverless) first, then convert the serverless index it creates.
* Bring Your Own Cloud (BYOC) indexes can't be converted.
* An index that already has a document schema can't be converted, and neither can a text index.
* With on-demand read capacity, the new index can take at most 1,000 GB of source data. For a larger source, set `read_capacity` to [dedicated read nodes](/guides/optimize/dedicated-read-nodes/overview) in the request, or contact support.
* The new index can't use the source's name or any name already taken in the project, including by an index an earlier conversion created. A name that's taken is rejected with a `409`. You can convert the same source more than once, as long as each new index has its own name.

## Plan the schema

The `schema` you pass in the request defines the new index, and Pinecone fills its fields from each source record as follows. For how to design the schema itself, see [Data modeling](/guides/indexes/data-modeling).

| Source | Target field |
| - | - |
| Dense vector | The schema's one `dense_vector` field, or its `string` field with `embed`. |
| Sparse vector | The schema's one `sparse_vector` field, or its `string` field with `sparse_embed`. |
| Metadata key that matches a full-text field name | The `string` field with `full_text_search` of the same name. The value moves into that field and is no longer metadata. |
| All other metadata | Carried over unchanged, and still filterable. |

A schema field that no source record has a value for isn't an error. The field is empty in the new index, and searching it returns no results, so name each full-text field after a metadata key your records already use.

### Schema requirements

* The dense field has to use the source's dimension and metric. A mismatch is rejected with a `400` that names the dimension or metric to set.
* A schema made only of the reserved `_values` and `_sparse_values` fields is rejected, because it describes a legacy vector index rather than a document index.

### Sources with sparse vectors

Records that carry sparse values need a field those values can go into, even when the source is an index of dense vectors. Without one, those records can't be converted, and [`error_mode`](#handle-mismatched-records) decides what happens to them. For a sparse index, the schema needs a `sparse_vector` field and no `dense_vector` field. In the new index, the dense and sparse vectors are separate fields, and a search ranks by one of them. To combine both, run a dense search and a sparse search and merge the results with [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion).

### Legacy integrated indexes

For an index created with `create_index_for_model`, declare a `string` field named after the source's embedded text field and give it `embed` (or `sparse_embed`) with the source's model. The vectors carry over, so your text isn't embedded again. Pinecone doesn't add this field for you. If you declare only a `dense_vector` field, the conversion succeeds, but the new index has no integrated embedding. A `string` field with `embed` is rejected with a `400` when the source isn't a legacy integrated index, or when the field's name or model doesn't match the source's.

### Handle mismatched records

`error_mode.on_error` decides how the job treats a source record the schema can't hold, such as a record whose metadata value for a `full_text_search` field is a number instead of a string.

* `abort` is the default. The conversion fails, and the job's `error` names the record and the reason.
* `continue` skips the record and counts it in the job's `records_skipped`.

## Run a conversion

This example converts `support-tickets`, a serverless index of 1024-dimension cosine vectors whose records carry `ticket_text`, `product`, and `priority` metadata. The new index, `support-tickets-docs`, keeps the vectors for semantic search and indexes `ticket_text` for full-text search, with `product` and `priority` still filterable.

### 1. Check the source index

Read the source's dimension and metric, which your schema has to match, and confirm that its state is `Ready`.

```bash Request theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X GET https://api.pinecone.io/indexes/support-tickets \
     -H "Accept: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07"
```

```json Response expandable theme={null}
{
  "name": "support-tickets",
  "host": "support-tickets-govk0nt.svc.aped-4627-b74a.pinecone.io",
  "status": {
    "ready": true,
    "state": "Ready"
  },
  "deployment": {
    "deployment_type": "managed",
    "region": "us-east-1",
    "cloud": "aws",
    "environment": "aped-4627-b74a"
  },
  "read_capacity": {
    "mode": "OnDemand",
    "status": {
      "state": "Ready",
      "current_shards": null,
      "current_replicas": null
    }
  },
  "schema": {
    "fields": {
      "_values": {
        "type": "dense_vector",
        "description": null,
        "dimension": 1024,
        "metric": "cosine"
      },
      "_sparse_values": {
        "type": "sparse_vector",
        "description": null
      }
    }
  },
  "tags": null,
  "deletion_protection": "disabled"
}
```

A legacy vector index always reports both reserved fields, `_values` for dense vectors and `_sparse_values` for sparse vectors, whether or not its records carry sparse values.

### 2. Start the conversion

Use the [Convert an index into a document index](/reference/api/2026-07/control-plane/convert_index) operation, passing the name of the new index and the schema you want it to have. The `embedding` field takes the source's dense vectors, and the `ticket_text` field is filled from the `ticket_text` metadata key on each record. `on_error` is set to `continue` so that a record with a malformed `ticket_text` value is skipped instead of failing the whole job.

```bash Request expandable theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl https://api.pinecone.io/indexes/support-tickets/convert \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07" \
     -d '{
           "name": "support-tickets-docs",
           "schema": {
             "fields": {
               "embedding": {
                 "type": "dense_vector",
                 "dimension": 1024,
                 "metric": "cosine"
               },
               "ticket_text": {
                 "type": "string",
                 "full_text_search": {
                   "language": "en"
                 }
               }
             }
           },
           "error_mode": {
             "on_error": "continue"
           }
         }'
```

```json Response theme={null}
{
  "conversion_job_id": "670e8400-e29b-41d4-a716-446655440001",
  "index_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

The request returns as soon as the new index is created in the `Initializing` state and the job is queued. You can also set `tags`, `deletion_protection`, and `read_capacity` on the new index in the same request. If you leave them out, the new index copies the source's tags, while deletion protection is disabled and read capacity is on-demand, whatever the source uses.

### 3. Track the conversion job

Pass the `conversion_job_id` from the previous step to the [Describe a conversion job](/reference/api/2026-07/control-plane/describe_conversion_job) operation to get the job's status and progress.

```bash Request theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
JOB_ID="670e8400-e29b-41d4-a716-446655440001"

curl -X GET "https://api.pinecone.io/conversion-jobs/$JOB_ID" \
     -H "Accept: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07"
```

```json Response expandable theme={null}
{
  "conversion_job_id": "670e8400-e29b-41d4-a716-446655440001",
  "source_index_name": "support-tickets",
  "source_index_id": "670e8400-e29b-41d4-a716-446655440000",
  "target_index_name": "support-tickets-docs",
  "target_index_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "InProgress",
  "error_mode": {
    "on_error": "continue"
  },
  "percent_complete": 42.5,
  "records_converted": 425000,
  "records_skipped": 3,
  "error": null,
  "created_at": "2026-10-07T10:30:00Z",
  "completed_at": null
}
```

A job is `Pending` until it starts, `InProgress` while it runs, and then `Completed`, `Failed`, or `Cancelled`. `percent_complete` is absent until the job starts, `completed_at` is `null` until it ends, and `error` is `null` unless the job fails.

### 4. Confirm the new index is ready

When the job reaches `Completed`, the new index moves from `Initializing` to `Ready`.

```bash Request theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X GET https://api.pinecone.io/indexes/support-tickets-docs \
     -H "Accept: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07"
```

```json Response expandable theme={null}
{
  "name": "support-tickets-docs",
  "host": "support-tickets-docs-govk0nt.svc.aped-4627-b74a.pinecone.io",
  "status": {
    "ready": true,
    "state": "Ready"
  },
  "deployment": {
    "deployment_type": "managed",
    "region": "us-east-1",
    "cloud": "aws",
    "environment": "aped-4627-b74a"
  },
  "read_capacity": {
    "mode": "OnDemand",
    "status": {
      "state": "Ready",
      "current_shards": null,
      "current_replicas": null
    }
  },
  "schema": {
    "fields": {
      "embedding": {
        "type": "dense_vector",
        "description": null,
        "dimension": 1024,
        "metric": "cosine"
      },
      "ticket_text": {
        "type": "string",
        "description": null,
        "full_text_search": {
          "language": "en",
          "stemming": false,
          "stop_words": false
        },
        "store_text": true
      }
    }
  },
  "tags": null,
  "deletion_protection": "disabled"
}
```

Each document carries the ID its record had, the vector in `embedding`, the ticket text in `ticket_text`, and `product` and `priority` as filterable metadata. Read and write the index through the Documents API, where you can rank by BM25 on `ticket_text` with [full-text search](/guides/search/full-text-search) or by vector similarity on `embedding`, and filter on `product` and `priority` as before.

## Switch to the new index

The new index has its own name and host, and you read and write it through the [Documents API](/guides/get-started/documents-api), so your application's write and search calls change. Until the new index is `Ready`, it rejects reads and writes with a `401` and the message `Not ready`.

### 1. Replay writes made during the conversion

The new index holds the source as it stood when the job started, so upserts and deletes sent to the source after your request might not be in it. Either pause writes to the source until you switch, or log them and replay them to the new index once it's `Ready`.

A replayed upsert is a document. The record's ID goes in `_id`, its vector goes in the dense field, and its metadata keys become top-level fields. An upsert replaces the whole document, so send every field, not only the ones that changed.

```bash Upsert theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="support-tickets-docs-govk0nt.svc.aped-4627-b74a.pinecone.io"
VECTOR="[0.12, 0.45, 0.33, 0.81]"  # The record's 1024-dimension vector

curl "https://$INDEX_HOST/namespaces/__default__/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "documents": [
          {
            "_id": "ticket-1742",
            "embedding": '"$VECTOR"',
            "ticket_text": "Refund not applied after plan downgrade",
            "product": "billing",
            "priority": "high"
          }
        ]
      }'
```

```bash Delete theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="support-tickets-docs-govk0nt.svc.aped-4627-b74a.pinecone.io"

curl "https://$INDEX_HOST/namespaces/__default__/documents/delete" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "ids": ["ticket-1733"]
      }'
```

### 2. Point your searches at the new index

Send searches to the new index's host, which the describe response in [Confirm the new index is ready](#confirm-the-new-index-is-ready) returns. A legacy Vectors API query by vector becomes a `dense_vector` clause on `embedding` in `score_by`. The `filter` carries over unchanged, and `include_fields` names the fields to return.

```bash Request theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="support-tickets-docs-govk0nt.svc.aped-4627-b74a.pinecone.io"
QUERY_VECTOR="[0.12, 0.45, 0.33, 0.81]"  # A 1024-dimension query vector

curl "https://$INDEX_HOST/namespaces/__default__/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "score_by": [
          {
            "type": "dense_vector",
            "fields": ["embedding"],
            "values": '"$QUERY_VECTOR"'
          }
        ],
        "filter": {"product": {"$eq": "billing"}},
        "include_fields": ["ticket_text", "priority"],
        "top_k": 5
      }'
```

```json Response theme={null}
{
  "matches": [
    {
      "_id": "ticket-1742",
      "_score": 0.92,
      "ticket_text": "Refund not applied after plan downgrade",
      "priority": "high"
    }
  ],
  "namespace": "__default__",
  "usage": {
    "read_units": 1
  }
}
```

Matches come back with `_id` and `_score` in place of `id` and `score`. To rank by keywords in `ticket_text` instead, see [Full-text search](/guides/search/full-text-search). Confirm the new index returns the results you expect before you move on.

### 3. Delete the source index

When you no longer need the source, [delete it](/guides/indexes/manage-indexes#delete-an-index). Don't delete it while a job is still reading it, because that fails the job. Deleting the source doesn't remove its completed conversion job.

## Manage conversion jobs

### List conversion jobs

The [List conversion jobs](/reference/api/2026-07/control-plane/list_conversion_jobs) operation returns the project's conversion jobs, newest first. Use this to find the job behind an index you don't recognize, or the earlier job that claimed a name you want.

```bash Request theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X GET "https://api.pinecone.io/conversion-jobs?limit=10" \
     -H "Accept: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07"
```

```json Response expandable theme={null}
{
  "data": [
    {
      "conversion_job_id": "670e8400-e29b-41d4-a716-446655440001",
      "source_index_name": "support-tickets",
      "source_index_id": "670e8400-e29b-41d4-a716-446655440000",
      "target_index_name": "support-tickets-docs",
      "target_index_id": "123e4567-e89b-12d3-a456-426614174000",
      "status": "Completed",
      "error_mode": {
        "on_error": "continue"
      },
      "percent_complete": 100,
      "records_converted": 1000000,
      "records_skipped": 3,
      "error": null,
      "created_at": "2026-10-07T10:30:00Z",
      "completed_at": "2026-10-07T11:05:00Z"
    }
  ],
  "pagination": {
    "next": "dXNlcl9pZD11c2VyXzE="
  }
}
```

To get the next page, pass the response's `pagination.next` token as the `paginationToken` query parameter.

### Cancel a conversion job

The [Cancel a conversion job](/reference/api/2026-07/control-plane/cancel_conversion_job) operation stops a job that's `Pending` or `InProgress` and leaves the index it was filling in the `InitializationFailed` state.

```bash Request theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
JOB_ID="670e8400-e29b-41d4-a716-446655440001"

curl -X POST "https://api.pinecone.io/conversion-jobs/$JOB_ID/cancel" \
     -H "Accept: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07"
```

```json Response expandable theme={null}
{
  "conversion_job_id": "670e8400-e29b-41d4-a716-446655440001",
  "source_index_name": "support-tickets",
  "source_index_id": "670e8400-e29b-41d4-a716-446655440000",
  "target_index_name": "support-tickets-docs",
  "target_index_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "Cancelled",
  "error_mode": {
    "on_error": "continue"
  },
  "percent_complete": 42.5,
  "records_converted": 425000,
  "records_skipped": 3,
  "error": null,
  "created_at": "2026-10-07T10:30:00Z",
  "completed_at": "2026-10-07T10:48:00Z"
}
```

The response is the job as it stands after the request, so canceling a job that has already ended changes nothing and returns the job as it was. To reuse the index's name, see [Troubleshooting](#troubleshooting).

## Troubleshooting

A job that fails or is canceled leaves its index in the `InitializationFailed` state. The index holds no usable data and keeps its name, so [delete it](/guides/indexes/manage-indexes#delete-an-index) before you convert into that name again.

When a job fails because of your data, `error` says what went wrong. With the default `on_error` of `abort`, it names the record the new index couldn't take and the reason, as in this trimmed job. A job that fails because of an internal error leaves `error` as `null`.

```json theme={null}
{
  "conversion_job_id": "670e8400-e29b-41d4-a716-446655440001",
  "status": "Failed",
  "error": "Record with id 'ticket-1742': metadata field `ticket_text` must be a string to fill the full-text field of that name"
}
```

Fix the schema so it can hold that record, or set `on_error` to `continue` to skip records like it, then start a new conversion. With `continue`, a job that skips every record in a namespace still fails, because nothing was written to the new index.

A job also fails when the source has no indexed records. New writes can take a few minutes to be indexed for conversion, even after queries return them, so if you wrote to the source just before converting, wait, delete the new index, and start the conversion again.

These errors are returned when you start a conversion, before a job exists:

| Status | Cause | Fix |
| - | - | - |
| `400` | The source is pod-based, BYOC, a text index, or already has a document schema, or the new index has the source's name | The message names the problem |
| `400` | The schema can't hold the source's vectors, or `on_error` isn't `abort` or `continue`. For example, a vector field is missing or doubled, a sparse index's schema has a dense field, a dimension, metric, or embedding doesn't match the source, or the schema has only `_values` and `_sparse_values` | The message names the problem and the value to use |
| `403` | The organization is on the Starter or Builder plan, the API key can't create indexes, or the project's index quota is exhausted | Upgrade to Standard or Enterprise, use a key with `control::index::create`, or raise the quota |
| `404` | The source index doesn't exist | Check the index name in the request path |
| `409` | An index with that name already exists, possibly from an earlier conversion | Choose another name, or [list conversion jobs](#list-conversion-jobs) to find the earlier job |
| `412` | The source index isn't `Ready`, for example because it's being deleted, has failed, or is disabled | Wait until it's `Ready`, then retry. The message says what state the source is in |
