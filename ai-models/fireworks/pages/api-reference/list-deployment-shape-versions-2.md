---
title: "List Deployment Shapes Versions"
source: https://docs.fireworks.ai/api-reference/list-deployment-shape-versions
path: api-reference/list-deployment-shape-versions
---

get /v1/accounts/{account_id}/deploymentShapes/{deployment_shape_id}/versions

Use this endpoint to query available deployment shape versions for a given model. Use `-` as a wildcard for both `account_id` and `deployment_shape_id` to search across all accounts and shapes.

## Example: List shapes for a model

To list validated deployment shapes for a specific model, use the `filter` parameter with `snapshot.base_model` and `latest_validated=true`:

```bash theme={null}
curl -s "https://api.fireworks.ai/v1/accounts/-/deploymentShapes/-/versions?filter=snapshot.base_model%3D%22accounts%2Ffireworks%2Fmodels%2Fgpt-oss-120b%22%20AND%20latest_validated%3Dtrue&order_by=create_time%20desc" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" | jq .
```

### Filter syntax

The `filter` parameter uses [AIP-160 filtering](https://google.aip.dev/160). Common patterns:

| Filter                                                       | Description                                            |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| `snapshot.base_model="accounts/fireworks/models/MODEL_NAME"` | Filter by base model                                   |
| `latest_validated=true`                                      | Only return the latest validated version of each shape |

Combine multiple conditions with `AND`:

```
snapshot.base_model="accounts/fireworks/models/MODEL_NAME" AND latest_validated=true
```

<Note>
  Remember to URL-encode the filter value when using curl directly. `=` becomes `%3D`, `"` becomes `%22`, and `/` becomes `%2F`.
</Note>
