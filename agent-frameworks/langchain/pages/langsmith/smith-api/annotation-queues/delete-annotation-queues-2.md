---
title: "Delete annotation queues"
source: https://docs.langchain.com/langsmith/smith-api/annotation-queues/delete-annotation-queues
path: langsmith/smith-api/annotation-queues/delete-annotation-queues
---

/langsmith/langsmith-platform-openapi.json delete /api/v1/annotation-queues
Delete multiple annotation queues with partial success support.

Returns:
    - 200: All queues deleted successfully
    - 207: Some queues deleted successfully, some failed
