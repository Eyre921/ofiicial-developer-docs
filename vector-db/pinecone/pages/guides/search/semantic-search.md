---
title: "Semantic search"
source: https://docs.pinecone.io/guides/search/semantic-search
path: guides/search/semantic-search
---

Run semantic search in Pinecone over dense vectors in a document index or vector index, querying with a dense vector, a record ID, or text.

Semantic search finds the documents or records in an [index with dense vectors](/guides/index-data/indexing-overview#indexes-with-dense-vectors) that are most similar in meaning and context to a query. It's also called nearest neighbor search, similarity search, or vector search.

Semantic search uses [dense vectors](https://www.pinecone.io/learn/vector-embeddings/). Each number in a dense vector corresponds to a point in a multidimensional space. Vectors that are closer together in that space are semantically similar.

## Search a document index

In a [document index](/guides/index-data/data-modeling#documents), you choose how to score each search with a clause in `score_by`. Use an `embed` clause to search with text, or a `dense_vector` clause to search with a dense vector you generate yourself.

### Search with text

To search with text, the `string` field must declare `embed`, which enables [integrated embedding](/guides/search/integrated-embedding). Pinecone embeds your query text with the field's model. For example, this searches the `chunk_text` field of an index whose schema declares `"chunk_text": {"type": "string", "embed": {}}` and returns the 2 documents most semantically related to "Disease prevention":

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

results = index.documents.search(
    namespace="example-namespace",
    top_k=2,
    score_by=[
        {"type": "embed", "fields": ["chunk_text"], "query": "Disease prevention"}
    ],
    include_fields=["chunk_text", "category"],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: "INDEX_HOST", namespace: "example-namespace" })

const results = await index.documents.search({
  topK: 2,
  scoreBy: [
    { type: 'embed', fields: ['chunk_text'], query: 'Disease prevention' },
  ],
  includeFields: ['chunk_text', 'category'],
})

console.log(results)
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
        TopK: 2,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeEmbed, Fields: []string{"chunk_text"}, Query: &query},
        },
        IncludeFields: []string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/example-namespace/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "top_k": 2,
            "score_by": [
                {
                    "type": "embed",
                    "fields": ["chunk_text"],
                    "query": "Disease prevention"
                }
            ],
            "include_fields": ["chunk_text", "category"]
        }'
```

### Search with a dense vector

To search a `dense_vector` field, pass a `dense_vector` clause in `score_by` with the query's dense vector. Generate the query vector with the same embedding model you used at upsert. For example, this searches the `embedding` field of the [`articles-hybrid` schema](/guides/search/full-text-search#example-schemas), so the query vector must have 1536 dimensions:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

results = index.documents.search(
    namespace="articles",
    top_k=3,
    score_by=[
        {
            "type": "dense_vector",
            "fields": ["embedding"],
            "values": [0.0236663818359375, -0.032989501953125, ..., 0.0086669921875],
        }
    ],
    include_fields=["title"],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index({ host: "INDEX_HOST", namespace: "articles" })

const results = await index.documents.search({
  topK: 3,
  scoreBy: [
    { type: 'dense_vector', fields: ['embedding'], values: [0.0236663818359375, -0.032989501953125, ..., 0.0086669921875] },
  ],
  includeFields: ['title'],
})

console.log(results)
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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "articles"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    queryVector := []float32{0.0236663818359375, -0.032989501953125, ..., 0.0086669921875}
    res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
        TopK: 3,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeDenseVector, Fields: []string{"embedding"}, Values: &queryVector},
        },
        IncludeFields: []string{"title"},
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/articles/documents/search" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
            "top_k": 3,
            "score_by": [
                {
                    "type": "dense_vector",
                    "fields": ["embedding"],
                    "values": [0.0236663818359375, -0.032989501953125, ..., 0.0086669921875]
                }
            ],
            "include_fields": ["title"]
        }'
```

## Search a vector index

In a vector index, the query is either a dense vector or the ID of a record whose vector Pinecone uses as the query.

