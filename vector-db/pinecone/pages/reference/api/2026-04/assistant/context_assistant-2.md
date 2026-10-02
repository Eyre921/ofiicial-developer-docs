---
title: "Retrieve context from an assistant"
source: https://docs.pinecone.io/reference/api/2026-04/assistant/context_assistant
path: reference/api/2026-04/assistant/context_assistant
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/assistant_data_2026-04.oas.yaml POST /chat/{assistant_name}/context
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
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
      "query": "Who is the CFO of Netflix?"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "snippets":
      [
          {
              "type":"text",
              "content":"EXHIBIT 31.3\nCERTIFICATION OF CHIEF FINANCIAL OFFICER\nPURSUANT TO SECTION 302 OF THE SARBANES-OXLEY ACT OF 2002\nI, Spencer Neumann, certify that: ...",
              "score":0.9960699,
              "reference":
              {
                  "type":"pdf",
                  "file":
                  {
                      "status":"Available","id":"e6034e51-0bb9-4926-84c6-70597dbd07a7",
                      "name":"Netflix-10-K-01262024.pdf",
                      "size":1073470,
                      "metadata":null,
                      "updated_on":"2024-11-21T22:59:10.426001030Z",
                      "created_on":"2024-11-21T22:58:35.879120257Z",
                      "signed_url":"https://storage.googleapis.com..."
                      },
                  "pages":[78]
              }
          },
  {
      "type":"text",
      "content":"EXHIBIT 32.1\n..."
  ...
  ```
</ResponseExample>
