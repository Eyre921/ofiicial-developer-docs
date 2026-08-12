---
title: "Scale pod-based indexes"
source: https://docs.pinecone.io/guides/indexes/pods/scale-pod-based-indexes
path: guides/indexes/pods/scale-pod-based-indexes
---

Scale Pinecone pod-based indexes by adding pods or replicas. Legacy guide: pod indexes are unavailable to new customers; serverless scales automatically.

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

While your index can still serve queries, new upserts may fail as the capacity becomes exhausted. If you need to scale your environment to accommodate more vectors, you can modify your existing index and scale it vertically or create a new index and scale horizontally.

This page explains how you can scale your [pod-based indexes](/guides/index-data/indexing-overview#pod-based-indexes) horizontally and vertically.

## Vertical vs. horizontal scaling

If you need to scale your environment to accommodate more vectors, you can modify your existing index to scale it vertically or create a new index and scale horizontally. This article will describe both methods and how to scale your index effectively.

## Vertical scaling

[Vertical scaling](https://www.pinecone.io/learn/testing-p2-collections-scaling/#vertical-scaling-on-p1-and-s1) is fast and involves no downtime. This is a good choice when you can't pause upserts and must continue serving traffic. It also allows you to double your capacity instantly. However, there are some factors to consider.

### Increase pod size

The default [pod size](/guides/index-data/indexing-overview#pod-size-and-performance) is `x1`. You can increase the size to `x2`, `x4`, or `x8`. Moving up to the next size effectively doubles the capacity of the index. If you need to scale by smaller increments, then consider horizontal scaling.

Increasing the pod size of your index does not result in downtime. Reads and writes continue uninterrupted during the scaling process, which completes in about 10 minutes. You cannot reduce the pod size of your indexes.

The number of base pods you specify when you initially create the index is static and cannot be changed. For example, if you start with 10 pods of `p1.x1` and vertically scale to `p1.x2`, this equates to 20 pods worth of usage. Pod types (performance versus storage pods) also cannot be changed with vertical scaling. If you want to change your pod type while scaling, then horizontal scaling is the better option.

#### When to increase pod size

If your index is at around 90% fullness, we recommend increasing its size. This helps ensure optimal performance and prevents upserts from failing due to capacity constraints.

#### How to increase pod size

You can increase the pod size in the Pinecone console or using the API.

<Tabs>
  <Tab title="Console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index you want to configure.
    3. Go to **Database > Indexes**.
    4. Select the index.
    5. Click the **...** button.
    6. Select **Configure**.
    7. In the dropdown, choose the pod size to use.
    8. Click **Confirm**.
  </Tab>

  <Tab title="API">
    Use the [`configure_index`](/reference/api/latest/control-plane/configure_index) operation and append the new size to the `pod_type` parameter, separated by a period (.).

    **Example**

    The following example assumes that `docs-example` has size `x1` and increases the size to `x2`.

    <CodeGroup>
      ```Python Python theme={null}
      from pinecone.grpc import PineconeGRPC as Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      pc.configure_index("docs-example", pod_type="s1.x2")
      ```

      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone'

      const pinecone = new Pinecone({
        apiKey: 'YOUR_API_KEY'
      });

      await pc.configureIndex('docs-example', {
        spec: {
          pod: {
            podType: 's1.x2',
          },
        },
      });
      ```

      ```java Java theme={null}
      import io.pinecone.clients.Pinecone;

      public class ConfigureIndexExample {
          public static void main(String[] args) {
              Pinecone pc = new Pinecone.Builder("PINECONE_API_KEY").build();
              pc.configurePodsIndex("docs-example", "s1.x2");
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

          idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{PodType: "s1.x2"})
        	if err != nil {
              log.Fatalf("Failed to configure index \"%v\": %v", idx.Name, err)
          } else {
              fmt.Printf("Successfully configured index \"%v\"", idx.Name)
          }
      }
      ```

      ```bash curl theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
        -H "Content-Type: application/json" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H "X-Pinecone-Api-Version: 2025-10" \
        -d '{
               "pod_type": "s1.x2"
            }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  The size change can take up to 15 minutes to complete.
</Note>

### Decrease pod size

After creating an index, you cannot vertically downscale the index/pod size. Instead, you must [create a collection](/guides/indexes/pods/back-up-a-pod-based-index) and then [create a new index from your collection](/guides/indexes/pods/restore-a-pod-based-index) and specify your desired pod size.

### Check the status of a pod size change

To check the status of a pod size change, use the [`describe_index`](/reference/api/latest/control-plane/describe_index/) endpoint. The `status` field in the results contains the key-value pair `"state":"ScalingUp"` or `"state":"ScalingDown"` during the resizing process and the key-value pair `"state":"Ready"` after the process is complete.

The index fullness metric provided by [`describe_index_stats`](/reference/api/latest/data-plane/describeindexstats) may be inaccurate until the resizing process is complete.

**Example**

The following example uses `describe_index` to get the index status of the index `docs-example`. The `status` field contains the key-value pair `"state":"ScalingUp"`, indicating that the resizing process is still ongoing.

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.describe_index(name="docs-example")
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.describeIndex({
    name: "docs-example",
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.*;

  public class DescribeIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          IndexModel indexModel = pc.describeIndex("docs-example");
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

      idx, err := pc.DescribeIndex(ctx, "docs-example")
    	if err != nil {
          log.Fatalf("Failed to describe index %v: %v", idx.Name, err)
      } else {
          fmt.Printf("Successfully found index: %v", idx.Name)
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X GET "https://api.pinecone.io/indexes/docs-example-curl" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

## Horizontal scaling

There are two approaches to horizontal scaling in Pinecone: adding pods and adding replicas. Adding pods increases all resources but requires a pause in upserts; adding replicas only increases throughput and requires no pause in upserts.

### Add pods

Adding additional pods to a running index is not supported directly. However, you can increase the number of pods by using our [collections](/guides/indexes/pods/understanding-collections) feature to create a new index with more pods.

A collection is an immutable snapshot of your index in time: a collection stores the data but not the original index configuration. When you [create an index from a collection](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection), you define the new index configuration. This allows you to scale the base pod count horizontally without scaling vertically.

The main advantage of this approach is that you can scale incrementally instead of doubling capacity as with vertical scaling. Also, you can redefine pod types if you are experimenting or if you need to use a different pod type, such as performance-optimized pods or storage-optimized pods. Another advantage of this method is that you can change your [metadata configuration](/guides/indexes/pods/manage-pod-based-indexes#selective-metadata-indexing) to redefine metadata fields as indexed or stored-only. This is important when tuning your index for the best throughput.

Here are the general steps to make a copy of your index and create a new index while changing the pod type, pod count, metadata configuration, replicas, and all typical parameters when creating a new collection:

1. Pause upserts.
2. Create a collection from the current index.
3. Create an index from the collection with new parameters.
4. Continue upserts to the newly created index. Note: the URL has likely changed.
5. Delete the old index if desired.

For detailed steps on creating the collection, see [backup indexes](/guides/manage-data/back-up-an-index#create-a-backup-using-a-collection). For steps on creating an index from a collection, see [Create an index from a collection](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection).

### Add replicas

Each replica duplicates the resources and data in an index. This means that adding additional replicas increases the throughput of the index but not its capacity. However, adding replicas does not require downtime.

Throughput in terms of queries per second (QPS) scales linearly with the number of replicas per index.

#### When to add replicas

There are two primary scenarios where adding replicas is beneficial:

**Increase QPS**: The primary reason to add replicas is to increase your index's queries per second (QPS). Each new replica adds another pod for reading from your index and, generally speaking, will increase your QPS by an equal amount as a single pod. For example, if you consistently get 25 QPS for a single pod, each replica will result in 25 more QPS.

If you don't see an increase in QPS after adding replicas, add multiprocessing to your application to ensure you are running parallel operations. You can use the [Pinecone gRPC SDK](/guides/index-data/upsert-data#grpc-python-sdk), or your multiprocessing library of choice.

**Provide data redundancy**: When you add a replica to your index, the Pinecone controller will choose a zone in the same region that does not currently have a replica, up to a maximum of three zones (your fourth and subsequent replicas will be hosted in zones with existing replicas). If your application requires multizone redundancy, this is our recommended approach to achieve that.

#### How to add replicas

To add replicas, use the `configure_index` endpoint to increase the number of replicas for your index:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.configure_index("docs-example", replicas=4)
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
  });

  await pc.configureIndex('docs-example', {
    spec: {
      pod: {
        replicas: 4,
      },
    },
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class ConfigureIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("PINECONE_API_KEY").build();
          pc.configurePodsIndex("docs-example", 4, DeletionProtection.DISABLED);
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

      idx, err := pc.ConfigureIndex(ctx, "docs-example", pinecone.ConfigureIndexParams{Replicas: 4})
    	if err != nil {
          log.Fatalf("Failed to configure index \"%v\": %v", idx.Name, err)
      } else {
          fmt.Printf("Successfully configured index \"%v\"", idx.Name)
      }
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s -X PATCH "https://api.pinecone.io/indexes/docs-example-curl" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
           "replicas": 4
        }'
  ```
</CodeGroup>

## Next steps

* See our learning center for more information on [vertical scaling](https://www.pinecone.io/learn/testing-p2-collections-scaling/#vertical-scaling-on-p1-and-s1).
* Learn more about [collections](/guides/indexes/pods/understanding-collections).
