---
title: "Unload an adapter"
source: https://docs.fireworks.ai/api-reference/specialized-model-inference/unload
path: api-reference/specialized-model-inference/unload
---

DELETE https://api.fireworks.ai/v1/accounts/{account_id}/deployedModels/{deployed_model_id}
Remove an adapter from serverless and free one of your adapter slots.

Preview

```bash theme={null}
curl -X DELETE "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels/$DEPLOYED_MODEL_ID" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY"
```

This takes the deployed model ID, not the adapter ID. Get it from the load response, or see [Find the deployed model ID](/api-reference/specialized-model-inference/list#find-the-deployed-model-id-for-an-adapter).

The firectl equivalent takes the adapter ID instead:

```bash theme={null}
firectl model unload-lora my-lora --serverless --wait
```

## Path parameters

**account\_id** `string` *required*

Your account ID.

**deployed\_model\_id** `string` *required*

The last segment of the deployed model's `name`.

## Behavior

The adapter stops serving shortly after and no longer counts toward your adapter limit. The LoRA model stays in your account, so you can load it again later.

Unloading removes one copy. To remove a dedicated copy instead, pass that copy's deployed model ID; [List](/api-reference/specialized-model-inference/list) shows each copy with its `serverless` value.

> [!NOTE]
>
> Wait for the unload to finish before loading the same adapter again. A load during an unload fails with `409`. The adapter is gone when it no longer appears in `firectl deployed-model list`.

## Errors

| Status | Cause | Fix |
| - | - | - |
| `404` | You passed the adapter ID instead of the deployed model ID, or it's already unloaded | Look up the deployed model ID, or use `firectl model unload-lora` |
