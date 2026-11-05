---
title: "Index configuration"
source: https://docs.pinecone.io/guides/indexes/index-configuration
path: guides/indexes/index-configuration
---

Reference for the naming rules, cloud regions, similarity metrics, and hosted embedding models you choose when you create a Pinecone index.

When you create a Pinecone index, you choose a name, the cloud region where it's hosted, a similarity metric for dense vectors, and, for integrated embedding, a hosted embedding model. To index only the metadata fields you filter on, rather than all of them, see [Configure metadata indexing](/guides/indexes/configure-metadata-indexing).

## Index names

An index name must be unique within its project and 1 to 45 characters long. It can contain only lowercase letters, numbers, and hyphens (`-`), and it must start and end with a letter or number.

## Cloud regions

When creating an index, you must choose the cloud and region where you want the index to be hosted. The following table lists the available public clouds and regions and the plans that support them:

| Cloud | Region | [Supported plans](https://www.pinecone.io/pricing/) | [Availability phase](/release-notes/feature-availability) |
| - | - | - | - |
| `aws` | `us-east-1` (Virginia) | Starter, Builder, Standard, Enterprise | General availability |
| `aws` | `us-west-2` (Oregon) | Builder, Standard, Enterprise | General availability |
| `aws` | `eu-west-1` (Ireland) | Builder, Standard, Enterprise | General availability |
| `aws` | `eu-central-1` (Frankfurt) | Builder, Standard, Enterprise | General availability |
| `aws` | `ap-southeast-1` (Singapore) | Builder, Standard, Enterprise | General availability |
| `gcp` | `us-central1` (Iowa) | Builder, Standard, Enterprise | General availability |
| `gcp` | `europe-west4` (Netherlands) | Builder, Standard, Enterprise | General availability |
| `azure` | `eastus2` (Virginia) | Builder, Standard, Enterprise | General availability |

The cloud and region can't be changed after a serverless index is created.

> [!NOTE]
>
> On the Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade to the Builder, Standard, or Enterprise plan](/admin/billing/upgrade-billing-plan).

## Similarity metrics

When creating an index that stores dense vectors, you can choose from the following similarity metrics. For the most accurate results, choose the similarity metric used to train the embedding model for your vectors. For more information, see [Vector Similarity Explained](https://www.pinecone.io/learn/vector-similarity/).

> [!NOTE]
>
> Indexes that store [sparse vectors](/guides/get-started/key-terms#sparse-vector) must use the `dotproduct` metric.

> [accordion] Euclidean
>
> Querying indexes with this metric returns a similarity score equal to the squared Euclidean distance between the result and query vectors.
>
> This metric calculates the square of the distance between two data points in a plane. It's one of the most commonly used distance metrics. For an example, see the [IT threat detection example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/it-threat-detection.ipynb).
>
> When you use `metric='euclidean'`, the most similar results are those with the **lowest similarity score**.

> [accordion] Cosine
>
> This is often used to find similarities between different documents. The advantage is that the scores are normalized to \[-1,1] range. For an example, see the [generative question answering example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb).

> [accordion] Dotproduct
>
> This multiplies two vectors to measure how similar they are. The more positive the result, the closer the two vectors are in direction. For an example, see the [semantic search example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb).

## Embedding models

Pinecone hosts these embedding models. You can use them for [integrated embedding](/guides/search/integrated-embedding), where Pinecone embeds text as you upsert and search, and some of them for [standalone embedding](/reference/api/latest/inference/generate-vectors).

* Dense:
  * [`gemini-embedding-2`](/models/gemini-embedding-2)
  * [`llama-text-embed-v2`](/models/llama-text-embed-v2)
  * [`multilingual-e5-large`](/models/multilingual-e5-large)
  * [`text-embedding-3-large`](/models/text-embedding-3-large)
  * [`text-embedding-3-small`](/models/text-embedding-3-small)
* Sparse:
  * [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0)

Each model's page lists the parameters it accepts and its specs, such as dimension, max tokens, metric, supported API, and plan. To compare the models, see the [model gallery](/models/overview).

> [!NOTE]
>
> To understand how cost is calculated for embedding, see [Embedding cost](/guides/cost/understand-cost#embedding). To get model details via the API, see [List models](/reference/api/latest/inference/list-available-models) and [Describe a model](/reference/api/latest/inference/describe-a-model).
