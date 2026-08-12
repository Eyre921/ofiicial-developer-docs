---
title: "Bring your own cloud (BYOC)"
source: https://docs.pinecone.io/guides/production/bring-your-own-cloud
path: guides/production/bring-your-own-cloud
---

Deploy Pinecone BYOC in your own AWS, GCP, or Azure account for data sovereignty, network isolation, and regional data residency requirements.

<Note>
  BYOC is in [public preview](/release-notes/feature-availability) on AWS, GCP, and Azure.
</Note>

Pinecone BYOC (bring your own cloud) is designed for organizations with strict requirements around data sovereignty, network isolation, and data residency.

With BYOC, you deploy the Pinecone data plane in your own cloud account (AWS, GCP, or Azure), and you get the benefits of a managed service — upgrades, scaling, and maintenance — without giving up control of your data or infrastructure.

Pinecone never has direct access to your cloud account. Your vectors, metadata, and queries never leave your environment, and no inbound network access is required. An agent in your cluster pulls operations from Pinecone and executes them locally.

<img alt="BYOC architecture diagram" />

<img alt="BYOC architecture diagram" />

BYOC uses a split architecture:

* The data plane runs entirely in your cloud account within a dedicated VPC, storing and processing your vectors, executing queries, and managing index data in object storage (S3 on AWS, GCS on GCP, or Azure Blob Storage on Azure).
* The control plane is managed by Pinecone globally and handles index lifecycle management, authentication, billing, and user management, but never stores or processes your vectors.

For maintenance, the agent authenticates with Pinecone's control plane, pulls pending operations (upgrades, scaling, etc.), and executes them locally. All operations are stored as Kubernetes CRDs, providing a complete audit trail.

Only operational metrics (CPU, memory, latency) and traces are transmitted to Pinecone for monitoring; customer data is filtered out before transmission.

## Encryption and customer-managed keys

In the **standard Pinecone service**, [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) are how you connect Pinecone-managed storage to **your** AWS KMS keys through the Pinecone console.

