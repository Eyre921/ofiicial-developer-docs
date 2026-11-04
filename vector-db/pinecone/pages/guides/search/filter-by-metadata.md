---
title: "Filter by metadata"
source: https://docs.pinecone.io/guides/search/filter-by-metadata
path: guides/search/filter-by-metadata
---

Narrow Pinecone search results with metadata filter expressions such as $eq, $in, $gt, and $and, and with text-match filters on document indexes.

[Documents](/guides/core-concepts/key-terms#document) can carry [metadata](/guides/indexes/indexing-overview#metadata), key-value pairs that store related information. When you search, add a metadata filter to limit results to the documents that match it. Document indexes also support [text-match filters](#text-match-filters) on full-text fields.

For a legacy vector index, see [Query with a metadata filter](/guides/legacy/vectors-api/query-vectors#query-with-a-metadata-filter). For a legacy integrated index, see [Search with a metadata filter](/guides/legacy/records-api/search-with-text#search-with-a-metadata-filter).

## Search with a metadata filter

The following code searches for the 3 documents that are most semantically similar to a query and that have a `category` metadata field with the value `digestive system`.

On a document index with [integrated embedding](/guides/search/integrated-embedding), you search with query text, and Pinecone embeds it with the model declared on the field. This example assumes a `chunk_text` field declared with `embed`.

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

filtered_results = index.documents.search(
    namespace="example-namespace",
    top_k=3,
    score_by=[
        {"type": "embed", "fields": ["chunk_text"], "query": "Disease prevention"}
    ],
    filter={"category": {"$eq": "digestive system"}},
    include_fields=["category", "chunk_text"],
)

print(filtered_results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

const response = await index.documents.search({
  topK: 3,
  scoreBy: [
    { type: 'embed', fields: ['chunk_text'], query: 'Disease prevention' },
  ],
  filter: { category: { $eq: 'digestive system' } },
  includeFields: ['category', 'chunk_text'],
});

console.log(response);
```

```go Go theme={null}
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func prettifyStruct(obj interface{}) string {
	bytes, _ := json.MarshalIndent(obj, "", "  ")
	return string(bytes)
}

func main() {
	ctx := context.Background()

	pc, err := pinecone.NewClient(pinecone.NewClientParams{
		ApiKey: "YOUR_API_KEY",
	})
	if err != nil {
		log.Fatalf("Failed to create Client: %v", err)
	}

	// To get the unique host for an index,
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	query := "Disease prevention"
	res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
		TopK: 3,
		ScoreBy: []pinecone.DocumentScoringMethod{
			{Type: pinecone.DocumentScoringTypeEmbed, Fields: []string{"chunk_text"}, Query: &query},
		},
		Filter: map[string]interface{}{
			"category": map[string]interface{}{"$eq": "digestive system"},
		},
		IncludeFields: []string{"category", "chunk_text"},
	})
	if err != nil {
		log.Fatalf("Failed to search documents: %v", err)
	}
	fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
INDEX_HOST="INDEX_HOST"
NAMESPACE="example-namespace"
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://$INDEX_HOST/namespaces/$NAMESPACE/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 3,
    "score_by": [
      { "type": "embed", "fields": ["chunk_text"], "query": "Disease prevention" }
    ],
    "filter": { "category": { "$eq": "digestive system" } },
    "include_fields": ["category", "chunk_text"]
  }'
```

## Metadata filter expressions

Pinecone's filtering language supports the following operators:

| Operator | Function | Supported types |
| :- | :- | :- |
| `$eq` | Matches records or documents with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}` | Number, string, boolean |
| `$ne` | Matches records or documents with metadata values that aren't equal to a specified value. Example: `{"genre": {"$ne": "drama"}}` | Number, string, boolean |
| `$gt` | Matches records or documents with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}` | Number |
| `$gte` | Matches records or documents with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}` | Number |
| `$lt` | Matches records or documents with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}` | Number |
| `$lte` | Matches records or documents with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}` | Number |
| `$in` | Matches records or documents with metadata values that are in a specified array. The array can hold up to [10,000 values](/reference/api/database-limits/operation-limits#metadata-filter-limits). Example: `{"genre": {"$in": ["comedy", "documentary"]}}` | String, number |
| `$nin` | Matches records or documents with metadata values that aren't in a specified array. The array can hold up to [10,000 values](/reference/api/database-limits/operation-limits#metadata-filter-limits). Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number |
| `$exists` | Matches records or documents with the specified metadata field. Example: `{"genre": {"$exists": true}}` | Number, string, boolean |
| `$and` | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}` | - |
| `$or` | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}` | - |
| `$not` | Matches records or documents that don't match the wrapped clause. Example: `{"genre": {"$not": {"$eq": "drama"}}}` | - |

At the top level, list one or more fields (combined with implicit AND) or combine clauses with the logical operators `$and` and `$or`. Use `$not` to negate a clause, as shown in the table. A bare comparison operator (like `$gt`) can't appear at the top level. Nest it under a field.

A metadata field can hold an array of strings, such as `{"genre": ["comedy", "documentary"]}`. A filter on that field matches when any value in the array satisfies it, so each of these filters matches:

```json JSON theme={null}
{"genre": "comedy"}
{"genre": {"$in": ["documentary", "action"]}}
{"$and": [{"genre": "comedy"}, {"genre": "documentary"}]}
```

These filters don't match, because the array has no `"drama"` value and because `$ne` and `$nin` exclude an item when any of its values matches:

```json JSON theme={null}
{"$and": [{"genre": "comedy"}, {"genre": "drama"}]}
{"genre": {"$ne": "comedy"}}
```

A filter value can't be an array. To match several values, use `$in`. These filters are invalid and return a `400` error:

```json JSON theme={null}
{"genre": ["comedy", "documentary"]}
{"genre": {"$eq": ["comedy", "documentary"]}}
```

## Text-match filters

On a [document index](/guides/indexes/data-modeling#documents), three more operators match text in `string` fields that have `full_text_search` enabled, or that declare `embed` or `sparse_embed` without setting `store_text: false`. Like metadata operators, they narrow the candidates before scoring.

| Operator | Example | Description |
| - | - | - |
| `$match_phrase` | `{"body": {"$match_phrase": "machine learning"}}` | Exact phrase match (contiguous tokens) on a text-searchable field. |
| `$match_all` | `{"body": {"$match_all": "machine learning"}}` | All tokens present, in any order. |
| `$match_any` | `{"body": {"$match_any": "AI robotics"}}` | At least one token present. |

Text-match operators use the field's tokenizer and stemmer, so a token that matches in BM25 scoring also matches in a filter. Filter values are literal text. Lucene syntax such as phrase slop (`"phrase"~N`), term boosting (`^N`), and phrase prefix (`"phrase pre"*`) isn't parsed. To use it, score with `query_string` instead.

You can combine text-match operators with metadata operators under `$and`, `$or`, and `$not`, at any nesting level:

```json theme={null}
{
  "$and": [
    { "body": { "$match_all": "federal reserve" } },
    { "category": { "$eq": "finance" } },
    { "year": { "$gte": 2024 } }
  ]
}
```

> [!WARNING]
>
> Text-match operators work on `documents/search` and [`documents/fetch`](/guides/data/fetch-data#fetch-documents). A filtered [`documents/update`](/guides/data/update-data#update-documents) or [`documents/delete`](/guides/data/delete-data#delete-documents) rejects them with a `400`. To update or delete by text match, first search or fetch to get the matching IDs, then update or delete by ID.
