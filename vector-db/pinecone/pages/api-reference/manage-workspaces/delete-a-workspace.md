---
title: "Delete a workspace"
source: https://docs.pinecone.io/api-reference/manage-workspaces/delete-a-workspace
path: api-reference/manage-workspaces/delete-a-workspace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_control_2026-07.oas.yaml delete /workspaces/{workspace_name}
Delete an existing workspace. Deletion is asynchronous: the workspace transitions to the `Terminating` state and its contexts are deleted, after which the workspace itself is removed.
