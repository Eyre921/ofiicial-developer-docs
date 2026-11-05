---
title: "Check usage per request"
source: https://docs.pinecone.io/guides/cost/check-usage-per-request
path: guides/cost/check-usage-per-request
---

Check the read units and embedding tokens Pinecone returns on each search, fetch, list, and embedding request to see what a single call consumed.

Requests that consume read units or embedding tokens return a `usage` field alongside their results. Reading it tells you what a single request cost, so you can compare approaches before running them at scale.

## Read units

[Search](/guides/search/search-overview), [fetch](/guides/data/fetch-data), and [list](/guides/data/list-record-ids) requests return a `usage` field with the [read unit](/guides/cost/understand-cost#read-units) consumption of that request.

> [!NOTE]
>
> While Pinecone tracks read unit usage with decimal precision, the Pinecone API and SDKs round these values up to the nearest whole number in search, query, fetch, and list responses. For example, if a search uses 0.45 read units, the API and SDKs will report it as 1 read unit.
>
> For precise read unit reporting, see [index-level metrics](/guides/production/monitor-performance) or the organization-wide [Usage dashboard](/admin/billing/download-usage-report).

In the REST API and the Node.js and Go SDKs, `usage` also reports `egress_bytes` (`egressBytes` in Node.js), the size of the response that counts toward [egress](/guides/cost/understand-cost#egress). The Python SDK doesn't report `egress_bytes`, and its `documents.list` paginator doesn't expose `usage`.

For example, the following search scores documents by a 1536-dimension `dense_vector` field named `embedding`:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

# Replace with your query embedding, which must match the index's dimension (1536 in this example)
query_vector = [0.1] * 1536

response = index.documents.search(
    namespace="example-namespace",
    top_k=3,
    score_by=[
        {"type": "dense_vector", "fields": ["embedding"], "values": query_vector}
    ],
)

print(response.usage)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: "INDEX_HOST", namespace: "example-namespace" })

// Replace with your query embedding, which must match the index's dimension (1536 in this example)
const queryVector = new Array(1536).fill(0.1)

const response = await index.documents.search({
  topK: 3,
  scoreBy: [
    { type: 'dense_vector', fields: ['embedding'], values: queryVector },
  ],
})

console.log(response)
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
    res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
        TopK: 3,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeDenseVector, Fields: []string{"embedding"}, Values: &queryVector},
        },
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

# Replace the values with your 1536-dimension query embedding
curl "https://$INDEX_HOST/namespaces/example-namespace/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 3,
    "score_by": [
      { "type": "dense_vector", "fields": ["embedding"], "values": [0.1, 0.1, 0.1, ...] }
    ]
  }'
```

The response looks like this:

```python Python theme={null}
DocumentSearchUsage(read_units=1, embed_total_tokens=None)
```

```javascript JavaScript theme={null}
{
  matches: [
    { _id: 'doc4', _score: 0.8751253 },
    { _id: 'doc8', _score: 0.87052643 },
    { _id: 'doc1', _score: 0.8700179 }
  ],
  namespace: 'example-namespace',
  usage: { readUnits: 1, egressBytes: 68, embedTotalTokens: undefined }
}
```

```go Go theme={null}
{
  "matches": [
    {
      "_id": "doc4",
      "_score": 0.8751253
    },
    {
      "_id": "doc8",
      "_score": 0.87052643
    },
    {
      "_id": "doc1",
      "_score": 0.8700179
    }
  ],
  "namespace": "example-namespace",
  "usage": {
    "read_units": 1,
    "egress_bytes": 68
  }
}
```

```json curl theme={null}
{
  "matches": [
    { "_id": "doc4", "_score": 0.8751253 },
    { "_id": "doc8", "_score": 0.87052643 },
    { "_id": "doc1", "_score": 0.8700179 }
  ],
  "namespace": "example-namespace",
  "usage": { "read_units": 1, "egress_bytes": 68 }
}
```

## Embedding tokens

Requests that use one of [Pinecone's hosted embedding models](/guides/indexes/index-configuration#embedding-models) return a `usage` field with the number of tokens embedded:

* The [Generate vectors](/reference/api/latest/inference/generate-vectors) operation reports `total_tokens`.
* Upserts and searches on an index with [integrated embedding](/guides/search/integrated-embedding) report `embed_total_tokens` (`embedTotalTokens` in Node.js). A search reports it alongside `read_units`.

For example, the following request uses the `llama-text-embed-v2` model to embed sentences related to the word "apple":

```python Python theme={null}
# Import the Pinecone library
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import time

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key="YOUR_API_KEY")

