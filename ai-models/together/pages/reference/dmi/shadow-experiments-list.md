---
title: "List shadow experiments"
source: https://docs.together.ai/reference/dmi/shadow-experiments-list
path: reference/dmi/shadow-experiments-list
---

GET /projects/{projectId}/endpoints/{endpointId}/shadowExperiments
Lists experiments that mirror sampled endpoint traffic to target deployments without affecting client responses. Set `includeTargets=true` to include target details inline.
