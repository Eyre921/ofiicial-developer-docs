---
title: "Search with a vector"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/query
path: reference/api/2026-04/data-plane/query
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /query
Search a namespace using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

For guidance, examples, and limits, see [Search](https://docs.pinecone.io/guides/search/search-overview).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
      "namespace": "example-namespace",
      "vector": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      "filter": {"genre": {"$eq": "documentary"}},
      "topK": 3,
      "includeValues": true
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "matches":[
      {
        "id": "vec3",
        "score": 0,
        "values": [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
      },
      {
        "id": "vec2",
        "score": 0.0800000429,
        "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
      },
      {
        "id": "vec4",
        "score": 0.0799999237,
        "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
      }
    ],
    "namespace": "example-namespace",
    "usage": {"read_units": 6}
  }
  ```
</ResponseExample>
