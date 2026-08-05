---
title: "Read a task file (raw bytes)"
source: https://docs.pinecone.io/reference/api/nexus/read_task_file
path: reference/api/nexus/read_task_file
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_2026-07.oas.yaml GET /tasks/{id}/files/read/{path}
Serves from the live container while the task runs, and from the archived blob store afterwards. This is how a finished pack's `<slug>.context.zip` is downloaded.
