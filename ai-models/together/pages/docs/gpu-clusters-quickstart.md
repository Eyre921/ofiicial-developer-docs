---
title: "Quickstart"
source: https://docs.together.ai/docs/gpu-clusters-quickstart
path: docs/gpu-clusters-quickstart
---

Create a reserved or on-demand GPU cluster and connect to it.

## Create a cluster

Follow these steps to create your first GPU cluster:

### 1. Access the cluster console

1. Log into [api.together.ai](https://api.together.ai)
2. Select **GPU Clusters** in the top navigation menu
3. Select **Create Cluster**

### 2. Choose capacity type

Select the billing mode that fits your needs:

* **Reserved:** Pay upfront to reserve capacity for 1-90 days with discounted pricing.
* **On-demand:** Pay hourly with no commitment. Terminate anytime.

[Learn more about capacity types →](/docs/gpu-clusters-overview#capacity-options)

### 3. Configure your cluster

**Cluster size**

* Select the number and type of GPUs (for example, `8xH100`).
* Available options: H100, H200, and B200.

**Cluster name**

* Enter a descriptive name.

**Cluster type**

* **Kubernetes:** For containerized workloads and Kubernetes-native tools.
* **Slurm:** For HPC-style batch scheduling and traditional workflows.

**Region**

* Defaults to **Any region**. Together assigns the region with the most available capacity for your selected GPU type when you create the cluster.
* Select a specific datacenter region instead if you need the cluster in a particular location.
* Changing the GPU type resets the region to **Any region** and clears any selected shared volume, because volumes are region-specific.

**Duration** (reserved only)

* Choose reservation length: 1-90 days.

**Shared volume**

* Create and name your persistent storage volume.
* Minimum size: 1 TiB.
* Can be resized later as needed.

**Optional settings**

* Select NVIDIA driver version.
* Select CUDA version.

### 4. Create and verify

1. Select **Proceed** to create your cluster.
2. Monitor the cluster status in the UI as it provisions.
3. Wait for status to transition to **Ready**.

Your cluster is now ready to use!

## Connect to the cluster

### For Kubernetes clusters

1. **Install kubectl**
   * [macOS installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/).
   * Or use your preferred method for your OS.

2. **Download kubeconfig**

   Use the [Together CLI](/reference/cli/clusters) to download the cluster's credentials to your local `~/.kube/config`. Find your cluster ID with `tg beta clusters list`:

```bash theme={null}
tg beta clusters get-credentials <CLUSTER_ID> --set-default-context
```

3. **Verify connectivity**

```bash theme={null}
kubectl get nodes
```

You should see all worker and control plane nodes listed.

4. **Start using your cluster**
   * [Deploy workloads](/docs/gpu-clusters-management#kubernetes-usage).
   * [Access the Kubernetes dashboard](/docs/gpu-clusters-management#kubernetes-dashboard).

### For Slurm clusters

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
   * [Learn about Slurm commands](/docs/slurm).
   * Submit batch jobs with `sbatch`.
   * Run interactive jobs with `srun`.

5. **Optional: Download kubeconfig**

   Slurm clusters run on Kubernetes, so if you need `kubectl` access to the underlying cluster API, any project member can download the kubeconfig from the cluster details page or with the Together CLI:

```bash theme={null}
tg beta clusters get-credentials <CLUSTER_ID> --set-default-context
```

SSH to the login node remains the primary workflow for submitting jobs. See [Download cluster kubeconfig](/docs/gpu-clusters-management#download-cluster-kubeconfig) for console steps and OIDC visibility rules.

## Common first tasks

### Upload data

For small datasets:

```bash theme={null}
# Create a pod with your shared volume mounted
# Then copy files directly
kubectl cp local_file.tar.gz pod-name:/mnt/shared/
```

For large datasets, create a pod that downloads from S3 or your data source.

### Run a test job

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

* Check cluster status in the UI (should be **Ready**).
* Re-download the latest credentials with `tg beta clusters get-credentials <CLUSTER_ID>`.

### SSH connection refused

* Verify your SSH key was added before cluster creation.
* Check the connection command in the cluster UI.
* Ensure you're using the correct hostname.

### Capacity unavailable

* Use the **Notify Me** option to get alerts when capacity is available.
* Try a different region.
* Contact [support@together.ai](mailto:support@together.ai) for custom requirements.

## Next steps

<CardGroup>
  <Card title="Manage clusters" icon="server" href="/docs/gpu-clusters-management">
    Deploy workloads, manage storage, and scale a running cluster.
  </Card>

  <Card title="Capacity types" icon="scale" href="/docs/gpu-clusters-capacity-types">
    Compare reserved and on-demand capacity and how each is billed.
  </Card>

  <Card title="API and CLI" icon="terminal" href="/docs/gpu-clusters-api">
    Create and manage clusters from the API or Together CLI.
  </Card>

  <Card title="GPU cluster pricing" icon="currency-dollar" href="https://www.together.ai/pricing#gpu-clusters">
    View current reserved and on-demand GPU cluster rates.
  </Card>
</CardGroup>
