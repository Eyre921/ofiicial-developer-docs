---
title: "firectl deployment-shape-version get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-shape-version-get
path: tools-sdks/firectl/commands/deployment-shape-version-get
---

Prints information about a deployment shape version.

```
firectl deployment-shape-version get [flags]
```

### Examples

```
firectl deployment-shape-version get accounts/my-account/deploymentShapes/my-deployment-shape/versions/my-version
firectl deployment-shape-version get accounts/my-account/deploymentShapes/my-deployment-shape/versions/latest
```

### Flags

```
      --dry-run         Print the request proto without running it.
  -h, --help            help for get
  -o, --output Output   Set the output format to "text", "json", or "flag". (default text)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
