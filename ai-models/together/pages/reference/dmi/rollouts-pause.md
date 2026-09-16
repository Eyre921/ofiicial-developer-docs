---
title: "Pause a rollout"
source: https://docs.together.ai/reference/dmi/rollouts-pause
path: reference/dmi/rollouts-pause
---

openapi.yaml POST /projects/{projectId}/endpoints/{endpointId}/rollouts/{id}/pause
Requests a running or stabilizing rollout to pause and records an optional reason. The response returns the PAUSING snapshot; poll GetRollout until state is PAUSED to confirm the executor has parked.
