---
title: "Get a task (with steps)"
source: https://docs.pinecone.io/api-reference/tasks/get-a-task-with-steps
path: api-reference/tasks/get-a-task-with-steps
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_data_2026-07.oas.yaml get /tasks/{id}
Unlike the listing, this carries the task's `steps` — every one by default, or the newest N with `steps_limit`, where `steps_total` reports the true count.
