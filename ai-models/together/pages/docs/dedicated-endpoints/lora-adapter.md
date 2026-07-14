---
title: "Serve multiple LoRA adapters on one endpoint"
source: https://docs.together.ai/docs/dedicated-endpoints/lora-adapter
path: docs/dedicated-endpoints/lora-adapter
---

Attach, list, and remove LoRA adapters on a running dedicated endpoint to serve several adapters from one deployment.

<Note>
  This feature is in beta. You can share feedback on the [Together AI Discord](https://discord.gg/togetherai) or by [contacting support](https://www.together.ai/contact-sales).
</Note>

If you already run a LoRA-enabled [dedicated endpoint](/docs/dedicated-endpoints/overview) for an adapter's base model, you can attach the adapter to that endpoint instead of [deploying it on its own hardware](/docs/dedicated-endpoints/adapter#deploy-the-adapter). One endpoint can serve multiple LoRA adapters that share the same base model, and inference requests select among them by model name.

Use this when you want to:

* Serve several adapters trained against the same base model from one endpoint.
* Avoid paying for separate hardware per adapter.
* Change which adapter handles traffic without redeploying.

## Requirements

The target endpoint must be a private dedicated endpoint with LoRA enabled, running a base model that's compatible with the adapter. The adapter's base model must match the endpoint's model, and both the adapter and the endpoint must be owned by the same account.

If you don't have a LoRA-enabled endpoint for the base model yet, [create one](/docs/dedicated-endpoints/adapter#deploy-the-adapter) first.

## Supported models

LoRA-enabled endpoints are available for the models below. Each adapter you attach must target the same model as the endpoint and train only from that model's supported target modules. **Max loaded adapters** is the maximum number of adapters you can keep attached to a single endpoint for that model.

| Model                                                | Supported target modules                                                                                                                                                                          | Max loaded adapters |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `google/gemma-3-270m-it-lora`                        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       | 16                  |
| `google/gemma-3-27b-it-lora`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       | 16                  |
| `google/gemma-4-31B-it-lora`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       | 16                  |
| `mistralai/Mixtral-8x7B-Instruct-v0.1-FP8-Lora`      | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            | 16                  |
| `meta-llama/Llama-3.3-70B-Instruct-FP8-Lora`         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       | 16                  |
| `meta-llama/Llama-4-Scout-17B-16E-Instruct-FP8-Lora` | `k_proj`, `o_proj`, `q_proj`, `v_proj`, `shared_expert.gate_proj`, `shared_expert.up_proj`, `shared_expert.down_proj`, `feed_forward.gate_proj`, `feed_forward.up_proj`, `feed_forward.down_proj` | 16                  |
| `Qwen/Qwen3.5-0.8B-Lora`                             | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-2B-Lora`                               | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-4B-Lora`                               | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-9B-Lora`                               | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-27B-Lora`                              | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-35B-A3B-Base-Lora`                     | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-35B-A3B-Lora`                          | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-122B-A10B-Lora`                        | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.5-397B-A17B-Lora`                        | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.6-27B-Lora`                              | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |
| `Qwen/Qwen3.6-35B-A3B-Lora`                          | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` <sup>†</sup>                                                                                                          | 5                   |

<Note>
  <sup>†</sup> For the Qwen3.5 and Qwen3.6 models, adapters target the standard attention (`q_proj`, `k_proj`, `v_proj`, `o_proj`) and MLP (`gate_proj`, `up_proj`, `down_proj`) projections. Adapters that target other layers, such as the vision encoder, may not load for serving.
</Note>

## Attach an adapter from the dashboard

<Steps>
  <Step title="Open the adapter">
    Go to [My Models](https://api.together.ai/models) and open the adapter you want to attach.
  </Step>

  <Step title="Select Deploy adapter to endpoint">
    From the actions menu on the adapter, select **Deploy adapter to endpoint**. A dialog lists running endpoints that are LoRA-enabled and match the adapter's base model.
  </Step>

  <Step title="Select an endpoint and deploy">
    Select a compatible endpoint, then select **Deploy adapter**. If no endpoints appear, create a LoRA-enabled dedicated endpoint for the base model first.
  </Step>
</Steps>

## Attach an adapter from the API

The API uses two different identifiers for the base endpoint:

* `<ENDPOINT_ID>` is the endpoint's `id`, a system-generated handle like `endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08c1`. It goes in the URL path and as the first argument to the SDK and CLI calls.
* `<ENDPOINT_NAME>` is the endpoint's `name`, an auto-generated namespaced string like `tester/Qwen/Qwen3.5-9B-FP8-bb04c904`. It's the prefix of the combined `model_id`. This isn't the display name you set at creation; read it from the endpoint's `name` field.

Both are returned when you create an endpoint and by the list and get operations. Retrieve them for an existing endpoint with the same calls used to [manage endpoints](/docs/dedicated-endpoints/manage#list-your-endpoints):

<CodeGroup>
  ```shell CLI theme={null}
  together endpoints list
  ```

  ```python Python theme={null}
  for endpoint in client.endpoints.list(mine=True).data:
      print(endpoint.id, endpoint.name)
  ```

  ```typescript TypeScript theme={null}
  const endpoints = await client.endpoints.list({ mine: true });
  for (const endpoint of endpoints.data) {
    console.log(endpoint.id, endpoint.name);
  }
  ```
</CodeGroup>

Each adapter is identified by a combined `model_id` in the form `endpoint_name:adapter_model_name`, where `adapter_model_name` is the `model_name` returned when you uploaded the adapter. The `endpoint_name` prefix must match the endpoint resolved from `<ENDPOINT_ID>`.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  result = client.endpoints.adapters.add(
      "<ENDPOINT_ID>",
      model_id="<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>",
  )
  print(result.api_model_id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const result = await client.endpoints.adapters.add("<ENDPOINT_ID>", {
    model_id: "<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>",
  });
  console.log(result.model_id);
  ```

  ```shell CLI theme={null}
  together endpoints adapters add <ENDPOINT_ID> <ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>
  ```

  ```shell cURL theme={null}
  curl -X POST "https://api.together.ai/v1/endpoints/<ENDPOINT_ID>/adapters" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model_id": "<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>"}'
  ```
</CodeGroup>

The response echoes the bound `model_id`:

```json theme={null}
{ "model_id": "<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>" }
```

## List attached adapters

<CodeGroup>
  ```python Python theme={null}
  adapters = client.endpoints.adapters.list("<ENDPOINT_ID>")
  for adapter in adapters.data or []:
      print(adapter.api_model_id, adapter.adapter_name, adapter.endpoint_name)
  ```

  ```typescript TypeScript theme={null}
  const adapters = await client.endpoints.adapters.list("<ENDPOINT_ID>");
  for (const adapter of adapters.data ?? []) {
    console.log(adapter.model_id, adapter.adapter_name, adapter.endpoint_name);
  }
  ```

  ```shell CLI theme={null}
  together endpoints adapters list <ENDPOINT_ID>
  ```

  ```shell cURL theme={null}
  curl "https://api.together.ai/v1/endpoints/<ENDPOINT_ID>/adapters" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

The list alias `ls` is also accepted by the CLI. Add `--json` to print the raw API response:

```json theme={null}
{
  "object": "list",
  "data": [
    {
      "model_id": "<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>",
      "adapter_name": "<ADAPTER_MODEL_NAME>",
      "endpoint_name": "<ENDPOINT_NAME>"
    }
  ]
}
```

<Note>
  In the Python SDK, the combined identifier is exposed on the response object as `api_model_id`, while the JSON field returned by the API is `model_id`. The TypeScript SDK and the raw API both use `model_id`.
</Note>

## Remove an adapter

Removing an adapter detaches it from the endpoint. The uploaded adapter stays in your account and can be re-attached or deployed elsewhere.

<CodeGroup>
  ```python Python theme={null}
  client.endpoints.adapters.remove(
      "<ENDPOINT_ID>",
      model_id="<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>",
  )
  ```

  ```typescript TypeScript theme={null}
  await client.endpoints.adapters.remove("<ENDPOINT_ID>", {
    model_id: "<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>",
  });
  ```

  ```shell CLI theme={null}
  together endpoints adapters remove <ENDPOINT_ID> <ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>
  ```

  ```shell cURL theme={null}
  curl -X DELETE "https://api.together.ai/v1/endpoints/<ENDPOINT_ID>/adapters" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model_id": "<ENDPOINT_NAME>:<ADAPTER_MODEL_NAME>"}'
  ```
</CodeGroup>

The CLI accepts `delete` and `rm` as aliases for `remove`.

## Run inference

Once the adapter is attached, send inference requests using the adapter model name as the `model` parameter. Requests are routed to the endpoint automatically. You can also pass the full `endpoint_name:adapter_model_name` form.

<CodeGroup>
  ```python Python theme={null}
  response = client.chat.completions.create(
      model="<ADAPTER_MODEL_NAME>",
      messages=[{"role": "user", "content": "Hello!"}],
      max_tokens=128,
  )
  print(response.choices[0].message.content)
  ```

  ```shell cURL theme={null}
  curl -X POST "https://api.together.ai/v1/chat/completions" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "<ADAPTER_MODEL_NAME>",
      "messages": [{"role": "user", "content": "Hello!"}],
      "max_tokens": 128
    }'
  ```
</CodeGroup>

## Serve multiple adapters

A LoRA-enabled endpoint can hold several adapters at once, as long as they all share the endpoint's base model. Attach each one with a separate add call, then route requests to whichever adapter you need by passing its model name.

All attached adapters share the endpoint's hardware and replicas, so concurrent traffic across adapters draws on the same capacity rather than scaling independently. If load grows, raise the endpoint's replica count through [autoscaling](/docs/dedicated-endpoints/scaling).

## Troubleshooting

* **"model\_id must be in format 'endpoint\_model\_name:adapter\_name'":** The `model_id` field must contain exactly one `:` separator with non-empty parts.

* **"endpoint name in model\_id does not match endpoint":** The endpoint name prefix in `model_id` doesn't match the endpoint resolved from the URL path.

* **"Could not find model":** The adapter model name after the `:` doesn't exist or isn't owned by your account.

* **"No endpoint with this id exists":** The endpoint ID in the URL doesn't exist or isn't owned by your account.

* **"endpoint does not have LoRA enabled":** The target endpoint wasn't created with LoRA support enabled.

* **"adapter base model is not compatible with endpoint model":** The adapter's base model doesn't match the model running on the endpoint.

* **"adapter is already bound to endpoint":** The adapter is already attached to a different endpoint. Remove it first before attaching it to a new one. Re-attaching to the same endpoint is allowed.

* **"adapter is not bound to endpoint":** When removing, the adapter isn't currently routed to this endpoint.

* **"new\_lora\_model must be a dedicated endpoint":** Only dedicated endpoints, not serverless, can be used as adapter targets.

* **"new\_lora\_model cannot be a public dedicated endpoint":** Only private endpoints can be used as adapter targets.
