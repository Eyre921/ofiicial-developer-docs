---
title: "Rerank results"
source: https://docs.pinecone.io/guides/search/rerank-results
path: guides/search/rerank-results
---

Improve retrieval quality by reranking initial search results with a hosted or external model to surface the most relevant matches for RAG.

Reranking is used as part of a two-stage vector retrieval process to improve the quality of results. You first query an index for a given number of relevant results, and then you send the query and results to a reranking model. The reranking model scores the results based on their semantic relevance to the query and returns a new, more accurate ranking. This approach is one of the simplest methods for improving quality in retrieval augmented generation (RAG) pipelines.

Pinecone provides [hosted reranking models](#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model or external model to rerank results as a standalone operation.

> [!NOTE]
>
> To run through this guide in your browser, see the [Rerank example notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-reranker.ipynb).

## Integrated reranking

To rerank initial results as an integrated part of a query, without any extra steps, use the [Search with text](/reference/api/latest/data-plane/search_records) operation with the `rerank` parameter, including the [hosted reranking model](#reranking-models) you want to use, the number of reranked results to return, and the fields to use for reranking, if different than the main query.

For example, the following code searches for the 3 records most semantically related to a query text and uses the hosted `bge-reranker-v2-m3` model to rerank the results and return only the 2 most relevant documents:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

ranked_results = index.search(
    namespace="example-namespace", 
    query={
        "inputs": {"text": "Disease prevention"}, 
        "top_k": 4
    },
    rerank={
        "model": "bge-reranker-v2-m3",
        "top_n": 2,
        "rank_fields": ["chunk_text"]
    },
    fields=["category", "chunk_text"]
)

print(ranked_results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

const response = await namespace.searchRecords({
  query: {
    topK: 2,
    inputs: { text: 'Disease prevention' },
  },
  fields: ['chunk_text', 'category'],
  rerank: {
    model: 'bge-reranker-v2-m3',
    rankFields: ['chunk_text'],
    topN: 2,
  },
});

console.log(response);
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;
import org.openapitools.db_data.client.model.SearchRecordsRequestRerank;
import org.openapitools.db_data.client.model.SearchRecordsResponse;

import java.util.*;

public class SearchText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-dense-java");

        String query = "Disease prevention";
        List<String> fields = new ArrayList<>();
        fields.add("category");
        fields.add("chunk_text");

        List<String>rankFields = new ArrayList<>();
        rankFields.add("chunk_text");
        SearchRecordsRequestRerank rerank = new SearchRecordsRequestRerank()
                .query(query)
                .model("bge-reranker-v2-m3")
                .topN(2)
                .rankFields(rankFields);

        SearchRecordsResponse recordsResponseReranked = index.searchRecordsByText(query,  "example-namespace", fields,4, null, rerank);

        System.out.println(recordsResponseReranked);
    }
}
```

```go Go theme={null}
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
    return string(bytes)
}

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

    topN := int32(2)
    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 3,
            Inputs: &map[string]interface{}{
                "text": "Disease prevention",
            },
        },
        Rerank: &pinecone.SearchRecordsRerank{
            Model:      "bge-reranker-v2-m3",
            TopN:       &topN,
            RankFields: []string{"chunk_text"},
        },
        Fields: &[]string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Printf(prettifyStruct(res))
}
```

```shell curl theme={null}
INDEX_HOST="INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE"
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "query": {
            "inputs": {"text": "Disease prevention"},
            "top_k": 4
        },
        "rerank": {
            "model": "bge-reranker-v2-m3",
            "top_n": 2,
            "rank_fields": ["chunk_text"]
        },
        "fields": ["category", "chunk_text"]
     }'
