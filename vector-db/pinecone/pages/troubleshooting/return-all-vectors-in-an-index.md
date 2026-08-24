---
title: "Return all vectors in an index"
source: https://docs.pinecone.io/troubleshooting/return-all-vectors-in-an-index
path: troubleshooting/return-all-vectors-in-an-index
---

Learn why a single Pinecone query can't return every vector in an index, and how to page through record IDs with the list operation instead.

Pinecone is designed to find vectors that are similar to a given set of conditions, either by comparing a new vector to the ones in the index or by comparing a vector in the index to all of the others using the [query by ID feature](/reference/api/latest/data-plane/query). Because the Pinecone query function relies on performing this similarity search, there isn't a way to return all of the vectors currently stored in the index with a single query.

To work through every record in a serverless index instead, [list the record IDs](/guides/manage-data/list-record-ids) in a namespace and [fetch](/guides/manage-data/fetch-data) them in batches. For a static copy of a whole index rather than a query, [create a backup](/guides/manage-data/back-up-an-index).
