---
title: "firectl training-shape create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-create
path: tools-sdks/firectl/commands/training-shape-create
---

Creates a new training shape.

```
firectl training-shape create [flags]
```

### Examples

```
firectl training-shape create --base-model llama-v2-7b --deployment-shape-version accounts/fireworks/deploymentShapes/rft-qwen3-4b/versions/ra6uiv8w --trainer-image-tag 0.24.10
firectl training-shape create --base-model accounts/fireworks/models/llama-v2-7b --deployment-shape-version accounts/fireworks/deploymentShapes/my-shape/versions/v1 --trainer-image-tag 0.24.10 --accelerator-count 8 --max-context-length 4096 --node-count 1
firectl training-shape create --base-model qwen3-30b-a3b-instruct --deployment-shape-version accounts/fireworks/deploymentShapes/rft-qwen3-30b/versions/v1 --trainer-image-tag 0.32.9 --trainer-mode forward_only --tp 2 --pp 1 --accelerator-type NVIDIA_H200_141GB
```

### Flags

```
      --accelerator-count int32           Number of accelerators
      --accelerator-type string           Accelerator type (e.g. NVIDIA_H200_141GB, NVIDIA_H100_80GB, NVIDIA_A100_80GB)
      --base-model string                 Base model name or ID (required)
      --cp int32                          Context-parallel degree (default server-side 1)
      --deployment-shape-version string   Validated deployment shape version resource name (required)
      --description string                Description of the training shape
      --display-name string               Human-readable display name
      --dry-run                           Print the request proto without running it.
      --ep int32                          Expert-parallel degree (default server-side 1)
  -h, --help                              help for create
      --max-context-length int32          Max supported context length
      --node-count int32                  Node count for multi-node training (default 1)
  -o, --output Output                     Set the output format to "text", "json", or "flag". (default text)
      --pp int32                          Pipeline-parallel degree (default server-side 1)
      --sequence-parallel                 Enable sequence parallelism
      --tp int32                          Tensor-parallel degree (default server-side 1)
      --trainer-image-tag string          Validated trainer runtime image tag (required)
      --trainer-mode string               Trainer mode: policy_trainer, forward_only, or lora_trainer
      --training-shape-id string          Training shape ID (optional, auto-generated if not set)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
