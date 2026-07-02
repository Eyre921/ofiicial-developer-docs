---
title: "firectl supervised-fine-tuning-job get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/supervised-fine-tuning-job-get
path: tools-sdks/firectl/commands/supervised-fine-tuning-job-get
---

Retrieves information about a supervised fine-tuning job.

```
firectl supervised-fine-tuning-job get [flags]
```

### Examples

```
firectl supervised-fine-tuning-job get my-sft-job
firectl supervised-fine-tuning-job get accounts/my-account/supervisedFineTuningJobs/my-sft-job
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
