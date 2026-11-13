---
title: "Load an adapter"
source: https://docs.fireworks.ai/api-reference/specialized-model-inference/load
path: api-reference/specialized-model-inference/load
---

POST https://api.fireworks.ai/v1/accounts/{account_id}/deployedModels
Load a LoRA adapter onto serverless with Specialized Model Inference.

Preview

Loads a LoRA adapter onto the shared serverless pool. Loading takes about 2 to 5 minutes. You're billed per token only when you call the adapter.

```bash theme={null}
curl -X POST "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"accounts/$ACCOUNT_ID/models/my-lora\", \"serverless\": true}"
```

The firectl equivalent:

```bash theme={null}
firectl model load-lora my-lora --serverless --wait
```

## Path parameters

**account_id** `string` *required*

Your account ID.

## Body

**model** `string` *required*

The LoRA model to load: `accounts/{account_id}/models/{adapter_id}`. It must be in the `READY` state, trained on a supported base model, with rank 64 or lower.

**serverless** `boolean`

`true` to load onto Fireworks' shared serverless pool. Required unless you set `deployment`.

**deployment** `string`

Load onto one of your dedicated deployments instead: `accounts/{account_id}/deployments/{deployment_id}`. The deployment must have addons enabled. Billed by GPU-hour, not per token.

**displayName** `string`

Optional display name.

**description** `string`

Optional description.

> [!WARNING]
>
> Set exactly one of `serverless: true` or `deployment`. A request with both, or neither, is rejected.

## Response

Returns the [deployed model](/api-reference/specialized-model-inference/overview#the-deployed-model-object). It starts in `DEPLOYING`; send traffic once it's `DEPLOYED`. Save `name`: its last segment is the deployed model ID you need to unload over REST.

```json theme={null}
{
  "name": "accounts/your-account-id/deployedModels/abc123",
  "model": "accounts/your-account-id/models/my-lora",
  "serverless": true,
  "default": true,
  "state": "DEPLOYING"
}
```

## Behavior

* **One serverless copy per adapter.** Loading the same adapter onto serverless again fails while the first copy exists.
* **The first request is slower.** The first request after loading a LoRA adapter can take up to a minute. Later requests have much lower latency.
* **The bare model name.** The first copy of an adapter you load becomes its default and answers `accounts/<ACCOUNT_ID>/models/<LORA_ID>`. If another copy already holds that name, this copy loads with `default: false`. Call it with `accounts/<ACCOUNT_ID>/deployedModels/<DEPLOYED_MODEL_ID>`. There is no `#serverless` suffix. See [Which model string to use](/serverless/specialized-model-inference/overview#which-model-string-to-use).
* **Adapter limit.** You can load up to 3 adapters per base model on serverless at a time. Going over it returns `429 RESOURCE_EXHAUSTED`. Unload an adapter to free up a slot. For more slots, contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) or your account team. See [Supported models and limits](/serverless/specialized-model-inference/overview#supported-models-and-limits).

## Errors

| Status | Cause | Fix |
| - | - | - |
| `400` | Rank above 64 | Retrain with `--lora-rank 64` or lower |
| `400` | Base model isn't supported on serverless | Train on `accounts/fireworks/models/glm-5p3-flash` |
| `400` | `serverless` and `deployment` both set or both missing | Send only `"serverless": true` |
| `404` | The adapter doesn't exist in this account | Check the adapter ID with `firectl model get my-lora` |
| `409` | Already loaded, or an unload is still in progress | Check `firectl deployed-model list` and wait for the unload to finish |
| `429` | Adapter limit reached | Unload an adapter you don't need |

## Load onto a dedicated deployment instead

```bash theme={null}
curl -X POST "https://api.fireworks.ai/v1/accounts/$ACCOUNT_ID/deployedModels" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"accounts/$ACCOUNT_ID/models/my-lora\", \"deployment\": \"accounts/$ACCOUNT_ID/deployments/$DEPLOYMENT_ID\"}"
```
