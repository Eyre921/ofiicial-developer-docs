---
title: "Operation limits"
source: https://docs.pinecone.io/reference/api/database-limits/operation-limits
path: reference/api/database-limits/operation-limits
---

Fixed limits on Pinecone Database operations, including upsert, import, query, fetch, and delete batch sizes and metadata filter expressions.

Operation limits are restrictions on the size, number, or other characteristics of operations in Pinecone. Operation limits are fixed and don't vary based on pricing plan.

If one of these limits is blocking you, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case. There's often a workaround.

## Upsert limits

| Metric                                                                                      | Limit                           |
| :------------------------------------------------------------------------------------------ | :------------------------------ |
| Max [batch size](/guides/index-data/upsert-data#upsert-in-batches) for records with vectors | 1,000 records, up to 2 MB total |
| Max batch size for records with text                                                        | 96 records                      |
| Max documents per upsert request                                                            | 1,000                           |
| Max document upsert request size                                                            | 2 MB                            |
| Max document size                                                                           | 2 MB                            |
| Max `full_text_search` string fields per schema                                             | 100                             |
| Max size per `full_text_search` string field                                                | 100 KB                          |
| Max tokens per `full_text_search` string field                                              | 10,000                          |
| Max bytes per token                                                                         | 256 bytes                       |
| Max filterable metadata size per document                                                   | 40 KB                           |
| Max length for a record ID                                                                  | 512 characters                  |
| Max dimensionality for dense vectors                                                        | 20,000                          |
| Max non-zero values for sparse vectors                                                      | 2048                            |
| Max dimensionality for sparse vectors                                                       | 4.2 billion                     |

The limit for text is lower because Pinecone converts that text to vectors at upsert time with [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding), and 96 is the max batch size of the [hosted embedding models](/guides/index-data/create-an-index#embedding-models) doing the conversion.

The 40 KB filterable metadata limit doesn't apply to `full_text_search` text fields.

## Import limits

<Note>
  If your import exceeds these limits, you'll get an error specifying the limit exceeded. See [Troubleshooting](/guides/index-data/import-data#troubleshooting) for details.
</Note>

| Metric                                        | Limit     |
| :-------------------------------------------- | :-------- |
| Max namespaces per import                     | 10,000    |
| Max total input data size (on-demand indexes) | 1 TB      |
| Max total input data size (DRN indexes)       | Unlimited |
| Max files per import                          | 100,000   |
| Max size per file                             | 10 GB     |

The total input data size limit does not apply to indexes with [dedicated read nodes](/guides/index-data/dedicated-read-nodes).

Bulk import supports indexes without a schema definition (Parquet files) and indexes with document schemas ([JSONL files](/guides/search/full-text-search#bulk-import)). Semantic-text (auto-embedded) fields are not yet supported in document schemas.

## Query limits

| Metric            | Limit  |
| :---------------- | :----- |
| Max `top_k` value | 10,000 |
| Max result size   | 4MB    |

The query result size is affected by the dimension of the dense vectors and whether or not dense vector values and metadata are included in the result.

<Tip>
  If a query fails due to exceeding the 4MB result size limit, choose a lower `top_k` value, or use `include_metadata=False` or `include_values=False` to exclude metadata or values from the result. For better performance, especially with higher `top_k` values, avoid including vector values unless you need them.
</Tip>

## Fetch limits

**Fetch by ID limits:**

| Metric                           | Limit |
| :------------------------------- | :---- |
| Max record IDs per fetch request | 1,000 |

**Fetch by metadata limits:**

| Metric                   | Limit                               |
| :----------------------- | :---------------------------------- |
| Max records per response | 10,000                              |
| Max response size        | 4 MB                                |
| Max request rate         | 5 requests per second per namespace |

To retrieve more than 10,000 matching records, paginate through results using the `paginationToken` parameter. See [Fetch records by metadata](/guides/manage-data/fetch-data#fetch-records-by-metadata).

## Delete limits

| Metric                            | Limit |
| :-------------------------------- | :---- |
| Max record IDs per delete request | 1,000 |

## Metadata filter limits

The following limits apply to [metadata filter expressions](/guides/search/filter-by-metadata#metadata-filter-expressions) used in query, delete, update, and fetch operations.

| Limit                                       | Value  | Description                                                                                                                                                                                                       |
| :------------------------------------------ | :----- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum values per `$in` or `$nin` operator | 10,000 | Each `$in` or `$nin` operator accepts up to 10,000 values in its array. This limit applies per operator. If you have multiple `$in` operators in a single filter, each is independently limited to 10,000 values. |

When you exceed this limit, the request returns a `400 - BAD_REQUEST` error.

### Rationale

Large `$in` operators can impact query performance and cost. Filters with thousands of values increase request payload size and end-to-end latency. Additionally, using large filters typically indicates a shared namespace architecture, which increases query costs. Queries scan the entire namespace regardless of filters.

### Alternative approaches

If you need to filter by more than 10,000 values, consider these alternatives:

* **Use namespaces for tenant isolation**: Instead of filtering by tenant IDs within a single namespace, create separate namespaces for each tenant or tenant group. This can also reduce query costs. See [Design for multi-tenancy](/guides/index-data/data-modeling#design-for-multi-tenancy).
* **Use broader access control groups**: Instead of filtering by individual user IDs, filter by organization, project, or role. This reduces the number of values in your `$in` filter. See [Design for multi-tenancy](/guides/index-data/data-modeling#use-access-control-groups-instead-of-individual-ids).
* **Post-filter client-side**: Retrieve a larger top K without filtering (for example, top 1000), then filter results client-side.
* **Run multiple queries**: Split your filter into multiple queries with smaller `$in` operators and combine the results client-side.

<Tip>
  To avoid hitting this limit in production, validate the size of your `$in` and `$nin` arrays in your application code before making the request to Pinecone.
</Tip>
