---
title: "Slurm management system"
source: https://docs.together.ai/docs/slurm
path: docs/slurm
---

Use Slurm for HPC-style workload management on GPU clusters with familiar batch scheduling commands and job arrays.

[Learn more about GPU Clusters →](/docs/gpu-clusters-overview)

## Overview

Slurm is a cluster management system that allows users to manage and schedule jobs on a cluster of computers. A Together GPU Cluster provides Slurm configured out-of-the-box for distributed training and the option to use your own scheduler. Users can submit computing jobs to the Slurm head node where the scheduler will assign the tasks to available GPU nodes based on resource availability. For more information on Slurm, see the [Slurm Quick Start User Guide](https://slurm.schedmd.com/quickstart.html).

### **Slurm Basic Concepts**

1. **Jobs**: A job is a unit of work that is submitted to the cluster. Jobs can be scripts, programs, or other types of tasks.
2. **Nodes**: A node is a computer in the cluster that can run jobs. Nodes can be physical machines or virtual machines.
3. **Head Node**: Each Together GPU Cluster is configured with a head node. A user will log in to the head node to write jobs, submit jobs to the GPU cluster, and retrieve the results.
4. **Partitions**: A partition is a group of nodes that can be used to run jobs. Partitions can be configured to have different properties, such as the number of nodes and the amount of memory available.
5. **Priorities**: Priorities are used to determine which jobs should be run first. Jobs with higher priorities are given preference over jobs with lower priorities.

### **Using Slurm**

1. **Job Submission**: Jobs can be submitted to the cluster using the **`sbatch`** command. Jobs can be submitted in batch mode or interactively using the **`srun`** command.
2. **Job Monitoring**: Jobs can be monitored using the **`squeue`** command, which displays information about the jobs that are currently running or waiting to run.
3. **Job Control**: Jobs can be controlled using the **`scancel`** command, which allows users to cancel or interrupt jobs that are running.

<Warning>
  **Set memory limits explicitly in your `sbatch` scripts.**

  Set `--mem` to a specific value (e.g., `--mem=500G`) rather than `--mem=0`. `--mem=0` tells Slurm to use all memory on the node, which can crash the node under load. We recommend not exceeding 90% of the node's memory to leave headroom for system processes. Adjust lower based on what your job actually needs.

  If a job exceeds its allocation, Slurm fails it with an `OUT_OF_MEMORY` error instead of crashing the node.
</Warning>

### Slurm Job Arrays

You can use Slurm job arrays to partition input files into k chunks and distribute the chunks across the nodes. See this example on processing RPv1 which will need to be adapted to your processing: [arxiv-clean-slurm.sbatch](https://github.com/togethercomputer/RedPajama-Data/blob/rp_v1/data_prep/arxiv/scripts/arxiv-clean-slurm.sbatch)

### Run a Jupyter notebook on a GPU node

Reserve a node through Slurm, start Jupyter there, then tunnel to it from your local machine:

1. Start an interactive session on the target node:

   ```bash theme={null}
   srun --pty --nodes=1 --nodelist=<NODE_NAME> --ntasks-per-node=1 --gres=gpu:8 /bin/bash
   ```

2. Launch Jupyter from that session:

   ```bash theme={null}
   jupyter lab --no-browser --port=8888 --ip=0.0.0.0
   ```

3. From your local machine, open an SSH tunnel to the node through the cluster's SSH proxy (see [Direct SSH access](/docs/gpu-clusters-management#direct-ssh-access) for the host format):

   ```bash theme={null}
   ssh -N -L 8888:localhost:8888 -J <LOGIN>@ssh.<CLUSTER_ID>.<REGION>.cloud.together.ai <LOGIN>@<NODE_NAME>.slurm-compute.slurm
   ```

4. Open `http://localhost:8888` in your browser and sign in with the token Jupyter printed in step 2.

### Install Python packages that persist

Login node environments can be reset when the login pod restarts. Create a virtual environment on the shared filesystem instead of installing packages system-wide:

```bash theme={null}
python -m venv /home/$USER/venvs/myenv
source /home/$USER/venvs/myenv/bin/activate
pip install <package>
```

See [Cluster storage](/docs/cluster-storage) for which paths persist on your cluster type.

## Troubleshooting

### Jobs stuck in a pending state

The most common causes:

* **Insufficient resources:** All GPUs are currently allocated. Check the queue and node availability with `squeue` and `sinfo`.
* **Request exceeds limits:** The job requests more resources than any node provides.
* **Partition limits:** The job targets a partition with limited capacity. See [Slurm configuration](/docs/slurm-configuration#modify-partitions) to adjust partitions.

Inspect a specific job with:

```bash theme={null}
squeue -u $USER
scontrol show job <JOB_ID>
```

### "Unable to contact slurm controller (connect failure)"

The Slurm controller is unreachable, usually because it's restarting or there's a network issue between nodes. Wait a few minutes and retry. Check the controller pod's status with `kubectl get pods -n slurm`, and see [Slurm configuration](/docs/slurm-configuration#troubleshooting) for restart and log commands. If the issue persists for more than 30 minutes, [contact support](https://www.together.ai/contact) with the cluster name, the exact error, and when it started.

### "couldn't chdir to home directory" errors

```
slurmstepd: error: couldn't chdir to `/home/<username>': No such file or directory: going to /tmp instead
```

The job's working directory isn't accessible on the compute node. On Slurm clusters, `/home` is a shared NFS filesystem mounted on all nodes, so this usually means the mount is missing or unhealthy on that node. Set the working directory explicitly in your job script (`#SBATCH --chdir=<path>`), confirm the path exists on the node, and [contact support](https://www.together.ai/contact) if `/home` isn't mounted where it should be. See [Cluster storage](/docs/cluster-storage) for how `/home` behaves on each cluster type.

### Node drained with reason "KillTaskFailure"

`sinfo -R` shows a node drained with `KillTaskFailure` when Slurm couldn't cleanly terminate a job step on it. Slurm drains the node so no new work lands there. Common causes are unkillable processes (stuck in kernel I/O or a hung GPU driver call), container teardown failures, or a `KillWait` timeout that's too short for your cleanup.

To recover:

1. Confirm the reason and the affected jobs:

   ```bash theme={null}
   scontrol show node <NODE_NAME> | egrep -i "State=|Reason="
   sacct -j <JOB_ID> --format=JobID,State,ExitCode,NodeList,Elapsed
   ```

2. Try resuming the node:

   ```bash theme={null}
   scontrol update nodename=<NODE_NAME> state=resume
   ```

3. If your job caused it, make it easier to kill next time: handle `SIGTERM` promptly in your training script, checkpoint periodically so exits are fast, and make sure all ranks of a distributed job exit when one rank is terminated.

If the node won't resume, [contact support](https://www.together.ai/contact) with the cluster name, node name, drain reason, and the job IDs that were running.

### Array jobs fail with "Invalid job array specification"

The array exceeds the configured `MaxArraySize` (a maximum array index of 1,000 by default). Raise it in `slurm.conf` by editing the cluster's ConfigMap, then restart the controller. See [Slurm configuration](/docs/slurm-configuration#edit-configuration) for the procedure.

### Jobs need more time to shut down cleanly

If jobs are killed before checkpointing finishes, check the `KillWait` setting (30 seconds by default):

```bash theme={null}
scontrol show config | grep -i killwait
```

Raise it in `slurm.conf` the same way as other configuration changes. See [Slurm configuration](/docs/slurm-configuration#edit-configuration).
