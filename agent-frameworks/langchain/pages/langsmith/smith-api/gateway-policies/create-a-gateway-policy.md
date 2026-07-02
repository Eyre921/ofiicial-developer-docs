---
title: "Create a gateway policy"
source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/create-a-gateway-policy
path: langsmith/smith-api/gateway-policies/create-a-gateway-policy
---

/langsmith/langsmith-platform-openapi.json post /v1/platform/gateway-policies
Creates a gateway policy for the calling organization.

**policy_type** is one of `spend_cap`, `default_spend_cap`, or
`guard`. The shape of `config` depends on policy_type:
- `spend_cap` / `default_spend_cap`:
`{"window": "hourly"|"daily"|"weekly"|"monthly", "limit_usd": <number>}`
- `guard`:
`{"version": 1, "detect": {"pii": <bool>, "secrets": <bool>}, "timeout_seconds": <number>, "timeout_action": "allow"|"block"}`
`timeout_seconds` (optional, 0.1–30) caps guard pipeline execution time; defaults to 2s. `timeout_action` defaults to `allow`.

**subject_matchers** is a list of `{key, value}` pairs.
`key` is one of `organization_id`, `workspace_id`, `user_id`,
`api_key_id`, or `run_rule_id`. Multiple matchers AND together. A
`default_spend_cap` uses `{key, value: ""}` so the runtime
materializes a per-subject child for every distinct subject
of that kind it sees in request metadata.

**action** is currently always `block`. Spend caps reject the
request with 402 when the limit is hit; guard policies redact
matched content in-place before forwarding upstream.

**Upsert by matchers:** if a policy with the same
`subject_matchers` already exists in this organization, the
existing policy is updated in place instead of a duplicate
being created. `id` is preserved. Returns 201 either way.
