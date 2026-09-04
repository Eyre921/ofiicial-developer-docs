---
title: "Create a workspace"
source: https://docs.pinecone.io/api-reference/manage-workspaces/create-a-workspace
path: api-reference/manage-workspaces/create-a-workspace
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/nexus_control_2026-07.oas.yaml post /workspaces
Create a Nexus workspace. The workspace name must be unique within the project.

Workspaces are created asynchronously. On success the workspace is returned in the `Initializing` state with `ready` set to `false`. Poll [Describe workspace](#operation/describe_workspace) until the workspace reaches the `Ready` state before using it.
