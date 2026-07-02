---
title: "Cluster storage"
source: https://docs.together.ai/docs/cluster-storage
path: docs/cluster-storage
---

Understand storage types, persistence, and best practices for GPU clusters

Together GPU Clusters provides multiple storage options. It is critical to understand which storage is **persistent** and which is **ephemeral** so you can architect your workloads to avoid data loss.

<Warning>
  **Local NVMe disks and node-local storage are ephemeral.** Data on these drives can be lost at any time during node migrations/recreations, maintenance, or other cluster operations. Always use shared volumes (PVC-backed storage) for any data you need to keep.
</Warning>

## Storage types at a glance

**Use this to decide where to store your data:**

* **Shared volumes (PVC)**: Persistent. Survives pod restarts, node reboots/migrations/recreations, cluster operations, and even cluster deletion. **Use this for training data, checkpoints, model weights, and anything you cannot lose.**
* **Local NVMe disks**: Ephemeral. Fast local storage on each node. **Data can be lost during node migrations/recreations or cluster operations.** Use only for temporary scratch data (e.g., intermediate computation files).
* **`/home` directory**: Persistence depends on cluster type (see below).

## Persistent storage: shared volumes

Shared volumes are remote-attached, high-speed filesystems. They are created during cluster setup (or attached from an existing volume) and are accessible from all nodes.

**Persists across:**

* Pod restarts and rescheduling
* Node reboots, migrations, recreations, and maintenance
* Cluster scaling operations
* Cluster deletion (volumes persist independently. In case of reserved, they move to on-demand pricing and can be reattached to other clusters)

**How to use shared volumes:**

* **Kubernetes clusters**: A static PersistentVolume (PV) is provided with the same name as your shared volume. Create a PersistentVolumeClaim (PVC) referencing it, then mount it in your pods. [Step-by-step setup →](/docs/gpu-clusters-management#deploy-pods-with-storage)
* **Slurm clusters**: The shared volume is mounted and accessible from all compute and login nodes at /home directory path.

<Tip>
  **Best practice:** Always store training data, checkpoints, model weights, logs, and application state on shared volumes. This ensures your data survives any cluster event.
</Tip>

## Ephemeral storage: local NVMe disks

Each node has local NVMe drives that provide high-speed read/write performance.

<Warning>
  **Data on local NVMe disks is not durable.** It can be lost without warning during:

  * Node migrations/recreations (scheduled or unscheduled)
  * Cluster maintenance operations
  * Hardware failures
  * Pod rescheduling to a different node

  Do **not** rely on local NVMe for any data you need to keep. Use it only for temporary scratch files that can be regenerated.
</Warning>

## `/home` directory

The behavior of `/home` differs between cluster types:

### Slurm clusters

On Slurm clusters, `/home` is a **persistent NFS-backed file system** shared across all nodes (compute and login). It is mounted from the head node and is suitable for:

* Code and scripts
* Configuration files
* Logs
* Small datasets
* Model weights and training data

We recommend logging into the Slurm head node first to set up your user folder with the correct permissions.

### Kubernetes clusters

On Kubernetes clusters, `/home` is **local to each node and ephemeral**. It is not shared across nodes and is subject to the same data loss risks as local NVMe storage.

<Warning>
  On Kubernetes clusters, do **not** store important data in `/home`. Use a shared volume (PVC) instead.
</Warning>

## Which storage should I use?

* **Training data, datasets** → Shared volume (PVC), or `/home` on Slurm clusters
* **Checkpoints, model weights** → Shared volume (PVC), or `/home` on Slurm clusters
* **Application state, databases** → Shared volume (PVC), or `/home` on Slurm clusters
* **Code, configs** → Shared volume (PVC), or `/home` on Slurm clusters
* **Temporary scratch files** → Local NVMe (acceptable to lose)
* **Intermediate computation artifacts** → Local NVMe (acceptable to lose)

## Upload your data

**For small datasets:**

1. Create a PVC using the shared volume name as the `volumeName`, and a pod to mount the volume
2. Run `kubectl cp LOCAL_FILENAME YOUR_POD_NAME:/data/`

**For large datasets:**

Schedule a pod on the cluster that downloads directly from S3 or your data source. [See example →](/docs/gpu-clusters-management#upload-data)

[Learn more about GPU Clusters →](/docs/gpu-clusters-overview)
