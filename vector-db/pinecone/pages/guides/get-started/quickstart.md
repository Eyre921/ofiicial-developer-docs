---
title: "Quickstart"
source: https://docs.pinecone.io/guides/get-started/quickstart
path: guides/get-started/quickstart
---

Add Pinecone to your AI agent or app in minutes. Build a knowledge retrieval agent, use your IDE assistant, or integrate the SDK directly.

Get Pinecone running in your agent or app. Install the Pinecone plugin for your AI coding tool to get started instantly, or follow a step-by-step path below.

## Agent / LLM? Start here

If you're an AI agent or LLM reading this page to generate Pinecone code, here's the full working pattern as a single runnable script.

```python theme={null}
import time
from pinecone import Pinecone

pc = Pinecone(api_key="{{YOUR_API_KEY}}")

# Use create_index_for_model, not the dimension-based create_index
if not pc.has_index("quickstart"):
    pc.create_index_for_model(
        name="quickstart",
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "llama-text-embed-v2",
            "field_map": {"text": "content"}
        }
    )

index = pc.Index("quickstart")

# Use upsert_records, not upsert(); keyword args required in SDK v9+; each record needs _id + the field_map field
index.upsert_records(
    namespace="docs",
    records=[
        {"_id": "rec1", "content": "Refund requests must be submitted within 30 days.", "category": "policy"},
        {"_id": "rec2", "content": "Enterprise support responds within 4 hours.", "category": "policy"},
        {"_id": "rec3", "content": "New employees receive 15 days PTO in year one.", "category": "hr"},
        {"_id": "rec4", "content": "Production deployments require team lead approval.", "category": "ops"},
        {"_id": "rec5", "content": "API rate limit: 1000 requests/minute on Pro tier.", "category": "specs"},
    ]
)

time.sleep(5)  # records take a few seconds to become searchable

# Use search() with inputs, not query() with vector=
results = index.search(
    namespace="docs",
    query={"top_k": 5, "inputs": {"text": "what is the refund policy"}},
    rerank={
        "model": "bge-reranker-v2-m3",
        "top_n": 3,
        "rank_fields": ["content"]
    }
)

for hit in results["result"]["hits"]:
    print(f"{hit.score:.2f}  {hit.fields['content']}")
```

***

## Get set up

To get started, you'll need a Pinecone account and API key.

### 1. Create a Pinecone account

If you're new to Pinecone, sign up at [app.pinecone.io](https://app.pinecone.io) and choose a plan:

