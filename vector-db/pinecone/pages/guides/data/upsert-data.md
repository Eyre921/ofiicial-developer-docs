---
title: "Upsert data"
source: https://docs.pinecone.io/guides/data/upsert-data
path: guides/data/upsert-data
---

Upsert documents into a Pinecone document index, batch upserts for higher throughput, and partition data with namespaces.

This page shows you how to upsert documents into a namespace in a document index. [Namespaces](/guides/indexes/indexing-overview#namespaces) let you partition data within an index and are essential for [implementing multitenancy](/guides/data/implement-multitenancy) when you need to isolate the data of each customer or user.

If an ID already exists, upserting overwrites the entire document. To change only part of a document, [update](/guides/data/update-data) it.

For a legacy vector index, see [Upsert vectors](/guides/legacy/vectors-api/upsert-vectors). For a legacy integrated index, see [Upsert text](/guides/legacy/records-api/upsert-text).

> [!TIP]
>
> Upserts consume [write units (WUs)](/guides/manage-cost/understanding-cost#write-units). See [Understand Pinecone cost](/guides/manage-cost/understanding-cost#upsert) for how upsert cost is calculated. To control costs when ingesting large datasets (10,000,000+ documents), use [import](/guides/data/import-data) instead of upsert.

## Upsert documents

[Documents](/guides/core-concepts/key-terms#document) are the unit of data in a document index. Each field in a document is indexed according to the configuration you declared for it in the schema, not just its type. For example, a `string` field can be indexed for BM25 with the `full_text_search` config, and a separate `dense_vector` field can store vector values you provide at upsert time. A `string` field can also declare `embed` or `sparse_embed` so Pinecone embeds its text with [integrated embedding](/guides/search/integrated-embedding).

The following example upserts two documents into the `articles` namespace with the Documents API. Each document is indexed for BM25 ranking on `body`. The `category` field isn't declared in the schema, so it's stored as metadata and automatically indexed for filtering:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.upsert(
    namespace="articles",
    documents=[
        {
            "_id": "doc1",
            "body": "Pinecone serverless indexes scale automatically with your workload.",
            "category": "platform",
        },
        {
            "_id": "doc2",
            "body": "Full-text search uses BM25 ranking on text fields with full-text search enabled.",
            "category": "search",
        },
    ],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'articles' });

await index.documents.upsert({
  documents: [
    {
      _id: 'doc1',
      body: 'Pinecone serverless indexes scale automatically with your workload.',
      category: 'platform',
    },
    {
      _id: 'doc2',
      body: 'Full-text search uses BM25 ranking on text fields with full-text search enabled.',
      category: 'search',
    },
  ],
});
```

```go Go theme={null}
package main

import (
	"context"
	"log"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "articles"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	_, err = idxConnection.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
		Documents: []pinecone.Document{
			{
				"_id":      "doc1",
				"body":     "Pinecone serverless indexes scale automatically with your workload.",
				"category": "platform",
			},
			{
				"_id":      "doc2",
				"body":     "Full-text search uses BM25 ranking on text fields with full-text search enabled.",
				"category": "search",
			},
		},
	})
	if err != nil {
		log.Fatalf("Failed to upsert documents: %v", err)
	}
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/articles/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      {
        "_id": "doc1",
        "body": "Pinecone serverless indexes scale automatically with your workload.",
        "category": "platform"
      },
      {
        "_id": "doc2",
        "body": "Full-text search uses BM25 ranking on text fields with full-text search enabled.",
        "category": "search"
      }
    ]
  }'
