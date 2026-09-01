---
title: "firectl billing export-metrics"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-export-metrics
path: tools-sdks/firectl/commands/billing-export-metrics
---

Exports billing metrics

```
firectl billing export-metrics [flags]
```

### Examples

```
firectl billing export-metrics
```

### Flags

```
      --end-time string     The end time (exclusive).
      --filename string     The file name to export to. (default "billing_metrics.csv")
  -h, --help                help for export-metrics
      --start-time string   The start time (inclusive).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
