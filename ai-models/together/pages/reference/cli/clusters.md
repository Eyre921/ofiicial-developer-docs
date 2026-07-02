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

<Note>
  Run `tg beta clusters create` with no flags to launch an interactive prompt that walks through the required fields. Pass `--non-interactive` (or `--json`) to skip prompts in CI.
</Note>

## Update a cluster

```bash theme={null}
tg beta clusters update [CLUSTER_ID]
```

### Parameters

| Flag                                 | Description                                |
| ------------------------------------ | ------------------------------------------ |
| `--num-gpus [integer]`               | Number of GPUs to allocate in the cluster. |
| `--cluster-type [KUBERNETES\|SLURM]` | Cluster workload manager or orchestrator.  |

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
