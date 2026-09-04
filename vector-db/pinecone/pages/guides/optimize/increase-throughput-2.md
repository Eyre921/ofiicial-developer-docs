---
title: "Increase throughput"
source: https://docs.pinecone.io/guides/optimize/increase-throughput
path: guides/optimize/increase-throughput
---

Increase Pinecone throughput with bulk import from object storage, batch upserts, parallel requests, and the Python gRPC SDK for faster ingestion.

## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

## Upsert in batches

[Upserting in batches](/guides/index-data/upsert-data#upsert-in-batches) is another efficient way to ingest large numbers of records (up to 1000 per batch). Batch upserting is also a good option if you cannot work around bulk import's current [limitations](/guides/index-data/import-data#import-limits).

## Upsert/search in parallel

Pinecone is thread-safe, so you can send multiple [upsert](/guides/index-data/upsert-data#upsert-in-parallel) requests and multiple [query](/guides/search/semantic-search#parallel-queries) requests in parallel to help increase throughput.

## Python SDK options

### Use gRPC

Use the [Python SDK with gRPC extras](/reference/sdks/python/overview) to run data operations such as upserts and queries over [gRPC](https://grpc.io/) rather than HTTP for a modest performance improvement.

### Upsert from a dataframe

To quickly ingest data when using the Python SDK, use the [`upsert_from_dataframe` method](/reference/sdks/python/overview#upsert-from-a-dataframe). The method includes retry logic and `batch_size`, and is performant especially with Parquet file data sets.

## See also

Read more about [high-throughput optimizations](https://www.pinecone.io/blog/working-at-scale/) on our blog.
