---
title: "Jig CLI reference"
source: https://docs.together.ai/reference/cli/jig
path: reference/cli/jig
---

CLI commands, pyproject.toml configuration, environment variables, and Python SDK for dedicated containers.

<Info>
  Jig is a beta feature. The CLI surface, configuration schema, and supported hardware can change. Reach out to your Together AI contact or [contact sales](https://www.together.ai/contact-sales) with feedback.
</Info>

Jig is the CLI for building, pushing, and deploying [dedicated containers](/docs/dedicated-container-inference). For an end-to-end walkthrough, see the [Jig CLI guide](/docs/deployments-jig).

Jig is included with the Together AI [Python library](https://github.com/togethercomputer/together-python):

<CodeGroup>
  ```bash pip theme={null}
  pip install together
  ```

  ```bash uv theme={null}
  uv add together
  ```
</CodeGroup>

## Environment variables

| Variable           | Default                   | Description                               |
| ------------------ | ------------------------- | ----------------------------------------- |
| `TOGETHER_API_KEY` | Required                  | Your Together API key.                    |
| `TOGETHER_DEBUG`   | `""`                      | Enable debug logging (`"1"` or `"true"`). |
| `WARMUP_ENV_NAME`  | `TORCHINDUCTOR_CACHE_DIR` | Environment variable for cache location.  |
| `WARMUP_DEST`      | `torch_cache`             | Cache directory path in container.        |

All commands are subcommands of `tg beta jig`. Use `--config <path>` to specify a custom config file (default: `pyproject.toml`).

## Build

### `jig init`

Create a starter `pyproject.toml` with sensible defaults.

```bash theme={null}
tg beta jig init
```

### `jig dockerfile`

Generate a Dockerfile from your `pyproject.toml` configuration. Useful for debugging the build.

```bash theme={null}
tg beta jig dockerfile
```

### `jig build`

Build the Docker image locally.

```bash theme={null}
tg beta jig build [flags]
```

| Flag          | Description                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| `--tag <tag>` | Image tag. Default: content hash.                                                                                |
| `--warmup`    | Pre-generate compile caches after build. Requires a GPU. See [Cache warmup](/docs/deployments-jig#cache-warmup). |

### `jig push`

Push the built image to Together's registry at `registry.together.xyz`.

```bash theme={null}
tg beta jig push [flags]
```

| Flag          | Description        |
| ------------- | ------------------ |
| `--tag <tag>` | Image tag to push. |

## Deployments

### `jig deploy`

Build, push, and create or update the deployment. Combines `build`, `push`, and deployment creation into one step.

```bash theme={null}
tg beta jig deploy [flags]
```

| Flag            | Description                                     |
| --------------- | ----------------------------------------------- |
| `--tag <tag>`   | Image tag.                                      |
| `--warmup`      | Pre-generate compile caches. Requires a GPU.    |
| `--build-only`  | Build and push only. Skips deployment creation. |
| `--image <ref>` | Deploy an existing image. Skips build and push. |

### `jig status`

Show deployment status and configuration.

```bash theme={null}
tg beta jig status
```

### `jig list`

List all deployments in your organization.

```bash theme={null}
tg beta jig list
```

### `jig logs`

Retrieve deployment logs.

```bash theme={null}
tg beta jig logs [flags]
```

| Flag       | Description               |
| ---------- | ------------------------- |
| `--follow` | Stream logs in real time. |

### `jig destroy`

Delete the deployment.

```bash theme={null}
tg beta jig destroy
```

### `jig endpoint`

Print the deployment's endpoint URL.

```bash theme={null}
tg beta jig endpoint
```

## Queue

### `jig submit`

Submit a job to the deployment's queue.

```bash theme={null}
tg beta jig submit [flags]
```

| Flag               | Description                                        |
| ------------------ | -------------------------------------------------- |
| `--prompt <text>`  | Shorthand for `--payload '{"prompt": "..."}'`.     |
| `--payload <json>` | Full JSON payload.                                 |
| `--watch`          | Wait for the job to complete and print the result. |

### `jig job-status`

Get the status of a submitted job.

```bash theme={null}
tg beta jig job-status --request-id <id>
```

| Flag                | Description                        |
| ------------------- | ---------------------------------- |
| `--request-id <id>` | The job's request ID. **required** |

### `jig queue-status`

Show queue backlog and worker status.

```bash theme={null}
tg beta jig queue-status
```

## Secrets

Secrets are encrypted environment variables injected at runtime. Manage them with the `secrets` subcommand.

<Warning>
  A name cannot appear in both `[tool.jig.deploy.environment_variables]` and a secret. `jig deploy` fails and lists each colliding name if the same name is defined in both places. Remove the duplicate from your config or run `tg beta jig secrets unset --name <name>`.
</Warning>

### `jig secrets set`

```bash theme={null}
tg beta jig secrets set --name <name> --value <value> [flags]
```

| Flag                   | Description                 |
| ---------------------- | --------------------------- |
| `--name <name>`        | Secret name. **required**   |
| `--value <value>`      | Secret value. **required**  |
| `--description <text>` | Human-readable description. |

### `jig secrets list`

List all secrets for the deployment.

```bash theme={null}
tg beta jig secrets list
```

### `jig secrets unset`

Remove a secret from the local state without touching the deployment.

```bash theme={null}
tg beta jig secrets unset --name <name>
```

### `jig secrets delete`

Delete a secret from the deployment and unset it locally.

```bash theme={null}
tg beta jig secrets delete --name <name>
```

## Volumes

Volumes mount read-only data, such as model weights, into your container without baking them into the image.

### `jig volumes create`

Create a volume and upload files.

```bash theme={null}
tg beta jig volumes create --name <name> --source <path>
```

| Flag              | Description                             |
| ----------------- | --------------------------------------- |
| `--name <name>`   | Volume name. **required**               |
| `--source <path>` | Local directory to upload. **required** |

### `jig volumes update`

Update a volume with new files.

```bash theme={null}
tg beta jig volumes update --name <name> --source <path>
```

Updating a volume bumps its version by 1. To mount the new version, specify the version explicitly in your `pyproject.toml`:

```toml theme={null}
[[tool.jig.deploy.volume_mounts]]
name = "my-weights"
mount_path = "/models"
version = 2
```

If `version` is not specified, the initial version (version 0) of the volume is mounted. You can view current and historical volume versions using the `jig volumes describe` command.

### `jig volumes describe`

Show volume details and contents.

```bash theme={null}
tg beta jig volumes describe --name <name>
```

### `jig volumes list`

List all volumes.

```bash theme={null}
tg beta jig volumes list
```

### `jig volumes delete`

Delete a volume.

```bash theme={null}
tg beta jig volumes delete --name <name>
```

## Configuration reference

Jig reads configuration from your `pyproject.toml` file or a standalone `jig.toml` file. You can also specify a custom config file explicitly:

```bash theme={null}
tg beta jig --config staging_jig.toml deploy
```

This is useful for managing multiple environments (e.g., `staging_jig.toml`, `production_jig.toml`).

The configuration is split into three sections: build settings, deployment settings, and autoscaling.

### The `[tool.jig.image]` section

The `[tool.jig.image]` section controls how your container image is built.

#### `python_version`

Sets the Python version for the container. Jig uses this to select the appropriate base image.

```toml theme={null}
[tool.jig.image]
python_version = "3.11"
```

Default: `"3.11"`

#### `system_packages`

A list of APT packages to install in the container. Useful for libraries that require system dependencies like FFmpeg for video processing or OpenGL for graphics.

```toml theme={null}
[tool.jig.image]
system_packages = ["git", "ffmpeg", "libgl1", "libglib2.0-0"]
```

Default: `[]`

#### `environment`

Environment variables are a part of the image (as `ENV` directives). These are available during the Docker build, the warmup step, and at runtime. Use this for build configuration like CUDA architecture targets.

```toml theme={null}
[tool.jig.image]
environment = { TORCH_CUDA_ARCH_LIST = "8.0 9.0" }
```

For environment variables that should only be set at runtime use `[tool.jig.deploy.environment_variables]` instead. This is useful for values that can change without changing the image.

Default: `{}`

#### `run`

Additional shell commands to run during the Docker build. Each command becomes a separate `RUN` instruction. Use this for custom installation steps that can't be expressed as Python dependencies.

```toml theme={null}
[tool.jig.image]
run = [
    "pip install flash-attn --no-build-isolation",
    "python -c 'import torch; print(torch.__version__)'"
]
```

Default: `[]`

#### `cmd`

The default command to run when the container starts. This becomes the Docker `CMD` instruction.

```toml theme={null}
[tool.jig.image]
cmd = "python app.py --queue"
```

For queue-based workloads using Sprocket, include the `--queue` flag.

Default: `"python app.py"`

#### `copy`

A list of files and directories to copy into the container. Paths are relative to your project root.

```toml theme={null}
[tool.jig.image]
copy = ["app.py", "models/", "config.json"]
```

Default: `[]`

#### `auto_include_git`

When enabled, automatically includes all git-tracked files in the container in addition to files specified in `copy`. Requires a clean git repository (no uncommitted changes).

```toml theme={null}
[tool.jig.image]
auto_include_git = true
```

This is convenient for projects where you want everything in version control to be deployed. You can combine it with `copy` to include additional untracked files.

Default: `false`

### The `[tool.jig.deploy]` section

The `[tool.jig.deploy]` section controls how your container runs on Together's infrastructure.

#### `description`

A human-readable description of your deployment. This appears in the Together dashboard and API responses.

```toml theme={null}
[tool.jig.deploy]
description = "Video generation model v2 with style transfer"
```

Default: `""`

#### `gpu_type`

The type of GPU to allocate for each replica. Together supports NVIDIA H100, NVIDIA B200, or CPU-only deployments.

```toml theme={null}
[tool.jig.deploy]
gpu_type = "h100-80gb"
```

Available options:

* `"h100-80gb"` - NVIDIA H100 with 80GB memory (recommended for large models)
* `"b200-192gb"` - NVIDIA B200 with 192GB memory (next-generation hardware for the largest models)
* `"none"` - CPU-only deployment

Default: `"h100-80gb"`

Other hardware is available on request. [Contact sales](https://www.together.ai/contact-sales) to discuss options.

#### `gpu_count`

The number of GPUs to allocate per replica. For multi-GPU inference with tensor parallelism, set this higher and use `use_torchrun=True` in your Sprocket. See [Multi-GPU / distributed inference](/docs/deployments-sprocket#multi-gpu--distributed-inference).

```toml theme={null}
[tool.jig.deploy]
gpu_type = "h100-80gb"
gpu_count = 4
```

Default: `1`

#### `cpu`

CPU cores to allocate per replica. Supports fractional values for smaller workloads.

```toml theme={null}
[tool.jig.deploy]
cpu = 8
```

Examples:

* `0.1` = 100 millicores, `1` = 1 core, `8` = 8 cores

Default: `1.0`

#### `memory`

Memory to allocate per replica, in gigabytes. Supports fractional values. Set this high enough for your model weights plus inference overhead.

```toml theme={null}
[tool.jig.deploy]
memory = 64
```

Examples:

* `0.5` = 512 MB, `8` = 8 GB, `64` = 64 GB

If you're seeing OOM (out of memory) errors, increase this value.

Default: `8.0`

#### `storage`

Ephemeral storage to allocate per replica, in gigabytes. This is the disk space available to your container at runtime for temporary files, caches, and model artifacts.

```toml theme={null}
[tool.jig.deploy]
storage = 200
```

Default: `100`

#### `min_replicas`

The minimum number of replicas to keep running. Set to `0` to allow scaling to zero when idle (saves costs but adds cold start latency).

```toml theme={null}
[tool.jig.deploy]
min_replicas = 1
```

Default: `1`

#### `max_replicas`

The maximum number of replicas the autoscaler can create. Set this based on your expected peak load and budget.

```toml theme={null}
[tool.jig.deploy]
min_replicas = 1
max_replicas = 20
```

Default: `1`

#### `port`

The port your container listens on. Sprocket uses port 8000 by default.

```toml theme={null}
[tool.jig.deploy]
port = 8000
```

Default: `8000`

#### `health_check_path`

The endpoint Together uses to check if your container is ready to accept traffic. The endpoint must return a `200` status when healthy.

```toml theme={null}
[tool.jig.deploy]
health_check_path = "/health"
```

Sprocket provides this endpoint automatically.

Default: `"/health"`

#### `termination_grace_period_seconds`

How long to wait for a worker to finish its current job before forcefully terminating during shutdown or scale-down. Set this higher for long-running inference jobs.

```toml theme={null}
[tool.jig.deploy]
termination_grace_period_seconds = 600
```

Default: `300`

#### `command`

Override the container's startup command at deploy time. This takes precedence over the `cmd` setting in `[tool.jig.image]`.

```toml theme={null}
[tool.jig.deploy]
command = ["python", "app.py", "--queue", "--workers", "2"]
```

Default: `null` (uses the image's CMD)

#### `environment_variables`

Runtime environment variables injected into your container. For sensitive values like API keys, use [secrets](#secrets) instead.

Each name must be unique across `[tool.jig.deploy.environment_variables]` and secrets. `jig deploy` rejects duplicate names.

```toml theme={null}
[tool.jig.deploy.environment_variables]
MODEL_PATH = "/models/weights"
TORCH_COMPILE = "1"
LOG_LEVEL = "INFO"
```

Default: `{}`

### The `[tool.jig.deploy.autoscaling]` section

The `[tool.jig.deploy.autoscaling]` section controls how your deployment scales based on demand. For all supported metrics and scaling behavior, see [Autoscaling](/docs/together-deployments#autoscaling).

#### `metric`

The autoscaling strategy to use. Currently, `QueueBacklogPerWorker` is the recommended metric for queue-based workloads.

```toml theme={null}
[tool.jig.deploy.autoscaling]
metric = "QueueBacklogPerWorker"
```

**QueueBacklogPerWorker** scales based on queue depth relative to worker count. When the queue grows, more replicas are added. When workers are idle, replicas are removed (down to `min_replicas`).

#### `target`

The target ratio for the autoscaler. This controls how aggressively the system scales.

```toml theme={null}
[tool.jig.deploy.autoscaling]
metric = "QueueBacklogPerWorker"
target = 1.05
```

The formula is: `desired_replicas = queue_depth / target`

For example, if there are 100 jobs in the pending or running state, here's what happens with each setting:

* `1.0`: exact match, 100 workers.
* `1.05`: 5% underprovisioning, 95 workers (slightly less than needed, recommended).
* `0.95`: 5% overprovisioning, 105 workers (more than strictly needed, lower latency).

### Full configuration example

<CodeGroup>
  ```toml pyproject.toml theme={null}
  [project]
  name = "video-generator"
  version = "0.1.0"
  requires-python = ">=3.11"
  dependencies = [
      "torch>=2.0",
      "diffusers",
      "sprocket",
  ]

  [project.optional-dependencies]
  dev = ["pytest", "black"]

  [tool.jig.image]
  python_version = "3.11"
  system_packages = ["git", "ffmpeg", "libgl1"]
  environment = { TORCH_CUDA_ARCH_LIST = "8.0 9.0" }
  run = ["pip install flash-attn --no-build-isolation"]
  cmd = "python app.py --queue"
  copy = ["app.py", "models/"]

  [tool.jig.deploy]
  description = "Video generation model"
  gpu_type = "h100-80gb"
  gpu_count = 2
  cpu = 8
  memory = 64
  min_replicas = 1
  max_replicas = 20
  port = 8000
  health_check_path = "/health"

  [[tool.jig.deploy.volume_mounts]]
  name = "my-weights"
  mount_path = "/models"

  [tool.jig.deploy.environment_variables]
  MODEL_PATH = "/models/weights"
  TORCH_COMPILE = "1"

  [tool.jig.deploy.autoscaling]
  metric = "QueueBacklogPerWorker"
  target = 1.05
  ```
</CodeGroup>

## Related

* [Dedicated containers overview](/docs/dedicated-container-inference). Platform overview and when to use dedicated containers.
* [Jig CLI guide](/docs/deployments-jig). End-to-end walkthrough of building and deploying with Jig.
* [Sprocket SDK reference](/reference/dci-reference-sprocket). API reference for the worker SDK Jig deploys.