### Search with a dense vector

To search with a dense vector representation of a query, use the [Search with a vector](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `vector` parameter with the dense vector values representing your query.
* The `top_k` parameter with the number of results to return.
* Optionally, set `include_values`, `include_metadata`, or both to `true` to include the vector values, metadata, or both for the matching records in the response. For better performance, especially with higher `top_k` values, avoid including vector values unless you need them. See [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed) for more details.

For example, the following code uses a dense vector representation of the query "Disease prevention" to search for the 3 most semantically similar records in the `example-namespace` namespace:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

index.query(
    namespace="example-namespace",
    vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
    top_k=3,
    include_metadata=True,
    include_values=False
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

const queryResponse = await index.namespace('example-namespace').query({
    vector: [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
    topK: 3,
    includeValues: false,
    includeMetadata: true,
});
```

```java Java theme={null}
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
        Index index = new Index(connection, "INDEX_NAME");
        List<Float> query = Arrays.asList(0.0236663818359375f, -0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f);
        QueryResponseWithUnsignedIndices queryResponse = index.query(3, query, null, null, null, "example-namespace", null, false, true);
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

    res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
        Vector:          queryVector,
        TopK:            3,
        IncludeValues:   false,
        IncludeMetadata: true,
    })
    if err != nil {
        log.Fatalf("Error encountered when querying by vector: %v", err)
    } else {
        fmt.Println(prettifyStruct(res))
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
        "includeMetadata": true,
        "includeValues": false
    }'
```

In the response, each record has a similarity score that represents its distance to the query vector, calculated according to the index's [similarity metric](/guides/index-data/index-configuration#similarity-metrics):

```python Python theme={null}
{'matches': [{'id': 'rec3',
              'metadata': {'category': 'immune system',
                           'chunk_text': 'Rich in vitamin C and other '
                                          'antioxidants, apples contribute to '
                                          'immune health and may reduce the '
                                          'risk of chronic diseases.'},
              'score': 0.82026422,
              'values': []},
             {'id': 'rec1',
              'metadata': {'category': 'digestive system',
                           'chunk_text': 'Apples are a great source of '
                                          'dietary fiber, which supports '
                                          'digestion and helps maintain a '
                                          'healthy gut.'},
              'score': 0.793068111,
              'values': []},
             {'id': 'rec4',
              'metadata': {'category': 'endocrine system',
                           'chunk_text': 'The high fiber content in apples '
                                          'can also help regulate blood sugar '
                                          'levels, making them a favorable '
                                          'snack for people with diabetes.'},
              'score': 0.780169606,
              'values': []}],
 'namespace': 'example-namespace',
 'usage': {'read_units': 6}}
```

```javascript JavaScript theme={null}
{
  matches: [
    {
      id: 'rec3',
      score: 0.819709897,
      values: [],
      sparseValues: undefined,
      metadata: [Object]
    },
    {
      id: 'rec1',
      score: 0.792900264,
      values: [],
      sparseValues: undefined,
      metadata: [Object]
    },
    {
      id: 'rec4',
      score: 0.780068815,
      values: [],
      sparseValues: undefined,
      metadata: [Object]
    }
  ],
  namespace: 'example-namespace',
  usage: { readUnits: 6 }
}
```

```java Java theme={null}
class QueryResponseWithUnsignedIndices {
    matches: [ScoredVectorWithUnsignedIndices {
        score: 0.8197099
        id: rec3
        values: []
        metadata: fields {
          key: "category"
          value {
            string_value: "immune system"
          }
        }
        fields {
          key: "chunk_text"
          value {
            string_value: "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
          }
        }
        
        sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
            indicesWithUnsigned32Int: []
            values: []
        }
    }, ScoredVectorWithUnsignedIndices {
        score: 0.79290026
        id: rec1
        values: []
        metadata: fields {
          key: "category"
          value {
            string_value: "digestive system"
          }
        }
        fields {
          key: "chunk_text"
          value {
            string_value: "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
          }
        }
        
        sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
            indicesWithUnsigned32Int: []
            values: []
        }
    }, ScoredVectorWithUnsignedIndices {
        score: 0.7800688
        id: rec4
        values: []
        metadata: fields {
          key: "category"
          value {
            string_value: "endocrine system"
          }
        }
        fields {
          key: "chunk_text"
          value {
            string_value: "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
          }
        }
        
        sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
            indicesWithUnsigned32Int: []
            values: []
        }
    }]
    namespace: example-namespace
    usage: read_units: 6

}
```

```go Go theme={null}
{
  "matches": [
    {
      "vector": {
        "id": "rec3",
        "metadata": {
          "category": "immune system",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
        }
      },
      "score": 0.8197099
    },
    {
      "vector": {
        "id": "rec1",
        "metadata": {
          "category": "digestive system",
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
        }
      },
      "score": 0.79290026
    },
    {
      "vector": {
        "id": "rec4",
        "metadata": {
          "category": "endocrine system",
          "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
        }
      },
      "score": 0.7800688
    }
  ],
  "usage": {
    "read_units": 6
  },
  "namespace": "example-namespace"
}
```

```json curl theme={null}
{
    "results": [],
    "matches": [
        {
            "id": "rec3",
            "score": 0.820593238,
            "values": [],
            "metadata": {
                "category": "immune system",
                "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
            }
        },
        {
            "id": "rec1",
            "score": 0.792266726,
            "values": [],
            "metadata": {
                "category": "digestive system",
                "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
            }
        },
        {
            "id": "rec4",
            "score": 0.780045748,
            "values": [],
            "metadata": {
                "category": "endocrine system",
                "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
            }
        }
    ],
    "namespace": "example-namespace",
    "usage": {
        "readUnits": 6
    }
}
```

### Search with a record ID

When you search with a record ID, Pinecone uses the dense vector associated with the record as the query. Because search is approximate, the results aren't guaranteed to include that record, even with a high `top_k`. To retrieve a specific record, [fetch it by ID](/guides/manage-data/fetch-data#fetch-records-by-id). To search with a record ID, use the [Search with a vector](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `id` parameter with the unique record ID containing the vector to use as the query.
* The `top_k` parameter with the number of results to return.
* Optionally, set `include_values`, `include_metadata`, or both to `true` to include the vector values, metadata, or both for the matching records in the response. For better performance, especially with higher `top_k` values, avoid including vector values unless you need them. See [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed) for more details.

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that are most semantically similar to the dense vector in the record:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

index.query(
    namespace="example-namespace",
    id="rec2", 
    top_k=3,
    include_metadata=True,
    include_values=False
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

const queryResponse = await index.namespace('example-namespace').query({
    id: 'rec2',
    topK: 3,
    includeValues: false,
    includeMetadata: true,
});
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

public class QueryExample {
    public static void main(String[] args) {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/manage-data/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(connection, "INDEX_NAME");
        QueryResponseWithUnsignedIndices queryResponse = index.queryByVectorId(3, "rec2", "example-namespace", null, false, true);
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

    vectorId := "rec2"
    res, err := idxConnection.QueryByVectorId(ctx, &pinecone.QueryByVectorIdRequest{
        VectorId:      vectorId,
        TopK:          3,
        IncludeValues: false,
        IncludeMetadata: true,
    })
    if err != nil {
        log.Fatalf("Error encountered when querying by vector ID `%v`: %v", vectorId, err)
    } else {
        fmt.Println(prettifyStruct(res.Matches))
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
        "id": "rec2",
        "namespace": "example-namespace",
        "topK": 3,
        "includeMetadata": true,
        "includeValues": false
    }'
```