```

> [!NOTE]
>
> The Documents API requires API version `2026-07` or later.

The schema declares only ranking fields: `string` fields with `full_text_search`, `embed`, or `sparse_embed`, plus `dense_vector` and `sparse_vector` fields. Any other field you upsert is stored on the document as metadata, returned with `include_fields`, and indexed for filtering.

Field names must be unique, non-empty strings of up to 64 bytes. They can't start with `_`, which is reserved for system fields such as `_id` and `_score`, or with `$`, which is reserved for filter operators.

Upsert replaces the whole document for a given `_id`. To change individual fields, see [Update documents](/guides/data/update-data#update-documents). For document, field, and request size limits, see [Upsert limits](/reference/api/database-limits/operation-limits#upsert-limits). For more examples and the response schema, see [Full-text search](/guides/search/full-text-search).

## Upsert dense vectors

To upsert dense vectors into a [document index](/guides/indexes/create-an-index#create-a-document-index), use the [Upsert documents](/reference/api/latest/data-plane/upsert_documents) operation:

* Specify the [`namespace`](/guides/indexes/indexing-overview#namespaces) to upsert into. If the namespace doesn't exist, it's created. To use the default namespace, set the namespace to `"__default__"`.
* Format your input data as documents, each with the following:
  * An `_id` field with a unique document identifier for the index namespace.
  * The `dense_vector` field declared in the index schema, with the vector values. This example uses a field named `embedding`.
  * Optionally, other fields, which are stored as [metadata](/guides/indexes/indexing-overview#metadata). When you search the index, you can use metadata to [filter search results](/guides/search/filter-by-metadata).

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.upsert(
    namespace="example-namespace",
    documents=[
        {
            "_id": "A",
            "embedding": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            "genre": "comedy",
            "year": 2020
        },
        {
            "_id": "B",
            "embedding": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
            "genre": "documentary",
            "year": 2019
        },
        {
            "_id": "C",
            "embedding": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
            "genre": "comedy",
            "year": 2019
        },
        {
            "_id": "D",
            "embedding": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
            "genre": "drama"
        },
    ],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

await index.documents.upsert({
  documents: [
    { _id: 'A', embedding: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], genre: "comedy", year: 2020 },
    { _id: 'B', embedding: [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], genre: "documentary", year: 2019 },
    { _id: 'C', embedding: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], genre: "comedy", year: 2019 },
    { _id: 'D', embedding: [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], genre: "drama" },
  ],
});
```

```go Go theme={null}
package main

import (
	"context"
	"log"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	_, err = idxConnection.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
		Documents: []pinecone.Document{
			{
				"_id":       "A",
				"embedding": []float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1},
				"genre":     "comedy",
				"year":      2020,
			},
			{
				"_id":       "B",
				"embedding": []float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2},
				"genre":     "documentary",
				"year":      2019,
			},
			{
				"_id":       "C",
				"embedding": []float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
				"genre":     "comedy",
				"year":      2019,
			},
			{
				"_id":       "D",
				"embedding": []float32{0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4},
				"genre":     "drama",
			},
		},
	})
	if err != nil {
		log.Fatalf("Failed to upsert documents: %v", err)
	}
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/example-namespace/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      { "_id": "A", "embedding": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], "genre": "comedy", "year": 2020 },
      { "_id": "B", "embedding": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "genre": "documentary", "year": 2019 },
      { "_id": "C", "embedding": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], "genre": "comedy", "year": 2019 },
      { "_id": "D", "embedding": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], "genre": "drama" }
    ]
  }'
```

## Upsert sparse vectors

