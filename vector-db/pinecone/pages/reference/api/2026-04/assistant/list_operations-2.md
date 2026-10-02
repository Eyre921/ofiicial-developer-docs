---
title: "List operations"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/list_operations
path: reference/api/2026-04/assistant/list_operations
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_data_2026-04.oas.yaml GET /operations/{assistant_name}
List all operations for an assistant. Returns operations that are in progress, as well as recently completed or failed operations.
Both successful and failed operations are retained for 30 days after completion.
Use the `operation_type` and `status` query parameters to filter results.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  # List all operations
  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"

  # Filter by status
  # curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME?status=Processing" \
  #   -H "Api-Key: $PINECONE_API_KEY" \
  #   -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>
