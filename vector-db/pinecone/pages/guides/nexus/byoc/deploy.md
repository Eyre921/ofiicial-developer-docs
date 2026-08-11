---
title: "Deploy Nexus BYOC"
source: https://docs.pinecone.io/guides/nexus/byoc/deploy
path: guides/nexus/byoc/deploy
---

Install and operate Pinecone Nexus in your own cloud account.

<Note>
  Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

For architecture, see the [Nexus BYOC overview](/guides/nexus/byoc/overview). For data residency and limits, see [Data residency and limits](/guides/nexus/byoc/reference).

## Prerequisites

Before deploying Nexus BYOC, ensure you have the following tools installed on the machine that runs the install:

| Tool         | Purpose                         | Install                                                                      |
| ------------ | ------------------------------- | ---------------------------------------------------------------------------- |
| Git          | Clone the deployment repository | [git-scm.com](https://git-scm.com/downloads)                                 |
| Python 3.12+ | Runtime                         | [python.org](https://www.python.org/downloads/)                              |
| uv           | Package manager                 | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
| Pulumi       | Infrastructure-as-code          | [pulumi.com/docs/install](https://www.pulumi.com/docs/install/)              |
| kubectl      | Cluster access                  | [kubernetes.io](https://kubernetes.io/docs/tasks/tools/)                     |

You also need:

* The CLI for your cloud provider:
  * **AWS**: [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
  * **GCP**: [gcloud CLI](https://cloud.google.com/sdk/docs/install), plus the `gke-gcloud-auth-plugin` component (`gcloud components install gke-gcloud-auth-plugin`)
  * **Azure**: [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* A **dedicated cloud account** with admin-level permissions, used only for this deployment:
  * **AWS**: a dedicated account with `AdministratorAccess`. The installer creates IAM roles and policies, so `PowerUserAccess` is not sufficient.
  * **GCP**: a dedicated project with `roles/owner` and billing enabled. The installer creates IAM service accounts and bindings, so `roles/editor` is not sufficient.
  * **Azure**: a dedicated subscription with `Owner`. The installer creates managed identities and role assignments, so `Contributor` is not sufficient.
* A **Pinecone API key** from the Pinecone console.
* A Pinecone **Enterprise plan** (required for BYOC access).
* A **generation-LLM key**. Every model Nexus uses is BYOM and configurable through the model catalog: generation, embedding, and rerank. The catalog is backed by [LiteLLM](https://docs.litellm.ai/docs/providers), so you can bring any model any LiteLLM-supported provider offers, referenced by its LiteLLM `provider/model` identifier. The shipped defaults route generation to Google Gemini (get a key from [Google AI Studio](https://aistudio.google.com/apikey)) and route embedding and rerank to Pinecone-hosted models (no extra key). You can repoint any tier at a different provider (including endpoints inside your own boundary), each with its own key. Which model each call reaches determines where the content of that call goes. See [Data flows and residency](/guides/nexus/byoc/reference#data-flows-and-residency).
* A **Pulumi state backend** (either Pulumi Cloud or local state via `pulumi login --local`).
* Sufficient cloud quota for the resources (the setup wizard validates this).

Confirm these environment inputs before you start:

* **Region and three availability zones (AZs).** Deploy across three AZs, the supported high-availability shape. The generation-model provider you choose must be available in the region.
* **A spare private IP range** (RFC 1918, `/16` to `/20`) that does not overlap your existing networks. This becomes the Nexus virtual network.
* **Where your source data lives.** Know where your corpus resides so you can stage it into a context after install.
* **Egress paths.** Nexus makes outbound connections for the control-plane callback, metrics and traces, container image pulls, and calls to the inference models you configure. What content those model calls carry depends on how you configure your models. See [Data flows and residency](/guides/nexus/byoc/reference#data-flows-and-residency).

<Note>
  If you install any new tools, open a new terminal session before proceeding so that your shell picks up the updated PATH and environment.
</Note>

## 1. Deploy

To deploy Nexus BYOC, follow these steps.

<Steps>
  <Step title="Authenticate">
    The setup script checks your credentials but does not log you in, so authenticate to your cloud and to Pulumi first.

    <Tabs>
      <Tab title="AWS">
        ```bash theme={null}
        aws configure                  # or: aws sso login / exported AWS_* env vars
        aws sts get-caller-identity    # verify
        pulumi login                   # or: pulumi login --local
        ```
      </Tab>

      <Tab title="GCP">
        ```bash theme={null}
        gcloud auth login
        gcloud auth application-default login
        pulumi login                   # or: pulumi login --local
        ```
      </Tab>

      <Tab title="Azure">
        ```bash theme={null}
        az login
        az account show                # verify
        pulumi login                   # or: pulumi login --local
        ```
      </Tab>
    </Tabs>

    If you use the local Pulumi backend, choose a passphrase for encrypting stack secrets and export it as `PULUMI_CONFIG_PASSPHRASE`. Every `pulumi` command needs it.
  </Step>

  <Step title="Run the setup wizard">
    Clone the deployment repository and run the bootstrap script from the clone. The generated project is created next to the clone and depends on it.

    ```bash theme={null}
    git clone https://github.com/pinecone-io/pulumi-pinecone-nexus-byoc.git
    bash pulumi-pinecone-nexus-byoc/bootstrap.sh --cloud gcp
    ```

    Use `--cloud aws` or `--cloud azure` for the other clouds, and `--stack-name <name>` to name the Pulumi stack (default: `prod`).

    The script selects your cloud provider, checks that required tools are installed, verifies your cloud credentials, prompts for the project directory and name, then launches an interactive wizard that collects your configuration, validates your quotas, and generates a Pulumi project in an adjacent directory (default: `pinecone-nexus-byoc`). No cloud resources are created during this step.

    <Accordion title="Setup wizard prompts">
      The wizard prompts you for the following:

      | Prompt                         | Description                                                                                                                                             |
      | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **Cloud provider**             | AWS, GCP, or Azure (skipped if pre-selected via `--cloud`).                                                                                             |
      | **Project directory and name** | Where to generate the Pulumi project. Defaults to `pinecone-nexus-byoc`.                                                                                |
      | **Pinecone API key**           | Your API key from the Pinecone console (or uses `PINECONE_API_KEY`).                                                                                    |
      | **Cloud credentials**          | Validates credentials and displays your account/project/subscription ID.                                                                                |
      | **Region**                     | Region for deployment.                                                                                                                                  |
      | **Availability zones**         | Three zones for high availability.                                                                                                                      |
      | **VPC/VNet CIDR block**        | Private IP range for the deployment. Choose a `/16` to `/20` that doesn't overlap existing networks.                                                    |
      | **Generation-LLM key**         | The default catalog's Gemini API key (BYOM).                                                                                                            |
      | **Network access**             | Public access. Private-only access is not supported for Nexus. See [Limitations](/guides/nexus/byoc/reference#limitations).                             |
      | **Deletion protection**        | Whether to protect storage and database resources from accidental deletion. Enable to guard against teardown mistakes. Disable before `pulumi destroy`. |
      | **Preflight checks**           | Validates cloud quotas. If checks fail, request quota increases before proceeding.                                                                      |
      | **Pulumi backend**             | Local (`~/.pulumi` with passphrase) or Pulumi Cloud.                                                                                                    |
    </Accordion>

    After completing the wizard, a Pulumi project is generated in your project directory. To change configuration later, edit `Pulumi.<stack>.yaml` and run `pulumi up`.
  </Step>

  <Step title="Deploy the infrastructure">
    Deploy the generated Pulumi project to create your cloud resources:

    ```bash theme={null}
    cd pinecone-nexus-byoc
    pulumi up
    ```

    Pulumi shows a preview of all resources to be created. Confirm to proceed. Provisioning time depends on the cloud:

    | Cloud | Typical provisioning time |
    | ----- | ------------------------- |
    | GCP   | 25 to 30 minutes          |
    | AWS   | 25 to 40 minutes          |
    | Azure | about 35 minutes          |

    When complete, the output displays:

    * The `update_kubeconfig_command` for configuring cluster access.
    * Your BYOC **environment name**.
    * Two workspace console links, printed once the first-run `default` workspace reaches `Ready`:
      * `nexus_default_workspace_data_console_url`: the workspace console for the `default` workspace, served from your deployment (where you work with contexts and run queries).
      * `nexus_default_workspace_control_console_url`: the Pinecone Console page for that workspace.

    <Note>
      The first `pulumi up` creates a `default` workspace automatically and waits for it to become ready before printing the links. Later `pulumi up` runs never recreate or modify it.
    </Note>

    <Accordion title="Infrastructure provisioned">
      The deployment creates the following in your cloud account:

      | Component            | AWS                                                             | GCP                                           | Azure                                    |
      | -------------------- | --------------------------------------------------------------- | --------------------------------------------- | ---------------------------------------- |
      | **VPC / Networking** | VPC, public and private subnets, NAT gateways, internet gateway | VPC network, subnets, Cloud NAT, Cloud Router | VNet, subnets, NAT gateway               |
      | **Kubernetes**       | EKS cluster with managed node groups                            | GKE cluster with node pools                   | AKS cluster with agent pools             |
      | **Object storage**   | S3 buckets (corpus, knowledge artifacts, data, WAL, backups)    | GCS buckets                                   | Blob Storage containers                  |
      | **Metadata store**   | FoundationDB (Nexus metadata)                                   | FoundationDB                                  | FoundationDB                             |
      | **Load balancing**   | Network Load Balancer                                           | Internal load balancer                        | Internal load balancer                   |
      | **DNS**              | Route 53 hosted zone                                            | Cloud DNS managed zone                        | Azure DNS zone                           |
      | **TLS certificates** | AWS Certificate Manager                                         | cert-manager                                  | cert-manager                             |
      | **IAM**              | IAM roles and policies                                          | Service accounts and Workload Identity        | Managed identities and Workload Identity |

      The cluster comes up small and then autoscales across several node pools spread over the three AZs. See [Cluster footprint](/guides/nexus/byoc/reference#cluster-footprint) for the node pools.
    </Accordion>
  </Step>

  <Step title="Verify the deployment">
    Configure `kubectl` using the `update_kubeconfig_command` from the deployment output:

    <Tabs>
      <Tab title="AWS">
        ```bash theme={null}
        aws eks update-kubeconfig --region <region> --name <cluster-name>
        ```
      </Tab>

      <Tab title="GCP">
        ```bash theme={null}
        gcloud container clusters get-credentials <cluster-name> --region <region> --project <project-id>
        ```
      </Tab>

      <Tab title="Azure">
        ```bash theme={null}
        az aks get-credentials --resource-group <resource-group> --name <cluster-name>
        ```
      </Tab>
    </Tabs>

    Cluster access is for administrative tasks like viewing operations and troubleshooting. Everyday work (creating contexts, curating sources, and running queries) uses the Nexus console, CLI, or API.

    Verify all components are running:

    ```bash theme={null}
    kubectl get pods -A | grep -E "(pinecone|pc-|nexus)"
    ```

    All pods should show `Running` status. If any are in `Pending` or `CrashLoopBackOff`, see [Troubleshooting](#troubleshooting).
  </Step>
</Steps>

## 2. Use

Once your deployment is up and the `default` workspace is ready, you work with Nexus the same way you would in the managed service. For the end-to-end lifecycle (create a context, stage sources, curate, and query with KnowQL), see the [Nexus quickstart](/guides/nexus/quickstart).

Two things are specific to BYOC:

* **Point your client at your own workspace host.** Instead of the Pinecone-hosted endpoint, use your deployment's workspace host, the base of `nexus_default_workspace_data_console_url` from the deployment output. For the CLI, pass it as `--api-url`:

  ```bash theme={null}
  nexus login --api-url https://default-<vault>.wksp.<environment>.pinecone.io --api-key "$PINECONE_API_KEY"
  ```

  Authentication uses your Pinecone API key, and the tenancy boundary is the workspace's Pinecone project.

* **A `default` workspace is created on the first `pulumi up`.** The install creates it automatically and prints its data console URL (served from your deployment) and its Pinecone Console URL. Later `pulumi up` runs never recreate or modify it.

## 3. Manage

<Note>
  Deploying a BYOC environment creates an internal project named `__SLI__` in your organization. Pinecone uses it to enforce SLAs for your BYOC environment. Do not modify or delete it.
</Note>

### Operations and upgrades

Pinecone uses a pull-based model for cluster operations:

1. When upgrades, scaling, or maintenance are needed, Pinecone queues operations in the control plane.
2. An agent running in your cluster (deployed automatically during setup) continuously pulls pending operations.
3. Operations execute locally within your cluster.
4. Status is reported back to Pinecone for monitoring.

This model ensures Pinecone never needs direct access to your infrastructure. All communication is outbound from your cluster.

A deployment is pinned to two independent image tags that roll separately: `pinecone-version` (the Pinecone Database images) and `nexus-version` (the Nexus images). The two pins are unrelated. Bumping one does not touch the other. Pinecone manages upgrades in the background. To trigger one manually, set either pin (or both) to your target version (for example, `main-abc1234`) and re-run `pulumi up`:

```bash theme={null}
# Bump the Pinecone Database version
pulumi config set pinecone-version <new-db-tag>
pulumi up

# Bump the Nexus version
pulumi config set nexus-version <new-nexus-tag>
pulumi up
```

### Monitoring

You can monitor your deployment through multiple channels:

<AccordionGroup>
  <Accordion title="Pinecone console">
    View workspace and index metrics in the Pinecone console. Control plane operations and metrics work regardless of your network access mode.
  </Accordion>

  <Accordion title="Prometheus">
    To use Prometheus, configure your monitoring tool within your VPC to scrape metrics from the cluster. Your Prometheus instance must have network access to the BYOC VPC. The deployment output includes the metrics endpoint URL and port.
  </Accordion>

  <Accordion title="Audit logs">
    Cluster operations are persisted as Kubernetes CRDs for compliance and auditing:

    ```bash theme={null}
    kubectl get cluster-operations
    ```
  </Accordion>
</AccordionGroup>

### Cleanup

<Warning>
  Delete all Nexus workspaces before destroying the cluster. Resources cannot be properly terminated if the cluster is destroyed first.
</Warning>

To destroy your deployment:

```bash theme={null}
# 1. Delete all workspaces via the Pinecone console
# 2. Then destroy the infrastructure
pulumi destroy
```

If `deletion-protection` is enabled (the default), you must either disable it in `Pulumi.<stack>.yaml` and run `pulumi up`, or manually delete the protected storage and database resources via the cloud console before running `pulumi destroy`.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Preflight check failures">
    The setup wizard validates cloud quotas before deployment. If checks fail:

    | Check                                | Resolution                                                                                    |
    | ------------------------------------ | --------------------------------------------------------------------------------------------- |
    | VPC / network quota                  | Request a limit increase via your cloud provider's quota console                              |
    | Kubernetes cluster quota             | Request an EKS, GKE, or AKS cluster limit increase                                            |
    | IP address quota                     | Release unused IPs or request a limit increase                                                |
    | Instance / machine type availability | Verify the required type is available in your region                                          |
    | vCPU quota                           | Request a regional vCPU increase                                                              |
    | Required APIs / providers            | Enable the cloud APIs (GCP) or register the resource providers (Azure) the installer requires |
  </Accordion>

  <Accordion title="Deployment failures">
    If `pulumi up` fails partway through:

    ```bash theme={null}
    pulumi refresh  # Sync state with actual resources
    pulumi up       # Retry deployment
    ```

    On AWS, the slowest single step is VPC endpoint service private DNS verification: roughly 15 minutes of `Waiting for domain verification (pendingVerification)` polling is normal, not a hang. Let it finish.
  </Accordion>

  <Accordion title="Cluster access issues">
    Ensure your cloud credentials match the account where the cluster is deployed:

    <Tabs>
      <Tab title="AWS">
        ```bash theme={null}
        aws sts get-caller-identity
        ```
      </Tab>

      <Tab title="GCP">
        ```bash theme={null}
        gcloud auth list
        gcloud config get-value project
        ```
      </Tab>

      <Tab title="Azure">
        ```bash theme={null}
        az account show
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Workspace stuck initializing">
    The first-run `default` workspace is created asynchronously and becomes ready only once the Nexus services in your deployment are up. If `pulumi up` times out waiting for it, re-run `pulumi up` once the cluster pods are `Running`. If it remains stuck, contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).
  </Accordion>
</AccordionGroup>

For additional help, see the [GitHub Issues](https://github.com/pinecone-io/pulumi-pinecone-nexus-byoc/issues) for the deployment repository.
