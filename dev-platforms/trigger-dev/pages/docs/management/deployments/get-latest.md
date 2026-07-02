---
title: "Get latest deployment"
source: https://trigger.dev/docs/management/deployments/get-latest
path: docs/management/deployments/get-latest
---

v3-openapi GET /api/v1/deployments/latest
Retrieve information about the latest unmanaged deployment for the authenticated project.

<Warning>
  This endpoint only returns **unmanaged** deployments, which are used in self-hosted setups. It
  will return `404` for standard CLI deployments made against Trigger.dev Cloud.

  If you're using the CLI to deploy, use the [list deployments](/docs/management/deployments/list) endpoint instead.
</Warning>
