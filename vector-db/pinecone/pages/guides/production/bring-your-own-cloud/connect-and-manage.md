---
title: "Connect to and manage BYOC"
source: https://docs.pinecone.io/guides/production/bring-your-own-cloud/connect-and-manage
path: guides/production/bring-your-own-cloud/connect-and-manage
---

Connect to your Pinecone BYOC indexes over public or private networking, and manage, monitor, and tear down your BYOC deployment.

Once your BYOC environment is deployed, connect to your indexes over public or private networking, then monitor and maintain the deployment.

## Connect to your index

How you connect to your indexes for data plane operations like [querying](/reference/api/latest/data-plane/query), [upserting](/reference/api/latest/data-plane/upsert), and [fetching](/reference/api/latest/data-plane/fetch) vectors depends on your network access mode.

> [!NOTE]
>
> BYOC doesn't support reading and writing data from the index browser in the Pinecone console.

### Connect over the public endpoint

Use the `host` URL from the Pinecone console or the [Describe an index](/reference/api/latest/control-plane/describe_index) API response. For example:

```
https://my-index-abc123.svc.us-east-1.byoc.pinecone.io
```

Connect from anywhere using the standard Pinecone SDK or API.

### Connect over a private endpoint

With public access disabled, you can only connect from within your VPC via private connectivity. Control plane operations (create, delete, list indexes) still work.

After deployment, the Pulumi stack outputs include the service name needed to create a private endpoint for your cloud provider. Use this service name to set up private connectivity:

**AWS**

**1. Create a VPC endpoint**

Follow the instructions in the AWS documentation to [create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) for connecting to your indexes via AWS PrivateLink.

For **Resource configurations**, use the VPC endpoint service name from the Pulumi stack outputs.

**2. Select network settings**

For **Network settings**, select the VPC for your BYOC deployment.

**3. Enable DNS name**

In **Additional settings**, select **Enable DNS name** to allow you to access your indexes using a DNS name.

**GCP**

**1. Create a private endpoint**

Follow the instructions in the GCP documentation to [create a private endpoint](https://cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) for connecting to your indexes via GCP Private Service Connect.

* Set the **Target service** to the service attachment from the Pulumi stack outputs.
* Copy the IP address of the private endpoint. You'll need it later.

**2. Create a private DNS zone**

Follow the instructions in the GCP documentation to [create a private DNS zone](https://cloud.google.com/dns/docs/zones#create-private-zone).

* Set the **DNS name** to the following:

  ```
  <YOUR-BYOC-ENVIRONMENT>.byoc.pinecone.io
  ```
* Select the same VPC network as the private endpoint.

**3. Add a resource record set**

Follow the instructions in the GCP documentation to [add a resource record set](https://cloud.google.com/dns/docs/records#add-rrset).

* Set the **DNS name** to **\***.

* Set the **Resource record type** to **A**.

* Set the **Ipv4 Address** to the IP address of the private endpoint.

**Azure**

**1. Create a private endpoint**

Follow the instructions in the Azure documentation to [create a private endpoint](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal) for connecting to your indexes via Azure Private Link.

* Set the **Resource type** to `Microsoft.Network/privateLinkServices`.
* Select the Private Link Service name from the Pulumi stack outputs.
* Copy the IP address of the private endpoint. You'll need it later.

**2. Create a private DNS zone**

Follow the instructions in the Azure documentation to [create a private DNS zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal).

* Set the **Name** to the following:

  ```
  <YOUR-BYOC-ENVIRONMENT>.byoc.pinecone.io
  ```
* Link the zone to the VNet containing the private endpoint.

**3. Add a wildcard A record**

Follow the instructions in the Azure documentation to [add a record set](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#create-an-additional-dns-record).

* Set the **Name** to **\***.

* Set the **Type** to **A**.

* Set the **IP address** to the IP address of the private endpoint.

Once configured, use the `private_host` URL from the Pinecone console or the [Describe an index](/reference/api/latest/control-plane/describe_index) API response. For example:

```
https://my-index-abc123.svc.private.us-east-1.byoc.pinecone.io
```

## Manage BYOC

Pinecone handles upgrades, scaling, and maintenance through the in-cluster agent. You monitor the deployment and tear it down when you no longer need it.

### Operations and upgrades

Pinecone uses a pull-based model for cluster operations:

1. When upgrades, scaling, or maintenance are needed, Pinecone queues operations in the control plane.
2. An agent running in your cluster (deployed automatically during setup) continuously pulls pending operations.
3. Operations execute locally within your cluster.
4. Status is reported back to Pinecone for monitoring.

This model ensures Pinecone never needs direct access to your infrastructure. All operations are stored as Kubernetes CRDs, providing a complete audit trail.

### Monitoring

You can monitor your BYOC deployment through multiple channels:

> **Pinecone console**
>
> View index metrics (read/write units, latency, storage) in the Pinecone console. Control plane operations and metrics work regardless of your network access mode.

> **Prometheus**
>
> To use [Prometheus](/guides/production/monitoring#monitor-with-prometheus), configure your monitoring tool within your VPC to scrape metrics from the cluster. Your Prometheus instance must have network access to the BYOC VPC. The deployment output includes the metrics endpoint URL and port for configuration.

> **Audit logs**
>
> All cluster operations are persisted as Kubernetes CRDs for compliance and auditing:
>
> ```bash theme={null}
> kubectl get cluster-operations
> ```

### Cleanup

To destroy your BYOC deployment:

> [!WARNING]
>
> Delete all BYOC indexes before destroying the cluster. Indexes cannot be properly terminated if the cluster is destroyed first.

```bash theme={null}
# 1. Delete all indexes via Pinecone API or console
# 2. Then destroy the infrastructure
pulumi destroy
```

If `deletion-protection` is enabled (the default), you must either disable it in `Pulumi.<stack>.yaml` and run `pulumi up`, or manually delete protected resources via the cloud console before running `pulumi destroy`:

* **AWS**: S3 buckets
* **GCP**: GCS buckets
* **Azure**: storage accounts
