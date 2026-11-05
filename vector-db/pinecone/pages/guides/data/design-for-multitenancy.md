---
title: "Design for multitenancy"
source: https://docs.pinecone.io/guides/data/design-for-multitenancy
path: guides/data/design-for-multitenancy
---

Design multitenancy in Pinecone by choosing between namespace-per-tenant isolation and metadata filtering, with their cost and performance tradeoffs.

Many applications have a concept of tenants: users, organizations, projects, or other groups that should only access their own data. How you model this access control significantly impacts query performance and cost.

## Use namespaces for tenant isolation

The most efficient way to implement multitenancy is to use [namespaces](/guides/indexes/index-data-overview#namespaces) to separate data by tenant. With this approach, each tenant has their own namespace, and searches only scan that tenant's data, resulting in better performance and lower costs.

* **Lower search costs and faster performance**: Search cost is based on namespace size. If you have 100 tenants with 1 GB each, searching one tenant's namespace costs 1 RU and scans only 1 GB. With metadata filtering in a single namespace (100 GB total), the same search costs 100 RUs and scans all 100 GB, even though the filter narrows results.
* **Natural isolation**: Reduces the risk of application bugs that could search the wrong tenant's data (for example, by passing an incorrect filter value).

For a complete implementation guide with examples, see [Implement multitenancy](/guides/data/implement-multitenancy).

## Avoid filtering by high-cardinality IDs

A common anti-pattern is storing all data in a single namespace and using metadata filters to scope searches to specific users. The examples on this page search a `dense_vector` field named `embedding`:

```python Python theme={null}
# Anti-pattern: Filtering by many user IDs
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

query_vector = [0.1, 0.2, 0.3, ...]  # Your query vector
results = index.documents.search(
    namespace="example-namespace",
    top_k=10,
    score_by=[
        {"type": "dense_vector", "fields": ["embedding"], "values": query_vector}
    ],
    filter={
        "allowed_user_ids": {"$in": ["user_1", "user_2", ..., "user_10000"]}
    },
)

for match in results.matches:
    print(match._id, match._score)
```

```javascript JavaScript theme={null}
// Anti-pattern: Filtering by many user IDs
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

const queryVector = [0.1, 0.2, 0.3, ...];  // Your query vector
const results = await index.documents.search({
  topK: 10,
  scoreBy: [
    { type: 'dense_vector', fields: ['embedding'], values: queryVector },
  ],
  filter: {
    allowed_user_ids: { $in: ["user_1", "user_2", ..., "user_10000"] }
  }
});

console.log(results);
```

```go Go theme={null}
// Anti-pattern: Filtering by many user IDs
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

    queryVector := []float32{0.1, 0.2, 0.3, ...} // Your query vector
    userIds := []interface{}{"user_1", "user_2", /* ... up to 10,000 values */}

    res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
        TopK: 10,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeDenseVector, Fields: []string{"embedding"}, Values: &queryVector},
        },
        Filter: map[string]interface{}{
            "allowed_user_ids": map[string]interface{}{"$in": userIds},
        },
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
# Anti-pattern: Filtering by many user IDs
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/example-namespace/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 10,
    "score_by": [
      { "type": "dense_vector", "fields": ["embedding"], "values": [0.1, 0.2, 0.3, ...] }
    ],
    "filter": {
      "allowed_user_ids": {
        "$in": ["user_1", "user_2", ..., "user_10000"]
      }
    }
  }'
```

This approach has several drawbacks:

* **Performance degradation**: Large `$in` filters increase network payload size and query latency.
* **Hard limits**: Each `$in` or `$nin` operator is limited to 10,000 values. Exceeding this limit will cause the request to fail. See [Metadata filter limits](/reference/api/database-limits/operation-limits#metadata-filter-limits).

## Use access control groups instead of individual IDs

If data must be shared across many tenants, design your access control using the smallest number of groups that describe a user's access:

```python Python theme={null}
# Better: Filter by organization or role instead of individual users
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

query_vector = [0.1, 0.2, 0.3, ...]  # Your query vector
results = index.documents.search(
    namespace="example-namespace",
    top_k=10,
    score_by=[
        {"type": "dense_vector", "fields": ["embedding"], "values": query_vector}
    ],
    filter={
        "$or": [
            {"organization_id": {"$eq": "org_A"}},
            {"project_id": {"$eq": "project_B"}}
        ]
    },
)

for match in results.matches:
    print(match._id, match._score)
```

```javascript JavaScript theme={null}
// Better: Filter by organization or role instead of individual users
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

const queryVector = [0.1, 0.2, 0.3, ...];  // Your query vector
const results = await index.documents.search({
  topK: 10,
  scoreBy: [
    { type: 'dense_vector', fields: ['embedding'], values: queryVector },
  ],
  filter: {
    $or: [
      { organization_id: { $eq: "org_A" } },
      { project_id: { $eq: "project_B" } }
    ]
  }
});

console.log(results);
```

```go Go theme={null}
// Better: Filter by organization or role instead of individual users
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

    queryVector := []float32{0.1, 0.2, 0.3, ...} // Your query vector

    res, err := idxConnection.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
        TopK: 10,
        ScoreBy: []pinecone.DocumentScoringMethod{
            {Type: pinecone.DocumentScoringTypeDenseVector, Fields: []string{"embedding"}, Values: &queryVector},
        },
        Filter: map[string]interface{}{
            "$or": []interface{}{
                map[string]interface{}{"organization_id": map[string]interface{}{"$eq": "org_A"}},
                map[string]interface{}{"project_id": map[string]interface{}{"$eq": "project_B"}},
            },
        },
    })
    if err != nil {
        log.Fatalf("Failed to search documents: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
# Better: Filter by organization or role instead of individual users
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/example-namespace/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 10,
    "score_by": [
      { "type": "dense_vector", "fields": ["embedding"], "values": [0.1, 0.2, 0.3, ...] }
    ],
    "filter": {
      "$or": [
        { "organization_id": { "$eq": "org_A" } },
        { "project_id": { "$eq": "project_B" } }
      ]
    }
  }'
```

Instead of passing thousands of user IDs, this filter uses only 2 group identifiers to achieve the same access control.

## Multitenancy patterns

The following table provides general guidelines for choosing a multitenancy approach. Evaluate your specific use case, access patterns, and requirements to determine the best fit for your application.

| Data pattern | Recommended approach | Query cost | Performance |
| :- | :- | :- | :- |
| Each tenant's data is completely separate | One index, one namespace per tenant | Lowest (scans only tenant namespace) | Fastest |
| Large tenants with many sub-groups | One index per large tenant, namespaces for sub-groups | Low (scans only sub-group namespace) | Fast |
| Data shared across tenants | One index, shared namespace, filter by group IDs (org, project, role) | Higher (scans entire shared namespace) | Slower |

> [!WARNING]
>
> Avoid filtering by large lists of individual user IDs. For the limits, the performance and cost impact, and the alternatives, see [Avoid filtering by high-cardinality IDs](#avoid-filtering-by-high-cardinality-ids).

For a complete step-by-step implementation guide, see [Implement multitenancy](/guides/data/implement-multitenancy).
