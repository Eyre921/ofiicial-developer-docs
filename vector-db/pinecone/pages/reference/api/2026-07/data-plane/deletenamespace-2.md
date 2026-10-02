---
title: "Delete a namespace"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/deletenamespace
path: reference/api/2026-07/data-plane/deletenamespace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml delete /namespaces/{namespace}
Delete a namespace from a serverless index. Deleting a namespace is irreversible; all data in the namespace is permanently deleted.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE" # To target the default namespace, use "__default__".

  curl -X DELETE "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
