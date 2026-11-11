---
title: "Bring your own vectors"
source: https://docs.pinecone.io/guides/search/bring-your-own-vectors
path: guides/search/bring-your-own-vectors
---

Store embeddings you generate yourself in a document index, then search them by vector similarity with a query vector from the same model.

If you already generate embeddings, store them in a `dense_vector` field on a document index. This fits when you use a model Pinecone doesn't host, a model you've fine-tuned, or vectors you've already computed. You embed every document before you upsert it and every query before you search. To have Pinecone embed your text instead, use [integrated embedding](/guides/search/integrated-embedding).

For a legacy vector index, see [Create a vector index](/guides/legacy/vectors-api/create-a-vector-index), [Upsert vectors](/guides/legacy/vectors-api/upsert-vectors), and [Query vectors](/guides/legacy/vectors-api/query-vectors).

The steps use an SDK or the REST API, with your API key in the `PINECONE_API_KEY` environment variable. To set them up, see the [quickstart](/guides/get-started/quickstart#set-it-up-yourself). The JavaScript examples use top-level `await`, so run them as an ES module. The Go examples build one `main` function: the first block is the full program, and each later block adds to it.

### 1. Generate embeddings for your documents

Embed each document's text with the model of your choice. So the example runs as is, it uses Pinecone's hosted `llama-text-embed-v2` model through the [standalone embedding API](/reference/api/latest/inference/generate-vectors), which returns 1,024-dimension vectors. Set `input_type` to `passage` for documents.

```python Python theme={null}
import os, time
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

texts = [
    "Refund requests must be submitted within 30 days of purchase.",
    "Enterprise customers get support with a 4-hour response time.",
    "Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.",
    "To reset your password, open Settings and choose Security.",
    "Order 88231 shipped on 2026-08-20 via express courier.",
]

embeddings = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=texts,
    parameters={"input_type": "passage"},
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone(); // reads PINECONE_API_KEY

const texts = [
  'Refund requests must be submitted within 30 days of purchase.',
  'Enterprise customers get support with a 4-hour response time.',
  'Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.',
  'To reset your password, open Settings and choose Security.',
  'Order 88231 shipped on 2026-08-20 via express courier.',
];

const embeddings = await pc.inference.embed({
  model: 'llama-text-embed-v2',
  inputs: texts,
  parameters: { inputType: 'passage' },
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

	pc, err := pinecone.NewClient(pinecone.NewClientParams{}) // reads PINECONE_API_KEY
	if err != nil {
		log.Fatal(err)
	}

	texts := []string{
		"Refund requests must be submitted within 30 days of purchase.",
		"Enterprise customers get support with a 4-hour response time.",
		"Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.",
		"To reset your password, open Settings and choose Security.",
		"Order 88231 shipped on 2026-08-20 via express courier.",
	}

	embeddings, err := pc.Inference.Embed(ctx, &pinecone.EmbedRequest{
		Model:      "llama-text-embed-v2",
		TextInputs: texts,
		Parameters: pinecone.EmbedParameters{"input_type": "passage"},
	})
	if err != nil {
		log.Fatal(err)
	}
}
```

```bash curl theme={null}
TEXTS='[
  "Refund requests must be submitted within 30 days of purchase.",
  "Enterprise customers get support with a 4-hour response time.",
  "Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.",
  "To reset your password, open Settings and choose Security.",
  "Order 88231 shipped on 2026-08-20 via express courier."
]'

# Embed the texts and save the response (requires jq)
jq -n --argjson t "$TEXTS" \
  '{model: "llama-text-embed-v2", parameters: {input_type: "passage"}, inputs: [$t[] | {text: .}]}' |
curl -s -X POST "https://api.pinecone.io/embed" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d @- > embeddings.json
```

### 2. Create an index with a dense\_vector field

Declare a `dense_vector` field whose `dimension` matches your model's output and whose `metric` matches what the model was trained for. `llama-text-embed-v2` uses `cosine`. This schema also declares `chunk_text` with `full_text_search`, so the index stores each document's text and can rank it by keyword too. Fields you don't declare are stored as metadata.

```python Python theme={null}
schema = (
    SchemaBuilder()
      .add_dense_vector_field("embedding", dimension=1024, metric="cosine")
      .add_string_field("chunk_text", full_text_search={"language": "en"})
      .build()
)
if not pc.indexes.exists(name="byo-vectors"):
    pc.indexes.create(name="byo-vectors", schema=schema)

while not pc.indexes.describe(name="byo-vectors").status.ready:
    time.sleep(2)

index = pc.index(name="byo-vectors")
```

```javascript JavaScript theme={null}
await pc.indexes.create({
  name: 'byo-vectors',
  schema: {
    fields: {
      embedding: { type: 'dense_vector', dimension: 1024, metric: 'cosine' },
      chunk_text: { type: 'string', fullTextSearch: { language: 'en' } },
    },
  },
  waitUntilReady: true,
  suppressConflicts: true,
});

const index = pc.index({ name: 'byo-vectors', namespace: '__default__' });
```

```go Go theme={null}
// Add "time" to your imports, then add to the main function:
if _, err := pc.DescribeIndex(ctx, "byo-vectors"); err != nil {
	language := "en"
	_, err = pc.CreateIndex(ctx, &pinecone.CreateIndexRequest{
		Name: "byo-vectors",
		Schema: pinecone.IndexSchema{
			Fields: map[string]pinecone.IndexSchemaField{
				"embedding": {DenseVector: &pinecone.DenseVectorField{
					Dimension: 1024,
					Metric:    pinecone.IndexMetricCosine,
				}},
				"chunk_text": {String: &pinecone.StringField{
					FullTextSearch: &pinecone.FullTextSearchConfig{Language: &language},
				}},
			},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
}

idx, err := pc.DescribeIndex(ctx, "byo-vectors")
for err == nil && !idx.Status.Ready {
	time.Sleep(2 * time.Second)
	idx, err = pc.DescribeIndex(ctx, "byo-vectors")
}
if err != nil {
	log.Fatal(err)
}

index, err := pc.Index(pinecone.NewIndexConnParams{Host: idx.Host, Namespace: "__default__"})
if err != nil {
	log.Fatal(err)
}
```

```bash curl theme={null}
curl -X POST "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "byo-vectors",
    "schema": {
      "fields": {
        "embedding": { "type": "dense_vector", "dimension": 1024, "metric": "cosine" },
        "chunk_text": { "type": "string", "full_text_search": { "language": "en" } }
      }
    }
  }'

# Wait until the index is ready, then save its host
until curl -s "https://api.pinecone.io/indexes/byo-vectors" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" | jq -e '.status.ready' > /dev/null; do
  sleep 2
done

INDEX_HOST=$(curl -s "https://api.pinecone.io/indexes/byo-vectors" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" | jq -r '.host')
```

### 3. Upsert documents with their vectors

Put each vector on the `embedding` field, next to the text it came from. Each vector must have exactly 1,024 values. Documents are indexed asynchronously, so the code waits 10 seconds before you search.

```python Python theme={null}
index.documents.upsert(
    namespace="__default__",
    documents=[
        {"_id": str(i + 1), "chunk_text": text, "embedding": e.values}
        for i, (text, e) in enumerate(zip(texts, embeddings))
    ],
)

time.sleep(10)  # documents are indexed asynchronously, so wait a moment
```

```javascript JavaScript theme={null}
await index.documents.upsert({
  documents: texts.map((text, i) => ({
    _id: String(i + 1),
    chunk_text: text,
    embedding: embeddings.data[i].values,
  })),
});

await new Promise((resolve) => setTimeout(resolve, 10000)); // documents are indexed asynchronously, so wait a moment
```

```go Go theme={null}
// Add "strconv" to your imports, then add to the main function:
var documents []pinecone.Document
for i, text := range texts {
	documents = append(documents, pinecone.Document{
		"_id":        strconv.Itoa(i + 1),
		"chunk_text": text,
		"embedding":  embeddings.Data[i].DenseEmbedding.Values,
	})
}

if _, err := index.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{Documents: documents}); err != nil {
	log.Fatal(err)
}

time.Sleep(10 * time.Second) // documents are indexed asynchronously, so wait a moment
```

```bash curl theme={null}
jq -n --argjson t "$TEXTS" --slurpfile e embeddings.json \
  '{documents: [range(0; $t | length) as $i |
    {_id: ($i + 1 | tostring), chunk_text: $t[$i], embedding: $e[0].data[$i].values}]}' |
curl -X POST "https://$INDEX_HOST/namespaces/__default__/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d @-

sleep 10  # documents are indexed asynchronously, so wait a moment
```

### 4. Embed your query

Embed the query with the same model you used for the documents. Vectors from different models aren't comparable, so a different model returns meaningless rankings. For `llama-text-embed-v2`, set `input_type` to `query`.

```python Python theme={null}
query = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=["how do I get my money back?"],
    parameters={"input_type": "query"},
)
```

```javascript JavaScript theme={null}
const query = await pc.inference.embed({
  model: 'llama-text-embed-v2',
  inputs: ['how do I get my money back?'],
  parameters: { inputType: 'query' },
});
```

```go Go theme={null}
// Add to the main function:
query, err := pc.Inference.Embed(ctx, &pinecone.EmbedRequest{
	Model:      "llama-text-embed-v2",
	TextInputs: []string{"how do I get my money back?"},
	Parameters: pinecone.EmbedParameters{"input_type": "query"},
})
if err != nil {
	log.Fatal(err)
}
```

```bash curl theme={null}
curl -s -X POST "https://api.pinecone.io/embed" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "model": "llama-text-embed-v2",
    "parameters": { "input_type": "query" },
    "inputs": [{ "text": "how do I get my money back?" }]
  }' | jq '.data[0].values' > query.json
```

### 5. Search by vector similarity

Score by `dense_vector` and pass the query vector in `values`. Pinecone ranks documents by the field's `metric`.

```python Python theme={null}
results = index.documents.search(
    namespace="__default__",
    top_k=3,
    score_by=[{"type": "dense_vector", "fields": ["embedding"], "values": query.data[0].values}],
    include_fields=["chunk_text"],
)

for m in results.matches:
    print(m.id, f"{m.score:.3f}", m.chunk_text)
```

```javascript JavaScript theme={null}
const results = await index.documents.search({
  topK: 3,
  scoreBy: [{ type: 'dense_vector', fields: ['embedding'], values: query.data[0].values }],
  includeFields: ['chunk_text'],
});

for (const m of results.matches) {
  console.log(m._id, m._score.toFixed(3), m.chunk_text);
}
```

```go Go theme={null}
// Add "fmt" to your imports, then add to the main function:
queryVector := query.Data[0].DenseEmbedding.Values
results, err := index.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
	TopK: 3,
	ScoreBy: []pinecone.DocumentScoringMethod{
		{Type: pinecone.DocumentScoringTypeDenseVector, Fields: []string{"embedding"}, Values: &queryVector},
	},
	IncludeFields: []string{"chunk_text"},
})
if err != nil {
	log.Fatal(err)
}

for _, m := range results.Matches {
	fmt.Printf("%s %.3f %s\n", m.Id, *m.Score, m.Fields["chunk_text"])
}
```

```bash curl theme={null}
jq -n --slurpfile q query.json \
  '{top_k: 3, score_by: [{type: "dense_vector", fields: ["embedding"], values: $q[0]}], include_fields: ["chunk_text"]}' |
curl -X POST "https://$INDEX_HOST/namespaces/__default__/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d @-
```

The refund policy ranks first:

```text Output theme={null}
1 0.417 Refund requests must be submitted within 30 days of purchase.
4 0.119 To reset your password, open Settings and choose Security.
2 0.089 Enterprise customers get support with a 4-hour response time.
```

Because `chunk_text` declares `full_text_search`, the same index also supports a [full-text search](/guides/search/full-text-search) on the text, and either search accepts a [metadata filter](/guides/search/filter-by-metadata).