Upsert sparse vectors when your data is encoded by a learned sparse model, such as [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0), or when your application generates the sparse vectors itself. For BM25 keyword search over raw text without managing a model, see [Upsert documents](#upsert-documents).

To upsert sparse vectors into a [document index](/guides/indexes/create-an-index#create-a-document-index), use the [Upsert documents](/reference/api/latest/data-plane/upsert_documents) operation:

* Specify the [`namespace`](/guides/indexes/indexing-overview#namespaces) to upsert into. If the namespace doesn't exist, it's created. To use the default namespace, set the namespace to `"__default__"`.
* Format your input data as documents, each with the following:
  * An `_id` field with a unique document identifier for the index namespace.
  * The `sparse_vector` field declared in the index schema, with `indices` and `values` arrays. This example uses a field named `sparse_embedding`.
  * Optionally, other fields, which are stored as [metadata](/guides/indexes/indexing-overview#metadata). When you search the index, you can use metadata to [filter search results](/guides/search/filter-by-metadata).

For example, the following code upserts sparse vector representations of sentences related to the term "apple", with the source text and additional fields stored as metadata:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.documents.upsert(
    namespace="example-namespace",
    documents=[
        {
            "_id": "vec1",
            "sparse_embedding": {
                "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191],
                "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688]
            },
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
            "category": "technology",
            "quarter": "Q3"
        },
        {
            "_id": "vec2",
            "sparse_embedding": {
                "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697],
                "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469]
            },
            "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
            "category": "technology",
            "quarter": "Q4"
        },
        {
            "_id": "vec3",
            "sparse_embedding": {
                "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697],
                "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094]
            },
            "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
            "category": "technology",
            "quarter": "Q3"
        },
        {
            "_id": "vec4",
            "sparse_embedding": {
                "indices": [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673],
                "values": [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375]
            },
            "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
            "category": "technology",
            "quarter": "Q4"
        },
    ],
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

await index.documents.upsert({
  documents: [
    {
      _id: 'vec1',
      sparse_embedding: {
        indices: [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191],
        values: [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
      },
      chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
      category: 'technology',
      quarter: 'Q3',
    },
    {
      _id: 'vec2',
      sparse_embedding: {
        indices: [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697],
        values: [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
      },
      chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
      category: 'technology',
      quarter: 'Q4',
    },
    {
      _id: 'vec3',
      sparse_embedding: {
        indices: [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697],
        values: [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
      },
      chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
      category: 'technology',
      quarter: 'Q3',
    },
    {
      _id: 'vec4',
      sparse_embedding: {
        indices: [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673],
        values: [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375],
      },
      chunk_text: "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
      category: 'technology',
      quarter: 'Q4',
    },
  ],
});
```

```go Go theme={null}
package main

import (
	"context"
	"log"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	_, err = idxConnection.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
		Documents: []pinecone.Document{
			{
				"_id": "vec1",
				"sparse_embedding": map[string]interface{}{
					"indices": []uint32{822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191},
					"values":  []float32{1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688},
				},
				"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
				"category":   "technology",
				"quarter":    "Q3",
			},
			{
				"_id": "vec2",
				"sparse_embedding": map[string]interface{}{
					"indices": []uint32{131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697},
					"values":  []float32{0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469},
				},
				"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
				"category":   "technology",
				"quarter":    "Q4",
			},
			{
				"_id": "vec3",
				"sparse_embedding": map[string]interface{}{
					"indices": []uint32{8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697},
					"values":  []float32{2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094},
				},
				"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
				"category":   "technology",
				"quarter":    "Q3",
			},
			{
				"_id": "vec4",
				"sparse_embedding": map[string]interface{}{
					"indices": []uint32{131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673},
					"values":  []float32{0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375},
				},
				"chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
				"category":   "technology",
				"quarter":    "Q4",
			},
		},
	})
	if err != nil {
		log.Fatalf("Failed to upsert documents: %v", err)
	}
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/namespaces/example-namespace/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      { "_id": "vec1", "sparse_embedding": { "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191], "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688] }, "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", "category": "technology", "quarter": "Q3" },
      { "_id": "vec2", "sparse_embedding": { "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697], "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469] }, "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.", "category": "technology", "quarter": "Q4" },
      { "_id": "vec3", "sparse_embedding": { "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697], "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094] }, "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production", "category": "technology", "quarter": "Q3" },
      { "_id": "vec4", "sparse_embedding": { "indices": [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673], "values": [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375] }, "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", "category": "technology", "quarter": "Q4" }
    ]
  }'
```

## Upsert in batches

> [!TIP]
>
> To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/data/import-data) instead of upsert.

Send upserts in batches to help increase throughput. A request can contain up to 1,000 documents and 2 MB, or up to 96 documents when the schema declares `embed` or `sparse_embed`. The lower limit comes from the [hosted embedding models](/guides/indexes/index-configuration#embedding-models) used during integrated embedding.

In Python, `index.documents.batch_upsert` splits a larger list into batches, sends them in parallel, and halves any batch the server rejects as too large.

```python Python theme={null}
import random
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

# Example data: 10,000 documents with a 128-dimension `embedding` field
documents = [
    {"_id": f"doc-{i}", "embedding": [random.random() for _ in range(128)]}
    for i in range(10000)
]

# Upsert 200 documents per request
result = index.documents.batch_upsert(
    namespace="example-namespace",
    documents=documents,
    batch_size=200,
)
print(result)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

// Example data: 10,000 documents with a 128-dimension `embedding` field
const documents = Array.from({ length: 10000 }, (_, i) => ({
  _id: `doc-${i}`,
  embedding: Array.from({ length: 128 }, () => Math.random()),
}));

// Upsert 200 documents per request
for (let i = 0; i < documents.length; i += 200) {
  await index.documents.upsert({ documents: documents.slice(i, i + 200) });
}
```

```go Go theme={null}
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	// Example data: 10,000 documents with a 128-dimension `embedding` field
	documents := make([]pinecone.Document, 10000)
	for i := range documents {
		embedding := make([]float32, 128)
		for j := range embedding {
			embedding[j] = rand.Float32()
		}
		documents[i] = pinecone.Document{"_id": fmt.Sprintf("doc-%d", i), "embedding": embedding}
	}

	// Upsert 200 documents per request
	batchSize := 200
	for start := 0; start < len(documents); start += batchSize {
		end := min(start+batchSize, len(documents))
		_, err := idxConnection.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{Documents: documents[start:end]})
		if err != nil {
			log.Fatalf("Failed to upsert batch starting at %d: %v", start, err)
		}
	}
}
```

## Upsert in parallel

> [!TIP]
>
> Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Asyncio support lets you use Pinecone with async web frameworks such as FastAPI, Quart, and Sanic. For details, see [Async requests](/reference/sdks/python/overview#async-requests).

Send multiple upserts in parallel to help increase throughput. Each upsert call blocks until the response arrives, so send several at once.

In Python, `batch_upsert` sends batches in parallel. Set `max_concurrency` to cap the number of requests in flight. In JavaScript and Go, send the batches concurrently yourself:

```python Python theme={null}
import random
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

