---
title: "Describe a model"
source: https://docs.pinecone.io/reference/api/2026-04/inference/describe_model
path: reference/api/2026-04/inference/describe_model
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/inference_2026-04.oas.yaml get /models/{model_name}
Get a description of a model hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/models/llama-text-embed-v2" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "model": "llama-text-embed-v2",
    "short_description": "A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).",
    "type": "embed",
    "vector_type": "dense",
    "default_dimension": 1024,
    "modality": "text",
    "max_sequence_length": 2048,
    "max_batch_size": 96,
    "provider_name": "NVIDIA",
    "supported_metrics": [
      "Cosine",
      "DotProduct"
    ],
    "supported_dimensions": [
      384,
      512,
      768,
      1024,
      2048
    ],
    "supported_parameters": [
      {
        "parameter": "input_type",
        "required": true,
        "type": "one_of",
        "value_type": "string",
        "allowed_values": [
          "query",
          "passage"
        ]
      },
      {
        "parameter": "truncate",
        "required": false,
        "default": "END",
        "type": "one_of",
        "value_type": "string",
        "allowed_values": [
          "END",
          "NONE",
          "START"
        ]
      },
      {
        "parameter": "dimension",
        "required": false,
        "default": 1024,
        "type": "one_of",
        "value_type": "integer",
        "allowed_values": [
          384,
          512,
          768,
          1024,
          2048
        ]
      }
    ]
  }
  ```
</ResponseExample>
