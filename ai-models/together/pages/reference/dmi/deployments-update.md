---
title: "Update a deployment"
source: https://docs.together.ai/reference/dmi/deployments-update
path: reference/dmi/deployments-update
---

openapi.yaml PATCH /projects/{projectId}/endpoints/{endpointId}/deployments/{id}
Updates mutable deployment fields such as its model, configuration, autoscaling bounds, or LoRA support. Changes that affect serving may trigger asynchronous reprovisioning.
