---
title: "firectl training-shape clone"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-clone
path: tools-sdks/firectl/commands/training-shape-clone
---

Clones an existing training shape to a new shape.

### Usage

Fetches the source training shape and creates a new training shape with the same configuration. Override flags can be used to change specific fields.

```
firectl training-shape clone <source-training-shape-id> [flags]
```

### Examples

```
firectl training-shape clone my-source-shape --training-shape-id my-new-shape
firectl training-shape clone my-source-shape --training-shape-id my-new-shape --trainer-image-tag 0.24.11
firectl training-shape clone accounts/my-account/trainingShapes/my-source-shape --training-shape-id my-new-shape --accelerator-count 16
```

### Flags

```
      --accelerator-count int32           Number of accelerators (overrides source)
      --accelerator-type string           Accelerator type (overrides source)
      --cp int32                          Context-parallel degree (overrides source)
      --deployment-shape-version string   Deployment shape version (overrides source)
      --description string                Description (overrides source)
      --display-name string               Human-readable display name (overrides source)
      --ep int32                          Expert-parallel degree (overrides source)
  -h, --help                              help for clone
      --max-context-length int32          Max supported context length (overrides source)
      --node-count int32                  Node count (overrides source)
      --pp int32                          Pipeline-parallel degree (overrides source)
      --sequence-parallel                 Enable sequence parallelism (overrides source)
      --tp int32                          Tensor-parallel degree (overrides source)
      --trainer-image-tag string          Trainer image tag (overrides source)
      --trainer-mode string               Trainer mode (overrides source)
      --training-shape-id string          ID for the new training shape (required)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
