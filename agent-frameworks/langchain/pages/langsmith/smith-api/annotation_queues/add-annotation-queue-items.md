---
title: "Add annotation queue items"
source: https://docs.langchain.com/langsmith/smith-api/annotation_queues/add-annotation-queue-items
path: langsmith/smith-api/annotation_queues/add-annotation-queue-items
---

/langsmith/langsmith-platform-openapi.json post /api/v1/platform/annotation-queues/{queue_id}/items
Add RUN or THREAD items to a single annotation queue. RUN items require run_id unless they are created from a suggested example. THREAD items require thread_id and project_id.
