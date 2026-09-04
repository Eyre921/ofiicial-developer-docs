---
title: "Understanding pod-based indexes"
source: https://docs.pinecone.io/guides/indexes/pods/understanding-pod-based-indexes
path: guides/indexes/pods/understanding-pod-based-indexes
---

Understand Pinecone pod-based indexes, including pod types and sizing. Legacy: pod indexes are unavailable to new customers; use serverless for new projects.

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

With pod-based indexes, you choose one or more pre-configured units of hardware (pods). Depending on the pod type, pod size, and number of pods used, you get different amounts of storage and higher or lower latency and throughput. Be sure to [choose an appropriate pod type and size](/guides/indexes/pods/choose-a-pod-type-and-size) for your dataset and workload.

## Pod types

Different pod types are priced differently. See [Understanding cost](/guides/manage-cost/understanding-cost) for more details.

<Note>
  Once a pod-based index is created, you cannot change its pod type. However, you can create a collection from an index and then [create a new index with a different pod type](/guides/indexes/pods/create-a-pod-based-index#create-a-pod-index-from-a-collection) from the collection.
</Note>

### s1 pods

These storage-optimized pods provide large storage capacity and lower overall costs with slightly higher query latencies than p1 pods. They are ideal for very large indexes with moderate or relaxed latency requirements.

Each s1 pod has enough capacity for around 5M vectors of 768 dimensions.

### p1 pods

These performance-optimized pods provide very low query latencies, but hold fewer vectors per pod than s1 pods. They are ideal for applications with low latency requirements (\<100ms).

Each p1 pod has enough capacity for around 1M vectors of 768 dimensions.

### p2 pods

The p2 pod type provides greater query throughput with lower latency. For vectors with fewer than 128 dimension and queries where `topK` is less than 50, p2 pods support up to 200 QPS per replica and return queries in less than 10ms. This means that query throughput and latency are better than s1 and p1.

Each p2 pod has enough capacity for around 1M vectors of 768 dimensions. However, capacity may vary with dimensionality.

The data ingestion rate for p2 pods is significantly slower than for p1 pods; this rate decreases as the number of dimensions increases. For example, a p2 pod containing vectors with 128 dimensions can upsert up to 300 updates per second; a p2 pod containing vectors with 768 dimensions or more supports upsert of 50 updates per second. Because query latency and throughput for p2 pods vary from p1 pods, test p2 pod performance with your dataset.

The p2 pod type does not support sparse vector values.

## Pod size and performance

Each pod type supports four pod sizes: `x1`, `x2`, `x4`, and `x8`. Your index storage and compute capacity doubles for each size step. The default pod size is `x1`. You can increase the size of a pod after index creation.

To learn about changing the pod size of an index, see [Configure an index](/guides/indexes/pods/scale-pod-based-indexes#increase-pod-size).

## Pod environments

When creating a pod-based index, you must choose the cloud environment where you want the index to be hosted. The project environment can affect your [pricing](https://pinecone.io/pricing). The following table lists the available cloud regions and the corresponding values of the `environment` parameter for the [`create_index`](/guides/index-data/create-an-index#create-a-pod-based-index) endpoint:

| Cloud | Region                       | Environment                   |
| ----- | ---------------------------- | ----------------------------- |
| GCP   | us-west-1 (N. California)    | `us-west1-gcp`                |
| GCP   | us-central-1 (Iowa)          | `us-central1-gcp`             |
| GCP   | us-west-4 (Las Vegas)        | `us-west4-gcp`                |
| GCP   | us-east-4 (Virginia)         | `us-east4-gcp`                |
| GCP   | northamerica-northeast-1     | `northamerica-northeast1-gcp` |
| GCP   | asia-northeast-1 (Japan)     | `asia-northeast1-gcp`         |
| GCP   | asia-southeast-1 (Singapore) | `asia-southeast1-gcp`         |
| GCP   | us-east-1 (South Carolina)   | `us-east1-gcp`                |
| GCP   | eu-west-1 (Belgium)          | `eu-west1-gcp`                |
| GCP   | eu-west-4 (Netherlands)      | `eu-west4-gcp`                |
| AWS   | us-east-1 (Virginia)         | `us-east-1-aws`               |
| Azure | eastus (Virginia)            | `eastus-azure`                |

[Contact us](http://www.pinecone.io/contact/) if you need a dedicated deployment in other regions.

The environment cannot be changed after the index is created.

## Pod costs

For each pod-based index, billing is determined by the per-minute price per pod and the number of pods the index uses, regardless of index activity. The per-minute price varies by pod type, pod size, account plan, and cloud region. For the latest pod-based index pricing rates, see [Pricing](https://www.pinecone.io/pricing/pods).

Total cost depends on a combination of factors:

* **Pod type.** Each pod type has different per-minute pricing.
* **Number of pods.** This includes replicas, which duplicate pods.
* **Pod size.**  Larger pod sizes have proportionally higher costs per minute.
* **Total pod-minutes.** This includes the total time each pod is running, starting at pod creation and rounded up to 15-minute increments.
* **Cloud provider.** The cost per pod-type and pod-minute varies depending on the cloud provider you choose for your project.
* **Collection storage.** Collections incur costs per GB of data per minute in storage, rounded up to 15-minute increments.
* **Plan.** The free plan incurs no costs; the Standard or Enterprise plans incur different costs per pod-type, pod-minute, cloud provider, and collection storage.

The following equation calculates the total costs accrued over time:

```
(Number of pods) * (pod size) * (number of replicas) * (minutes pod exists) * (pod price per minute) 
+ (collection storage in GB) * (collection storage time in minutes) * (collection storage price per GB per minute)
```

To see a calculation of your current usage and costs, go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.

<Accordion title="Example">
  While our pricing page lists rates on an hourly basis for ease of comparison, this example lists prices per minute, as this is how Pinecone calculates billing.

  An example application has the following requirements:

  * 1,000,000 vectors with 1536 dimensions
  * 150 queries per second with `top_k` = 10
  * Deployment in an EU region
  * Ability to store 1GB of inactive vectors

  [Based on these requirements](/guides/indexes/pods/choose-a-pod-type-and-size), the organization chooses to configure the project to use the Standard billing plan to host one `p1.x2` pod with three replicas and a collection containing 1 GB of data. This project runs continuously for the month of January on the Standard plan. The components of the total cost for this example are given in Table 1 below:

  **Table 1: Example billing components**

  | Billing component             | Value        |
  | ----------------------------- | ------------ |
  | Number of pods                | 1            |
  | Number of replicas            | 3            |
  | Pod size                      | x2           |
  | Total pod count               | 6            |
  | Minutes in January            | 44,640       |
  | Pod-minutes (pods \* minutes) | 267,840      |
  | Pod price per minute          | \$0.0012     |
  | Collection storage            | 1 GB         |
  | Collection storage minutes    | 44,640       |
  | Price per storage minute      | \$0.00000056 |

  The invoice for this example is given in Table 2 below:

  **Table 2: Example invoice**

  | Product       | Quantity | Price per unit | Charge   |
  | ------------- | -------- | -------------- | -------- |
  | Collections   | 44,640   | \$0.00000056   | \$0.025  |
  | P2 Pods (AWS) | 0        |                | \$0.00   |
  | P2 Pods (GCP) | 0        |                | \$0.00   |
  | S1 Pods       | 0        |                | \$0.00   |
  | P1 Pods       | 267,840  | \$0.0012       | \$514.29 |

  Amount due \$514.54
</Accordion>

## Known limitations

* [Pod storage capacity](#pod-types)
  * Each **p1** pod has enough capacity for 1M vectors with 768 dimensions.
  * Each **s1** pod has enough capacity for 5M vectors with 768 dimensions.
* [Metadata](/guides/index-data/indexing-overview#metadata)
  * Metadata with high cardinality, such as a unique value for every vector in a large index, uses more memory than expected and can cause the pods to become full.
* [Collections](/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections)
  * You cannot query or write to a collection after its creation. For this reason, a collection only incurs storage costs.
  * You can only perform operations on collections in the current Pinecone project.
* [Sparse-dense vectors](/guides/search/hybrid-search/single-index)
  * Only `s1` and `p1` [pod-based indexes](/guides/indexes/pods/understanding-pod-based-indexes#pod-types) using the dotproduct distance metric support sparse-dense vectors.
