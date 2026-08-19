---
title: "Configure Private Endpoints"
source: https://docs.pinecone.io/guides/production/configure-private-endpoints
path: guides/production/configure-private-endpoints
---

Configure Pinecone Private Endpoints with AWS PrivateLink or Azure Private Link to keep index traffic off the public internet and secure VPCs.

This page describes how to create and use [Private Endpoints](/guides/production/security-overview#private-endpoints) to connect to Pinecone through AWS PrivateLink or Azure Private Link, keeping your traffic private from the public internet.

<a />

## Use Private Endpoints with Pinecone

### Before you begin

The following steps assume you have:

<Tabs>
  <Tab title="AWS">
    * Access to the [AWS console](https://console.aws.amazon.com/console/home).
    * [Created an Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources) in the same AWS [region](/guides/index-data/create-an-index#cloud-regions) as the index you want to connect to. You can optionally enable DNS hostnames and resolution, if you want your VPC to automatically discover the DNS CNAME for your PrivateLink and do not want to configure a CNAME.

      * To [configure the routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) yourself, use one of Pinecone's DNS entry for the corresponding region:

      | Index region                 | Pinecone DNS entry                     |
      | ---------------------------- | -------------------------------------- |
      | `us-east-1` (N. Virginia)    | `*.private.aped-4627-b74a.pinecone.io` |
      | `us-west-2` (Oregon)         | `*.private.apw5-4e34-81fa.pinecone.io` |
      | `eu-west-1` (Ireland)        | `*.private.apu-57e2-42f6.pinecone.io`  |
      | `eu-central-1` (Frankfurt)   | `*.private.apec-a2ee-38c6.pinecone.io` |
      | `ap-southeast-1` (Singapore) | `*.private.aps-d9bb-582b.pinecone.io`  |
  </Tab>

  <Tab title="Azure">
    * Access to the [Azure portal](https://portal.azure.com).
    * [Created an Azure VNet](https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-portal) in the same [region](/guides/index-data/create-an-index#cloud-regions) as the index you want to connect to.
    * A subnet with **Private endpoint network policies** set to **Disabled**. This is required for Azure Private Endpoints.

      * DNS resolution for private endpoints requires a manual setup step after creating the endpoint (unlike AWS, where DNS can be auto-configured). See the [DNS setup note below](#1-create-a-private-endpoint-in-your-cloud-provider).

      | Index region         | Pinecone DNS entry                              |
      | -------------------- | ----------------------------------------------- |
      | `eastus2` (Virginia) | `*.private.eastus2-5e25.prod-azure.pinecone.io` |
  </Tab>
</Tabs>

* A [Pinecone Enterprise plan](https://www.pinecone.io/pricing/).
* [Created a serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in the same [region](/guides/index-data/create-an-index#cloud-regions) as your VPC or VNet.

<Note>
  Private Endpoints are configured at the project-level and you can add up to 10 endpoints per project. If you have multiple projects in your organization, Private Endpoints need to be set up separately for each.
</Note>

<a />

### 1. Create a private endpoint in your cloud provider

<Tabs>
  <Tab title="AWS">
    In the [AWS console](https://console.aws.amazon.com/console/home):

    1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

    2. In the navigation pane, click **Endpoint**.

    3. Click **Create endpoint**.

    4. For **Service category**, select **Other endpoint services**.

    5. In **Service settings**, enter the **Service name**, based on the region your Pinecone index is in:
       | Index region                 | Service name                                                   |
       | ---------------------------- | -------------------------------------------------------------- |
       | `us-east-1` (N. Virginia)    | `com.amazonaws.vpce.us-east-1.vpce-svc-05ef6f1f0b9130b54`      |
       | `us-west-2` (Oregon)         | `com.amazonaws.vpce.us-west-2.vpce-svc-04ecb9a0e0d5aab01`      |
       | `eu-west-1` (Ireland)        | `com.amazonaws.vpce.eu-west-1.vpce-svc-03c6b7e17ff02a70f`      |
       | `eu-central-1` (Frankfurt)   | `com.amazonaws.vpce.eu-central-1.vpce-svc-037997ff6b3d25e34`   |
       | `ap-southeast-1` (Singapore) | `com.amazonaws.vpce.ap-southeast-1.vpce-svc-0c12f00812e786068` |

    6. Click **Verify service**.

    7. Select the **VPC** to host the endpoint.

    8. (Optional) In **Additional settings**, **Enable DNS name**.
       The enables you to access our service with the DNS name we configure. An additional CNAME record is needed if you disable this option.

    9. Select the **Subnets** and **Subnet ID** for the endpoint.

    10. Select the **Security groups** to apply to the endpoint.

    11. Click **Create endpoint**.

    12. Copy the **VPC endpoint ID** (e.g., `vpce-XXXXXXX`).
        This will be used to [add a Private Endpoint in Pinecone](#2-add-a-private-endpoint-in-pinecone).
  </Tab>

  <Tab title="Azure">
    In the [Azure portal](https://portal.azure.com):

    1. Search for **Private Link** and select **Private Link Center**.

    2. In the navigation pane, click **Private endpoints**.

    3. Click **Create**.

    4. Select your **Subscription** and **Resource group**.

    5. Enter a **Name** for the private endpoint and select the **Region** matching your Pinecone index.

    6. Click **Next: Resource**.

    7. For **Connection method**, select **Connect to an Azure resource by resource ID or alias**.

    8. Enter the **Resource ID or alias** for Pinecone's Private Link Service, based on the region your Pinecone index is in:

       | Index region         | Private Link Service alias                                                       |
       | -------------------- | -------------------------------------------------------------------------------- |
       | `eastus2` (Virginia) | `pinecone.bdbc7759-0243-46c1-af51-794c4602745b.eastus2.azure.privatelinkservice` |

    9. Click **Next: Virtual Network**.

    10. Select the **Virtual network** and **Subnet** for the private endpoint.

    11. Click **Next: DNS**. Skip the DNS integration tab (you will configure DNS manually after setup).

    12. Click **Next: Tags**.

    13. Click **Review + create**, then **Create**.

    14. Once the private endpoint is created, open it and copy the **Resource ID** from the **Properties** tab (or the **Overview** tab — it's the `/subscriptions/…/privateEndpoints/<name>` ARM ID).
        This will be used to [add a Private Endpoint in Pinecone](#2-add-a-private-endpoint-in-pinecone).

    <Note>
      After creating the private endpoint, configure DNS so that `*.private.{subdomain}.pinecone.io` resolves to your private endpoint's IP address:

      1. Find your private endpoint's IP address: in the Azure portal, open your private endpoint, go to **Overview**, and note the **Private IP address** (e.g., `172.30.0.6`).
      2. Create an [Azure Private DNS Zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal) named `private.{subdomain}.pinecone.io` (e.g., `private.eastus2-5e25.prod-azure.pinecone.io`). You can find the `{subdomain}` in your index's host URL — it's the portion after `svc.` and before `.pinecone.io`.
      3. [Link the zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links) to the VNet where your private endpoint is created.
      4. Add a **wildcard A record** (`*`) pointing to your private endpoint's IP address.
    </Note>
  </Tab>
</Tabs>

### 2. Add a Private Endpoint in Pinecone

To add a Private Endpoint using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
3. Click **Add a connection**.
4. Select your cloud provider and region.
   Only indexes in the selected region in this project will be affected.
5. Click **Next**.
6. Enter the endpoint ID you copied in the [section above](#1-create-a-private-endpoint-in-your-cloud-provider):
   * **AWS**: The VPC endpoint ID (e.g., `vpce-XXXXXXX`)
   * **Azure**: The private endpoint's ARM Resource ID (e.g., `/subscriptions/<sub-uuid>/resourceGroups/<rg>/providers/Microsoft.Network/privateEndpoints/<name>`)
7. Click **Next**.
8. (optional) To **enable private endpoint access only**, turn the toggle on.
   This can also be enabled later. For more information, see [Manage internet access to your project](#manage-internet-access-to-your-project).
9. Click **Finish setup**.

<Note>
  Private Endpoints only affect [data plane](/guides/get-started/database-architecture#data-plane) access. [Control plane](/guides/get-started/database-architecture#control-plane) access will continue over the public internet.
</Note>

## Read and write data

Once your private endpoint is configured, you can run data operations against an index as usual, but you must target the index using its private endpoint URL. The only difference in the URL is that `.svc.` is changed to `.svc.private.`.

You can get the private endpoint URL for an index from the Pinecone console or API.

<Tabs>
  <Tab title="Console">
    To get the private endpoint URL for an index from the Pinecone console:

    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index.
    3. Select the index.
    4. Copy the URL under **PRIVATE ENDPOINT**.
  </Tab>

  <Tab title="API">
    To get the private endpoint URL for an index from the API, use the [`describe_index`](/reference/api/latest/control-plane/describe_index) operation, which returns the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      await pc.describeIndex('docs-example');
      ```

      ```go Go theme={null}
      package main

      import (
          "context"
          "encoding/json"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func prettifyStruct(obj interface{}) string {
          bytes, _ := json.MarshalIndent(obj, "", "  ")
          return string(bytes)
      }

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          idx, err := pc.DescribeIndex(ctx, "docs-example")
          if err != nil {
              log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
          } else {
              fmt.Printf("index: %v\n", prettifyStruct(idx))
          }
      }
      ```

      ```bash curl theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
          -H "Api-Key: YOUR_API_KEY" \
          -H "X-Pinecone-Api-Version: 2025-10"
      ```
    </CodeGroup>

    The response includes the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```json JavaScript {6} theme={null}
      {
        name: 'docs-example',
        dimension: 1536,
        metric: 'cosine',
        host: 'docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io',
        privateHost: 'docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io',
        deletionProtection: 'disabled',
        tags: { environment: 'production' },
        embed: undefined,
        spec: {
          byoc: undefined,
          pod: undefined,
          serverless: { cloud: 'aws', region: 'us-east-1' }
        },
        status: { ready: true, state: 'Ready' },
        vectorType: 'dense'
      }
      ```

      ```go Go {5} theme={null}
      index: {
        "name": "docs-example",
        "dimension": 1536,
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "metric": "cosine",
        "deletion_protection": "disabled",
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "tags": {
          "environment": "production"
        }
      }
      ```

      ```json curl {12} theme={null}
      {
        "id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
        "vector_type": "dense",
        "name": "docs-example",
        "metric": "cosine",
        "dimension": 1536,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "spec": {
          "serverless": {
            "region": "us-east-1",
            "cloud": "aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": {
          "environment": "production"
        }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  If you run data operations against an index from outside the Private Endpoint, you will get an `Unauthorized` response.
</Note>

## Manage internet access to your project

Once your Private Endpoint is configured, you can turn off internet access to your project. To enable private endpoint access only:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select your project.
3. Go to **Network > Access**.
4. Turn the **Private endpoint access only** toggle on.
   This will turn off internet access to the project. This can be turned off at any point.

   <Warning>
     This access control is set at the *project-level* and can unintentionally affect Pinecone indexes that communicate via the internet in the same project. Only indexes communicating through Private Endpoints will continue to work.
   </Warning>

## Manage Private Endpoints

In addition to [creating Private Endpoints](#2-add-a-private-endpoint-in-pinecone), you can also:

* [View Private Endpoints](#view-private-endpoints)
* [Delete a Private Endpoint](#delete-a-private-endpoint)

### View Private Endpoints

To view Private Endpoints using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
   A list of Private Endpoints displays with the associated endpoint ID and cloud provider.

### Delete a Private Endpoint

To delete a Private Endpoint using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
3. For the Private Endpoint you want to delete, click the *...* (Actions) icon.
4. Click **Delete**.
5. Enter the endpoint name.
6. Click **Delete Endpoint**.
