---
title: "Filter by metadata"
source: https://docs.pinecone.io/guides/search/filter-by-metadata
path: guides/search/filter-by-metadata
---

Narrow Pinecone search results with metadata filter expressions such as $eq, $in, $gt, and $and, and with text-match filters on document indexes.

[Documents](/guides/core-concepts/key-terms#document) and [records](/guides/core-concepts/key-terms#record) can carry [metadata](/guides/index-data/indexing-overview#metadata), key-value pairs that store related information. When you search, add a metadata filter to limit results to the documents or records that match it. Document indexes also support [text-match filters](#text-match-filters) on full-text fields.

## Search with a metadata filter

The following code searches for the 3 documents or records that are most semantically similar to a query and that have a `category` metadata field with the value `digestive system`.

**Document index**

On a document index with [integrated embedding](/guides/search/integrated-embedding), you search with query text, and Pinecone embeds it with the model declared on the field. This example assumes a `chunk_text` field declared with `embed`.

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

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
// see https://docs.pinecone.io/guides/manage-data/target-an-index
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
	// see https://docs.pinecone.io/guides/manage-data/target-an-index
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

**Vector index**

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

index.query(
    namespace="example-namespace",
    vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
    top_k=3,
    filter={
        "category": {"$eq": "digestive system"}
    },
    include_metadata=True,
    include_values=False
)
```

```JavaScript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

const queryResponse = await index.namespace('example-namespace').query({
    vector: [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
    topK: 3,
    filter: {
        "category": { "$eq": "digestive system" }
    },
    includeValues: false,
    includeMetadata: true,
});
```

```java Java theme={null}
import com.google.protobuf.Struct;
import com.google.protobuf.Value;
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

import java.util.Arrays;
import java.util.List;

public class QueryExample {
    public static void main(String[] args) {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/manage-data/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
        List<Float> query = Arrays.asList(0.0236663818359375f, -0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f);
        Struct filter = Struct.newBuilder()
                .putFields("category", Value.newBuilder()
                        .setStructValue(Struct.newBuilder()
                                .putFields("$eq", Value.newBuilder()
                                        .setStringValue("digestive system")
                                        .build()))
                        .build())
                .build();

        QueryResponseWithUnsignedIndices queryResponse = index.query(3, query, null, null, null, "example-namespace", filter, false, true);
        System.out.println(queryResponse);
    }
}
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
    "google.golang.org/protobuf/types/known/structpb"
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
    // see https://docs.pinecone.io/guides/manage-data/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

    queryVector := []float32{0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875}

    metadataMap := map[string]interface{}{
        "category": map[string]interface{}{
            "$eq": "digestive system",
        },
    }

    metadataFilter, err := structpb.NewStruct(metadataMap)
    if err != nil {
        log.Fatalf("Failed to create metadata map: %v", err)
    }

    res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
        Vector:          queryVector,
        TopK:            3,
        MetadataFilter: metadataFilter,
        IncludeValues:   false,
        IncludeMetadata: true,
    })
    if err != nil {
        log.Fatalf("Error encountered when querying by vector: %v", err)
    } else {
        fmt.Printf(prettifyStruct(res))
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/query" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "vector": [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
        "namespace": "example-namespace",
        "topK": 3,
        "filter": {"category": {"$eq": "digestive system"}},
        "includeMetadata": true,
        "includeValues": false
    }'
```

**Legacy integrated index**

> [!NOTE]
>
> This example uses the legacy Records API, which works only with [legacy integrated indexes](/guides/index-data/create-an-index#integrated-embedding-legacy) created with `create_index_for_model`. For new projects, use a document index with [integrated embedding](/guides/search/integrated-embedding) instead, which you can combine with full-text search on the same field.

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

filtered_results = index.search(
    namespace="example-namespace", 
    query={
        "inputs": {"text": "Disease prevention"}, 
        "top_k": 3,
        "filter": {"category": "digestive system"},
    },
    fields=["category", "chunk_text"]
)

print(filtered_results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

const response = await namespace.searchRecords({
  query: {
    topK: 3,
    inputs: { text: "Disease prevention" },
    filter: { category: "digestive system" }
  },
  fields: ['chunk_text', 'category']
});

console.log(response);
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;
import org.openapitools.db_data.client.model.SearchRecordsResponse;

import java.util.*;

public class SearchText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/manage-data/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-dense-java");

        String query = "Disease prevention";
        List<String> fields = new ArrayList<>();
        fields.add("category");
        fields.add("chunk_text");

        Map<String, Object> filter = new HashMap<>();
        filter.put("category", "digestive system");

        // Search the index
        SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 3, filter, null);

        // Print the results
        System.out.println(recordsResponse);
    }
}
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
    // see https://docs.pinecone.io/guides/manage-data/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    } 

    metadataMap := map[string]interface{}{
        "category": map[string]interface{}{
            "$eq": "digestive system",
        },
    }
    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 3,
            Inputs: &map[string]interface{}{
                "text": "Disease prevention",
            },
            Filter: &metadataMap,
        },
        Fields: &[]string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Printf(prettifyStruct(res))
}
```

```shell curl theme={null}
INDEX_HOST="INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE"
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "query": {
            "inputs": {"text": "Disease prevention"},
            "top_k": 3,
            "filter": {"category": "digestive system"}
        },
        "fields": ["category", "chunk_text"]
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

On a [document index](/guides/index-data/data-modeling#documents), three more operators match text in `string` fields that have `full_text_search` enabled. Like metadata operators, they narrow the candidates before scoring.

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
> Text-match operators work on `documents/search` and [`documents/fetch`](/guides/manage-data/fetch-data#fetch-documents). A filtered [`documents/update`](/guides/manage-data/update-data#update-documents) or [`documents/delete`](/guides/manage-data/delete-data#delete-documents) rejects them with a `400`. To update or delete by text match, first search or fetch to get the matching IDs, then update or delete by ID.
