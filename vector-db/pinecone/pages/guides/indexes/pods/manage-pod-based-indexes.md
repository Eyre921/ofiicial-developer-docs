---
title: "Manage pod-based indexes"
source: https://docs.pinecone.io/guides/indexes/pods/manage-pod-based-indexes
path: guides/indexes/pods/manage-pod-based-indexes
---

Manage Pinecone pod-based indexes. Legacy guide: pod indexes are unavailable to new customers as of August 2025; serverless is recommended for new projects.

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

This page shows you how to manage pod-based indexes.

For guidance on serverless indexes, see [Manage serverless indexes](/guides/manage-data/manage-indexes).

## Describe a pod-based index

Use the [`describe_index`](/reference/api/latest/control-plane/describe_index) endpoint to get a complete description of a specific index:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.describe_index(name="docs-example")

  # Response:
  # {'dimension': 1536,
  #  'host': 'docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io',
  #  'metric': 'cosine',
  #  'name': 'docs-example',
  #  'spec': {'pod': {'environment': 'us-east-1-aws',
  #                   'pod_type': 's1.x1',
  #                   'pods': 1,
  #                   'replicas': 1,
  #                   'shards': 1}},
  #  'status': {'ready': True, 'state': 'Ready'}}
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.describeIndex('docs-example');

  // Response:
  // {
  //    "name": "docs-example",
  //    "dimension": 1536,
  //    "metric": "cosine",
  //    "host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  //    "deletionProtection": "disabled",
  //    "spec": {
  //       "pod": {
  //          "environment": "us-east-1-aws",
  //          "pod_type": "s1.x1",
  //          "pods": 1,
  //          "replicas": 1,
  //          "shards": 1
  //       }
  //    },
  //    "status": {
  //       "ready": true,
  //       "state": "Ready"
  //    }
  // }
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class DescribeIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOURE_API_KEY").build();
          IndexModel indexModel = pc.describeIndex("docs-example");
          System.out.println(indexModel);
      }
  }

  // Response:
  // class IndexModel {
  //     name: docs-example
  //     dimension: 1536
  //     metric: cosine
  //     host: docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io
  //     deletionProtection: disabled
  //     spec: class IndexModelSpec {
  //         serverless: null
  //         pod: class PodSpec {
  //             cloud: aws
  //             region: us-east-1
  //             environment: us-east-1-aws,
  //             podType: s1.x1,
  //             pods: 1,
  //             replicas: 1,
  //             shards: 1
  //         }
  //     }
  //     status: class IndexModelStatus {
  //         ready: true
  //         state: Ready
  //     }
  // }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
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

      idx, err := pc.DescribeIndex(ctx, "docs-example")
      if err != nil {
          log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
      } else {
          fmt.Printf("index: %v\n", prettifyStruct(idx))
      }
  }

  // Response:
  // index: {
  // 	"name": "docs-example",
  // 	"dimension": 1536,
  // 	"host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  // 	"metric": "cosine",
  //  "deletion_protection": "disabled",
  // 	"spec": {
  // 	  "pod": {
  //       "environment": "us-east-1-aws",
  //       "pod_type": "s1.x1",
  //       "pods": 1,
  //       "replicas": 1,
  //       "shards": 1
  // 	  }
  // 	},
  // 	"status": {
  // 	  "ready": true,
  // 	  "state": "Ready"
  // 	}
  // }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  # Response:
  # {
  #    "name": "docs-example",
  #    "metric": "cosine",
  #    "dimension": 1536,
  #    "status": {
  #       "ready": true,
  #       "state": "Ready"
  #    },
  #    "host": "docs-example-4mkljsz.svc.aped-4627-b74a.pinecone.io",
  #    "spec": {
  #       "pod": {
  #          "environment": "us-east-1-aws",
  #          "pod_type": "s1.x1",
  #          "pods": 1,
  #          "replicas": 1,
  #          "shards": 1
  #       }
  #    }
  # }
  ```
</CodeGroup>

<Warning>
  **Do not target an index by name in production.**

  When you target an index by name for data operations such as `upsert` and `query`, the SDK gets the unique DNS host for the index using the `describe_index` operation. This is convenient for testing but should be avoided in production because `describe_index` uses a different API than data operations and therefore adds an additional network call and point of failure. Instead, you should get an index host once and cache it for reuse or specify the host directly.
</Warning>

## Delete a pod-based index

Use the [`delete_index`](/reference/api/latest/control-plane/delete_index) operation to delete a pod-based index and all of its associated resources.

<Note>
  You are billed for a pod-based index even when it is not in use.
</Note>

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone, PodSpec

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.delete_index(name="docs-example")
  ```

  ```javascript JavaScript theme={null}
  // npm install @pinecone-database/pinecone
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.deleteIndex('docs-example');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class DeleteIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.deleteIndex("docs-example");
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

      err = pc.DeleteIndex(ctx, indexName)
      if err != nil {
          log.Fatalf("Failed to delete index: %v", err)
      } else {
          fmt.Println("Index \"%v\" deleted successfully", indexName)
      }
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -i -X DELETE "https://api.pinecone.io/indexes/docs-example" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

If deletion protection is enabled on an index, requests to delete it will fail and return a `403 - FORBIDDEN` status with the following error:

```
Deletion protection is enabled for this index. Disable deletion protection before retrying.
```

Before you can delete such an index, you must first [disable deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).

<Tip>
  You can delete an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). For the index you want to delete, click the three dots to the right of the index name, then click **Delete**.
</Tip>

## Selective metadata indexing

For pod-based indexes, Pinecone indexes all metadata fields by default. When metadata fields contains many unique values, pod-based indexes will consume significantly more memory, which can lead to performance issues, pod fullness, and a reduction in the number of possible vectors that fit per pod.

To avoid indexing high-cardinality metadata that is not needed for [filtering your queries](/guides/index-data/indexing-overview#metadata) and keep memory utilization low, specify which metadata fields to index using the `metadata_config` parameter.

<Note>
  Since high-cardinality metadata does not cause high memory utilization in serverless indexes, selective metadata indexing is not supported.
</Note>

The value for the `metadata_config` parameter is a JSON object containing the names of the metadata fields to index.

```JSON JSON theme={null}
{
    "indexed": [
        "metadata-field-1",
        "metadata-field-2",
        "metadata-field-n"
    ]
}
```

**Example**

The following example creates a pod-based index that only indexes the `genre` metadata field. Queries against this index that filter for the `genre` metadata field may return results; queries that filter for other metadata fields behave as though those fields do not exist.

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
      pods=1,
      metadata_config = {
        "indexed": ["genre"]
      }
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
        pods: 1,
        metadata_config: {
          indexed: ["genre"]
        }
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
          CreateIndexRequestSpecPodMetadataConfig podSpecMetadataConfig = new CreateIndexRequestSpecPodMetadataConfig();
          List<String> indexedItems = Arrays.asList("genre", "year");
          podSpecMetadataConfig.setIndexed(indexedItems);
          pc.createPodsIndex("docs-example", 1536, "us-west1-gcp",
                  "p1.x1", "cosine", podSpecMetadataConfig, DeletionProtection.DISABLED);
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

      podIndexMetadata := &pinecone.PodSpecMetadataConfig{
          Indexed: &[]string{"genre"},
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

  curl -s https://api.pinecone.io/indexes \
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
                 "pods": 1,
                 "metadata_config": {
                    "indexed": ["genre"]
                 }
              }
           },
           "deletion_protection": "disabled"
        }'
  ```
