---
title: "Fetch data"
source: https://docs.pinecone.io/guides/data/fetch-data
path: guides/data/fetch-data
---

Retrieve Pinecone documents from a namespace in a document index by ID or metadata filter to inspect their fields and metadata.

This page shows you how to fetch documents by ID or by metadata filter from a [namespace](/guides/indexes/index-data-overview#namespaces) in a document index. For a legacy vector index, see [Fetch vectors](/guides/legacy/vectors-api/fetch-vectors).

You can also fetch data in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser).

> [!TIP]
>
> Fetches consume [read units (RUs)](/guides/cost/understand-cost#read-units). See [Understand Pinecone cost](/guides/cost/understand-cost#fetch) for how fetch cost is calculated.

## Fetch documents

In an index with a document schema, fetch documents by ID or by metadata filter. A request specifies exactly one of `ids` or `filter`, and can name up to 1,000 IDs. `include_fields` selects which fields come back, and omitting it returns all of them.

### Fetch documents by ID

To fetch specific documents, pass their IDs:

```Python Python theme={null}
# pip install --upgrade pinecone
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

response = index.documents.fetch(
    namespace="articles",
    ids=["doc-1", "doc-2"],
    include_fields=["title", "body"],
)
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/articles/documents/fetch" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "ids": ["doc-1", "doc-2"],
            "include_fields": ["title", "body"]
        }'
```

The response keys each document by its ID:

```json theme={null}
{
    "documents": {
        "doc-1": { "_id": "doc-1", "title": "First", "body": "First body text." },
        "doc-2": { "_id": "doc-2", "title": "Second", "body": "Second body text." }
    },
    "namespace": "articles",
    "usage": { "read_units": 1, "egress_bytes": 98 }
}
```

### Fetch documents by metadata

To fetch every document matching a [metadata filter expression](/guides/indexes/index-data-overview#metadata-filter-expressions), pass a `filter` instead of `ids`:

```Python Python theme={null}
# Connect to an index as shown above.
response = index.documents.fetch(
    namespace="articles",
    filter={"category": {"$eq": "news"}},
    include_fields=["*"],
)
```

```bash curl theme={null}
curl "https://$INDEX_HOST/namespaces/articles/documents/fetch" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "filter": { "category": { "$eq": "news" } },
            "include_fields": ["*"]
        }'
```

A filtered fetch returns one page at a time, holding 100 documents by default and 10,000 at most. When more documents match, the response carries a `pagination.next` token. Pass it back as `pagination_token` to get the next page, and stop when the response has no `pagination` token. In the REST API, `limit` sets the page size.

Unlike a filtered update or delete, a filtered fetch accepts the [text-match operators](/guides/search/filter-by-metadata#text-match-filters) `$match_phrase`, `$match_all`, and `$match_any` on full-text fields, so you can fetch documents by their text without running a search.

For the full request and response schema, see [Fetch documents](/reference/api/latest/data-plane/fetch_documents).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed documents are visible to queries. You can view index stats to [check data freshness](/guides/data/check-data-freshness).