In **BYOC**, your vectors and index data are stored in **your** cloud account (for example object storage, databases, and block volumes). You apply your cloud provider’s KMS to those resources using the same native controls you use for other workloads (key policies, rotation, and compliance programs such as PCI or ISO 27001). When you deploy with [pulumi-pinecone-byoc](https://github.com/pinecone-io/pulumi-pinecone-byoc), you can supply your KMS key where the template supports it; see that repository’s README for current options. This is not the console **CMEK** flow used for hosted projects.

## Prerequisites

Before deploying BYOC, ensure you have the following tools installed on your local machine:

| Tool         | Purpose                | Install                                                                      |
| ------------ | ---------------------- | ---------------------------------------------------------------------------- |
| Python 3.12+ | Runtime                | [python.org](https://www.python.org/downloads/)                              |
| uv           | Package manager        | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
| Pulumi       | Infrastructure-as-code | [pulumi.com/docs/install](https://www.pulumi.com/docs/install/)              |
| kubectl      | Cluster access         | [kubernetes.io](https://kubernetes.io/docs/tasks/tools/)                     |

You also need:

* The CLI for your cloud provider:
  * **AWS**: [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
  * **GCP**: [gcloud CLI](https://cloud.google.com/sdk/docs/install)
  * **Azure**: [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* A cloud account with admin-level permissions:
  * **AWS**: `AdministratorAccess`. `PowerUserAccess` is not sufficient because BYOC creates IAM roles and policies.
  * **GCP**: `roles/owner`. `roles/editor` is not sufficient because BYOC creates IAM service accounts and bindings.
  * **Azure**: `Owner` on the subscription. `Contributor` is not sufficient because BYOC creates managed identities and role assignments.
* Sufficient cloud quota for the resources (the setup wizard validates this)
* A Pinecone API key from the Pinecone console.
* A Pinecone Enterprise plan (required for BYOC access)

<Note>
  If you install any new tools, open a new terminal session before proceeding so that your shell picks up the updated PATH and environment.
</Note>

## Deploy BYOC

To deploy BYOC, follow these steps:

<Steps>
  <Step title="Run the setup wizard">
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

    <Accordion title="Setup wizard prompts">
      The wizard prompts you for the following:

      | Prompt                    | Description                                                                                                                                    | Default                                                    |
      | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
      | **Cloud provider**        | Select AWS, GCP, or Azure (skipped if pre-selected via `--cloud`).                                                                             | -                                                          |
      | **Pinecone API key**      | Your API key from the Pinecone console (or uses `PINECONE_API_KEY` env var).                                                                   | -                                                          |
      | **Cloud credentials**     | Validates credentials and displays your account/project/subscription ID.                                                                       | -                                                          |
      | **GCP project ID**        | *(GCP only)* Your GCP project ID.                                                                                                              | Detected from `gcloud`                                     |
      | **Azure subscription ID** | *(Azure only)* Your Azure subscription ID.                                                                                                     | Detected from `az account show`                            |
      | **Region**                | Region for deployment.                                                                                                                         | `us-east-1` (AWS) / `us-central1` (GCP) / `eastus` (Azure) |
      | **Availability zones**    | Zones for high availability. Wizard fetches available options.                                                                                 | First two zones                                            |
      | **Custom AMI**            | *(AWS only)* Custom AMI ID for EKS nodes. Leave blank for the default AWS AMI.                                                                 | None                                                       |
      | **VPC CIDR block**        | IP range for your VPC/VNet. Choose a range that doesn't conflict with existing networks.                                                       | `10.0.0.0/16` (AWS/Azure) / `10.112.0.0/12` (GCP)          |
      | **Deletion protection**   | Protect databases and storage from accidental deletion.                                                                                        | Enabled                                                    |
      | **Network access**        | Public access (connect from anywhere) or private only (requires PrivateLink on AWS, Private Service Connect on GCP, or Private Link on Azure). | Public enabled                                             |
      | **Resource tags/labels**  | Custom tags (AWS/Azure) or labels (GCP) for cost tracking (e.g., `team=platform,env=prod`).                                                    | None                                                       |
      | **Preflight checks**      | Validates cloud quotas. If checks fail, request quota increases before proceeding.                                                             | -                                                          |
      | **Project name**          | Name for your deployment.                                                                                                                      | `pinecone-byoc`                                            |
      | **Pulumi backend**        | Where to store state: local (`~/.pulumi` with passphrase) or Pulumi Cloud.                                                                     | Local                                                      |
    </Accordion>

    After completing the wizard, a Pulumi project is generated in your project directory.

    <Accordion title="Generated configuration file">
      The wizard creates a `Pulumi.<stack>.yaml` file with configurable options. The options vary by cloud provider:

      <Tabs>
        <Tab title="AWS">
          | Option                  | Description                                         | Default                        |
          | ----------------------- | --------------------------------------------------- | ------------------------------ |
          | `pinecone-version`      | Pinecone release version                            | -                              |
          | `region`                | AWS region                                          | `us-east-1`                    |
          | `availability-zones`    | Availability zones for high availability            | `["us-east-1a", "us-east-1b"]` |
          | `vpc-cidr`              | VPC IP range                                        | `10.0.0.0/16`                  |
          | `deletion-protection`   | Protect RDS and S3 from accidental deletion         | `true`                         |
          | `public-access-enabled` | Enable public endpoint (`false` = PrivateLink only) | `true`                         |
          | `custom-ami-id`         | Custom AMI ID for EKS nodes                         | Default AWS AMI                |
          | `tags`                  | Custom tags for all AWS resources                   | `{}`                           |
        </Tab>

        <Tab title="GCP">
          | Option                  | Description                                                     | Default                              |
          | ----------------------- | --------------------------------------------------------------- | ------------------------------------ |
          | `gcp:project`           | GCP project ID                                                  | -                                    |
          | `pinecone-version`      | Pinecone release version                                        | -                                    |
          | `region`                | GCP region                                                      | `us-central1`                        |
          | `availability-zones`    | Zones for high availability                                     | `["us-central1-a", "us-central1-b"]` |
          | `vpc-cidr`              | VPC IP range                                                    | `10.112.0.0/12`                      |
          | `deletion-protection`   | Protect AlloyDB and GCS from accidental deletion                | `true`                               |
          | `public-access-enabled` | Enable public endpoint (`false` = Private Service Connect only) | `true`                               |
          | `labels`                | Custom labels for all GCP resources                             | `{}`                                 |
        </Tab>

        <Tab title="Azure">
          | Option                  | Description                                                             | Default       |
          | ----------------------- | ----------------------------------------------------------------------- | ------------- |
          | `subscription-id`       | Azure subscription ID                                                   | -             |
          | `pinecone-version`      | Pinecone release version                                                | -             |
          | `region`                | Azure region                                                            | `eastus`      |
          | `availability-zones`    | Zones for high availability                                             | `["1", "2"]`  |
          | `vpc-cidr`              | VNet IP range                                                           | `10.0.0.0/16` |
          | `deletion-protection`   | Protect PostgreSQL Flexible Server and storage from accidental deletion | `true`        |
          | `public-access-enabled` | Enable public endpoint (`false` = Private Link only)                    | `true`        |
          | `tags`                  | Custom tags for all Azure resources                                     | `{}`          |
        </Tab>
      </Tabs>

      To change configuration after initial setup, edit `Pulumi.<stack>.yaml` and run `pulumi up`.
    </Accordion>

    <Accordion title="Programmatic usage">
      For advanced users who want to integrate BYOC into existing Pulumi infrastructure, the `pulumi-pinecone-byoc` package is available on [PyPI](https://pypi.org/project/pulumi-pinecone-byoc/). Install with cloud-specific dependencies:

      ```bash theme={null}
      # For AWS
      uv add 'pulumi-pinecone-byoc[aws]'

      # For GCP
      uv add 'pulumi-pinecone-byoc[gcp]'

      # For Azure
      uv add 'pulumi-pinecone-byoc[azure]'
      ```

      Import the cluster class for your cloud provider:

      ```python theme={null}
      # AWS
      from pulumi_pinecone_byoc.aws import PineconeAWSCluster, PineconeAWSClusterArgs

      # GCP
      from pulumi_pinecone_byoc.gcp import PineconeGCPCluster, PineconeGCPClusterArgs

      # Azure
      from pulumi_pinecone_byoc.azure import PineconeAzureCluster, PineconeAzureClusterArgs
      ```

      See the [repository README](https://github.com/pinecone-io/pulumi-pinecone-byoc#programmatic-usage) for full usage examples.
    </Accordion>
  </Step>

  <Step title="Deploy the infrastructure">
    Deploy the generated Pulumi project to create your cloud resources:

    ```bash theme={null}
    cd pinecone-byoc
    pulumi up
    ```

    Pulumi shows a preview of all resources to be created. Confirm to proceed. Provisioning takes approximately 25-30 minutes.

    When complete, the output displays:

    * Your BYOC **environment name** (used when creating indexes).
    * The **kubectl command** to configure cluster access.

    <Accordion title="Infrastructure provisioned">
      The deployment creates the following resources in your cloud account:

      | Component            | AWS                                                             | GCP                                                 | Azure                                            |
      | -------------------- | --------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ |
      | **VPC / Networking** | VPC, public and private subnets, NAT gateways, internet gateway | VPC network, subnets, Cloud NAT, Cloud Router       | VNet, subnets, NAT gateway                       |
      | **Kubernetes**       | EKS cluster with managed node groups                            | GKE cluster with node pools                         | AKS cluster with agent pools                     |
      | **Object storage**   | S3 buckets (data, WAL, backups)                                 | GCS buckets (data, WAL, backups)                    | Blob Storage containers (data, WAL, backups)     |
      | **Database**         | Aurora PostgreSQL (RDS)                                         | AlloyDB                                             | PostgreSQL Flexible Server                       |
      | **Load balancing**   | Network Load Balancer                                           | Internal load balancer with Private Service Connect | Internal load balancer with Private Link Service |
      | **DNS**              | Route 53 hosted zone                                            | Cloud DNS managed zone                              | Azure DNS zone                                   |
      | **TLS certificates** | AWS Certificate Manager                                         | cert-manager                                        | cert-manager                                     |
      | **IAM**              | IAM roles and policies                                          | Service accounts and Workload Identity              | Managed identities and Workload Identity         |

      The initial deployment provisions 3 Kubernetes nodes. After setup, the cluster autoscales based on the services Pinecone deploys and your workload.
    </Accordion>
  </Step>

  <Step title="Verify the deployment">
    Configure `kubectl` to connect to your cluster using the command from the deployment output:

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

    The above command configures your local `kubectl` tool to communicate with your Kubernetes cluster. You'll use cluster access for administrative tasks like viewing operations and troubleshooting. Creating indexes and reading/writing vectors still use the standard Pinecone API.

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
  </Step>
</Steps>

## Use BYOC

Once your BYOC environment is deployed, you can create indexes and read/write data using the standard Pinecone API.

### Control plane operations

Control plane operations like [creating](/reference/api/latest/control-plane/create_index), [listing](/reference/api/latest/control-plane/list_indexes), and [deleting](/reference/api/latest/control-plane/delete_index) indexes work via the standard Pinecone API regardless of your network access mode.

<Note>
  BYOC supports [dedicated read nodes](/guides/index-data/dedicated-read-nodes) indexes, but not on-demand indexes.
</Note>

<Accordion title="Create an index">
  Use the environment name from the deployment output to create indexes in your BYOC environment. BYOC supports [dedicated read nodes](/guides/index-data/dedicated-read-nodes) indexes only.

  <CodeGroup>
    ```bash curl theme={null}
    PINECONE_API_KEY="YOUR_API_KEY"

    curl -X POST "https://api.pinecone.io/indexes" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -H "Api-Key: $PINECONE_API_KEY" \
         -H "X-Pinecone-Api-Version: 2025-10" \
         -d '{
               "name": "example-byoc-index",
               "dimension": 1536,
               "metric": "cosine",
               "vector_type": "dense",
               "spec": {
                 "byoc": {
                   "environment": "aws-us-east-1-26bf.byoc",
                   "read_capacity": {
                     "mode": "Dedicated",
                     "dedicated": {
                       "node_type": "b1",
                       "scaling": "Manual",
                       "manual": {
                         "shards": 1,
                         "replicas": 1
                       }
                     }
                   }
                 }
               },
               "deletion_protection": "disabled"
             }'
    ```

    ```python Python theme={null}
    from pinecone import Pinecone
    from pinecone.db_control.models import ByocSpec

    pc = Pinecone(api_key="YOUR_API_KEY")

    pc.db.index.create(
        name="example-byoc-index",
        dimension=1536,
        metric="cosine",
        vector_type="dense",
        spec=ByocSpec(
            environment="aws-us-east-1-26bf.byoc",
            read_capacity={
                "mode": "Dedicated",
                "dedicated": {
                    "node_type": "b1",
                    "scaling": "Manual",
                    "manual": {
                        "shards": 1,
                        "replicas": 1,
                    },
                },
            },
        ),
        deletion_protection="disabled",
    )
    ```
  </CodeGroup>
</Accordion>

### Data plane operations

Data plane operations like [querying](/reference/api/latest/data-plane/query), [upserting](/reference/api/latest/data-plane/upsert), and [fetching](/reference/api/latest/data-plane/fetch) vectors depend on your network access mode.

<Note>
  BYOC does not support reading and writing data from the index browser in the Pinecone console.
</Note>

<AccordionGroup>
  <Accordion title="Public access enabled (default)">
    Use the `host` URL from the Pinecone console or the [Describe an index](/reference/api/latest/control-plane/describe_index) API response. For example:

    ```
    https://my-index-abc123.svc.us-east-1.byoc.pinecone.io
    ```

    Connect from anywhere using the standard Pinecone SDK or API.
  </Accordion>

  <Accordion title="Public access disabled">
    With public access disabled, you can only connect from within your VPC via private connectivity. You cannot use the Pinecone console for data plane operations (query, upsert, fetch), though control plane operations (create, delete, list indexes) still work.

    After deployment, the Pulumi stack outputs include the service name needed to create a private endpoint for your cloud provider. Use this service name to set up private connectivity:

    <Tabs>
      <Tab title="AWS">
        <Steps>
          <Step title="Create a VPC endpoint">
            Follow the instructions in the AWS documentation to [create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) for connecting to your indexes via AWS PrivateLink.

            For **Resource configurations**, use the VPC endpoint service name from the Pulumi stack outputs.
          </Step>

          <Step title="Select network settings">
            For **Network settings**, select the VPC for your BYOC deployment.
          </Step>

          <Step title="Enable DNS name">
            In **Additional settings**, select **Enable DNS name** to allow you to access your indexes using a DNS name.
          </Step>
        </Steps>
      </Tab>

      <Tab title="GCP">
        <Steps>
          <Step title="Create a private endpoint">
            Follow the instructions in the GCP documentation to [create a private endpoint](https://cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) for connecting to your indexes via GCP Private Service Connect.

            * Set the **Target service** to the service attachment from the Pulumi stack outputs.
            * Copy the IP address of the private endpoint. You'll need it later.
          </Step>

          <Step title="Create a private DNS zone">
            Follow the instructions in the GCP documentation to [create a private DNS zone](https://cloud.google.com/dns/docs/zones#create-private-zone).

            * Set the **DNS name** to the following:

              ```
              <YOUR-BYOC-ENVIRONMENT>.byoc.pinecone.io
              ```
            * Select the same VPC network as the private endpoint.
          </Step>

          <Step title="Add a resource record set">
            Follow the instructions in the GCP documentation to [add a resource record set](https://cloud.google.com/dns/docs/records#add-rrset).

            * Set the **DNS name** to **\***.

            * Set the **Resource record type** to **A**.

            * Set the **Ipv4 Address** to the IP address of the private endpoint.
          </Step>
        </Steps>
      </Tab>

      <Tab title="Azure">
        <Steps>
          <Step title="Create a private endpoint">
            Follow the instructions in the Azure documentation to [create a private endpoint](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal) for connecting to your indexes via Azure Private Link.

            * Set the **Resource type** to `Microsoft.Network/privateLinkServices`.
            * Select the Private Link Service name from the Pulumi stack outputs.
            * Copy the IP address of the private endpoint. You'll need it later.
          </Step>

          <Step title="Create a private DNS zone">
            Follow the instructions in the Azure documentation to [create a private DNS zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal).

            * Set the **Name** to the following:

              ```
              <YOUR-BYOC-ENVIRONMENT>.byoc.pinecone.io
              ```
            * Link the zone to the VNet containing the private endpoint.
          </Step>

          <Step title="Add a wildcard A record">
            Follow the instructions in the Azure documentation to [add a record set](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#create-an-additional-dns-record).

            * Set the **Name** to **\***.

            * Set the **Type** to **A**.

            * Set the **IP address** to the IP address of the private endpoint.
          </Step>
        </Steps>
      </Tab>
    </Tabs>

    Once configured, use the `private_host` URL from the Pinecone console or the [Describe an index](/reference/api/latest/control-plane/describe_index) API response. For example:

    ```
    https://my-index-abc123.svc.private.us-east-1.byoc.pinecone.io
    ```
  </Accordion>
</AccordionGroup>

## Manage BYOC

### Operations and upgrades

Pinecone uses a pull-based model for cluster operations:

1. When upgrades, scaling, or maintenance are needed, Pinecone queues operations in the control plane.
2. An agent running in your cluster (deployed automatically during setup) continuously pulls pending operations.
3. Operations execute locally within your cluster.
4. Status is reported back to Pinecone for monitoring.

This model ensures Pinecone never needs direct access to your infrastructure. All operations are stored as Kubernetes CRDs, providing a complete audit trail.

### Monitoring

You can monitor your BYOC deployment through multiple channels:

<AccordionGroup>
  <Accordion title="Pinecone console">
    View index metrics (read/write units, latency, storage) in the Pinecone console. Control plane operations and metrics work regardless of your network access mode.
  </Accordion>

  <Accordion title="Prometheus">
    To use Prometheus, configure your monitoring tool within your VPC to scrape metrics from the cluster. Your Prometheus instance must have network access to the BYOC VPC. The deployment output includes the metrics endpoint URL and port for configuration.
  </Accordion>

  <Accordion title="Audit logs">
    All cluster operations are persisted as Kubernetes CRDs for compliance and auditing:

    ```bash theme={null}
    kubectl get cluster-operations
    ```
  </Accordion>
</AccordionGroup>

### Cleanup

To destroy your BYOC deployment:

<Warning>
  Delete all BYOC indexes before destroying the cluster. Indexes cannot be properly terminated if the cluster is destroyed first.
</Warning>

```bash theme={null}
# 1. Delete all indexes via Pinecone API or console
# 2. Then destroy the infrastructure
pulumi destroy
```

If `deletion_protection` is enabled (the default), you must either disable it in `Pulumi.<stack>.yaml` and run `pulumi up`, or manually delete protected resources via the cloud console before running `pulumi destroy`:

* **AWS**: RDS instances and S3 buckets
* **GCP**: AlloyDB instances and GCS buckets
* **Azure**: PostgreSQL Flexible Server instances and Storage accounts

## Reference

### Troubleshooting

Common issues and how to resolve them:

<AccordionGroup>
  <Accordion title="Preflight check failures">
    The setup wizard validates cloud quotas before deployment. If checks fail:

    | Check                                | Resolution                                                                                                                                                                                                                          |
    | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | VPC / network quota                  | Request a limit increase via your cloud provider's quota console                                                                                                                                                                    |
    | Kubernetes cluster quota             | Request an EKS, GKE, or AKS cluster limit increase                                                                                                                                                                                  |
    | IP address quota                     | Release unused IPs or request a limit increase                                                                                                                                                                                      |
    | Instance / machine type availability | Verify the required type is available in your region                                                                                                                                                                                |
    | vCPU quota (Azure)                   | Request a "Total Regional vCPUs" increase via the Azure Portal (minimum 8 required)                                                                                                                                                 |
    | VM SKU availability (Azure)          | Verify `Standard_D4s_v5` and L-series SKUs are available in your region                                                                                                                                                             |
    | Resource providers (Azure)           | Register required providers: `Microsoft.Compute`, `Microsoft.ContainerService`, `Microsoft.DBforPostgreSQL`, `Microsoft.Storage`, `Microsoft.Network`, `Microsoft.KeyVault`, `Microsoft.ManagedIdentity`, `Microsoft.Authorization` |
    | Required APIs (GCP only)             | Enable Compute Engine, GKE, AlloyDB, Cloud Storage, and Cloud DNS                                                                                                                                                                   |
  </Accordion>

  <Accordion title="Deployment failures">
    If `pulumi up` fails partway through:

    ```bash theme={null}
    pulumi refresh  # Sync state with actual resources
    pulumi up       # Retry deployment
    ```
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

  <Accordion title="Index stuck in terminating state">
    If you destroyed the cluster before deleting indexes, indexes may be stuck in a "terminating" state. Contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket) for assistance.
  </Accordion>
</AccordionGroup>

For additional help, see the [GitHub Issues](https://github.com/pinecone-io/pulumi-pinecone-byoc/issues) for the deployment repository.

### Limitations

Some features available in the standard Pinecone service are not yet supported or have constraints in BYOC:

* Each organization can have up to 2 BYOC environments. To request an increase, contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).
* [Integrated embedding and inference](/guides/index-data/indexing-overview#integrated-embedding), which relies on models hosted by Pinecone outside your cloud account.
* Reading and writing data from the index browser in the Pinecone console.
* Pinecone CLI data plane operations (queries, upserts, fetches). Control plane operations (create, list, delete indexes) work as expected.
* Imports from private cloud storage buckets, unless the bucket is in the same cloud account as your BYOC deployment.
* On-demand indexes (initial release supports DRN indexes only).

To [monitor with Prometheus](/guides/production/monitoring#monitor-with-prometheus), you must configure Prometheus within your VPC.

### FAQs

Answers to common questions about BYOC:

<AccordionGroup>
  <Accordion title="Does Pinecone have access to my cloud account?">
    No. BYOC is designed so Pinecone never needs direct access to your infrastructure. Specifically:

    * Pinecone does not need SSH, VPN, or inbound access to your cluster.
    * You control cloud account boundaries, networking, and Kubernetes access.
    * Operational changes run through explicit, software-mediated workflows.
    * You don't open inbound firewall ports for Pinecone operations.

    Operations are executed via a pull-based model where your cluster retrieves and runs operations locally. All communication is outbound from your cluster.
  </Accordion>

  <Accordion title="What data leaves my cluster?">
    **Does not leave your cloud account:**

    * Vectors, metadata, and index contents
    * Query and upsert payloads
    * Customer data

    **Can leave your cloud account:**

    * Operational metrics and traces (for example, CPU, memory, latency)
    * Cluster health and operation status

    Customer data is filtered out before transmission and never leaves your cloud account.
  </Accordion>

  <Accordion title="What is the difference between BYOC and Pinecone's standard service?">
    In the standard service, Pinecone manages all cloud resources and includes their cost in the service fee. In BYOC, you provision and pay for cloud resources directly through your own cloud account, providing greater control, data sovereignty, and access to available cloud credits or discounts.
  </Accordion>

  <Accordion title="How does authentication work?">
    You use API keys from the Pinecone console, just like with the standard Pinecone service. Authentication is handled by Pinecone's global control plane, and your data plane caches API keys locally. This means you manage users and API keys through the console as usual.
  </Accordion>

  <Accordion title="How is data secured in BYOC?">
    Data is stored and processed exclusively within your cloud account, with encryption at rest and in transit. You control at-rest encryption for the underlying resources (including KMS keys in your account) the same way you do for other infrastructure. Communication between the data plane and control plane is encrypted using TLS. Private connectivity (AWS PrivateLink, GCP Private Service Connect, or Azure Private Link) can be used for additional network isolation. For how this relates to hosted [CMEK](/guides/production/configure-cmek), see [Encryption and customer-managed keys](#encryption-and-customer-managed-keys).
  </Accordion>

  <Accordion title="Which cloud providers does BYOC support?">
    BYOC is available on AWS, GCP, and Azure.
  </Accordion>

  <Accordion title="What happens if I destroy the cluster before deleting indexes?">
    Indexes cannot be properly terminated if the cluster is destroyed first. Always delete indexes via the Pinecone API or console before running `pulumi destroy`.
  </Accordion>

  <Accordion title="What is the __SLI__ project in my organization?">
    Deploying a BYOC environment creates an internal project named `__SLI__` in your organization. This is used by Pinecone to enforce SLAs for your BYOC environment. Do not modify or delete this project.
  </Accordion>
</AccordionGroup>

### Pricing

BYOC pricing is based on provisioned resources (compute and storage) in your deployment, metered over time. Usage is measured by the Pinecone BYOC agent running in your cluster, which periodically reports the resources that are provisioned.

What you pay:

* Pinecone fees: Based on provisioned compute (vCPU and RAM) and storage (NVMe) resources
* Cloud provider fees: You pay your cloud provider directly for the underlying infrastructure (Kubernetes nodes, object storage, databases, networking, etc.)

Billing follows the agent heartbeat connection to Pinecone's control plane:

* When heartbeats are received, you are billed for the provisioned compute and storage the agent reports, even if the cluster is unhealthy.
* Short heartbeat interruptions (under 60 minutes) are treated as a grace period.
* If heartbeats are missing for more than 60 minutes, billing stops and the deployment is marked disconnected.

<Note>
  Billing is based on provisioned resources, not query volume. Resources that are running in your cluster are billed whether they are idle, actively processing queries, or experiencing errors.
</Note>
