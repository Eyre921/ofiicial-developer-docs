---
title: "Add a deployment adapter"
source: https://docs.together.ai/reference/dmi/adapters-add
path: reference/dmi/adapters-add
---

POST /projects/{projectId}/endpoints/{endpointId}/deployments/{deploymentId}/adapters
Attaches a LoRA adapter to a deployment. If the deployment is at adapter capacity, force can evict the oldest adapter.