```

The response looks as follows. For each hit, the `_score` represents the relevance of a document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.

```python Python theme={null}
{'result': {'hits': [{'_id': 'rec3',
                      '_score': 0.004399413242936134,
                      'fields': {'category': 'immune system',
                                 'chunk_text': 'Rich in vitamin C and other '
                                                'antioxidants, apples '
                                                'contribute to immune health '
                                                'and may reduce the risk of '
                                                'chronic diseases.'}},
                     {'_id': 'rec4',
                      '_score': 0.0029235430993139744,
                      'fields': {'category': 'endocrine system',
                                 'chunk_text': 'The high fiber content in '
                                                'apples can also help regulate '
                                                'blood sugar levels, making '
                                                'them a favorable snack for '
                                                'people with diabetes.'}}]},
 'usage': {'embed_total_tokens': 8, 'read_units': 6, 'rerank_units': 1}}
```

```javascript JavaScript theme={null}
{
  result: { 
    hits: [ 
      {
        _id: 'rec3',
        _score: 0.004399413242936134,
        fields: {
          category: 'immune system',
          chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
        }
      },
      {
        _id: 'rec4',
        _score: 0.0029235430993139744,
        fields: {
          category: 'endocrine system',
          chunk_text: 'The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.'
        }
      }
    ]
  },
  usage: { 
    readUnits: 6, 
    embedTotalTokens: 8,
    rerankUnits: 1 
  }
}
```

```java Java theme={null}
class SearchRecordsResponse {
    result: class SearchRecordsResponseResult {
        hits: [class Hit {
            id: rec3
            score: 0.004399413242936134
            fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
            additionalProperties: null
        }, class Hit {
            id: rec4
            score: 0.0029235430993139744
            fields: {category=endocrine system, chunk_text=The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.}
            additionalProperties: null
        }]
        additionalProperties: null
    }
    usage: class SearchUsage {
        readUnits: 6
        embedTotalTokens: 13
        rerankUnits: 1
        additionalProperties: null
    }
    additionalProperties: null
}
```

```go Go theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "rec3",
        "_score": 0.13683891,
        "fields": {
          "category": "immune system",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
        }
      },
      {
        "_id": "rec4",
        "_score": 0.0029235430993139744,
        "fields": {
          "category": "endocrine system",
          "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
        }
      }
    ]
  },
  "usage": {
    "read_units": 6,
    "embed_total_tokens": 8,
    "rerank_units": 1
  }
}
```

```json curl theme={null}
{
    "result": {
        "hits": [
            {
                "_id": "rec3",
                "_score": 0.004433765076100826,
                "fields": {
                    "category": "immune system",
                    "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                }
            },
            {
                "_id": "rec4",
                "_score": 0.0029121784027665854,
                "fields": {
                    "category": "endocrine system",
                    "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
                }
            }
        ]
    },
    "usage": {
        "embed_total_tokens": 8,
        "read_units": 6,
        "rerank_units": 1
    }
}
```

## Standalone reranking

To rerank initial results as a standalone operation, use the [Rerank results](/reference/api/latest/inference/rerank-results) operation with the [hosted reranking model](#reranking-models) you want to use, the query results and the query, the number of ranked results to return, the field to use for reranking, and any other model-specific parameters.

For example, the following code uses the hosted `bge-reranker-v2-m3` model to rerank the values of the `documents.chunk_text` fields based on their relevance to the query and return only the 2 most relevant documents, along with their score:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

ranked_results = pc.inference.rerank(
    model="bge-reranker-v2-m3",
    query="What is AAPL's outlook, considering both product launches and market conditions?",
    documents=[
        {"id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
        {"id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
        {"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."},
    ],
    top_n=2,
    rank_fields=["chunk_text"],
    return_documents=True,
    parameters={
        "truncate": "END"
    }
)

print(ranked_results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

const rerankingModel = 'bge-reranker-v2-m3';

const query = "What is AAPL's outlook, considering both product launches and market conditions?";

const documents = [
  { id: 'vec2', chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market." },
  { id: 'vec3', chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production." },
  { id: 'vec1', chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones." },
];

const rerankOptions = {
  topN: 2,
  rankFields: ['chunk_text'],
  returnDocuments: true,
  parameters: {
    truncate: 'END'
  }, 
};

const rankedResults = await pc.inference.rerank(
  rerankingModel,
  query,
  documents,
  rerankOptions
);

console.log(rankedResults);
```

```java Java theme={null}
import io.pinecone.clients.Inference;
import io.pinecone.clients.Pinecone;
import org.openapitools.inference.client.model.RerankResult;
import org.openapitools.inference.client.ApiException;

import java.util.*;

public class RerankExample {
    public static void main(String[] args) throws ApiException {
        Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
        Inference inference = pc.getInferenceClient();

        // The model to use for reranking
        String model = "bge-reranker-v2-m3";

        // The query to rerank documents against
        String query = "What is AAPL's outlook, considering both product launches and market conditions?";

        // Add the documents to rerank
        List<Map<String, Object>> documents = new ArrayList<>();
        Map<String, Object> doc1 = new HashMap<>();
        doc1.put("id", "vec2");
        doc1.put("chunk_text", "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.");
        documents.add(doc1);

        Map<String, Object> doc2 = new HashMap<>();
        doc2.put("id", "vec3");
        doc2.put("chunk_text", "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production");
        documents.add(doc2);

        Map<String, Object> doc3 = new HashMap<>();
        doc3.put("id", "vec1");
        doc3.put("chunk_text", "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.");
        documents.add(doc3);

        // The fields to rank the documents by. If not provided, the default is "text"
        List<String> rankFields = Arrays.asList("chunk_text");

        // The number of results to return sorted by relevance. Defaults to the number of inputs
        int topN = 2;

        // Whether to return the documents in the response
        boolean returnDocuments = true;

        // Additional model-specific parameters for the reranker
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("truncate", "END");

        // Send ranking request
        RerankResult result = inference.rerank(model, query, documents, rankFields, topN, returnDocuments, parameters);

        // Get ranked data
        System.out.println(result.getData());
    }
}
```

```go Go theme={null}
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/pinecone-io/go-pinecone/v7/pinecone"
)

func prettifyStruct(obj interface{}) string {
	bytes, _ := json.MarshalIndent(obj, "", "  ")
	return string(bytes)
}

func main() {
	ctx := context.Background()

	pc, err := pinecone.NewClient(pinecone.NewClientParams{
		ApiKey: "YOUR_API_KEY",
	})
	if err != nil {
		log.Fatalf("Failed to create Client: %v", err)
	}

	rerankModel := "bge-reranker-v2-m3"
	topN := 2
	returnDocuments := true
	documents := []pinecone.Document{
		{"id": "vec2", "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
		{"id": "vec3", "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
		{"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."},
	}

	ranking, err := pc.Inference.Rerank(ctx, &pinecone.RerankRequest{
		Model:           rerankModel,
		Query:           "What is AAPL's outlook, considering both product launches and market conditions?",
		ReturnDocuments: &returnDocuments,
		TopN:            &topN,
		RankFields:      &[]string{"chunk_text"},
		Documents:       documents,
	})
	if err != nil {
		log.Fatalf("Failed to rerank: %v", err)
	}
	fmt.Printf(prettifyStruct(ranking))
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl https://api.pinecone.io/rerank \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -d '{
  "model": "bge-reranker-v2-m3",
  "query": "What is AAPL'\''s outlook, considering both product launches and market conditions?",
  "documents": [
    {"id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."},
    {"id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production."},
    {"id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."}
  ],
  "top_n": 2,
  "rank_fields": ["chunk_text"],
  "return_documents": true,
  "parameters": {
    "truncate": "END"
  }
}'
```

The response looks as follows. For each hit, the \_score represents the relevance of a document to the query, normalized between 0 and 1, with scores closer to 1 indicating higher relevance.

```python Python theme={null}
RerankResult(
  model='bge-reranker-v2-m3',
  data=[{
    index=0,
    score=0.004166256,
    document={
        id='vec2',
        chunk_text="Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."
    }
  },{
    index=2,
    score=0.0011513996,
    document={
        id='vec1',
        chunk_text='AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.'
    }
  }],
  usage={'rerank_units': 1}
)
```

```javascript JavaScript theme={null}
{
  model: 'bge-reranker-v2-m3',
  data: [
    { index: 0, score: 0.004166256, document: [id: 'vec2', chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market."] },
    { index: 2, score: 0.0011513996, document: [id: 'vec1', chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.'] }
  ],
  usage: { rerankUnits: 1 }
}
```

```java Java theme={null}
[class RankedDocument {
    index: 0
    score: 0.0063143647
    document: {id=vec2, chunk_text=Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.}
    additionalProperties: null
}, class RankedDocument {
    index: 2
    score: 0.0011513996
    document: {id=vec1, chunk_text=AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.}
    additionalProperties: null
}]
```

```go Go theme={null}
{
  "data": [
    {
      "document": {
        "id": "vec2",
        "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market."
      },
      "index": 0,
      "score": 0.0063143647
    },
    {
      "document": {
        "id": "vec1",
        "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones."
      },
      "index": 2,
      "score": 0.0011513996
    }
  ],
  "model": "bge-reranker-v2-m3",
  "usage": {
    "rerank_units": 1
  }
}
```

```json curl theme={null}
{
    "model": "bge-reranker-v2-m3",
    "data": [
        {
            "index": 0,
            "document": {
                "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                "id": "vec2"
            },
            "score": 0.007606672
        },
        {
            "index": 3,
            "document": {
                "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand# Build a knowledge retrieval agent
Source: https://docs.pinecone.io/guides/agents/build-a-knowledge-agent

Build an AI agent that uses Pinecone to retrieve knowledge and answer questions accurately, with Pinecone as a tool inside the agent.

Build an AI agent that uses Pinecone to retrieve knowledge and answer questions accurately. This demo shows Pinecone as a tool inside an agent, which is the same pattern you'd use in production.

> [!NOTE]
>
> This guide requires an [Anthropic](https://console.anthropic.com/) or [OpenAI](https://platform.openai.com/api-keys) API key alongside your Pinecone API key.

### 1. Install dependencies

```bash Anthropic (Claude) theme={null}
pip install --upgrade pinecone anthropic
```

```bash OpenAI theme={null}
pip install --upgrade pinecone openai
```

### 2. Create an index and load knowledge

Create a document index whose `content` field uses [integrated embedding](/guides/search/integrated-embedding), so Pinecone embeds the text for you, and load a small knowledge base. These are facts your LLM doesn't know on its own, so retrieval is the only way to answer accurately.

```python Anthropic (Claude) theme={null}
import anthropic
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key="{{YOUR_API_KEY}}")
llm = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")

