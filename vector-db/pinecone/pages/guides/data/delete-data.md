---
title: "Delete data"
source: https://docs.pinecone.io/guides/data/delete-data
path: guides/data/delete-data
---

Delete Pinecone documents from a namespace in a document index by ID or metadata filter, or delete every document the namespace holds.

This page shows you how to delete documents by ID, by metadata filter, or all at once from a [namespace](/guides/indexes/indexing-overview#namespaces) in a document index. For a legacy vector index, see [Delete vectors](/guides/legacy/vectors-api/delete-vectors).

> [!TIP]
>
> Deletes consume [write units (WUs)](/guides/manage-cost/understanding-cost#write-units). See [Understand Pinecone cost](/guides/manage-cost/understanding-cost#delete) for how delete cost is calculated.

## Delete documents

In an index with a document schema, delete documents by ID, by metadata filter, or delete the whole namespace's contents. A request specifies exactly one of `ids`, `filter`, or `delete_all`, and can name up to 1,000 IDs.

### Delete documents by ID

To delete specific documents, pass their IDs:

```Python Python theme={null}
# pip install --upgrade pinecone
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.delete(namespace="articles", ids=["doc-1", "doc-2"])
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/articles/documents/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "ids": ["doc-1", "doc-2"]
        }'
```

### Delete documents by metadata

To delete every document matching a [metadata filter expression](/guides/indexes/indexing-overview#metadata-filter-expressions), pass a `filter`. The response reports how many documents matched:

```Python Python theme={null}
# Connect to an index as shown above.
response = index.documents.delete(
    namespace="articles",
    filter={"category": {"$eq": "news"}},
)
print(response.matched_records)
```

```bash curl theme={null}
curl "https://$INDEX_HOST/namespaces/articles/documents/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "filter": { "category": { "$eq": "news" } }
        }'
```

```json theme={null}
{
    "matched_records": 6
}
```

### Delete all documents in a namespace

To empty a namespace without deleting the namespace itself, pass `delete_all`:

```Python Python theme={null}
# Connect to an index as shown above.
index.documents.delete(namespace="articles", delete_all=True)
```

```bash curl theme={null}
curl "https://$INDEX_HOST/namespaces/articles/documents/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "delete_all": true
        }'
```

A delete by ID and a `delete_all` return an empty response body. Only a filtered delete reports `matched_records`.

> [!NOTE]
>
> [Text-match operators](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) aren't supported in a filtered delete, and a request carrying one is rejected with a `400`. To delete documents by text match, [search](/guides/search/full-text-search) for them first and delete the IDs the search returns.

For the full request and response schema, see [Delete documents](/reference/api/latest/data-plane/delete_documents).

## Delete an entire namespace

To delete an entire namespace and all of its documents, see [Delete a namespace](/guides/data/manage-namespaces#delete-a-namespace).

## Delete an entire index

To remove all documents from an index, [delete the index](/guides/indexes/manage-indexes#delete-an-index) and [recreate it](/guides/indexes/create-an-index).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed documents are visible to queries. You can view index stats to [check data freshness](/guides/data/check-data-freshness).
