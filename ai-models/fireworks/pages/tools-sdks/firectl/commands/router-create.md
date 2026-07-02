---
title: "firectl router create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/router-create
path: tools-sdks/firectl/commands/router-create
---

Creates a router.

```
firectl router create [flags]
```

### Examples

```
firectl router create --deployments=my-deployment1,my-deployment2
firectl router create --strategy=even-load --deployments=my-deployment1,my-deployment2
firectl router create --strategy=weighted-random --deployments=my-deployment1,my-deployment2
```

### Flags

```
      --display-name string   The display name of the router.
      --model string          The model to route traffic to.
      --strategy string       The strategy to use for routing traffic. (default "weighted-random")
      --deployments strings   The deployment names to be covered by the router.
      --router-id string      The ID of the router. If not specified, a random ID will be generated.
      --public                Whether the router is public. If not specified, the router is private.
      --dry-run               Print the request proto without running it.
  -o, --output Output         Set the output format to "text", "json", or "flag". (default text)
  -h, --help                  help for create
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