## Search a legacy integrated index

> [!NOTE]
>
> Legacy integrated indexes are created with `create_index_for_model` and searched through the legacy Records API. For new indexes, declare `embed` on a `string` field in a document index instead. See [Integrated embedding](/guides/search/integrated-embedding).

To search a legacy integrated index with query text, use the [Search with text](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `query.inputs.text` parameter with the query text. Pinecone uses the embedding model integrated with the index to convert the text to a dense vector automatically.
* The `query.top_k` parameter with the number of similar records to return.
* Optionally, the `fields` to return in the response. If you don't specify any, the response includes all fields.

For example, the following code searches for the 2 records most semantically related to the query text "Disease prevention":

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/manage-data/target-an-index
index = pc.Index(host="INDEX_HOST")

results = index.search(
    namespace="example-namespace", 
    query={
        "inputs": {"text": "Disease prevention"}, 
        "top_k": 2
    },
    fields=["category", "chunk_text"]
)

print(results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/manage-data/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

const response = await namespace.searchRecords({
  query: {
    topK: 2,
    inputs: { text: 'Disease prevention' },
  },
  fields: ['chunk_text', 'category'],
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

        // Search the index
        SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 2, null, null);

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

    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 2,
            Inputs: &map[string]interface{}{
                "text": "Disease prevention",
            },
        },
        Fields: &[]string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
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
            "top_k": 2
        },
        "fields": ["category", "chunk_text"]
     }'
