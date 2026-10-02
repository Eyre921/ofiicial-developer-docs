---
title: "Describe an operation"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/describe_operation
path: reference/api/2026-04/assistant/describe_operation
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_data_2026-04.oas.yaml GET /operations/{assistant_name}/{operation_id}
Get the status of an operation.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  OPERATION_ID="op-1234-abcd-5678"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/operations/$ASSISTANT_NAME/$OPERATION_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<Note>
  Operation responses may include `error_message`, but only when the operation status is `Failed`.
</Note>
