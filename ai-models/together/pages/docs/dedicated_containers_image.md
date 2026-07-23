---
title: "Image generation with Flux2"
source: https://docs.together.ai/docs/dedicated_containers_image
path: docs/dedicated_containers_image
---

Deploy a Flux2 image generation model on Together's managed GPU infrastructure using dedicated containers.

This example demonstrates deploying a text-to-image model using Dedicated Containers. You'll build a Sprocket worker that generates images from text prompts and deploy it to Together's managed GPU infrastructure.

## What you'll learn

* Deploying a custom model with Sprocket and Jig
* Returning base64-encoded images from your worker
* Submitting jobs via the Queue API and polling for results
* Configuring autoscaling for production workloads

## Prerequisites

* **Together API key**: Get one from [together.ai](https://together.ai)
* **Dedicated Containers access**: Contact [support@together.ai](mailto:support@together.ai) to enable for your organization
* **Docker**: For building container images. [Install Docker](https://docs.docker.com/engine/install)
* **Together CLI**: Install with `pip install "together[cli]" --upgrade` or `uv tool install "together[cli]"`

Set your API key:

```shell theme={null}
export TOGETHER_API_KEY=your_key_here
```

Install Together library:

<CodeGroup>
  ```shell pip theme={null}
  pip install together
  ```

  ```shell uv theme={null}
  uv add together
  ```
</CodeGroup>

## Overview

This example deploys a Flux2 text-to-image model as a Dedicated Container. The Sprocket worker handles job processing, and Together manages GPU provisioning, autoscaling, and observability.

**What gets deployed:**

* A Sprocket worker running on an H100 GPU
* Queue-based job processing for async image generation
* Automatic scaling based on queue depth

## How it works

1. **Build**: Jig builds a Docker image from your `pyproject.toml` configuration
2. **Push**: The image is pushed to Together's private container registry
3. **Deploy**: Together provisions an H100 GPU and starts your container
4. **Queue**: Jobs are submitted to the managed queue and processed by your Sprocket worker
5. **Scale**: The autoscaler adjusts replicas based on queue depth

## Project structure

```
flux2-dev/
├── pyproject.toml    # Configuration and dependencies
└── run.py             # Sprocket worker implementation
```

## Implementation

### Sprocket Worker Code

<CodeGroup>
  ```python run.py theme={null}
  import base64
  import logging
  from io import BytesIO

  import sprocket
  import torch
  from diffusers import Flux2Pipeline

  logging.basicConfig(level=logging.INFO)


  class Flux2Sprocket(sprocket.Sprocket):
      def setup(self) -> None:
          model_id = "diffusers/FLUX.2-dev-bnb-4bit"
          device = "cuda" if torch.cuda.is_available() else "cpu"

          logging.info(f"Loading Flux2 pipeline from {model_id} on {device}...")
          self.pipe = Flux2Pipeline.from_pretrained(
              model_id, torch_dtype=torch.bfloat16
          ).to(device)
          logging.info("Pipeline loaded successfully!")

      def predict(self, args: dict) -> dict:
          prompt = args.get("prompt", "a cat")

          # Optional parameters with defaults
          num_inference_steps = args.get("num_inference_steps", 28)
          guidance_scale = args.get("guidance_scale", 4.0)

          # Generate image
          logging.info(f"Generating image for prompt: {prompt[:50]}...")
          image = self.pipe(
              prompt=prompt,
              num_inference_steps=num_inference_steps,
              guidance_scale=guidance_scale,
          ).images[0]

          # Convert to base64
          buffered = BytesIO()
          image.save(buffered, format="PNG")
          img_str = base64.b64encode(buffered.getvalue()).decode()
          logging.info("Image generated successfully")

          return {"image": img_str, "format": "png", "encoding": "base64"}


  if __name__ == "__main__":
      sprocket.run(Flux2Sprocket())
  ```
</CodeGroup>

### Configuration

<CodeGroup>
  ```toml pyproject.toml theme={null}
  [project]
  name = "sprocket-flux2-dev"
  version = "0.1.0"
  dependencies = [
      "diffusers==0.36.0",
      "transformers==4.57.6",
      "torch==2.6.0",
      "pillow==12.2.0",
      "accelerate==1.13.0",
      "sprocket==0.1.4",
      "torchvision==0.21.0",
      "bitsandbytes==0.48.2",
      "safetensors==0.6.2",
  ]

  [[tool.uv.index]]
  name = "together-pypi"
  url = "https://pypi.together.ai/"

  [tool.uv.sources]
  sprocket = { index = "together-pypi" }

  [tool.jig.image]
  python_version = "3.11"
  # triton (via bitsandbytes) JIT-compiles CUDA kernels at import time, needs gcc
  system_packages = ["gcc", "g++"]
  cmd = "python3 run.py --queue"
  auto_include_git = false
  copy = ["run.py"]

  [tool.jig.deploy]
  description = "Flux2-dev Image Generation with Sprocket"
  gpu_type = "h100-80gb"
  gpu_count = 1
  cpu = 4
  memory = 32
  port = 8000
  min_replicas = 1
  max_replicas = 1
  ```
</CodeGroup>

## Key Concepts

### Base64 Image Encoding

Images are returned as base64-encoded strings for JSON compatibility:

```python theme={null}
def predict(self, args: dict) -> dict:
    # Generate the image
    image = self.pipe(prompt=args["prompt"]).images[0]

    # Encode as PNG in base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return {"image": img_str, "format": "png", "encoding": "base64"}
```

**Decoding on the client:**

```python theme={null}
import base64
from PIL import Image
from io import BytesIO

# Decode the response
image_data = base64.b64decode(response["image"])
image = Image.open(BytesIO(image_data))
image.save("output.png")
```

### Generation Parameters

Flux2 supports several parameters to control generation:

| Parameter             | Default   | Description                                              |
| --------------------- | --------- | -------------------------------------------------------- |
| `prompt`              | `"a cat"` | Text description of the image                            |
| `num_inference_steps` | `28`      | Denoising steps (more = better quality, slower)          |
| `guidance_scale`      | `4.0`     | How closely to follow the prompt (higher = more literal) |

```python theme={null}
image = self.pipe(
    prompt=prompt,
    num_inference_steps=28,  # Default for good quality/speed balance
    guidance_scale=4.0,  # Moderate guidance
).images[0]
```

## Deployment

### Deploy

<CodeGroup>
  ```shell Shell theme={null}
  # Deploy (builds, pushes, and creates deployment)
  tg beta jig deploy

  # Or deploy with cache warmup to reduce cold start latency
  tg beta jig deploy --warmup

  # Monitor startup (model download takes a few minutes on first deploy)
  tg beta jig logs --follow
  ```
</CodeGroup>

### Check Deployment Status

<CodeGroup>
  ```shell Shell theme={null}
  # View deployment status and replica health
  tg beta jig status
  ```
</CodeGroup>

Wait until the deployment shows `running` and replicas are ready before submitting jobs.

### Submit Jobs

Jobs are submitted to the managed queue and processed asynchronously. You'll need to poll for the result.

<CodeGroup>
  ```python Python SDK theme={null}
  from together import Together
  import base64
  import time
  from io import BytesIO
  from PIL import Image

  client = Together()
  deployment = "sprocket-flux2-dev"

  # Submit job to queue
  job = client.beta.queue.submit(
      model=deployment,
      payload={
          "prompt": "A serene Japanese garden with cherry blossoms",
          "num_inference_steps": 28,
          "guidance_scale": 4.0,
      },
  )
  print(f"Job submitted: {job.request_id}")

  # Poll for completion
  while True:
      status = client.beta.queue.retrieve(
          request_id=job.request_id,
          model=deployment,
      )

      if status.status == "done":
          # Decode and save the image
          image_data = base64.b64decode(status.outputs["image"])
          image = Image.open(BytesIO(image_data))
          image.save("output.png")
          print("Image saved to output.png")
          break
      elif status.status == "failed":
          print(f"Job failed: {status.error}")
          break
      else:
          print(f"Status: {status.status}")
          time.sleep(2)
  ```

  ```python requests theme={null}
  import base64
  import time
  import requests
  from io import BytesIO
  from PIL import Image

  api_key = "your_key_here"
  deployment = "sprocket-flux2-dev"

  # Submit job to queue
  response = requests.post(
      "https://api.together.ai/v1/queue/submit",
      headers={"Authorization": f"Bearer {api_key}"},
      json={
          "model": deployment,
          "payload": {
              "prompt": "A serene Japanese garden with cherry blossoms",
              "num_inference_steps": 28,
              "guidance_scale": 4.0,
          },
      },
  )
  job = response.json()
  print(f"Job submitted: {job['request_id']}")

  # Poll for completion
  while True:
      status_response = requests.get(
          f"https://api.together.ai/v1/queue/status?request_id={job['request_id']}&model={deployment}",
          headers={"Authorization": f"Bearer {api_key}"},
      )
      status = status_response.json()

      if status["status"] == "done":
          # Decode and save the image
          image_data = base64.b64decode(status["outputs"]["image"])
          image = Image.open(BytesIO(image_data))
          image.save("output.png")
          print("Image saved to output.png")
          break
      elif status["status"] == "failed":
          print(f"Job failed: {status.get('error')}")
          break
      else:
          print(f"Status: {status['status']}")
          time.sleep(2)
  ```

  ```shell cURL theme={null}
  # Submit job
  curl -X POST https://api.together.ai/v1/queue/submit \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sprocket-flux2-dev",
      "payload": {
        "prompt": "A futuristic cityscape at night with neon lights",
        "num_inference_steps": 28,
        "guidance_scale": 4.0
      }
    }'

  # Response: {"request_id": "req_abc123", "status": "pending"}

  # Poll for result (replace REQUEST_ID with actual value)
  curl "https://api.together.ai/v1/queue/status?request_id=REQUEST_ID&model=sprocket-flux2-dev" \
    -H "Authorization: Bearer $TOGETHER_API_KEY"

  # When status is "done", decode the image from outputs.image
  ```
</CodeGroup>

## Input Parameters

| Parameter             | Type   | Default   | Description                               |
| --------------------- | ------ | --------- | ----------------------------------------- |
| `prompt`              | string | `"a cat"` | Text description of the image to generate |
| `num_inference_steps` | int    | `28`      | Number of denoising steps                 |
| `guidance_scale`      | float  | `4.0`     | Classifier-free guidance scale            |

## Output

```json theme={null}
{
  "image": "iVBORw0KGgoAAAANSUhEUgAA...",
  "format": "png",
  "encoding": "base64"
}
```

* `image`: Base64-encoded PNG image data
* `format`: Image format (always `"png"`)
* `encoding`: Encoding type (always `"base64"`)

### Batch Processing and Autoscaling

The configuration above can be updated to include autoscaling by increasing the `max_replicas` parameter. Then when the queue backlog grows, more replicas are added automatically. When workers are idle, replicas are removed (down to `min_replicas`).

To scale more aggressively for high-throughput workloads:

```toml theme={null}
[tool.jig.deploy]
min_replicas = 2      # Always keep 2 warm replicas
max_replicas = 50     # Scale up to 50 replicas

[tool.jig.deploy.autoscaling]
metric = "QueueBacklogPerWorker"
target = 0.9   # More aggressive scaling (more workers than needed)
```

To scale to zero when idle, specify `min_replicas = 0` (saves costs but adds cold start latency):

```toml theme={null}
[tool.jig.deploy]
min_replicas = 0
max_replicas = 10
```

## Cleanup

When you're done, delete the deployment:

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig destroy
  ```
</CodeGroup>

## Next Steps

* [Video Generation Example](/docs/dedicated_containers_video) – Multi-GPU inference with torchrun
* [OpenAI-Compatible Endpoint Example](/docs/dedicated_containers_openai) – Serve the same model behind the OpenAI Images API
* [Quickstart](/docs/containers-quickstart) – Deploy your first container in 20 minutes
* [Sprocket SDK](/reference/dci-reference-sprocket) – Full SDK reference for workers
* [Jig CLI Reference](/reference/cli/jig) – CLI commands and configuration options
* [Deployments API Reference](/reference/deployments-list) – REST API for deployments, secrets, storage, and queues
