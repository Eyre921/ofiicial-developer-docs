---
title: "Quickstart"
source: https://docs.together.ai/docs/gpu-clusters-quickstart
path: docs/gpu-clusters-quickstart
---

Get started with GPU Clusters in minutes.

## Create a Cluster

Follow these steps to create your first GPU cluster:

### 1. Access the Cluster Console

1. Log into [api.together.ai](https://api.together.ai)
2. Select **GPU Clusters** in the top navigation menu
3. Select **Create Cluster**

### 2. Choose Capacity Type

Select the billing mode that fits your needs:

* **Reserved** – Pay upfront to reserve capacity for 1-90 days with discounted pricing
* **On-demand** – Pay hourly with no commitment; terminate anytime

[Learn more about capacity types →](/docs/gpu-clusters-capacity-types)

### 3. Configure Your Cluster

**Cluster Size**

* Select the number and type of GPUs (e.g., `8xH100`)
* Available options: H100, H200, B200

**Cluster Name**

* Enter a descriptive name for easy identification

**Cluster Type**

* **Kubernetes** – For containerized workloads and K8s-native tools
* **Slurm** – For HPC-style batch scheduling and traditional workflows

**Region**

* Defaults to **Any region**. Together assigns the region with the most available capacity for your selected GPU type when you create the cluster.
* Select a specific datacenter region instead if you need the cluster in a particular location.
* Changing the GPU type resets the region to **Any region** and clears any selected shared volume, because volumes are region-specific.

**Duration** (Reserved only)

* Choose reservation length: 1-90 days

**Shared Volume**

* Create and name your persistent storage volume
* Minimum size: 1 TiB
* Can be resized later as needed

**Optional Settings**

* Select NVIDIA driver version
* Select CUDA version

### 4. Create and Verify

1. Click **Proceed** to create your cluster
2. Monitor the cluster status in the UI as it provisions
3. Wait for status to transition to **Ready**

Your cluster is now ready to use!

## Next Steps

### For Kubernetes Clusters

1. **Install kubectl**
   * [MacOS installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
   * Or use your preferred method for your OS

2. **Download kubeconfig**

   Use the [Together CLI](/reference/cli/clusters) to download the cluster's credentials to your local `~/.kube/config`. Find your cluster ID with `tg beta clusters list`:

```bash theme={null}
tg beta clusters get-credentials [CLUSTER_ID] --set-default-context
```

3. **Verify connectivity**

```bash theme={null}
kubectl get nodes
```

You should see all worker and control plane nodes listed.

4. **Start using your cluster**
   * [Deploy workloads](/docs/gpu-clusters-management#kubernetes-usage)
   * [Access the K8s Dashboard](/docs/gpu-clusters-management#kubernetes-dashboard)

### For Slurm Clusters

1. **Choose an SSH access method**
   * On clusters with OIDC enabled, select **OIDC** or **Key-based** in **SSH access method** on the cluster details page.
   * **OIDC:** Install the [Together CLI](/reference/cli/getting-started) (`uv tool install "together[cli]"`, requires CLI 2.20+ and Python 3.10+) and choose a login name when prompted. No SSH key is required.
   * **Key-based:** Add your SSH key at [api.together.ai/settings/ssh-key](https://api.together.ai/settings/ssh-key) before cluster creation.

2. **Connect via SSH**
   * Copy the head node command from the cluster sidebar with **Copy head node SSH command**.
   * Paste and run the command in your terminal to reach the Slurm login node.

3. **Verify Slurm**

```bash theme={null}
sinfo          # View node status
squeue         # View job queue
```

4. **Start submitting jobs**
   * [Learn about Slurm commands](/docs/slurm)
   * Submit batch jobs with `sbatch`
   * Run interactive jobs with `srun`

## Common First Tasks

### Upload Data

For small datasets:

```bash theme={null}
# Create a pod with your shared volume mounted
# Then copy files directly
kubectl cp local_file.tar.gz pod-name:/mnt/shared/
```

For large datasets, create a pod that downloads from S3 or your data source.

### Run a Test Job

**Kubernetes example:**

```bash theme={null}
kubectl run test --image=ubuntu --command -- sleep infinity
kubectl exec -it test -- bash
```

**Slurm example:**

```bash theme={null}
srun --gpus=1 --pty bash
nvidia-smi
```

## Troubleshooting

### Can't see my nodes

* Check cluster status in the UI (should be "Ready")
* Re-download the latest credentials with `tg beta clusters get-credentials [CLUSTER_ID]`

### SSH connection refused

* Verify your SSH key was added before cluster creation
* Check the connection command in the cluster UI
* Ensure you're using the correct hostname

### Capacity unavailable

* Use the "Notify Me" option to get alerts when capacity is available
* Try a different region
* Contact [support@together.ai](mailto:support@together.ai) for custom requirements

## What's Next?

* [Learn cluster management operations](/docs/gpu-clusters-management)
* [Understand capacity types and billing](/docs/gpu-clusters-capacity-types)
* [Explore API and CLI options](/docs/gpu-clusters-api)
* [View current GPU Cluster pricing](https://www.together.ai/pricing#gpu-clusters)
