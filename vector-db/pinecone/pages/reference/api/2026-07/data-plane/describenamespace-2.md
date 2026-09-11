---
title: "Describe a namespace"
source: https://docs.pinecone.io/reference/api/2026-07/data-plane/describenamespace
path: reference/api/2026-07/data-plane/describenamespace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_data_2026-07.oas.yaml get /namespaces/{namespace}
Describe a namespace in a serverless index, including the total number of vectors in the namespace.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"  # To target the default namespace, use "__default__".

  curl "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
  ```
</RequestExample>
