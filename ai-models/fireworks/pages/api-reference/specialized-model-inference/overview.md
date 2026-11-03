---
title: "API overview"
source: https://docs.fireworks.ai/api-reference/specialized-model-inference/overview
path: api-reference/specialized-model-inference/overview
---

REST endpoints and the deployed model object for Specialized Model Inference on Serverless.

Preview

A loaded adapter is a **deployed model**: a record that ties an adapter in your account to where it serves. For an adapter on serverless, that record has `serverless: true`. You load and unload adapters with the control-plane API and call them with the inference API.

| Base URL | Use |
| - | - |
| `https://api.fireworks.ai/v1` | Load, list, get and unload adapters |
| `https://api.fireworks.ai/inference/v1` | Send requests to adapters |

All requests use `Authorization: Bearer $FIREWORKS_API_KEY`. The examples on these pages use the same variables as the [Get started](/serverless/specialized-model-inference/overview#get-started) guide:

```bash theme={null}
export FIREWORKS_API_KEY="fw_..."
export ACCOUNT_ID="your-account-id"
```

The examples use `my-lora` as the adapter ID. Replace it with your adapter's ID.

## Endpoints

| Action | Method and path |
| - | - |
| [Load an adapter](/api-reference/specialized-model-inference/load) | `POST /v1/accounts/{account_id}/deployedModels` |
| [List loaded adapters](/api-reference/specialized-model-inference/list) | `GET /v1/accounts/{account_id}/deployedModels` |
| [Get a loaded adapter](/api-reference/specialized-model-inference/get) | `GET /v1/accounts/{account_id}/deployedModels/{deployed_model_id}` |
| [Unload an adapter](/api-reference/specialized-model-inference/unload) | `DELETE /v1/accounts/{account_id}/deployedModels/{deployed_model_id}` |
| [Call an adapter](/serverless/specialized-model-inference/overview#step-3-call-the-serverless-endpoint) | `POST /inference/v1/chat/completions` or `/completions` |

> [!NOTE]
>
> Two IDs are involved. The **adapter ID** (for example `my-lora`) names the LoRA model you trained. The **deployed model ID** names one loaded copy of it. Load and call use the adapter ID. Get and unload over REST use the deployed model ID.

## The deployed model object

**name** `string`

Resource name: `accounts/{account_id}/deployedModels/{deployed_model_id}`. The last segment is the `deployed_model_id`.

**model** `string`

The LoRA model being served: `accounts/{account_id}/models/{adapter_id}`.

**serverless** `boolean`

`true` for adapters loaded on serverless. Set by Fireworks from where the adapter is placed.

**default** `boolean`

`true` if this copy answers requests to the bare model name, without a `#` suffix.

**state** `enum`

One of `DEPLOYING`, `DEPLOYED`, `UPDATING` or `UNDEPLOYING`. Send traffic once it's `DEPLOYED`.

**status** `object`

Details about the last load or unload, including any error.

**displayName** `string`

Optional display name.

**description** `string`

Optional description.

**createTime** `timestamp`

When the adapter was loaded.

**updateTime** `timestamp`

When the record last changed.

## Errors

| Status | Meaning |
| - | - |
| `400` | Bad request: rank above 64, unsupported base model, or `serverless` and `deployment` both set or both missing |
| `403` | Your model-access policy blocks the adapter's base model |
| `404` | The adapter or deployed model doesn't exist in this account, or your key is from a different account |
| `409` | The adapter is already loaded on serverless, or an unload is still in progress |
| `429` | `RESOURCE_EXHAUSTED`: you've hit your adapter limit (on load) or your rate limit (on inference) |
