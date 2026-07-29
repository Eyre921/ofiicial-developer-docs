---
title: "Clusters"
source: https://docs.together.ai/reference/cli/clusters
path: reference/cli/clusters
---

Reserve, configure, and manage GPU clusters from your terminal.

<Info>
  GPU clusters are a beta feature. Behavior, flags, and supported hardware can change. Reach out to your Together AI contact or [contact sales](https://www.together.ai/contact-sales) with feedback.
</Info>

## Create a cluster

```bash theme={null}
tg beta clusters create
```

### Parameters

| Flag                                   | Description                                                                                                                                                                                                                                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--name [string]`                      | Name for the cluster.                                                                                                                                                                                                                                                                                      |
| `--num-gpus [integer]`                 | Number of GPUs to allocate in the cluster.                                                                                                                                                                                                                                                                 |
| `--region [string]`                    | Region to create the cluster in. Valid regions can be found with `tg beta clusters list-regions`.                                                                                                                                                                                                          |
| `--billing-type [ON_DEMAND\|RESERVED]` | Cluster reservation approach.<br /><br /><ul><li>`ON_DEMAND` begins billing the moment the cluster is created. Billing continues until you delete the cluster.</li><li>`RESERVED` starts billing immediately. The cluster is automatically torn down after the `--duration-days` length elapses.</li></ul> |
| `--nvidia-driver-version [string]`     | NVIDIA driver version. Valid versions can be found with `tg beta clusters list-regions`.                                                                                                                                                                                                                   |
| `--cuda-version [string]`              | CUDA version. Valid versions can be found with `tg beta clusters list-regions`.                                                                                                                                                                                                                            |
| `--duration-days [number]`             | Only used with `RESERVED` billing. Specifies how many days the cluster is reserved for.                                                                                                                                                                                                                    |
| `--gpu-type [string]`                  | GPU type to use for the cluster. One of `H100_SXM`, `H200_SXM`, `RTX_6000_PCI`, `L40_PCIE`, `B200_SXM`, `H100_SXM_INF`. Available types vary by region; see `tg beta clusters list-regions`.                                                                                                               |
| `--cluster-type [KUBERNETES\|SLURM]`   | Cluster workload manager or orchestrator.                                                                                                                                                                                                                                                                  |
| `--volume [string]`                    | Storage volume ID to attach to the cluster. List existing volumes with `tg beta clusters storage list`.                                                                                                                                                                                                    |
| `--num-reserved-gpus [integer]`        | Number of prepaid reserved GPUs. When omitted for `RESERVED` billing, defaults to `num_gpus`.                                                                                                                                                                                                              |
| `--headlamp-addon`                     | Enable the Headlamp Kubernetes dashboard add-on.                                                                                                                                                                                                                                                           |
| `--slurm-web-addon`                    | Enable the Slurm Web add-on.                                                                                                                                                                                                                                                                               |

<Note>
  Run `tg beta clusters create` with no flags to launch an interactive prompt that walks through the required fields. Pass `--non-interactive` (or `--json`) to skip prompts in CI.
</Note>

## Update a cluster

```bash theme={null}
tg beta clusters update [CLUSTER_ID]
```

### Parameters

| Flag                                 | Description                                                                                 |
| ------------------------------------ | ------------------------------------------------------------------------------------------- |
| `--num-gpus [integer]`               | Number of GPUs to allocate in the cluster.                                                  |
| `--cluster-type [KUBERNETES\|SLURM]` | Cluster workload manager or orchestrator.                                                   |
| `--num-reserved-gpus [integer]`      | Number of reserved GPUs to update to. Only applicable for clusters with `RESERVED` billing. |
| `--num-capacity-pool-gpus [integer]` | Desired number of capacity pool GPUs. Must be a multiple of 8 and cannot exceed `num_gpus`. |
| `--num-preemptible-gpus [integer]`   | Desired number of preemptible GPUs for the cluster.                                         |
| `--headlamp/--no-headlamp`           | Enable or disable the Headlamp Kubernetes dashboard add-on.                                 |
| `--slurm-web/--no-slurm-web`         | Enable or disable the Slurm Web add-on.                                                     |

## Retrieve a cluster

```bash theme={null}
tg beta clusters retrieve [CLUSTER_ID]
```

## Delete a cluster

```bash theme={null}
tg beta clusters delete [CLUSTER_ID]
```

## List clusters

```bash theme={null}
tg beta clusters list
```

## List regions

Get configuration information per region for creating a GPU cluster.

```bash theme={null}
tg beta clusters list-regions
```

### Example output

```json theme={null}
{
  "regions": [
    {
      "driver_versions": [
        {
          "cuda_version": "12.9",
          "nvidia_driver_version": "575"
        },
        {
          "cuda_version": "12.8",
          "nvidia_driver_version": "570"
        },
        {
          "cuda_version": "13.1",
          "nvidia_driver_version": "590"
        },
        {
          "cuda_version": "13.1",
          "nvidia_driver_version": "580"
        }
      ],
      "name": "us-central-8",
      "supported_instance_types": [
        "H100_SXM",
        "H200_SXM"
      ]
    }
  ]
}
```

## SSH into a cluster

SSH into a Slurm cluster using a short-lived OIDC-signed certificate. The command opens your browser to sign in, requests a certificate from the cluster's certificate authority, and connects through the bastion host. No API key or long-lived SSH key is required.

<Note>
  Requires Together CLI 2.20+ and [Python 3.10+](https://www.python.org/). Check your version with `tg --version`. To install or upgrade, see [Get started](/reference/cli/getting-started#install-the-together-cli).
</Note>

```bash theme={null}
tg beta clusters ssh https://dex.<REGION>.cloud.together.ai/<CLUSTER_ID> --login <LOGIN>
```

Copy the Dex issuer URL and login name from the cluster UI when **OIDC** is selected as the SSH access method.

### Parameters

| Flag                   | Description                                                                                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEX_URL` (positional) | Cluster Dex issuer URL: `https://dex.<BASE>/<CLUSTER_ID>`. **required**                                                                                                     |
| `--login`, `-l`        | POSIX login or SSH username on the cluster. **required**                                                                                                                    |
| `--host`               | Target host reachable through the bastion. Default: `slurm-login`. For compute nodes, pass the node hostname shown in the UI (for example, `worker-1.slurm-compute.slurm`). |
| `--client-id`          | Dex public client ID. Default: `together-cli`.                                                                                                                              |
| `--scope`              | OIDC scopes. Default: `openid email`.                                                                                                                                       |
| `--key-type`           | Ephemeral key type (`ecdsa` or `ed25519`). Default: `ecdsa`.                                                                                                                |
| `--ca-root`            | step-ca root certificate (PEM) for TLS verification.                                                                                                                        |
| `--cache`              | Cache SSH keys and certificates while valid. Default: `true`.                                                                                                               |
| `--refresh`            | Force refresh the cached SSH certificate.                                                                                                                                   |
| `--cache-dir`          | Directory for cached SSH keys and certificates.                                                                                                                             |
| `--print-ssh-command`  | Print the underlying `ssh` command instead of executing it.                                                                                                                 |
| `--ssh-config-alias`   | Print an `ssh_config` Host entry for this alias instead of executing `ssh`.                                                                                                 |
| `--write-ssh-config`   | Write or update the alias in `~/.together/ssh/config` and include it from `~/.ssh/config`. Requires `--ssh-config-alias`.                                                   |

<Note>
  Any arguments after `DEX_URL` are passed through to `ssh` as a remote command.
</Note>

<Note>
  On the bastion-to-target hop, the CLI disables SSH host key verification (`StrictHostKeyChecking=no`). Cluster hosts are reprovisioned frequently, so their host keys are not pinned. Authentication uses the short-lived step-ca user certificate from the OIDC flow, not the target host key.
</Note>

## Get cluster credentials

Download the cluster's configuration and credentials to your local `.kube/config` file to manage Kubernetes resources.

```bash theme={null}
tg beta clusters get-credentials [CLUSTER_ID]
```

### Parameters

| Flag                      | Description                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `--file [Path\|-]`        | Override the path to write the kubeconfig to. Pass `-` to print the config to stdout instead of writing to a file. Default: `~/.kube/config`. |
| `--context-name [string]` | Name of the context to add to the kubeconfig. Defaults to the cluster name.                                                                   |
| `--overwrite-existing`    | If there is a conflict with the existing kubeconfig, overwrite it instead of raising an error.                                                |
| `--set-default-context`   | Change the current context for `kubectl` to the new context.                                                                                  |

## Approve a node remediation

Approve a pending [node repair](/docs/node-repair) remediation. Find pending remediations and their IDs in the **Repairs** tab of your cluster in the Together Cloud UI.

```bash theme={null}
tg beta clusters remediations approve [REMEDIATION_ID]
```

### Parameters

| Flag                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--comment [string]`                                                 | Comment explaining the approval.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `--mode [VM_ONLY\|HOST_AWARE\|EVICT_WITHOUT_REPLACEMENT\|REBOOT_VM]` | Remediation mode to apply after approval. When omitted, the remediation keeps its existing mode.<br /><br /><ul><li>`VM_ONLY` deletes the VM and provisions a new one on the same host (quick reprovision).</li><li>`HOST_AWARE` cordons the host, deletes the VM, and provisions a new one on a different host (migrate to new host).</li><li>`EVICT_WITHOUT_REPLACEMENT` evicts the VM without provisioning a replacement (remove).</li><li>`REBOOT_VM` reboots the VM in place (reboot).</li></ul> |

## Create cluster storage

```bash theme={null}
tg beta clusters storage create
```

### Parameters

| Flag                     | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| `--region [string]`      | Region to create the storage volume in. **required** |
| `--size-tib [integer]`   | Size of the storage volume in TiB. **required**      |
| `--volume-name [string]` | Name for the storage volume. **required**            |

## Retrieve cluster storage

```bash theme={null}
tg beta clusters storage retrieve [VOLUME_ID]
```

## List cluster storage

```bash theme={null}
tg beta clusters storage list
```

## Delete cluster storage

```bash theme={null}
tg beta clusters storage delete [VOLUME_ID]
```
