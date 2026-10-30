---
title: "Delete a volume (Beta)"
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/delete-a-volume-beta
path: langsmith/smith-api/sandboxes/delete-a-volume-beta
---

/langsmith/langsmith-platform-openapi.json delete /api/v2/sandboxes/volumes/{volume}
**Beta:** This API is in active development and may change without notice. Requires sandbox volumes to be enabled for your workspace. Delete a volume and its data. A volume attached to any sandbox cannot be deleted. Storage is reclaimed asynchronously. Only the volume's creator, or a role with sandboxes:exec, may delete it.
