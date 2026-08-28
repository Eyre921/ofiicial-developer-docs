---
title: "Limits"
source: https://developers.notion.com/workers/reference/limits
path: workers/reference/limits
---

Rate limits and other quotas that apply to workers.

Notion enforces rate limits on worker execution to keep the platform stable for every workspace. The limits below are standard workspace defaults. A workspace with custom limits may have different thresholds.

## Run rate limits

Worker runs use separate limits by capability type. Every worker in a workspace shares the applicable workspace budget.

| Action                                  | Default limit                       | Scope                                                             |
| --------------------------------------- | ----------------------------------- | ----------------------------------------------------------------- |
| Tool runs and queued webhook executions | 600 per hour; 60 per minute burst   | Per workspace, shared between tools and queued webhook executions |
| Sync runs                               | 600 per hour; 60 per minute burst   | Per workspace                                                     |
| Builds (`ntn workers deploy`)           | 100 per day; 10 per 5 minutes burst | Per workspace                                                     |

When a tool run, sync run, or queued webhook execution reaches its limit, its recorded worker run has a `rate_limit_error` result. The result includes `retryAfterSeconds` when available. The way a direct invocation surfaces that error depends on its transport.

## Webhook ingress limits

Before Notion accepts a webhook event, it applies a separate workspace-level admission limit of 600 requests per hour, with a burst limit of 60 requests per minute. This limit is separate from the queued webhook execution limit above.

Incoming webhook HTTP requests are also throttled before worker code runs:

| Scope                                        | Default limit             |
| -------------------------------------------- | ------------------------- |
| Per worker                                   | 600 requests per minute   |
| Per workspace (all webhook workers combined) | 1,200 requests per minute |

If a webhook request exceeds an ingress or admission limit, Notion responds synchronously with HTTP `429` and `{ "error": "Rate limit exceeded" }`. A request that receives `202 Accepted` was queued, but its later asynchronous execution can still reach the shared tool and webhook execution limit. Notion retries rate-limited webhook executions.

## Sync database write limits

Sync upserts and deletes (the `changes` your `execute` function returns) are limited separately from sync runs, since a single sync run can write many rows:

| Scope         | Default limit                          | Burst limit       |
| ------------- | -------------------------------------- | ----------------- |
| Per workspace | 1,000,000 database operations per hour | 25,000 per minute |

## Next steps

<CardGroup>
  <Card title="Syncs" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/arrowCircleLoopForward.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=25d8d1ea2405c9af06347df80ab90fcf" href="/workers/guides/syncs">
    Configure sync schedules and pace outbound requests to third-party APIs.
  </Card>

  <Card title="Webhooks" icon="https://mintcdn.com/notion-demo/yKfkO8UsVZTLLPNp/icons/nds/bell.svg?fit=max&auto=format&n=yKfkO8UsVZTLLPNp&q=85&s=0ee1c6e084361d853c48609a1f989a2c" href="/workers/guides/webhooks">
    Receive HTTP events and understand webhook delivery behavior.
  </Card>
</CardGroup>
