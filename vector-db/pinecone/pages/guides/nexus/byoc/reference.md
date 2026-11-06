---
title: "Nexus BYOC data residency and limits"
source: https://docs.pinecone.io/guides/nexus/byoc/reference
path: guides/nexus/byoc/reference
---

See where your data lives and travels in Nexus BYOC, plus its authentication, encryption, cluster footprint, and limitations.

> [!NOTE]
>
> Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).

This page covers where your Nexus BYOC data stays and where it travels, how you authenticate and encrypt it, the cluster's footprint, and current limitations.

## Data flows and residency

Nexus BYOC keeps your data at rest in your cloud account. Like any system that calls a language model, though, it sends the content it's processing to the model that serves each request, so understand these flows before you make residency or compliance commitments.

### Data at rest

These stay in object storage and databases inside your virtual network:

* Your uploaded sources
* The chunks and artifacts compiled from them
* The indexes behind your contexts, and the Nexus metadata store

### Data that leaves your account

* **Pinecone control plane and observability:** Operational metrics (such as CPU, memory, and latency), traces, and cluster and operation status. Customer data is filtered out before it's sent.
* **Inference models you configure:** The content being processed. During curation, Nexus sends source text to the embedding model, and to the generation model for artifact generation. During a query, it sends the query text to the embedding model, the query text and retrieved passages to the generation model, and candidate passages to the rerank model. Each call carries that content to whichever provider serves the model.

With the shipped defaults, generation runs on a provider you bring (Google Gemini, with your key), so source text, query text, and retrieved passages go to that provider. Embedding and rerank run on Pinecone-hosted models, so the text being embedded or reranked goes to Pinecone.

You choose the provider for generation, embedding, and rerank independently. To keep all customer content inside your trust boundary, point each one at a model you host or control. A residency-strict deployment doesn't need any Pinecone-hosted or third-party model.

> [!WARNING]
>
> This differs from [Database BYOC](/guides/production/bring-your-own-cloud), where [integrated embedding](/guides/production/bring-your-own-cloud#limitations) is unsupported specifically so that document text never leaves your account. Nexus always performs an embedding step, so by default some document and query text is sent to Pinecone.

## Authentication and access

You authenticate to a BYOC deployment with Pinecone API keys. Nexus has no separate user model. Identity is delegated to Pinecone, and the tenancy boundary is the Pinecone project behind the workspace. Manage users and API keys in the Pinecone console.

## Encryption and customer-managed keys

Your data (sources, compiled knowledge, index contents, and the metadata store) lives on object storage, databases, and block volumes in your cloud account. You encrypt it with your cloud provider's KMS, using the same key policies, rotation, and compliance programs (such as PCI or ISO 27001) you use for other workloads. On AWS, the setup wizard also accepts your own KMS key (`kms-key-arn`) to encrypt S3 and RDS. GCP and Azure deployments don't support supplying your own key.

This isn't the console's [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) flow for hosted Pinecone projects. For how the two relate, see [Encryption and customer-managed keys](/guides/production/bring-your-own-cloud#encryption-and-customer-managed-keys) on the Database BYOC page.

## Cluster footprint

Nexus BYOC runs a Kubernetes cluster with several dedicated node pools spread over three availability zones (AZs):

| Node pool | Purpose |
| - | - |
| Pinecone Database | The data plane, including query routing and index builds |
| Metadata store | Stores Nexus metadata, backed by FoundationDB |
| Nexus services | The curation and query runtimes and their workflow jobs |
| [Dedicated read nodes](/guides/optimize/dedicated-read-nodes/overview) | Scale from zero as read demand grows |

The cluster starts small and autoscales with load and with the number of contexts and indexes. Node counts and instance types change between releases, so size your cloud quotas from the installer's preflight quota checks in [Deploy Nexus BYOC](/guides/nexus/byoc/deploy), not from a fixed node count.

## Limitations

* **Endpoint:** The Nexus API and console use a public endpoint that requires authentication. Private-only access (PrivateLink, Private Service Connect, or Private Endpoint) isn't supported for Nexus, although the Pinecone Database data plane in the same deployment can run privately.
* **Domain and TLS:** The endpoint uses a Pinecone-managed domain (`.byoc.pinecone.io`), and its certificates are issued and renewed automatically. Custom domains aren't supported, so you don't need to delegate DNS or hand off certificates.
* **Models:** You choose the generation, embedding, and rerank models, and a generation-model key is required (Google Gemini by default). Provider quota is your responsibility, so size it to your ingest volume. Your model choices determine where content is sent, as [Data flows and residency](#data-flows-and-residency) describes.
* **Workspace names:** Workspace names are unique per Pinecone project. When several deployments share one project, give each additional deployment its own workspace name with `nexus-default-workspace-name`.
* **Environments:** Each organization can create a limited number of BYOC environments. To request more, contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).

To install, see [Deploy Nexus BYOC](/guides/nexus/byoc/deploy).
