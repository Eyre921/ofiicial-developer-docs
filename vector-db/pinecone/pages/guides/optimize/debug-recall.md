---
title: "Diagnose poor search results"
source: https://docs.pinecone.io/guides/optimize/debug-recall
path: guides/optimize/debug-recall
---

Find out whether poor search results come from your embedding model or from Pinecone recall by comparing exact brute-force search with your index's results.

Poor search results have one of two causes: the embedding model doesn't place relevant records near your queries, or the index doesn't return the true nearest neighbors (low recall). Comparing exact brute-force search with your index's results tells you which one.

**1. Build an evaluation set**

Choose at least 10 queries and a source dataset that resembles your production data, for example 100,000 records. For each query, label the records in the source dataset that are correct answers. Then choose an evaluation metric that fits your use case. For guidance, see [Evaluation measures in information retrieval](https://www.pinecone.io/learn/offline-evaluation/).

**2. Generate embeddings**

Use your model to embed the queries and the source dataset.

**3. Measure model quality with brute-force search**

Run an exact nearest-neighbor search for each query vector over the source vectors, for example with FAISS or NumPy, using the same similarity metric your index will use, and record the returned record IDs. Score the results against your labeled answers. If the score is too low, the problem is the model, not Pinecone.

**4. Query your index**

[Create an index](/guides/index-data/create-an-index) whose dimension and metric match your model and the brute-force search. [Upsert](/guides/index-data/upsert-data) the source vectors, run the same queries with the same `top_k`, and record the returned record IDs.

**5. Calculate recall**

For each query, recall is the fraction of the brute-force record IDs that Pinecone also returned. Average across all queries to get overall recall.

If your index uses dedicated read nodes, query-time parameters trade recall for latency. See [Tune queries](/guides/index-data/dedicated-read-nodes/tune-queries).

**6. Report low recall**

If recall is too low for your use case, [contact support](/admin/support/contact-support) with the dataset and queries that reproduce the issue.
