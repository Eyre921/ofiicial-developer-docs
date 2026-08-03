---
title: "Delete an endpoint"
source: https://docs.together.ai/reference/dmi/endpoints-delete
path: reference/dmi/endpoints-delete
---

openapi.yaml DELETE /projects/{projectId}/endpoints/{id}
Permanently deletes an endpoint. Delete its deployments first; use `etag` to reject the request if the endpoint changed after it was read.