# Define a sample dataset where each item has a unique ID and piece of text
data = [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
]

# Convert the text into numerical vectors that Pinecone can index
embeddings = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=[d['text'] for d in data],
    parameters={"input_type": "passage", "truncate": "END"}
)

print(embeddings)
```

```javascript JavaScript theme={null}
// Import the Pinecone library
import { Pinecone } from '@pinecone-database/pinecone';

// Initialize a Pinecone client with your API key
const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// Define a sample dataset where each item has a unique ID and piece of text
const data = [
  { id: 'vec1', text: 'Apple is a popular fruit known for its sweetness and crisp texture.' },
  { id: 'vec2', text: 'The tech company Apple is known for its innovative products like the iPhone.' },
  { id: 'vec3', text: 'Many people enjoy eating apples as a healthy snack.' },
  { id: 'vec4', text: 'Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.' },
  { id: 'vec5', text: 'An apple a day keeps the doctor away, as the saying goes.' },
  { id: 'vec6', text: 'Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.' }
];

// Convert the text into numerical vectors that Pinecone can index
const model = 'llama-text-embed-v2';

const embeddings = await pc.inference.embed({
  model,
  inputs: data.map(d => d.text),
  parameters: { inputType: 'passage', truncate: 'END' },
});

console.log(embeddings);
```

```java Java theme={null}
// Import the required classes
import io.pinecone.clients.Index;
import io.pinecone.clients.Inference;
import io.pinecone.clients.Pinecone;
import org.openapitools.inference.client.ApiException;
import org.openapitools.inference.client.model.Embedding;
import org.openapitools.inference.client.model.EmbeddingsList;

import java.math.BigDecimal;
import java.util.*;
import java.util.stream.Collectors;

public class GenerateEmbeddings {
    public static void main(String[] args) throws ApiException {
        // Initialize a Pinecone client with your API key
        Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
        Inference inference = pc.getInferenceClient();

        // Prepare input sentences to be embedded
        List<DataObject> data = Arrays.asList(
            new DataObject("vec1", "Apple is a popular fruit known for its sweetness and crisp texture."),
            new DataObject("vec2", "The tech company Apple is known for its innovative products like the iPhone."),
            new DataObject("vec3", "Many people enjoy eating apples as a healthy snack."),
            new DataObject("vec4", "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."),
            new DataObject("vec5", "An apple a day keeps the doctor away, as the saying goes."),
            new DataObject("vec6", "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.")
        );

        List<String> inputs = data.stream()
            .map(DataObject::getText)
            .collect(Collectors.toList());

        // Specify the embedding model and parameters
        String embeddingModel = "llama-text-embed-v2";

        Map<String, Object> parameters = new HashMap<>();
        parameters.put("input_type", "passage");
        parameters.put("truncate", "END");

        // Generate embeddings for the input data
        EmbeddingsList embeddings = inference.embed(embeddingModel, parameters, inputs);

        // Get embedded data
        List<Embedding> embeddedData = embeddings.getData();
    }

    private static List<Float> convertBigDecimalToFloat(List<BigDecimal> bigDecimalValues) {
        return bigDecimalValues.stream()
            .map(BigDecimal::floatValue)
            .collect(Collectors.toList());
    }
}

class DataObject {
    private String id;
    private String text;