</CodeGroup>

## Prevent index deletion

<Note>
  This feature requires [Pinecone API version](/reference/api/versioning) `2024-07`, [Python SDK](/reference/sdks/python/overview) v5.0.0, [Node.js SDK](/reference/sdks/node/overview) v3.0.0, [Java SDK](/reference/sdks/java/overview) v2.0.0, or [Go SDK](/reference/sdks/go/overview) v1.0.0 or later.
</Note>

You can prevent an index and its data from accidental deleting when [creating a new index](/guides/index-data/create-an-index) or when [configuring an existing index](/guides/indexes/pods/manage-pod-based-indexes). In both cases, you set the `deletion_protection` parameter to `enabled`.

To enable deletion protection when creating a new index:

<CodeGroup>
  ```python Python theme={null}
  # pip install "pinecone[grpc]"
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
      deletion_protection="enabled"
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
    deletionProtection: 'enabled',
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
                  "p1.x1", "cosine", DeletionProtection.ENABLED);
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
           "deletion_protection": "enabled"
        }'
  ```
</CodeGroup>

To enable deletion protection when configuring an existing index:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
     name="docs-example", 
     deletion_protection="enabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await client.configureIndex('docs-example', { deletionProtection: 'enabled' });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.configurePodsIndex("docs-example", DeletionProtection.ENABLED);
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{DeletionProtection: "enabled"})
    	if err != nil {
          log.Fatalf("Failed to configure index \"%v\": %v", idx.Name, err)
      } else {
          fmt.Printf("Successfully configured index \"%v\"", idx.Name)
      }
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -d '{
          "deletion_protection": "enabled"
          }'
  ```
</CodeGroup>

When deletion protection is enabled on an index, requests to delete the index fail and return a `403 - FORBIDDEN` status with the following error:

```
Deletion protection is enabled for this index. Disable deletion protection before retrying.
```

## Disable deletion protection

Before you can [delete an index](#delete-a-pod-based-index) with deletion protection enabled, you must first disable deletion protection as follows:

<CodeGroup>
  ```python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index(
     name="docs-example", 
     deletion_protection="disabled"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const client = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await client.configureIndex('docs-example', { deletionProtection: 'disabled' });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          pc.configurePodsIndex("docs-example", DeletionProtection.DISABLED);
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{DeletionProtection: "disabled"})
    	if err != nil {
          log.Fatalf("Failed to configure index \"%v\": %v", idx.Name, err)
      } else {
          fmt.Printf("Successfully configured index \"%v\"", idx.Name)
      }
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -d '{
          "deletion_protection": "disabled"
          }'
  ```
</CodeGroup>

## Delete an entire namespace

In pod-based indexes, reads and writes share compute resources, so deleting an entire namespace with many records can increase the latency of read operations. In such cases, consider [deleting records in batches](#delete-records-in-batches).

## Delete records in batches

In pod-based indexes, reads and writes share compute resources, so deleting an entire namespace or a large number of records can increase the latency of read operations. To avoid this, delete records in batches of up to 1000, with a brief sleep between requests. Consider using smaller batches if the index has active read traffic.

<CodeGroup>
  ```python Batch delete a namespace theme={null}
  from pinecone import Pinecone
  import numpy as np
  import time

  pc = Pinecone(api_key='API_KEY')

  INDEX_NAME = 'INDEX_NAME'
  NAMESPACE = 'NAMESPACE_NAME'
  # Consider using smaller batches if you have a high RPS for read operations
  BATCH = 1000

  index = pc.Index(name=INDEX_NAME)
  dimensions = index.describe_index_stats()['dimension']

  # Create the query vector
  query_vector = np.random.uniform(-1, 1, size=dimensions).tolist()
  results = index.query(vector=query_vector, namespace=NAMESPACE, top_k=BATCH)

  # Delete in batches until the query returns no results
  while len(results['matches']) > 0:
      ids = [i['id'] for i in results['matches']]
      index.delete(ids=ids, namespace=NAMESPACE)
      time.sleep(0.01)
      results = index.query(vector=query_vector, namespace=NAMESPACE, top_k=BATCH)
  ```

  ```python Batch delete by metadata theme={null}
  from pinecone import Pinecone
  import numpy as np
  import time

  pc = Pinecone(api_key='API_KEY')

  INDEX_NAME = 'INDEX_NAME'
  NAMESPACE = 'NAMESPACE_NAME'
  # Consider using smaller batches if you have a high RPS for read operations
  BATCH = 1000

  index = pc.Index(name=INDEX_NAME)
  dimensions = index.describe_index_stats()['dimension']

  METADATA_FILTER = {}

  # Create the query vector with a filter
  query_vector = np.random.uniform(-1, 1, size=dimensions).tolist()
  results = index.query(vector=query_vector, namespace=NAMESPACE, filter=METADATA_FILTER, top_k=BATCH)

  # Delete in batches until the query returns no results
  while len(results['matches']) > 0:
      ids = [i['id'] for i in results['matches']]
      index.delete(ids=ids, namespace=NAMESPACE)
      time.sleep(0.01)
      results = index.query(vector=query_vector, namespace=NAMESPACE, filter=METADATA_FILTER, top_k=BATCH)
  ```
</CodeGroup>

## Delete records by metadata

<Note>
  In pod-based indexes, if you are targeting a large number of records for deletion and the index has active read traffic, consider [deleting records in batches](#delete-records-in-batches).
</Note>

To delete records from a namespace based on their metadata values, pass a [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) to the `delete` operation. This deletes all records in the namespace that match the filter expression.

For example, the following code deletes all records with a `genre` field set to `documentary` from namespace `example-namespace`:

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(
      filter={
          "genre": {"$eq": "documentary"}
      },
      namespace="example-namespace" 
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const ns = index.namespace('example-namespace')

  await ns.deleteMany({
    genre: { $eq: "documentary" },
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class DeleteExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          Struct filter = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder()
                          .setStructValue(Struct.newBuilder()
                                  .putFields("$eq", Value.newBuilder()
                                          .setStringValue("documentary")
                                          .build()))
                          .build())
                  .build();
          index.deleteByFilter(filter, "example-namespace");
          
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
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

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      metadataFilter := map[string]interface{}{
  		"genre": map[string]interface{}{
  			"$eq": "documentary",
  		},
      }

      filter, err := structpb.NewStruct(metadataFilter)
      if err != nil {
          log.Fatalf("Failed to create metadata filter: %v", err)
      }

      err = idxConnection.DeleteVectorsByFilter(ctx, filter)
      if err != nil {
          log.Fatalf("Failed to delete vector(s) with filter %+v: %v", filter, err)
      }
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -i "https://$INDEX_HOST/vectors/delete" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "filter": {"genre": {"$eq": "documentary"}},
      "namespace": "example-namespace"
    }'
  ```
