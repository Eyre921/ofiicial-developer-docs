---
title: "Microsoft Azure"
source: https://developers.deepgram.com/docs/azure-k8s.md
path: docs/azure-k8s
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Microsoft Azure

> Deploy Deepgram self-hosted on Azure Kubernetes Service (AKS) with NVIDIA GPU node pools, Azure Files NFS model storage, and the deepgram-self-hosted Helm chart.

Deploying Deepgram on Microsoft Azure requires some preparation. In this guide, you'll provision an Azure Kubernetes Service (AKS) cluster with an NVIDIA GPU node pool, create shared storage for Deepgram model files, and install Deepgram with the official Helm chart. You'll run every step in your local terminal with the Azure CLI.

## Prerequisites

Make sure you've completed the requirements in the [Self-Hosted Introduction](/docs/self-hosted-introduction).

### Choose a GPU VM size

Deepgram Engine requires a dedicated NVIDIA GPU, and the GPU you choose determines which models you can run. Pick the VM size before you create the cluster.

* [Model and GPU Compatibility](/docs/self-hosted-deployment-environments#model-and-gpu-compatibility) is the source of truth for which Deepgram models (Nova-3, Nova-2, Aura-2, Flux STT, and Flux TTS) run on which NVIDIA GPUs.
* [Hardware Specifications](/docs/self-hosted-deployment-environments#hardware-specifications) lists the CPU, memory, and storage each Engine needs.
* Every supported GPU requires NVIDIA driver `>=580` with the **open** kernel modules. See [Drivers and Containerization Platforms](/docs/drivers-and-containerization-platforms).

This table maps the Azure VM series that ship NVIDIA CUDA drivers to those compatibility rules.

| Azure VM series | Example size               | GPU                         | Nova-3, Nova-2 | Aura-2 | Flux STT | Flux TTS |
| --------------- | -------------------------- | --------------------------- | :------------: | :----: | :------: | :------: |
| NCasT4_v3       | `Standard_NC8as_T4_v3`     | 1 × NVIDIA T4 (16 GB)       |        ✅       |    ✅   |     ❌    |     ❌    |
| NVadsA10_v5     | `Standard_NV36ads_A10_v5`  | 1 × NVIDIA A10 (24 GB)      |        ✅       |    ✅   |     ✅    |     ❌    |
| NC A100 v4      | `Standard_NC24ads_A100_v4` | 1 × NVIDIA A100 (80 GB)     |        ✅       |    ✅   |     ✅    |     ✅    |
| NCads H100 v5   | `Standard_NC40ads_H100_v5` | 1 × NVIDIA H100 NVL (94 GB) |        ✅       |    ✅   |     ✅    |     ✅    |

VM size names and GPU counts change as Azure adds series. To confirm a size is available in your region, run `az vm list-skus --location <your-region> --size Standard_NC --output table`, and check Microsoft's [GPU-optimized VM sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu) for current details.

### Request GPU quota

New Azure subscriptions often have no quota for GPU VM families, and GPU capacity is limited in many regions. Request a vCPU quota increase for your chosen VM family in your target region before you create the cluster. Follow the steps in [Requesting Quotas for NVIDIA GPUs](/docs/azure-docker-podman#requesting-quotas-for-nvidia-gpus).

### Azure CLI

The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) provides programmatic access to manage your Azure services. Many of the same actions are available in the Azure portal.

1. Follow the [installation guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) to install the CLI locally. You need version `2.72.2` or later, which adds the `--gpu-driver` option this guide uses.

2. Sign in and select the subscription to bill for this cluster.

   **`Shell`**

   ```shell Shell
   az login
   az account set --subscription "YOUR_SUBSCRIPTION_ID_OR_NAME"
   ```

> **Info**
>
> ## Choosing a region
>
> This guide provisions resources in the Azure `westus2` region. To deploy to a different region, change the `LOCATION` variable and confirm that your chosen GPU VM family is available there.

### `kubectl`

The Kubernetes command-line tool, `kubectl`, runs commands against Kubernetes clusters. You can use `kubectl` to deploy applications, inspect and manage cluster resources, and view logs.

Install it with the [official Kubernetes guides](https://kubernetes.io/docs/tasks/tools/#kubectl), or run `az aks install-cli`.

### Kubernetes packages with `helm`

[Helm](https://helm.sh/) is the package manager for Kubernetes. A Helm chart defines a Kubernetes application so you can install and upgrade it. This guide uses Helm to install Deepgram and the NVIDIA GPU Operator. See the [installation guide](https://helm.sh/docs/intro/install/) for details on how to install it locally.

## Create a cluster

Azure Kubernetes Service (AKS) is a managed Kubernetes service. AKS manages the availability and scalability of the Kubernetes control plane that schedules containers, manages application availability, and stores cluster data.

1. Set the variables this guide reuses, then create a resource group and an AKS cluster. The cluster starts with a small system node pool. You'll add node pools for each Deepgram component next.

   **`Shell`**

   ```shell Shell
   RESOURCE_GROUP=deepgram-self-hosted
   CLUSTER_NAME=deepgram-self-hosted
   LOCATION=westus2
   ENGINE_VM_SIZE=Standard_NC24ads_A100_v4 # Replace with the GPU VM size you chose

   az group create \
       --name $RESOURCE_GROUP \
       --location $LOCATION

   az aks create \
       --resource-group $RESOURCE_GROUP \
       --name $CLUSTER_NAME \
       --node-count 1 \
       --node-vm-size Standard_D4s_v5 \
       --enable-cluster-autoscaler \
       --min-count 1 \
       --max-count 3 \
       --generate-ssh-keys

   az aks get-credentials \
       --resource-group $RESOURCE_GROUP \
       --name $CLUSTER_NAME
   ```

2. Create a separate node pool for each Deepgram component (API, License Proxy, Engine). Adjust the VM sizes and node counts to your needs. You may wish to consult your Deepgram Account Representative when you plan your cluster's capacity.

   **`Shell`**

   ```shell Shell
   az aks nodepool add \
       --resource-group $RESOURCE_GROUP \
       --cluster-name $CLUSTER_NAME \
       --name apipool \
       --node-vm-size Standard_D8s_v5 \
       --node-count 1 \
       --enable-cluster-autoscaler \
       --min-count 1 \
       --max-count 3 \
       --labels k8s.deepgram.com/node-type=api

   az aks nodepool add \
       --resource-group $RESOURCE_GROUP \
       --cluster-name $CLUSTER_NAME \
       --name lpool \
       --node-vm-size Standard_D4s_v5 \
       --node-count 1 \
       --enable-cluster-autoscaler \
       --min-count 1 \
       --max-count 2 \
       --labels k8s.deepgram.com/node-type=license-proxy

   az aks nodepool add \
       --resource-group $RESOURCE_GROUP \
       --cluster-name $CLUSTER_NAME \
       --name enginepool \
       --node-vm-size $ENGINE_VM_SIZE \
       --node-count 1 \
       --enable-cluster-autoscaler \
       --min-count 1 \
       --max-count 8 \
       --gpu-driver none \
       --labels k8s.deepgram.com/node-type=engine
   ```

   > **Warning**
   >
   > ## Skip the AKS GPU driver install
   >
   > AKS can install an NVIDIA driver for you, but AKS selects the driver version. Deepgram requires driver `>=580` with the open kernel modules, so create the Engine node pool with `--gpu-driver none`. The `deepgram-self-hosted` Helm chart then installs a compliant driver with the [NVIDIA GPU Operator](https://learn.microsoft.com/en-us/azure/aks/nvidia-gpu-operator). Don't use `--enable-managed-gpu` on this node pool.
   >
   > You can only set `--gpu-driver` when you create a node pool. To change it later, create a new node pool.

3. Create a dedicated namespace for Deepgram resources.

   **`Shell`**

   ```shell Shell
   kubectl create namespace dg-self-hosted
   kubectl config set-context --current --namespace=dg-self-hosted
   ```

## Configure persistent storage

Deepgram Engine pods read model files from a shared volume. The Helm chart can download models automatically only for Amazon EFS, so on AKS you create an [Azure Files](https://learn.microsoft.com/en-us/azure/aks/create-volume-azure-files) NFS share, populate it from inside the cluster with a one-shot Kubernetes Job, and point the chart at the resulting `PersistentVolumeClaim`.

> **Info**
>
> Azure Files NFS shares need a Premium (SSD) storage account and network access from your cluster's subnet. Review the [NFS prerequisites](https://learn.microsoft.com/en-us/azure/aks/create-volume-azure-files#prerequisites-for-using-nfs-shares-with-azure-files) before you continue. If the AKS identity lacks the required roles, volume creation or mounting fails.

1. Create a `StorageClass` for NFS shares. The `Retain` reclaim policy keeps your model files if you delete the claim later.

   **`Shell`**

   ```shell Shell
   cat <<'EOF' | kubectl apply -f -
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: dg-models-nfs
   provisioner: file.csi.azure.com
   reclaimPolicy: Retain
   allowVolumeExpansion: true
   parameters:
     protocol: nfs
     skuName: Premium_LRS
   mountOptions:
     - nconnect=4
     - noresvport
     - actimeo=30
   EOF
   ```

2. Create a `PersistentVolumeClaim` for the models. Premium file shares have a 100 GiB minimum size.

   **`Shell`**

   ```shell Shell
   cat <<'EOF' | kubectl apply -f -
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: dg-model-storage
     namespace: dg-self-hosted
   spec:
     accessModes:
       - ReadWriteMany
     storageClassName: dg-models-nfs
     resources:
       requests:
         storage: 100Gi
   EOF
   kubectl get pvc dg-model-storage
   ```

   The claim should reach the `Bound` status within a few minutes.

3. Run a one-shot `Job` that mounts the claim and downloads the model files provided by your Deepgram Account Representative.

   > **Info**
   >
   > Replace the `wget` lines below with the model URLs supplied by your Deepgram Account Representative.

   **`Shell`**

   ```shell Shell
   cat <<'EOF' | kubectl apply -f -
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: dg-model-downloader
     namespace: dg-self-hosted
   spec:
     backoffLimit: 3
     template:
       spec:
         restartPolicy: Never
         containers:
           - name: downloader
             image: alpine:3
             command: ["sh", "-c"]
             args:
               - |
                 set -eu
                 apk add --no-cache wget ca-certificates
                 cd /mnt/models
                 # Replace these with the model URLs from your Deepgram Account Representative.
                 wget -c https://link-to-model-1.dg
                 wget -c https://link-to-model-2.dg
                 # ... continue for all model files
             volumeMounts:
               - name: models
                 mountPath: /mnt/models
         volumes:
           - name: models
             persistentVolumeClaim:
               claimName: dg-model-storage
   EOF
   ```

4. Wait for the Job to complete, then delete it. The claim and the model files remain.

   **`Shell`**

   ```shell Shell
   kubectl wait --namespace dg-self-hosted --for=condition=complete job/dg-model-downloader --timeout=30m
   kubectl logs --namespace dg-self-hosted job/dg-model-downloader
   kubectl delete --namespace dg-self-hosted job dg-model-downloader
   ```

## Configure Kubernetes Secrets

Deepgram strongly recommends following [best practices for configuring Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/). Refer to [Securing Your Cluster](/docs/securing-your-cluster) for more details.

The `deepgram-self-hosted` Helm chart takes two Secret references. One is a set of distribution credentials that allow the cluster to pull images from Deepgram's container image repository. The other is your self-hosted API key that licenses each Deepgram container that's created.

1. Complete the [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) guide to generate distribution credentials and a self-hosted API key.

2. If you use an external Secret store provider, such as Azure Key Vault, configure cluster access to these two Secrets, and name them `dg-regcred` (distribution credentials) and `dg-self-hosted-api-key`.

3. If you don't use an external Secret store provider, create the Secrets manually in your cluster.

   1. Using the distribution credentials username and password generated in the Deepgram Console, create a Kubernetes Secret named `dg-regcred`.

      ```shell Shell
      kubectl create secret docker-registry dg-regcred \
          --docker-server=quay.io \
          --docker-username='QUAY_DG_USER' \
          --docker-password='QUAY_DG_PASSWORD'
      ```

      > **Info**
      >
      > Replace the placeholders `QUAY_DG_USER` and `QUAY_DG_PASSWORD` with the distribution credentials you generated in the [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) guide.

   2. Create a Kubernetes Secret named `dg-self-hosted-api-key` to store your self-hosted API key.

      ```shell Shell
      kubectl create secret generic dg-self-hosted-api-key \
          --from-literal=DEEPGRAM_API_KEY='YOUR_API_KEY_HERE'
      ```

      > **Info**
      >
      > Replace the placeholder `YOUR_API_KEY_HERE` with the Deepgram API key you generated in the [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) guide.

## Deploy Deepgram

Deepgram maintains the official `deepgram-self-hosted` Helm chart. You can reference the [source](https://github.com/deepgram/self-hosted-resources/blob/main/charts/deepgram-self-hosted/README.md) and [Artifact Hub listing](https://artifacthub.io/packages/helm/deepgram-self-hosted/deepgram-self-hosted) for more details. We'll use this chart to deploy Deepgram services in your cluster.

1. [Fetch the repository info](https://github.com/deepgram/self-hosted-resources/blob/main/charts/deepgram-self-hosted/README.md#get-repository-info).

   **`Shell`**

   ```shell Shell
   helm repo add deepgram https://deepgram.github.io/self-hosted-resources
   helm repo update
   ```

2. Save the following as `my-values.yaml`. It pins each component to the node pool you created, mounts the Azure Files claim as the model volume, and lets the chart install the NVIDIA GPU Operator. See the [chart README](https://github.com/deepgram/self-hosted-resources/blob/main/charts/deepgram-self-hosted/README.md#values) for every available option.

   **`my-values.yaml`**

   ```yaml my-values.yaml
   global:
     pullSecretRef: "dg-regcred"
     deepgramSecretRef: "dg-self-hosted-api-key"

   scaling:
     replicas:
       api: 1
       engine: 1
     auto:
       enabled: false

   api:
     affinity:
       nodeAffinity:
         requiredDuringSchedulingIgnoredDuringExecution:
           nodeSelectorTerms:
             - matchExpressions:
                 - key: k8s.deepgram.com/node-type
                   operator: In
                   values:
                     - api
     resources:
       requests:
         memory: "4Gi"
         cpu: "2000m"
       limits:
         memory: "12Gi"
         cpu: "4000m"

   engine:
     affinity:
       nodeAffinity:
         requiredDuringSchedulingIgnoredDuringExecution:
           nodeSelectorTerms:
             - matchExpressions:
                 - key: k8s.deepgram.com/node-type
                   operator: In
                   values:
                     - engine
     resources:
       requests:
         memory: "24Gi"
         cpu: "5000m"
         gpu: 1
       limits:
         memory: "40Gi"
         cpu: "8000m"
         gpu: 1
     modelManager:
       volumes:
         customVolumeClaim:
           enabled: true
           name: dg-model-storage
           modelsDirectory: "/"

   licenseProxy:
     enabled: true
     affinity:
       nodeAffinity:
         requiredDuringSchedulingIgnoredDuringExecution:
           nodeSelectorTerms:
             - matchExpressions:
                 - key: k8s.deepgram.com/node-type
                   operator: In
                   values:
                     - license-proxy
     resources:
       requests:
         memory: "4Gi"
         cpu: "1000m"
       limits:
         memory: "8Gi"
         cpu: "2000m"

   # The Engine node pool was created with `--gpu-driver none`, so the GPU Operator
   # installs the NVIDIA driver (>=580, open kernel modules) and container toolkit.
   # The chart's default container toolkit (v1.15.0) doesn't register the `nvidia`
   # runtime with the containerd 2.x that current AKS nodes use, so pin a newer one.
   gpu-operator:
     enabled: true
     toolkit:
       version: v1.17.8-ubi8
   ```

3. Adjust the values to match your cluster.

   * Set `scaling.replicas.api` and `scaling.replicas.engine` to the initial number of replicas. Keep the Engine replica count at or below the number of nodes in `enginepool`, because each Engine pod requests one GPU.
   * If you chose a VM with less memory than the example, lower the `requests` and `limits` so the pods fit on the node.
   * For Aura text-to-speech, each Engine needs two GPUs. Set `engine.resources.requests.gpu` and `engine.resources.limits.gpu` to `2`, and start from the [Deploy TTS Services](/docs/deploy-tts-services) guide.

   > **Info**
   >
   > Node pool autoscaling, which you configured with the Azure CLI, is separate from pod autoscaling in the chart. To enable pod autoscaling, reach out to your Deepgram Account Representative to discuss which limits and values suit your traffic. See [Autoscaling Best Practices](/docs/autoscaling-best-practices).

4. Install the Helm chart with your values file.

   **`Shell`**

   ```shell Shell
   helm install deepgram deepgram/deepgram-self-hosted \
       -f my-values.yaml \
       --namespace dg-self-hosted \
       --atomic \
       --timeout 1h
   # Monitor the installation in a separate shell
   watch kubectl get all
   ```

   > **Warning**
   >
   > ## Allow time for the first install
   >
   > The GPU Operator installs the NVIDIA driver on each GPU node, and AKS may need to provision a new node first. This can take several minutes. If a pod isn't scheduled as you expect, `kubectl describe pod <pod-name>` lists the events that explain why.

## Verify the GPU setup

Confirm that the cluster advertises your GPUs and that the installed driver meets Deepgram's requirements.

1. List the GPUs Kubernetes can schedule on each Engine node.

   **`Shell`**

   ```shell Shell
   kubectl get nodes \
       --selector k8s.deepgram.com/node-type=engine \
       --output custom-columns='NAME:.metadata.name,GPUS:.status.allocatable.nvidia\.com/gpu'
   ```

2. Check the driver version that the GPU Operator installed.

   **`Shell`**

   ```shell Shell
   DRIVER_POD=$(
       kubectl get pods \
           --namespace dg-self-hosted \
           --selector app=nvidia-driver-daemonset \
           --output jsonpath='{.items[0].metadata.name}'
   )
   kubectl exec --namespace dg-self-hosted $DRIVER_POD -c nvidia-driver-ctr -- nvidia-smi
   kubectl exec --namespace dg-self-hosted $DRIVER_POD -c nvidia-driver-ctr -- cat /proc/driver/nvidia/version
   ```

   The `nvidia-smi` output should list your GPU and a driver version of `580` or later. The version string should read `NVIDIA UNIX Open Kernel Module`.

## Test your Deepgram setup with a sample request

Test your Deepgram deployment on AKS with an audio file.

1. Launch an ephemeral pod to send your test request from.

   **`Shell`**

   ```shell Shell
   kubectl run --namespace dg-self-hosted api-client \
       --stdin --tty --rm \
       --image=curlimages/curl \
       -- /bin/sh
   ```

2. Inside the ephemeral pod, download a sample file from Deepgram, or supply your own file.

   **`Shell`**

   ```shell Shell
   wget https://dpgr.am/bueller.wav
   ```

3. Send your audio file to your Deepgram setup for transcription.

   **`Shell`**

   ```shell Shell
   curl \
       -X POST \
       --data-binary @bueller.wav \
       "http://deepgram-api-external.dg-self-hosted.svc.cluster.local:8080/v1/listen?model=nova-3&smart_format=true"
   ```

   > **Info**
   >
   > If needed, adjust pieces of the above command:
   >
   > * the query parameters to match the directions from your Deepgram Account Representative
   > * the service name `deepgram-api-external`
   > * the namespace `dg-self-hosted`

You should receive a JSON response with the transcript and associated metadata. You're all set: your self-hosted setup is working.

## Troubleshoot common AKS issues

| Symptom                                                                                                                                                               | Likely cause and fix                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enginepool` creation fails with a quota or `OperationNotAllowed` error                                                                                               | Your subscription has no quota for that VM family in the region. [Request quota](#request-gpu-quota), or choose another region or size.                                                                                                                 |
| `unrecognized arguments: --gpu-driver`                                                                                                                                | Your Azure CLI is older than `2.72.2`. Upgrade it with `az upgrade`.                                                                                                                                                                                    |
| Engine pod stays `Pending` with `Insufficient nvidia.com/gpu`                                                                                                         | The GPU Operator hasn't finished installing the driver and device plugin on the node. Check `kubectl get pods --namespace dg-self-hosted`, and wait for the `nvidia-*` pods to reach `Running`.                                                         |
| `nvidia-operator-validator`, `nvidia-device-plugin-daemonset` and other GPU Operator pods stay in `Init`, and pod events show `no runtime for "nvidia" is configured` | The NVIDIA container toolkit is too old for the containerd 2.x on your nodes. Set `gpu-operator.toolkit.version` to `v1.17.8-ubi8`, as in the values file above, and run `helm upgrade`.                                                                |
| `nvidia-driver-daemonset` pod fails or restarts repeatedly                                                                                                            | The node OS or kernel isn't supported by the GPU Operator driver image. See NVIDIA's [supported platforms](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/platform-support.html), and use the default Ubuntu node image.           |
| `dg-model-storage` stays `Pending`, or pods can't mount it                                                                                                            | The AKS identity can't create or reach the storage account. Review the NFS prerequisites in Microsoft's [Azure Files guide](https://learn.microsoft.com/en-us/azure/aks/create-volume-azure-files#prerequisites-for-using-nfs-shares-with-azure-files). |
| Engine pod exits at startup with a missing model error                                                                                                                | The model files aren't in the root of the share. Check the downloader Job logs, and confirm the file names match what your Deepgram Account Representative provided.                                                                                    |

For general Kubernetes issues, see [Troubleshooting](/docs/k8s-troubleshooting).

## Next steps

Your Deepgram services are accessible within your cluster through the `deepgram-api-external` Service that the Helm chart created.

To accept requests from outside the cluster, expose the API with an Azure load balancer. In your `my-values.yaml`, set `api.service.type` to `LoadBalancer`. Add the `service.beta.kubernetes.io/azure-load-balancer-internal: "true"` annotation under `api.service.annotations` to keep the load balancer private to your virtual network. See Microsoft's [AKS load balancer documentation](https://learn.microsoft.com/en-us/azure/aks/load-balancer-standard) for details. Your installation automatically balances received requests across the cluster, so the load balancer serves as the ingress endpoint into the cluster.

To stop charges when you're done testing, delete the resource group. This removes the cluster, node pools, and model storage.

**`Shell`**

```shell Shell
az group delete --name $RESOURCE_GROUP --yes --no-wait
```

---

What's next

Now that you have a basic Deepgram setup working, take some time to learn about building up to a production-level environment, as well as helpful Deepgram add-on services.

* [Securing Your Cluster](/docs/securing-your-cluster)
* [Scaling and Deployment Strategies](/docs/scaling-and-deployment-strategies)
* [Self-Hosted Add Ons](/docs/self-hosted-add-ons)
