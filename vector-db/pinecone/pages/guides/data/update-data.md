---
title: "Update data"
source: https://docs.pinecone.io/guides/data/update-data
path: guides/data/update-data
---

Patch fields on Pinecone documents by ID, or update metadata fields across every document in a document index that matches a filter.

This page shows you how to update documents in a [namespace](/guides/indexes/indexing-overview#namespaces) of a document index. You can patch fields on a document by ID, or patch metadata fields across every document matching a filter. To replace whole documents, use the [upsert](/guides/data/upsert-data) operation instead. For a legacy vector index, see [Update vectors](/guides/legacy/vectors-api/update-vectors).

> [!TIP]
>
> Updates consume [write units (WUs)](/guides/manage-cost/understanding-cost#write-units). See [Understand Pinecone cost](/guides/manage-cost/understanding-cost#update) for how update cost is calculated.

## Update documents

In an index with a document schema, [upsert](/guides/data/upsert-data#upsert-documents) replaces the whole document for a given `_id`. To change individual fields instead, use the documents update operation, which leaves the fields you don't mention unchanged.

To patch specific documents, send one entry per `_id`. Include the fields you want to set, and name any fields to drop in `_remove_fields`. Both schema-declared fields and metadata fields can be set or removed this way:

```Python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.update(
    namespace="articles",
    documents=[
        {"_id": "doc1", "body": "Updated body text."},  # schema-declared field
        {"_id": "doc2", "_remove_fields": ["author"]},  # metadata field
    ],
)
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/articles/documents/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "documents": [
                { "_id": "doc1", "body": "Updated body text." },
                { "_id": "doc2", "_remove_fields": ["author"] }
            ]
        }'
```

To apply the same patch to every document matching a [metadata filter expression](/guides/indexes/indexing-overview#metadata-filter-expressions), send `filter` with `set_fields`, `remove_fields`, or both:

```Python Python theme={null}
# Connect to an index as shown above.
index.documents.update(
    namespace="articles",
    filter={"category": {"$eq": "news"}},
    set_fields={"status": "archived"},
    remove_fields=["author"],
)
```

```bash curl theme={null}
curl "https://$INDEX_HOST/namespaces/articles/documents/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "filter": { "category": { "$eq": "news" } },
            "set_fields": { "status": "archived" },
            "remove_fields": ["author"]
        }'
```

The response reports how many documents matched the filter:

```json theme={null}
{
    "matched_records": 2
}
```

For the full request and response schema, see [Update documents](/reference/api/latest/data-plane/update_documents).

### Limitations

* **By-ID requests**: Each request can patch up to 1,000 documents, or 96 when the schema declares `embed` or `sparse_embed` (even a metadata-only patch). See [Update limits](/reference/api/database-limits/operation-limits#update-limits).
* **By-filter requests**: `set_fields` and `remove_fields` both accept metadata fields only, and reject a field declared in the schema with a `400`. A by-filter update applies one value to every matched document, which would leave vector and full-text-searchable fields identical across the whole match set. To change a schema-declared field, patch each document by ID.
* **Text-match filters**: A by-filter update rejects [text-match operators](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) with a `400`. To update documents by text match, [search](/guides/search/full-text-search) for them first and patch the IDs the search returns.

> [!WARNING]
>
> This operation ignores the `dry_run` parameter that [Update by metadata](/guides/legacy/vectors-api/update-vectors#update-by-metadata) on the legacy Vectors API supports. A `dry_run` request returns `202` with a `matched_records` count and applies the update anyway. It also accepts unrecognized parameters rather than rejecting them, so check the parameter names before you send a request you can't undo.

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before updates are visible to queries. You can [use log sequence numbers](/guides/data/check-data-freshness#check-the-log-sequence-number) to check whether an update request has completed.

## See also

* [Replace a chunked document](/guides/data/manage-document-chunks#replace-a-chunked-document)
