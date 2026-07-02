---
title: "firectl training-shape update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-update
path: tools-sdks/firectl/commands/training-shape-update
---

Updates a training shape (mutable fields only). Creates a new version automatically.

```
firectl training-shape update [flags]
```

### Examples

```
firectl training-shape update my-shape --trainer-image-tag 0.24.11
firectl training-shape update my-shape --trainer-mode forward_only --node-count 2 --tp 2 --pp 4
```

### Flags

```
      --accelerator-count int32              Number of accelerators
      --accelerator-type string              Accelerator type (e.g. NVIDIA_H200_141GB, NVIDIA_H100_80GB)
      --base-model-weight-precision string   Base model weight precision (e.g. BFLOAT16, FP8)
      --cp int32                             Context-parallel degree (default server-side 1)
      --deployment-shape-version string      Validated deployment shape version resource name
      --description string                   Description of the training shape
      --display-name string                  Human-readable display name
      --dry-run                              Print the request proto without running it.
      --ep int32                             Expert-parallel degree (default server-side 1)
  -h, --help                                 help for update
      --max-context-length int32             Max supported context length
      --node-count int32                     Node count for multi-node training
  -o, --output Output                        Set the output format to "text", "json", or "flag". (default text)
      --pp int32                             Pipeline-parallel degree (default server-side 1)
      --sequence-parallel                    Enable sequence parallelism
      --tp int32                             Tensor-parallel degree (default server-side 1)
      --trainer-image-tag string             Validated trainer runtime image tag
      --trainer-mode string                  Trainer mode: policy_trainer or forward_only
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
