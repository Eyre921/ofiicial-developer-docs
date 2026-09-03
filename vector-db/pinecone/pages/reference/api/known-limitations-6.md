---
title: "Known limitations"
source: https://docs.pinecone.io/reference/api/known-limitations
path: reference/api/known-limitations
---

Known limitations and feature restrictions for Pinecone indexes, including upsert consistency, metadata rules, and serverless caveats.

This page describes known limitations and feature restrictions in Pinecone.

## Upserts

* Pinecone is eventually consistent, so there can be a slight delay before [upserted records](/guides/index-data/upsert-data) are available to query. After upserting records, use the [`describe_index_stats`](/reference/api/latest/data-plane/describeindexstats) operation to check whether the current vector count matches the number of records you expect, although this method may not work for pod-based indexes with multiple replicas.
* Only indexes using the [dotproduct distance metric](/guides/index-data/indexing-overview#dotproduct) support querying sparse-dense vectors. Upserting, updating, and fetching sparse-dense vectors in indexes with a different distance metric will succeed, but querying will return an error.
* Indexes created before February 22, 2023 don't support sparse vectors.

## Metadata

* Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.
* Nested JSON objects aren't supported.

## Serverless indexes

Serverless indexes don't support the following features:

* [Filtering index statistics by metadata](/reference/api/latest/data-plane/describeindexstats)
* [Private endpoints](/guides/production/configure-private-endpoints)

  * This feature is available on AWS only.