# Example data: 10,000 documents with a 128-dimension `embedding` field
documents = [
    {"_id": f"doc-{i}", "embedding": [random.random() for _ in range(128)]}
    for i in range(10000)
]

# Send up to 10 requests of 200 documents at a time
result = index.documents.batch_upsert(
    namespace="example-namespace",
    documents=documents,
    batch_size=200,
    max_concurrency=10,
)
print(result)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: 'INDEX_HOST', namespace: 'example-namespace' });

// Example data: 10,000 documents with a 128-dimension `embedding` field
const documents = Array.from({ length: 10000 }, (_, i) => ({
  _id: `doc-${i}`,
  embedding: Array.from({ length: 128 }, () => Math.random()),
}));

// Break the documents into batches of 200
const batches = [];
for (let i = 0; i < documents.length; i += 200) {
  batches.push(documents.slice(i, i + 200));
}

// Send all batches in parallel
await Promise.all(batches.map((batch) => index.documents.upsert({ documents: batch })));
```

```go Go theme={null}
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"sync"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	// Example data: 10,000 documents with a 128-dimension `embedding` field
	documents := make([]pinecone.Document, 10000)
	for i := range documents {
		embedding := make([]float32, 128)
		for j := range embedding {
			embedding[j] = rand.Float32()
		}
		documents[i] = pinecone.Document{"_id": fmt.Sprintf("doc-%d", i), "embedding": embedding}
	}

	// Send up to 10 requests of 200 documents at a time
	batchSize := 200
	semaphore := make(chan struct{}, 10)
	errs := make(chan error, len(documents)/batchSize+1)
	var wg sync.WaitGroup

	for start := 0; start < len(documents); start += batchSize {
		batch := documents[start:min(start+batchSize, len(documents))]
		wg.Add(1)
		semaphore <- struct{}{}
		go func(start int, batch []pinecone.Document) {
			defer wg.Done()
			defer func() { <-semaphore }()
			if _, err := idxConnection.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{Documents: batch}); err != nil {
				errs <- fmt.Errorf("batch starting at %d: %w", start, err)
			}
		}(start, batch)
	}

	wg.Wait()
	close(errs)
	for err := range errs {
		log.Printf("Failed to upsert %v", err)
	}
}
```

## Upsert limits

| Metric | Limit |
| :- | :- |
| Max [batch size](/guides/legacy/vectors-api/upsert-vectors#upsert-in-batches) for records with vectors | 1,000 records, up to 2 MB total |
| Max batch size for records with text | 96 records |
| Max documents per upsert request | 1,000, or 96 when the schema declares `embed` or `sparse_embed` |
| Max document upsert request size | 2 MB |
| Max document size | 2 MB |
| Max `full_text_search` string fields per schema | 100 |
| Max size per `full_text_search` string field | 100 KB |
| Max tokens per `full_text_search` string field | 10,000 |
| Max [bytes per token](/guides/search/full-text-search/text-processing#tokens-and-analyzers) | 1,024 bytes |
| Max filterable metadata size per document | 40 KB |
| Max length for a record ID | 512 characters |
| Max dimensionality for dense vectors | 20,000 |
| Max non-zero values for sparse vectors | 2048 |
| Max dimensionality for sparse vectors | 4.2 billion |

The limit for text is lower because Pinecone converts that text to vectors at upsert time with [integrated embedding](/guides/indexes/indexing-overview#integrated-embedding), and 96 is the max batch size of the [hosted embedding models](/guides/indexes/index-configuration#embedding-models) doing the conversion.

The 40 KB filterable metadata limit doesn't apply to `full_text_search` text fields.
