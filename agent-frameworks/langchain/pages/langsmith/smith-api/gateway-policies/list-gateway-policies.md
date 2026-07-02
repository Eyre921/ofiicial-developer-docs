---
title: "List gateway policies"
source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/list-gateway-policies
path: langsmith/smith-api/gateway-policies/list-gateway-policies
---

/langsmith/langsmith-platform-openapi.json get /v1/platform/gateway-policies
Returns every gateway policy in the current organization.
The response includes both admin-created policies and
runtime-materialized children of `default_spend_cap`
policies (children carry `parent_policy_id`).

**Spend tracking:** each spend-cap policy carries
`current_spend_usd` — the spend accumulated in the policy's
active window.