```

In the response, each record has a similarity score that represents its distance to the query vector, calculated according to the index's [similarity metric](/guides/index-data/index-configuration#similarity-metrics):

```python Python theme={null}
{'result': {'hits': [{'_id': 'rec3',
                      '_score': 0.8204272389411926,
                      'fields': {'category': 'immune system',
                                 'chunk_text': 'Rich in vitamin C and other '
                                               'antioxidants, apples '
                                               'contribute to immune health '
                                               'and may reduce the risk of '
                                               'chronic diseases.'}},
                     {'_id': 'rec1',
                      '_score': 0.7931625843048096,
                      'fields': {'category': 'digestive system',
                                 'chunk_text': 'Apples are a great source of '
                                               'dietary fiber, which supports '
                                               'digestion and helps maintain a '
                                               'healthy gut.'}}]},
 'usage': {'embed_total_tokens': 8, 'read_units': 6}}
```

```javascript JavaScript theme={null}
{
  result: { 
    hits: [ 
      {
        _id: 'rec3',
        _score: 0.82042724,
        fields: {
          category: 'immune system',
          chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
        }
      },
      {
        _id: 'rec1',
        _score: 0.7931626,
        fields: {
          category: 'digestive system',
          chunk_text: 'Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.'
        }
      }
    ]
  },
  usage: { 
    readUnits: 6, 
    embedTotalTokens: 8 
  }
}
```

```java Java theme={null}
class SearchRecordsResponse {
    result: class SearchRecordsResponseResult {
        hits: [class Hit {
            id: rec3
            score: 0.8204272389411926
            fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
            additionalProperties: null
        }, class Hit {
            id: rec1
            score: 0.7931625843048096
            fields: {category=endocrine system, chunk_text=Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.}
            additionalProperties: null
        }]
        additionalProperties: null
    }
    usage: class SearchUsage {
        readUnits: 6
        embedTotalTokens: 13
    }
    additionalProperties: null
}
```

```go Go theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "rec3",
        "_score": 0.82042724,
        "fields": {
          "category": "immune system",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
        }
      },
      {
        "_id": "rec1",
        "_score": 0.7931626,
        "fields": {
          "category": "digestive system",
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
        }
      }
    ]
  },
  "usage": {
    "read_units": 6,
    "embed_total_tokens": 8
  }
}
```

```json curl theme={null}
 {
    "result": {
        "hits": [
            {
                "_id": "rec3",
                "_score": 0.82042724,
                "fields": {
                    "category": "immune system",
                    "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                }
            },
            {
                "_id": "rec1",
                "_score": 0.7931626,
                "fields": {
                    "category": "digestive system",
                    "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
                }
            }
        ]
    },
    "usage": {
        "embed_total_tokens": 8,
        "read_units": 6
    }
}
```
