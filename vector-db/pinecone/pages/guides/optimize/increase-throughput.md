---
title: "Increase throughput"
source: https://docs.pinecone.io/guides/optimize/increase-throughput
path: guides/optimize/increase-throughput
---

Increase Pinecone throughput with bulk import, batch upserts, parallel upserts and searches, and Python SDK options like async requests and gRPC.

## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective way to load large numbers of documents or records into an index. You store your data in object storage as [JSON Lines](https://jsonlines.org/) (JSONL) files for a document index or Parquet files for a vector index. Then you integrate your object storage with Pinecone and start an asynchronous, long-running operation that imports and indexes your data. You can't import into an index whose schema declares `embed` or `sparse_embed`, so upsert in batches instead.

## Upsert in batches

[Upserting in batches](/guides/index-data/upsert-data#upsert-in-batches) is another efficient way to ingest large numbers of documents or records. A batch can hold up to 1,000 documents or records, or 96 when Pinecone embeds the text. See [Upsert limits](/reference/api/database-limits/operation-limits#upsert-limits). Batch upserting is also a good option if you can't work around bulk import's [limitations](/guides/index-data/import-data#import-limits).

For a document index, the Python SDK's `index.documents.batch_upsert` method splits a list of documents into batches and sends them in parallel. Failed batches are returned in the result instead of raised, so you can retry only the failures. For example, the following code upserts 1,000 documents into an index whose `chunk_text` field declares `embed`, then resends any batches a retry could help:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

documents = [{"_id": f"doc{i}", "chunk_text": f"Paragraph {i}"} for i in range(1000)]

result = index.documents.batch_upsert(namespace="example-namespace", documents=documents)

retryable = [item for error in result.errors if error.retryable for item in error.items]
if retryable:
    index.documents.batch_upsert(namespace="example-namespace", documents=retryable)
```

## Upsert and search in parallel

Pinecone is thread-safe, so you can send multiple [upsert](/guides/index-data/upsert-data#upsert-in-parallel) requests and multiple [search](#parallel-queries) requests in parallel to help increase throughput.

### Parallel queries

Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Asyncio support makes it possible to use Pinecone with async web frameworks such as FastAPI, Quart, and Sanic, and can make running queries in parallel much more efficient. For details, see [Async requests](/reference/sdks/python/overview#async-requests).

You can also run synchronous queries in parallel with a thread pool. For example, the following code runs three text searches concurrently against a document index whose `chunk_text` field declares `embed`:

```python Python theme={null}
from concurrent.futures import ThreadPoolExecutor
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.index(host="INDEX_HOST")

queries = ["Disease prevention", "Healthy digestion", "Immune support"]

def run_query(query):
    return index.documents.search(
        namespace="example-namespace",
        top_k=3,
        score_by=[{"type": "embed", "fields": ["chunk_text"], "query": query}],
        include_fields=["chunk_text"],
    )

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(run_query, queries))

for query, result in zip(queries, results):
    print(query, [match._id for match in result.matches])
```

On a vector index, run `index.query` with query vectors instead, using the same client and thread pool:

```python Python theme={null}
def run_query(vector):
    return index.query(namespace="example-namespace", vector=vector, top_k=3)

# Replace with your query embeddings, which must match the index's dimension (1536 in this example)
query_vectors = [
    [0.1, 0.2] * 768,
    [0.2, 0.1] * 768,
]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(run_query, query_vectors))
```

## Python SDK options

### Use gRPC

For a vector index, use the [Python SDK with gRPC](/reference/sdks/python/overview) to run data operations such as upserts and queries over [gRPC](https://grpc.io/) rather than HTTP for a modest performance improvement. The gRPC client doesn't support the Documents API, so use the sync or async client for a document index.

### Upsert from a dataframe

To quickly ingest data into a vector index with the Python SDK, use the [`upsert_from_dataframe` method](/reference/sdks/python/overview#upsert-from-a-dataframe). The method includes retry logic and `batch_size`, and performs especially well with Parquet datasets.
