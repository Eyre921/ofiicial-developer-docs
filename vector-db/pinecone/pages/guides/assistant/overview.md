---
title: "Pinecone Assistant"
source: https://docs.pinecone.io/guides/assistant/overview
path: guides/assistant/overview
---

Overview of Pinecone Assistant, a managed service for building production-grade RAG chat and agent applications grounded in your data.

<CardGroup>
  <Card title="Assistant quickstart" icon="comments" href="/guides/assistant/quickstart/sdk-quickstart">
    Create an AI assistant that answers complex questions about your proprietary data
  </Card>

  <Card title="Database quickstart" icon="database" href="/guides/get-started/quickstart">
    Set up a fully managed vector database for high-performance semantic search
  </Card>
</CardGroup>

## Use cases

Pinecone Assistant is useful for a variety of tasks, especially for the following:

* Prototyping and deploying an AI assistant quickly.
* Providing context-aware answers about your proprietary data without training an LLM.
* Retrieving answers grounded in your data, with references.

## SDK support

You can use the [Assistant API](/reference/api/assistant/introduction) directly, through the [Pinecone Python SDK](/reference/sdks/python/overview), or through the [Pinecone Node.js SDK](/reference/sdks/node/overview).

## Workflow

You can use the Pinecone Assistant through the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant) or [Pinecone API](/reference/api/assistant/introduction).