* [Starter plan](https://pinecone.io/pricing/) (free): Free access to most features, but you're limited to one cloud region and need to stay under Starter plan [limits](/reference/api/database-limits).

* [Builder plan](https://pinecone.io/pricing/) (\$20/month): Higher quotas than Starter and predictable flat pricing with no usage overages, plus the ability to create indexes in any supported cloud region. Ideal for small production apps.

* [Standard plan trial](/guides/organizations/manage-billing/standard-trial): 21 days and \$300 in credits with access to Standard plan [features](https://www.pinecone.io/pricing/) and [higher limits](/reference/api/database-limits) that let you test Pinecone at scale.

<Note>
  If you're already on a Starter plan, you can [upgrade to Builder](/guides/organizations/manage-billing/upgrade-billing-plan) at any time, or activate a Standard plan trial (one trial per organization).
</Note>

After signing up, you'll receive an API key in the console. Save this key. You'll need it to authenticate your requests to Pinecone.

### 2. Get a Pinecone API key

Create a new API key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys), or use the widget below to generate a key. If you don't have a Pinecone account, the widget will sign you up for the free [Starter plan](https://www.pinecone.io/pricing/).

<div>
  <div>
    <div>
      <div />
    </div>
  </div>
</div>

Your generated API key:

```shell theme={null}
"{{YOUR_API_KEY}}"
```

## Fastest: use your AI coding tool

Install the Pinecone plugin for your AI coding tool, then run the quickstart command. The plugin gives your agent up-to-date Pinecone API references, skills, and a bundled MCP server. The quickstart command walks you through setup with the official [Pinecone CLI](/reference/cli/quickstart) before generating and running sample code, so you end up with a reproducible setup instead of pasted snippets.

<Tabs>
  <Tab title="Claude Code">
    Set your API key, then install the [Pinecone plugin for Claude Code](/integrations/claude-code):

    ```shell theme={null}
    export PINECONE_API_KEY="{{YOUR_API_KEY}}"
    claude plugin install pinecone
    ```

    Start Claude Code and run the quickstart command:

    ```text theme={null}
    /pinecone:quickstart
    ```

    The plugin also includes other slash commands, such as `/pinecone:query`, for interactively querying your indexes.
  </Tab>

  <Tab title="Cursor">
    Add your Pinecone API key to a `.env` file at your workspace root:

    ```text theme={null}
    PINECONE_API_KEY={{YOUR_API_KEY}}
    ```

    Install the [Pinecone plugin for Cursor](/integrations/cursor) from the [Cursor Marketplace](https://cursor.com/marketplace/pinecone), or in Cursor chat run:

    ```text theme={null}
    /add-plugin pinecone
    ```

    Then run the quickstart command in Cursor Agent chat:

    ```text theme={null}
    /pinecone-quickstart
    ```
  </Tab>

  <Tab title="Other IDEs">
    Install [Pinecone Agent Skills](/integrations/agent-skills), then ask your agent to get started:

    ```bash theme={null}
    npx skills add pinecone-io/skills
    ```

    ```text theme={null}
    Help me get started with Pinecone. Create a serverless index with
    integrated embedding, upsert some sample data, and run a search.
    ```
  </Tab>
</Tabs>

<Tip>
  To drive the same setup yourself without an AI tool, use the [Pinecone CLI](/reference/cli/quickstart) directly. For full MCP server setup (index management, search, and docs access from your IDE), see [Use the Pinecone MCP server](/guides/operations/mcp-server).
</Tip>

## Choose your path

<Note>
  **Records or documents?** There are two ways to model data in Pinecone, and the choice is made when you create the index. An index created with a dense or sparse vector type holds [records](/guides/get-started/concepts#record), the path the steps below follow using integrated embedding (`create_index_for_model` + `upsert_records` + `search`). An index created with a document schema holds [documents](/guides/get-started/concepts#document) and supports [full-text search](/guides/search/full-text-search) with BM25 ranking and Lucene queries (public preview, with REST and Python SDK support). If keyword and phrase matching matters to your search, or you need more than one ranking signal in a single index, start from [full-text search](/guides/search/full-text-search) instead. To compare the two models, see [Data modeling](/guides/index-data/data-modeling).
</Note>

<CardGroup>
  <Card title="Agent" icon="robot" href="#build-a-knowledge-retrieval-agent">
    Build a knowledge retrieval agent with Pinecone as a tool. \~80 lines of Python.
  </Card>

  <Card title="IDE assistant" icon="wand-magic-sparkles" href="#fastest-use-your-ai-coding-tool">
    Let Claude Code, Cursor, or Gemini CLI build it for you.
  </Card>

  <Card title="SDK" icon="code" href="#integrate-the-sdk-directly">
    Integrate Pinecone directly with Python, JavaScript, Java, or Go.
  </Card>

  <Card title="No-code" icon="diagram-project" href="#no-code-with-n8n">
    Build a workflow in n8n without writing code.
  </Card>
</CardGroup>

***

## Build a knowledge retrieval agent

Build an AI agent that uses Pinecone to retrieve knowledge and answer questions accurately. This demo shows Pinecone as a tool inside an agent, which is the same pattern you'd use in production.

<Note>
  This path requires an [Anthropic](https://console.anthropic.com/) or [OpenAI](https://platform.openai.com/api-keys) API key alongside your Pinecone API key. If you don't have one, try the [IDE assistant](#fastest-use-your-ai-coding-tool) or [SDK](#integrate-the-sdk-directly) path instead.
</Note>

<Steps>
  <Step title="Install dependencies">
    <CodeGroup>
      ```bash Anthropic (Claude) theme={null}
      pip install pinecone anthropic
      ```

      ```bash OpenAI theme={null}
      pip install pinecone openai
      ```
    </CodeGroup>
  </Step>

  <Step title="Create an index and load knowledge">
    Create a Pinecone index with [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding) and load a small knowledge base. These are facts your LLM doesn't know on its own, so retrieval is the only way to answer accurately.

    <CodeGroup>
      ```python Anthropic (Claude) theme={null}
      import anthropic
      from pinecone import Pinecone

      pc = Pinecone(api_key="{{YOUR_API_KEY}}")
      llm = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")

      # Create an index with integrated embedding
      if not pc.has_index("knowledge"):
          pc.create_index_for_model(
              name="knowledge",
              cloud="aws",
              region="us-east-1",
              embed={
                  "model": "llama-text-embed-v2",
                  "field_map": {"text": "content"}
              }
          )

      index = pc.Index("knowledge")

      # Load your knowledge base
      index.upsert_records(
          namespace="docs",
          records=[
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
          ]
      )
      ```

      ```python OpenAI theme={null}
      from openai import OpenAI
      from pinecone import Pinecone

      pc = Pinecone(api_key="{{YOUR_API_KEY}}")
      llm = OpenAI(api_key="YOUR_OPENAI_API_KEY")

      # Create an index with integrated embedding
      if not pc.has_index("knowledge"):
          pc.create_index_for_model(
              name="knowledge",
              cloud="aws",
              region="us-east-1",
              embed={
                  "model": "llama-text-embed-v2",
                  "field_map": {"text": "content"}
              }
          )

      index = pc.Index("knowledge")

      # Load your knowledge base
      index.upsert_records(
          namespace="docs",
          records=[
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
          ]
      )
      ```
    </CodeGroup>

    <Note>
      Pinecone is eventually consistent. New records may take a few seconds to become searchable.
    </Note>
  </Step>

  <Step title="Define Pinecone as a tool">
    Wrap Pinecone search in a function your agent can call. Drop this into any agent codebase to add knowledge retrieval. Run all snippets in the same Python session so `index` and `llm` stay in scope.

    <div>
      **Agent tool: `search_knowledge_base`**

      ```python Python theme={null}
      def search_knowledge_base(query: str) -> str:
          """Search the knowledge base for relevant information."""
          results = index.search(
              namespace="docs",
              # To scope by metadata, add "filter": {"category": {"$eq": "policies"}} to the query dict
              query={"top_k": 3, "inputs": {"text": query}},
              rerank={
                  "model": "bge-reranker-v2-m3",
                  "top_n": 3,
                  "rank_fields": ["content"]
              }
          )
          return "\n\n".join(
              hit.fields["content"]
              for hit in results["result"]["hits"]
          )
      ```
    </div>
  </Step>

  <Step title="Wire the tool into your agent">
    Give your LLM the ability to call the search function when it needs information.

    <CodeGroup>
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
              model="claude-sonnet-4-5",
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
                  model="claude-sonnet-4-5",
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
    </CodeGroup>
  </Step>

  <Step title="Ask your agent a question">
    ```python theme={null}
    print(ask("What's the refund policy?"))
    ```

    If the agent says it can't find the information, wait a few seconds and retry. Pinecone is eventually consistent, so freshly upserted records take a moment to become searchable.

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
  </Step>
</Steps>

<Note>
  **What just happened:** Your LLM received a question, decided it needed more information, and called the `search_knowledge_base` tool. Pinecone returned the most relevant records with reranking, and the LLM synthesized an accurate answer from the retrieved context. Production RAG agents use this same pattern, and the `search_knowledge_base` function works in any agent framework.
</Note>

### Next steps

<CardGroup>
  <Card title="Build a RAG chatbot" icon="comments" href="/guides/get-started/build-a-rag-chatbot">
    Add conversation history, streaming, and a web UI
  </Card>

  <Card title="Search methods" icon="magnifying-glass" href="/guides/search/search-overview">
    Explore semantic, hybrid, and full-text search
  </Card>

  <Card title="Data modeling" icon="table" href="/guides/index-data/data-modeling">
    Model your data for efficient retrieval
  </Card>
</CardGroup>

***

## Integrate the SDK directly

Integrate Pinecone directly into your application. Use these SDK calls wherever your code needs knowledge retrieval, whether that's an agent, a backend service, or a standalone script.

<Tip>
  To get started in your browser, use the [Quickstart colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-quickstart.ipynb).
</Tip>

### 1. Install an SDK

<CodeGroup>
  ```shell Python theme={null}
  pip install pinecone
  ```

  ```shell JavaScript theme={null}
  npm install @pinecone-database/pinecone
  ```

  ```shell Java theme={null}
  # Maven
  <dependency>
    <groupId>io.pinecone</groupId>
    <artifactId>pinecone-client</artifactId>
    <version>5.0.0</version>
  </dependency>

  # Gradle
  implementation "io.pinecone:pinecone-client:5.0.0"
  ```

  ```shell Go theme={null}
  go get github.com/pinecone-io/go-pinecone/v4/pinecone
  ```
</CodeGroup>

### 2. Create an index

Create an [index with integrated embedding](/guides/index-data/create-an-index#create-an-index-for-dense-vectors) so you can upsert and search with text. Pinecone generates the vectors for you.

<Note>
  If you prefer to use external embedding models, see [Bring your own vectors](/guides/index-data/indexing-overview#bring-your-own-vectors).
</Note>

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="{{YOUR_API_KEY}}")

index_name = "quickstart-py"
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model":"llama-text-embed-v2",
            "field_map":{"text": "chunk_text"}
        }
    )
```

<Accordion title="JavaScript, Java, and Go">
  <CodeGroup>
    ```javascript JavaScript theme={null}
    import { Pinecone } from '@pinecone-database/pinecone'

    const pc = new Pinecone({ apiKey: '{{YOUR_API_KEY}}' });

    const indexName = 'quickstart-js';
    await pc.createIndexForModel({
      name: indexName,
      cloud: 'aws',
      region: 'us-east-1',
      embed: {
        model: 'llama-text-embed-v2',
        fieldMap: { text: 'chunk_text' },
      },
      waitUntilReady: true,
    });
    ```

    ```java Java theme={null}
    import io.pinecone.clients.Index;
    import io.pinecone.clients.Pinecone;
    import org.openapitools.db_control.client.ApiException;
    import org.openapitools.db_control.client.model.CreateIndexForModelRequest;
    import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
    import org.openapitools.db_control.client.model.DeletionProtection;
    import org.openapitools.db_control.client.model.IndexModel;
    import org.openapitools.db_data.client.model.SearchRecordsRequestQuery;
    import org.openapitools.db_data.client.model.SearchRecordsResponse;
    import io.pinecone.proto.DescribeIndexStatsResponse;

    import java.util.*;

    public class Quickstart {
        public static void main(String[] args) throws ApiException {
            Pinecone pc = new Pinecone.Builder("{{YOUR_API_KEY}}").build();
            String indexName = "quickstart-java";
            String region = "us-east-1";
            HashMap<String, String> fieldMap = new HashMap<>();
            fieldMap.put("text", "chunk_text");
            CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                    .model("llama-text-embed-v2")
                    .fieldMap(fieldMap);
            IndexModel index = pc.createIndexForModel(
                    indexName,
                    CreateIndexForModelRequest.CloudEnum.AWS,
                    region,
                    embed,
                    DeletionProtection.DISABLED,
                    null
            );
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

        "github.com/pinecone-io/go-pinecone/v4/pinecone"
    )

    func main() {
        ctx := context.Background()

        pc, err := pinecone.NewClient(pinecone.NewClientParams{
            ApiKey: "{{YOUR_API_KEY}}",
        })
        if err != nil {
            log.Fatalf("Failed to create Client: %v", err)
        }

      	indexName := "quickstart-go"
        index, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
            Name:   indexName,
            Cloud:  pinecone.Aws,
            Region: "us-east-1",
            Embed: pinecone.CreateIndexForModelEmbed{
                Model:    "llama-text-embed-v2",
                FieldMap: map[string]interface{}{"text": "chunk_text"},
            },
        })
        if err != nil {
            log.Fatalf("Failed to create serverless index: %v", err)
        } else {
            fmt.Printf("Successfully created serverless index: %v", index.Name)
        }
    }

    func prettifyStruct(obj interface{}) string {
      	bytes, _ := json.MarshalIndent(obj, "", "  ")
        return string(bytes)
    }
    ```
  </CodeGroup>
</Accordion>

### 3. Upsert data

Load records into your index. Each record has an ID, text content, and optional metadata. Pinecone converts the text to vectors automatically using the integrated embedding model.

```python Python [expandable] theme={null}
index = pc.Index(index_name)

index.upsert_records(
    namespace="example-namespace",
    records=[
        {"_id": "rec1", "chunk_text": "The Eiffel Tower was completed in 1889 and stands in Paris, France.", "category": "history"},
        {"_id": "rec2", "chunk_text": "Photosynthesis allows plants to convert sunlight into energy.", "category": "science"},
        {"_id": "rec3", "chunk_text": "Albert Einstein developed the theory of relativity.", "category": "science"},
        {"_id": "rec4", "chunk_text": "The mitochondrion is often called the powerhouse of the cell.", "category": "biology"},
        {"_id": "rec5", "chunk_text": "Shakespeare wrote many famous plays, including Hamlet and Macbeth.", "category": "literature"},
        {"_id": "rec6", "chunk_text": "The Great Wall of China was built to protect against invasions.", "category": "history"},
        {"_id": "rec7", "chunk_text": "The Pyramids of Giza are among the Seven Wonders of the Ancient World.", "category": "history"},
        {"_id": "rec8", "chunk_text": "Leonardo da Vinci painted the Mona Lisa.", "category": "art"},
        {"_id": "rec9", "chunk_text": "The internet revolutionized communication and information sharing.", "category": "technology"},
        {"_id": "rec10", "chunk_text": "Renewable energy sources include wind, solar, and hydroelectric power.", "category": "energy"},
    ]
)
```

<Accordion title="JavaScript, Java, and Go">
  <CodeGroup>
    ```javascript JavaScript [expandable] theme={null}
    const namespace = pc.index(indexName).namespace("example-namespace");

    await namespace.upsertRecords({ records: [
      {"_id": "rec1", "chunk_text": "The Eiffel Tower was completed in 1889 and stands in Paris, France.", "category": "history"},
      {"_id": "rec2", "chunk_text": "Photosynthesis allows plants to convert sunlight into energy.", "category": "science"},
      {"_id": "rec3", "chunk_text": "Albert Einstein developed the theory of relativity.", "category": "science"},
      {"_id": "rec4", "chunk_text": "The mitochondrion is often called the powerhouse of the cell.", "category": "biology"},
      {"_id": "rec5", "chunk_text": "Shakespeare wrote many famous plays, including Hamlet and Macbeth.", "category": "literature"},
      {"_id": "rec6", "chunk_text": "The Great Wall of China was built to protect against invasions.", "category": "history"},
      {"_id": "rec7", "chunk_text": "The Pyramids of Giza are among the Seven Wonders of the Ancient World.", "category": "history"},
      {"_id": "rec8", "chunk_text": "Leonardo da Vinci painted the Mona Lisa.", "category": "art"},
      {"_id": "rec9", "chunk_text": "The internet revolutionized communication and information sharing.", "category": "technology"},
      {"_id": "rec10", "chunk_text": "Renewable energy sources include wind, solar, and hydroelectric power.", "category": "energy"},
    ] });
    ```

    ```java Java [expandable] theme={null}
    // Add to the Quickstart class:
    Index index = pc.getIndexConnection(indexName);

    ArrayList<Map<String, String>> upsertRecords = new ArrayList<>();
    String[][] data = {
        {"rec1", "The Eiffel Tower was completed in 1889 and stands in Paris, France.", "history"},
        {"rec2", "Photosynthesis allows plants to convert sunlight into energy.", "science"},
        {"rec3", "Albert Einstein developed the theory of relativity.", "science"},
        {"rec4", "The mitochondrion is often called the powerhouse of the cell.", "biology"},
        {"rec5", "Shakespeare wrote many famous plays, including Hamlet and Macbeth.", "literature"},
        {"rec6", "The Great Wall of China was built to protect against invasions.", "history"},
        {"rec7", "The Pyramids of Giza are among the Seven Wonders of the Ancient World.", "history"},
        {"rec8", "Leonardo da Vinci painted the Mona Lisa.", "art"},
        {"rec9", "The internet revolutionized communication and information sharing.", "technology"},
        {"rec10", "Renewable energy sources include wind, solar, and hydroelectric power.", "energy"},
    };
    for (String[] row : data) {
        HashMap<String, String> record = new HashMap<>();
        record.put("_id", row[0]);
        record.put("chunk_text", row[1]);
        record.put("category", row[2]);
        upsertRecords.add(record);
    }
    index.upsertRecords("example-namespace", upsertRecords);
    ```

    ```go Go [expandable] theme={null}
    // Add to the main function:
    idxConnection, err := pc.IndexFromName(ctx, indexName)
    if err != nil {
        log.Fatalf("Failed to get index connection: %v", err)
    }

    records := []pinecone.UpsertRecord{
        {Id: "rec1", Fields: map[string]interface{}{"chunk_text": "The Eiffel Tower was completed in 1889 and stands in Paris, France.", "category": "history"}},
        {Id: "rec2", Fields: map[string]interface{}{"chunk_text": "Photosynthesis allows plants to convert sunlight into energy.", "category": "science"}},
        {Id: "rec3", Fields: map[string]interface{}{"chunk_text": "Albert Einstein developed the theory of relativity.", "category": "science"}},
        {Id: "rec4", Fields: map[string]interface{}{"chunk_text": "The mitochondrion is often called the powerhouse of the cell.", "category": "biology"}},
        {Id: "rec5", Fields: map[string]interface{}{"chunk_text": "Shakespeare wrote many famous plays, including Hamlet and Macbeth.", "category": "literature"}},
        {Id: "rec6", Fields: map[string]interface{}{"chunk_text": "The Great Wall of China was built to protect against invasions.", "category": "history"}},
        {Id: "rec7", Fields: map[string]interface{}{"chunk_text": "The Pyramids of Giza are among the Seven Wonders of the Ancient World.", "category": "history"}},
        {Id: "rec8", Fields: map[string]interface{}{"chunk_text": "Leonardo da Vinci painted the Mona Lisa.", "category": "art"}},
        {Id: "rec9", Fields: map[string]interface{}{"chunk_text": "The internet revolutionized communication and information sharing.", "category": "technology"}},
        {Id: "rec10", Fields: map[string]interface{}{"chunk_text": "Renewable energy sources include wind, solar, and hydroelectric power.", "category": "energy"}},
    }
    err = idxConnection.UpsertRecords(ctx, "example-namespace", records)
    if err != nil {
        log.Fatalf("Failed to upsert records: %v", err)
    }
    ```
  </CodeGroup>
</Accordion>

<Note>
  Pinecone is eventually consistent. New records may take a few seconds to become searchable.
</Note>

### 4. Search and rerank

Search the index for records semantically similar to a query, then [rerank](/guides/search/rerank-results) for more accurate results.

```python Python theme={null}
query = "Famous historical structures and monuments"

results = index.search(
    namespace="example-namespace",
    query={
        "top_k": 10,
        "inputs": {"text": query}
    },
    rerank={
        "model": "bge-reranker-v2-m3",
        "top_n": 5,
        "rank_fields": ["chunk_text"]
    }
)

for hit in results["result"]["hits"]:
    print(f"score: {round(hit.score, 2):<5} | {hit.fields['chunk_text']}")
```

```console Output theme={null}
score: 0.11  | The Eiffel Tower was completed in 1889 and stands in Paris, France.
score: 0.06  | The Great Wall of China was built to protect against invasions.
score: 0.02  | The Pyramids of Giza are among the Seven Wonders of the Ancient World.
score: 0.01  | Leonardo da Vinci painted the Mona Lisa.
score: 0.0   | Shakespeare wrote many famous plays, including Hamlet and Macbeth.
```

<Accordion title="JavaScript, Java, and Go">
  <CodeGroup>
    ```javascript JavaScript theme={null}
    const query = 'Famous historical structures and monuments';

    const results = await namespace.searchRecords({
      query: {
        topK: 10,
        inputs: { text: query },
      },
      rerank: {
        model: 'bge-reranker-v2-m3',
        topN: 5,
        rankFields: ['chunk_text'],
      },
    });

    results.result.hits.forEach(hit => {
      console.log(`score: ${hit._score.toFixed(2)}, text: ${hit.fields.chunk_text}`);
    });
    ```

    ```java Java theme={null}
    // Add to the Quickstart class:
    String query = "Famous historical structures and monuments";
    List<String> fields = new ArrayList<>();
    fields.add("category");
    fields.add("chunk_text");

    List<String> rankFields = new ArrayList<>();
    rankFields.add("chunk_text");
    SearchRecordsRequestRerank rerank = new SearchRecordsRequestRerank()
            .query(query)
            .model("bge-reranker-v2-m3")
            .topN(5)
            .rankFields(rankFields);

    SearchRecordsResponse response = index.searchRecordsByText(
        query, "example-namespace", fields, 10, null, rerank
    );
    System.out.println(response);
    ```

    ```go Go theme={null}
    // Add to the main function:
    query := "Famous historical structures and monuments"
    topN := int32(5)

    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 10,
            Inputs: &map[string]interface{}{
                "text": query,
            },
        },
        Rerank: &pinecone.SearchRecordsRerank{
            Model:      "bge-reranker-v2-m3",
            TopN:       &topN,
            RankFields: []string{"chunk_text"},
        },
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Printf(prettifyStruct(res))
    ```
  </CodeGroup>
</Accordion>

### 5. Clean up

When you no longer need the example index, delete it:

```python Python theme={null}
pc.delete_index(index_name)
```

<Accordion title="JavaScript, Java, and Go">
  <CodeGroup>
    ```javascript JavaScript theme={null}
    await pc.deleteIndex(indexName);
    ```

    ```java Java theme={null}
    pc.deleteIndex(indexName);
    ```

    ```go Go theme={null}
    err = pc.DeleteIndex(ctx, indexName)
    if err != nil {
        log.Fatalf("Failed to delete index: %v", err)
    }
    ```
  </CodeGroup>
</Accordion>

<Tip>
  For production indexes, consider [enabling deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).
</Tip>

### Next steps

<CardGroup>
  <Card title="Index data" icon="book-open" href="/guides/index-data/indexing-overview">
    Learn more about storing data in Pinecone
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/guides/search/search-overview">
    Explore different forms of vector search
  </Card>

  <Card title="Optimize" icon="rocket" href="/guides/optimize">
    Find out how to improve performance
  </Card>
</CardGroup>

***

## No-code with n8n

Create an AI workflow that uses Pinecone for knowledge retrieval without writing any code.

Use [n8n](https://docs.n8n.io/choose-n8n/) to create a workflow that downloads files via HTTP and lets you chat with them using Pinecone Database and OpenAI.

<Tip>
  If you're not interested in chunking and embedding your own data, [use n8n with Pinecone Assistant](/guides/assistant/quickstart/n8n-quickstart) instead.
</Tip>

### 1. Get an OpenAI API key

Create a new API key in the [OpenAI console](https://platform.openai.com/api-keys).

### 2. Create an index

[Create an index](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless) in the Pinecone console:

* Name your index `n8n-dense-index`
* Under **Configuration**, check **Custom settings** and set **Dimension** to 1536.
* Leave everything else as default.

### 3. Set up n8n

<Steps>
  <Step title="Create a new workflow">
    In your n8n account, [create a new workflow](https://docs.n8n.io/workflows/create/).
  </Step>

  <Step title="Import a workflow template">
    Copy this workflow template URL:

    ```shell theme={null}
    https://raw.githubusercontent.com/pinecone-io/n8n-templates/refs/heads/main/database-quickstart/database-quickstart.json
    ```

    Paste the URL into the workflow editor and then click **Import** to add the workflow.
  </Step>

  <Step title="Add credentials to the workflow">
    * Add your Pinecone credentials:
      * In the **Pinecone Vector Store** node, select **Credential to connect with** > **Create new credential** and paste in your Pinecone API key.
      * Name the credential **Pinecone** so that other nodes reference it.

    * Add your OpenAI credentials:
      * In the **OpenAI Chat Model**, select **Credential to connect with** > **Create new credential** and paste in your OpenAI API key.
  </Step>

  <Step title="Activate the workflow">
    The workflow is configured to download recent Pinecone release notes and upload them to your Pinecone index. Click **Execute workflow** to start the workflow.

    <Tip>
      You can add your own files to the workflow by changing the URLs in the **Set file urls** node.
    </Tip>
  </Step>
</Steps>

### 4. Chat with your docs

Once the workflow is activated, ask it for the latest changes to Pinecone Database:

```
What's new in Pinecone Database?
```

### Next steps

* Use your own data:
  * Change the urls in **Set file urls** node to use your own files.
  * You may need to adjust the chunk sizes in the **Recursive Character Text Splitter** node or use a different chunking strategy. See [Chunking Strategies for LLM Applications](https://www.pinecone.io/learn/chunking-strategies/) for more info.
  * Customize the system message of the **AI Agent** node to reflect what the **Pinecone Vector Store Tool** will be used for.
  * Customize the description of the **Pinecone Vector Store Tool** to reflect what data you are storing in the Pinecone index.
* Use n8n, Pinecone Assistant, and OpenAI to [chat with your Google Drive documents](https://n8n.io/workflows/9942-rag-powered-document-chat-with-google-drive-openai-and-pinecone-assistant/).
* Get help in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH).
