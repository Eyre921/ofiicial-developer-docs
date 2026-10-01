---
title: "Delete an example"
source: https://docs.langchain.com/langsmith/smith-api/examples/delete-an-example
path: langsmith/smith-api/examples/delete-an-example
---

/langsmith/langsmith-platform-openapi.json delete /api/v1/platform/datasets/{dataset_id}/examples/{example_id}
Soft-delete an example, preserving prior versions and their attachments. If the latest version is already deleted, the request succeeds without creating another version. Deletion is recorded at the current time or just after the latest version, whichever is later. For future-dated versions, latest reads reflect deletion immediately; timestamp reads reflect deletion only at or after the recorded deletion timestamp.
