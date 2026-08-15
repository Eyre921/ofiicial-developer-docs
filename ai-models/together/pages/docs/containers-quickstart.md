---
title: "Quickstart"
source: https://docs.together.ai/docs/containers-quickstart
path: docs/containers-quickstart
---

Deploy your first container in 20 minutes.

This guide walks you through deploying a sample inference worker to Together's managed GPU infrastructure.

## Requirements

* **Together API Key** – Required for all operations. Get one from [together.ai](https://together.ai).
* **Dedicated Containers access** – Contact your account representative or [support@together.ai](mailto:support@together.ai) to enable Dedicated Containers for your organization.
* **Docker** – For building and pushing container images. Get it [here](https://docs.docker.com/engine/install).
* **uv** (optional) – For Python/package management. Install from [astral-sh/uv](https://github.com/astral-sh/uv).

## Step 1: Install the Together CLI

<CodeGroup>
  ```shell uv theme={null}
  uv tool install "together[cli]"
  ```

  ```shell pip theme={null}
  pip install "together[cli]" --upgrade
  ```
</CodeGroup>

Set your API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=your_key_here
  ```
</CodeGroup>

## Step 2: Clone the Sprocket examples

<CodeGroup>
  ```shell Shell theme={null}
  git clone git@github.com:togethercomputer/sprocket.git
  cd sprocket
  ```
</CodeGroup>

The hello-world worker, included in `sprocket/examples/hello_world`, is a minimal Sprocket that returns a greeting:

<CodeGroup>
  ```python hello_world.py theme={null}
  import os
  import sprocket


  class HelloWorld(sprocket.Sprocket):
      def setup(self) -> None:
          self.greeting = "Hello"

      def predict(self, args: dict) -> dict:
          name = args.get("name", "world")
          return {"message": f"{self.greeting}, {name}!"}


  if __name__ == "__main__":
      queue_name = os.environ.get("TOGETHER_DEPLOYMENT_NAME", "hello-world")
      sprocket.run(HelloWorld(), queue_name)
  ```
</CodeGroup>

## Step 3: Build and deploy

Deployments can be configured with a `pyproject.toml` file.

The deployment name, set by the configuration, must be globally unique. The example worker uses this `pyproject.toml` configuration:

<CodeGroup>
  ```toml pyproject.toml theme={null}
  [project]
  name = "hello-world"
  version = "0.1.0"
  dependencies = ["sprocket"]

  [[tool.uv.index]]
  name = "together-pypi"
  url = "https://pypi.together.ai/"

  [tool.uv.sources]
  sprocket = { index = "together-pypi" }

  [tool.jig.image]
  python_version = "3.11"
  cmd = "python3 hello_world.py --queue"
  copy = ["hello_world.py"]

  [tool.jig.deploy]
  gpu_type = "none"
  gpu_count = 0
  cpu = 1
  memory = 2
  storage = 10
  port = 8000
  min_replicas = 1
  max_replicas = 1
  ```
</CodeGroup>

<Note>
  Change the project name in `pyproject.toml` and use this name for the rest of the tutorial.
</Note>

Navigate to the example worker and deploy:

<CodeGroup>
  ```shell Shell theme={null}
  cd examples/hello-world
  tg beta jig deploy
  ```
</CodeGroup>

This command:

1. Builds the Docker image from the example
2. Pushes it to Together's private registry
3. Creates a deployment on Together's GPU infrastructure

## Step 4: Watch deployment status

<CodeGroup>
  ```shell Shell theme={null}
  watch 'tg beta jig status'
  ```
</CodeGroup>

Wait until the deployment shows `running` and replicas are ready. Press `Ctrl+C` to stop watching. Note that `watch` is not installed by default on MacOS, use `brew install watch` or your package manager of choice.

<Note>
  You can also view the status of your deployments from the [Together AI web console](https://api.together.ai/containers).
</Note>

## Step 5: Test the health endpoint

<CodeGroup>
  ```shell Shell theme={null}
  curl https://api.together.ai/v1/deployment-request/hello-world/health \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

**Expected response:**

```json theme={null}
{"status": "healthy"}
```

## Step 6: Submit a job

<CodeGroup>
  ```shell Shell theme={null}
  curl -X POST "https://api.together.ai/v1/queue/submit" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "hello-world",
      "payload": {"name": "Together"},
      "priority": 1
    }'
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "request_id": "req_abc123"
}
```

Copy the `request_id` for the next step.

## Step 7: Get the job result

<CodeGroup>
  ```shell Shell theme={null}
  curl "https://api.together.ai/v1/queue/status?model=hello-world&request_id=req_abc123" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"
  ```
</CodeGroup>

<Note>
  Real request IDs use UUIDv7 format (e.g., `019ba379-92da-71e4-ac40-d98059fd67c7`). Replace `req_abc123` with your actual request ID from the submit response.
</Note>

**Response (when complete):**

```json theme={null}
{
  "request_id": "req_abc123",
  "model": "hello-world",
  "status": "done",
  "outputs": {"message": "Hello, Together!"}
}
```

## Step 8: View logs

Stream logs from your deployment:

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig logs --follow
  ```
</CodeGroup>

## Step 9: Clean up

When you're done, delete the deployment:

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig destroy
  ```
</CodeGroup>

## Next steps

Now that you've deployed your first container, explore the full platform:

* [**Dedicated Containers Overview**](/docs/dedicated-container-inference) – Architecture and concepts
* [**Jig CLI**](/docs/deployments-jig) – Build, push, deploy, secrets, and volumes
* [**Sprocket SDK**](/docs/deployments-sprocket) – Build queue-integrated inference workers
* [**API Reference**](/reference/deployments-list) – REST API for deployments, secrets, and queues

### Example guides

* [**Image Generation with Flux2**](/docs/dedicated_containers_image) – Single-GPU inference with 4-bit quantization
* [**Video Generation with Wan 2.1**](/docs/dedicated_containers_video) – Multi-GPU inference with torchrun
