---
title: "Deploy BYOC"
source: https://docs.pinecone.io/guides/production/bring-your-own-cloud/deploy
path: guides/production/bring-your-own-cloud/deploy
---

Deploy Pinecone BYOC into your own AWS, GCP, or Azure account with the setup wizard and Pulumi, then verify the deployment.

Deploy the Pinecone BYOC data plane into your own AWS, GCP, or Azure account using the setup wizard and Pulumi, then verify it's running.

## Prerequisites

Before deploying BYOC, ensure you have the following tools installed on your local machine:

| Tool | Purpose | Install |
| - | - | - |
| Python 3.12+ | Runtime | [python.org](https://www.python.org/downloads/) |
| uv | Package manager | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
| Pulumi | Infrastructure-as-code | [pulumi.com/docs/install](https://www.pulumi.com/docs/install/) |
| kubectl | Cluster access | [kubernetes.io](https://kubernetes.io/docs/tasks/tools/) |

You also need:

* The CLI for your cloud provider:
  * **AWS**: [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
  * **GCP**: [gcloud CLI](https://cloud.google.com/sdk/docs/install)
  * **Azure**: [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* A cloud account with admin-level permissions:
  * **AWS**: `AdministratorAccess`. `PowerUserAccess` isn't sufficient because BYOC creates IAM roles and policies.
  * **GCP**: `roles/owner`. `roles/editor` isn't sufficient because BYOC creates IAM service accounts and bindings.
  * **Azure**: `Owner` on the subscription. `Contributor` isn't sufficient because BYOC creates managed identities and role assignments.
* Sufficient cloud quota for the resources (the setup wizard validates this)
* A Pinecone API key from the Pinecone console
* A Pinecone Enterprise plan (required for BYOC access)

> [!NOTE]
>
> If you install any new tools, open a new terminal session before proceeding so that your shell picks up the updated PATH and environment.

## Deploy your environment

To deploy BYOC, follow these steps:

### 1. Run the setup wizard

Run the bootstrap script from the BYOC deployment repository ([github.com/pinecone-io/pulumi-pinecone-byoc](https://github.com/pinecone-io/pulumi-pinecone-byoc)) to start the interactive setup wizard:

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/pinecone-io/pulumi-pinecone-byoc/main/bootstrap.sh | bash
```

You can also pre-select your cloud provider:

```bash theme={null}
# AWS
curl -fsSL https://raw.githubusercontent.com/pinecone-io/pulumi-pinecone-byoc/main/bootstrap.sh | bash -s -- --cloud aws

# GCP
curl -fsSL https://raw.githubusercontent.com/pinecone-io/pulumi-pinecone-byoc/main/bootstrap.sh | bash -s -- --cloud gcp

# Azure
curl -fsSL https://raw.githubusercontent.com/pinecone-io/pulumi-pinecone-byoc/main/bootstrap.sh | bash -s -- --cloud azure
```

The script selects your cloud provider, checks that required tools are installed, verifies your cloud credentials, then launches an interactive wizard that collects your configuration choices, validates your quotas, and generates a Pulumi project. No cloud resources are created during this step.

> **Setup wizard prompts**
>
> The wizard prompts you for the following:
>
> | Prompt | Description | Default |
> | - | - | - |
> | **Cloud provider** | Select AWS, GCP, or Azure (skipped if pre-selected via `--cloud`). | - |
> | **Pinecone API key** | Your API key from the Pinecone console (or uses `PINECONE_API_KEY` env var). | - |
> | **Cloud credentials** | Validates credentials and displays your account/project/subscription ID. | - |
> | **GCP project ID** | *(GCP only)* Your GCP project ID. | Detected from `gcloud` |
> | **Azure subscription ID** | *(Azure only)* Your Azure subscription ID. | Detected from `az account show` |
> | **Region** | Region for deployment. | `us-east-1` (AWS) / `us-central1` (GCP) / `eastus` (Azure) |
> | **Availability zones** | Zones for high availability. Wizard fetches available options. | First two zones |
> | **Custom AMI** | *(AWS only)* Custom AMI ID for EKS nodes. Leave blank for the default AWS AMI. | None |
> | **VPC CIDR block** | IP range for your VPC/VNet. Choose a range that doesn't conflict with existing networks. | `10.0.0.0/16` (AWS/Azure) / `10.112.0.0/12` (GCP) |
> | **Deletion protection** | Protect object storage from accidental deletion. | Enabled |
> | **Network access** | Public access (connect from anywhere) or private only (requires PrivateLink on AWS, Private Service Connect on GCP, or Private Link on Azure). | Public enabled |
> | **Resource tags/labels** | Custom tags (AWS/Azure) or labels (GCP) for cost tracking (e.g., `team=platform,env=prod`). | None |
> | **Preflight checks** | Validates cloud quotas. If checks fail, request quota increases before proceeding. | - |
> | **Project name** | Name for your deployment. | `pinecone-byoc` |
> | **Pulumi backend** | Where to store state: local (`~/.pulumi` with passphrase) or Pulumi Cloud. | Local |

After completing the wizard, a Pulumi project is generated in your project directory.

> **Generated configuration file**
>
> The wizard creates a `Pulumi.<stack>.yaml` file with configurable options. The options vary by cloud provider:
>
> **AWS**
>
> | Option | Description | Default |
> | - | - | - |
> | `pinecone-version` | Pinecone release version | - |
> | `region` | AWS region | `us-east-1` |
> | `availability-zones` | Availability zones for high availability | `["us-east-1a", "us-east-1b"]` |
> | `vpc-cidr` | VPC IP range | `10.0.0.0/16` |
> | `deletion-protection` | Protect S3 buckets from accidental deletion | `true` |
> | `public-access-enabled` | Enable public endpoint (`false` = PrivateLink only) | `true` |
> | `custom-ami-id` | Custom AMI ID for EKS nodes | Default AWS AMI |
> | `tags` | Custom tags for all AWS resources | `{}` |
>
> **GCP**
>
> | Option | Description | Default |
> | - | - | - |
> | `gcp:project` | GCP project ID | - |
> | `pinecone-version` | Pinecone release version | - |
> | `region` | GCP region | `us-central1` |
> | `availability-zones` | Zones for high availability | `["us-central1-a", "us-central1-b"]` |
> | `vpc-cidr` | VPC IP range | `10.112.0.0/12` |
> | `deletion-protection` | Protect GCS buckets from accidental deletion | `true` |
> | `public-access-enabled` | Enable public endpoint (`false` = Private Service Connect only) | `true` |
> | `labels` | Custom labels for all GCP resources | `{}` |
>
> **Azure**
>
> | Option | Description | Default |
> | - | - | - |
> | `subscription-id` | Azure subscription ID | - |
> | `pinecone-version` | Pinecone release version | - |
> | `region` | Azure region | `eastus` |
> | `availability-zones` | Zones for high availability | `["1", "2"]` |
> | `vpc-cidr` | VNet IP range | `10.0.0.0/16` |
> | `deletion-protection` | Protect storage accounts from accidental deletion | `true` |
> | `public-access-enabled` | Enable public endpoint (`false` = Private Link only) | `true` |
> | `tags` | Custom tags for all Azure resources | `{}` |
>
> To change configuration after initial setup, edit `Pulumi.<stack>.yaml` and run `pulumi up`.

> **Programmatic usage**
>
> For advanced users who want to integrate BYOC into existing Pulumi infrastructure, the `pulumi-pinecone-byoc` package is available on [PyPI](https://pypi.org/project/pulumi-pinecone-byoc/). Install with cloud-specific dependencies:
>
> ```bash theme={null}
> # For AWS
> uv add 'pulumi-pinecone-byoc[aws]'
>
> # For GCP
> uv add 'pulumi-pinecone-byoc[gcp]'
>
> # For Azure
> uv add 'pulumi-pinecone-byoc[azure]'
> ```
>
> Import the cluster class for your cloud provider:
>
> ```python theme={null}
> # AWS
> from pulumi_pinecone_byoc.aws import PineconeAWSCluster, PineconeAWSClusterArgs
>
> # GCP
> from pulumi_pinecone_byoc.gcp import PineconeGCPCluster, PineconeGCPClusterArgs
>
> # Azure
> from pulumi_pinecone_byoc.azure import PineconeAzureCluster, PineconeAzureClusterArgs
> ```
>
> See the [repository README](https://github.com/pinecone-io/pulumi-pinecone-byoc#programmatic-usage) for full usage examples.

### 2. Deploy the infrastructure

Deploy the generated Pulumi project to create your cloud resources:

```bash theme={null}
cd pinecone-byoc
pulumi up
```

Pulumi shows a preview of all resources to be created. Confirm to proceed. Provisioning takes approximately 25-30 minutes.

When complete, the output displays:

* Your BYOC **environment name** (used when creating indexes).
* The **kubectl command** to configure cluster access.

> **Infrastructure provisioned**
>
> The deployment creates the following resources in your cloud account:
>
> | Component | AWS | GCP | Azure |
> | - | - | - | - |
> | **VPC / Networking** | VPC, public and private subnets, NAT gateways, internet gateway | VPC network, subnets, Cloud NAT, Cloud Router | VNet, subnets, NAT gateway |
> | **Kubernetes** | EKS cluster with managed node groups | GKE cluster with node pools | AKS cluster with agent pools |
> | **Object storage** | S3 buckets (data, WAL, backups) | GCS buckets (data, WAL, backups) | Blob Storage containers (data, WAL, backups) |
> | **Block storage** | EBS volumes | Persistent Disk | Managed Disks |
> | **Metadata store** | FoundationDB (in-cluster) | FoundationDB (in-cluster) | FoundationDB (in-cluster) |
> | **Load balancing** | Network Load Balancer | Internal load balancer with Private Service Connect | Internal load balancer with Private Link Service |
> | **DNS** | Route 53 hosted zone | Cloud DNS managed zone | Azure DNS zone |
> | **TLS certificates** | AWS Certificate Manager | cert-manager | cert-manager |
> | **IAM** | IAM roles and policies | Service accounts and Workload Identity | Managed identities and Workload Identity |
>
> The initial deployment provisions 3 Kubernetes nodes. After setup, the cluster autoscales based on the services Pinecone deploys and your workload.

### 3. Verify the deployment

Configure `kubectl` to connect to your cluster using the command from the deployment output:

**AWS**

```bash theme={null}
aws eks update-kubeconfig --region <region> --name <cluster-name>
```

**GCP**

```bash theme={null}
gcloud container clusters get-credentials <cluster-name> --region <region> --project <project-id>
```

**Azure**

```bash theme={null}
az aks get-credentials --resource-group <resource-group> --name <cluster-name>
```

This command configures your local `kubectl` tool to communicate with your Kubernetes cluster. You'll use cluster access for administrative tasks like viewing operations and troubleshooting. Creating indexes and reading/writing vectors still use the standard Pinecone API.

Verify all components are running:

```bash theme={null}
# Check that all pods are running
kubectl get pods -A | grep -E "(pinecone|pc-)"
```

All pods should show `Running` status. If any pods are in `Pending` or `CrashLoopBackOff`, check the [Troubleshooting](#troubleshooting) section.

You can also verify the cluster operations CRD is installed:

```bash theme={null}
kubectl get cluster-operations
```

It's normal to see "No resources found" on a fresh deployment. Operations appear here as Pinecone performs upgrades and other management tasks.

## Troubleshooting

Common issues and how to resolve them:

> **Preflight check failures**
>
> The setup wizard validates cloud quotas before deployment. If checks fail:
>
> | Check | Resolution |
> | - | - |
> | VPC / network quota | Request a limit increase via your cloud provider's quota console |
> | Kubernetes cluster quota | Request an EKS, GKE, or AKS cluster limit increase |
> | IP address quota | Release unused IPs or request a limit increase |
> | Instance / machine type availability | Verify the required type is available in your region |
> | vCPU quota (Azure) | Request a "Total Regional vCPUs" increase via the Azure Portal (minimum 8 required) |
> | VM SKU availability (Azure) | Verify `Standard_D4s_v5` and L-series SKUs are available in your region |
> | Resource providers (Azure) | Register required providers: `Microsoft.Compute`, `Microsoft.ContainerService`, `Microsoft.Storage`, `Microsoft.Network`, `Microsoft.KeyVault`, `Microsoft.ManagedIdentity`, `Microsoft.Authorization` |
> | Required APIs (GCP only) | Enable Compute Engine, GKE, Cloud Storage, and Cloud DNS |

> **Deployment failures**
>
> If `pulumi up` fails partway through:
>
> ```bash theme={null}
> pulumi refresh  # Sync state with actual resources
> pulumi up       # Retry deployment
> ```

> **Cluster access issues**
>
> Ensure your cloud credentials match the account where the cluster is deployed:
>
> **AWS**
>
> ```bash theme={null}
> aws sts get-caller-identity
> ```
>
> **GCP**
>
> ```bash theme={null}
> gcloud auth list
> gcloud config get-value project
> ```
>
> **Azure**
>
> ```bash theme={null}
> az account show
> ```

> **Index stuck in terminating state**
>
> If you destroyed the cluster before deleting indexes, indexes may be stuck in a "terminating" state. Contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket) for assistance.

For additional help, see the [GitHub Issues](https://github.com/pinecone-io/pulumi-pinecone-byoc/issues) for the deployment repository.

## Next steps

* [Create an index in your BYOC environment](/guides/production/bring-your-own-cloud/create-an-index)
