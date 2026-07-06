---
title: "Create a pod-based index"
source: https://docs.pinecone.io/guides/indexes/pods/create-a-pod-based-index
path: guides/indexes/pods/create-a-pod-based-index
---

Legacy instructions for creating Pinecone pod-based indexes. New customers cannot create pod indexes as of August 2025. See serverless index creation for current instructions.

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

This page shows you how to create a pod-based index. For guidance on serverless indexes, see [Create a serverless index](/guides/index-data/create-an-index).

## Create a pod index

To create a pod index, use the [`create_index`](/reference/api/latest/control-plane/create_index) operation as follows:

* Provide a `name` for the index.
* Specify the `dimension` and `metric` of the vectors you'll store in the index. This should match the dimension and metric supported by your embedding model.
* Set `spec.environment` to the [environment](/guides/index-data/create-an-index#cloud-regions) where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.
* Set `spec.pod_type` to the [pod type](/guides/indexes/pods/understanding-pod-based-indexes#pod-types) and [size](/guides/index-data/indexing-overview#pod-size-and-performance) that you want.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_index) for details.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=PodSpec(
      environment="us-west1-gcp",
      pod_type="p1.x1",
      pods=1
    ),
    deletion_protection="disabled"

  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.createIndex({
    name: 'docs-example',
    dimension: 1536,
    metric: 'cosine',
    spec: {
      pod: {
        environment: 'us-west1-gcp',
        podType: 'p1.x1',
        pods: 1
      }
    },
    deletionProtection: 'disabled',
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.createPodsIndex("docs-example", 1536, "us-west1-gcp",
                  "p1.x1", "cosine", DeletionProtection.DISABLED);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      indexName := "docs-example"
    	metric := pinecone.Dotproduct
  	  deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreatePodIndex(ctx, &pinecone.CreatePodIndexRequest{
          Name:               indexName,
          Metric:             &metric,
          Dimension:          1536,
          Environment:        "us-east1-gcp",
          PodType:            "p1.x1",
          DeletionProtection: &deletionProtection,
      })
      if err != nil {
          log.Fatalf("Failed to create pod-based index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created pod-based index: %v", idx.Name)
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
           "name": "docs-example",
           "dimension": 1536,
           "metric": "cosine",
           "spec": {
              "pod": {
                 "environment": "us-west1-gcp",
                 "pod_type": "p1.x1",
                 "pods": 1
              }
           },
           "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>

## Create a pod index from a collection

You can create a pod-based index from a collection. For more details, see [Restore an index](/guides/indexes/pods/restore-a-pod-based-index).
