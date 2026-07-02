---
title: "Rerank"
source: https://docs.together.ai/docs/inference/embeddings/rerank
path: docs/inference/embeddings/rerank
---

Reorder retrieved documents by relevance to a query for sharper search and RAG results.

A reranker is a model that reorders retrieved documents by relevance to a given query. It takes a query and a set of text inputs (called documents) and returns a relevancy score for each document. Use reranking to filter and prioritize the most relevant results.

In retrieval-augmented generation (RAG) pipelines, the reranking step sits between initial retrieval and final generation. It acts as a quality filter, refining the documents passed to the language model so the answer is grounded in the most relevant context.

## How the rerank API works

Together's [rerank API](https://docs.together.ai/reference/rerank-1) takes a `query` and a list of `documents`, and returns a relevancy score and ordering index for each document. It can also filter the response to the top `n` most relevant documents.

Key features:

* Long 8K context per document.
* Low latency for fast search queries.

## Get started

<Tip>
  Rerank models like `mxbai-rerank-large-v2` are only available on [dedicated endpoints](https://api.together.ai/endpoints/configure). Bring up a dedicated endpoint to use reranking in your applications.
</Tip>

### Example with text

The example below uses the [rerank API endpoint](/reference/rerank-1) to reorder a list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  query = "What animals can I find near Peru?"

  documents = [
      "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
      "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
      "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
      "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ]

  response = client.rerank.create(
      model="mixedbread-ai/mxbai-rerank-large-v2",
      query=query,
      documents=documents,
      top_n=2,
  )

  for result in response.results:
      print(f"Document Index: {result.index}")
      print(f"Document: {documents[result.index]}")
      print(f"Relevance Score: {result.relevance_score}")
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai"

  const client = new Together()

  const documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ]

  const response = await client.rerank.create({
    model: "mixedbread-ai/mxbai-rerank-large-v2",
    query: "What animals can I find near Peru?",
    documents,
    top_n: 2,
  })

  for (const result of response.results) {
    console.log(`Document index: ${result.index}`)
    console.log(`Document: ${documents[result.index]}`)
    console.log(`Relevance score: ${result.relevance_score}`)
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "mixedbread-ai/mxbai-rerank-large-v2",
         "query": "What animals can I find near Peru?",
         "documents": [
           "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
           "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
           "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
           "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations."
         ],
         "top_n": 2
       }'
  ```
</CodeGroup>

### Example with JSON data (dedicated endpoints only)

<Note>
  The following JSON data format with `rank_fields` is only supported on [dedicated endpoints](/docs/dedicated-endpoints/overview) running the `Salesforce/Llama-Rank-V1` model. All other rerank endpoints accept documents only as a list of strings.
</Note>

When using `Salesforce/Llama-Rank-V1`, pass a JSON object and specify the fields to rank over and the order to consider them in. If you don't pass `rank_fields`, the model defaults to the `text` key.

The example below shows passing in some emails, with the query `Which pricing did we get from Oracle?`.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  query = "Which pricing did we get from Oracle?"

  documents = [
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-03-27",
          "subject": "Follow-up",
          "text": "We are happy to give you the following pricing for your project.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-03-28",
          "subject": "Missing Information",
          "text": "Sorry, but here is the pricing you asked for for the newest line of your models.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-02-15",
          "subject": "Commited Pricing Strategy",
          "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
      },
      {
          "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2023-07-25",
          "subject": "Your latest flight travel plans",
          "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
      },
      {
          "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-01-26",
          "subject": "How to build generative AI applications using Generic Company Name",
          "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
      },
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-04-09",
          "subject": "Price Adjustment",
          "text": "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
      },
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",  # requires dedicated endpoint
      query=query,
      documents=documents,
      return_documents=True,
      rank_fields=["from", "to", "date", "subject", "text"],
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai"

  const client = new Together()

  const documents = [
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-03-27",
      subject: "Follow-up",
      text: "We are happy to give you the following pricing for your project.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-03-28",
      subject: "Missing Information",
      text: "Sorry, but here is the pricing you asked for for the newest line of your models.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-02-15",
      subject: "Commited Pricing Strategy",
      text: "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
    },
    {
      from: "Generic Airline Company<no_reply@generic_airline_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2023-07-25",
      subject: "Your latest flight travel plans",
      text: "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
    },
    {
      from: "Generic SaaS Company<marketing@generic_saas_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-01-26",
      subject:
        "How to build generative AI applications using Generic Company Name",
      text: "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
    },
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-04-09",
      subject: "Price Adjustment",
      text: "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
    },
  ]

  const response = await client.rerank.create({
    model: "Salesforce/Llama-Rank-V1", // requires dedicated endpoint
    query: "Which pricing did we get from Oracle?",
    documents,
    return_documents: true,
    rank_fields: ["from", "to", "date", "subject", "text"],
  })

  console.log(response)
  ```

  ```bash cURL theme={null}
  # Note: requires a dedicated endpoint running Salesforce/Llama-Rank-V1
  curl -X POST "https://api.together.ai/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-V1",
         "query": "Which pricing did we get from Oracle?",
         "documents": [
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-03-27",
             "subject": "Follow-up",
             "text": "We are happy to give you the following pricing for your project."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-03-28",
             "subject": "Missing Information",
             "text": "Sorry, but here is the pricing you asked for for the newest line of your models."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-02-15",
             "subject": "Commited Pricing Strategy",
             "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand."
           },
           {
             "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2023-07-25",
             "subject": "Your latest flight travel plans",
             "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed."
           },
           {
             "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-01-26",
             "subject": "How to build generative AI applications using Generic Company Name",
             "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!"
           },
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-04-09",
             "subject": "Price Adjustment",
             "text": "Re: our previous correspondence on 3/27 we'\''d like to make an amendment on our pricing proposal. We'\''ll have to decrease the expected base price by 5%."
           }
         ],
         "return_documents": true,
         "rank_fields": ["from", "to", "date", "subject", "text"]
       }'
  ```
</CodeGroup>

The `documents` parameter is a list of objects with the keys `from`, `to`, `date`, `subject`, and `text`. The `rank_fields` parameter names which keys to rank over and the order to consider them in.

Because `return_documents` is set to `true`, the response also includes each email alongside the rankings.

```json JSON theme={null}
{
  "model": "Salesforce/Llama-Rank-V1",
  "choices": [
    {
      "index": 0,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-03-27\",\"subject\":\"Follow-up\",\"text\":\"We are happy to give you the following pricing for your project.\"}"
      },
      "relevance_score": 0.606349439153678
    },
    {
      "index": 5,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-04-09\",\"subject\":\"Price Adjustment\",\"text\":\"Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.\"}"
      },
      "relevance_score": 0.5059948716207964
    },
    {
      "index": 1,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-03-28\",\"subject\":\"Missing Information\",\"text\":\"Sorry, but here is the pricing you asked for for the newest line of your models.\"}"
      },
      "relevance_score": 0.2271930688841643
    },
    {
      "index": 2,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-02-15\",\"subject\":\"Commited Pricing Strategy\",\"text\":\"I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.\"}"
      },
      "relevance_score": 0.2229844295907072
    },
    {
      "index": 4,
      "document": {
        "text": "{\"from\":\"Generic SaaS Company<marketing@generic_saas_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-01-26\",\"subject\":\"How to build generative AI applications using Generic Company Name\",\"text\":\"Hey Steve! Generative AI is growing so quickly and we know you want to build fast!\"}"
      },
      "relevance_score": 0.0021253144747196517
    },
    {
      "index": 3,
      "document": {
        "text": "{\"from\":\"Generic Airline Company<no_reply@generic_airline_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2023-07-25\",\"subject\":\"Your latest flight travel plans\",\"text\":\"Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.\"}"
      },
      "relevance_score": 0.0010322494264659
    }
  ]
}
```
