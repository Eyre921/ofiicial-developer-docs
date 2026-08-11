---
title: "Data residency and limits"
source: https://docs.pinecone.io/guides/nexus/byoc/reference
path: guides/nexus/byoc/reference
---

Where your data lives and travels in Nexus BYOC, plus authentication, encryption, cluster footprint, and limitations.

<Note>
  Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

The security and operational details of a Nexus BYOC deployment: where your data stays and where it travels, how you authenticate and encrypt it, the cluster footprint, and the current limitations. For what BYOC is and how it is architected, see the [Nexus BYOC overview](/guides/nexus/byoc/overview).

## Data flows and residency

Nexus BYOC keeps your data at rest in your account, but, like any system that calls a language model, it must send the content being processed to whatever model serves each request. Understand this before making residency or compliance commitments.

**Stays in your cloud account (at rest):**

* Your uploaded sources.
* The compiled knowledge built from them: chunks and derived artifacts.
* The indexes that back your contexts and the Nexus metadata store.

These live in your object storage, database, and metadata store, inside your virtual network.

**Leaves your account, and where it goes:**

* **To Pinecone (control plane and observability):** operational metrics, traces, and cluster and operation status (for example, CPU, memory, and latency). *No customer content.* Customer data is filtered out before transmission.
* **To the inference models you configure:** the content being processed. Nexus calls models during curation (embedding your source text, and for artifact generation sending source text to the generation model) and during a query (sending the query text and the retrieved passages to the generation model, the query text to the embedding model, and candidate passages to the rerank model). Each such call carries that content to whichever provider serves the model:
  * With the shipped defaults, the generation model is an external provider you bring (Google Gemini by default, using your key), so source text (during artifact generation) and query text plus retrieved passages go to that provider. Embedding and rerank run on Pinecone-hosted models, so the text being embedded or reranked is sent to Pinecone.
  * **Every model is BYOM and configurable.** You choose the provider (and therefore the destination) for the generation, embedding, and rerank tiers independently. To keep all customer content inside your trust boundary, repoint each tier at a model you host or otherwise control. A residency-strict deployment does not have to use any Pinecone-hosted or third-party model.

<Warning>
  This differs from [Database BYOC](/guides/production/bring-your-own-cloud), where [integrated embedding](/guides/production/bring-your-own-cloud#limitations) is unsupported specifically so that document text never leaves your account. Nexus always performs an embedding step, so by default some document and query text is sent to Pinecone.
</Warning>

## Authentication and access

You authenticate to a BYOC deployment with Pinecone API keys. Nexus has no separate user model. Identity is delegated to Pinecone, and the tenancy boundary is the Pinecone project behind the workspace. Manage users and API keys in the Pinecone console.

## Encryption and customer-managed keys

In BYOC, your data (sources, compiled knowledge, index contents, and the metadata store) is stored in your cloud account, on object storage, databases, and block volumes you own. You apply your cloud provider's KMS to those resources using the same native controls you use for other workloads: key policies, rotation, and compliance programs such as PCI or ISO 27001. Where the installer supports supplying your own KMS key, you can provide it. See the [deployment repository's README](https://github.com/pinecone-io/pulumi-pinecone-nexus-byoc) for current options. This is not the console [CMEK](/guides/production/configure-cmek) flow used for hosted Pinecone projects. For how the two relate, see the Database BYOC page's [Encryption and customer-managed keys](/guides/production/bring-your-own-cloud#encryption-and-customer-managed-keys).

## Cluster footprint

Nexus BYOC runs a Kubernetes cluster across several dedicated node pools spread over three availability zones (AZs):

| Node pool                                                       | Purpose                                                  |
| --------------------------------------------------------------- | -------------------------------------------------------- |
| Pinecone Database                                               | The data plane, including query routing and index builds |
| Metadata store                                                  | Stores Nexus metadata, backed by FoundationDB            |
| Nexus services                                                  | The curation and query runtimes and their workflow jobs  |
| [Dedicated read nodes](/guides/index-data/dedicated-read-nodes) | Scale from zero as read demand grows                     |

The cluster comes up small and autoscales with load and with the number of contexts and indexes. Node counts and instance types change across releases as the footprint is tuned. Size your cloud quotas from the installer's preflight quota checks in [Deploy Nexus BYOC](/guides/nexus/byoc/deploy) rather than from a fixed node count.

## Limitations

* **The endpoint is public and authenticated.** The Nexus API and console are reached over a public, access-controlled endpoint. Private-only access (PrivateLink, Private Service Connect, or Private Endpoint) for Nexus is not supported. (The Pinecone Database data plane in the same deployment can run privately, but Nexus cannot.)
* **Domain and TLS are Pinecone-managed.** The endpoint is served on a Pinecone-managed domain (`.byoc.pinecone.io`) with certificates issued and renewed automatically. Custom or customer-owned domains are not supported, so no DNS delegation or certificate handoff is required from you.
* **Bring your own models.** Generation, embedding, and rerank are all BYOM and configurable. A generation-LLM key is required (default: Google Gemini). Provider quota is your responsibility, so size the tier to your ingest volume. Model configuration determines where content is sent. See [Data flows and residency](#data-flows-and-residency).
* **Workspace names are unique per Pinecone project.** When several deployments share one project, give each additional deployment a distinct workspace name via `nexus-default-workspace-name`.
* **Environment cap.** Each organization can create a limited number of BYOC environments. To request an increase, contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).

To install, see [Deploy Nexus BYOC](/guides/nexus/byoc/deploy).
