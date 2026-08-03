---
title: "Google Cloud Platform"
source: https://developers.deepgram.com/docs/gcp-k8s.md
path: docs/gcp-k8s
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Google Cloud Platform

Deploying Deepgram on Google Cloud Platform (GCP) requires some preparation. In this section, you will learn how to provision a managed Kubernetes Cluster where you will deploy Deepgram products. You will need to perform some of these steps in the Google Cloud Console and some in your local terminal.

# Prerequisites

Make sure you have completed the requirements in the [Self-Hosted Introduction](/docs/self-hosted-introduction).

GPU availability has been extremely limited across cloud providers, including GCP. You may need to [request a GPU quota](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus#request_quota) if you are not able to provision spot GPU instances in your node pools.

## `kubectl`

The Kubernetes command-line tool, `kubectl`, allows you to run commands against Kubernetes clusters. You can use `kubectl` to deploy applications, inspect and manage cluster resources, and view logs.

Install locally using [the official Kubernetes guides](https://kubernetes.io/docs/tasks/tools/#kubectl) .

## `gcloud` CLI

The [`gcloud` CLI](https://cloud.google.com/sdk/gcloud) provides programmatic access to manage your GCP services. Certain steps in this guide are enabled by this tool, although many of the same actions can be performed manually in the Google Cloud Console.

1. Follow the [installation guide](https://cloud.google.com/sdk/docs/install) to install the CLI locally.
2. Once installed, run `gcloud init` to configure the CLI with access to your GCP account and project.

<h2> Choosing a Region </h2>
The templates and steps in this guide provision resources in the GCP `us-west1` region.

If you would like to deploy to a different region, make sure to adjust templates and steps in this guide accordingly.

## Cluster Management with `gcloud container clusters`

The `gcloud container clusters` command group allows you to create and manage GKE clusters.

Certain steps in this guide use these commands, although many of the same actions can be performed manually in the Google Cloud Console.

## Kubernetes Packages with `helm`

[Helm](https://helm.sh/) is the package manager for Kubernetes. A package in Kubernetes is defined by a Helm Chart, which helps you define, install, and upgrade even the most complex Kubernetes application.

We use Helm to install several components in this guide. See the [installation guide](https://helm.sh/docs/intro/install/) for details on how to install locally.

# Creating a Cluster

Google Kubernetes Engine (GKE) is a managed Kubernetes service to run Kubernetes in GCP. In the cloud, GKE automatically manages the availability and scalability of the Kubernetes control plane nodes responsible for scheduling containers, managing application availability, storing cluster data, and other key tasks.

1. Create a new GKE cluster with `gcloud`, and get the zones where your cluster is created.

   ```shell Shell
   CLUSTER_NAME=deepgram-self-hosted
   CLUSTER_LOCATION=us-west1
   gcloud container clusters create $CLUSTER_NAME \
       --location $CLUSTER_LOCATION \
       --num-nodes 1 \
       --enable-autoscaling \
       --machine-type n1-standard-2 \
       --addons=GcePersistentDiskCsiDriver

   CLUSTER_ZONES=$(
        gcloud container clusters describe $CLUSTER_NAME \
            --location $CLUSTER_LOCATION \
            --format="value(locations.join(','))"
   )
   ENGINE_NP_ZONE=$(echo "$CLUSTER_ZONES" | cut -d',' -f1)
   ```

2. Create separate node pools for each Deepgram component (API, Engine, License Proxy). Adjust the machine types and node counts according to your needs. You may wish to consult your Deepgram Account Representative in planning your cluster's capacity.

   <h2> `num-nodes` Default Behavior</h2>
   `num-nodes` configures the number of nodes in the node pool ***in each of the cluster's zones***. If your cluster is configured in 3 zones, setting`num-nodes` to 1 will result in 1 node per zone, or 3 nodes across the entire cluster.

   We restrict the `engine-pool` to one cluster zone because [you can't use regional persistent disks on VMs that use G2 standard machine types](https://cloud.google.com/compute/docs/accelerator-optimized-machines#g2_standard_limitations). This guide uses a zonal persistent disk as a workaround, which means we must limit the nodes in `engine-pool` to a single zone in order to mount the disk.

   ```shell Shell
   gcloud container node-pools create api-pool \
       --cluster $CLUSTER_NAME \
       --location $CLUSTER_LOCATION \
       --num-nodes 1 \
       --enable-autoscaling \
       --max-nodes 3 \
       --machine-type n1-standard-4 \
       --node-labels k8s.deepgram.com/node-type=api

   gcloud container node-pools create engine-pool \
       --cluster $CLUSTER_NAME \
       --region $CLUSTER_LOCATION \
       --node-locations $ENGINE_NP_ZONE \
       --num-nodes 1 \
       --enable-autoscaling \
       --max-nodes 8 \
       --machine-type g2-standard-8 \
       --accelerator=type=nvidia-l4,count=1,gpu-driver-version=latest \
       --node-labels k8s.deepgram.com/node-type=engine

   gcloud container node-pools create license-proxy-pool \
       --cluster $CLUSTER_NAME \
       --location $CLUSTER_LOCATION \
       --num-nodes 1 \
       --enable-autoscaling \
       --max-nodes 2 \
       --machine-type n1-standard-2 \
       --node-labels k8s.deepgram.com/node-type=license-proxy
   ```

3. Create a dedicated namespace for Deepgram resources.

   ```shell Shell
   kubectl create namespace dg-self-hosted
   kubectl config set-context --current --namespace=dg-self-hosted
   ```

### Configure Namespace Resource Quotas for GKE

When deploying workloads in a non-default namespace (such as `dg-self-hosted`), GKE does not automatically provision quotas for the `system-node-critical` and `system-cluster-critical` priority classes in that namespace. GPU driver DaemonSets (and other node-critical system workloads) rely on these priorities to schedule correctly.

Create a `ResourceQuota` in your Deepgram namespace to enable these priorities:

```yaml "ResourceQuota Resource"
apiVersion: v1
kind: ResourceQuota
metadata:
  name: gcp-critical-pods
  namespace: dg-self-hosted
  labels:
    addonmanager.kubernetes.io/mode: EnsureExists
spec:
  # Set a limit on the number of pods allowed with critical priority classes in this namespace.
  # Pick a value >= total nodes that will run the NVIDIA driver DaemonSet, plus a small buffer.
  hard:
    pods: 5
  scopeSelector:
    matchExpressions:
    - operator: In
      scopeName: PriorityClass
      values: ["system-node-critical", "system-cluster-critical"]
```

&#x20;Without this quota, pods that require these priority classes may remain unscheduled.&#x20;

# Configure Persistent Storage

Next, create a Google Cloud Persistent Disk to hold the Deepgram model files. Populate the disk from inside the cluster with a one-shot Kubernetes Job, then delete the Job. The disk remains, and will later be mounted read-only into the Deepgram Engine pods when the Helm chart is installed.

The `deepgram-self-hosted` Helm chart mounts the Persistent Disk through a `ReadOnlyMany` PV/PVC, so it cannot be used to write the initial model files. Bind a separate, temporary `ReadWriteOnce` PV/PVC to the same underlying disk for the download, then delete it before installing the chart.

1. Create a Google Persistent Disk to store Deepgram model files and share them across multiple Deepgram Engine pods.

   ```shell Shell
   DISK_NAME=deepgram-model-storage
   DISK_URI=$(
       gcloud compute disks create \
           $DISK_NAME \
           --size=40GB \
           --type=pd-ssd \
           --zone $ENGINE_NP_ZONE \
           --format="value(selfLink)" | \
       sed -e 's#.*/projects/#projects/#'
   )
   ```

2. Create a temporary writable `PersistentVolume` and `PersistentVolumeClaim` that point at the disk you just provisioned. The PV uses `ReadWriteOnce` and `Retain` so the underlying disk is preserved when you delete the PV later. The `nodeAffinity` block keeps the downloader pod in the same zone as the zonal Persistent Disk so the disk can attach.

   ```shell Shell
   cat <<EOF | kubectl apply -f -
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: dg-model-downloader
   spec:
     capacity:
       storage: 40Gi
     accessModes:
       - ReadWriteOnce
     persistentVolumeReclaimPolicy: Retain
     storageClassName: ""
     csi:
       driver: pd.csi.storage.gke.io
       volumeHandle: $DISK_URI
       fsType: ext4
     nodeAffinity:
       required:
         nodeSelectorTerms:
           - matchExpressions:
               - key: topology.kubernetes.io/zone
                 operator: In
                 values:
                   - $ENGINE_NP_ZONE
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: dg-model-downloader
     namespace: dg-self-hosted
   spec:
     accessModes:
       - ReadWriteOnce
     resources:
       requests:
         storage: 40Gi
     storageClassName: ""
     volumeName: dg-model-downloader
   EOF
   ```

3. Run a one-shot `Job` that mounts the writable PVC and downloads the model files provided by your Deepgram Account Representative. The CSI driver creates the `ext4` filesystem on the disk the first time the volume is attached.

   Replace the `wget` lines below with the model URLs supplied by your Deepgram Account Representative.

   ```shell Shell
   cat <<'EOF' | kubectl apply -f -
   apiVersion: batch/v1
   kind: Job
   metadata:
     name: dg-model-downloader
     namespace: dg-self-hosted
   spec:
     backoffLimit: 0
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
                 wget https://link-to-model-1.dg
                 wget https://link-to-model-2.dg
                 # ... continue for all model files
             volumeMounts:
               - name: models
                 mountPath: /mnt/models
         volumes:
           - name: models
             persistentVolumeClaim:
               claimName: dg-model-downloader
   EOF
   ```

4. Wait for the Job to complete successfully.

   ```shell Shell
   kubectl wait -n dg-self-hosted --for=condition=complete job/dg-model-downloader --timeout=30m
   kubectl logs -n dg-self-hosted job/dg-model-downloader
   ```

5. Delete the Job and the temporary writable PV and PVC. Because the PV uses `persistentVolumeReclaimPolicy: Retain`, the underlying Google Persistent Disk is preserved with the model files intact.

   ```shell Shell
   kubectl delete -n dg-self-hosted job dg-model-downloader
   kubectl delete -n dg-self-hosted pvc dg-model-downloader
   kubectl delete pv dg-model-downloader
   ```

# Configure Kubernetes Secrets

Deepgram strongly recommends following [best practices for configuring Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) . Please refer to [Securing Your Cluster](/docs/securing-your-cluster) for more details.

The `deepgram-self-hosted` Helm chart takes two Secret references. One is a set of distribution credentials that allow the cluster to pull images from Deepgram's container image repository. The other is your self-hosted API key that licenses each Deepgram container that is created.

1. Complete the [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) guide to generate distribution credentials and a self-hosted API key.

2. If using an external Secret store provider, configure cluster access to these two Secrets, naming them `dg-regcred` (distribution credentials) and `dg-self-hosted-api-key`.

3. If not using an external Secret store provider, create the Secrets manually in your cluster.

   1. Using the distribution credentials username and password generated in the Deepgram Console, create a Kubernetes Secret named `dg-regcred`.

      ```shell Shell
      kubectl create secret docker-registry dg-regcred \
          --docker-server=quay.io \
          --docker-username='QUAY_DG_USER' \
          --docker-password='QUAY_DG_PASSWORD'
      ```

      Replace the placeholders `QUAY_DG_USER` and `QUAY_DG_PASSWORD` with the distribution credentials you generated in the [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) guide.

   2. Create a Kubernetes Secret named `dg-self-hosted-api-key` to store your self-hosted API key.

      ```shell Shell
      kubectl create secret generic dg-self-hosted-api-key \
          --from-literal=DEEPGRAM_API_KEY='YOUR_API_KEY_HERE'
      ```

      Replace the placeholder `YOUR_API_KEY_HERE` with the Deepgram API key you generated in the [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) guide.

# Deploy Deepgram

Deepgram maintains the official `deepgram-self-hosted` Helm Chart. You can reference the [source](https://github.com/deepgram/self-hosted-resources/blob/main/charts/deepgram-self-hosted/README.md) and [Artifact Hub listing](https://artifacthub.io/packages/helm/deepgram-self-hosted/deepgram-self-hosted) for more details. We'll use this Chart to facilitate deploying Deepgram services in your self-hosted environment.

1. [Fetch the repository info](https://github.com/deepgram/self-hosted-resources/blob/main/charts/deepgram-self-hosted/README.md#get-repository-info).

   ```shell Shell
   helm repo add deepgram https://deepgram.github.io/self-hosted-resources
   helm repo update
   ```

2. Download a `values.yaml` template for Deepgram's self-hosted Helm chart [from here](https://github.com/deepgram/self-hosted-resources/blob/main/charts/deepgram-self-hosted/values.yaml).

3. Modify the `values.yaml` file:

   * Update the `scaling.static.{api,engine,licenseProxy}.replicas` values to match your node pool sizes.

   * Configure the `engine.modelManager.volumes.gcp.gpd` values to use the Google Persistent Disk you created earlier.

     ```shell Shell
     echo $DISK_URI
     ```

     ```yaml yaml
     engine:
       modelManager:
         volumes:
           gcp:
             gpd:
               enabled: true
               volumeHandle: "<your DISK_URI here>"
     ```

4. Install the Helm Chart with your `values.yaml` file.

   ```shell Shell
   helm install deepgram deepgram/deepgram-self-hosted \
       -f my-values.yaml \
       --namespace dg-self-hosted \
       --create-namespace \
       --atomic \
       --timeout 1h
   # Monitor the installation in a separate shell
   watch kubectl get all
   ```

   <h2> Resource Limits </h2>
   It may take some time for GKE to resize the number of nodes in your cluster to accommodate your deployment.

   If you want to monitor the status, or your pods aren't being scheduled as you expect, you can see a pod's scheduling status with `kubectl describe pod <pod-name>`, which may contain details on what is preventing scheduling.

# Test Your Deepgram Setup with a Sample Request

Test your environment and container setup with a local file.

1. Get the name of one of the Deepgram API Pods.
   ```shell Shell
   API_POD_NAME=$(
       kubectl get pods \
           --selector app=deepgram-api \
           --output jsonpath='{.items[0].metadata.name}' \
           --no-headers
   )
   ```

2. Launch an ephemeral container to send your test request from.
   ```shell Shell
   kubectl debug $API_POD_NAME \
       -it \
       --image=curlimages/curl \
       -- /bin/sh
   ```

3. Inside the ephemeral container, download a sample file from Deepgram (or supply your own file).
   ```shell Shell
   wget https://dpgr.am/bueller.wav
   ```

4. Send your audio file to your local Deepgram setup for transcription.

   ```bash cURL
   curl \
       -X POST \
       --data-binary @bueller.wav \
       "http://localhost:8080/v1/listen?model=nova-3&smart_format=true"
   ```

   If needed, adjust pieces of the above command:

   * the query parameters to match the directions from your Deepgram Account Representative
   * the service name `deepgram-api-external`
   * the namespace `dg-self-hosted`

You should receive a JSON response with the transcript and associated metadata. Congratulations - your self-hosted setup is working!

# Next Steps

Your Deepgram services are accessible within your cluster via the `deepgram-api-external` Service that was created by the Helm Chart.

You may consider configuring additional ingress with a GCP Load Balancer to access your services. Note that your installation will automatically load balance any received requests within the cluster to distribute load evenly. The load balancer would primarily serve as the ingress endpoint into the cluster.

---

What’s Next

Now that you have a basic Deepgram setup working, take some time to learn about building up to a production-level environment, as well as helpful Deepgram add-on services.

* [Securing Your Cluster](/docs/securing-your-cluster)
* [Scaling and Deployment Strategies](/docs/scaling-and-deployment-strategies)
* [Self-Hosted Add Ons](/docs/self-hosted-add-ons)
