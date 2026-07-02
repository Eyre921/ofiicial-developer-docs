---
title: "Cluster management"
source: https://docs.together.ai/docs/gpu-clusters-management
path: docs/gpu-clusters-management
---

Manage, scale, and operate your GPU clusters

## On this page

* [Kubernetes Usage](#kubernetes-usage)
* [GPU Access in Containers](#understanding-gpu-access-in-containers-for-kubernetes-clusters)
* [Kubernetes Dashboard](#kubernetes-dashboard)
* [Direct SSH Access](#direct-ssh-access)
* [Managing Cluster Access](#managing-cluster-access)
* [Cluster Scaling](#cluster-scaling)
* [Monitoring and Status](#monitoring-and-status)
* [Best Practices](#best-practices)

## Kubernetes Usage

Use `kubectl` to interact with Kubernetes clusters for containerized workloads.

### Deploy Pods with Storage

<Note>
  **New to Kubernetes?** A [PersistentVolumeClaim (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) is a request for storage that your pods can use. Think of it like requesting a disk that persists even when pods restart.
</Note>

We provide a static [PersistentVolume (PV)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) with the same name as your shared volume. As long as you use the static PV, your data will persist across pod restarts, cluster operations, and even after cluster deletion.

#### Understanding Storage in Kubernetes

Kubernetes uses a three-step process for storage:

1. **PersistentVolume (PV)** - The actual storage resource (managed by Together AI)
2. **PersistentVolumeClaim (PVC)** - Your request to use that storage (you create this)
3. **Pod with volumeMounts** - Mounts the PVC into your container at a specific path (you create this)

#### Step 1: Create a PersistentVolumeClaim

**Shared Storage PVC (Multi-Pod Access):**

```yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-pvc                    # Name you'll reference in pods
spec:
  accessModes:
    - ReadWriteMany                   # Multiple pods can read/write simultaneously
  resources:
    requests:
      storage: 10Gi                   # Requested size (can be adjusted)
  volumeName: <shared volume name>    # Replace with your shared volume name from cluster UI
```

**Key fields explained:**

* `accessModes: ReadWriteMany` - Allows multiple pods across different nodes to mount this volume simultaneously ([learn more](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes))
* `volumeName` - Must match the exact name of your shared volume shown in the cluster UI
* `storage: 10Gi` - The amount of storage you're requesting

**Local Storage PVC (Single-Node Access):**

```yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc                     # Name you'll reference in pods
spec:
  accessModes:
    - ReadWriteOnce                   # Only one pod/node can mount at a time
  resources:
    requests:
      storage: 50Gi                   # Requested size
  storageClassName: local-storage-class
```

**Key fields explained:**

* `accessModes: ReadWriteOnce` - Only one pod can mount this volume (typically for fast local NVMe storage)
* `storageClassName` - Specifies the type of storage to provision

Save these to files (e.g., `shared-pvc.yaml`, `local-pvc.yaml`) and apply:

```bash theme={null}
kubectl apply -f shared-pvc.yaml -n default # change to your namespace
kubectl apply -f local-pvc.yaml -n default # change to your namespace

# Verify PVCs are bound
kubectl get pvc -A # across all namespaces
```

You should see `STATUS: Bound` for both PVCs.

#### Step 2: Create a Pod with Mounted Volumes

Now create a pod that mounts these volumes:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  restartPolicy: Never
  containers:
    - name: ubuntu
      image: debian:stable-slim
      command: ["/bin/sh", "-c", "sleep infinity"]  # Keeps pod running
      volumeMounts:                                   # Where to mount volumes inside container
        - name: shared-storage                        # References volume defined below
          mountPath: /mnt/shared                      # Path inside container
        - name: local-storage
          mountPath: /mnt/local
  volumes:                                            # Defines volumes from PVCs
    - name: shared-storage                            # Internal name for this volume
      persistentVolumeClaim:
        claimName: shared-pvc                         # Must match PVC name from Step 1
    - name: local-storage
      persistentVolumeClaim:
        claimName: local-pvc
```

**Key fields explained:**

* `volumeMounts.mountPath` - The directory path inside your container where the volume will appear
* `volumes[].name` - An internal identifier that connects the volume definition to the volumeMount
* `persistentVolumeClaim.claimName` - Must exactly match the PVC name you created in Step 1

[Learn more about volumes in pods →](https://kubernetes.io/docs/concepts/storage/volumes/)

#### Step 3: Deploy and Access Your Pod

Save the pod definition to a file (e.g., `pod-with-storage.yaml`) and deploy:

```bash theme={null}
# Deploy the pod
kubectl apply -f pod-with-storage.yaml -n default # should be same as the namespace in which PVC is deployed

# Wait for pod to be running
kubectl get pods -w

# Once STATUS shows "Running", access the pod
kubectl exec -it test-pod -- bash
```

#### Step 4: Verify Mounted Volumes

Once inside the pod, verify your volumes are mounted:

```bash theme={null}
# Check mounted filesystems
df -h | grep /mnt

# List mounted directories
ls -la /mnt/shared
ls -la /mnt/local

# Test write access
echo "Hello from pod" > /mnt/shared/test.txt
cat /mnt/shared/test.txt
```

#### Accessing Volumes from Multiple Pods

Because the shared storage uses `ReadWriteMany`, multiple pods can access it simultaneously:

```bash theme={null}
# Create a second pod using the same shared PVC
kubectl run test-pod-2 --image=debian:stable-slim --command -- sleep infinity

# Exec into the second pod
kubectl exec -it test-pod-2 -- bash

# The file you created from the first pod is visible here
cat /mnt/shared/test.txt
```

#### Understanding GPU Access in Containers for Kubernetes Clusters

Our Kubernetes runtime exposes **all GPU devices to all containers on the host**. However, whether you can use tools like `nvidia-smi` inside your container depends on your container image.

**Two scenarios:**

1. **Container with CUDA drivers (e.g., `nvidia/cuda`, `pytorch/pytorch`):**
   * ✓ GPU devices are accessible
   * ✓ `nvidia-smi` works
   * ✓ CUDA libraries available
   * **Recommended for GPU workloads**

2. **Container without CUDA drivers (e.g., `debian`, `ubuntu` base images):**
   * ✓ GPU devices are still exposed by the runtime
   * ✗ `nvidia-smi` command not found (CUDA drivers not installed in container)
   * ✗ Cannot run GPU workloads without installing CUDA
   * GPU hardware is accessible, but you need CUDA software to use it

<Note>
  **Key Concept:** The container runtime makes GPU devices available, but the container image must include CUDA drivers and tools to interact with them. Think of it like having a GPU plugged in (runtime provides this) but needing drivers installed (image must provide this).
</Note>

**To run GPU workloads or access your data volumes in the Kubernetes Clusters:**

Deploy a pod with GPU and storage access, then exec into it.

First, ensure you have a PVC created ([see PVC creation above](#step-1-create-a-persistentvolumeclaim)), then create a pod with a **CUDA-enabled base image**.

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: gpu-workload-pod
spec:
  restartPolicy: Never
  containers:
    - name: pytorch
      image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime  # CUDA-enabled image
      command: ["/bin/bash", "-c", "sleep infinity"]
      resources:
        limits:
          nvidia.com/gpu: 1  # Request 1 GPU
      volumeMounts:
        - name: shared-storage
          mountPath: /mnt/shared
  volumes:
    - name: shared-storage
      persistentVolumeClaim:
        claimName: shared-pvc  # Must match your PVC name from earlier
```

Deploy and access:

```bash theme={null}
# Deploy the pod
kubectl apply -f gpu-pod.yaml

# Wait for it to be running
kubectl wait --for=condition=Ready pod/gpu-workload-pod

# Exec into the pod
kubectl exec -it gpu-workload-pod -- bash

# Inside the pod, you can now:
nvidia-smi                    # See GPU(s) allocated to this pod
ls /mnt/shared                # Access your mounted volumes
python train.py               # Run your GPU workloads
```

### Kubernetes Dashboard

Access the Kubernetes Dashboard for visual cluster management:

1. From the cluster UI, click the **K8s Dashboard URL**
2. Retrieve your access token:

```bash theme={null}
kubectl -n kubernetes-dashboard get secret \
  $(kubectl -n kubernetes-dashboard get secret | grep admin-user-token | awk '{print $1}') \
  -o jsonpath='{.data.token}' | base64 -d | pbcopy
```

3. Paste the token into the dashboard login

## Direct SSH Access

### Prerequisites

* SSH key must be added to your account at [api.together.ai/settings/ssh-key](https://api.together.ai/settings/ssh-key)

### SSH to GPU Worker Nodes (in Kubernetes) and Slurm Compute Nodes (Slurm)

You can SSH directly into any GPU worker node/ Slurm compute nodes from the cluster UI.

**From the UI:**

1. Navigate to your cluster in the Together Cloud UI
2. Go to the **Worker Nodes** section
3. Find the node you want to access
4. Click the **Copy** icon under the host column next to the node
5. Paste and run the command in your terminal

The copied command includes the full hostname and is ready to use:

```bash theme={null}
ssh 9cvq-68pzlt-99e6e06b-ec17-4198-96c2-6a7a9c2236b2.s1.us-central-4b.cloud.together.ai
```

**Use cases for direct worker node access:**

* Check GPU utilization across all GPUs on the node with `nvidia-smi`
* Monitor node-level performance metrics (CPU, memory, disk, network)
* Inspect system logs (`journalctl`, `/var/log`)
* Debug node-level networking or storage issues
* Check Kubernetes kubelet status and logs
* View all processes running on the node
* In case of Slurm clusters you can directly run GPU workloads on the compute nodes via ssh

<Warning>
  **Important: SSH access matrix (Kubernetes vs Slurm)**

  | Access method            | Kubernetes clusters (SSH to worker node)      | Slurm clusters (SSH to compute node)                         |
  | ------------------------ | --------------------------------------------- | ------------------------------------------------------------ |
  | GPU visibility           | See all GPUs on the node with `nvidia-smi`    | See all GPUs on the node with `nvidia-smi`                   |
  | Run GPU workloads        | ✗ Not available (no direct GPU device access) | ✓ Available (run workloads directly)                         |
  | Access PersistentVolumes | ✗ Not available (mounted in pods only)        | ✓ Available via /home directory                              |
  | Best for                 | Node-level monitoring and debugging           | Node-level monitoring, debugging, and direct Slurm workflows |

  If you need GPU workloads or PersistentVolumes on Kubernetes, exec into a pod with GPU and storage access.
</Warning>

### SSH to Slurm Login Nodes

For HPC workflows, [Slurm clusters](/docs/slurm) provide SSH access to login nodes for job submission.

The cluster UI shows copy-ready Slurm commands tailored to your cluster. Use these to quickly verify connectivity and submit jobs.

**Hostnames:**

* Worker nodes: `<node-name>.slurm.pod` (e.g., `gpu-dp-hmqnh-nwlnj.slurm.pod`)
* Login node: Always `slurm-login` (where you'll start most jobs)

**Common Slurm commands:**

```bash theme={null}
sinfo          # View node and partition status
squeue         # View job queue
srun           # Run interactive jobs
sbatch         # Submit batch jobs
scancel        # Cancel jobs
```

<Warning>
  **Set memory limits explicitly in your `sbatch` scripts.**

  Set `--mem` to a specific value (e.g., `--mem=500G`) rather than `--mem=0`. `--mem=0` tells Slurm to use all memory on the node, which can crash the node under load. We recommend not exceeding 90% of the node's memory to leave headroom for system processes. Adjust lower based on what your job actually needs.

  If a job exceeds its allocation, Slurm fails it with an `OUT_OF_MEMORY` error instead of crashing the node.
</Warning>

#### VS Code Remote SSH Setup

To use VS Code with your Slurm cluster, configure SSH with a proxy jump host in your `~/.ssh/config`:

```ssh-config theme={null}
# Keep connections alive
Host *
  ServerAliveInterval 60

# Together AI jump host (if applicable)
Host together-jump
  HostName <your-jump-host>
  User <your-username>

# Your Slurm login node
Host slurm-cluster
  HostName slurm-login
  ProxyJump together-jump
  User <your-username>
```

Then in VS Code's Remote SSH extension, connect to `slurm-cluster`. The connection will automatically route through the jump host.

## Managing Cluster Access

Cluster access is controlled through Together's [project-based permissions](/docs/projects). Users with access to a project can access all clusters and volumes within it. There are two roles:

* **Admin** -- Can create/delete clusters, modify configurations, manage users, and use clusters
* **Editor** -- Can use clusters (SSH, kubectl, Slurm) but can't create, delete, or modify infrastructure

For the full permission matrix, see [Roles & Permissions](/docs/roles-permissions).

### Adding Users to a Cluster Project

For step-by-step instructions on adding and removing project members, see [Managing Project Members](/docs/projects#managing-project-members).

<Info>
  **Quick version:** Go to **Settings > Collaborators**, find the project that contains your cluster, click **View Project**, then **Add collaborator**. If you don't see Collaborators yet, use the **GPU Cluster Projects** tab instead (this tab is being replaced by the unified Collaborators page).
</Info>

New members are added with the **Editor** role by default, unless they are an organization admin (who are admins for every project by default). The user must already belong to your [organization](/docs/organizations).

### Removing Users

See [Removing Members](/docs/projects#removing-members) for the full steps.

<Warning>
  Removing a user revokes their access to all clusters and volumes in the project, including SSH permissions and Kubernetes Dashboard access. This takes effect within minutes.
</Warning>

<CardGroup>
  <Card title="Projects" icon="folder" href="/docs/projects">
    How project-based access works
  </Card>

  <Card title="Roles & Permissions" icon="shield" href="/docs/roles-permissions">
    Full Admin vs Member permission matrix
  </Card>
</CardGroup>

## Cluster Scaling

Clusters can scale flexibly in real time. Add on-demand compute to temporarily scale up when workload demand spikes, then scale back down as demand decreases.

Scaling operations can be performed via:

* Together Cloud UI
* Together CLI
* REST API

### Cluster Autoscaling

Cluster Autoscaling automatically adjusts the number of nodes in your cluster based on workload demand using the Kubernetes Cluster Autoscaler.

**How It Works:**

The Kubernetes Cluster Autoscaler monitors your cluster and:

* **Scales up** when pods are pending due to insufficient resources
* **Scales down** when nodes are underutilized for an extended period
* **Respects constraints** like minimum/maximum node counts and resource limits

When pods cannot be scheduled due to lack of resources, the autoscaler provisions additional nodes automatically. When nodes remain idle below a utilization threshold, they are safely drained and removed.

**Enabling Autoscaling:**

1. Navigate to **GPU Clusters** in the Together Cloud UI
2. Click **Create Cluster**
3. In the cluster configuration, toggle **Enable Autoscaling**
4. Configure your maximum GPUs
5. Create the cluster

Once enabled, the autoscaler runs continuously in the background, responding to workload changes without manual intervention.

<Note>
  Autoscaling works with both reserved and on-demand capacity. Scaling beyond reserved capacity will provision on-demand nodes at standard hourly rates.
</Note>

### Targeted Scale-down

To control which nodes are removed during scale-down:

1. **Cordon the node(s)** to prevent new workloads
   * For Kubernetes: `kubectl cordon <node_to_cordon>`
   * For Slurm: `sudo scontrol update NodeName=<node_name> State=drain Reason="<reason_for_cordoning>"`
2. **Trigger scale-down** via UI, CLI, or API

Cordoned and annotated nodes are prioritized for deletion above all others.

## Storage Management

Clusters support long-lived, resizable shared storage with persistent data.

### Storage Tiers

<Warning>
  **Local NVMe disks are ephemeral.** Data can be lost during node migrations, recreations, maintenance, or cluster operations. Use shared volumes for any data you need to keep. [See full storage guide →](/docs/cluster-storage)
</Warning>

All clusters include:

* **Shared volumes** – **Persistent.** Multi-NIC file-systems with high throughput. Survives pod restarts, node reboots/migrations/recreations, and cluster deletion.
* **Local NVMe disks** – **Ephemeral.** Fast local storage on each node. Use only for temporary scratch data.
* **`/home` directory** – **Persistent on Slurm** (NFS-backed, shared across nodes). **Ephemeral on Kubernetes** (local to each node).

### Upload Data

**For small datasets:**

```bash theme={null}
# Create a PVC and pod with your shared volume mounted
kubectl cp LOCAL_FILENAME POD_NAME:/data/
```

**For large datasets:**

Schedule a pod on the cluster that downloads directly from S3 or your data source:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: data-loader
spec:
  containers:
    - name: downloader
      image: amazon/aws-cli
      command: ["aws", "s3", "cp", "s3://bucket/data", "/mnt/shared/", "--recursive"]
      volumeMounts:
        - name: shared-storage
          mountPath: /mnt/shared
  volumes:
    - name: shared-storage
      persistentVolumeClaim:
        claimName: shared-pvc
```

### Resize Storage

Storage volumes can be dynamically resized as your data grows. Use the UI, CLI, or API to increase volume size.

[Learn more about storage options →](/docs/cluster-storage)

## Monitoring and Status

### Check Cluster Health

**From the UI:**

* View cluster status (Provisioning, Ready, Error)
* Monitor resource utilization
* Check node health indicators

**From kubectl:**

```bash theme={null}
kubectl get nodes           # Node status
kubectl top nodes           # Resource usage
kubectl get pods --all-namespaces  # All running workloads
```

**From Slurm:**

```bash theme={null}
sinfo                       # Node and partition status
squeue                      # Job queue
scontrol show node          # Detailed node info
```

## Best Practices

### Resource Management

* **Always** use shared volumes (PVC) for training data, checkpoints, model weights, and application state
* **Never** rely on local NVMe or node-local `/home` (on Kubernetes) for data you cannot afford to lose — it is ephemeral and can be wiped during migrations/recreations or maintenance
* Use local NVMe only for temporary scratch files that can be regenerated
* Set resource requests and limits in pod specs

### Job Scheduling

* Use Kubernetes Jobs for batch processing
* Use Slurm job arrays for embarrassingly parallel workloads
* Set appropriate timeouts and retry policies

### Data Management

* Download large datasets directly on the cluster (not via local machine)
* Use shared storage for training data and checkpoints
* Use local NVMe for temporary files during training

### Scaling Strategy

* Start with reserved capacity for baseline workload
* Add on-demand capacity for burst periods
* Use targeted scale-down to control costs

## GPU capacity not available

In case you do not see GPU capacity of the type you require in the api.together.ai cloud console, you can request GPU capacity by going to the create cluster view, selecting your region and GPU capacity, type required and clicking on "Request" button. Please also, select the date from which you need the GPUs.

We use these requests as input for our demand planning, and our team will reach out to you if and when that becomes available.

<Note>
  Submitting a request for capacity does not guarantee fulfillment due to very high demand, we try our best to fulfill these requests based on available GPU capacity. In case you need guaranteed GPU capacity for fixed periods of time, [please reach out to our team](https://www.together.ai/contact-sales).
</Note>

## Troubleshooting

### Pods not scheduling

* Check node status: `kubectl get nodes`
* Verify resource requests don't exceed available resources
* Check for taints on nodes: `kubectl describe node <node-name>`

### Storage mount issues

* Verify PVC is bound: `kubectl get pvc`
* Check volume name matches your shared volume
* Ensure storage class exists for local storage

### Slurm jobs not running

* Check node status: `sinfo`
* Verify partition is available
* Check job status: `scontrol show job <jobid>`

## What's Next?

* [Manage cluster access](/docs/projects#managing-project-members)
* [Understand roles and permissions](/docs/roles-permissions)
* [Understand billing and pricing](/docs/gpu-clusters-billing)
* [Explore API and automation options](/docs/gpu-clusters-api)
