---
title: "Generate embeddings"
source: https://docs.together.ai/docs/inference/embeddings/embeddings
path: docs/inference/embeddings/embeddings
---

Turn text into vector embeddings for search, classification, recommendations, and RAG.

<Tip>Using a coding agent? Install the [together-embeddings](https://github.com/togethercomputer/skills/tree/main/skills/together-embeddings) skill to let your agent write correct embeddings code automatically. See [agent skills](/docs/agent-skills) for details.</Tip>

The embeddings API turns an input string into a vector of numbers. You can compare two vectors to measure how closely related the source texts are.

Common use cases include search, classification, recommendations, and retrieval-augmented generation (RAG). For long-term retrieval, store embeddings in a vector database and query by similarity.

For the full parameter list, see the [Create embedding reference](/reference/embeddings). For available embedding models, see the [serverless](/docs/serverless/models) and [dedicated endpoint](/docs/dedicated-endpoints/models) model catalogs.

## Generate an embedding

Call `client.embeddings.create` with a model and an input string.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="intfloat/multilingual-e5-large-instruct",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.embeddings.create({
    model: "intfloat/multilingual-e5-large-instruct",
    input: "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.together.ai/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "input": "Our solar system orbits the Milky Way galaxy at about 515,000 mph.",
           "model": "intfloat/multilingual-e5-large-instruct"
          }'
  ```
</CodeGroup>

The response contains the embedding under `data`, along with metadata.

```json JSON theme={null}
{
  "model": "intfloat/multilingual-e5-large-instruct",
  "object": "list",
  "data": [
    {
      "index": 0,
      "object": "embedding",
      "embedding": [0.2633975, 0.13856208, 0.04331574]
    }
  ]
}
```

## Generate multiple embeddings

Pass an array of strings to `input` to embed several texts in one call.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="intfloat/multilingual-e5-large-instruct",
      input=[
          "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
          "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
      ],
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.embeddings.create({
    model: "intfloat/multilingual-e5-large-instruct",
    input: [
      "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
      "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
    ],
  });
  ```

  ```bash cURL theme={null}
  curl -X POST https://api.together.ai/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "model": "intfloat/multilingual-e5-large-instruct",
           "input": [
              "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
              "Jupiter'\''s Great Red Spot is a storm that has been raging for at least 350 years."
           ]
          }'
  ```
</CodeGroup>

`response.data` contains one object per input, each with the matching `index`.

```json JSON theme={null}
{
  "model": "intfloat/multilingual-e5-large-instruct",
  "object": "list",
  "data": [
    {
      "index": 0,
      "object": "embedding",
      "embedding": [0.2633975, 0.13856208, 0.04331574]
    },
    {
      "index": 1,
      "object": "embedding",
      "embedding": [-0.14496337, 0.21044481, -0.16187587]
    }
  ]
}
```

## Next steps

* Browse [embedding models](/docs/serverless/models#embedding-models).
* Read the [Create embedding API reference](/reference/embeddings).
* Use embeddings with the [Vercel AI SDK](/docs/using-together-with-vercels-ai-sdk#embedding-models).
