---
title: "Overview"
source: https://docs.together.ai/docs/dedicated-endpoints/overview
path: docs/dedicated-endpoints/overview
---

Deploy a model for inference on dedicated GPUs.

<Tip>
  Using a coding agent? Install the [together-dedicated-model-inference](https://github.com/togethercomputer/skills/tree/main/skills/together-dedicated-model-inference) skill to let your agent deploy and manage dedicated endpoints automatically. See [agent skills](/docs/agent-skills) for details.
</Tip>

Dedicated model inference (DMI) lets you serve a model on reserved hardware, providing several advantages over [serverless models](/docs/serverless/overview):

* **Better performance:** Dedicated GPUs provide higher throughput, lower latency, and more predictable performance.
* **No hard rate limits:** You're only limited by the capacity of your selected hardware, plus the bounds of your autoscaling configuration.
* **Fine-tuned models:** Deploy a model you fine-tuned from a supported base model.
* **Cost-efficient at scale:** DMI bills per-GPU-minute, which is cheaper at high utilization than serverless models (which bill per-token).

Dedicated model inference uses the same [inference APIs](/docs/inference/overview#shared-inference-api) as serverless models, so you can prototype on serverless, then deploy on DMI without changing your application code.

<Tip>
  If you're running a stock model in production and want a defined SLA without managing hardware, contact sales for [provisioned throughput](/docs/inference/provisioned-throughput).
</Tip>

## Get started

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/dedicated-endpoints/quickstart">
    Deploy and call your first endpoint in a few minutes.
  </Card>

  <Card title="Concepts" icon="sitemap" href="/docs/dedicated-endpoints/concepts">
    The DMI resource model and development workflow.
  </Card>

  <Card title="Manage deployments" icon="tool" href="/docs/dedicated-endpoints/manage">
    Create, scale, stop, and delete your deployments.
  </Card>

  <Card title="Supported models" icon="list" href="/docs/dedicated-endpoints/models">
    Browse the list of Together-hosted models you can deploy.
  </Card>

  <Card title="Upload a fine-tuned model" icon="upload" href="/docs/dedicated-endpoints/custom-models">
    Deploy a model you fine-tuned from a supported base model.
  </Card>

  <Card title="Migrate from v1" icon="git-branch" href="/docs/dedicated-endpoints/migrate-from-v1">
    Migrate a dedicated endpoint to the new DMI resource model.
  </Card>
</CardGroup>

## Together CLI

The easiest way to manage dedicated model inference is by using the [Together CLI](/reference/cli/endpoints-beta). Each command creates and wires up the underlying resources for you:

| Command                    | Description                                                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tg beta endpoints deploy` | Deploys a model: creates an endpoint, attaches a deployment, and routes all traffic to it.                                                                        |
| `tg beta endpoints ab`     | Starts an [A/B test](/docs/dedicated-endpoints/ab-tests): adds a variant deployment and splits traffic between it and a control.                                  |
| `tg beta endpoints shadow` | Starts a [shadow experiment](/docs/dedicated-endpoints/shadow-experiments): mirrors a fraction of live traffic to a new deployment without serving its responses. |
| `tg beta endpoints rm`     | Deletes any endpoint, deployment, or experiment by its ID.                                                                                                        |

To learn more about the underlying resources, see [Concepts](/docs/dedicated-endpoints/concepts).

## Project scope

The `tg beta` commands, the management API, and the Python SDK's `client.beta.*` methods operate within a [Together AI project](/docs/projects). The CLI reads the project from the `TOGETHER_PROJECT_ID` environment variable, or you can pass `--project` on any command. If neither is set, it uses the project associated with your API key.

In the Python SDK, pass `project_id` to `Together()` or set `TOGETHER_PROJECT_ID`. Otherwise, call `client.whoami().project_id` before project-scoped API calls.

```bash theme={null}
export TOGETHER_PROJECT_ID=your_project_id
```

## Development workflow

To create a deployment, run the `tg beta endpoints deploy` command, passing the model and endpoint name. This creates an endpoint, attaches a deployment, and routes all traffic to it:

```bash theme={null}
tg beta endpoints deploy google/gemma-4-E4B-it \
  --endpoint my-endpoint
```

The command prints the new endpoint's **endpoint string** (`<project_slug>/<endpoint_name>`): pass it as the `model` parameter on inference requests.

Once the deployment is ready, send inference requests to the endpoint using the same [inference API](/docs/inference/overview#shared-inference-api) as serverless models. Pass the endpoint string as the `model` parameter:

<CodeGroup>
  ```python Python {6} theme={null}
  from together import Together

  client = Together(base_url="https://api-inference.together.ai/v1")

  response = client.chat.completions.create(
      model="your-project-slug/my-endpoint",
      messages=[{"role": "user", "content": "What is 2+2?"}],
      max_tokens=512,
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript {8} theme={null}
  import Together from 'together-ai';

  const client = new Together({
    baseURL: 'https://api-inference.together.ai/v1',
  });

  const response = await client.chat.completions.create({
    model: 'your-project-slug/my-endpoint',
    messages: [{ role: 'user', content: 'What is 2+2?' }],
    max_tokens: 512,
  });

  console.log(response.choices[0].message.content);
  ```

  ```bash cURL {5} theme={null}
  curl -s -X POST https://api-inference.together.ai/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "your-project-slug/my-endpoint",
      "messages": [{"role": "user", "content": "What is 2+2?"}],
      "max_tokens": 512
    }'
  ```
</CodeGroup>

`deploy` bundles the endpoint, deployment, and traffic-routing steps for you. To run those steps individually, or to drive them from the Python and TypeScript SDKs, see [Manage deployments](/docs/dedicated-endpoints/manage).

For a step-by-step walkthrough, [follow the quickstart](/docs/dedicated-endpoints/quickstart). For more details on the DMI resource model, see [Concepts](/docs/dedicated-endpoints/concepts).

## Key features

* **Deploy any supported model:** Run a [Together-hosted model](/docs/dedicated-endpoints/models), a [model you fine-tuned on Together](/docs/fine-tuning/overview), or [a fine-tuned model you upload](/docs/dedicated-endpoints/custom-models).
* **Autoscale on demand:** [Scale your deployments with replicas](/docs/dedicated-endpoints/scaling) to meet demand, and stop them when you don't need them to reduce costs.
* **Split traffic across deployments:** Host multiple deployments behind one endpoint URL and [route requests](/docs/dedicated-endpoints/split-traffic) between them by weight.
* **Compare deployments on live traffic:** Run an [A/B test](/docs/dedicated-endpoints/ab-tests) with control and variant splits to measure a candidate against a baseline before you promote it.
* **Monitor endpoints:** Track latency, throughput, and utilization in [built-in dashboards](/docs/dedicated-endpoints/monitoring), and trace lifecycle changes through the events feed.

## Pricing

Dedicated model inference bills per minute by hardware while a deployment runs, regardless of model or request volume. Each running replica bills independently and stops billing as soon as it scales down. For more details, see [Pricing](/docs/dedicated-endpoints/pricing).
