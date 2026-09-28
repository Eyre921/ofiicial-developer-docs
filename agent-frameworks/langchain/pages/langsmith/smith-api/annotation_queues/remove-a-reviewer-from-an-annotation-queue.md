---
title: "Remove a reviewer from an annotation queue"
source: https://docs.langchain.com/langsmith/smith-api/annotation_queues/remove-a-reviewer-from-an-annotation-queue
path: langsmith/smith-api/annotation_queues/remove-a-reviewer-from-an-annotation-queue
---

/langsmith/langsmith-platform-openapi.json delete /api/v1/platform/annotation-queues/{queue_id}/reviewers/{identity_id}
Unassigns an identity as a reviewer for the queue. Idempotent.
