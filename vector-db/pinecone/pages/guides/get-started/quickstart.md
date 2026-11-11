---
title: "Pinecone quickstart"
source: https://docs.pinecone.io/guides/get-started/quickstart
path: guides/get-started/quickstart
---

Get started with Pinecone in minutes. Create an index that searches your text by meaning and by exact terms, load sample documents, and run both searches.

One document index handles both kinds of search: by meaning, and by exact terms like IDs, error codes, and phrases. You upsert plain text, and Pinecone embeds it for you with [integrated embedding](/guides/search/integrated-embedding).

## Prerequisites

* A Pinecone account and API key ([get one](https://app.pinecone.io) or [view pricing](https://www.pinecone.io/pricing/)).

## Let your agent set it up

The quickest way to start is to let your AI coding agent do the setup: it designs your schema, ingests your data, and runs your first query, all conversationally.

The steps below cover Claude Code and Codex, which share the same Pinecone skills. Using Cursor or another agent? See [all supported AI coding tools](/integrations/ai-coding-tools) for the equivalent setup.

### 1. Set your API key and install the plugin

The plugin needs [Node.js](https://nodejs.org/) and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. The quickstart skill uses uv to run its bundled Python scripts.

> [tab] Claude Code
>
> ```bash Terminal theme={null}
> export PINECONE_API_KEY="YOUR_API_KEY"
> claude plugin install pinecone
> ```
>
> > [!NOTE]
> >
> > Installing the plugin requires access to the [official Anthropic marketplace](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace). Claude Code adds this access automatically the first time you start it. If the install fails with a `Marketplace "claude-plugins-official" not found` error, your network or your organization's Claude Code setup is probably blocking it.
>
> Restart Claude Code to activate the plugin.

> [tab] Codex
>
> ```bash Terminal theme={null}
> export PINECONE_API_KEY="YOUR_API_KEY"
> codex plugin marketplace add pinecone-io/pinecone-codex-plugin
> codex plugin add pinecone --marketplace pinecone-codex-plugins
> ```
>
> Start Codex from the same shell so it picks up the key. To install from the ChatGPT desktop app instead, see the [Codex plugin](/integrations/codex#installation) page.

### 2. Run the quickstart command

> [tab] Claude Code
>
> ```text Claude Code theme={null}
> /pinecone:quickstart
> ```

> [tab] Codex
>
> ```text Codex theme={null}
> $pinecone:quickstart
> ```

## Set it up yourself

Build the index with an SDK or the REST API. Its `chunk_text` field is set up the same way as the default `chunk_text` field in the [Pinecone console's create index form](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless). The steps run on sample documents, so you can finish first and then [use your own files](#use-your-own-files).

> [!NOTE]
>
> If you already generate your own embeddings, store them in a `dense_vector` field instead of declaring `embed`. For the steps, see [Bring your own vectors](/guides/search/bring-your-own-vectors).

### 1. Install an SDK

Install the Pinecone SDK for your language. Integrated embedding needs Python SDK `10.1.0` or later (Python 3.10+), Node.js SDK `9.1.0` or later (Node.js 22+), or Go SDK `7.1.0` or later (Go 1.25+, or Go 1.26+ for SDK `7.2.0` and later). The curl examples need no SDK, but they use `jq` to read the index host.

```bash Python theme={null}
pip install --upgrade "pinecone>=10.1.0"
```

```bash JavaScript theme={null}
npm install "@pinecone-database/pinecone@>=9.1.0"
```

```bash Go theme={null}
go get github.com/pinecone-io/go-pinecone/v7/pinecone@latest
```

The JavaScript examples use top-level `await`, so run them as an ES module, such as a `.mjs` file. The Go examples build one `main` function: the first block is the full program, and each later block adds to it.

### 2. Set your API key

Set your API key as an environment variable. The SDKs read it automatically, and the curl examples pass it in a header.

```bash Terminal theme={null}
export PINECONE_API_KEY="YOUR_API_KEY"
```

### 3. Create an index

Declare one `string` field with both `full_text_search` and `embed`. Pinecone indexes the field's text for keyword (BM25) search and embeds it for semantic search, so one field supports both. An empty `embed` config uses the default model, `llama-text-embed-v2`, at 1,024 dimensions. Only searchable fields go in the schema; other fields are stored on the documents as metadata (capped at 40 KB per document).

```python Python theme={null}
import os, time
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

schema = (
    SchemaBuilder()
      .add_string_field("chunk_text", full_text_search={"language": "en"}, embed={})
      .build()
)
if not pc.indexes.exists(name="quickstart"):
    pc.indexes.create(name="quickstart", schema=schema)

while not pc.indexes.describe(name="quickstart").status.ready:
    time.sleep(2)

index = pc.index(name="quickstart")
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone(); // reads PINECONE_API_KEY

await pc.indexes.create({
  name: 'quickstart',
  schema: {
    fields: {
      chunk_text: { type: 'string', fullTextSearch: { language: 'en' }, embed: {} },
    },
  },
  waitUntilReady: true,
  suppressConflicts: true,
});

const index = pc.index({ name: 'quickstart', namespace: '__default__' });
```

```go Go theme={null}
package main

import (
	"context"
	"log"
	"time"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func main() {
	ctx := context.Background()

	pc, err := pinecone.NewClient(pinecone.NewClientParams{}) // reads PINECONE_API_KEY
	if err != nil {
		log.Fatal(err)
	}

	if _, err := pc.DescribeIndex(ctx, "quickstart"); err != nil {
		language := "en"
		_, err = pc.CreateIndex(ctx, &pinecone.CreateIndexRequest{
			Name: "quickstart",
			Schema: pinecone.IndexSchema{
				Fields: map[string]pinecone.IndexSchemaField{
					"chunk_text": {String: &pinecone.StringField{
						FullTextSearch: &pinecone.FullTextSearchConfig{Language: &language},
						Embed:          &pinecone.EmbedConfig{},
					}},
				},
			},
		})
		if err != nil {
			log.Fatal(err)
		}
	}

	idx, err := pc.DescribeIndex(ctx, "quickstart")
	for err == nil && !idx.Status.Ready {
		time.Sleep(2 * time.Second)
		idx, err = pc.DescribeIndex(ctx, "quickstart")
	}
	if err != nil {
		log.Fatal(err)
	}

	index, err := pc.Index(pinecone.NewIndexConnParams{Host: idx.Host, Namespace: "__default__"})
	if err != nil {
		log.Fatal(err)
	}
}
```

```bash curl theme={null}
curl -X POST "https://api.pinecone.io/indexes" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "name": "quickstart",
    "schema": {
      "fields": {
        "chunk_text": {
          "type": "string",
          "full_text_search": { "language": "en" },
          "embed": {}
        }
      }
    }
  }'

# Wait until the index is ready, then save its host (requires jq)
until curl -s "https://api.pinecone.io/indexes/quickstart" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" | jq -e '.status.ready' > /dev/null; do
  sleep 2
done

INDEX_HOST=$(curl -s "https://api.pinecone.io/indexes/quickstart" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" | jq -r '.host')
```

### 4. Load sample documents

Each document has a required `_id`, plain text on the `chunk_text` field, and any metadata you want to filter on, like `category` here. Pinecone embeds the text on write, so you don't send vectors. Documents are indexed asynchronously, so the code waits 10 seconds before you search. If a search returns no results, wait a few seconds and run it again.

```python Python theme={null}
index.documents.upsert(
    namespace="__default__",
    documents=[
        {"_id": "1", "chunk_text": "Refund requests must be submitted within 30 days of purchase.", "category": "policy"},
        {"_id": "2", "chunk_text": "Enterprise customers get support with a 4-hour response time.", "category": "policy"},
        {"_id": "3", "chunk_text": "Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.", "category": "log"},
        {"_id": "4", "chunk_text": "To reset your password, open Settings and choose Security.", "category": "support"},
        {"_id": "5", "chunk_text": "Order 88231 shipped on 2026-08-20 via express courier.", "category": "order"},
    ],
)

time.sleep(10)  # documents are indexed asynchronously, so wait a moment
```

```javascript JavaScript theme={null}
await index.documents.upsert({
  documents: [
    { _id: '1', chunk_text: 'Refund requests must be submitted within 30 days of purchase.', category: 'policy' },
    { _id: '2', chunk_text: 'Enterprise customers get support with a 4-hour response time.', category: 'policy' },
    { _id: '3', chunk_text: 'Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.', category: 'log' },
    { _id: '4', chunk_text: 'To reset your password, open Settings and choose Security.', category: 'support' },
    { _id: '5', chunk_text: 'Order 88231 shipped on 2026-08-20 via express courier.', category: 'order' },
  ],
});

await new Promise((resolve) => setTimeout(resolve, 10000)); // documents are indexed asynchronously, so wait a moment
```

```go Go theme={null}
// Add to the main function:
_, err = index.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{
	Documents: []pinecone.Document{
		{"_id": "1", "chunk_text": "Refund requests must be submitted within 30 days of purchase.", "category": "policy"},
		{"_id": "2", "chunk_text": "Enterprise customers get support with a 4-hour response time.", "category": "policy"},
		{"_id": "3", "chunk_text": "Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.", "category": "log"},
		{"_id": "4", "chunk_text": "To reset your password, open Settings and choose Security.", "category": "support"},
		{"_id": "5", "chunk_text": "Order 88231 shipped on 2026-08-20 via express courier.", "category": "order"},
	},
})
if err != nil {
	log.Fatal(err)
}

time.Sleep(10 * time.Second) // documents are indexed asynchronously, so wait a moment
```

```bash curl theme={null}
curl -X POST "https://$INDEX_HOST/namespaces/__default__/documents/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "documents": [
      { "_id": "1", "chunk_text": "Refund requests must be submitted within 30 days of purchase.", "category": "policy" },
      { "_id": "2", "chunk_text": "Enterprise customers get support with a 4-hour response time.", "category": "policy" },
      { "_id": "3", "chunk_text": "Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.", "category": "log" },
      { "_id": "4", "chunk_text": "To reset your password, open Settings and choose Security.", "category": "support" },
      { "_id": "5", "chunk_text": "Order 88231 shipped on 2026-08-20 via express courier.", "category": "order" }
    ]
  }'

sleep 10  # documents are indexed asynchronously, so wait a moment
```

### 5. Search by meaning

Score by `embed` and pass the query as text. Pinecone embeds the query with the same model it used for the documents and ranks them by semantic similarity, so a question finds the right passage even when it shares no words with it. The `filter` limits the search to documents whose `category` metadata is `policy`.

```python Python theme={null}
meaning = index.documents.search(
    namespace="__default__",
    top_k=3,
    score_by=[{"type": "embed", "fields": ["chunk_text"], "query": "how do I get my money back?"}],
    filter={"category": {"$eq": "policy"}},
    include_fields=["chunk_text"],
)

for m in meaning.matches:
    print(m.id, f"{m.score:.3f}", m.chunk_text)
```

```javascript JavaScript theme={null}
const meaning = await index.documents.search({
  topK: 3,
  scoreBy: [{ type: 'embed', fields: ['chunk_text'], query: 'how do I get my money back?' }],
  filter: { category: { $eq: 'policy' } },
  includeFields: ['chunk_text'],
});

for (const m of meaning.matches) {
  console.log(m._id, m._score.toFixed(3), m.chunk_text);
}
```

```go Go theme={null}
// Add "fmt" to your imports, then add to the main function:
meaningQuery := "how do I get my money back?"
meaning, err := index.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
	TopK: 3,
	ScoreBy: []pinecone.DocumentScoringMethod{
		{Type: pinecone.DocumentScoringTypeEmbed, Fields: []string{"chunk_text"}, Query: &meaningQuery},
	},
	Filter:        map[string]interface{}{"category": map[string]interface{}{"$eq": "policy"}},
	IncludeFields: []string{"chunk_text"},
})
if err != nil {
	log.Fatal(err)
}

for _, m := range meaning.Matches {
	fmt.Printf("%s %.3f %s\n", m.Id, *m.Score, m.Fields["chunk_text"])
}
```

```bash curl theme={null}
curl -X POST "https://$INDEX_HOST/namespaces/__default__/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 3,
    "score_by": [
      { "type": "embed", "fields": ["chunk_text"], "query": "how do I get my money back?" }
    ],
    "filter": { "category": { "$eq": "policy" } },
    "include_fields": ["chunk_text"]
  }'
```

Only the two policy documents are searched, and the refund policy ranks first:

```text Output theme={null}
1 0.417 Refund requests must be submitted within 30 days of purchase.
2 0.089 Enterprise customers get support with a 4-hour response time.
```

### 6. Search by exact terms

Score by `text` to rank the same field by BM25 keyword relevance, so an exact identifier like `E1042` surfaces the document that contains it.

```python Python theme={null}
terms = index.documents.search(
    namespace="__default__",
    top_k=3,
    score_by=[{"type": "text", "fields": ["chunk_text"], "query": "E1042"}],
    include_fields=["chunk_text"],
)

for m in terms.matches:
    print(m.id, f"{m.score:.3f}", m.chunk_text)
```

```javascript JavaScript theme={null}
const terms = await index.documents.search({
  topK: 3,
  scoreBy: [{ type: 'text', fields: ['chunk_text'], query: 'E1042' }],
  includeFields: ['chunk_text'],
});

for (const m of terms.matches) {
  console.log(m._id, m._score.toFixed(3), m.chunk_text);
}
```

```go Go theme={null}
// Add to the main function:
termsQuery := "E1042"
terms, err := index.SearchDocuments(ctx, &pinecone.SearchDocumentsRequest{
	TopK: 3,
	ScoreBy: []pinecone.DocumentScoringMethod{
		{Type: pinecone.DocumentScoringTypeText, Fields: []string{"chunk_text"}, Query: &termsQuery},
	},
	IncludeFields: []string{"chunk_text"},
})
if err != nil {
	log.Fatal(err)
}

for _, m := range terms.Matches {
	fmt.Printf("%s %.3f %s\n", m.Id, *m.Score, m.Fields["chunk_text"])
}
```

```bash curl theme={null}
curl -X POST "https://$INDEX_HOST/namespaces/__default__/documents/search" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "top_k": 3,
    "score_by": [
      { "type": "text", "fields": ["chunk_text"], "query": "E1042" }
    ],
    "include_fields": ["chunk_text"]
  }'
```

Only the document that contains the term matches:

```text Output theme={null}
3 1.225 Error E1042: the connection timed out after 30 seconds. Retry with a longer timeout.
```

Either search accepts a `filter`. For phrase matching and boolean queries, see the [query syntax reference](/guides/search/full-text-search/query-syntax).

Each search returns its own ranking, and the scores are on different scales, so don't compare them across searches. To merge the two rankings into one list, use [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion) in your client.

## Use your own files

To search your own documents, upsert text from your files the same way. Pinecone doesn't extract or chunk files, so do those steps in your code before you upsert. If you already have embeddings for your files, see [Bring your own vectors](/guides/search/bring-your-own-vectors) instead.

### 1. Extract text from your files

Convert each file (PDF, DOCX, HTML, and so on) to plain text using a parser of your choice. The result should be a list of records, each with an ID and text, like the `docs` list below.

> [!NOTE]
>
> If you're searching images instead of text, embed them with a multimodal embedding model and store the vectors in a `dense_vector` field, as in [Bring your own vectors](/guides/search/bring-your-own-vectors).

```python Python theme={null}
docs = [
    {"id": "handbook-1", "text": "Refund requests must be submitted within 30 days of purchase."},
    {"id": "handbook-2", "text": "Enterprise customers get support with a 4-hour response time."},
    # ...extracted from your files
]
```

```javascript JavaScript theme={null}
const docs = [
  { id: 'handbook-1', text: 'Refund requests must be submitted within 30 days of purchase.' },
  { id: 'handbook-2', text: 'Enterprise customers get support with a 4-hour response time.' },
  // ...extracted from your files
];
```

```go Go theme={null}
// Add to the main function:
type Doc struct{ ID, Text string }

docs := []Doc{
	{"handbook-1", "Refund requests must be submitted within 30 days of purchase."},
	{"handbook-2", "Enterprise customers get support with a 4-hour response time."},
	// ...extracted from your files
}
```

### 2. Chunk the text

Split your text into smaller pieces so each one is a focused, searchable passage. The embedding model reads only the first 2,048 tokens of a value and truncates the rest, so keep chunks well under that. The function below is a simple length-based split. For smarter approaches (by sentence, token, or document structure), see [chunking strategies](https://www.pinecone.io/learn/chunking-strategies/). Each chunk ID starts with its source document's ID, so you can later [fetch, replace, or delete all of a document's chunks](/guides/data/manage-document-chunks) at once.

```python Python theme={null}
def chunk(text, size=500):
    return [text[i:i + size] for i in range(0, len(text), size)]

chunks = [
    {"id": f"{d['id']}#{i}", "text": part}
    for d in docs
    for i, part in enumerate(chunk(d["text"]))
]
```

```javascript JavaScript theme={null}
const chunk = (text, size = 500) => {
  const parts = [];
  for (let i = 0; i < text.length; i += size) parts.push(text.slice(i, i + size));
  return parts;
};

const chunks = docs.flatMap((d) =>
  chunk(d.text).map((part, i) => ({ id: `${d.id}#${i}`, text: part })),
);
```

```go Go theme={null}
// Add to the main function:
chunk := func(text string, size int) []string {
	runes := []rune(text)
	var parts []string
	for i := 0; i < len(runes); i += size {
		parts = append(parts, string(runes[i:min(i+size, len(runes))]))
	}
	return parts
}

var chunks []Doc
for _, d := range docs {
	for i, part := range chunk(d.Text, 500) {
		chunks = append(chunks, Doc{fmt.Sprintf("%s#%d", d.ID, i), part})
	}
}
```

### 3. Upsert the chunks

An index with an `embed` field accepts up to 96 documents per upsert, so send the chunks in batches. Then search them with the same calls as above.

```python Python theme={null}
for i in range(0, len(chunks), 96):
    index.documents.upsert(
        namespace="__default__",
        documents=[
            {"_id": c["id"], "chunk_text": c["text"]}
            for c in chunks[i:i + 96]
        ],
    )
```

```javascript JavaScript theme={null}
for (let i = 0; i < chunks.length; i += 96) {
  await index.documents.upsert({
    documents: chunks.slice(i, i + 96).map((c) => ({ _id: c.id, chunk_text: c.text })),
  });
}
```

```go Go theme={null}
// Add to the main function:
for i := 0; i < len(chunks); i += 96 {
	var batch []pinecone.Document
	for _, c := range chunks[i:min(i+96, len(chunks))] {
		batch = append(batch, pinecone.Document{"_id": c.ID, "chunk_text": c.Text})
	}
	if _, err := index.UpsertDocuments(ctx, &pinecone.UpsertDocumentsRequest{Documents: batch}); err != nil {
		log.Fatal(err)
	}
}
```

For a large dataset in Python, use [`batch_upsert`](/guides/optimize/increase-throughput#upsert-in-batches), which sends batches in parallel and returns any failed batches so you can retry them. You can't [bulk import](/guides/data/import-data) into an index with an `embed` field.

## Next steps

* [Design a schema](/guides/indexes/data-modeling) for your own data, with more than one searchable field.
* [Choose an embedding model or dimension](/guides/search/integrated-embedding), or add `sparse_embed` for learned-sparse search.
* [Filter by metadata](/guides/search/filter-by-metadata), including text-match filters on full-text search fields.
