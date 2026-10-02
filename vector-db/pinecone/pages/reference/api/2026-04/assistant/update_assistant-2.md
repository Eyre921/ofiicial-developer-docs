---
title: "Update an assistant"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/update_assistant
path: reference/api/2026-04/assistant/update_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_control_2026-04.oas.yaml PATCH /assistants/{assistant_name}
Update an existing assistant. You can modify the assistant's instructions.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#add-instructions-to-an-assistant).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X PATCH "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.1"}
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.1"},
    "status": "Ready",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-10-01T12:30:00Z",
    "updated_at": "2025-10-01T12:45:00Z"
  }
  ```
</ResponseExample>
