---
title: "Design for multitenancy"
source: https://docs.pinecone.io/guides/index-data/design-for-multitenancy
path: guides/index-data/design-for-multitenancy
---

Design multitenancy in Pinecone by choosing between namespace-per-tenant isolation and metadata filtering, with their cost and performance tradeoffs.

Many applications have a concept of tenants: users, organizations, projects, or other groups that should only access their own data. How you model this access control significantly impacts query performance and cost.

## Use namespaces for tenant isolation

The most efficient way to implement multitenancy is to use [namespaces](/guides/index-data/indexing-overview#namespaces) to separate data by tenant. With this approach, each tenant has their own namespace, and queries only scan that tenant's data, resulting in better performance and lower costs.

For a complete implementation guide with examples across all SDKs, see [Implement multitenancy](/guides/index-data/implement-multitenancy).

<Accordion title="Why namespaces are more efficient">
  When you use namespaces for multitenancy:

  * **Lower query costs and faster performance**: Query cost is based on namespace size. If you have 100 tenants with 1 GB each, querying one tenant's namespace costs 1 RU and scans only 1 GB. With metadata filtering in a single namespace (100 GB total), the same query costs 100 RUs and scans all 100 GB, even though the filter narrows results.
  * **Natural isolation**: Reduces the risk of application bugs that could query the wrong tenant's data (for example, by passing an incorrect filter value).
</Accordion>

## Avoid filtering by high-cardinality IDs

A common anti-pattern is storing all data in a single namespace and using metadata filters to scope queries to specific users:

<CodeGroup>
  ```python Python theme={null}
  # Anti-pattern: Filtering by many user IDs
  query_vector = [0.1, 0.2, 0.3, ...]  # Your query vector
  results = index.query(
      vector=query_vector,
      top_k=10,
      filter={
          "allowed_user_ids": {"$in": ["user_1", "user_2", ..., "user_10000"]}
      }
  )
  ```

  ```javascript JavaScript theme={null}
  // Anti-pattern: Filtering by many user IDs
  const queryVector = [0.1, 0.2, 0.3, ...];  // Your query vector
  const results = await index.query({
    vector: queryVector,
    topK: 10,
    filter: {
      allowed_user_ids: { $in: ["user_1", "user_2", ..., "user_10000"] }
    }
  });
  ```

  ```java Java theme={null}
  // Anti-pattern: Filtering by many user IDs
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;
  import java.util.Arrays;
  import java.util.List;

  Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();
  Index index = pinecone.getIndexConnection("your-index-name");
  List<Float> queryVector = Arrays.asList(0.1f, 0.2f, 0.3f, ...);  // Your query vector

  // Build filter with $in operator (up to 10,000 values)
  Struct.Builder filterBuilder = Struct.newBuilder();
  Value.Builder listValueBuilder = Value.newBuilder();
  listValueBuilder.getListValueBuilder()
      .addAllValues(Arrays.asList(
          Value.newBuilder().setStringValue("user_1").build(),
          Value.newBuilder().setStringValue("user_2").build()
          // ... up to 10,000 values
      ));
  filterBuilder.putFields("allowed_user_ids",
      Value.newBuilder()
          .setStructValue(Struct.newBuilder()
              .putFields("$in", listValueBuilder.build())
              .build())
          .build());
  Struct filter = filterBuilder.build();

  QueryResponseWithUnsignedIndices results = index.queryByVector(
      10,
      queryVector,
      null, // default namespace
      filter
  );
  ```

  ```go Go theme={null}
  // Anti-pattern: Filtering by many user IDs
  import (
      "context"
      "fmt"
      "log"
      "github.com/pinecone-io/go-pinecone/v5/pinecone"
      "google.golang.org/protobuf/types/known/structpb"
  )

  ctx := context.Background()

  clientParams := pinecone.NewClientParams{
      ApiKey: "YOUR_API_KEY",
  }
  pc, err := pinecone.NewClient(clientParams)
  if err != nil {
      log.Fatalf("Failed to create Client: %v", err)
  }

  idx, err := pc.DescribeIndex(ctx, "your-index-name")
  if err != nil {
      log.Fatalf("Failed to describe index: %v", err)
  }

  idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
      Host: idx.Host,
  })
  if err != nil {
      log.Fatalf("Failed to create IndexConnection: %v", err)
  }

  queryVector := []float32{0.1, 0.2, 0.3, ...}  // Your query vector

  userIds := []interface{}{"user_1", "user_2", /* ... up to 10,000 values */}
  metadataMap := map[string]interface{}{
      "allowed_user_ids": map[string]interface{}{
          "$in": userIds,
      },
  }
  filter, err := structpb.NewStruct(metadataMap)
  if err != nil {
      log.Fatalf("Failed to create filter: %v", err)
  }

  queryReq := &pinecone.QueryByVectorValuesRequest{
      Vector:          queryVector,
      TopK:            10,
      MetadataFilter:  filter,
      IncludeMetadata: true,
  }
  results, err := idxConnection.QueryByVectorValues(ctx, queryReq)
  if err != nil {
      log.Fatalf("Failed to query: %v", err)
  }
  fmt.Printf("Found %d matches:\n", len(results.Matches))
  for _, match := range results.Matches {
      fmt.Printf("  ID: %s, Score: %.4f\n", match.Vector.Id, match.Score)
      if match.Vector.Metadata != nil {
          fmt.Printf("    Metadata: %v\n", match.Vector.Metadata)
      }
  }
  ```

  ```bash curl theme={null}
  # Anti-pattern: Filtering by many user IDs
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/query" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "Content-Type: application/json" \
       -H "X-Pinecone-Api-Version: 2026-07" \
       -d '{
             "vector": [0.1, 0.2, 0.3, ...],
             "topK": 10,
             "includeMetadata": true,
             "filter": {
               "allowed_user_ids": {
                 "$in": ["user_1", "user_2", ..., "user_10000"]
               }
             }
          }'
  ```
</CodeGroup>

This approach has several drawbacks:

* **Performance degradation**: Large `$in` filters increase network payload size and query latency.
* **Hard limits**: Each `$in` or `$nin` operator is limited to 10,000 values. Exceeding this limit will cause the request to fail. See [Metadata filter limits](/reference/api/database-limits/operation-limits#metadata-filter-limits).

## Use access control groups instead of individual IDs

If data must be shared across many tenants, design your access control using the smallest number of groups that describe a user's access:

<CodeGroup>
  ```python Python theme={null}
  # Better: Filter by organization or role instead of individual users
  query_vector = [0.1, 0.2, 0.3, ...]  # Your query vector
  results = index.query(
      vector=query_vector,
      top_k=10,
      filter={
          "$or": [
              {"organization_id": {"$eq": "org_A"}},
              {"project_id": {"$eq": "project_B"}}
          ]
      }
  )
  ```

  ```javascript JavaScript theme={null}
  // Better: Filter by organization or role instead of individual users
  const queryVector = [0.1, 0.2, 0.3, ...];  // Your query vector
  const results = await index.query({
    vector: queryVector,
    topK: 10,
    filter: {
      $or: [
        { organization_id: { $eq: "org_A" } },
        { project_id: { $eq: "project_B" } }
      ]
    }
  });
  ```

  ```java Java theme={null}
  // Better: Filter by organization or role instead of individual users
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.clients.Pinecone;
  import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;
  import java.util.Arrays;
  import java.util.List;

  Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();
  Index index = pinecone.getIndexConnection("your-index-name");
  List<Float> queryVector = Arrays.asList(0.1f, 0.2f, 0.3f, ...);  // Your query vector

  // Build filter with $or operator
  Struct.Builder orgFilterBuilder = Struct.newBuilder();
  orgFilterBuilder.putFields("organization_id",
      Value.newBuilder()
          .setStructValue(Struct.newBuilder()
              .putFields("$eq", Value.newBuilder()
                  .setStringValue("org_A")
                  .build())
              .build())
          .build());

  Struct.Builder projectFilterBuilder = Struct.newBuilder();
  projectFilterBuilder.putFields("project_id",
      Value.newBuilder()
          .setStructValue(Struct.newBuilder()
              .putFields("$eq", Value.newBuilder()
                  .setStringValue("project_B")
                  .build())
              .build())
          .build());

  Struct.Builder orFilterBuilder = Struct.newBuilder();
  orFilterBuilder.putFields("$or",
      Value.newBuilder()
          .getListValueBuilder()
          .addValues(Value.newBuilder().setStructValue(orgFilterBuilder.build()).build())
          .addValues(Value.newBuilder().setStructValue(projectFilterBuilder.build()).build())
          .build());

  QueryResponseWithUnsignedIndices results = index.queryByVector(
      10,
      queryVector,
      null, // default namespace
      orFilterBuilder.build(),
      false, // includeValues
      true // includeMetadata
  );
  ```

  ```go Go theme={null}
  // Better: Filter by organization or role instead of individual users
  import (
      "context"
      "fmt"
      "log"
      "github.com/pinecone-io/go-pinecone/v5/pinecone"
      "google.golang.org/protobuf/types/known/structpb"
  )

  ctx := context.Background()

  clientParams := pinecone.NewClientParams{
      ApiKey: "YOUR_API_KEY",
  }
  pc, err := pinecone.NewClient(clientParams)
  if err != nil {
      log.Fatalf("Failed to create Client: %v", err)
  }

  idx, err := pc.DescribeIndex(ctx, "your-index-name")
  if err != nil {
      log.Fatalf("Failed to describe index: %v", err)
  }

  idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
      Host: idx.Host,
  })
  if err != nil {
      log.Fatalf("Failed to create IndexConnection: %v", err)
  }

  queryVector := []float32{0.1, 0.2, 0.3, ...}  // Your query vector

  metadataMap := map[string]interface{}{
      "$or": []interface{}{
          map[string]interface{}{
              "organization_id": map[string]interface{}{
                  "$eq": "org_A",
              },
          },
          map[string]interface{}{
              "project_id": map[string]interface{}{
                  "$eq": "project_B",
              },
          },
      },
  }
  filter, err := structpb.NewStruct(metadataMap)
  if err != nil {
      log.Fatalf("Failed to create filter: %v", err)
  }

  queryReq := &pinecone.QueryByVectorValuesRequest{
      Vector:          queryVector,
      TopK:            10,
      MetadataFilter:  filter,
      IncludeMetadata: true,
  }
  results, err := idxConnection.QueryByVectorValues(ctx, queryReq)
  if err != nil {
      log.Fatalf("Failed to query: %v", err)
  }
  fmt.Printf("Found %d matches:\n", len(results.Matches))
  for _, match := range results.Matches {
      fmt.Printf("  ID: %s, Score: %.4f\n", match.Vector.Id, match.Score)
      if match.Vector.Metadata != nil {
          fmt.Printf("    Metadata: %v\n", match.Vector.Metadata)
      }
  }
  ```

  ```bash curl theme={null}
  # Better: Filter by organization or role instead of individual users
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/query" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "Content-Type: application/json" \
       -H "X-Pinecone-Api-Version: 2026-07" \
       -d '{
             "vector": [0.1, 0.2, 0.3, ...],
             "topK": 10,
             "includeMetadata": true,
             "filter": {
               "$or": [
                 {"organization_id": {"$eq": "org_A"}},
                 {"project_id": {"$eq": "project_B"}}
               ]
             }
          }'
  ```
</CodeGroup>

Instead of passing thousands of user IDs, this filter uses only 2 group identifiers to achieve the same access control.

## Multitenancy patterns

The following table provides general guidelines for choosing a multitenancy approach. Evaluate your specific use case, access patterns, and requirements to determine the best fit for your application.

| Data pattern                              | Recommended approach                                                  | Query cost                             | Performance |
| :---------------------------------------- | :-------------------------------------------------------------------- | :------------------------------------- | :---------- |
| Each tenant's data is completely separate | One index, one namespace per tenant                                   | Lowest (scans only tenant namespace)   | Fastest     |
| Large tenants with many sub-groups        | One index per large tenant, namespaces for sub-groups                 | Low (scans only sub-group namespace)   | Fast        |
| Data shared across tenants                | One index, shared namespace, filter by group IDs (org, project, role) | Higher (scans entire shared namespace) | Slower      |

<Warning>
  Avoid filtering by large lists of individual user IDs. For the limits, the performance and cost impact, and the alternatives, see [Avoid filtering by high-cardinality IDs](#avoid-filtering-by-high-cardinality-ids).
</Warning>

For a complete step-by-step implementation guide, see [Implement multitenancy](/guides/index-data/implement-multitenancy).
