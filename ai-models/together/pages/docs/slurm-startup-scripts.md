---
title: "Slurm startup scripts"
source: https://docs.together.ai/docs/slurm-startup-scripts
path: docs/slurm-startup-scripts
---

Configure lifecycle hook scripts that run automatically at node startup, job start, and job completion.

Startup scripts let you customize Slurm worker nodes, login nodes, and the controller by running shell scripts at specific lifecycle events. Use them to install packages, prepare job environments, clean up after jobs, and append custom Slurm configuration.

<Note>
  This feature is available on **Slurm Slinky v1.0 clusters only**. It works for both new cluster creation and editing existing v1.0 clusters.
</Note>

## Script types at a glance

Scripts fall into three categories based on when they run.

**Node init scripts** run once when a node starts up:

* **Worker init script:** Runs on each Slurm worker at boot. Install system packages, configure drivers, or pull container images.
* **Login init script:** Runs on the login node at startup. Install CLI tools and packages for interactive SSH sessions.

**Job lifecycle scripts** run on every job allocation and completion:

* **Worker prolog:** Runs on each worker node before a job starts. Set up directories, load datasets into local scratch, or export environment variables.
* **Worker epilog:** Runs on each worker node after a job ends. Clean up scratch files, flush logs, or reset node state.
* **Controller prolog:** Runs on the Slurm controller (`slurmctld`) at job allocation. Validate job parameters, send notifications, or log job metadata centrally.
* **Controller epilog:** Runs on the Slurm controller (`slurmctld`) at job completion. Log results, trigger downstream pipelines, or send completion notifications.

**Extra configuration** is not a script but a raw config block:

* **Extra slurm.conf:** Custom lines appended to `slurm.conf` on all nodes. Use this for scheduler tuning, prolog flags, or partition overrides.

## Node init scripts

### Worker init script

Runs on each Slurm worker node at boot, before the node accepts jobs. Use it to install packages or configure the environment that all jobs on this node depend on.

**Common use cases:**

* Install system packages (`apt-get install -y sox ffmpeg`).
* Install the AWS CLI or other data-transfer tools.
* Pull container images or download shared assets.
* Configure environment variables that apply to every job.

**Example:**

```bash theme={null}
#!/bin/bash
set -e

# Install audio and video processing tools
apt-get update && apt-get install -y sox ffmpeg

# Install AWS CLI for S3 data transfers
pip install awscli

echo "Worker init complete"
```

### Login init script

Runs on the login node at startup. The login node is where users SSH in to submit jobs and inspect results, so this script installs tools for interactive use.

**Common use cases:**

* Install CLI utilities for data exploration.
* Set up shared Python environments.
* Configure shell defaults for all users.

**Example:**

```bash theme={null}
#!/bin/bash
set -e

# Install interactive tools
apt-get update && apt-get install -y htop tmux tree

echo "Login init complete"
```

## Job lifecycle scripts

### Worker prolog

Runs on each allocated worker node before the job starts. The script runs as root and executes before any user processes launch.

**Common use cases:**

* Create per-job scratch directories on local NVMe.
* Stage input data from shared storage to local disk.
* Export environment variables for the job.
* Verify GPU health before the job runs.

**Example:**

```bash theme={null}
#!/bin/bash
set -e

# Create a per-job scratch directory on local NVMe
JOB_SCRATCH="/scratch/job_${SLURM_JOB_ID}"
mkdir -p "$JOB_SCRATCH"
chown "$SLURM_JOB_USER" "$JOB_SCRATCH"

echo "Worker prolog complete for job ${SLURM_JOB_ID}"
```

<Note>
  By default, the worker prolog runs when the first job step starts on the node, not at allocation time. To run it immediately at allocation, add `PrologFlags=Alloc` to the **Extra slurm.conf** field.
</Note>

### Worker epilog

Runs on each allocated worker node after the job ends. The script runs as root and executes after all user processes have terminated.

**Common use cases:**

* Remove per-job scratch directories.
* Flush job logs to shared storage.
* Reset GPU state or clear shared memory.
* Kill orphaned processes.

**Example:**

```bash theme={null}
#!/bin/bash

# Clean up per-job scratch directory
JOB_SCRATCH="/scratch/job_${SLURM_JOB_ID}"
rm -rf "$JOB_SCRATCH"

# Kill any orphaned user processes
pkill -u "$SLURM_JOB_USER" || true

echo "Worker epilog complete for job ${SLURM_JOB_ID}"
```

### Controller prolog

Runs on the Slurm controller (`slurmctld`) at job allocation, before the job reaches the worker nodes. Use this for centralized setup that does not need to run on every node.

**Common use cases:**

* Log job metadata to a central database.
* Send a Slack or webhook notification when a job starts.
* Validate job parameters before workers are assigned.

**Example:**

