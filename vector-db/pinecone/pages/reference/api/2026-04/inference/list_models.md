---
title: "List available models"
source: https://docs.pinecone.io/reference/api/2026-04/inference/list_models
path: reference/api/2026-04/inference/list_models
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/inference_2026-04.oas.yaml get /models
List the embedding and reranking models hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/models" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "models": [
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
      },
      {
        "model": "multilingual-e5-large",
        "short_description": "A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "type": "embed",
        "vector_type": "dense",
        "default_dimension": 1024,
        "modality": "text",
        "max_sequence_length": 507,
        "max_batch_size": 96,
        "provider_name": "Microsoft",
        "supported_metrics": [
          "Cosine",
          "Euclidean"
        ],
        "supported_dimensions": [
          1024
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
              "NONE"
            ]
          }
        ]
      },
      {
        "model": "pinecone-sparse-english-v0",
        "short_description": "A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.",
        "type": "embed",
        "vector_type": "sparse",
        "modality": "text",
        "max_sequence_length": 512,
        "max_batch_size": 96,
        "provider_name": "Pinecone",
        "supported_metrics": [
          "DotProduct"
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
              "NONE"
            ]
          },
          {
            "parameter": "return_tokens",
            "required": false,
            "default": false,
            "type": "any",
            "value_type": "boolean"
          }
        ]
      },
      {
        "model": "bge-reranker-v2-m3",
        "short_description": "A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 1024,
        "max_batch_size": 100,
        "provider_name": "BAAI",
        "supported_parameters": [
          {
            "parameter": "truncate",
            "required": false,
            "default": "NONE",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      },
      {
        "model": "cohere-rerank-3.5",
        "short_description": "Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 40000,
        "max_batch_size": 200,
        "provider_name": "Cohere",
        "supported_parameters": [
          {
            "parameter": "max_chunks_per_doc",
            "required": false,
            "default": 3072,
            "type": "numeric_range",
            "value_type": "integer",
            "min": 1,
            "max": 3072
          }
        ]
      },
      {
        "model": "pinecone-rerank-v0",
        "short_description": "A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 512,
        "max_batch_size": 100,
        "provider_name": "Pinecone",
        "supported_parameters": [
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      }
    ]
  }
  ```
</ResponseExample>
