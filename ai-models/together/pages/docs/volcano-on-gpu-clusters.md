---
title: "Gang-schedule GPU jobs with Volcano"
source: https://docs.together.ai/docs/volcano-on-gpu-clusters
path: docs/volcano-on-gpu-clusters
---

Install the Volcano scheduler and run gang-scheduled GPU jobs on a Together Kubernetes cluster.

<Tip>Using a coding agent? Load the [together-volcano](https://github.com/togethercomputer/skills/tree/main/skills/together-volcano) skill to teach your agent to write correct Volcano and GPU cluster code for Together AI. [Learn more](/docs/agent-skills).</Tip>

<Note>
  Running third-party schedulers on Together GPU clusters is in beta. The steps and pinned version here (Volcano v1.15.0) are validated on current clusters, but the workflow and defaults may change. Report issues to [support@together.ai](mailto:support@together.ai).
</Note>

[Volcano](https://volcano.sh/) is a Kubernetes-native batch scheduler for AI, machine learning, and high-performance computing workloads. Its defining feature is [gang scheduling](https://volcano.sh/en/docs/gang_scheduling/): a group of pods is scheduled all-at-once or not at all, so a distributed training job never starts with half its workers running and the rest stuck pending. This guide installs Volcano on a Together GPU cluster and runs a gang-scheduled job across the cluster's GPUs.

For background on every field used here, see the [Volcano documentation](https://volcano.sh/en/docs/).

## Prerequisites

* A Together [Kubernetes GPU cluster](/docs/gpu-clusters-quickstart) in the **Ready** state.
* `kubectl` configured against the cluster. Download credentials with `tg beta clusters get-credentials <cluster_id> --set-default-context`.
* Cluster-admin access. The kubeconfig from the Together CLI grants it.

Confirm you can reach the cluster and see its GPU nodes:

```bash theme={null}
kubectl get nodes -o custom-columns='NODE:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu'
```

GPU nodes report an `nvidia.com/gpu` count. The NVIDIA device plugin that exposes this resource is preinstalled on Together clusters.

## Install Volcano

Install the scheduler, controllers, and custom resource definitions from the versioned release manifest. For other install methods and version compatibility, see the [Volcano installation guide](https://volcano.sh/en/docs/installation/):

```bash theme={null}
kubectl apply -f https://raw.githubusercontent.com/volcano-sh/volcano/v1.15.0/installer/volcano-development.yaml
```

Wait for the control plane to become available:

```bash theme={null}
kubectl -n volcano-system wait --for=condition=Available deployment --all --timeout=180s
kubectl -n volcano-system get pods
```

All pods should be `Running` or `Completed`:

```
NAME                                  READY   STATUS      RESTARTS   AGE
volcano-admission-5f4fcdc56f-6n2j4    1/1     Running     0          3m
volcano-admission-init-bbjdf          0/1     Completed   0          3m
volcano-controllers-f79b44f67-nxbg7   1/1     Running     0          3m
volcano-scheduler-d8b968cbb-kc885     1/1     Running     0          3m
```

Volcano creates a `default` queue automatically:

```bash theme={null}
kubectl get queue
```

<Tip>
  Prefer Helm? Add the chart repo and install into the same namespace: `helm repo add volcano-sh https://volcano-sh.github.io/helm-charts && helm install volcano volcano-sh/volcano -n volcano-system --create-namespace`.
</Tip>

## Create a queue

A [queue](https://volcano.sh/en/docs/queue/) is the unit Volcano uses to divide cluster capacity between teams or workloads. Create one with a GPU capability cap so jobs in it can request up to eight GPUs:

```yaml research-queue.yaml theme={null}
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: research
spec:
  reclaimable: true      # let other queues borrow this queue's idle capacity
  weight: 1              # relative share of contended resources vs. other queues
  capability:           # hard ceiling on what jobs in this queue can use at once
    nvidia.com/gpu: 8
```

```bash theme={null}
kubectl apply -f research-queue.yaml
```

* `weight`: the queue's share of cluster resources relative to other queues when capacity is contended.
* `capability`: the hard upper bound on resources the queue can consume at once.
* `reclaimable`: whether the queue gives resources back to other queues when it is over its fair share.

See the [queue reference](https://volcano.sh/en/docs/queue/) for the full field list, including hierarchical queues and guaranteed resources.

## Attach shared storage

Together provisions a static [PersistentVolume](/docs/gpu-clusters-management#kubernetes-usage) named after your cluster's shared volume. Bind a PersistentVolumeClaim to it so every worker reads and writes the same dataset and checkpoints:

```yaml shared-pvc.yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-pvc
spec:
  accessModes:
    - ReadWriteMany                 # many pods across nodes mount it at the same time
  storageClassName: shared-wekafs   # Together's default shared storage class
  volumeName: <SHARED_VOLUME_NAME>  # the static PV named after your shared volume
  resources:
    requests:
      storage: 100Gi
```

```bash theme={null}
kubectl apply -f shared-pvc.yaml
kubectl get pvc shared-pvc   # STATUS should be Bound
```

The next section mounts this claim into the job.

## Run a gang-scheduled job

A Volcano [`Job`](https://volcano.sh/en/docs/vcjob/) (`vcjob`) wraps a set of tasks and enforces gang scheduling through `minAvailable`. The scheduler admits the job only once it can place at least `minAvailable` pods together. The following job runs four workers, each requesting two GPUs, for eight GPUs total, with the shared volume mounted at `/mnt/shared`:

```yaml gpu-gang-job.yaml theme={null}
apiVersion: batch.volcano.sh/v1alpha1
kind: Job                          # a Volcano Job (vcjob), not a core batch/v1 Job
metadata:
  name: gpu-gang
spec:
  minAvailable: 4                  # gang size: schedule all 4 pods together or none
  schedulerName: volcano           # route pods to Volcano instead of the default scheduler
  queue: research                  # draw resources from the "research" queue
  policies:
    - event: PodEvicted            # if any pod in the gang is evicted...
      action: RestartJob           # ...restart the whole job so workers stay in sync
  tasks:
    - replicas: 4                  # number of worker pods in the gang
      name: worker
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: worker
              image: nvidia/cuda:12.4.0-base-ubuntu22.04
              command: ["bash", "-c", "nvidia-smi -L; sleep 300"]
              resources:
                limits:
                  nvidia.com/gpu: 2  # GPUs per worker; 4 x 2 = 8 GPUs for the gang
              volumeMounts:
                - name: shared
                  mountPath: /mnt/shared   # shared volume visible to every worker
          volumes:
            - name: shared
              persistentVolumeClaim:
                claimName: shared-pvc      # the PVC bound above
```

```bash theme={null}
kubectl apply -f gpu-gang-job.yaml
```

`schedulerName: volcano` routes the pods to Volcano instead of the default Kubernetes scheduler. `minAvailable: 4` means all four workers start together or none do.

Watch the job reach `Running`:

```bash theme={null}
kubectl get vcjob gpu-gang
```

```
NAME       STATUS    MINAVAILABLE   RUNNINGS   AGE
gpu-gang   Running   4              4          30s
```

Volcano tracks the group through a `PodGroup`. Inspect it and the pods:

```bash theme={null}
kubectl get podgroup
kubectl get pods -l volcano.sh/job-name=gpu-gang -o wide
```

Confirm the GPUs are visible inside a worker:

```bash theme={null}
kubectl logs gpu-gang-worker-0
```

```
GPU 0: NVIDIA H100 80GB HBM3 (UUID: GPU-0b416d98-...)
GPU 1: NVIDIA H100 80GB HBM3 (UUID: GPU-149c362a-...)
```

Confirm the shared volume is mounted and writable from every worker. All workers read and write the same `ReadWriteMany` volume, so a file written by one is visible to the others:

```bash theme={null}
kubectl exec gpu-gang-worker-0 -- touch /mnt/shared/hello
kubectl exec gpu-gang-worker-1 -- ls /mnt/shared   # shows hello
```

### Verify all-or-nothing behavior

Gang scheduling matters most when a job cannot fit. Delete the running job, then submit one that requests more GPUs than the cluster has (eight workers at two GPUs each is 16 GPUs, past this cluster's 8):

```bash theme={null}
kubectl delete vcjob gpu-gang
```

Change `minAvailable` to `8` and `replicas` to `8` in the manifest and reapply. The job stays `Pending` and, critically, **no** pods run. The default scheduler would start as many as fit and strand the rest; Volcano keeps the whole group pending:

```bash theme={null}
kubectl get pods -l volcano.sh/job-name=gpu-gang --no-headers | awk '{print $3}' | sort | uniq -c
#    8 Pending

kubectl get events --field-selector involvedObject.name=gpu-gang-worker-0 | tail -1
# Warning  FailedScheduling  ... once resource is released and minAvailable is satisfied
```

The `PodGroup` sits in the `Inqueue` phase until enough resources free up to admit the entire gang.

## Route other workloads to Volcano

Any pod, Deployment, or third-party job type can use Volcano by setting `schedulerName: volcano` in its pod template. This is how you schedule multi-node training launched through the [MPI Operator](https://github.com/kubeflow/mpi-operator), which is preinstalled on Together clusters. For gang guarantees on those workloads, create a `PodGroup` and reference it from the pods; see the [Volcano documentation](https://volcano.sh/en/docs/podgroup/).

## Troubleshooting

* **Pods stay `Pending` and the `PodGroup` is `Inqueue`:** the queue cannot fit `minAvailable` pods at once. Lower `minAvailable`, raise the queue's `capability`, or wait for other jobs to release GPUs.
* **Pods schedule on the default scheduler instead of Volcano:** `schedulerName: volcano` is missing from the pod template. On a `vcjob` it belongs under `spec`.
* **Job rejected on creation:** the Volcano admission webhook may still be starting. Confirm `volcano-admission` is `Running` in the `volcano-system` namespace and reapply.
* **Queue rejects a job:** the job's total request exceeds the queue's `capability`. Raise the cap or split the work.

## Next steps

<CardGroup>
  <Card title="Queue GPU jobs with Kueue" icon="stack-2" href="/docs/kueue-on-gpu-clusters">
    Gate GPU jobs on quota with a Kubernetes-native queueing controller.
  </Card>

  <Card title="Manage GPU clusters" icon="server" href="/docs/gpu-clusters-management">
    Deploy workloads, attach storage, and access the Kubernetes dashboard.
  </Card>
</CardGroup>