# Create a document index that embeds the content field
if not pc.indexes.exists(name="knowledge"):
    pc.indexes.create(
        name="knowledge",
        schema=(
            SchemaBuilder()
              .add_string_field(name="content", embed={"model": "llama-text-embed-v2"})
              .build()
        ),
    )

index = pc.index(name="knowledge")

# Load your knowledge base
index.documents.upsert(
    namespace="docs",
    documents=[
        {"_id": "policy-1", "content": "Refund requests must be submitted within 30 days of purchase. After 30 days, only store credit is available.", "category": "policies"},
        {"_id": "policy-2", "content": "Enterprise customers get dedicated support with a 4-hour response time SLA. Standard support responds within 24 hours.", "category": "policies"},
        {"_id": "spec-1", "content": "The WonderVector 5000 supports up to 100,000 vectors per namespace with a maximum dimensionality of 4096.", "category": "specs"},
        {"_id": "spec-2", "content": "API rate limits: Free tier is 100 requests/minute, Pro tier is 1000 requests/minute, Enterprise is unlimited with fair use.", "category": "specs"},
        {"_id": "spec-3", "content": "Data is encrypted at rest using AES-256 and in transit using TLS 1.3. SOC2 Type II compliance is maintained.", "category": "security"},
        {"_id": "hr-1", "content": "New employees receive 15 days PTO in their first year, increasing to 20 days after 2 years and 25 days after 5 years.", "category": "hr"},
        {"_id": "hr-2", "content": "The company matches 401k contributions up to 4% of salary. Vesting is immediate for all employees.", "category": "hr"},
        {"_id": "proc-1", "content": "To request a new software license, submit a ticket in the IT portal. Approvals take 2-3 business days for standard software.", "category": "procedures"},
        {"_id": "proc-2", "content": "Production deployments require approval from the team lead and a passing CI/CD pipeline. Hotfixes can bypass the lead approval.", "category": "procedures"},
        {"_id": "proc-3", "content": "Vendor invoices over $10,000 require VP approval. Under $10,000 requires manager approval only.", "category": "procedures"},
    ],
)
```

```python OpenAI theme={null}
from openai import OpenAI
from pinecone import Pinecone, SchemaBuilder

