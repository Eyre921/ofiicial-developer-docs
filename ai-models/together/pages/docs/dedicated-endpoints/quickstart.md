---
title: "Quickstart"
source: https://docs.together.ai/docs/dedicated-endpoints/quickstart
path: docs/dedicated-endpoints/quickstart
---

Pick a model, deploy a dedicated endpoint with one CLI command, and send your first request in under 5 minutes.

## Prerequisites

Before you begin, make sure you have:

* [Created an account](https://api.together.ai/settings/projects/~first/api-keys) and generated an API key.
* [Set your API key as an environment variable](https://docs.together.ai/docs/api-keys-authentication) in your terminal.
* [Installed the Together CLI](/reference/cli/getting-started) on your machine.
* [Installed the Python or TypeScript SDK](/docs/quickstart#step-2-install-the-sdk).

## Step 1: Pick a model

You can deploy any model from the [dedicated endpoint model catalog](/docs/dedicated-endpoints/models), or upload your own [custom model](/docs/dedicated-endpoints/custom-models). For this quickstart we'll use `Qwen/Qwen3.5-9B-FP8`.

## Step 2: Pick your hardware

Some models can be deployed on multiple hardware types at different price points. List compatible hardware options with the CLI:

```shell Shell theme={null}
tg endpoints hardware --model Qwen/Qwen3.5-9B-FP8
```

You'll see output similar to this:

```text theme={null}
Hardware ID              GPU    Memory    Count    Price (per minute)    availability
1x_nvidia_h100_80gb_sxm  h100   80GB      1        \$0.06                ✓ available
```

## Step 3: Deploy the endpoint

Create the endpoint with the [`tg endpoints create`](/reference/cli/endpoints#create) command, using the hardware ID output from the previous step. The `--wait` flag blocks until the endpoint is ready:

```shell Shell theme={null}
tg endpoints create \
  --model Qwen/Qwen3.5-9B-FP8 \
  --hardware 1x_nvidia_h100_80gb_sxm \
  --display-name "My quickstart endpoint" \
  --wait
```

When it returns, copy the endpoint name from the `Name` field (e.g., `tester/Qwen/Qwen3.5-9B-FP8-bb04c904`).

<Note>
  The **endpoint name** is passed to the `model` parameter for API inference requests. The **endpoint ID** (e.g., `endpoint-e6c6b82f-...`) is used for management operations like start, stop, update, and delete.
</Note>

## Step 4: Send a request

Send a request to your endpoint, passing the name you copied in the previous step into the `model` parameter:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="tester/Qwen/Qwen3.5-9B-FP8-bb04c904",
      messages=[{"role": "user", "content": "Hello!"}],
  )
  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.chat.completions.create({
    model: "tester/Qwen/Qwen3.5-9B-FP8-bb04c904",
    messages: [{ role: "user", content: "Hello!" }],
  });
  console.log(response.choices[0].message.content);
  ```

  ```shell cURL theme={null}
  curl -X POST https://api.together.ai/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "tester/Qwen/Qwen3.5-9B-FP8-bb04c904",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```
</CodeGroup>

<Check>
  Congrats! You just deployed and called your first dedicated endpoint on Together AI.
</Check>

## Stop the endpoint

Dedicated endpoints bill per minute as long as they're running. Stop your endpoint when you no longer need it so you don't accrue charges:

```shell Shell theme={null}
tg endpoints stop <endpoint_id>
```

Find the endpoint ID in the `ID` field of [`tg endpoints retrieve`](/reference/cli/endpoints#retrieve), or run [`tg endpoints list`](/reference/cli/endpoints#list) to see all your endpoints.

## Next steps

<CardGroup>
  <Card title="Available models" icon="list" href="/docs/dedicated-endpoints/models">
    Browse the list of available models for instant deployment.
  </Card>

  <Card title="Manage endpoints" icon="tool" href="/docs/dedicated-endpoints/manage">
    Create, start, stop, restart, list, update, and delete dedicated endpoints via the web UI, API, or CLI.
  </Card>

  <Card title="Endpoint settings" icon="adjustments-horizontal" href="/docs/dedicated-endpoints/settings">
    Configure endpoint hardware, autoscaling, decoding, and prompt caching.
  </Card>

  <Card title="Upload a custom model" icon="upload" href="/docs/dedicated-endpoints/custom-models">
    Upload your own model weights.
  </Card>
</CardGroup>
