---
title: "Health checks"
source: https://docs.together.ai/docs/health-checks
path: docs/health-checks
---

Monitor GPU node health with active diagnostic tests and continuous passive monitoring.

Health checks detect hardware and software issues on your GPU nodes before they impact running workloads. Together supports two types of health checks: [active checks](#active-health-checks) that run on-demand diagnostic tests, and [passive checks](#passive-health-checks) that monitor nodes continuously in the background. Issues detected by either type can trigger [node repair](/docs/node-repair) recommendations.

## Active health checks

Active health checks let you run targeted diagnostic tests on your GPU nodes to validate GPUs, InfiniBand networking, storage, and other components. These tests require full GPU utilization and run on demand.

### How to run health checks

#### Quick steps

1. Navigate to your cluster in the [Together web interface](https://api.together.ai/clusters).
2. Go to the **Cluster Details** tab and select the **Health Checks** sub-tab.
3. Select the **Run a health check** button (top right).
4. In the **Run Health Checks** dialog, select one or more tests to run:
   * **DCGM Diag:** NVIDIA GPU diagnostics.
   * **GPU Burn:** GPU stress test.
   * **Single-Node NCCL:** Single-node GPU communication test.
   * **NVBandwidth: CPU to GPU Bandwidth:** PCIe bandwidth test.
   * **NVBandwidth: GPU to CPU Bandwidth:** PCIe bandwidth test.
   * **NVBandwidth: GPU-CPU Latency:** PCIe latency test.
   * **InfiniBand Write Bandwidth:** InfiniBand network performance test.
   * **Storage Performance:** Storage throughput and data-integrity test.
5. Select **Next: Select Nodes**.
6. Choose which nodes to test.
7. (Optional) Configure test parameters like duration or diagnostic level.
8. Select **Run** to start the health checks.

<Note>
  **Active tests:** These health checks require full GPU utilization from the node and impact any running workloads during the test.
</Note>

### Available tests

Each health check validates different aspects of your GPU infrastructure:

#### GPU diagnostics

**DCGM Diag**

* Runs NVIDIA Data Center GPU Manager diagnostics.
* Validates GPU compute capability, memory integrity, and thermal performance.
* **Configurable:** Diagnostic level (1-3, where 3 is most comprehensive).
* **Use for:** Comprehensive GPU health validation.
* **Learn more:** [NVIDIA DCGM documentation](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html).

**GPU Burn**

* Stress tests GPUs with intensive compute workloads.
* Validates stability under sustained high utilization.
* **Configurable:** Test duration.
* **Use for:** Identifying thermal issues, power problems, or instability.
* **Learn more:** [GPU Burn on GitHub](https://github.com/wilicc/gpu-burn).

#### Network performance

**Single-Node NCCL**

* Tests NVIDIA Collective Communications Library on a single node.
* Validates GPU-to-GPU communication within the node.
* **Use for:** Multi-GPU training readiness.
* **Learn more:** [NVIDIA NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html).

**InfiniBand Write Bandwidth**

* Measures InfiniBand network write throughput.
* Validates high-speed interconnect performance.
* **Use for:** Distributed training and multi-node workloads.

#### PCIe performance

**NVBandwidth Tests**

* **CPU to GPU Bandwidth:** Host-to-device transfer rates.
* **GPU to CPU Bandwidth:** Device-to-host transfer rates.
* **GPU-CPU Latency:** Data transfer latency.
* **Use for:** Identifying PCIe bottlenecks or degraded lanes.
* **Learn more:** [NVIDIA nvbandwidth documentation](https://github.com/NVIDIA/nvbandwidth).

#### Storage

**Storage Performance**

* Runs storage benchmarks against the shared and local storage volumes available to the cluster.
* Validates data integrity with a checksummed write and read-back, and measures sequential read and write throughput.
* **Use for:** Detecting slow or degraded storage before it bottlenecks data loading or checkpointing.

<Warning>
  **Important: shared storage checks on Kubernetes clusters**

  The shared storage performance check reports a **Skipped** result with the message **"Shared volume PVC not created"** when your cluster is not yet set up to use shared storage.

  To use shared storage, follow the steps in [Shared Storage PVC](/docs/gpu-clusters-management#step-1-create-a-persistentvolumeclaim).
</Warning>

### Understanding test results

Health check results are displayed in the Health Checks table:

* **Status:** Passed (green), Failed (red), or Skipped (gray) indicator.
* **Last Run:** Timestamp of test execution.
* **Node Tested:** Which nodes were included in the test.
* **Details:** Select **View details** to see:
  * Full test output.
  * Detailed metrics and measurements.
  * Workflow CR (Custom Resource) with complete results.
  * Pass/fail criteria details.

### Pass/fail thresholds

Performance-based health checks compare the measured result against a reference value. For bandwidth tests, a test **passes** when the measured value is greater than or equal to the threshold. For latency tests, lower is better, so a test passes when the measured value is less than or equal to the threshold. The following thresholds are the defaults applied during health checks and automatic acceptance testing.

| Test                              | Metric                           | Pass threshold | Test configuration                                                                     |
| --------------------------------- | -------------------------------- | -------------- | -------------------------------------------------------------------------------------- |
| Single-Node NCCL                  | Average bus bandwidth            | ≥ 300 GB/s     | `all_reduce_perf` across 8 GPUs, 32 GiB message size.                                  |
| Multi-Node NCCL                   | Average bus bandwidth            | ≥ 330 GB/s     | `all_reduce_perf` across all GPUs on the selected nodes.                               |
| InfiniBand Write Bandwidth        | Reported write bandwidth         | ≥ 320 Gb/s     | `ib_write_bw` per device, 8 MiB message size, 2-second duration.                       |
| NVBandwidth: CPU to GPU Bandwidth | Per-GPU host-to-device bandwidth | ≥ 30 GB/s      | `host_to_device_memcpy_ce`, averaged across 8 GPUs.                                    |
| NVBandwidth: GPU to CPU Bandwidth | Per-GPU device-to-host bandwidth | ≥ 30 GB/s      | `device_to_host_memcpy_ce`, averaged across 8 GPUs.                                    |
| NVBandwidth: GPU-CPU Latency      | Per-GPU host-device latency      | ≤ 2000 ns      | `host_device_latency_sm`, averaged across 8 GPUs.                                      |
| Storage: Sequential Read          | Bandwidth                        | ≥ 10 GiB/s     | `fio` sequential read, 1 MiB blocks across 8 jobs at iodepth 64, 30-second timed run.  |
| Storage: Sequential Write         | Bandwidth                        | ≥ 5 GiB/s      | `fio` sequential write, 1 MiB blocks across 8 jobs at iodepth 64, 30-second timed run. |

<Note>
  **Units differ by test:** NCCL and NVBandwidth bandwidth thresholds are reported in gigabytes per second (GB/s), while InfiniBand write bandwidth is reported in gigabits per second (Gb/s). The two are not directly comparable (320 Gb/s is roughly 40 GB/s). Latency is reported in nanoseconds (ns).
</Note>

These thresholds are tuned for current GPU node types and may be adjusted over time as hardware and reference baselines change.

### Automatic acceptance testing

When you provision a new GPU cluster, Together automatically runs acceptance tests on each node before making it available for your workloads. This ensures that all nodes meet quality standards before joining your cluster.

#### During cluster provisioning

The cluster provisioning process includes an automatic testing phase:

**Phase: Running Tests**

During this phase, each node undergoes single-node acceptance tests:

* **DCGM Diag Level 2:** Comprehensive GPU diagnostics.
* **5-minute GPU Burn:** Sustained GPU stress test.
* **Single-Node NCCL:** GPU-to-GPU communication validation.
* **Multi-Node NCCL:** GPU-to-GPU communication validation across node GPUs.
* **Storage Performance:** Storage performance validation for storage volumes attached to the cluster.

You'll see the cluster status as:

* **Running Tests:** Acceptance tests are in progress.
* **Tests Failed:** One or more acceptance tests did not pass.
* **Running:** Tests passed and the cluster is ready.

#### Viewing acceptance test results

If acceptance tests fail during provisioning:

1. Navigate to your cluster in the Together Cloud UI.
2. Go to the **Cluster Details** tab.
3. Select the **Health Checks** sub-tab.
4. Find the acceptance test runs for the affected nodes.
5. Select **View details** to see:
   * Which specific test failed (DCGM Diag, GPU Burn, NCCL, or Storage Performance).
   * Detailed error messages and logs.
   * Performance metrics from the tests.

<Note>
  **Automatic remediation:** If acceptance tests fail, Together's infrastructure team is automatically notified and investigates. Nodes that fail acceptance tests are not added to your cluster until the issue is resolved.
</Note>

#### Why acceptance testing matters

Automatic acceptance testing provides several benefits:

* **Quality assurance:** Every node is validated before you can use it.
* **Early detection:** Hardware or configuration issues are caught immediately.
* **Reduced downtime:** Problems are fixed before they impact your workloads.
* **Consistent performance:** All nodes meet the same performance standards.

<Tip>
  **Provisioning time:** Acceptance tests typically add 5-10 minutes to cluster provisioning time, but this ensures you receive fully validated, production-ready nodes.
</Tip>

### When to run active health checks

**Proactive testing:**

* Before deploying critical workloads.
* After cluster scaling events.
* On a regular schedule (weekly or monthly).
* After maintenance windows.

**Reactive testing:**

* When experiencing unexplained job failures.
* Before triggering node repair actions.
* When investigating performance degradation.
* After node repairs to validate fixes.

**Specific issue investigation:**

* **Training instability:** Run GPU Burn and DCGM Diag.
* **Slow data loading:** Run Storage Performance and NVBandwidth tests.
* **Multi-GPU failures:** Run Single-Node NCCL.
* **Distributed training issues:** Run InfiniBand tests.

### Best practices

1. **Schedule workload-free windows:** Health checks require full GPU utilization.
2. **Start with DCGM Diag:** It provides a comprehensive overview of GPU health.
3. **Run baseline tests:** Test new nodes immediately to establish a performance baseline.
4. **Document results:** Keep records of passed tests for comparison.
5. **Test after repair:** Always validate node health after repair actions.
6. **Use appropriate test levels:** Higher DCGM diagnostic levels take longer but are more thorough.

<Warning>
  **Workload impact:** Health checks fully utilize the GPU and can interfere with running workloads. Run tests during maintenance windows or on idle nodes.
</Warning>

## Passive health checks

Passive health checks run continuously on every node in your cluster, observing real workloads, system logs, and GPU metrics in the background. Unlike active checks, passive checks require no manual action and have zero impact on running jobs.

### How passive checks work

Passive checks monitor node telemetry and system logs in real time. There is no synthetic load: the system observes your production traffic and flags degradation as it happens. When an issue is detected, the system creates an internal alert with supporting evidence. If the alert meets repair criteria, a [repair recommendation](/docs/node-repair#auto-node-repair) is generated automatically.

### Detected failure modes

Passive health checks currently detect three categories of failure:

* **GPU fell off the bus:** The GPU becomes unreachable on the PCIe bus, typically caused by a hardware or connector failure. The node can no longer schedule GPU workloads until the GPU is restored.
* **GPU thermal throttling:** Sustained high temperatures cause the GPU to reduce clock speeds. Training throughput and inference latency degrade without any visible error in your application.
* **Fatal Xid errors:** Critical NVIDIA driver errors (for example, Xid 79) that indicate unrecoverable GPU faults. The GPU is unusable until the node is repaired.

<Note>
  The list of detected failure modes is expanding. Future releases will cover additional hardware and software signals.
</Note>

### Active vs. passive checks

* **Active checks:** Run on demand, use synthetic workloads that require full GPU utilization, and validate specific hardware capabilities. Best for targeted diagnostics and pre-deployment validation.
* **Passive checks:** Run continuously with zero overhead, observe real workloads and system logs, and catch degradation as it happens. Best for ongoing monitoring and early detection.

Both types feed into [node repair](/docs/node-repair) recommendations.

## Next steps

<CardGroup>
  <Card title="Node repair" icon="wrench" href="/docs/node-repair">
    Restore unhealthy nodes through automated recommendations or manual repair actions.
  </Card>

  <Card title="Cluster management" icon="server" href="/docs/gpu-clusters-management">
    Manage, monitor, and scale your GPU clusters.
  </Card>
</CardGroup>
