---
title: "Increase throughput"
source: https://docs.pinecone.io/guides/optimize/increase-throughput
path: guides/optimize/increase-throughput
---

Increase Pinecone throughput with bulk import from object storage, batch upserts, parallel requests, and the Python gRPC SDK for faster ingestion.

## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

## Upsert in batches

[Upserting in batches](/guides/index-data/upsert-data#upsert-in-batches) is another efficient way to ingest large numbers of records (up to 1000 per batch). Batch upserting is also a good option if you can't work around bulk import's current [limitations](/guides/index-data/import-data#import-limits).

## Upsert/search in parallel

Pinecone is thread-safe, so you can send multiple [upsert](/guides/index-data/upsert-data#upsert-in-parallel) requests and multiple [query](#parallel-queries) requests in parallel to help increase throughput.

### Parallel queries

Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Async support makes it possible to use Pinecone with modern async web frameworks such as FastAPI, Quart, and Sanic, and can significantly increase the efficiency of running queries in parallel. For details, see [Async requests](/reference/sdks/python/overview#async-requests).

Alternatively, you can run multi-threaded, synchronous queries in parallel. For example, the following code uses a thread pool to run multiple queries concurrently. This example assumes a 1536-dimension serverless vector index named `docs-example`, and that you've installed the [Pinecone Python SDK](/reference/sdks/python/overview) and [`numpy`](https://numpy.org/). [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) is part of the Python standard library.

```python Python theme={null}
import os
from pinecone import Pinecone
from concurrent.futures import ThreadPoolExecutor

# Get the API key from the environment variable and initialize Pinecone
api_key = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)

# Define the index name
index_name = "docs-example"

# Define the index
index = pc.Index(index_name)

# Define the function to run parallel queries
def run_parallel_queries(vectors):
    """
    Run a list of vectors in parallel using ThreadPoolExecutor.
    
    Parameters:
    vectors (list): A list of vectors.
    
    Returns:
    list: A list of query results.
    """
    
    # Define the maximum number of concurrent queries
    MAX_CONCURRENT_QUERIES = 4

    def run_query(vector):
        """
        Run a single query.
        """
        return index.query(
            namespace="example-namespace",
            vector=vector,
            top_k=3,
            include_values=True
        )
    
    # Run the queries in parallel
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_QUERIES) as executor:
        results = list(executor.map(run_query, vectors))
    
    return results

def test_parallel_queries():
    """
    Test the run_parallel_queries function with 20 random vectors.
    """
    import numpy as np

    # Generate 20 random vectors of size 1536 and convert them to lists
    vectors = [np.random.rand(1536).tolist() for _ in range(20)]

    # Run the parallel queries
    results = run_parallel_queries(vectors)

    # Print the results
    for i, result in enumerate(results):
        print(f"Query {i+1} results: {result}")

if __name__ == "__main__":
    test_parallel_queries()
```

## Python SDK options

### Use gRPC

Use the [Python SDK with gRPC](/reference/sdks/python/overview) to run data operations such as upserts and queries over [gRPC](https://grpc.io/) rather than HTTP for a modest performance improvement.

### Upsert from a dataframe

To quickly ingest data when using the Python SDK, use the [`upsert_from_dataframe` method](/reference/sdks/python/overview#upsert-from-a-dataframe). The method includes retry logic and `batch_size`, and is performant especially with Parquet file data sets.

## See also

Read more about [high-throughput optimizations](https://www.pinecone.io/blog/working-at-scale/) on our blog.
