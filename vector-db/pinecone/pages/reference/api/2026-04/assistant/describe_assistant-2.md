---
title: "Check assistant status"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/describe_assistant
path: reference/api/2026-04/assistant/describe_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_control_2026-04.oas.yaml GET /assistants/{assistant_name}
Get the status of an assistant.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#get-the-status-of-an-assistant)

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "status": "Ready",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-10-01T12:30:00Z",
    "updated_at": "2025-10-01T12:45:00Z"
  }
  ```
</ResponseExample>
