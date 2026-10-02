---
title: "List assistants"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/list_assistants
path: reference/api/2026-04/assistant/list_assistants
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_control_2026-04.oas.yaml GET /assistants
List of all assistants in a project.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#list-assistants-for-a-project).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "assistants": [
      {
        "name": "example-assistant",
        "instructions": "Use American English for spelling and grammar.",
        "metadata": {"team": "customer-support", "version": "1.0"},
        "status": "Ready",
        "host": "https://prod-1-data.ke.pinecone.io",
        "created_at": "2025-10-01T12:30:00Z",
        "updated_at": "2025-10-01T12:45:00Z"
      }
    ]
  }
  ```
</ResponseExample>
