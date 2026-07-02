---
title: "firectl deployment scale"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-scale
path: tools-sdks/firectl/commands/deployment-scale
---

Scales a deployment to a specified number of replicas.

```
firectl deployment scale [flags]
```

### Examples

```
firectl deployment scale my-deployment --replica-count=3
firectl deployment scale accounts/my-account/deployments/my-deployment --replica-count=3
```

### Flags

```
  -h, --help                  help for scale
      --replica-count int32   The desired number of replicas. Must be non-negative.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
