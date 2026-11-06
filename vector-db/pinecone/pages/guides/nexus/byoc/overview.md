---
title: "Nexus BYOC overview"
source: https://docs.pinecone.io/guides/nexus/byoc/overview
path: guides/nexus/byoc/overview
---

Learn what Nexus BYOC deploys in your cloud account, what data leaves it, and how it compares to Database BYOC.

> [!NOTE]
>
> Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).

Pinecone Nexus compiles your enterprise data into queryable knowledge that AI agents retrieve with a single [KnowQL](/guides/nexus/concepts#knowql) query. Nexus BYOC (Bring Your Own Cloud) deploys Nexus, and the Pinecone Database data plane it runs on, inside your own AWS, GCP, or Azure account. It's built for organizations with strict data sovereignty, network isolation, and data residency requirements, and Pinecone still handles upgrades, scaling, and maintenance. To install it, see [Deploy Nexus BYOC](/guides/nexus/byoc/deploy).

## Architecture

Nexus BYOC splits into two planes:

* **Data plane:** Runs in your cloud account within a dedicated virtual network (a VPC on AWS and GCP, a VNet on Azure). It holds the Nexus services, the Pinecone Database data plane they depend on, a metadata store, and object storage for your corpus and derived knowledge artifacts. Your sources are curated, indexed, and queried here.
* **Control plane:** Managed by Pinecone globally. It handles workspace lifecycle, authentication, billing, and user management, and never stores or processes your data.

Pinecone never has direct access to your cloud account, and the deployment needs no inbound network access. For maintenance, an agent in your cluster authenticates with Pinecone's control plane, pulls pending operations such as upgrades and scaling, and runs them locally.

## Data residency

Your sources and compiled knowledge stay in your cloud account. Data leaves it in two ways:

* **Inference calls:** To curate and answer, Nexus sends the content it's processing to the model endpoint for each step. Generation always uses the provider you configure. By default, embedding and rerank run on Pinecone-hosted models, so some document and query text goes to Pinecone for those steps. You can change any of these [models](/guides/nexus/models).
* **Operational telemetry:** Metrics such as CPU, memory, and latency, plus traces. Customer data is filtered out before it's sent.

Before you make residency commitments, read [Data flows and residency](/guides/nexus/byoc/reference#data-flows-and-residency) for the exact breakdown.

## Nexus BYOC vs. Database BYOC

Nexus BYOC installs from one repository, [`pulumi-pinecone-nexus-byoc`](https://github.com/pinecone-io/pulumi-pinecone-nexus-byoc). One `pulumi up` deploys both the Nexus services and the Pinecone Database data plane they run on, so there's no separate Database install. The Database data plane is the storage and retrieval engine beneath your contexts, not a product you operate on its own, and you work with the deployment through contexts and KnowQL.

Nexus BYOC needs one thing Database BYOC doesn't: a key for a generation model, Google Gemini by default.

To run Pinecone Database on its own in your cloud, use [Database BYOC](/guides/production/bring-your-own-cloud), which has its own installer.
