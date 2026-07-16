---
title: "Delete a deployment"
source: https://docs.together.ai/reference/dmi/deployments-delete
path: reference/dmi/deployments-delete
---

DELETE /projects/{projectId}/endpoints/{endpointId}/deployments/{id}
Permanently deletes a deployment from its endpoint. Remove the deployment from live traffic first; use `etag` to reject the request if it changed after it was read.
