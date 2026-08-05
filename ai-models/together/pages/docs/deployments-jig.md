---
title: "Jig CLI"
source: https://docs.together.ai/docs/deployments-jig
path: docs/deployments-jig
---

Build, push, and deploy containers to Together's managed GPU infrastructure.

Jig is a lightweight CLI for building Docker images from a `pyproject.toml`, pushing them to Together's private container registry, and managing deployments. It's included with the [Together Python library](https://github.com/togethercomputer/together-python).

<Tip>
  **See Jig in action:** Check out the end-to-end examples for [Image Generation with Flux2](/docs/dedicated_containers_image) and [Video Generation with Wan 2.1](/docs/dedicated_containers_video).
</Tip>

## The deploy workflow

Jig combines several steps into a single `deploy` command:

1. **Init:** `tg beta jig init` scaffolds a `pyproject.toml` with sensible defaults.
2. **Build:** Generates a Dockerfile from your config and builds the image locally.
3. **Push:** Pushes the image to Together's registry at `registry.together.ai`.
4. **Deploy:** Creates or updates the deployment on Together's infrastructure.

<CodeGroup>
  ```shell Shell theme={null}
  # One command does it all
  tg beta jig deploy

  # Or step by step
  tg beta jig build
  tg beta jig push
  tg beta jig deploy --image registry.together.ai/myproject/mymodel@sha256:abc123
  ```
</CodeGroup>

Once deployed, monitor your containers:

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig status
  tg beta jig logs --follow
  ```
</CodeGroup>

For the full list of commands and flags, see the [Jig CLI reference](/reference/cli/jig).

<Tip>
  Jig builds images locally and pushes them to Together's registry. ML images can be 10GB+, so building on a machine with a fast network connection saves significant time compared to pushing from a laptop over wifi.
</Tip>

## Cache warmup

The `--warmup` option lets you pre-generate inference engine compile caches (such as those created by `torch.compile` or TensorRT) at build time, rather than waiting for the first request in production. This can significantly reduce cold-start latency.

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig deploy --warmup
  tg beta jig build --warmup   # Build only, no deploy
  ```
</CodeGroup>

### How it works

1. **Build phase**: Jig builds the base image normally
2. **Warmup phase**: Jig runs the container with GPU access, mounting your local workspace to `/app`
3. **Cache capture**: The container runs your Sprocket's `warmup_inputs`, generating compile caches
4. **Final image**: Jig builds a new image layer with the cache baked in

The cache location inside the container is controlled by `WARMUP_ENV_NAME` (default: `TORCHINDUCTOR_CACHE_DIR`) and `WARMUP_DEST` (default: `torch_cache`).
Jig sets the environment variable to point to the cache directory during warmup and copies its contents into the final image.

### Sprocket integration

Define `warmup_inputs` on your Sprocket class to specify what inputs to run during warmup:

<CodeGroup>
  ```python app.py theme={null}
  import base64
  import logging
  import os
  from io import BytesIO

  import sprocket
  import torch
  from diffusers import Flux2Pipeline


  class Flux2Sprocket(sprocket.Sprocket):
      # Define inputs to run during warmup - this pre-generates compile caches
      warmup_inputs = [
          {"prompt": "a white cat"},
      ]

      def setup(self) -> None:
          device = "cuda" if torch.cuda.is_available() else "cpu"

          logging.info(f"Loading Flux2 pipeline on {device}...")
          self.pipe = Flux2Pipeline.from_pretrained(
              "diffusers/FLUX.2-dev-bnb-4bit",
              torch_dtype=torch.bfloat16,
          ).to(device)
          logging.info("Pipeline loaded successfully!")

      def predict(self, args: dict) -> dict:
          prompt = args.get("prompt", "a cat")
          num_inference_steps = args.get("num_inference_steps", 28)
          guidance_scale = args.get("guidance_scale", 4.0)

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

          return {"image": img_str, "format": "png", "encoding": "base64"}


  if __name__ == "__main__":
      queue_name = os.environ.get(
          "TOGETHER_DEPLOYMENT_NAME", "sprocket-flux2-dev"
      )
      sprocket.run(Flux2Sprocket(), queue_name)
  ```
</CodeGroup>

During a --warmup build, the `predict(...)` function is invoked once for each input specified in `warmup_inputs`. If `warmup_inputs` is empty or not defined, the warmup step invokes `predict({})` once as a fallback. Make sure all the compile paths would be exercised by the warmup inputs.
In normal build (no `--warmup`), an empty `warmup_inputs` means no warmup runs at all.

Since the local workspace is mounted to `/app`, model weights and example inputs can live in your project directory and be referenced directly.

### Requirements

* A GPU on your build machine: warmup runs your model locally to generate caches. If you don't have a local GPU, [Together instant clusters](/docs/gpu-clusters-overview) provide on-demand H100s with fast connectivity to Together's container registry.
* `warmup_inputs` defined on your Sprocket with representative inputs
* Weights and example inputs accessible in local workspace

## Secrets

Secrets are encrypted environment variables injected into your container at runtime. Use them for API keys, tokens, and other sensitive values that shouldn't be baked into the image.

<Warning>
  A name cannot appear in both `[tool.jig.deploy.environment_variables]` and a secret. `jig deploy` fails and lists each colliding name if the same name is defined in both places. Remove the duplicate from your config or run `tg beta jig secrets unset --name <name>`.
</Warning>

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig secrets set --name HF_TOKEN --value hf_xxxxx --description "Hugging Face token"
  tg beta jig secrets list
  tg beta jig secrets unset HF_TOKEN
  ```
</CodeGroup>

Secrets are available to your container as environment variables at runtime. Do not also define the same name under `[tool.jig.deploy.environment_variables]`. See the [Jig CLI reference](/reference/cli/jig#secrets) for all secrets commands.

## Volumes

Volumes let you mount read-only data, like model weights, into your container without baking them into the image. This keeps images small and lets you update weights independently of code.

Create a volume and upload files:

<CodeGroup>
  ```shell Shell theme={null}
  tg beta jig volumes create --name my-weights --source ./model_weights/
  ```
</CodeGroup>

Then mount it in your `pyproject.toml`:

```toml theme={null}
[[tool.jig.deploy.volume_mounts]]
name = "my-weights"
mount_path = "/models"
```

See the [Jig CLI reference](/reference/cli/jig#volumes) for all volume commands.
