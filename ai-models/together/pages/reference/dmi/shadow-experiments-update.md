---
title: "Update a shadow experiment"
source: https://docs.together.ai/reference/dmi/shadow-experiments-update
path: reference/dmi/shadow-experiments-update
---

PATCH /projects/{projectId}/endpoints/{endpointId}/shadowExperiments/{id}
Updates a shadow experiment's description or source sampling strategy. `updateMask` is required; source changes also require the current `etag` in the request body.
