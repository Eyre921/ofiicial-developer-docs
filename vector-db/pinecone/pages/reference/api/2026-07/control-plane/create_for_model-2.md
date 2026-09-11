---
title: "Create an index with integrated embedding"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_for_model
path: reference/api/2026-07/control-plane/create_for_model
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes/create-for-model
Create an index with integrated embedding.
With this type of index, you provide source text, and Pinecone uses a [hosted embedding model](https://docs.pinecone.io/guides/index-data/create-an-index#embedding-models) to convert the text automatically during [upsert](https://docs.pinecone.io/reference/api/2026-07/data-plane/upsert_records) and [search](https://docs.pinecone.io/reference/api/2026-07/data-plane/search_records).
The response is this version's index model, with the embedding configuration surfaced as a `semantic_text` field in the index `schema`, named after the `field_map` text entry. Read and write the index through the records API.
For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index#integrated-embedding).

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_model = pc.create_index_for_model(
      name="docs-example",
      cloud="aws",
      region="us-east-1",
      embed={
          "model": "multilingual-e5-large",
          "field_map": {"text": "chunk_text"}
      }
  )
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/create-for-model" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "name": "docs-example",
      "cloud": "aws",
      "region": "us-east-1",
      "embed": {
        "model": "multilingual-e5-large",
        "field_map": {"text": "chunk_text"}
      }
    }'
  ```
</RequestExample>
