---
title: "Node repair"
source: https://docs.together.ai/docs/node-repair
path: docs/node-repair
---

Restore unhealthy GPU nodes through automated recommendations or manual repair actions.

Node repair restores GPU nodes that [health checks](/docs/health-checks) have flagged as unhealthy. You can repair nodes through two paths: [auto repair](#auto-node-repair), where health checks detect the fault and the system remediates it (after your approval or on its own, depending on the cluster's [confirmation policy](#confirmation-policy)), and [manual repair](#manual-node-repair), where you trigger a repair action directly from the UI.

## Auto node repair

When [passive](/docs/health-checks#passive-health-checks) or [active](/docs/health-checks#active-health-checks) health checks detect a node-level issue, the system generates a repair recommendation and remediates the node. Together handles detection and selects the remediation in every case. The cluster's [confirmation policy](#confirmation-policy) decides whether that recommendation waits for your approval or executes on its own.

### How auto repair works

1. Health checks detect an issue on a node and create an alert with supporting evidence.
2. The system evaluates the alert and generates a repair recommendation with a suggested mode (for example, migrate to new host).
3. The recommendation appears in the **Repairs** tab of your cluster.
4. Under **Approve before repair**, you review the recommendation and approve a repair action. The system marks its suggested action as recommended, but you can override it and approve a different action instead. Under **Fully automatic**, the system auto-approves an in-scope recommendation with no review and runs the recommended action.
5. The system cordons the node so no new work lands on it, then applies the cluster's [wait policy](#control-job-interruption).
6. Together drains the node, executes the remediation action, and rejoins the node to the cluster.

<Note>
  Auto repair accounts for in-flight work. Training jobs need to checkpoint before a node drains, and inference workloads need their replicas rebalanced. Use the [job interruption controls](#control-job-interruption) to give that work time to finish, and under **Approve before repair**, confirm your workloads are ready for the disruption before accepting.
</Note>

### Recommended repair actions

When the system generates a repair recommendation, it selects an action based on the detected issue. Auto repair uses three repair actions, from lightest to heaviest: reboot, quick reprovision, and migrate to new host (see [Available repair actions](#available-repair-actions)). If a lighter action does not clear the issue, it escalates to a heavier one. Some signals are warning-only: they surface an alert for review without an automated repair action.

The detected issues come from [passive health check signals](/docs/health-checks#detected-failure-modes):

| **Detected issue**                | **Signal**                       | **Recommended action**               |
| --------------------------------- | -------------------------------- | ------------------------------------ |
| GPU fell off the bus              | `DmesgGpuFallenOffBus`           | Migrate to new host                  |
| GPU thermal throttling            | `GpuSmClockThermalThrottle`      | Migrate to new host                  |
| High PCIe replay rate             | `GpuPcieReplayRateHigh`          | Migrate to new host                  |
| InfiniBand rails down or degraded | `IBRailsDownOrDegraded`          | Migrate to new host                  |
| InfiniBand link flapping          | `IBLinkFlapping`                 | Migrate to new host                  |
| Fatal platform hardware error     | `NpdCperHardwareErrorFatal`      | Quick reprovision                    |
| Read-only filesystem              | `NpdReadonlyFilesystem`          | Quick reprovision                    |
| XFS shutdown                      | `NpdXfsShutdown`                 | Quick reprovision                    |
| GPU Xid error                     | `DmesgXidError`                  | Reboot (Xid 79 migrates to new host) |
| Uncorrectable ECC error           | `GpuEccDoubleBitError`           | Reboot                               |
| GPU row-remap failure             | `GpuRowRemapFailure`             | Reboot                               |
| Kernel deadlock                   | `NpdKernelDeadlock`              | Reboot                               |
| Frequent kubelet restarts         | `NpdFrequentKubeletRestart`      | Reboot                               |
| Frequent containerd restarts      | `NpdFrequentContainerdRestart`   | Reboot                               |
| Frequent netdev unregister        | `NpdFrequentUnregisterNetDevice` | Reboot                               |
| Node memory pressure              | `KubeNodeMemoryPressure`         | Reboot                               |
| Node PID pressure                 | `KubeNodePIDPressure`            | Reboot                               |
| Node disk pressure                | `KubeNodeDiskPressure`           | Warning                              |
| Slurm node unavailable            | `SlurmNodeUnavailable`           | Warning                              |

<Note>
  Automated recommendations are enabled per cluster and are still expanding. Not every signal above triggers an automated recommendation today. Some raise an internal alert that Together's team reviews first. A recommendation waits for your approval unless the cluster's [confirmation policy](#confirmation-policy) is set to **Fully automatic** and the fault is in scope for automatic execution.
</Note>

### Confirmation policy

The confirmation policy controls whether auto repair pauses for a human. Open your cluster in the [cloud console](https://api.together.ai/clusters), select the **Repairs** tab, and find **Auto-remediation policy**.

| **Confirmation policy** | **Behavior**                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Approve before repair   | Each fault produces a recommendation that waits in the **Repairs** tab. The repair runs after you approve it.                                                                                          |
| Fully automatic         | Faults you have [scoped for automatic execution](#select-which-faults-and-alerts-repair-automatically) are repaired with no approval. Fastest recovery, at the cost of potentially interrupting a job. |

Clusters use **Approve before repair** by default. Detection, recommendation, and execution are identical under both policies. Only the approval step differs.

#### Fully automatic

When you choose **Fully automatic**, the repair loop is handled for you end to end: passive health checks detect the fault, the system generates a repair recommendation, and auto repair executes it with no human approval. Job protection is handled by the wait policy instead of by a review step.

Automatically approved repairs produce the same audit trail as manually approved ones. In the repair details, **Reviewed by** shows Auto-Approved, alongside the alert evidence that triggered the recommendation.

**Fully automatic** is not all-or-nothing. Use **Repair actions** to choose which faults run unattended and which should wait for human approval, and [turn off auto repair for individual nodes](#turn-off-auto-repair-for-individual-nodes) you want to exclude entirely.

The [behavioral details](#behavioral-details) below apply under both policies.

#### Select which faults and alerts repair automatically

Under **Repair actions**, faults are grouped by the repair they trigger: **Migrate to new host**, **Reprovision**, and **VM reboot**. Expand a group to see the individual faults it covers and check them one at a time. **VM reboot** and **Reprovision** correspond to the reboot and quick reprovision actions in [Available repair actions](#available-repair-actions).

Checked faults repair automatically. Unchecked faults wait for approval in the **Repairs** tab. A group with both shows as mixed.

The **Repair actions** list appears under both confirmation policies, so it also works in the other direction: under **Approve before repair**, check specific faults to let them repair automatically while everything else waits for review.

<Warning>
  **Reprovision** and **Migrate to new host** destroy all local VM data. When those groups are checked, they run with no review. Store data on PersistentVolumes, or leave those groups unchecked so they stay gated on approval.
</Warning>

**Remove** is not listed under **Repair actions**. Permanent removal for RMA is always human-initiated and never runs automatically.

#### Turn off auto repair for individual nodes

You can also opt a single node out of auto repair, independent of the cluster's confirmation policy. In the **Nodes** tab, each node has an **Auto Repair** control. Set it to **Disabled** to exclude that node from auto repair while the rest of the cluster keeps the cluster-wide behavior.

Use this to hold a specific node for inspection, for example while debugging a recurring fault you want preserved, without giving up auto repair everywhere else. [Manual repair](#manual-node-repair) remains available for a node that has opted out, and you can re-enable **Auto Repair** on the node at any time.

#### Control job interruption

**Wait for idle** determines whether an approved repair waits for running work to finish. The field below the toggle changes with it.

* **Wait for idle off:** The node is cordoned immediately, the system waits out the **Grace period**, then drains and interrupts whatever is still running, busy or not.

* **Wait for idle on:** The repair holds until the node becomes idle, or until **Maximum wait** expires, whichever comes first. Check **Do not interrupt running jobs** to remove the upper bound and wait indefinitely for the node to go idle.

**Wait for idle** starts on with a two-hour **Maximum wait** when you first configure the policy, and both fields cap at 24 hours. The console shows these controls when **Fully automatic** is selected, but the saved values govern approved repairs under both policies. A cluster that has never saved wait settings waits 30 minutes after approval under **Approve before repair**, and does not wait under **Fully automatic**.

<Note>
  Both fields are in hours and accept fractional values: `0.5` is 30 minutes. Cordoning happens at the start of the wait either way, so no new work lands on a node that is queued for repair.
</Note>

Set the wait to at least your checkpoint interval so a training job can write a checkpoint before the node drains. Enabling **Do not interrupt running jobs** on a cluster running long jobs means a faulty node can stay in service indefinitely. The node is not repaired until the job ends on its own.

#### Choosing a policy

Choose **Fully automatic** when:

* Workloads checkpoint frequently, or are replicated inference deployments that tolerate losing a replica.
* The cluster is large enough that manual review is the bottleneck in mean time to recovery.
* Spare capacity means a node leaving the pool does not block scheduling.

Choose **Approve before repair** when:

* Long-running training jobs checkpoint infrequently.
* The cluster runs at full capacity, so losing a node stalls a job.
* You are debugging a recurring fault and want the node preserved for inspection.

If you want most of the benefit with less exposure, set **Fully automatic** and check only **VM reboot**. Transient faults, the majority by volume, clear without you, and anything that destroys local data still waits for review.

### Override the recommended action

When you review a recommendation, the system marks its suggested action as recommended. You can approve that action, or override it and approve a different action instead. Overriding lets you escalate or de-escalate the repair when you have more context than the automated policy. For example, you can choose migrate to new host instead of a recommended reboot when you suspect a hardware fault.

Overriding applies only to recommendations that wait for review, so a recommendation that runs automatically under **Fully automatic** executes its recommended action with no opportunity for override.

The review shows the health check failures that triggered the recommendation alongside the four repair actions:

* **Reboot:** Restart the VM in place on the same host.
* **Quick reprovision:** Recreate the VM on the same physical host.
* **Migrate to new host:** Provision a new VM on different physical hardware.
* **Remove:** Permanently remove the node for RMA.

Select an action to see its workload impact and an optional reason field, then confirm. Approving the recommended action runs the suggested repair. Selecting any other action overrides the recommendation and runs that repair instead.

See [Available repair actions](#available-repair-actions) for guidance on when to use each action. You can also approve a recommendation from the command line with [`tg beta clusters remediations approve`](/reference/cli/clusters#approve-a-node-remediation), which exposes the same actions through its `--mode` flag.

### Behavioral details

* **Auto-resolution mid-approval:** Recommendations can disappear if the underlying alert clears before you accept (5-minute default CompactTTL).
* **Cooldown window:** After a repair completes (succeeded, failed, or cancelled), no new recommendation is generated for \~30 minutes on the same node.
* **Mode escalation:** A pending recommendation can change its suggested mode in-place if a higher-severity failure is detected while it's waiting in the queue.

### The Repairs tab

To view repair recommendations and history:

1. Navigate to your cluster in the [cloud console](https://api.together.ai/clusters).
2. Select the **Repairs** tab.

The Repairs table shows all repair events with the following columns:

* **Node:** The affected node name.
* **State:** The current status of the repair. Values include Auto Resolved (issue resolved before action was taken), Succeeded (repair completed), and in-progress states.
* **Mode:** The remediation action (for example, Migrate to new host).
* **Trigger:** How the repair was initiated. Automated (generated by health checks) or Manual (triggered by a user). Automatically approved repairs show Auto-Approved in the repair's **Reviewed by** field.
* **Created:** When the repair recommendation was generated.

### Repair details

Select any row in the Repairs table to view the full repair details:

* **Node:** The affected node name.
* **State:** The current repair state (for example, Succeeded).
* **Mode:** The remediation action taken.
* **Created / Started:** When the recommendation was generated and when the repair execution began.
* **Requested by:** The source that initiated the repair. For auto repairs, this shows Together Health Checker.
* **Reviewed by:** Who approved the repair (your user name or Auto-Approved for auto-approved repairs).
* **Review time:** When the repair was approved.
* **Review comment:** Any notes from the approval (for example, "auto-approved: approved").
* **Repair ID:** Unique identifier for tracking and support requests.
* **Alert evidence:** Expandable section showing the underlying alerts that triggered the recommendation, including failure type and affected hardware.

### Linked alerts in API responses

When you retrieve or list remediations through the API, the `linked_alerts` field includes the passive health check alerts tied to that repair, including alerts that have already resolved. Each entry has:

* `passive_health_check_alert_id`: Alert UUID.
* `alert_name`: Alertmanager alert name.
* `severity`: `PHC_SEVERITY_INFO`, `PHC_SEVERITY_WARNING`, or `PHC_SEVERITY_CRITICAL`.
* `started_at` and `resolved_at`: When the alert fired and cleared (`resolved_at` is empty while the alert is still firing).
* `target_vm`: VM name from the alert labels.
* `annotations`: Alertmanager annotation key-value pairs.
* `cluster_id`: Cluster UUID the alert was raised against.
* `instance_id`: Resolved instance UUID (empty until the alert is joined to an instance).
* `node_remediation_intent_id`: Remediation intent UUID attached to the alert, if any.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  remediation = client.beta.clusters.remediations.retrieve(
      "<REMEDIATION_ID>",
      cluster_id="<CLUSTER_ID>",
      instance_id="<INSTANCE_ID>",
  )
  for alert in remediation.linked_alerts or []:
      print(alert.alert_name, alert.severity, alert.started_at)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const remediation = await client.beta.clusters.remediations.retrieve(
    "<REMEDIATION_ID>",
    { instance_id: "<INSTANCE_ID>", cluster_id: "<CLUSTER_ID>" },
  );
  for (const alert of remediation.linked_alerts ?? []) {
    console.log(alert.alert_name, alert.severity, alert.started_at);
  }
  ```
</CodeGroup>

## Manual node repair

When you encounter node problems or want to trigger a repair without waiting for an automated recommendation, you can start a repair directly from the Worker Nodes UI.

### How to trigger manual repair

1. Navigate to your cluster in the [cloud console](https://api.together.ai/clusters).
2. Go to the **Worker Nodes** section.
3. Find the problematic node.
4. Select the **⋮** (three dots) menu in the **State** column.
5. Select **Repair** from the dropdown.
6. A repair dialog appears showing:
   * Node details (name, GPU configuration).
   * Issue detected (if applicable).
   * Impact warning.
7. Choose one of the repair actions:
   * **Reboot:** For transient software issues (preserves local data).
   * **Quick reprovision:** For persistent software issues.
   * **Migrate to new host:** For hardware issues.
   * **Remove:** Permanently removes the node for RMA (return merchandise authorization).
   * **Report an issue** (optional): To notify support.

The repair process begins immediately and the node rejoins your cluster once complete.

### Available repair actions

**Reboot**

Reboots the VM in place on the same physical host.

* **When to use:** Transient software issues (GPU driver hangs, stuck processes, kernel-level errors) where a restart is likely to clear the problem.
* **What happens:** The node follows the Cordon → Drain → Reboot → Rejoin lifecycle. The VM restarts on the same physical hardware without reimaging. Local scratch and temporary data on `/scratch` and `/tmp` is preserved.

<Note>
  Reboot is the lightest repair action. Because the VM is not reimaged, it is faster than a reprovision and preserves local data. Try a reboot first for transient issues before escalating to a reprovision.
</Note>

**Quick reprovision**

Reprovisions the GPU node VM on the same underlying physical host.

* **When to use:** Persistent software-level issues (driver crashes, library corruption), VM configuration problems, or application-level issues that a reboot did not resolve.
* **What happens:** The node follows the Cordon → Drain → Reprovision lifecycle. The VM is recreated with a fresh software stack and rejoins the cluster automatically.

<Warning>
  You lose all local VM data during reprovision. Store data on PersistentVolumes or back it up before proceeding. No new jobs are scheduled on this node until remediation completes.
</Warning>

**Migrate to new host**

Provisions a new VM on a different underlying physical host.

* **When to use:** Hardware-level issues (GPU failures, PCIe problems), issues that persist after a quick reprovision, or physical component failures.
* **What happens:** The node follows the Cordon → Drain → Migrate lifecycle. A new VM is created on different physical hardware with different GPUs assigned, and rejoins the cluster automatically.

<Warning>
  You lose all local VM data during migration. Store data on PersistentVolumes or back it up before proceeding. No new jobs are scheduled on this node until remediation completes.
</Warning>

**Remove**

Permanently removes the node from the cluster. The cluster node count drops below the desired count.

* **When to use:** Faulty GPU hardware that needs to be returned to the provider for RMA. Use this when the node has a confirmed hardware defect that cannot be resolved by migration.
* **What happens:** The node follows the Cordon → Drain lifecycle, then is permanently removed from the cluster. The node is not replaced automatically.

<Warning>
  Removing a node is irreversible from the cluster's perspective. The node is taken out of service entirely and your cluster runs with fewer nodes until a replacement is provisioned. Only use this for confirmed hardware failures that require physical RMA.
</Warning>

**Report an issue**

Use this option if:

* You are unsure which repair action to use.
* You want Together support to investigate before taking action.
* The issue requires additional context or diagnosis.

## Repair lifecycle

Both auto and manual repairs follow the same lifecycle:

```text theme={null}
Cordon → Drain → Reboot/Reprovision/Migrate/Remove → Rejoin (or permanent removal)
```

**Cordon:** The node is marked as unschedulable. No new workloads are placed on the node, but existing workloads continue running.

**Drain:** Running workloads are gracefully terminated and pods are evicted from the node.

**Reboot/Reprovision/Migrate:**

* **Reboot:** The VM restarts in place on the same hardware. Local `/scratch` and `/tmp` data is preserved.
* **Quick reprovision:** The VM is recreated on the same physical host. Local data is lost.
* **Migrate to new host:** A new VM is created on different physical hardware. Local data is lost.
* **Remove:** The node is permanently removed from the cluster for RMA. No rejoin occurs.

**Rejoin:** The node automatically rejoins the cluster, becomes schedulable, and is ready to accept new workloads.

You can monitor repair progress in the **Repairs** tab (for auto repairs) or the **Worker Nodes** section (for manual repairs). The node progresses through these states: Cordoning → Draining → Repairing/Migrating → Joining → Running.

## Choosing a repair action

Use this table to determine which repair action fits your issue. Start with the lightest action (reboot) and escalate if the issue persists.

| **Issue type**                         | **Reboot**  | **Reprovision**   | **Migrate to new host** |
| -------------------------------------- | ----------- | ----------------- | ----------------------- |
| **GPU driver hang**                    | ✓ Try first | ✓ If reboot fails |                         |
| **Stuck GPU processes**                | ✓ Try first | ✓ If reboot fails |                         |
| **GPU watchdog timeouts**              | ✓ Try first | ✓ If reboot fails |                         |
| **Stuck GPU contexts**                 | ✓ Try first | ✓ If reboot fails |                         |
| **Recoverable Xid errors**             | ✓ Try first | ✓ If reboot fails |                         |
| **Application memory leaks**           | ✓ Try first | ✓ If reboot fails |                         |
| **Software-based throttling**          | ✓ Try first | ✓ If reboot fails |                         |
| **Driver crashes/corruption**          |             | ✓ Yes             |                         |
| **CUDA/ROCm library issues**           |             | ✓ Yes             |                         |
| **Incorrect GPU mode settings**        |             | ✓ Yes             |                         |
| **GPU not attached to VM**             |             | ✓ Yes             |                         |
| **Device permissions/cgroup issues**   |             | ✓ Yes             |                         |
| **NUMA affinity problems**             |             | ✓ Yes             |                         |
| **Single-bit ECC errors (occasional)** |             | ✓ Yes             |                         |
| **Complete GPU card failure**          |             |                   | ✓ Yes                   |
| **Persistent multi-bit ECC errors**    |             |                   | ✓ Yes                   |
| **GPU falling off PCIe bus**           |             |                   | ✓ Yes                   |
| **Fan failures**                       |             |                   | ✓ Yes                   |
| **PCIe lane degradation**              |             |                   | ✓ Yes                   |
| **Power delivery (VRM) issues**        |             |                   | ✓ Yes                   |
| **Thermal/cooling problems**           |             |                   | ✓ Yes                   |
| **Persistent Xid errors**              |             |                   | ✓ Yes                   |
| **Physical connector damage**          |             |                   | ✓ Yes                   |
| **Backplane/riser issues**             |             |                   | ✓ Yes                   |

<Note>
  Escalation path: reboot → reprovision → migrate to new host. If the issue persists after reprovisioning the VM to a fresh instance on the same physical GPU, it is a hardware problem requiring migration to a new host.
</Note>

## Best practices

**Before triggering a repair:**

* Store important data on PersistentVolumes, not local storage.
* Optionally drain workloads manually for more control over migration.
* Document symptoms for troubleshooting if the repair does not resolve the problem.
* Check running jobs so you know what will be interrupted.

**Choosing the right action:**

* **Start with reboot:** It is the fastest option, preserves local data, and resolves most transient software issues.
* **Escalate to quick reprovision:** When a reboot did not fix the issue, or the problem is a corrupted driver, library, or VM configuration that requires a fresh software stack.
* **Use migrate to new host:** When reprovision did not fix the issue, you see hardware error indicators (ECC errors, Xid errors, thermal warnings), or GPU diagnostics show hardware problems.

**After a repair:**

* Verify the node shows as Running in the cluster.
* Run a GPU workload to confirm operation.
* Monitor for recurrence of the same issue.
* Check GPU metrics to confirm normal operation.

## Common diagnostic commands

Before triggering a repair, you can SSH into the node to diagnose issues:

```bash theme={null}
# Check GPU status
nvidia-smi

# Check for Xid errors in system logs
sudo dmesg | grep -i xid

# Check GPU memory errors
nvidia-smi -q | grep -i ecc

# Check GPU temperature and throttling
nvidia-smi -q | grep -E 'Temperature|Throttle'

# Check PCIe link status
nvidia-smi -q | grep -E 'Link Width|Link Speed'

# Check running processes on GPU
nvidia-smi pmon

# Detailed GPU query
nvidia-smi -q
```

[Learn how to SSH into nodes →](/docs/gpu-clusters-management#direct-ssh-access)

## When to contact support

Contact [support@together.ai](mailto:support@together.ai) if:

* Issues persist after all repair actions.
* You see repeated failures on multiple nodes.
* You need help diagnosing whether an issue is software or hardware.
* Repair actions fail to complete.
* You are unsure which repair action to use.
* The node does not rejoin after repair completes.

Alternatively, use the **Report an issue** button in the repair dialog to notify support directly.

## Next steps

<CardGroup>
  <Card title="Health checks" icon="activity-heartbeat" href="/docs/health-checks">
    Monitor node health with active diagnostic tests and continuous passive monitoring.
  </Card>

  <Card title="Cluster management" icon="server" href="/docs/gpu-clusters-management">
    Manage, monitor, and scale your GPU clusters.
  </Card>
</CardGroup>
