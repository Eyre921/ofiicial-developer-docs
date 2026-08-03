---
title: "Create a deployment"
source: https://docs.together.ai/reference/dmi/deployments-create
path: reference/dmi/deployments-create
---

openapi.yaml POST /projects/{projectId}/endpoints/{endpointId}/deployments
Creates a model deployment under an endpoint. The deployment provisions asynchronously; monitor its status before routing live traffic to it.
