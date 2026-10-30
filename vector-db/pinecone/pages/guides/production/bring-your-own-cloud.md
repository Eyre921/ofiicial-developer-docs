---
title: "Bring Your Own Cloud (BYOC) overview"
source: https://docs.pinecone.io/guides/production/bring-your-own-cloud
path: guides/production/bring-your-own-cloud
---

Deploy Pinecone BYOC in your own AWS, GCP, or Azure account for data sovereignty, network isolation, and regional data residency requirements.

Pinecone BYOC (Bring Your Own Cloud) is designed for organizations with strict requirements around data sovereignty, network isolation, and data residency.

With BYOC, you deploy the Pinecone data plane in your own cloud account (AWS, GCP, or Azure), and you get the benefits of a managed service — upgrades, scaling, and maintenance — without giving up control of your data or infrastructure.

Pinecone never has direct access to your cloud account. Your vectors, metadata, and queries never leave your environment, and no inbound network access is required. An agent in your cluster pulls operations from Pinecone and executes them locally.

## Architecture

![BYOC architecture in which the Pinecone data plane, Kubernetes cluster, FoundationDB, object storage, and DNS run in a VPC in your AWS, GCP, or Azure account. The cluster pulls operations from the Pinecone-managed control plane, and only metrics and traces leave the cluster.](https://mintcdn.com/pinecone/ZVOnQqdJdQzJQn6W/images/byoc-architecture-light.svg?fit=max\&auto=format\&n=ZVOnQqdJdQzJQn6W\&q=85\&s=d94db2a849aca635dfb739d339edb48d)

BYOC uses a split architecture:

* The data plane runs entirely in your cloud account within a dedicated VPC, storing and processing your vectors, executing queries, and managing index data in object storage (S3 on AWS, GCS on GCP, or Azure Blob Storage on Azure). Cluster metadata lives in FoundationDB, which runs inside your Kubernetes cluster, so there's no managed database to operate.
* The control plane is managed by Pinecone globally and handles index lifecycle management, authentication, billing, and user management, but never stores or processes your vectors.

For maintenance, the agent authenticates with Pinecone's control plane, pulls pending operations (upgrades, scaling, etc.), and executes them locally. All operations are stored as Kubernetes CRDs, providing a complete audit trail.

Only operational metrics (CPU, memory, latency) and traces are transmitted to Pinecone for monitoring; customer data is filtered out before transmission.

## Encryption and customer-managed keys

In the standard Pinecone service, [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) are how you connect Pinecone-managed storage to *your* AWS KMS keys through the Pinecone console.

In BYOC, that console CMEK flow doesn't apply. Your vectors and index data are stored in *your* cloud account (for example, object storage and block storage), so you apply your cloud provider’s KMS to those resources using the same native controls you use for other workloads (key policies, rotation, and compliance programs such as PCI or ISO 27001). When you deploy with pulumi-pinecone-byoc, you can supply your KMS key where the template supports it. For the current options, see the [pulumi-pinecone-byoc README](https://github.com/pinecone-io/pulumi-pinecone-byoc).

## Limitations

Some features available in the standard Pinecone service aren't supported or have constraints in BYOC:

* Each organization can have up to 2 BYOC environments. To request an increase, contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).
* [Integrated embedding and inference](/guides/index-data/indexing-overview#integrated-embedding) isn't supported, because it relies on models Pinecone hosts outside your cloud account.
* You can't read or write data from the index browser in the Pinecone console.
* The Pinecone CLI can't run data plane operations (queries, upserts, fetches), though its control plane operations (create, list, delete indexes) work as expected.
* You can't import from private cloud storage buckets unless the bucket is in the same cloud account as your BYOC deployment.
* On-demand indexes in an environment share the pool, so per-index rate limits prevent a busy index from slowing down the others. If one index needs more capacity than the pool can share, create it as a dedicated read nodes index.

To [monitor with Prometheus](/guides/production/monitoring#monitor-with-prometheus), you must configure Prometheus within your VPC.

## Pricing

Your Pinecone bill for a BYOC environment has two parts: a flat platform fee, and a rate for each node you run, across both the shared on-demand pool and your dedicated read nodes indexes. Separately, you pay your cloud provider directly for the underlying infrastructure (Kubernetes nodes, object storage, block storage, networking, etc.).

```
Pinecone bill = platform fee + (node rate × number of nodes)
```

| Term | Description |
| :- | :- |
| **Platform fee** | Flat monthly fee for each BYOC environment. Covers the always-on Pinecone components that serve writes and control operations, plus support. |
| **Node rate** | Monthly rate for each node running in your cluster, metered in node hours. It applies to the nodes of the on-demand pool (`od1`) and to the [dedicated read nodes](/guides/index-data/dedicated-read-nodes/concepts#node-types) of your dedicated read nodes indexes (`b1` or `t1`). The rate varies by node type. Unlike the standard service, it's the same in every cloud and region. |
| **Number of nodes** | The nodes in the on-demand pool, plus the sum of [shards](/guides/index-data/dedicated-read-nodes/concepts#shards) × [replicas](/guides/index-data/dedicated-read-nodes/concepts#replicas) across every dedicated read nodes index in the environment. Counted separately for each node type. |

If an environment runs more than one node type, calculate the node cost for each type and add the results.

The on-demand pool starts with two `od1` nodes and is billed whether or not you create on-demand indexes. Creating on-demand indexes doesn't add nodes, because they share the pool, so you pay for more `od1` nodes only when the pool grows beyond its capacity. Each dedicated read nodes index adds its `shards × replicas`.

Unlike [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview#cost) in the standard service, BYOC has no separate Pinecone charges for storage or writes. That data lives in your own cloud account, so you pay your cloud provider for it instead of Pinecone.

> [!TIP]
>
> For current rates and help sizing your BYOC environment, [contact us](https://www.pinecone.io/contact/).

### Example

An environment with one dedicated read nodes index using two shards and two replicas runs four `b1` nodes in addition to the on-demand pool, which starts with two nodes. Its monthly bill is the platform fee, plus four times the `b1` node rate, plus two times the `od1` node rate (the starting pool), plus what you pay your cloud provider. Adding on-demand indexes to that environment doesn't change the bill until the pool needs more nodes.

### Metering and billing

The Pinecone BYOC agent running in your cluster measures node usage, periodically reporting which nodes are provisioned. Billing follows the agent heartbeat connection to Pinecone's control plane:

* When Pinecone receives heartbeats, you're billed for the nodes the agent reports, even if the cluster is unhealthy.
* Short heartbeat interruptions (under 60 minutes) are treated as a grace period.
* If heartbeats are missing for more than 60 minutes, billing stops and the deployment is marked disconnected.

> [!NOTE]
>
> Pinecone bills for provisioned nodes, not query volume. You're billed for nodes running in your cluster, including the on-demand pool, whether they're idle, actively processing queries, or experiencing errors.

## FAQs

Answers to common questions about BYOC:

> [accordion] Does Pinecone have access to my cloud account?
>
> No. BYOC uses a zero-access model, so Pinecone never needs direct access to your infrastructure. Specifically:
>
> * Pinecone does not need SSH, VPN, inbound access, or a standing cross-account role in your cloud account.
> * You control cloud account boundaries, networking, and Kubernetes access.
> * Operational changes run through explicit, software-mediated workflows.
> * You don't open inbound firewall ports for Pinecone operations.
>
> Operations are executed via a pull-based model where your cluster retrieves and runs operations locally. All communication is outbound from your cluster. Pinecone monitors cluster health through operational metrics such as CPU and latency, without seeing your data. You choose what logs to share with [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).

> [accordion] What is the difference between on-demand and dedicated read nodes in BYOC?
>
> On-demand indexes share one pool of nodes that starts with two `od1` nodes, and Pinecone adds nodes when you need more capacity. Each dedicated read nodes index gets its own nodes. For how the two modes differ, see [On-demand vs. dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview#on-demand-vs-dedicated-read-nodes).

> [accordion] Can I use on-demand indexes in an existing BYOC environment?
>
> Yes. On-demand is available in new and existing BYOC environments on AWS, GCP, and Azure. If on-demand isn't available in your environment, contact your Pinecone account team to enable it.

> [accordion] What data leaves my cluster?
>
> **Does not leave your cloud account:**
>
> * Vectors, metadata, and index contents
> * Query and upsert payloads
> * Customer data
>
> **Can leave your cloud account:**
>
> * Operational metrics and traces (for example, CPU, memory, latency)
> * Cluster health and operation status
>
> Customer data is filtered out before transmission and never leaves your cloud account.

> [accordion] What is the difference between BYOC and Pinecone's standard service?
>
> In the standard service, Pinecone manages all cloud resources and includes their cost in the service fee. In BYOC, you provision and pay for cloud resources directly through your own cloud account, providing greater control, data sovereignty, and access to available cloud credits or discounts. For a cost breakdown, see [Pricing](#pricing).

> [accordion] How does authentication work?
>
> You use API keys from the Pinecone console, just like with the standard Pinecone service. Authentication is handled by Pinecone's global control plane, and your data plane caches API keys locally. This means you manage users and API keys through the console as usual.

> [accordion] How is data secured in BYOC?
>
> Data is stored and processed exclusively within your cloud account, with encryption at rest and in transit. You control at-rest encryption for the underlying resources (including KMS keys in your account) the same way you do for other infrastructure. Communication between the data plane and control plane is encrypted using TLS. Private connectivity (AWS PrivateLink, GCP Private Service Connect, or Azure Private Link) can be used for additional network isolation. For how this relates to hosted [CMEK](/guides/production/configure-cmek), see [Encryption and customer-managed keys](#encryption-and-customer-managed-keys).

> [accordion] Which cloud providers does BYOC support?
>
> BYOC is available on AWS, GCP, and Azure.

> [accordion] What happens if I destroy the cluster before deleting indexes?
>
> Indexes cannot be properly terminated if the cluster is destroyed first. Always delete indexes via the Pinecone API or console before running `pulumi destroy`.

> [accordion] What is the **SLI** project in my organization?
>
> Deploying a BYOC environment creates an internal project named `__SLI__` in your organization. This is used by Pinecone to enforce SLAs for your BYOC environment. Do not modify or delete this project.

## Next steps

* [Deploy BYOC](/guides/production/bring-your-own-cloud/deploy)
