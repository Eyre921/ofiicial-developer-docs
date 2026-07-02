---
title: "firectl batch-inference-job get"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/batch-inference-job-get
path: tools-sdks/firectl/commands/batch-inference-job-get
---

Retrieves information about a batch inference job.

```
firectl batch-inference-job get [flags]
```

### Examples

```
firectl batch-inference-job get my-batch-job
firectl batch-inference-job get accounts/my-account/batchInferenceJobs/my-batch-job
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