<Tabs>
  <Tab title="Overview">
    The following steps outline the general Pinecone Assistant workflow:

    <Steps>
      <Step title="Create an assistant">
        [Create an assistant](/guides/assistant/create-assistant) to answer questions about your documents.
      </Step>

      <Step title="Upload documents">
        [Upload documents](/guides/assistant/upload-files) to your assistant. Your assistant manages chunking, embedding, and storage for you.
      </Step>

      <Step title="Chat with an assistant">
        [Chat with your assistant](/guides/assistant/chat-with-assistant) and receive responses as a JSON object or as a text stream. For each chat, your assistant queries a large language model (LLM) with context from your documents to ensure the LLM provides grounded responses.
      </Step>

      <Step title="Evaluate answers">
        [Evaluate the assistant's responses](/guides/assistant/evaluation-overview) for correctness and completeness.
      </Step>

      <Step title="Optimize performance">
        [Use custom instructions](https://www.pinecone.io/learn/assistant-api-deep-dive/#Custom-Instructions) to tailor your assistant's behavior and responses to specific use cases or requirements. [Filter by metadata associated with files](https://www.pinecone.io/learn/assistant-api-deep-dive/#Using-Metadata) to reduce latency and improve the accuracy of responses.
      </Step>

      <Step title="Retrieve context snippets">
        [Retrieve context snippets](/guides/assistant/retrieve-context-snippets) to understand what relevant data snippets Pinecone Assistant is using to generate responses. You can use the retrieved snippets with your own LLM, RAG application, or agentic workflow.
      </Step>
    </Steps>

    <Note>
      For information on how the Pinecone Assistant works, see [Assistant architecture](/reference/architecture/assistant-architecture).
    </Note>
  </Tab>

  <Tab title="Code sample">
    The following code samples outline the Pinecone Assistant workflow using either the [Pinecone Python SDK](/reference/sdks/python/overview) and [Pinecone Assistant plugin](/reference/sdks/python/overview#install-the-pinecone-assistant-python-plugin) or the [Pinecone Node.js SDK](/reference/sdks/node/overview).

    <CodeGroup>
      ```python Python theme={null}
      # pip install pinecone
      # pip install pinecone-plugin-assistant

      from pinecone import Pinecone
      import requests
      from pinecone_plugins.assistant.models.chat import Message

      pc = Pinecone(api_key="YOUR_API_KEY")

      # Create an assistant.
      assistant = pc.assistant.create_assistant(
          assistant_name="example-assistant", 
          instructions="Use American English for spelling and grammar.", # Description or directive for the assistant to apply to all responses.
          region="us", # Region to deploy assistant. Options: "us" (default) or "eu".    
          timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
      )

      # Upload a file to your assistant.
      response = assistant.upload_file(
          file_path="/Users/jdoe/Downloads/Netflix-10-K-01262024.pdf",
          metadata={"company": "netflix", "document_type": "form 10k"},
          timeout=None
      )

      # Set up for evaluation later.
      payload = {
          "question": "Who is the CFO of Netflix?", # Question to ask the assistant.
          "ground_truth_answer": "Spencer Neumann" # Expected answer to evaluate the assistant's response.
      }

      # Chat with the assistant.
      msg = Message(role="user", content=payload["question"])
      resp = assistant.chat(messages=[msg], model="gpt-4o")
      print(resp)

      # {
      #    'id': '0000000000000000163008a05b317b7b', 
      #    'model': 'gpt-4o-2024-05-13', 
      #    'usage': {
      #        'prompt_tokens': 9259, 
      #        'completion_tokens': 30, 
      #        'total_tokens': 9289
      #        }, 
      #        'message': {
      #            'content': 'The Chief Financial Officer (CFO) of Netflix is Spencer Neumann.', 
      #            'role': '"assistant"'
      #            }, 
      #            'finish_reason': 'stop', 
      #            'citations': [
      #                {
      #                    'position': 63, 
      #                    'references': [
      #                        {
      #                            'pages': [78, 72, 79], 
      #                            'file': {
      #                                'name': 'Netflix-10-K-01262024.p# Architecture
Source: https://docs.pinecone.io/guides/core-concepts/architecture

Learn how Pinecone is built, from organizations, projects, indexes, and namespaces down to the infrastructure that stores and serves your data.

Pinecone's architecture has two layers: the resource hierarchy that organizes your data, and the serverless infrastructure that stores and serves it.

## Resource hierarchy

Your data in Pinecone is organized as a hierarchy of resources. An [organization](/guides/core-concepts/key-terms#organization) contains [projects](/guides/core-concepts/key-terms#project), a project contains [indexes](/guides/core-concepts/key-terms#index), and an index is divided into [namespaces](/guides/core-concepts/key-terms#namespace) that hold your [records](/guides/core-concepts/key-terms#record) or [documents](/guides/core-concepts/key-terms#document). For a definition of each object, see [Key terms](/guides/core-concepts/key-terms).

<img />

<img />

## Serverless infrastructure

Pinecone runs as a managed service on AWS, GCP, and Azure cloud platforms. When you send a request to Pinecone, it goes through an [API gateway](#api-gateway) that routes it to either a global [control plane](#control-plane) or a regional [data plane](#data-plane). All your vector data is stored in highly efficient, distributed [object storage](#object-storage).

<img />

<img />

### API gateway

Every request to Pinecone includes an [API key](/guides/projects/manage-api-keys) that's assigned to a specific [project](/guides/projects/understanding-projects). The API gateway first validates your API key to make sure you have permission to access the project. Once validated, it routes your request to either the global control plane (for managing projects and indexes) or a regional data plane (for reading and writing data), depending on what you're trying to do.

### Control plane

The global control plane manages your organizational resources like projects and indexes. It uses a dedicated database to keep track of all these objects. The control plane also handles billing, user management, and coordinates operations across different regions.

### Data plane

The data plane handles all requests to write and read records in [indexes](/guides/index-data/indexing-overview) within a specific [cloud region](/guides/index-data/create-an-index#cloud-regions). Each index is divided into one or more logical [namespaces](/guides/index-data/indexing-overview#namespaces), and all your data read and write requests target a specific namespace.

Pinecone separates write and read operations into different paths, with each scaling independently based on demand. This separation ensures that your queries never slow down your writes, and your writes never slow down your queries.

### Object storage

For each namespace in a serverless index, Pinecone organizes records into immutable files called slabs. These slabs are [optimized for fast querying](#index-builder) and stored in distributed object storage that provides virtually unlimited scalability and high availability.

## Write path

<img />

<img />

### Request log

When you send a write request (to add, update, or delete records), the [data plane](#data-plane) first logs the request details with a unique sequence number (LSN). This ensures all operations happen in the correct order and provides a way to track the state of the index.

Pinecone immediately returns a `200 OK` response, guaranteeing that your write is durable and won't be lost. The system then processes your write in the background.

### Index builder

The index builder stores your write data in an in-memory structure called a memtable. This includes your vector data, any metadata you've attached, and the sequence number. If you're updating or deleting a record, the system also tracks how to handle the old version during queries.

Periodically, the index builder moves data from the memtable to permanent storage. In [object storage](#object-storage), your data is organized into immutable files called slabs. These slabs are optimized for query performance. Smaller slabs use fast indexing techniques that provide good performance with minimal resource requirements. As slabs grow, the system merges them into larger slabs that use more sophisticated methods that provide better performance at scale. This adaptive process both optimizes query performance for each slab and amortizes the cost of more expensive indexing through the lifetime of the namespace.

<Note>
  All read operations check the memtable first, so you can immediately search data that you've just written, even before it's moved to permanent storage. For more details, see [Query executors](#query-executors).
</Note>

## Read path

<img />

<img />

### Query routers

When you send a search query, the [data plane](#data-plane) first validates your request and checks that it meets system limits like [rate and object limits](/reference/api/database-limits). The query router then identifies which slabs contain relevant data and routes your query to the appropriate executors. It also searches the memtable for any recent data that hasn't been moved to permanent storage yet.

### Query executors

Each query executor searches through its assigned slabs and returns the most relevant candidates to the query router. If your query includes metadata filters, the executors exclude records that don't match your criteria before finding the best matches.

Most of the time, the slabs are cached in memory or on local SSD, which provides very fast query performance. If a slab isn't cached (which happens when it's accessed for the first time or hasn't been used recently), the executor fetches it from object storage and caches it for future queries.

The query router then combines results from all executors, removes duplicates, merges them with results from the memtable, and returns the final set of best matches to you.
