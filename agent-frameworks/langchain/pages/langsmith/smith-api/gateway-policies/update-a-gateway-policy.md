---
title: "Update a gateway policy"
source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/update-a-gateway-policy
path: langsmith/smith-api/gateway-policies/update-a-gateway-policy
---

/langsmith/langsmith-platform-openapi.json patch /v1/platform/gateway-policies/{id}
Partially updates a gateway policy. Only fields present in
the request body are applied; absent fields are left
unchanged. `policy_type` is immutable — to change a
policy's type, delete it and create a new one.

**config** if supplied must match the policy's type:
- spend-cap: `{"window": ..., "limit_usd": ...}`
- guard:     `{"version": 1, "detect": {...}, "timeout_seconds": <number>, "timeout_action": "allow"|"block"}`
Mismatched shapes are rejected with 400.

**default_spend_cap cascade:** editing a `default_spend_cap`
updates the config/action/enabled/priority on every
attached child policy so the template stays the source of
truth across rollouts.