pc = Pinecone(api_key="{{YOUR_API_KEY}}")
llm = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Create a document index that embeds the content field
if not pc.indexes.exists(name="knowledge"):
    pc.indexes.create(
        name="knowledge",
        schema=(
            SchemaBuilder()
              .add_string_field(name="content", embed={"model": "llama-text-embed-v2"})
              .build()
        ),
    )

index = pc.index(name="knowledge")

# Load your knowledge base
index.documents.upsert(
    namespace="docs",
    documents=[
        {"_id": "policy-1", "content": "Refund requests must be submitted within 30 days of purchase. After 30 days, only store credit is available.", "category": "policies"},
        {"_id": "policy-2", "content": "Enterprise customers get dedicated support with a 4-hour response time SLA. Standard support responds within 24 hours.", "category": "policies"},
        {"_id": "spec-1", "content": "The WonderVector 5000 supports up to 100,000 vectors per namespace with a maximum dimensionality of 4096.", "category": "specs"},
        {"_id": "spec-2", "content": "API rate limits: Free tier is 100 requests/minute, Pro tier is 1000 requests/minute, Enterprise is unlimited with fair use.", "category": "specs"},
        {"_id": "spec-3", "content": "Data is encrypted at rest using AES-256 and in transit using TLS 1.3. SOC2 Type II compliance is maintained.", "category": "security"},
        {"_id": "hr-1", "content": "New employees receive 15 days PTO in their first year, increasing to 20 days after 2 years and 25 days after 5 years.", "category": "hr"},
        {"_id": "hr-2", "content": "The company matches 401k contributions up to 4% of salary. Vesting is immediate for all employees.", "category": "hr"},
        {"_id": "proc-1", "content": "To request a new software license, submit a ticket in the IT portal. Approvals take 2-3 business days for standard software.", "category": "procedures"},
        {"_id": "proc-2", "content": "Production deployments require approval from the team lead and a passing CI/CD pipeline. Hotfixes can bypass the lead approval.", "category": "procedures"},
        {"_id": "proc-3", "content": "Vendor invoices over $10,000 require VP approval. Under $10,000 requires manager approval only.", "category": "procedures"},
    ],
)
```

> [!NOTE]
>
> Pinecone is eventually consistent. New documents may take a few seconds to become searchable.

### 3. Define Pinecone as a tool

Wrap Pinecone search in a function your agent can call. Drop this into any agent codebase to add knowledge retrieval. Run all snippets in the same Python session so `index` and `llm` stay in scope.

**Agent tool: `search_knowledge_base`**

```python Python theme={null}
def search_knowledge_base(query: str) -> str:
    """Search the knowledge base for relevant information."""
    results = index.documents.search(
        namespace="docs",
        top_k=3,
        score_by=[{"type": "embed", "fields": ["content"], "query": query}],
        # To scope by metadata, add filter={"category": {"$eq": "policies"}}
        include_fields=["content"],
    )
    return "\n\n".join(match.content for match in results.matches)
