---
title: "firectl deployment update"
source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-update
path: tools-sdks/firectl/commands/deployment-update
---

Update a deployment.

```
firectl deployment update [flags]
```

### Examples

```
firectl deployment update my-deployment
firectl deployment update accounts/my-account/deployments/my-deployment
firectl deployment update my-deployment --file=/path/to/deployment.json
```

### Flags

```
      --accelerator-count int32                  The number of accelerators to use per replica.
      --accelerator-type string                  The type of accelerator to use. Must be one of {NVIDIA_A100_80GB, NVIDIA_H100_80GB, NVIDIA_H200_141GB, AMD_MI300X_192GB}
      --deployment-shape string                  The deployment shape to use for this deployment.
      --description string                       Description of the deployment.
      --direct-route-api-keys stringArray        The API keys for the direct route. Only available to enterprise accounts.
      --direct-route-type string                 If set, this deployment will expose an endpoint that bypasses our API gateway. Must be one of {INTERNET, GCP_PRIVATE_SERVICE_CONNECT, AWS_PRIVATELINK}. Only available to enterprise accounts.
      --display-name string                      Human-readable name of the deployment. Must be fewer than 64 characters long.
      --draft-model string                       The draft model to use for speculative decoding. If the model is under your account, you can specify the model ID. If the model is under another account, you can specify the full resource name (e.g. accounts/other-account/models/falcon-7b).
      --draft-token-count int32                  The number of tokens to generate per step for speculative decoding.
      --dry-run                                  Print the request proto without running it.
      --enable-addons                            If true, enable addons for this deployment.
      --enable-session-affinity                  If true, does sticky routing based on the 'user' field. Only available to enterprise accounts.
  -h, --help                                     help for update
      --load-targets Map                         Map of autoscaling load metric names to their target utilization factors.
      --long-prompt                              Whether this deployment is optimized for long prompts.
      --max-context-length int32                 The maximum context length supported by the model (context window). If set to 0 or not specified, the model's default maximum context length will be used.
      --max-replica-count int32                  Maximum number of replicas for the deployment. If min-replica-count > 0 defaults to 0, otherwise defaults to 1.
      --max-with-revocable-replica-count int32   Maximum number of replicas including revocable replicas. Any replicas in excess of max_replica_count are revocable.
      --min-replica-count int32                  Minimum number of replicas for the deployment. If min-replica-count < max-replica-count the deployment will automatically scale between the two replica counts based on load.
      --ngram-speculation-length int32           The length of previous input sequence to be considered for N-gram speculation.
  -o, --output Output                            Set the output format to "text", "json", or "flag". (default text)
      --precision string                         The precision with which the model is served. If specified, must be one of {FP8, FP16, FP4, BF16}.
      --region string                            Placement: 'global', region group (us), or specific region (us-iowa-1).
      --scale-down-window duration               The duration the autoscaler will wait before scaling down a deployment after observing decreased load. Default is 10m.
      --scale-to-zero-window duration            The duration after which there are no requests that the deployment will be scaled down to zero replicas, if min-replica-count is 0. Default 1h.
      --scale-up-window duration                 The duration the autoscaler will wait before scaling up a deployment after observing increased load. Default is 30s.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
