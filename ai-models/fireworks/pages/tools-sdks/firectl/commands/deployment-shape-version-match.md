---
title: "firectl deployment-shape-version match"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-shape-version-match
path: tools-sdks/firectl/commands/deployment-shape-version-match
---

Prints the deployment shape versions this account can deploy a model on.

### Usage

Prints the validated deployment shape versions compatible with a model, restricted to the shapes the account can actually deploy on.

Unlike 'deployment-shape-version list --base-model', which shows every validated shape matching the model, this returns the deployable set for the account: shapes not usable by the account are dropped, exact base-model matches are preferred over same model-type and parameter-count siblings, and PEFT addons are resolved to their base model.

This runs the same server-side matching the shape picker in 'firectl create deployment' uses, but only on the model. It does not take the rest of a deployment's configuration into account, so it reports the default (non-addon) result: shapes are not filtered down to those advertising MULTI\_LORA, which a deployment created with --enable-addons requires.

A bare model ID is resolved against the account being matched for, so public models must be given as a full name (accounts/fireworks/models/...).

Superusers are exempt from both server-side account scopes, so for them this returns every visible shape and --account has no effect on the result.

```
firectl deployment-shape-version match [flags]
```

### Examples

```
firectl deployment-shape-version match --model accounts/fireworks/models/llama-v3p1-8b-instruct
firectl deployment-shape-version match --model my-lora-addon
firectl deployment-shape-version match --model my-lora-addon --account my-other-account
```

### Flags

```
      --account string   The account to match shapes for, and to resolve a bare --model ID against. Defaults to the signed-in account. Unlike the global --account-id, this does not change which account you authenticate as.
  -h, --help             help for match
      --model string     The model to match deployment shape versions against. A bare model ID is resolved against the account being matched for; give a full model name (accounts/<account-id>/models/<model-id>) for anything else, including public models. Required.
  -o, --output string    Set the output format to "text" or "json". (default "text")
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
