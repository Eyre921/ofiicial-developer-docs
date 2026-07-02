---
title: "firectl model update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-update
path: tools-sdks/firectl/commands/model-update
---

Updates a model.

```
firectl model update [flags]
```

### Examples

```
firectl model update my-model --display-name="New Name"
firectl model update accounts/my-account/models/my-model --display-name="New Name"
```

### Flags

```
      --default-draft-model string        The default speculative draft model to use when creating a deployment.
      --default-draft-token-count int32   The default speculative draft token count when creating a deployment.
      --description string                The description of the model.
      --display-name string               The display name of the model.
      --dry-run                           Print the request proto without running it.
      --github-url string                 The GitHub URL of the model.
  -h, --help                              help for update
      --hugging-face-url string           The Hugging Face URL of the model.
  -o, --output Output                     Set the output format to "text", "json", or "flag". (default text)
      --public                            Whether the model is publicly accessible.
      --supports-image-input              Whether the model supports image inputs.
      --supports-tools                    Whether the model supports function calling.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
