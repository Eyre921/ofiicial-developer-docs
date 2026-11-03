---
title: "Convert an index into a document index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/convert_index
path: reference/api/2026-07/control-plane/convert_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes/{index_name}/convert
Convert a serverless vector index or legacy integrated index into a new document index. The source index isn't changed, and the new index holds a snapshot of the source taken when the job starts.

The request returns once the new index is created in the `Initializing` state. Track the job with [Describe a conversion job](https://docs.pinecone.io/reference/api/2026-07/control-plane/describe_conversion_job). If the job fails or is canceled, the index is left in the `InitializationFailed` state with no usable data. Delete it to free its name. A job that fails because of your data is charged for the data it read, and a canceled job isn't charged.

For how source records map to the schema, see [Convert an index](https://docs.pinecone.io/guides/index-data/convert-an-index).

```bash Vector index theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl https://api.pinecone.io/indexes/support-tickets/convert \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "support-tickets-docs",
        "schema": {
          "fields": {
            "embedding": {
              "type": "dense_vector",
              "dimension": 1024,
              "metric": "cosine"
            },
            "ticket_text": {
              "type": "string",
              "full_text_search": {
                "language": "en"
              }
            }
          }
        },
        "error_mode": {
          "on_error": "continue"
        }
      }'
```

```bash Legacy integrated index theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl https://api.pinecone.io/indexes/support-articles/convert \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "support-articles-docs",
        "schema": {
          "fields": {
            "chunk_text": {
              "type": "string",
              "embed": {
                "model": "multilingual-e5-large"
              }
            }
          }
        }
      }'
```
