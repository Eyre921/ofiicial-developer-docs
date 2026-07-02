---
title: "Deploying Fine Tuned Models"
source: https://docs.fireworks.ai/fine-tuning/deploying-loras
path: fine-tuning/deploying-loras
---

Deploy one or multiple LoRA models fine tuned on Fireworks using live merge or multi-LoRA

After fine-tuning your model on Fireworks, deploy it to make it available for inference. Fireworks supports two deployment methods for LoRA fine-tuned models: **live merge** and **multi-LoRA**. Each method has different tradeoffs around performance, cost, and flexibility.

<Warning>
  Fine-tuned LoRA models, whether created on the Fireworks platform or imported, can **only** be deployed to **on-demand (dedicated) deployments**. Serverless deployment is not supported for LoRA models.
</Warning>

<Note>
  You can also upload and deploy LoRA models fine-tuned outside of Fireworks. See [importing fine-tuned models](/models/uploading-custom-models#importing-fine-tuned-models) for details.
</Note>

## Choosing a deployment method

Fireworks offers two ways to deploy LoRA fine-tuned models. The right choice depends on how many fine-tuned variants you need to serve and your performance requirements.

|                           | **Live merge**                                                                                 | **Multi-LoRA**                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **How it works**          | LoRA weights are merged into the base model at deployment time, creating a single merged model | Base model is deployed with addon support; LoRA adapters are loaded dynamically at request time |
| **Number of LoRAs**       | One per deployment                                                                             | Multiple per deployment                                                                         |
| **Inference performance** | Matches the base model (no overhead)                                                           | Some overhead per request due to dynamic adapter application                                    |
| **Throughput**            | Same as base model                                                                             | Lower maximum throughput under high concurrency                                                 |
| **Cost efficiency**       | One deployment per fine-tune                                                                   | Share a single deployment across many fine-tunes                                                |
| **Best for**              | Production workloads requiring maximum performance                                             | Experimentation, A/B testing, or serving many variants of the same base model                   |

<Tip>
  If you only need to serve a single fine-tuned model, **live merge is the recommended approach**. It delivers the best performance with the simplest setup.
</Tip>

## Live merge deployment

Live merge is the simplest way to deploy a fine-tuned model. Fireworks automatically merges the LoRA weights into the base model at deployment time, producing a model that performs identically to a natively fine-tuned model with no inference overhead.

### How it works

When you deploy a LoRA model directly, Fireworks:

1. Takes your LoRA adapter weights and the base model
2. Merges them into a single set of weights at deployment time
3. Serves the merged model as a standalone deployment

The result is a deployment that is indistinguishable from a fully fine-tuned model in terms of latency, throughput, and memory usage.

### Deploy with live merge

Deploy your LoRA fine-tuned model with a single command:

```bash theme={null}
firectl deployment create "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>"
```

<Check>
  Your deployment will be ready to use once it completes, with performance that matches the base model.
</Check>

### Sending requests

Send inference requests to your live-merge deployment by referencing the deployment directly:

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
      model="accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>",
      messages=[{"role": "user", "content": "Hello!"}]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>",
        "messages": [
          {
            "role": "user",
            "content": "Hello!"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

### When to use live merge

* You need maximum inference performance (latency and throughput matching the base model)
* You are serving a single fine-tuned model in production
* You want the simplest possible deployment workflow

## Multi-LoRA deployment

Multi-LoRA lets you load multiple LoRA adapters onto a single base model deployment. This is useful when you have several fine-tuned variants of the same base model and want to share GPU resources across them rather than creating a separate deployment for each.

### How it works

With multi-LoRA:

1. You deploy the base model with addon support enabled
2. You load one or more LoRA adapters onto the running deployment
3. At inference time, the correct adapter is selected and applied dynamically based on the model specified in the request

Because adapters are applied dynamically rather than merged, there is some performance overhead compared to live merge. This overhead increases with higher request concurrency.

### LoRA addon shape compatibility

Not all deployment shapes support LoRA addons. **FP8 and FP4 quantized shapes do not support `--enable-addons`.**

| Precision | `--enable-addons` supported? |
| --------- | ---------------------------- |
| BF16      | ✅ Yes                        |
| FP8       | ❌ No                         |
| FP4       | ❌ No                         |

Many base models default to FP8 or FP4 shapes. If you need LoRA addon inference on one of these models, you have two options:

**Option 1 — Use a BF16 deployment shape**

```bash theme={null}
# List available shapes for your model
firectl deployment-shape-version list --base-model accounts/fireworks/models/<MODEL_ID>

# Create deployment with a BF16 shape and addons enabled
firectl deployment create "accounts/fireworks/models/<BASE_MODEL_ID>" \
  --deployment-shape <bf16-shape-name> \
  --enable-addons
```

**Option 2 — Merge the adapter into a standalone model**

If no BF16 addon-compatible shape is available, use [live merge](#live-merge-deployment) (recommended for a single adapter) or merge the LoRA into a standalone Fireworks model, then deploy that merged model without `--enable-addons`. See [Uploading custom models](/models/uploading-custom-models#importing-fine-tuned-models) and [`firectl model create`](/tools-sdks/firectl/commands/model-create).

<Note>
  `"addons cannot be enabled with quantized precisions (FP8/FP4)"` — your model's default shape is quantized; use Option 1 or 2 above.

  `"the deployment shape version does not exist or you do not have access to it"` — the shape you requested is not available on your account; contact support.
</Note>

### Deploy with multi-LoRA

<Steps>
  <Step title="Create base model deployment with addon support">
    Deploy the base model with addons enabled:

    ```bash theme={null}
    firectl deployment create "accounts/fireworks/models/<BASE_MODEL_ID>" --enable-addons
    ```
  </Step>

  <Step title="Load LoRA adapters">
    Once the deployment is ready, load your LoRA models onto the deployment:

    ```bash theme={null}
    firectl load-lora <FINE_TUNED_MODEL_ID> --deployment <DEPLOYMENT_ID>
    ```

    Repeat this command for each LoRA adapter you want to load.
  </Step>
</Steps>

### Sending requests

To route inference requests to a specific LoRA adapter on a multi-LoRA deployment, set the `model` field to `<model_name>#<deployment_name>`. The `#` separator tells Fireworks to route the request to the specified adapter on the given deployment.

<Warning>
  **Deprecation notice:** The `deployedModel` request key for routing to LoRA addons is deprecated and will not be supported for any new deployments. Use the `model` field with the `<model_name>#<deployment_name>` format shown below.
</Warning>

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
      model="accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
      messages=[{"role": "user", "content": "Hello!"}]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        messages=[{"role": "user", "content": "Hello!"}]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
      messages: [
        {
          role: "user",
          content: "Hello!",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/<ACCOUNT_ID>/models/<FINE_TUNED_MODEL_ID>#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        "messages": [
          {
            "role": "user",
            "content": "Hello!"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

### When to use multi-LoRA

* You need to serve multiple fine-tuned models based on the same base model
* You want to maximize GPU utilization by sharing a single deployment
* You are running experiments or A/B tests across multiple fine-tuned variants
* You can accept some performance overhead compared to live merge

## Performance considerations

Live merge eliminates all LoRA-related inference overhead because the adapter weights are baked into the model at deployment time. The resulting deployment behaves exactly like a natively fine-tuned base model.

Multi-LoRA deployments incur overhead because adapters are applied dynamically:

* **Time to first token (TTFT):** Increases by roughly 10–30% due to adapter loading and prompt processing overhead
* **Generation speed:** Overhead grows with higher request concurrency
* **Maximum throughput:** Lower than a live-merge deployment under sustained load

For a deeper dive into LoRA performance characteristics and optimization strategies, see [Understanding LoRA Performance](/guides/understanding_lora_performance).

## Next steps

<CardGroup>
  <Card title="On-Demand Deployments" href="/guides/ondemand-deployments" icon="rocket">
    Learn about deployment configuration and optimization
  </Card>

  <Card title="Import Fine-Tuned Models" href="/models/uploading-custom-models#importing-fine-tuned-models" icon="upload">
    Upload LoRA models fine-tuned outside of Fireworks
  </Card>

  <Card title="LoRA Performance" href="/guides/understanding_lora_performance" icon="gauge-high">
    Understand performance tradeoffs and optimization strategies
  </Card>
</CardGroup>
