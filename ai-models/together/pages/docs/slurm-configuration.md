---
title: "Slurm configuration"
source: https://docs.together.ai/docs/slurm-configuration
path: docs/slurm-configuration
---

Customize Slurm cluster settings to match your workload requirements

Modify Slurm configuration files to optimize scheduling, resource allocation, and job management for your GPU cluster.

## Prerequisites

* `kubectl` CLI installed and configured
* Kubeconfig downloaded from your cluster
* Access to your cluster's Slurm namespace

## Configuration Files

Your Slurm cluster configuration is stored in a Kubernetes ConfigMap with four main files:

| File             | Purpose                                                    |
| ---------------- | ---------------------------------------------------------- |
| `slurm.conf`     | Main cluster configuration (nodes, partitions, scheduling) |
| `gres.conf`      | GPU and generic resource definitions                       |
| `cgroup.conf`    | Control group resource management                          |
| `plugstack.conf` | SPANK plugin configuration                                 |

## Edit Configuration

### Update ConfigMap

Edit the ConfigMap directly:

```bash theme={null}
kubectl edit configmap slurm -n slurm
```

This opens the ConfigMap in your default editor. Make your changes and save.

**Alternative method:**

```bash theme={null}
# Export to local file
kubectl get configmap slurm -n slurm -o yaml > slurm-config.yaml

# Edit locally
# ... make your changes ...

# Apply changes
kubectl apply -f slurm-config.yaml
```

### Restart Components

After editing the ConfigMap, restart the appropriate components:

**For `slurm.conf` changes:**

```bash theme={null}
# Restart controller
kubectl rollout restart statefulset slurm-controller -n slurm

# Restart compute node pods
kubectl delete pods -n slurm -l app=slurm-compute-production
```

**For `gres.conf` or `plugstack.conf` changes:**

```bash theme={null}
# Restart compute node pods only
kubectl delete pods -n slurm -l app=slurm-compute-production
```

### Verify Changes

```bash theme={null}
# Check rollout status
kubectl rollout status statefulset slurm-controller -n slurm

# Verify configuration in pod
kubectl exec -it slurm-controller-0 -n slurm -- cat /etc/slurm/slurm.conf

# Test Slurm functionality
kubectl exec -it slurm-controller-0 -n slurm -- scontrol show config
```

## Configuration Examples

### Configure GPU Resources

Edit `gres.conf` to define GPU resources:

```
Name=gpu Type=a100 File=/dev/nvidia[0-7]
Name=gpu Type=h100 File=/dev/nvidia[8-15]
```

### Modify Partitions

Edit the partition section in `slurm.conf`:

```
PartitionName=gpu Nodes=gpu-nodes State=UP Default=NO MaxTime=24:00:00
PartitionName=cpu Nodes=cpu-nodes State=UP Default=YES
```

### Tune Scheduler

Adjust scheduler parameters in `slurm.conf`:

```
SchedulerParameters=batch_sched_delay=10,bf_interval=180,sched_max_job_start=500
```

### Update Resource Allocation

Modify resource allocation settings:

```
SelectTypeParameters=CR_Core_Memory
DefMemPerCPU=4096  # 4GB per CPU
```

### Enable Cgroup Limits

Edit `cgroup.conf` to enforce resource limits:

```
CgroupPlugin=cgroup/v1
ConstrainCores=yes
ConstrainRAMSpace=yes
```

Then update `slurm.conf`:

```
ProctrackType=proctrack/cgroup
TaskPlugin=task/cgroup,task/affinity
```

## Troubleshooting

### Configuration Not Applied

```bash theme={null}
# Verify ConfigMap was updated
kubectl get configmap slurm -n slurm -o yaml

# Check pod age (should be recent after restart)
kubectl get pods -n slurm

# View controller logs
kubectl logs slurm-controller-0 -n slurm
```

### Syntax Errors

```bash theme={null}
# Check controller logs for errors
kubectl logs slurm-controller-0 -n slurm | grep -i error

# View recent events
kubectl get events -n slurm --sort-by='.lastTimestamp'
```

### Pods Not Restarting

```bash theme={null}
# Check rollout status
kubectl rollout status statefulset slurm-controller -n slurm

# Force delete and recreate pod
kubectl delete pod slurm-controller-0 -n slurm
```

### Jobs Failing After Changes

```bash theme={null}
# Check node status
kubectl exec -it slurm-controller-0 -n slurm -- sinfo

# Check specific node details
kubectl exec -it slurm-controller-0 -n slurm -- scontrol show node <nodename>

# View job errors
kubectl exec -it slurm-controller-0 -n slurm -- scontrol show job <jobid>
```

## Quick Reference

### View Configurations

```bash theme={null}
# View all Slurm configmaps
kubectl get configmaps -n slurm | grep slurm

# View slurm.conf content
kubectl get configmap slurm -n slurm -o jsonpath='{.data.slurm\.conf}'

# View gres.conf content
kubectl get configmap slurm -n slurm -o jsonpath='{.data.gres\.conf}'
```

### Restart Components

```bash theme={null}
# Restart controller
kubectl rollout restart statefulset slurm-controller -n slurm

# Restart accounting daemon
kubectl rollout restart statefulset slurm-accounting -n slurm

# Restart compute node pods
kubectl delete pods -n slurm -l app=slurm-compute-production
```

### Monitor Cluster

```bash theme={null}
# Watch pod status
kubectl get pods -n slurm -w

# View logs (follow mode)
kubectl logs -f slurm-controller-0 -n slurm

# Check Slurm cluster status
kubectl exec -it slurm-controller-0 -n slurm -- sinfo
```

## Best Practices

* **Back up configurations** before making changes
* **Test in development** before applying to production
* **Make incremental changes** to isolate issues
* **Document your changes** for future reference
* **Monitor logs and jobs** after applying changes
* **Use version control** to track configuration changes

<Note>
  Slurm compute nodes run as pods (not daemonsets). When you delete compute node pods, they will automatically restart with the new configuration. Running jobs may be affected during the restart.
</Note>

## Additional Resources

* [Slurm Configuration Tool](https://slurm.schedmd.com/configurator.html) - Interactive configuration generator
* [Slurm Configuration Reference](https://slurm.schedmd.com/slurm.conf.html) - Complete parameter documentation
* [GRES Configuration](https://slurm.schedmd.com/gres.html) - GPU and resource configuration guide
* [Scheduling Configuration](https://slurm.schedmd.com/sched_config.html) - Scheduler tuning guide
