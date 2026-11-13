---
title: "Get a loaded adapter"
source: https://docs.fireworks.ai/api-reference/specialized-model-inference/get
path: api-reference/specialized-model-inference/get
---

GET https://api.fireworks.ai/v1/accounts/{account_id}/deployedModels/{deployed_model_id}
Check one loaded adapter's state, for example to see whether it's ready for traffic.

Preview

```bash theme={null}
curl "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels/$DEPLOYED_MODEL_ID" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

This takes the deployed model ID, not the adapter ID. Get it from the load response, or see [Find the deployed model ID](/api-reference/specialized-model-inference/list#find-the-deployed-model-id-for-an-adapter).

## Path parameters

**account_id** `string` *required*

Your account ID.

**deployed_model_id** `string` *required*

The last segment of the deployed model's `name`.

## Response

Returns the [deployed model](/api-reference/specialized-model-inference/overview#the-deployed-model-object).

## Wait until the adapter is ready

If you loaded without `--wait`, poll until `state` is `DEPLOYED`:

```bash theme={null}
until [ "$(curl -s "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels/$DEPLOYED_MODEL_ID" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" | jq -r .state)" = "DEPLOYED" ]; do
  echo "waiting..."; sleep 15
done
echo "ready"
```