```

### 4. Wire the tool into your agent

Give your LLM the ability to call the search function when it needs information.

```python Anthropic (Claude) theme={null}
tools = [{
    "name": "search_knowledge_base",
    "description": "Search the company knowledge base for policies, specs, HR info, and procedures.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query"}
        },
        "required": ["query"]
    }
}]

def ask(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    # disable_parallel_tool_use keeps this loop simple: with parallel calls,
    # every tool_use block would need a matching tool_result in the next message
    response = llm.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        tools=tools,
        tool_choice={"type": "auto", "disable_parallel_tool_use": True},
        messages=messages
    )

    # If the model wants to use a tool, call it and return the result
    while response.stop_reason == "tool_use":
        tool_block = next(b for b in response.content if b.type == "tool_use")
        tool_result = search_knowledge_base(tool_block.input["query"])

        messages += [
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": tool_result
            }]}
        ]

        response = llm.messages.create(
            model="claude-sonnet-5",
            max_tokens=1024,
            tools=tools,
            tool_choice={"type": "auto", "disable_parallel_tool_use": True},
            messages=messages
        )

    return next(b.text for b in response.content if hasattr(b, "text"))
```

```python OpenAI theme={null}
import json

tools = [{
    "type": "function",
    "function": {
        "name": "search_knowledge_base",
        "description": "Search the company knowledge base for policies, specs, HR info, and procedures.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The search query"}
            },
            "required": ["query"]
        }
    }
}]