```bash theme={null}
#!/bin/bash

# Log job start to a central file
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) JOB_START job_id=${SLURM_JOB_ID} user=${SLURM_JOB_USER}" >> /var/log/slurm/job_events.log
```

### Controller epilog

Runs on the Slurm controller (`slurmctld`) at job completion. Use this for centralized teardown or post-job automation.

**Common use cases:**

* Log job completion and exit status.
* Trigger a downstream pipeline (fine-tuning, evaluation, deployment).
* Send a completion notification.

**Example:**

```bash theme={null}
#!/bin/bash

# Log job completion
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) JOB_END job_id=${SLURM_JOB_ID} user=${SLURM_JOB_USER}" >> /var/log/slurm/job_events.log
```

## Extra slurm.conf

Append custom Slurm configuration to `slurm.conf` on all nodes. Lines entered here are added verbatim after the default configuration.

**Common use cases:**

* Set `PrologFlags=Alloc` to run the worker prolog at allocation time instead of first job step.
* Tune scheduler parameters.
* Configure accounting or job completion plugins.

**Example:**

```ini theme={null}
PrologFlags=Alloc
SchedulerParameters=batch_sched_delay=10,bf_interval=180
```

<Note>
  Changes to **Extra slurm.conf** take effect after the cluster applies the updated configuration. Running jobs are not affected until they complete or the nodes restart.
</Note>

## View configured startup scripts

Configured scripts appear on the cluster details page as `.sh` files (and `extra_slurm.conf` for the extra configuration block). Select a file name to open a read-only dialog with the script contents and a copy button.

## Configure startup scripts

1. Open the [Together Cloud console](https://api.together.ai) and navigate to your cluster.
2. Select **Edit Configuration** in the top right of the cluster details page.
3. Enter your script in the corresponding text box (Worker Prolog, Worker Epilog, Login Init Script, etc.).
4. Select **Save**.

Every script must start with a shebang line (e.g., `#!/bin/bash`). The cluster applies the updated scripts to the relevant nodes automatically.

<Warning>
  **Saving triggers a live Slurm reconfigure on the running cluster.** For existing clusters, this can briefly affect job scheduling. Test configuration changes on a non-critical cluster first.
</Warning>

<Note>
  For prolog and epilog updates, the underlying ConfigMaps update immediately. However, existing worker nodes may cache the previous scripts via Slurm's configless mechanism. New jobs on those workers continue using the old scripts until the workers restart and pick up the updated versions.
</Note>

## Failure handling

Script failures have different consequences depending on which script fails.

**Worker prolog failure (non-zero exit):**

* The node is set to `DRAIN` state.
* The job is requeued (batch jobs only). Interactive jobs (`salloc`, `srun`) are cancelled.

**Worker epilog failure (non-zero exit):**

* The node is set to `DRAIN` state.
* A drained node does not accept new jobs until an admin resumes it.

**Controller prolog failure (non-zero exit):**

* The job is requeued (batch jobs) or cancelled (interactive jobs).
* The node is not affected.

**Controller epilog failure (non-zero exit):**

* The failure is logged but has no other effect on the job or node.

<Warning>
  A failing prolog or epilog on a worker node drains the node. Monitor your scripts carefully and test them before deploying to production clusters.
</Warning>

## Best practices

* Keep scripts short and fast. Long-running scripts delay job scheduling.
* Use `set -e` in init scripts so failures surface immediately instead of silently continuing.
* Do not call Slurm commands (`squeue`, `scontrol`, `sacctmgr`) inside prolog or epilog scripts. This can cause deadlocks and degrade scheduler performance.
* Use the `SLURM_JOB_ID` and `SLURM_JOB_USER` environment variables to scope cleanup and logging to the correct job.
* Test scripts on a development cluster before applying them to production.
* Use **Extra slurm.conf** with `PrologFlags=Alloc` if your worker prolog must run at allocation time rather than at first job step.

## Troubleshooting

### Node stuck in DRAIN state after script failure

A worker prolog or epilog that returns a non-zero exit code drains the node.

**Fix:**

* SSH into the login node and check the script output in `/var/log/slurm/`.
* Fix the script, then resume the node:
  ```bash theme={null}
  sudo scontrol update NodeName=<node_name> State=resume Reason="script fixed"
  ```

### Init script packages not available in jobs

The worker init script runs at node boot, not at job start. If a package install fails silently, jobs will not have the expected tools.

**Fix:**

* Add `set -e` to your init script to catch failures.
* SSH into a worker node and verify the package is installed.

### Worker prolog not running at allocation time

By default, the worker prolog runs at first job step, not at allocation. If your prolog must run immediately when the job is allocated, add `PrologFlags=Alloc` to the **Extra slurm.conf** field.

## Additional resources

* [Slurm prolog and epilog guide](https://slurm.schedmd.com/prolog_epilog.html)
* [Slurm environment variables](https://slurm.schedmd.com/sbatch.html#OPT_environment)
* [Slurm configuration](/docs/slurm-configuration)
