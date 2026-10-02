---
title: "Create an assistant"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/create_assistant
path: reference/api/2026-04/assistant/create_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_control_2026-04.oas.yaml POST /assistants
Create an assistant. This is where you specify the underlying training model, which cloud provider you would like to deploy with, and more.

For guidance and examples, see [Create an assistant](https://docs.pinecone.io/guides/assistant/create-assistant)

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "region":"us"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "status": "Initializing",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-10-01T12:30:00Z",
    "updated_at": "2025-10-01T12:30:00Z"
  }
  ```
</ResponseExample>
