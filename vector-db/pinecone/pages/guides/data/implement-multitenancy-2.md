---
title: "Implement multitenancy"
source: https://docs.pinecone.io/guides/data/implement-multitenancy
path: guides/data/implement-multitenancy
---

Implement multitenancy in Pinecone with one namespace per tenant on a serverless index to isolate customer data for SaaS RAG or semantic search apps.

[Multitenancy](https://en.wikipedia.org/wiki/Multitenancy) is a software architecture where a single instance of a system serves multiple customers, or tenants, while ensuring data isolation between them for privacy and security.

This page shows you how to implement multitenancy in Pinecone using a document index with one namespace per tenant. For when to use namespaces, metadata filtering, or other approaches, see [Design for multitenancy](/guides/data/design-for-multitenancy).

## How it works

In Pinecone, an [index](/guides/indexes/index-data-overview) is the highest-level organizational unit of data, where you define a schema for the documents stored in the index, such as the dimension and similarity metric of a `dense_vector` field.

Within an index, documents are stored in [namespaces](/guides/indexes/index-data-overview#namespaces), and all [upserts](/guides/data/upsert-data), [searches](/guides/search/search-overview), and other data read and write operations always target one namespace.

This structure makes it easy to implement multitenancy. For example, for an AI-powered SaaS application where you need to isolate the data of each customer, you would assign each customer to a namespace and target their writes and searches to that namespace:

![Diagram of a multitenant SaaS index with three namespaces, one per customer, each holding documents 1 through n. A query on customer 1's data targets namespace 1, and a new document for customer 3 goes to namespace 3.](https://mintcdn.com/pinecone/qjxrsVApPT3I4Dwt/images/multitenant-saas-namespaces-light.svg?fit=max\&auto=format\&n=qjxrsVApPT3I4Dwt\&q=85\&s=290ae697e92b15148b8fa36709755b8c)

In cases where you have different workload patterns (e.g., RAG and semantic search), you would use a different index for each workload, with one namespace per customer in each index:

![Diagram of a RAG index and a semantic search index, each with one namespace per customer. Queries on customer 1's data target namespace 1 in each index.](https://mintcdn.com/pinecone/qjxrsVApPT3I4Dwt/images/multitenant-saas-indexes-light.svg?fit=max\&auto=format\&n=qjxrsVApPT3I4Dwt\&q=85\&s=6ee475750713c79c223cd260d29bf113)

### Benefits

* **Tenant isolation:** In the [serverless architecture](/guides/get-started/architecture), each namespace is stored separately, so using namespaces provides physical isolation of data between tenants. This reduces the risk of application bugs that could search the wrong tenant's data.

* **No noisy neighbors:** Reads and writes always target a single namespace, so the behavior of one tenant doesn't affect other tenants.

* **No maintenance effort:** Serverless indexes scale automatically based on usage; you don't configure or manage any compute or storage resources.

* **Cost efficiency:** Search cost is based on namespace size (1 RU per 1 GB). With 100 tenants of 1 GB each, searching one tenant's namespace costs 1 RU. Using metadata filtering in a single 100 GB namespace would cost 100 RUs for the same search, because it scans all data regardless of filters.

* **Simple tenant offboarding:** To offboard a tenant, you just [delete the relevant namespace](/guides/data/manage-namespaces#delete-a-namespace). This is a lightweight and almost instant operation.

> [!NOTE]
>
> [Namespaces per serverless index](/reference/api/database-limits/object-limits) vary by plan (100 on Starter to 1,000,000 on Enterprise). Pinecone can accommodate more for specific use cases. If your application needs a higher limit, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

## Set up one namespace per tenant

### 1. Create a document index

Serverless indexes [separate storage from compute](/guides/get-started/architecture), scale automatically based on usage, and you pay only for the amount of data stored and operations performed. Combined with the isolation of tenant data using namespaces (next step), serverless indexes are ideal for multitenant use cases.

To [create a document index](/guides/indexes/create-an-index#create-a-document-index), set the cloud and region where the index should be deployed in `deployment`, and declare the fields to index in `schema`. This example declares one `dense_vector` field, `embedding`, with 8 dimensions and the cosine metric:

```python Python theme={null}
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key="YOUR_API_KEY")

schema = (
    SchemaBuilder()
      .add_dense_vector_field(name="embedding", dimension=8, metric="cosine")
      .build()
)

pc.indexes.create(
    name="multitenant-app",
    deployment={"deployment_type": "managed", "cloud": "aws", "region": "us-east-1"},
    schema=schema,
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

await pc.indexes.create({
  name: 'multitenant-app',
  deployment: {
    deploymentType: 'managed',
    cloud: 'aws',
    region: 'us-east-1',
  },
  schema: {
    fields: {
      embedding: {
        type: 'dense_vector',
        dimension: 8,
        metric: 'cosine',
      },
    },
  },
});
```

```go Go theme={null}
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }

    idx, err := pc.CreateIndex(ctx, &pinecone.CreateIndexRequest{
        Name: "multitenant-app",
        Deployment: &pinecone.IndexDeployment{
            Managed: &pinecone.ManagedDeployment{
                Cloud:  pinecone.CloudAWS,
                Region: "us-east-1",
            },
        },
        Schema: pinecone.IndexSchema{
            Fields: map[string]pinecone.IndexSchemaField{
                "embedding": {
                    DenseVector: &pinecone.DenseVectorField{
                        Dimension: 8,
                        Metric:    pinecone.IndexMetricCosine,
                    },
                },
            },
        },
    })
    if err != nil {
        log.Fatalf("Failed to create index: %v", err)
    }
    fmt.Printf("Successfully created index: %v", idx.Name)
}
```

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -s "https://api.pinecone.io/indexes" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
         "name": "multitenant-app",
         "deployment": {
            "deployment_type": "managed",
            "cloud": "aws",
            "region": "us-east-1"
         },
         "schema": {
            "fields": {
               "embedding": {
                  "type": "dense_vector",
                  "dimension": 8,
                  "metric": "cosine"
               }
            }
         }
      }'
```

Before you upsert, [wait for the index to be ready](/guides/indexes/create-an-index#wait-for-the-index-to-be-ready). The Python SDK waits by default.

### 2. Isolate tenant data

In a multitenant solution, you need to isolate data between tenants. To achieve this in Pinecone, use one namespace per tenant. In the [serverless architecture](/guides/get-started/architecture), each namespace is stored separately, so this approach ensures physical isolation of each tenant's data.

To [create a namespace for a tenant](/guides/indexes/index-data-overview#namespaces), specify the namespace when you first [upsert](/guides/data/upsert-data) the tenant's documents. For example, the following code upserts documents for `tenant1` and `tenant2` into the `multitenant-app` index:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.upsert(
    namespace="tenant1",
    documents=[
        {"_id": "A", "embedding": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
        {"_id": "B", "embedding": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
        {"_id": "C", "embedding": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
        {"_id": "D", "embedding": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
    ],
)

index.documents.upsert(
    namespace="tenant2",
    documents=[
        {"_id": "E", "embedding": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
        {"_id": "F", "embedding": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
        {"_id": "G", "embedding": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
        {"_id": "H", "embedding": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]},
    ],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const tenant1 = pc.index({ host: 'INDEX_HOST', namespace: 'tenant1' });
const tenant2 = pc.index({ host: 'INDEX_HOST', namespace: 'tenant2' });

await tenant1.documents.upsert({
  documents: [
    { _id: 'A', embedding: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] },
    { _id: 'B', embedding: [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2] },
    { _id: 'C', embedding: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3] },
    { _id: 'D', embedding: [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4] },
  ],
});

await tenant2.documents.upsert({
  documents: [
    { _id: 'E', embedding: [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] },
    { _id: 'F', embedding: [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6] },
    { _id: 'G', embedding: [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7] },
    { _id: 'H', embedding: [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8] },
  ],
});
```

```go Go theme={null}
package main

import (
    "context"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

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
    tenant1, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "tenant1"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    // This reuses the connection of tenant1 while targeting a different namespace
    tenant2 := tenant1.WithNamespace("tenant2")

    _, err = tenant1.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
        Documents: []pinecone.Document{
            {"_id": "A", "embedding": []float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1}},
            {"_id": "B", "embedding": []float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2}},
            {"_id": "C", "embedding": []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3}},
            {"_id": "D", "embedding": []float32{0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4}},
        },
    })
    if err != nil {
        log.Fatalf("Failed to upsert documents: %v", err)
    }

    _, err = tenant2.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
        Documents: []pinecone.Document{
            {"_id": "E", "embedding": []float32{0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5}},
            {"_id": "F", "embedding": []float32{0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6}},
            {"_id": "G", "embedding": []float32{0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7}},
            {"_id": "H", "embedding": []float32{0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8}},
        },
    })
    if err != nil {
        log.Fatalf("Failed to upsert documents: %v", err)
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/tenant1/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      { "_id": "A", "embedding": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] },
      { "_id": "B", "embedding": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2] },
      { "_id": "C", "embedding": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3] },
      { "_id": "D", "embedding": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4] }
    ]
  }'

curl "https://$INDEX_HOST/namespaces/tenant2/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      { "_id": "E", "embedding": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] },
      { "_id": "F", "embedding": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6] },
      { "_id": "G", "embedding": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7] },
      { "_id": "H", "embedding": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8] }
    ]
  }'
```

When upserting additional documents for a tenant, or when [updating](/guides/data/update-data) or [deleting](/guides/data/delete-data) documents for a tenant, specify the tenant's namespace. For example, the following code updates the `embedding` field of document `A` in `tenant1`:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.update(
    namespace="tenant1",
    documents=[
        {"_id": "A", "embedding": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]},
    ],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'tenant1' });

await index.documents.update({
  documents: [
    { _id: 'A', embedding: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8] },
  ],
});
```

```go Go theme={null}
package main

import (
    "context"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "tenant1"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    _, err = idxConnection.UpdateDocuments(ctx, &pinecone.UpdateDocumentsRequest{
        Documents: []pinecone.Document{
            {"_id": "A", "embedding": []float32{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8}},
        },
    })
    if err != nil {
        log.Fatalf("Failed to update document: %v", err)
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/tenant1/documents/update" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      { "_id": "A", "embedding": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8] }
    ]
  }'
```

### 3. Search tenant data

In a multitenant solution, you need to ensure that the searches of one tenant don't affect the experience of other tenants. To achieve this in Pinecone, target each tenant's [searches](/guides/search/search-overview) at the namespace for the tenant.

For example, the following code searches only `tenant2` for the 3 documents that are most similar to an example query vector:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

results = index.documents.search(
    namespace="tenant2",
    top_k=3,
    score_by=[
        {
            "type": "dense_vector",
            "fields": ["embedding"],
            "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        }
    ],
)

for match in results.matches:
    print(match._id, match._score)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'tenant2' });

const results = await index.documents.search({
  topK: 3,
  scoreBy: [
    { type: 'dense_vector', fields: ['embedding'], values: [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7] },
  ],
});

for (const match of results.matches) {
  console.log(match._id, match._score);
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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "tenant2"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    queryVector := []float32{0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7}
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

curl "https://$INDEX_HOST/namespaces/tenant2/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 3,
    "score_by": [
      {
        "type": "dense_vector",
        "fields": ["embedding"],
        "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
      }
    ]
  }'
```

## Offboard a tenant

In a multitenant solution, you also need it to be quick and easy to offboard a tenant and delete all of its documents. To achieve this in Pinecone, you just [delete the namespace](/guides/data/manage-namespaces#delete-a-namespace) for the specific tenant.

For example, the following code deletes the namespace and all documents for `tenant1`:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.delete_namespace(name="tenant1")
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST' });

await index.deleteNamespace('tenant1');
```

```go Go theme={null}
package main

import (
    "context"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

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
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    }

    err = idxConnection.DeleteNamespace(ctx, "tenant1")
    if err != nil {
        log.Fatalf("Failed to delete namespace: %v", err)
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl -X DELETE "https://$INDEX_HOST/namespaces/tenant1" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07"
```

## Alternative: Metadata filtering

When tenant isolation isn't a strict requirement, or when you need to search across multiple tenants simultaneously, you can store all documents in a single namespace and use metadata fields to assign documents to tenants. At search time, you can then [filter by metadata](/guides/indexes/index-data-overview#metadata).

> [!WARNING]
>
> This approach has significant performance and cost tradeoffs compared to using namespaces:
>
> * Higher search costs: Searches scan the entire namespace regardless of filters, so you pay for scanning all tenants' data even though results are filtered to one tenant.
> * Slower performance: Large namespaces increase search latency, and large filters add network overhead on the request side.
> * Filter size limits: Each `$in` or `$nin` operator is limited to 10,000 values. Exceeding this limit will cause requests to fail. See [Metadata filter limits](/reference/api/database-limits/operation-limits#metadata-filter-limits).
>
> Anti-pattern: Avoid filtering by large lists of individual user IDs. Instead, use access control groups (organization, project, role), namespaces, or post-filter client-side (for semantic search).
>
> For detailed guidance on choosing between namespaces and metadata filtering, see [Design for multitenancy](/guides/data/design-for-multitenancy).

For more background on this approach, see [Multitenancy in Vector Databases](https://www.pinecone.io/learn/series/vector-databases-in-production-for-busy-engineers/vector-database-multi-tenancy/).
