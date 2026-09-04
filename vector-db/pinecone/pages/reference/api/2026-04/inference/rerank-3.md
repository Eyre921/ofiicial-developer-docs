---
title: "Rerank results"
source: https://docs.pinecone.io/reference/api/2026-04/inference/rerank
path: reference/api/2026-04/inference/rerank
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/inference_2026-04.oas.yaml post /rerank
Rerank results according to their relevance to a query.

For guidance and examples, see [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/rerank \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -H "Api-Key: $PINECONE_API_KEY" \
  -d '{
    "model": "bge-reranker-v2-m3",
    "query": "The tech company Apple is known for its innovative products like the iPhone.",
    "return_documents": true,
    "top_n": 4,
    "documents": [
      {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
      {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
      {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
      {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."}
    ],
    "parameters": {
      "truncate": "END"
    }
  }'
  ```
</RequestExample>

<ResponseExample>
  ```JSON curl theme={null}
  {
    "data":[
      {
        "index":2,
        "document":{
          "id":"vec3",
          "text":"Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
        },
        "score":0.47654688
      },
      {
        "index":0,
        "document":{
          "id":"vec1",
          "text":"Apple is a popular fruit known for its sweetness and crisp texture."
        },
        "score":0.047963805
      },
      {
        "index":3,
        "document":{
          "id":"vec4",
          "text":"An apple a day keeps the doctor away, as the saying goes."
        },
        "score":0.007587992
      },
      {
        "index":1,
        "document":{
          "id":"vec2",
          "text":"Many people enjoy eating apples as a healthy snack."
        },
        "score":0.0006491712
      }
    ],
    "usage":{
      "rerank_units":1
    }
  }
  ```
</ResponseExample>
