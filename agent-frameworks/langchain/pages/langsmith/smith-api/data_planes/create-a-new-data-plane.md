---
title: "Create a new data plane"
source: https://docs.langchain.com/langsmith/smith-api/data_planes/create-a-new-data-plane
path: langsmith/smith-api/data_planes/create-a-new-data-plane
---

/langsmith/langsmith-platform-openapi.json post /orgs/current/data-planes
Creates a new data plane object. Persists the rendered data plane spec, and returns 202 with the data plane in status=requested. Requires BYOC enabled org and org admin.
