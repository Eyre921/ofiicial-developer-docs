---
title: "Queue GPU jobs with Kueue"
source: https://docs.together.ai/docs/kueue-on-gpu-clusters
path: docs/kueue-on-gpu-clusters
---

Install Kueue and gate GPU jobs on quota so a shared cluster admits work as capacity frees up.

<Tip>Using a coding agent? Load the [together-kueue](https://github.com/togethercomputer/skills/tree/main/skills/together-kueue) skill to teach your agent to write correct Kueue and GPU cluster code for Together AI. [Learn more](/docs/agent-skills).</Tip>

<Note>
  Running third-party schedulers on Together GPU clusters is in beta. The steps and pinned version here (Kueue v0.18.3) are validated on current clusters, but the workflow and defaults may change. Report issues to [support@together.ai](mailto:support@together.ai).
</Note>

[Kueue](https://kueue.sigs.k8s.io/) is a Kubernetes-native job queueing controller. Instead of letting every job compete for GPUs the moment it is created, Kueue holds jobs in a queue and admits them only when their quota is available, suspending the rest. This is how you share a fixed GPU pool across teams without overcommitting it. This guide installs Kueue on a Together GPU cluster and gates jobs on GPU quota.

For the concepts behind each object below, see the [Kueue documentation](https://kueue.sigs.k8s.io/docs/concepts/).

## Requirements

* A Together [Kubernetes GPU cluster](/docs/gpu-clusters-quickstart) in the **Ready** state.
* `kubectl` configured against the cluster. Download credentials with `tg beta clusters get-credentials <cluster_id> --set-default-context`.
* Cluster-admin access. The kubeconfig from the Together CLI grants it.

## Install Kueue

Apply the versioned release manifest. Use `--server-side` because the bundled custom resource definitions are large. For other install methods and configuration options, see the [Kueue installation guide](https://kueue.sigs.k8s.io/docs/installation/):

```bash theme={null}
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.18.3/manifests.yaml
```

Wait for the controller to become available:

```bash theme={null}
kubectl -n kueue-system wait --for=condition=Available deployment/kueue-controller-manager --timeout=240s
kubectl -n kueue-system get pods
```

```
NAME                                        READY   STATUS    RESTARTS   AGE
kueue-controller-manager-6c8685b746-tlc47   1/1     Running   0          20s
```

<Tip>
  Prefer Helm? Install the chart from the registry: `helm install kueue oci://registry.k8s.io/kueue/charts/kueue --version 0.18.3 --namespace kueue-system --create-namespace`.
</Tip>

## Define quotas

Kueue admits jobs against quota described by three resources:

* **[ResourceFlavor](https://kueue.sigs.k8s.io/docs/concepts/resource_flavor/):** a class of nodes. One flavor is enough when your GPU nodes are homogeneous.
* **[ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/):** the cluster-wide quota pool. It must cover every resource your jobs request, including CPU and memory, or matching jobs are never admitted.
* **[LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/):** a namespaced pointer to a ClusterQueue that users submit jobs to.

Create all three, budgeting eight GPUs:

```yaml kueue-quota.yaml theme={null}
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor               # a class of nodes; one is enough for homogeneous GPUs
metadata:
  name: gpu-flavor
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue                 # the cluster-wide quota pool
metadata:
  name: gpu-cluster-queue
spec:
  namespaceSelector: {}            # {} accepts jobs from every namespace
  resourceGroups:
    - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]  # every resource jobs request must be listed here
      flavors:
        - name: gpu-flavor         # must match the ResourceFlavor name above
          resources:
            - name: "cpu"
              nominalQuota: 64
            - name: "memory"
              nominalQuota: 512Gi
            - name: "nvidia.com/gpu"
              nominalQuota: 8       # admit at most 8 GPUs worth of jobs at once
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue                   # namespaced entry point users submit jobs to
metadata:
  namespace: default
  name: gpu-queue
spec:
  clusterQueue: gpu-cluster-queue  # points at the ClusterQueue above
```

```bash theme={null}
kubectl apply -f kueue-quota.yaml
```

`nominalQuota` is the amount of each resource the ClusterQueue can admit at once. Set the GPU quota to the number of GPUs you want this queue to control.

## Attach shared storage

Together provisions a static [PersistentVolume](/docs/gpu-clusters-management#kubernetes-usage) named after your cluster's shared volume. Bind a PersistentVolumeClaim to it so queued jobs read and write the same dataset and checkpoints:

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

Storage is not a quota resource, so it does not affect admission. The next section mounts this claim into the job.

## Submit a job to a queue

Point a standard `batch/v1` Job at the LocalQueue with the `kueue.x-k8s.io/queue-name` label and set `suspend: true`. Kueue takes over the suspend flag and flips it to `false` when it admits the job. For other supported workload types (JobSet, RayJob, MPIJob, and more), see [running jobs with Kueue](https://kueue.sigs.k8s.io/docs/tasks/run/jobs/):

```yaml gpu-job.yaml theme={null}
apiVersion: batch/v1
kind: Job
metadata:
  name: gpu-job-a
  namespace: default
  labels:
    kueue.x-k8s.io/queue-name: gpu-queue   # send this job to the "gpu-queue" LocalQueue
spec:
  parallelism: 1
  completions: 1
  suspend: true                            # start suspended; Kueue unsuspends it on admission
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: worker
          image: nvidia/cuda:12.4.0-base-ubuntu22.04
          command: ["bash", "-c", "nvidia-smi -L; sleep 180"]
          resources:
            requests:
              cpu: "2"                       # counted against the ClusterQueue cpu quota
              memory: "8Gi"                  # counted against the memory quota
            limits:
              nvidia.com/gpu: 6              # counted against the nvidia.com/gpu quota
          volumeMounts:
            - name: shared
              mountPath: /mnt/shared         # shared volume mounted into the job
      volumes:
        - name: shared
          persistentVolumeClaim:
            claimName: shared-pvc            # the PVC bound above
```

```bash theme={null}
kubectl apply -f gpu-job.yaml
```

Kueue creates a [`Workload`](https://kueue.sigs.k8s.io/docs/concepts/workload/) object for the job and admits it because six GPUs fit within the eight-GPU quota. The job's `suspend` flag flips to `false` and its pod starts:

```bash theme={null}
kubectl get workloads
```

```
NAME                  QUEUE       ADMITTED
job-gpu-job-a-272f3   gpu-queue   True
```

## Watch quota gate a second job

Submit a second job that also requests six GPUs. Together the two jobs need 12 GPUs, past the eight-GPU quota. Copy `gpu-job.yaml` to a new name (`gpu-job-b`) and apply it, then compare the two:

```bash theme={null}
kubectl get jobs -o custom-columns='NAME:.metadata.name,SUSPEND:.spec.suspend,ACTIVE:.status.active'
```

```
NAME        SUSPEND   ACTIVE
gpu-job-a   false     1
gpu-job-b   true      <none>
```

The first job runs; the second stays suspended. Its Workload reports exactly why:

```bash theme={null}
WORKLOAD=$(kubectl get workloads -o name | grep gpu-job-b)
kubectl get "$WORKLOAD" -o jsonpath='{.status.conditions[?(@.type=="QuotaReserved")].message}'
# couldn't assign flavors to pod set main: insufficient unused quota for nvidia.com/gpu in flavor gpu-flavor, 4 more needed
```

When the first job finishes or you delete it, Kueue re-admits the queued job automatically and its pod starts, no resubmission needed:

```bash theme={null}
kubectl delete job gpu-job-a
kubectl get job gpu-job-b -o jsonpath='{.spec.suspend}{"\n"}'
# false
```

## Troubleshooting

* **A job never leaves `suspend: true`:** its combined request exceeds the ClusterQueue quota, or the ClusterQueue does not cover one of its resources. Check the Workload's `QuotaReserved` condition message.
* **The job runs immediately without queueing:** the `kueue.x-k8s.io/queue-name` label is missing or names a LocalQueue that does not exist in the job's namespace.
* **The ClusterQueue shows no active quota:** its ResourceFlavor is missing or misnamed. The `flavors[].name` must match a ResourceFlavor.
* **A job requesting only GPUs is never admitted:** the ClusterQueue must also cover the CPU and memory the pods request. Add them to `coveredResources`.

## Next steps

<CardGroup>
  <Card title="Gang-schedule GPU jobs with Volcano" icon="layout-grid" href="/docs/volcano-on-gpu-clusters">
    Run distributed training with all-or-nothing gang scheduling.
  </Card>

  <Card title="Manage GPU clusters" icon="server" href="/docs/gpu-clusters-management">
    Deploy workloads, attach storage, and access the Kubernetes dashboard.
  </Card>
</CardGroup>
