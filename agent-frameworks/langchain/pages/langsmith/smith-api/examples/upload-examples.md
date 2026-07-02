---
title: "Upload Examples"
source: https://docs.langchain.com/langsmith/smith-api/examples/upload-examples
path: langsmith/smith-api/examples/upload-examples
---

/langsmith/langsmith-platform-openapi.json post /v1/platform/datasets/{dataset_id}/examples
This endpoint allows clients to upload examples to a specified dataset by sending a multipart/form-data POST request.
Each form part contains either JSON-encoded data or binary attachment files associated with an example.