def ask(question: str) -> str:
    messages = [{"role": "user", "content": question}]

    # parallel_tool_calls=False keeps this loop simple: with parallel calls,
    # every tool call would need a matching tool message in the next turn
    response = llm.chat.completions.create(
        model="gpt-4o",
        tools=tools,
        parallel_tool_calls=False,
        messages=messages
    )

    # If the model wants to use a tool, call it and return the result
    while response.choices[0].finish_reason == "tool_calls":
        tool_call = response.choices[0].message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        tool_result = search_knowledge_base(args["query"])

        messages += [
            response.choices[0].message,
            {"role": "tool", "tool_call_id": tool_call.id, "content": tool_result}
        ]

        response = llm.chat.completions.create(
            model="gpt-4o",
            tools=tools,
            parallel_tool_calls=False,
            messages=messages
        )

    return response.choices[0].message.content
```

### 5. Ask your agent a question

```python theme={null}
print(ask("What's the refund policy?"))
```

If the agent says it can't find the information, wait a few seconds and retry. Pinecone is eventually consistent, so freshly upserted documents take a moment to become searchable.

Your agent searches Pinecone, retrieves the relevant policy, and answers:

```console Output theme={null}
Refund requests must be submitted within 30 days of purchase. After that
30-day window, you can still receive store credit but not a direct refund.
```

Try a few more questions:

```python theme={null}
print(ask("How much PTO do new employees get?"))
print(ask("What approval do I need for a $15,000 vendor invoice?"))
```

> [!NOTE]
>
> **What just happened:** Your LLM received a question, decided it needed more information, and called the `search_knowledge_base` tool. Pinecone embedded the query and returned the most relevant documents, and the LLM synthesized an accurate answer from the retrieved context. Production RAG agents use this same pattern, and the `search_knowledge_base` function works in any agent framework.

### Next steps

> [card] [Use the MCP server](/guides/agents/mcp-server)
>
> Give agents Pinecone access over the Model Context Protocol

> [card] [Search methods](/guides/search/search-overview)
>
> Explore semantic, hybrid, and full-text search

> [card] [Data modeling](/guides/indexes/data-modeling)
>
> Model your data for efficient retrieval
