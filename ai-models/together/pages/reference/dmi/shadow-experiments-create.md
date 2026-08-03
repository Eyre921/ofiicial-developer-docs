---
title: "Create a shadow experiment"
source: https://docs.together.ai/reference/dmi/shadow-experiments-create
path: reference/dmi/shadow-experiments-create
---

openapi.yaml POST /projects/{projectId}/endpoints/{endpointId}/shadowExperiments
Creates an experiment that mirrors a sampled portion of endpoint traffic to one or more target deployments without returning their responses to clients. Add a description with the update operation after creation.
