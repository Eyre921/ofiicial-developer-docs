---
title: "Nexus BYOC overview"
source: https://docs.pinecone.io/guides/nexus/byoc/overview
path: guides/nexus/byoc/overview
---

What Nexus BYOC is, how it relates to Database BYOC, and its architecture.

<Note>
  Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

Pinecone Nexus compiles your enterprise data into queryable knowledge that AI agents retrieve with a single [KnowQL](/guides/nexus/concepts#knowql) query. Nexus BYOC (Bring Your Own Cloud) is a single installer that deploys both Nexus and the Pinecone Database data plane it runs on, entirely inside your own cloud account (AWS, GCP, or Azure). You do not install Database BYOC separately. Nexus BYOC includes it (see [how the two relate](#how-nexus-byoc-relates-to-database-byoc)).

Nexus BYOC is designed for organizations with strict requirements around data sovereignty, network isolation, and data residency. You get the benefits of a managed service (upgrades, scaling, and maintenance) without giving up control of your data or infrastructure.

Pinecone never has direct access to your cloud account, and no inbound network access is required. Components in your cluster pull operations from Pinecone and execute them locally. Your sources and compiled knowledge are stored within your account. Data leaves your account through the inference calls Nexus makes to curate and answer, plus operational telemetry (no customer content). Those inference calls carry the content being processed to the model endpoints used for each step. Models are configurable (BYOM). Generation always uses the provider you configure, and by default embedding and rerank run on Pinecone-hosted models, so with the defaults some document and query text is sent to Pinecone for those steps. See [Data flows and residency](/guides/nexus/byoc/reference#data-flows-and-residency) for the exact breakdown, and read it before making residency commitments.

Nexus BYOC uses a split architecture:

* The **data plane** runs entirely in your cloud account within a dedicated virtual network (a VPC on AWS and GCP, a VNet on Azure): the Nexus services, the Pinecone Database data plane they depend on, a metadata store, and object storage for your corpus and derived knowledge artifacts. This is where your sources are curated, indexed, and queried.
* The **control plane** is managed by Pinecone globally and handles workspace lifecycle, authentication, billing, and user management, but never stores or processes your data.

For maintenance, an agent in your cluster authenticates with Pinecone's control plane, pulls pending operations (upgrades, scaling, and so on), and executes them locally. Only operational metrics (CPU, memory, latency) and traces are transmitted to Pinecone for monitoring. Customer data is filtered out before transmission.

## How Nexus BYOC relates to Database BYOC

Nexus BYOC is installed from a single repository, [`pulumi-pinecone-nexus-byoc`](https://github.com/pinecone-io/pulumi-pinecone-nexus-byoc). One `pulumi up` deploys both the Nexus services and the Pinecone Database data plane they run on. There is no separate Database install to run first or alongside it.

The Pinecone Database data plane is deployed automatically because Nexus runs on it: it is the storage and retrieval engine beneath your contexts, not a separate product you operate. You work with a Nexus BYOC deployment through contexts and [KnowQL](/guides/nexus/concepts#knowql). Nexus BYOC brings one additional dependency: a generation-LLM key you supply (default: Google Gemini).

If you want a standalone Pinecone vector database in your own cloud instead, see [Database BYOC](/guides/production/bring-your-own-cloud), which has its own installer. The Database BYOC installer is not part of the Nexus install.

Nexus BYOC uses the core Nexus product terms (context, manifest, KnowQL, and workspace). See [Nexus concepts](/guides/nexus/concepts) for definitions, [Data residency and limits](/guides/nexus/byoc/reference) for the security and operational details, and [Deploy Nexus BYOC](/guides/nexus/byoc/deploy) to install.
