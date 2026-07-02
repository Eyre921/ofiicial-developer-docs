---
title: "firectl model create"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-create
path: tools-sdks/firectl/commands/model-create
---

Creates and uploads a model.

```
firectl model create [flags]
```

### Examples

```
firectl model create my-model /path/to/checkpoint/
firectl model create my-model s3://bucket/path --role-arn arn:aws:iam::123456789012:role/MyRole
firectl model create my-model https://storage-account.blob.core.windows.net/container/path --azure-sas-token-secret accounts/{account}/secrets/{secret}
firectl model create my-model https://storage-account.blob.core.windows.net/container/path --azure-client-id <client-id> --azure-tenant-id <tenant-id>
```

### Flags

```
      --base-model string                 If specified, then the model will be considered a PEFT addon with the given base model.
      --default-draft-model string        The default speculative draft model to use when creating a deployment.
      --default-draft-token-count int32   The default speculative draft token count when creating a deployment.
      --description string                The description of the model.
      --display-name string               The display name of the model.
      --dry-run                           Print the request proto without running it.
      --embedding                         If true, sets the model kind to an embeddings base model.
      --enable-resumable-upload           If true, uses resumable upload for the model.
      --github-url string                 The GitHub URL of the model.
  -h, --help                              help for create
      --hugging-face-url string           The Hugging Face URL of the model.
  -o, --output Output                     Set the output format to "text", "json", or "flag". (default text)
      --poll-duration duration            The duration to poll for model import operation completion. Default is 2 hours. (default 2h0m0s)
      --public                            Whether the model is publicly accessible.
      --quiet                             If true, does not print the upload progress bar.
      --supports-image-input              Whether the model supports image inputs.
      --supports-tools                    Whether the model supports function calling.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
