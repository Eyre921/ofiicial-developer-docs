---
title: "firectl model prepare"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-prepare
path: tools-sdks/firectl/commands/model-prepare
---

Prepare models for different precisions

```
firectl model prepare [flags]
```

### Examples

```
firectl model prepare my-model
firectl model prepare accounts/my-account/models/my-model
```

### Flags

```
  -h, --help                    help for prepare
      --wait                    Wait until the model preparation is complete.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
