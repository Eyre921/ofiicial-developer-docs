---
title: "Read a task file (raw bytes)"
source: https://docs.pinecone.io/api-reference/task-files/read-a-task-file-raw-bytes
path: api-reference/task-files/read-a-task-file-raw-bytes
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml get /tasks/{id}/files/read/{path}
Serves a task's files while it runs and after it finishes. This is how a finished pack's `<slug>.context.zip` is downloaded.
