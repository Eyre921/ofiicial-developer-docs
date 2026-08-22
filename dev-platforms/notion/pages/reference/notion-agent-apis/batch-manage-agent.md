---
title: "Batch manage agent"
source: https://developers.notion.com/reference/notion-agent-apis/batch-manage-agent
path: reference/notion-agent-apis/batch-manage-agent
---

post /v1/agents/batch
Asynchronously apply multiple agent management operations.

Each operation is authorized and applied independently. Poll the returned `status_url` to retrieve the completed batch result.

### Completed batch result

When the task succeeds, `result` is an `agent_batch_result` with a `results` array. Each entry includes `index`, `action`, `agent_id`, and `outcome`; use `index` to match it to the request because an agent can appear more than once.

| Outcome                       | Additional fields                                |
| :---------------------------- | :----------------------------------------------- |
| `update_status` success       | `status`, `pause_reason`, and `last_edited_time` |
| `update_credit_limit` success | `credit_limit` and `last_edited_time`            |
| `delete` success              | `status` (`deleted`) and `deleted_at`            |
| Error                         | `error`, a standard API error object             |
