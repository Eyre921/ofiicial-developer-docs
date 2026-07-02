---
title: "Manage dedicated endpoints"
source: https://docs.together.ai/docs/dedicated-endpoints/manage
path: docs/dedicated-endpoints/manage
---

Create, start, stop, restart, list, update, and delete dedicated endpoints via the web UI or the Together API.

## Create an endpoint

<Tip>
  To avoid unexpected charges, you can set an [auto-shutdown](/docs/dedicated-endpoints/settings#auto-shutdown) timer when creating an endpoint. Make sure to review your active deployments periodically in the [models dashboard](https://api.together.ai/models) to stop endpoints you're no longer using.
</Tip>

<Tabs>
  <Tab title="CLI / SDK">
    First, list available hardware options for your model:

    <CodeGroup>
      ```shell Shell theme={null}
      together endpoints hardware --model Qwen/Qwen3.5-9B-FP8
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      response = client.endpoints.list_hardware(model="Qwen/Qwen3.5-9B-FP8")
      for hw in response.data:
          print(hw.id)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const response = await client.endpoints.listHardware({
        model: "Qwen/Qwen3.5-9B-FP8",
      });
      for (const hw of response.data) {
        console.log(hw.id);
      }
      ```
    </CodeGroup>

    You'll see output similar to this:

    ```shell Shell theme={null}
    Hardware ID              GPU    Memory    Count    Price (per minute)    availability
    1x_nvidia_h100_80gb_sxm  h100   80GB      1        \$0.06                ✓ available
    ```

    Then create the endpoint, using the ID for your preferred hardware option:

    <CodeGroup>
      ```shell Shell theme={null}
      together endpoints create \
        --model Qwen/Qwen3.5-9B-FP8 \
        --hardware 1x_nvidia_h100_80gb_sxm \
        --display-name "My endpoint" \
        --wait
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      endpoint = client.endpoints.create(
          model="Qwen/Qwen3.5-9B-FP8",
          hardware="1x_nvidia_h100_80gb_sxm",
          display_name="My endpoint",
          autoscaling={"min_replicas": 1, "max_replicas": 1},
      )
      print(endpoint.id, endpoint.name)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const endpoint = await client.endpoints.create({
        model: "Qwen/Qwen3.5-9B-FP8",
        hardware: "1x_nvidia_h100_80gb_sxm",
        display_name: "My endpoint",
        autoscaling: { min_replicas: 1, max_replicas: 1 },
      });
      console.log(endpoint.id, endpoint.name);
      ```
    </CodeGroup>

    ### Output

    A successful create returns the new endpoint object:

    ```json theme={null}
    {
      "object": "endpoint",
      "id": "endpoint-d23901de-ef8f-44bf-b3e7-de9c1ca8f2d7",
      "name": "devuser/Qwen/Qwen3.5-9B-FP8-a32b82a1",
      "display_name": "My endpoint",
      "model": "Qwen/Qwen3.5-9B-FP8",
      "hardware": "1x_nvidia_h100_80gb_sxm",
      "type": "dedicated",
      "owner": "devuser",
      "state": "PENDING",
      "autoscaling": { "min_replicas": 1, "max_replicas": 1 },
      "created_at": "2026-05-04T10:43:55.405Z"
    }
    ```

    These are the two fields you'll use the most:

    | Field  | Example                                         | What it's for                                                                                                                                                                                                                                           |
    | ------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `id`   | `endpoint-d23901de-ef8f-44bf-b3e7-de9c1ca8f2d7` | The unique identifier for the endpoint. Pass this as `endpoint_id` to all management operations: inspect, start, stop, update, and delete.                                                                                                              |
    | `name` | `devuser/Qwen/Qwen3.5-9B-FP8-a32b82a1`          | The model identifier you pass as the `model` parameter when calling [inference APIs](/docs/inference/overview). It includes your username, the base model, and a unique suffix so you can run multiple deployments of the same base model side by side. |

    The endpoint starts in `PENDING` and moves to `STARTED` once provisioning finishes (typically a few minutes). You can call the inference API as soon as the state is `STARTED`.

    ### Target an availability zone

    If you have latency or geographic constraints, you can target a specific availability zone. Only do this if you need to, since it can limit hardware availability.

    <CodeGroup>
      ```shell Shell theme={null}
      together endpoints create \
        --model Qwen/Qwen3.5-9B-FP8 \
        --hardware 1x_nvidia_h100_80gb_sxm \
        --display-name "My endpoint" \
        --availability-zone us-east-1a \
        --wait

      # List all availability zones
      together endpoints availability-zones
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      endpoint = client.endpoints.create(
          model="Qwen/Qwen3.5-9B-FP8",
          hardware="1x_nvidia_h100_80gb_sxm",
          display_name="My endpoint",
          availability_zone="us-east-1a",
          autoscaling={"min_replicas": 1, "max_replicas": 1},
      )

      # List all availability zones
      zones = client.endpoints.list_avzones()
      print(zones.avzones)
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      const endpoint = await client.endpoints.create({
        model: "Qwen/Qwen3.5-9B-FP8",
        hardware: "1x_nvidia_h100_80gb_sxm",
        display_name: "My endpoint",
        availability_zone: "us-east-1a",
        autoscaling: { min_replicas: 1, max_replicas: 1 },
      });

      // List all availability zones
      const zones = await client.endpoints.listAvzones();
      console.log(zones.avzones);
      ```
    </CodeGroup>
  </Tab>

  <Tab title="UI">
    <Steps>
      <Step title="Open the models page">
        Go to the [Models page](https://api.together.ai/models) in the playground. Under **All models**, select **Dedicated** to filter to models that support dedicated endpoint deployment.
      </Step>

      <Step title="Pick a model">
        Browse the available models and select the one you want to deploy.
      </Step>

      <Step title="Pick hardware">
        Choose hardware for the endpoint. Options range across RTX-6000, L40, A100 SXM, A100 PCIe, and H100 at different price points.
      </Step>

      <Step title="Deploy">
        Click the play button. The endpoint takes up to 10 minutes to come up. You can navigate away while it provisions and come back when it's ready.
      </Step>

      <Step title="Use the endpoint">
        Once ready, copy the **model identifier** shown on the endpoint page and use it as the `model` parameter in your API calls. You'll find the endpoint anytime under **My Models > Endpoints**.
      </Step>
    </Steps>

    **Need a custom configuration?** [Contact us](https://www.together.ai/forms/monthly-reserved).
  </Tab>
</Tabs>

## Inspect an endpoint

Get the current state and configuration of an endpoint by ID:

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints retrieve <endpoint_id>
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  endpoint = client.endpoints.retrieve("endpoint_id")
  print(endpoint)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const endpoint = await client.endpoints.retrieve("endpoint_id");
  console.log(endpoint);
  ```
</CodeGroup>

Sample output:

```
ID:           endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx
Name:         tester/Qwen/Qwen3.5-9B-FP8-bb04c904
Display Name: My endpoint
Hardware:     1x_nvidia_h100_80gb_sxm
Autoscaling:  Min=1, Max=1
Model:        Qwen/Qwen3.5-9B-FP8
Type:         dedicated
Owner:        tester
State:        READY
Created:      2025-02-18 11:55:50.686000+00:00
```

## List your endpoints

<CodeGroup>
  ```shell Shell theme={null}
  # All your endpoints
  together endpoints list

  # Only on-demand dedicated endpoints
  together endpoints list --type dedicated --usage-type on-demand
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  # All your endpoints
  response = client.endpoints.list(mine=True)
  for endpoint in response.data:
      print(endpoint.id, endpoint.state)

  # Only on-demand dedicated endpoints
  response = client.endpoints.list(
      mine=True,
      type="dedicated",
      usage_type="on-demand",
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  // All your endpoints
  const all = await client.endpoints.list({ mine: true });
  for (const endpoint of all.data) {
    console.log(endpoint.id, endpoint.state);
  }

  // Only on-demand dedicated endpoints
  const dedicated = await client.endpoints.list({
    mine: true,
    type: "dedicated",
    usage_type: "on-demand",
  });
  ```
</CodeGroup>

## Start, stop, and restart

Stopping an endpoint pauses billing. Restarting brings it back online without re-provisioning hardware (subject to availability).

<Tabs>
  <Tab title="CLI / SDK">
    <CodeGroup>
      ```shell Shell theme={null}
      # Stop a running endpoint (billing pauses immediately)
      together endpoints stop <endpoint_id>

      # Start a stopped endpoint
      together endpoints start <endpoint_id>
      ```

      ```python Python theme={null}
      from together import Together

      client = Together()

      # Stop a running endpoint (billing pauses immediately)
      client.endpoints.update("endpoint_id", state="STOPPED")

      # Start a stopped endpoint
      client.endpoints.update("endpoint_id", state="STARTED")
      ```

      ```typescript TypeScript theme={null}
      import Together from "together-ai";

      const client = new Together();

      // Stop a running endpoint (billing pauses immediately)
      await client.endpoints.update("endpoint_id", { state: "STOPPED" });

      // Start a stopped endpoint
      await client.endpoints.update("endpoint_id", { state: "STARTED" });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="UI">
    Open the [models page](https://api.together.ai/models), click your model to expand the row, click the three-dot menu, and select **Stop endpoint**. Confirm in the prompt. Once stopped, the endpoint shows as offline. The same menu lets you start it again if you stopped by mistake.
  </Tab>
</Tabs>

## Update endpoint settings

You can change replica counts on a running endpoint without re-creating it. Both `min_replicas` and `max_replicas` must be supplied together.

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints update --min-replicas 2 --max-replicas 4 <endpoint_id>
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  client.endpoints.update(
      "endpoint_id",
      autoscaling={"min_replicas": 2, "max_replicas": 4},
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  await client.endpoints.update("endpoint_id", {
    autoscaling: { min_replicas: 2, max_replicas: 4 },
  });
  ```
</CodeGroup>

For other settings (hardware, decoding optimizations), see [Endpoint settings](/docs/dedicated-endpoints/settings). Some updates require a full deployment.

## Delete an endpoint

Deletion is permanent. Stopped endpoints incur no charges, so prefer stopping unless you want to completely remove the endpoint.

<CodeGroup>
  ```shell Shell theme={null}
  together endpoints delete <endpoint_id>
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  client.endpoints.delete("endpoint_id")
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  await client.endpoints.delete("endpoint_id");
  ```
</CodeGroup>

## Troubleshooting

Endpoints don't always deploy immediately. Here are the most common reasons:

* **Low availability:** Hardware may be available but only enough for a partial replica count. The endpoint starts but scales to the available count. If your minimum replica count is higher than current capacity, the endpoint stays queued until capacity recovers. To avoid the wait, lower the minimum replica count.
* **Hardware unavailable error:** If you see "Hardware for endpoint not available now, please try again later", the hardware you selected is fully claimed. Try a comparable model on different hardware (use [whichllm.together.ai](https://whichllm.together.ai/) to find substitutes), or retry later.
* **Model not supported:** Not every model is available for dedicated endpoint deployments. For a list of deployable models, see the [dedicated endpoint model catalog](/docs/dedicated-endpoints/models). A fine-tuned model can only deploy on a dedicated endpoint if its base model is supported.

## Next steps

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/dedicated-endpoints/quickstart">
    Deploy and call your first endpoint in 5 minutes.
  </Card>

  <Card title="Available models" icon="list" href="/docs/dedicated-endpoints/models">
    Browse the list of available models for instant deployment.
  </Card>

  <Card title="Endpoint settings" icon="adjustments-horizontal" href="/docs/dedicated-endpoints/settings">
    Configure endpoint hardware, autoscaling, decoding, prompt caching.
  </Card>

  <Card title="Scaling" icon="arrows-maximize" href="/docs/dedicated-endpoints/scaling">
    Learn how endpoints scale and when to use vertical vs. horizontal scaling.
  </Card>
</CardGroup>