    public DataObject(String id, String text) {
        this.id = id;
        this.text = text;
    }

    public String getId() {
        return id;
    }
    public String getText() {
        return text;
    }
}
```

```go Go theme={null}
package main

// Import the required packages
import (
    "context"
   	"encoding/json"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

type Data struct {
    ID   string
    Text string
}

func prettifyStruct(obj interface{}) string {
    bytes, _ := json.MarshalIndent(obj, "", "  ")
    return string(bytes)
}

func main() {
    ctx := context.Background()

    // Initialize a Pinecone client with your API key
    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    // Define a sample dataset where each item has a unique ID and piece of text
    data := []Data{
        {ID: "vec1", Text: "Apple is a popular fruit known for its sweetness and crisp texture."},
        {ID: "vec2", Text: "The tech company Apple is known for its innovative products like the iPhone."},
        {ID: "vec3", Text: "Many people enjoy eating apples as a healthy snack."},
        {ID: "vec4", Text: "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {ID: "vec5", Text: "An apple a day keeps the doctor away, as the saying goes."},
        {ID: "vec6", Text: "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."},
    }

    // Specify the embedding model and parameters
    embeddingModel := "llama-text-embed-v2"

    docParameters := pinecone.EmbedParameters{
        "input_type": "passage",
        "truncate":   "END",
    }

    // Convert the text into numerical vectors that Pinecone can index
    var documents []string
    for _, d := range data {
        documents = append(documents, d.Text)
    }

    docEmbeddingsResponse, err := pc.Inference.Embed(ctx, &pinecone.EmbedRequest{
        Model:      embeddingModel,
        TextInputs: documents,
        Parameters: docParameters,
    }) 
    if err != nil {
        log.Fatalf("Failed to embed documents: %v", err)
    } else {
        fmt.Println(prettifyStruct(docEmbeddingsResponse))
    }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl https://api.pinecone.io/embed \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
      "model": "llama-text-embed-v2",
      "parameters": {
        "input_type": "passage",
        "truncate": "END"
      },
      "inputs": [
        {"text": "Apple is a popular fruit known for its sweetness and crisp texture."},
        {"text": "The tech company Apple is known for its innovative products like the iPhone."},
        {"text": "Many people enjoy eating apples as a healthy snack."},
        {"text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
        {"text": "An apple a day keeps the doctor away, as the saying goes."},
        {"text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
      ]
  }'
```

The response looks like this:

```python Python theme={null}
EmbeddingsList(model='llama-text-embed-v2', vector_type='dense', count=6, usage=EmbedUsage(total_tokens=210))
```

```javascript JavaScript theme={null}
{
  model: 'llama-text-embed-v2',
  vectorType: 'dense',
  data: [
    { values: [Array], vectorType: 'dense' },
    ...
  ],
  usage: { totalTokens: 210 }
}
```

```java Java theme={null}
class EmbeddingsList {
    model: llama-text-embed-v2
    data: [class Embedding {
        values: [0.04925537109375, -0.01313018798828125, -0.0112762451171875, ...]
        additionalProperties: null
    }, ...]
    usage: class EmbeddingsListUsage {
        totalTokens: 130
        additionalProperties: null
    }
    additionalProperties: null
}
```

```go Go theme={null}
{
  "data": [
    {
      "dense_embedding": {
        "vector_type": "dense",
        "values": [
          0.00234222412109375,
          -0.0709228515625,
          0.052337646484375,
          ...
        ]
      }
    },
    ...
  ],
  "model": "llama-text-embed-v2",
  "vector_type": "dense",
  "usage": {
    "total_tokens": 210
  }
}
```

```json curl theme={null}
{
  "model": "llama-text-embed-v2",
  "vector_type": "dense",
  "data": [
    {
      "vector_type": "dense",
      "values": [
        0.00234222412109375,
        -0.0709228515625,
        0.052337646484375,
        ...
      ]
    },
    ...
  ],
  "usage": {
    "total_tokens": 210
  }
}
```
