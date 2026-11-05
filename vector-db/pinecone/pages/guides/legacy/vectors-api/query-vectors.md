---
title: "Query a legacy vector index"
source: https://docs.pinecone.io/guides/legacy/vectors-api/query-vectors
path: guides/legacy/vectors-api/query-vectors
---

Query a legacy vector index with the legacy Vectors API, using a dense vector, a sparse vector, or a record ID, with optional metadata filters.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

This page shows you how to query a legacy vector index with the legacy Vectors API. For a document index, see [Semantic search](/guides/search/semantic-search), [Sparse-vector search](/guides/search/sparse-vector-search), and [Filter by metadata](/guides/search/filter-by-metadata).

## Query with dense vectors

In a legacy vector index, the query is either a dense vector or the ID of a record whose vector Pinecone uses as the query.

### Query with a dense vector

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
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# Replace with your query embedding, which must match the index's dimension (1536 in this example)
query_vector = [0.1] * 1536

index.query(
    namespace="example-namespace",
    vector=query_vector,
    top_k=3,
    include_metadata=True,
    include_values=False
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

// Replace with your query embedding, which must match the index's dimension (1536 in this example)
const queryVector = new Array(1536).fill(0.1);

const queryResponse = await index.namespace('example-namespace').query({
    vector: queryVector,
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

import java.util.Collections;
import java.util.List;

public class QueryExample {
    public static void main(String[] args) {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
        // Replace with your query embedding, which must match the index's dimension (1536 in this example)
        List<Float> query = Collections.nCopies(1536, 0.1f);
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

    // Replace with your query embedding, which must match the index's dimension (1536 in this example)
    queryVector := make([]float32, 1536)
    for i := range queryVector {
        queryVector[i] = 0.1
    }

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
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

# Stand-in built with jq. Replace with your query embedding, which must match the index's dimension (1536 in this example)
QUERY_VECTOR=$(jq -nc '[range(1536) | 0.1]')

curl "https://$INDEX_HOST/query" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "vector": '"$QUERY_VECTOR"',
        "namespace": "example-namespace",
        "topK": 3,
        "includeMetadata": true,
        "includeValues": false
    }'
```

In the response, each record has a similarity score that represents its distance to the query vector, calculated according to the index's [similarity metric](/guides/indexes/index-configuration#similarity-metrics):

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

### Query with a record ID

When you search with a record ID, Pinecone uses the dense vector associated with the record as the query. Because search is approximate, the results aren't guaranteed to include that record, even with a high `top_k`. To retrieve a specific record, [fetch it by ID](/guides/legacy/vectors-api/fetch-vectors#fetch-records-by-id). To search with a record ID, use the [Search with a vector](/reference/api/latest/data-plane/query) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `id` parameter with the unique record ID containing the vector to use as the query.
* The `top_k` parameter with the number of results to return.
* Optionally, set `include_values`, `include_metadata`, or both to `true` to include the vector values, metadata, or both for the matching records in the response. For better performance, especially with higher `top_k` values, avoid including vector values unless you need them. See [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed) for more details.

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that are most semantically similar to the dense vector in the record:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

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
// see https://docs.pinecone.io/guides/indexes/target-an-index
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
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
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
# see https://docs.pinecone.io/guides/indexes/target-an-index
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

## Query with sparse vectors

In a legacy vector index, the query is either a sparse vector or the ID of a record whose sparse vector Pinecone uses as the query.

### Query with a sparse vector

To search an index of sparse vectors with a sparse vector representation of a query, use the [Search with a vector](/reference/api/latest/data-plane/query) operation with the following parameters:

* `namespace`: The [namespace](/guides/indexes/index-data-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `sparse_vector`: The sparse vector values and indices.
* `top_k`: The number of results to return.
* `include_values`: Whether to include the vector values of the matching records in the response. Defaults to `false`.
* `include_metadata`: Whether to include the metadata of the matching records in the response. Defaults to `false`.

> [!NOTE]
>
> When querying with `top_k` over 1000, for optimal performance set `include_values=false` and `include_metadata=false` to return only IDs and scores.
>
> Since vectors values are retrieved from object storage, include them in your query results only when you need them (especially with higher `top_k` values). For details, see [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed).

For example, the following code uses a sparse vector representation of the query "What is AAPL's outlook, considering both product launches and market conditions?" to search for the 3 most similar vectors in the `example-namespace` namespace:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

results = index.query(
    namespace="example-namespace",
    sparse_vector={
      "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
    }, 
    top_k=3,
    include_metadata=True,
    include_values=False
)

print(results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

const queryResponse = await index.namespace('example-namespace').query({
    sparseVector: {
        indices: [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697],
        values: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    },
    topK: 3,
    includeValues: false,
    includeMetadata: true
});

console.log(queryResponse);
```

```java Java theme={null}
import io.pinecone.clients.Pinecone;
import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;
import io.pinecone.clients.Index;

import java.util.*;

public class SearchSparseIndex {
    public static void main(String[] args) throws InterruptedException {
        // Instantiate Pinecone class
        Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

        String indexName = "docs-example";

        Index index = pinecone.getIndexConnection(indexName);

        List<Long> sparseIndices = Arrays.asList(
                767227209L, 1640781426L, 1690623792L, 2021799277L, 2152645940L,
                2295025838L, 2443437770L, 2779594451L, 2956155693L, 3476647774L,
                3818127854L, 4283091697L);
        List<Float> sparseValues = Arrays.asList(
                1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
                1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f);

        QueryResponseWithUnsignedIndices queryResponse = index.query(3, null, sparseIndices, sparseValues, null, "example-namespace", null, false, true);
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	sparseValues := pinecone.SparseValues{
		Indices: []uint32{767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697},
		Values:  []float32{1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0},
	}

	res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
		SparseValues:    &sparseValues,
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

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/query" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "sparseVector": {
            "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
        },
        "namespace": "example-namespace",
        "topK": 3,
        "includeMetadata": true,
        "includeValues": false
    }'
```

The results look like this. The most similar records are scored highest.

```python Python theme={null}
{'matches': [{'id': 'vec2',
              'metadata': {'category': 'technology',
                           'quarter': 'Q4',
                           'chunk_text': "Analysts suggest that AAPL'''s "
                                          'upcoming Q4 product launch event '
                                          'might solidify its position in the '
                                          'premium smartphone market.'},
              'score': 10.9042969,
              'values': []},
             {'id': 'vec3',
              'metadata': {'category': 'technology',
                           'quarter': 'Q3',
                           'chunk_text': "AAPL'''s strategic Q3 partnerships "
                                          'with semiconductor suppliers could '
                                          'mitigate component risks and '
                                          'stabilize iPhone production'},
              'score': 6.48010254,
              'values': []},
             {'id': 'vec1',
              'metadata': {'category': 'technology',
                           'quarter': 'Q3',
                           'chunk_text': 'AAPL reported a year-over-year '
                                          'revenue increase, expecting '
                                          'stronger Q3 demand for its flagship '
                                          'phones.'},
              'score': 5.3671875,
              'values': []}],
 'namespace': 'example-namespace',
 'usage': {'read_units': 1}}
```

```javascript JavaScript theme={null}
{ 
  matches: [
            { 
              id: 'vec2',
              score: 10.9042969,
              values: [],
              metadata: {
                chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                category: 'technology',
                quarter: 'Q4'
              }
            },
            {
              id: 'vec3',
              score: 6.48010254,
              values: [],
              metadata: {
                chunk_text: "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
                category: 'technology',
                quarter: 'Q3'
              }
            },
            {
              id: 'vec1',
              score: 5.3671875,
              values: [],
              metadata: {
                  chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.',
                  category: 'technology',
                  quarter: 'Q3'
              }
            }
          ],
  namespace: 'example-namespace',
  usage: {readUnits: 1}
}
```

```java Java theme={null}
class QueryResponseWithUnsignedIndices {
    matches: [ScoredVectorWithUnsignedIndices {
        score: 10.34375
        id: vec2
        values: []
        metadata: fields {
          key: "category"
          value {
            string_value: "technology"
          }
        }
        fields {
          key: "chunk_text"
          value {
            string_value: "Analysts suggest that AAPL\'\\\'\'s upcoming Q4 product launch event might solidify its position in the premium smartphone market."
          }
        }
        fields {
          key: "quarter"
          value {
            string_value: "Q4"
          }
        }
        
        sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
            indicesWithUnsigned32Int: []
            values: []
        }
    }, ScoredVectorWithUnsignedIndices {
        score: 5.8638916
        id: vec3
        values: []
        metadata: fields {
          key: "category"
          value {
            string_value: "technology"
          }
        }
        fields {
          key: "chunk_text"
          value {
            string_value: "AAPL\'\\\'\'s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"
          }
        }
        fields {
          key: "quarter"
          value {
            string_value: "Q3"
          }
        }
        
        sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
            indicesWithUnsigned32Int: []
            values: []
        }
    }, ScoredVectorWithUnsignedIndices {
        score: 5.3671875
        id: vec1
        values: []
        metadata: fields {
          key: "category"
          value {
            string_value: "technology"
          }
        }
        fields {
          key: "chunk_text"
          value {
            string_value: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
          }
        }
        fields {
          key: "quarter"
          value {
            string_value: "Q3"
          }
        }
        
        sparseValuesWithUnsignedIndices: SparseValuesWithUnsignedIndices {
            indicesWithUnsigned32Int: []
            values: []
        }
    }]
    namespace: example-namespace
    usage: read_units: 1

}
```

```go Go theme={null}
{
  "matches": [
    {
      "vector": {
        "id": "vec2",
        "metadata": {
          "category": "technology",
          "quarter": "Q4",
          "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
        }
      },
      "score": 10.904296
    },
    {
      "vector": {
        "id": "vec3",
        "metadata": {
          "category": "technology",
          "quarter": "Q3",
          "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production"
        }
      },
      "score": 6.4801025
    },
    {
      "vector": {
        "id": "vec1",
        "metadata": {
          "category": "technology",
          "quarter": "Q3",
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones"
        }
      },
      "score": 5.3671875
    }
  ],
  "usage": {
    "read_units": 1
  },
  "namespace": "example-namespace"
}
```

```json curl theme={null}
{
  "results": [],
  "matches": [
    {
      "id": "vec2",
      "score": 10.9042969,
      "values": [],
      "metadata": {
        "chunk_text": "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
        "category": "technology",
        "quarter": "Q4"
      }
    },
    {
      "id": "vec3",
      "score": 6.48010254,
      "values": [],
      "metadata": {
        "chunk_text": "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
        "category": "technology",
        "quarter": "Q3"
      }
    },
    {
      "id": "vec1",
      "score": 5.3671875,
      "values": [],
      "metadata": {
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "category": "technology",
          "quarter": "Q3"
      }
    }
  ],
  "namespace": "example-namespace",
  "usage": {
    "readUnits": 1
  }
}
```

### Query with a record ID

When you search with a record ID, Pinecone uses the sparse vector associated with the record as the query. To search an index of sparse vectors with a record ID, use the [Search with a vector](/reference/api/latest/data-plane/query) operation with the following parameters:

* `namespace`: The [namespace](/guides/indexes/index-data-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `id`: The unique record ID containing the sparse vector to use as the query.
* `top_k`: The number of results to return.
* `include_values`: Whether to include the vector values of the matching records in the response. Defaults to `false`.
* `include_metadata`: Whether to include the metadata of the matching records in the response. Defaults to `false`.

> [!NOTE]
>
> When querying with `top_k` over 1000, for optimal performance set `include_values=false` and `include_metadata=false` to return only IDs and scores.
>
> Since vectors values are retrieved from object storage, include them in your query results only when you need them (especially with higher `top_k` values). For details, see [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed).

For example, the following code uses an ID to search for the 3 records in the `example-namespace` namespace that best match the sparse vector in the record:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

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
// see https://docs.pinecone.io/guides/indexes/target-an-index
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
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
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
# see https://docs.pinecone.io/guides/indexes/target-an-index
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

## Query with a metadata filter

The following code queries for the 3 records that are most semantically similar to a query vector and that have a `category` metadata field with the value `digestive system`. For the supported operators, see [Metadata filter expressions](/guides/search/filter-by-metadata#metadata-filter-expressions).

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# Replace with your query embedding, which must match the index's dimension (1536 in this example)
query_vector = [0.1] * 1536

index.query(
    namespace="example-namespace",
    vector=query_vector,
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
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

// Replace with your query embedding, which must match the index's dimension (1536 in this example)
const queryVector = new Array(1536).fill(0.1);

const queryResponse = await index.namespace('example-namespace').query({
    vector: queryVector,
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

import java.util.Collections;
import java.util.List;

public class QueryExample {
    public static void main(String[] args) {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
        // Replace with your query embedding, which must match the index's dimension (1536 in this example)
        List<Float> query = Collections.nCopies(1536, 0.1f);
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

    // Replace with your query embedding, which must match the index's dimension (1536 in this example)
    queryVector := make([]float32, 1536)
    for i := range queryVector {
        queryVector[i] = 0.1
    }

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
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

# Stand-in built with jq. Replace with your query embedding, which must match the index's dimension (1536 in this example)
QUERY_VECTOR=$(jq -nc '[range(1536) | 0.1]')

curl "https://$INDEX_HOST/query" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "vector": '"$QUERY_VECTOR"',
        "namespace": "example-namespace",
        "topK": 3,
        "filter": {"category": {"$eq": "digestive system"}},
        "includeMetadata": true,
        "includeValues": false
    }'
```
