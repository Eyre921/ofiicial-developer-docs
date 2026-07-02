---
title: "firectl model load-lora"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-load-lora
path: tools-sdks/firectl/commands/model-load-lora
---

Loads a LoRA model.

### Usage

Loads a LoRA model to a dedicated deployment. If successful, a DeployedModel resource will be created.

```
firectl model load-lora [flags]
```

### Examples

```
firectl model load-lora my-lora --deployment my-deployment
```

### Flags

```
      --deployment string       The resource ID of the deployment where the LoRA model is to be loaded.
  -h, --help                    help for load-lora
      --public                  If true, the LoRA model will be publicly available for inference.
      --replace-merged-addon    Required when loading an addon to a hot reload deployment. If there is already an existing addon, it will be replaced.
      --wait                    Wait until the model is deployed.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
