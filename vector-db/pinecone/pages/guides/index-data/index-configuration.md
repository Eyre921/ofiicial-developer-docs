---
title: "Index configuration"
source: https://docs.pinecone.io/guides/index-data/index-configuration
path: guides/index-data/index-configuration
---

Reference for the naming rules, cloud regions, similarity metrics, and hosted embedding models you choose when you create a Pinecone index.

When you create a Pinecone index, you choose a name, the cloud region where it's hosted, a similarity metric for dense vectors, and, for integrated embedding, a hosted embedding model. To index only the metadata fields you filter on, rather than all of them, see [Configure metadata indexing](/guides/index-data/configure-metadata-indexing).

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

<Note>
  On the Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade to the Builder, Standard, or Enterprise plan](/admin/billing/upgrade-billing-plan).
</Note>

## Similarity metrics

When creating an index that stores dense vectors, you can choose from the following similarity metrics. For the most accurate results, choose the similarity metric used to train the embedding model for your vectors. For more information, see [Vector Similarity Explained](https://www.pinecone.io/learn/vector-similarity/).

<Note>Indexes that store [sparse vectors](/guides/core-concepts/key-terms#sparse-vector) must use the `dotproduct` metric.</Note>

<AccordionGroup>
  <Accordion title="Euclidean">
    Querying indexes with this metric returns a similarity score equal to the squared Euclidean distance between the result and query vectors.

    This metric calculates the square of the distance between two data points in a plane. It's one of the most commonly used distance metrics. For an example, see the [IT threat detection example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/it-threat-detection.ipynb).

    When you use `metric='euclidean'`, the most similar results are those with the **lowest similarity score**.
  </Accordion>

  <Accordion title="Cosine">
    This is often used to find similarities between different documents. The advantage is that the scores are normalized to \[-1,1] range. For an example, see the [generative question answering example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb).
  </Accordion>

  <Accordion title="Dotproduct">
    This multiplies two vectors to measure how similar they are. The more positive the result, the closer the two vectors are in direction. For an example, see the [semantic search example](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb).
  </Accordion>
</AccordionGroup>

## Embedding models

[Dense vectors](/guides/core-concepts/key-terms#dense-vector) and [sparse vectors](/guides/core-concepts/key-terms#sparse-vector) are the basic units of data in Pinecone and what Pinecone was specially designed to store and work with. Dense vectors represent the semantics of data such as text, images, and audio recordings, while sparse vectors represent documents or queries in a way that captures keyword information.

To transform data into vector format, you use an embedding model. Pinecone hosts several embedding models so it's easy to manage your vector storage and search process on a single platform. You can use a hosted model to embed your data as an integrated part of upserting and querying, or you can use a hosted model to embed your data as a standalone operation.

The following embedding models are hosted by Pinecone.

<Note>
  To understand how cost is calculated for embedding, see [Embedding cost](/guides/manage-cost/understanding-cost#embedding). To get model details via the API, see [List models](/reference/api/latest/inference/list-available-models) and [Describe a model](/reference/api/latest/inference/describe-a-model).
</Note>

### multilingual-e5-large

[`multilingual-e5-large`](/models/multilingual-e5-large) is an efficient dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs).

**Details**

* Vector type: Dense
* Modality: Text
* Dimension: 1024
* Recommended similarity metric: Cosine
* Max sequence length: 507 tokens
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits/rate-limits#model-throughput-limits) and [Embedding tokens per month](/reference/api/database-limits/rate-limits#monthly-usage-limits).

**Parameters**

The `multilingual-e5-large` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| :- | :- | :- | :- | :- |
| `input_type` | string | Required | The type of input data. Accepted values: `query` or `passage`. | |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the input token limit. `NONE` returns an error when the input exceeds the input token limit. | `END` |

### llama-text-embed-v2

[`llama-text-embed-v2`](/models/llama-text-embed-v2) is a high-performance dense embedding model optimized for text retrieval and ranking tasks. It's trained on a diverse range of text corpora and provides strong performance on longer passages and structured documents.

**Details**

* Vector type: Dense
* Modality: Text
* Dimension: 1024 (default), 2048, 768, 512, 384
* Recommended similarity metric: Cosine
* Max sequence length: 2048 tokens
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits/rate-limits#model-throughput-limits) and [Embedding tokens per month](/reference/api/database-limits/rate-limits#monthly-usage-limits).

**Parameters**

The `llama-text-embed-v2` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| :- | :- | :- | :- | :- |
| `input_type` | string | Required | The type of input data. Accepted values: `query` or `passage`. | |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END`, `NONE`, or `START`.<br /><br />`END` truncates the input sequence at the input token limit, keeping the start. `START` truncates from the start, keeping the end. `NONE` returns an error when the input exceeds the input token limit. | `END` |
| `dimension` | integer | Optional | Dimension of the vector to return. | 1024 |

### pinecone-sparse-english-v0

[`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) is a sparse embedding model for converting text to [sparse vectors](/guides/core-concepts/key-terms#sparse-vector) for [sparse-vector search](/guides/search/lexical-search) or hybrid search. Built on the innovations of the [DeepImpact architecture](https://arxiv.org/pdf/2104.12016), the model directly estimates the lexical importance of tokens by using their context, unlike traditional retrieval models like BM25, which rely solely on term frequency.

**Details**

* Vector type: Sparse
* Modality: Text
* Recommended similarity metric: Dotproduct
* Max sequence length: 512 or 2048
* Max batch size: 96 sequences

For rate limits, see [Embedding tokens per minute](/reference/api/database-limits/rate-limits#model-throughput-limits) and [Embedding tokens per month](/reference/api/database-limits/rate-limits#monthly-usage-limits).

**Parameters**

The `pinecone-sparse-english-v0` model supports the following parameters:

| Parameter | Type | Required/Optional | Description | Default |
| :- | :- | :- | :- | :- |
| `input_type` | string | Required | The type of input data. Accepted values: `query` or `passage`. | |
| `max_tokens_per_sequence` | integer | Optional | Maximum number of tokens to embed. Accepted values: `512` or `2048`. | `512` |
| `truncate` | string | Optional | How to handle inputs longer than those supported by the model. Accepted values: `END` or `NONE`.<br /><br />`END` truncates the input sequence at the `max_tokens_per_sequence` limit. `NONE` returns an error when the input exceeds the `max_tokens_per_sequence` limit. | `END` |
| `return_tokens` | boolean | Optional | Whether to return the string tokens. | `false` |
