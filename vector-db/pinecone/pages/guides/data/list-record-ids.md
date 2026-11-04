---
title: "List IDs"
source: https://docs.pinecone.io/guides/data/list-record-ids
path: guides/data/list-record-ids
---

List the IDs of Pinecone documents in a namespace of a document index, filter them by ID prefix, and paginate through the results.

This page shows you how to list the IDs in an index [namespace](/guides/indexes/indexing-overview#namespaces), either all of them or just those with a common ID prefix. Listing IDs without the data behind them is a cheap and fast way to check [upserts](/guides/data/upsert-data).

For a legacy vector index, see [List vector IDs](/guides/legacy/vectors-api/list-vector-ids).

> [!NOTE]
>
> The `list` endpoint is supported only for serverless indexes.

## List document IDs

In an index with a document schema, `list` returns document IDs in sorted order, 100 per page, which is also the maximum page size. Each entry carries only an `_id`. To get the fields of a document, [fetch](/guides/data/fetch-data#fetch-documents) it.

### List all document IDs

```Python Python theme={null}
# pip install --upgrade pinecone
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

for doc in index.documents.list(namespace="articles"):
    print(doc._id)
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/articles/documents/list" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "limit": 5
        }'
```

The response holds one entry per document, and a `pagination.next` token when more pages follow:

```json theme={null}
{
    "documents": [
        { "_id": "doc-00" },
        { "_id": "doc-01" },
        { "_id": "doc-02" },
        { "_id": "doc-03" },
        { "_id": "doc-04" }
    ],
    "namespace": "articles",
    "pagination": { "next": "Tm90aGluZyB0byBzZWUgaGVyZQo=" },
    "usage": { "read_units": 1 }
}
```

### List document IDs by prefix

To limit results to documents whose IDs start with a given string, pass a `prefix`. Combined with [structured IDs](/guides/indexes/data-modeling#use-structured-ids), this lets you list every chunk of a source document:

```Python Python theme={null}
# Connect to an index as shown above.
for doc in index.documents.list(namespace="articles", prefix="report-2026#"):
    print(doc._id)
```

```bash curl theme={null}
curl "https://$INDEX_HOST/namespaces/articles/documents/list" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "prefix": "report-2026#"
        }'
```

The Python SDK returns a paginator, so iterating it walks every page for you. In the REST API, a response with more results to follow carries a `pagination.next` token. Pass it back as `pagination_token` to get the next page, and stop when the response has no `pagination` token.

For the full request and response schema, see [List documents](/reference/api/latest/data-plane/list_documents).
