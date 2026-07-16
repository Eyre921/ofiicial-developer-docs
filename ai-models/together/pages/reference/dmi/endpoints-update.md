---
title: "Update an endpoint"
source: https://docs.together.ai/reference/dmi/endpoints-update
path: reference/dmi/endpoints-update
---

PATCH /projects/{projectId}/endpoints/{id}
Updates mutable endpoint fields such as its inference name, visibility, or deployment traffic split. Use `updateMask` to select fields explicitly and `etag` in the request body for optimistic concurrency.
