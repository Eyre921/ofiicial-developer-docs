---
title: "Cancel a rollout"
source: https://docs.together.ai/reference/dmi/rollouts-cancel
path: reference/dmi/rollouts-cancel
---

openapi.yaml POST /projects/{projectId}/endpoints/{endpointId}/rollouts/{id}/cancel
Cancels a running, pausing, paused, system-paused, or stabilizing rollout by freezing the current traffic split into standing weights. Revert is removed and rejected; after canceling, start another canary rollout in either direction or rebalance the traffic split. The response is the accepted rollout snapshot; poll GetRollout until it reaches CANCELED.