</CodeGroup>

## Tag an index

When configuring an index, you can tag the index to help with index organization and management. For more details, see [Tag an index](/guides/manage-data/manage-indexes#configure-index-tags).

## Manage costs

### Set a project pod limit

To control costs, [project owners](/guides/projects/understanding-projects#project-roles) can [set the maximum total number of pods](/reference/api/database-limits#pods-per-project) allowed across all pod-based indexes in a project. The default pod limit is 5.

<Tabs>
  <Tab title="Pinecone console">
    1. Go to [Settings > Projects](https://app.pinecone.io/organizations/-/settings/projects).
    2. For the project you want to update, click the **ellipsis (...) menu > Configure**.
    3. In the **Pod Limit** section, update the number of pods.
    4. Click **Save Changes**.
  </Tab>

  <Tab title="API">
    <token />

    ```bash curl theme={null}
    PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
    PROJECT_ID="YOUR_PROJECT_ID"

    curl -X PATCH "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
      -H "accept: application/json" \
      -H "Content-Type: application/json" \
    	-H "X-Pinecone-Api-Version: 2025-10" \
      -d '{
        "max_pods": 5
        }'
    ```

    The example returns a response like the following:

    ```json theme={null}
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "example-project",
      "max_pods": 5,
      "force_encryption_with_cmek": false,
      "organization_id": "string",
      "created_at": "2025-03-17T00:42:31.912Z"
    }
    ```
  </Tab>
</Tabs>

### Back up inactive pod-based indexes

For each pod-based index, billing is determined by the per-minute price per pod and the number of pods the index uses, regardless of index activity. When a pod-based index is not in use, [back it up using collections](/guides/indexes/pods/back-up-a-pod-based-index) and delete the inactive index. When you're ready to use the vectors again, you can [create a new index from the collection](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection). This new index can also use a different index type or size. Because it's relatively cheap to store collections, you can reduce costs by only running an index when it's in use.

### Choose the right index type and size

Pod sizes are designed for different applications, and some are more expensive than others. [Choose the appropriate pod type and size](/guides/indexes/pods/choose-a-pod-type-and-size), so you pay for the resources you need. For example, the `s1` pod type provides large storage capacity and lower overall costs with slightly higher query latencies than `p1` pods. By switching to a different pod type, you may be able to reduce costs while still getting the performance your application needs.

<Note>
  For pod-based indexes, project owners can [set limits for the total number of pods](/reference/api/database-limits#pods-per-project) across all indexes in the project. The default pod limit is 5.
</Note>

## Monitor performance

Pinecone generates time-series performance metrics for each Pinecone index. You can monitor these metrics directly in the Pinecone console or with tools like Prometheus or Datadog.

### Use the Pinecone Console

To view performance metrics in the Pinecone console:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project containing the index you want to monitor.
3. Go to **Database > Indexes**.
4. Select the index.
5. Go to the **Metrics** tab.

### Use Datadog

To monitor Pinecone with Datadog, use Datadog's [Pinecone integration](/integrations/datadog).

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

### Use Prometheus

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/). When using [Bring Your Own Cloud](/guides/production/bring-your-own-cloud), you must configure Prometheus monitoring within your VPC.
</Note>

To monitor all pod-based indexes in a specific region of a project, insert the following snippet into the [`scrape_configs`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) section of your `prometheus.yml` file and update it with values for your Prometheus integration:

```YAML theme={null}
scrape_configs:
  - job_name: "pinecone-pod-metrics"
    scheme: https
    metrics_path: '/metrics'
    authorization:
      credentials: API_KEY
    static_configs:
      - targets: ["metrics.ENVIRONMENT.pinecone.io" ]
```

* Replace `API_KEY` with an API key for the project you want to monitor. If necessary, you can [create an new API key](/reference/api/authentication) in the Pinecone console.

* Replace `ENVIRONMENT` with the [environment](/guides/indexes/pods/understanding-pod-based-indexes#pod-environments) of the pod-based indexes you want to monitor.

For more configuration details, see the [Prometheus docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

#### Available metrics

The following metrics are available when you integrate Pinecone with Prometheus:

| Name                                 | Type      | Description                                                                       |
| :----------------------------------- | :-------- | :-------------------------------------------------------------------------------- |
| `pinecone_vector_count`              | gauge     | The number of records per pod in the index.                                       |
| `pinecone_request_count_total`       | counter   | The number of data plane calls made by clients.                                   |
| `pinecone_request_error_count_total` | counter   | The number of data plane calls made by clients that resulted in errors.           |
| `pinecone_request_latency_seconds`   | histogram | The distribution of server-side processing latency for pinecone data plane calls. |
| `pinecone_index_fullness`            | gauge     | The fullness of the index on a scale of 0 to 1.                                   |

#### Metric labels

Each metric contains the following labels:

| Label          | Description                                                                                                                                    |
| :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `pid`          | Process identifier.                                                                                                                            |
| `index_name`   | Name of the index to which the metric applies.                                                                                                 |
| `project_name` | Name of the project containing the index.                                                                                                      |
| `request_type` | Type of request: `upsert`, `delete`, `fetch`, `query`, or `describe_index_stats`. This label is included only in `pinecone_request_*` metrics. |

#### Example queries

Return the average latency in seconds for all requests against the Pinecone index `docs-example`:

```shell theme={null}
avg by (request_type) (pinecone_request_latency_seconds{index_name="docs-example"})
```

Return the vector count for the Pinecone index `docs-example`:

```shell theme={null}
sum ((avg by (app) (pinecone_vector_count{index_name="docs-example"})))
```

Return the total number of requests against the Pinecone index `docs-example` over one minute:

```shell theme={null}
sum by (request_type)(increase(pinecone_request_count_total{index_name="docs-example"}[60s]))
```

Return the total number of upsert requests against the Pinecone index `docs-example` over one minute:

```shell theme={null}
sum by (request_type)(increase(pinecone_request_count_total{index_name="docs-example", request_type="upsert"}[60s]))
```

Return the total errors returned by the Pinecone index `docs-example` over one minute:

```shell theme={null}
sum by (request_type) (increase(pinecone_request_error_count{
      index_name="docs-example"}[60s]))
```

Return the index fullness metric for the Pinecone index `docs-example`:

```
round(max (pinecone_index_fullness{index_name="docs-example"} * 100))
```

## Troubleshooting

### Index fullness errors

Serverless indexes automatically scale as needed.

However, pod-based indexes can run out of capacity. When that happens, upserting new records will fail with the following error:

```console console theme={null}
Index is full, cannot accept data.
```

### High-cardinality metadata and over-provisioning

This [Loom video walkthrough](https://www.loom.com/share/ce6f5dd0c3e14ba0b988fe32d96b703a?sid=48646dfe-c10c-4143-82c6-031fefe05a68) shows you how to manage two scenarios:

* The first scenario involves customers loading an index replete with high cardinality metadata. This can trigger a series of unforeseen challenges, and hence, it's vital to comprehend how to manage this situation effectively. This methodology can be applied whenever you need to change your metadata configuration.

* The second scenario that we will address involves customers who have over-provisioned the number of pods they need. More specifically, we will discuss the process of re-scaling an index in instances where the customer has previously scaled vertically and now desires to scale the index back down.
