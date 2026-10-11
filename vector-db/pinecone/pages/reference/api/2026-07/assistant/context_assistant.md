---
title: "Retrieve context from an assistant"
source: https://docs.pinecone.io/reference/api/2026-07/assistant/context_assistant
path: reference/api/2026-07/assistant/context_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/assistant_data_2026-07.oas.yaml POST /chat/{assistant_name}/context
Retrieve context snippets from an assistant to use as part of RAG or any agentic flow.

For guidance and examples, see [Retrieve context snippets](https://docs.pinecone.io/guides/assistant/retrieve-context-snippets).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "query": "Who is the CFO of Netflix?"
  }'
  ```
</RequestExample>
