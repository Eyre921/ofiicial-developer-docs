---
title: "Data ingestion overview"
source: https://docs.pinecone.io/guides/index-data/data-ingestion-overview
path: guides/index-data/data-ingestion-overview
---

Compare data ingestion options in Pinecone: bulk import from object storage, upsert operations, and hosted embedding via the Inference API.

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Upsert

For ongoing ingestion into an index, either one record at a time or in batches, use the [upsert](/guides/index-data/upsert-data) operation. [Batch upserting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records if you cannot work around import's current [limitations](/guides/index-data/import-data#import-limits).

## When you only need embeddings

Import and upsert move vectors into Pinecone. For workflows where you only need vectors from hosted models (for example, to embed offline and upsert later), use the Inference API as follows:

You can call the [`embed` operation](/reference/api/latest/inference/generate-embeddings) through Pinecone Inference to turn text into vectors without writing to an index. That differs from [`upsert_records`](/reference/api/latest/data-plane/upsert_records) on an index with integrated embedding, where each request embeds and stores records in one step. To see how embedding consumption appears in billing and usage reports, see [Embedding tokens](/guides/manage-cost/monitor-usage-and-costs#embedding-tokens).

## Ingestion cost

* To understand how cost is calculated for imports, see [Import cost](/guides/manage-cost/understanding-cost#imports).
* To understand how cost is calculated for upserts, see [Write unit pricing](/guides/manage-cost/understanding-cost#write-units).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).
