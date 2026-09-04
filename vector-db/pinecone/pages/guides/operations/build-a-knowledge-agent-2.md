---
title: "Build a knowledge retrieval agent"
source: https://docs.pinecone.io/guides/operations/build-a-knowledge-agent
path: guides/operations/build-a-knowledge-agent
---

Build an AI agent that uses Pinecone to retrieve knowledge and answer questions accurately, with Pinecone as a tool inside the agent.

Build an AI agent that uses Pinecone to retrieve knowledge and answer questions accurately. This demo shows Pinecone as a tool inside an agent, which is the same pattern you'd use in production.

<Note>
  This guide requires an [Anthropic](https://console.anthropic.com/) or [OpenAI](https://platform.openai.com/api-keys) API key alongside your Pinecone API key.
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
  <Card title="Use the MCP server" icon="plug" href="/guides/operations/mcp-server">
    Give agents Pinecone access over the Model Context Protocol
  </Card>

  <Card title="Search methods" icon="magnifying-glass" href="/guides/search/search-overview">
    Explore semantic, hybrid, and full-text search
  </Card>

  <Card title="Data modeling" icon="table" href="/guides/index-data/data-modeling">
    Model your data for efficient retrieval
  </Card>
</CardGroup>
