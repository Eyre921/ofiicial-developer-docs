---
title: "firectl dpo-job export-metrics"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-export-metrics
path: tools-sdks/firectl/commands/dpo-job-export-metrics
---

Exports metrics for a dpo job.

```
firectl dpo-job export-metrics [flags]
```

### Examples

```
firectl dpo-job export-metrics my-dpo-job
firectl dpo-job export-metrics accounts/my-account/dpoJobs/my-dpo-job
```

### Flags

```
      --filename string   The file name to export to. (default "metrics.jsonl")
  -h, --help              help for export-metrics
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
