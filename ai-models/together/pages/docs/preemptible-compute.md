---
title: "Preemptible compute"
source: https://docs.together.ai/docs/preemptible-compute
path: docs/preemptible-compute
---

Run interruptible workloads on discounted preemptible GPU nodes in your cluster.

<Note>
  Preemptible compute is in public preview for Kubernetes clusters (Slurm clusters are not supported yet). There is no minimum-lifetime guarantee for preemptible nodes during preview, so design workloads that can survive losing nodes at any time.
</Note>

Together GPU clusters offer two compute types:

* **Standard** nodes (the default) are provisioned up front (synchronously) when you create or scale a cluster, and are never preempted.
* **Preemptible** nodes fill in over time (asynchronously). You set a target, and Together provisions toward it as spare capacity becomes available. The target is not guaranteed, and preemptible nodes can be preempted at any time.

Preemptible nodes are discounted relative to on-demand at a flat rate (not a bid), and usage is metered and billed sub-hourly (every one to two minutes).

See the [GPU clusters overview](/docs/gpu-clusters-overview#preemptible-compute-preview) for how compute types fit into the rest of the platform.

There is no separate preemptible cluster type—you add preemptible capacity to a cluster, at create time or later. Each cluster has a standard node count and a preemptible node count, and preemptible nodes join the same Kubernetes cluster. Every cluster requires at least one standard node (`num_gpus`), and you cannot convert a node between standard and preemptible in place.

Preemptible nodes carry the label `together.ai/compute-class=preemptible`. Node names encode the compute type: `gpu-dp` is standard, `gpu-preemptible-dp` is preemptible.

## How preemption works

When Together reclaims a preemptible node, the node receives a drain window of at most five minutes:

1. **T+0:** The node is cordoned, a `TogetherPreemptionNotified` Kubernetes event (`type: Warning`) is emitted on the node, and pods on the node receive SIGTERM.
2. Pods that set `terminationGracePeriodSeconds` (capped at 300 seconds) get up to the full window to checkpoint and exit. The node is reclaimed as soon as your pods exit, so checkpoint and exit promptly instead of sleeping through the window.
3. **T+5:00:** The node is removed, regardless of pod status. Five minutes is a hard maximum, not a guarantee that pods finish.

After it's reclaimed, Together automatically provisions replacement preemptible nodes toward your target as capacity becomes available, so you don't need to re-request capacity.

## Request preemptible capacity

Request a preemptible GPU target alongside the standard count, at cluster create or update, from the console, CLI, or API. See the [cluster create API reference](/reference/clusters-create) for the full schema.

| Field                        | Request or response         | Meaning                                                                                                                                                |
| ---------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `num_preemptible_gpus`       | Request (create and update) | Preemptible GPU target. Must be a multiple of 8. `project_id` is required when the target is greater than 0. Omit on update to keep the current value. |
| `desired_preemptible_gpus`   | Response (read-only)        | Echo of the target.                                                                                                                                    |
| `allocated_preemptible_gpus` | Response (read-only)        | Preemptible GPUs actually live. Rises from 0 toward the target as nodes are provisioned, and can sit below the target when capacity is tight.          |

Create a cluster with preemptible capacity. Preemptible capacity requires a project, so pass the global `--project` flag (or set `TOGETHER_PROJECT_ID`):

```bash theme={null}
tg beta clusters create \
  --name my-cluster \
  --region us-central-2 \
  --gpu-type RTX_6000_PCI \
  --cluster-type KUBERNETES \
  --num-gpus 8 \
  --billing-type ON_DEMAND \
  --nvidia-driver-version 570 \
  --cuda-version 12.8 \
  --num-preemptible-gpus 8 \
  --project <PROJECT_ID> \
  --non-interactive --json
```

Scale the preemptible target on an existing cluster:

```bash theme={null}
tg beta clusters update <CLUSTER_ID> --num-preemptible-gpus 16
```

Check the target against what is actually allocated:

```bash theme={null}
tg beta clusters retrieve <CLUSTER_ID> --json \
  | jq '{status, desired_preemptible_gpus, allocated_preemptible_gpus}'
```

## Schedule workloads onto preemptible nodes

Target preemptible nodes explicitly for interruptible workers, and keep coordinators and serving replicas on standard nodes.

```yaml theme={null}
# Interruptible worker: runs on preemptible nodes
nodeSelector:
  together.ai/compute-class: preemptible
```

Pin stateful anchors to standard nodes by excluding the preemptible label:

```yaml theme={null}
# Coordinator: never scheduled on preemptible nodes
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: together.ai/compute-class
              operator: NotIn
              values:
                - preemptible
```

## Detect preemption

Preemption surfaces through three channels:

1. **In-pod (recommended):** A SIGTERM handler or `preStop` hook reacts automatically, with no polling. See [Handle preemption](#handle-preemption) for examples.

2. **Kubernetes events:** Watch for `TogetherPreemptionNotified` events:

   ```bash theme={null}
   kubectl get events -A --field-selector reason=TogetherPreemptionNotified --watch
   ```

3. **Together API (no kubeconfig needed):** Reading a cluster returns a `node_lifecycle_events` array (72-hour retention, deduplicated by node and reason). Filter for `reason == "TogetherPreemptionNotified"`. Related reasons include `TogetherNodeAdded` and `TogetherScaledDown`.

   ```bash theme={null}
   curl -s -H "Authorization: Bearer $TOGETHER_API_KEY" \
     "https://api.together.ai/v1/compute/clusters/<CLUSTER_ID>" \
     | jq '.node_lifecycle_events[] | select(.reason == "TogetherPreemptionNotified")'
   ```

Preemption events also appear in the console under the cluster's Event Timeline.

## Handle preemption

**Pod-level: checkpoint on SIGTERM.** This pattern is per-workload and requires no extra infrastructure. Claim the full grace window with `terminationGracePeriodSeconds` and checkpoint when the signal arrives:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: training-worker
spec:
  terminationGracePeriodSeconds: 300 # claim the full 5-minute window
  nodeSelector:
    together.ai/compute-class: preemptible
  containers:
    - name: worker
      image: my-training-image
      command: ["/bin/sh", "-c"]
      args:
        - |
          trap 'echo "preempted: checkpointing"; ./checkpoint.sh; exit 0' TERM
          exec_training &
          wait
      lifecycle:
        preStop: # fires before SIGTERM reaches the container
          exec:
            command: ["/bin/sh", "-c", "./checkpoint.sh"]
```

<Note>
  The `preStop` hook runs first, then SIGTERM, and both count against the same grace period. Use one or the other as the checkpoint trigger, not both doing duplicate work. The `preStop` variant matters for containers whose main process can't trap signals, or where PID 1 swallows them.
</Note>

**Cluster-level: An operator watching preemption events.** For a coordinated, cluster-wide response (multi-node training, custom schedulers), run a controller that watches for `TogetherPreemptionNotified` events and reacts, for example by draining a job queue, triggering a coordinated checkpoint, or removing the node from a Ray or torchrun worker pool:

```python theme={null}
from kubernetes import client, config, watch

config.load_incluster_config()  # or load_kube_config() outside the cluster
v1 = client.CoreV1Api()
w = watch.Watch()

for event in w.stream(
    v1.list_event_for_all_namespaces,
    field_selector="reason=TogetherPreemptionNotified",
):
    node = event["object"].involved_object.name
    print(f"Node {node} preempted; drain window open (~5 min)")
    # React here, e.g.:
    #  - signal the training coordinator to checkpoint and rebalance
    #  - remove the node from your scheduler / worker pool
    #  - requeue pending work off the doomed node
```

## When to use preemptible

Use preemptible compute for:

* Checkpointed training, fine-tuning, evals, distillation, batch inference, and hyperparameter sweeps. Ray Train and PyTorch Lightning restart from checkpoints out of the box.
* Bursty research: raise the target for a sweep and drop it after. The cluster stays up.

Don't use preemptible compute for:

* The only copy of a multi-day run with no checkpoints.
* User-facing serving replicas with no fallback capacity.
* Workloads with strict SLOs.

As a sizing reference, a checkpoint of a roughly 10B-parameter model completes in about 90 seconds, leaving comfortable headroom within the five-minute window. Checkpoint often, and treat preemptible nodes as ephemeral.
