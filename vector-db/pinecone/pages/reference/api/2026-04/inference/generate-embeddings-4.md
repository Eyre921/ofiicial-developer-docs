---
title: "Generate vectors"
source: https://docs.pinecone.io/reference/api/2026-04/inference/generate-embeddings
path: reference/api/2026-04/inference/generate-embeddings
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/inference_2026-04.oas.yaml post /embed
Generate vector embeddings for input data. This endpoint uses Pinecone's [hosted embedding models](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/embed \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
        "model": "llama-text-embed-v2",
        "parameters": {
          "input_type": "passage",
          "truncate": "END"
        },
        "inputs": [
          {"text": "Apple is a popular fruit known for its sweetness and crisp texture."},
          {"text": "The tech company Apple is known for its innovative products like the iPhone."},
          {"text": "Many people enjoy eating apples as a healthy snack."},
          {"text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
          {"text": "An apple a day keeps the doctor away, as the saying goes."},
          {"text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
        ]
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "values": [
          0.04925537109375,
          -0.01313018798828125,
          -0.0112762451171875,
          ...
        ]
      }, 
      ...
    ],
    "model": "llama-text-embed-v2",
    "usage": {
      "total_tokens": 130
    }
  }
  ```
</ResponseExample>
