---
title: "List loaded adapters"
source: https://docs.fireworks.ai/api-reference/specialized-model-inference/list
path: api-reference/specialized-model-inference/list
---

GET https://api.fireworks.ai/v1/accounts/{account_id}/deployedModels
List every loaded copy of your adapters, on serverless and dedicated deployments.

Preview

```bash theme={null}
curl "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

The firectl equivalent:

```bash theme={null}
firectl deployed-model list
```

## Path parameters

**account\_id** `string` *required*

Your account ID.

## Query parameters

**filter** `string`

Filter results. For example, `serverless=true` returns only serverless copies.

**pageSize** `integer`

Maximum results per page.

**pageToken** `string`

The `nextPageToken` from a previous response.

**orderBy** `string`

Sort order, for example `createTime desc`.

## Response

```json theme={null}
{
  "deployedModels": [
    {
      "name": "accounts/your-account-id/deployedModels/abc123",
      "model": "accounts/your-account-id/models/my-lora",
      "serverless": true,
      "default": true,
      "state": "DEPLOYED"
    }
  ],
  "nextPageToken": ""
}
```

## Find the deployed model ID for an adapter

You need this ID to [get](/api-reference/specialized-model-inference/get) or [unload](/api-reference/specialized-model-inference/unload) over REST. This uses [jq](https://jqlang.org):

```bash theme={null}
DEPLOYED_MODEL_ID=$(curl -s "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" |
  jq -r --arg m "accounts/$ACCOUNT_ID/models/my-lora" \
    '.deployedModels[] | select(.model == $m and .serverless == true) | .name | split("/") | last')
echo "$DEPLOYED_MODEL_ID"
```
