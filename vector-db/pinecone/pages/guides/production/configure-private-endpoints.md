---
title: "Configure private endpoints"
source: https://docs.pinecone.io/guides/production/configure-private-endpoints
path: guides/production/configure-private-endpoints
---

Configure Pinecone private endpoints with AWS PrivateLink or Azure Private Link to keep index traffic off the public internet.

[Private endpoints](/guides/production/security-overview#private-endpoints) let your applications reach Pinecone indexes through AWS PrivateLink or Azure Private Link, so traffic between your network and Pinecone stays off the public internet.

* Private endpoints carry [data plane](/guides/core-concepts/architecture#data-plane) traffic only. [Control plane](/guides/core-concepts/architecture#control-plane) requests, such as creating or describing an index, still go over the public internet.
* Each private endpoint belongs to one project and connects only to that project's indexes in one region. You can add up to 10 private endpoints per project.

## Before you begin

Make sure you have the following:

* A [Pinecone Enterprise plan](https://www.pinecone.io/pricing/)
* The owner role in the Pinecone project you want to connect to
* A [serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in one of the regions listed in [step 1](#1-create-a-private-endpoint-in-your-cloud-provider)

<Tabs>
  <Tab title="AWS">
    - Access to the [AWS console](https://console.aws.amazon.com/console/home)
    - An [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources) in the same region as your index
  </Tab>

  <Tab title="Azure">
    * Access to the [Azure portal](https://portal.azure.com)
    * An [Azure VNet](https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-portal) in the same region as your index, with a subnet whose **Private endpoint network policies** setting is **Disabled**
  </Tab>
</Tabs>

## Set up a private endpoint

### 1. Create a private endpoint in your cloud provider

Create an endpoint in your VPC or VNet that connects to Pinecone's service in your index's region:

<Tabs>
  <Tab title="AWS">
    1. In the [Amazon VPC console](https://console.aws.amazon.com/vpc/), go to **Endpoints** and click **Create endpoint**.

    2. For **Type**, select **Endpoint services that use NLBs and GWLBs**.

    3. For **Service name**, enter the service name for your index's region, and then click **Verify service**:

       | Index region | Service name |
       | - | - |
       | `us-east-1` (N. Virginia) | `com.amazonaws.vpce.us-east-1.vpce-svc-05ef6f1f0b9130b54` |
       | `us-west-2` (Oregon) | `com.amazonaws.vpce.us-west-2.vpce-svc-04ecb9a0e0d5aab01` |
       | `eu-west-1` (Ireland) | `com.amazonaws.vpce.eu-west-1.vpce-svc-03c6b7e17ff02a70f` |
       | `eu-central-1` (Frankfurt) | `com.amazonaws.vpce.eu-central-1.vpce-svc-037997ff6b3d25e34` |
       | `ap-southeast-1` (Singapore) | `com.amazonaws.vpce.ap-southeast-1.vpce-svc-0c12f00812e786068` |

    4. For **VPC**, select the VPC your clients connect from.

    5. (Optional) In **Additional settings**, select **Enable DNS name**. This lets clients in the VPC resolve Pinecone's private DNS names without extra setup. It requires [DNS hostnames and DNS resolution](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) to be enabled on the VPC. If you leave it off, or clients outside the VPC need to connect, you'll set up DNS yourself in [step 3](#3-configure-dns).

    6. Select the **Subnets** for the endpoint, and select **Security groups** that allow inbound HTTPS (port 443) from your clients.

    7. Click **Create endpoint**.

    8. Copy the **VPC endpoint ID** (e.g., `vpce-XXXXXXX`). You'll enter it in Pinecone in the next step.
  </Tab>

  <Tab title="Azure">
    1. In the [Azure portal](https://portal.azure.com), search for **Private Link** and select **Private Link Center**. Then go to **Private endpoints** and click **Create**.

    2. Select your **Subscription** and **Resource group**, enter a **Name** for the private endpoint, and select the **Region** that matches your index. Then click **Next: Resource**.

    3. For **Connection method**, select **Connect to an Azure resource by resource ID or alias**, and enter the **Resource ID or alias** for your index's region:

       | Index region | Private Link Service alias |
       | - | - |
       | `eastus2` (Virginia) | `pinecone.bdbc7759-0243-46c1-af51-794c4602745b.eastus2.azure.privatelinkservice` |

    4. Click **Next: Virtual Network**, and select the **Virtual network** and **Subnet** for the private endpoint.

    5. Click **Next: DNS**, and skip this tab. You'll set up DNS in [step 3](#3-configure-dns).

    6. Click **Next: Tags**, then **Review + create**, and then **Create**.

    7. After Azure creates the private endpoint, open it, go to **Properties**, and copy the **Resource ID** (e.g., `/subscriptions/<sub-uuid>/resourceGroups/<rg>/providers/Microsoft.Network/privateEndpoints/<name>`). You'll enter it in Pinecone in the next step.
  </Tab>
</Tabs>

### 2. Add a private endpoint in Pinecone

Add the endpoint to your Pinecone project so Pinecone accepts connections through it:

1. In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), select your project and go to **Settings > Network**.
2. On the **PRIVATE ENDPOINTS** tab, click **Add an endpoint**.
3. Select your cloud provider and your index's region, and then click **Next**.
4. Enter the ID you copied in [step 1](#1-create-a-private-endpoint-in-your-cloud-provider), and then click **Next**:
   * **AWS**: The VPC endpoint ID.
   * **Azure**: The private endpoint's resource ID.
5. Leave **Restrict access to only private endpoints** off for now. Turning it on cuts off internet access to the project before your private endpoint works. You can [turn it on later](#restrict-access-to-private-endpoints).
6. Click **Finish setup**.

### 3. Configure DNS

Clients reach an index through its [private endpoint URL](#4-connect-to-your-index), such as `docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io`. Public DNS doesn't resolve these names, so DNS on your network must resolve them to your private endpoint's IP address. Clients must connect by hostname rather than IP address, because Pinecone's TLS certificate is issued for the hostname, not the IP address.

Each region has one private DNS zone. A single wildcard record (`*`) in that zone covers every index in the region:

| Cloud | Index region | Private DNS zone |
| - | - | - |
| AWS | `us-east-1` (N. Virginia) | `private.aped-4627-b74a.pinecone.io` |
| AWS | `us-west-2` (Oregon) | `private.apw5-4e34-81fa.pinecone.io` |
| AWS | `eu-west-1` (Ireland) | `private.apu-57e2-42f6.pinecone.io` |
| AWS | `eu-central-1` (Frankfurt) | `private.apec-a2ee-38c6.pinecone.io` |
| AWS | `ap-southeast-1` (Singapore) | `private.aps-d9bb-582b.pinecone.io` |
| Azure | `eastus2` (Virginia) | `private.eastus2-5e25.prod-azure.pinecone.io` |

Clients also need a network route to the private endpoint's IP address on port 443. For clients outside the VPC or VNet, such as on-premises servers, that usually means a VPN, AWS Direct Connect, Azure ExpressRoute, or network peering.

<Tabs>
  <Tab title="AWS">
    If you selected **Enable DNS name** when you created the VPC endpoint, clients in that VPC already resolve Pinecone's private DNS names. Set up DNS yourself if you turned that option off, or if clients outside the VPC need to connect:

    * **Route 53 private hosted zone**: Create a [private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) named after your region's private DNS zone and associate it with your VPCs. Then add a wildcard record (`*`) that [routes traffic to the VPC endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html).
    * **Your own DNS server**: On your organization's DNS server, create a zone named after your region's private DNS zone. Add a wildcard CNAME record (`*`) that points to the VPC endpoint's regional DNS name, which has the form `vpce-XXXXXXX.vpce-svc-XXXXXXX.REGION.vpce.amazonaws.com`. AWS publishes that name in public DNS, and it resolves to the endpoint's private IP addresses. To get it, run `aws ec2 describe-vpc-endpoints --vpc-endpoint-ids VPC_ENDPOINT_ID --query 'VpcEndpoints[*].DnsEntries'`. The first entry is the regional DNS name.
    * **Forward to Route 53**: If you selected **Enable DNS name**, you can keep AWS as the source of these records instead. Create a [Route 53 Resolver inbound endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the VPC, and then add a conditional forwarder on your DNS server that sends queries for the private DNS zone to the inbound endpoint's IP addresses.
  </Tab>

  <Tab title="Azure">
    Azure doesn't resolve Pinecone's private DNS names automatically, so you must set up DNS. First, find your private endpoint's IP address. In the Azure portal, open your private endpoint, and on its **Overview** page, select its network interface. The network interface's **Overview** page shows the **Private IP address** (e.g., `172.30.0.6`).

    Then set up DNS in one of the following ways.

    #### Use an Azure Private DNS zone

    Use this option if your clients use Azure-provided DNS.

    1. Create an [Azure Private DNS zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal) named `private.eastus2-5e25.prod-azure.pinecone.io`.
    2. [Link the zone](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links) to the VNet where you created the private endpoint, and to any other VNets whose clients connect to Pinecone.
    3. Add a wildcard A record (`*.private.eastus2-5e25.prod-azure.pinecone.io`) that points to your private endpoint's IP address.

    #### Use your own DNS server

    Use this option if your organization runs its own DNS server.

    1. On your DNS server, create a zone named `private.eastus2-5e25.prod-azure.pinecone.io`.
    2. Add a wildcard A record (`*.private.eastus2-5e25.prod-azure.pinecone.io`) that points to your private endpoint's IP address.
    3. Make sure the clients that connect to Pinecone use this DNS server.

    #### Forward to an Azure Private DNS zone

    Use this option if your organization runs its own DNS but manages private endpoint records in Azure.

    1. Set up an [Azure Private DNS zone](#use-an-azure-private-dns-zone) as described above.
    2. Create an [Azure DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview) with an inbound endpoint in a VNet that's linked to the zone.
    3. On your DNS server, add a conditional forwarder that sends queries for `private.eastus2-5e25.prod-azure.pinecone.io` to the inbound endpoint's IP address.

    For more on these patterns, see [Azure Private Endpoint DNS integration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns-integration).

    <Note>
      A private endpoint keeps its IP address for as long as it exists. If you point an A record at that address and later delete and re-create the endpoint, update the record with the new address.
    </Note>
  </Tab>
</Tabs>

To check your setup, look up your index's private endpoint URL from a client machine. Replace the example host with your index's **Private host** value from [step 4](#4-connect-to-your-index):

```bash Terminal theme={null}
nslookup docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io
```

The response should return your private endpoint's IP address. If the lookup fails or returns a different address, the client isn't using the DNS server or zone you configured.

### 4. Connect to your index

To send data operations through your private endpoint, target the index by its private endpoint URL instead of its standard host. The only difference is that `.svc.` becomes `.svc.private.`.

You can get the private endpoint URL for an index from the Pinecone console or API.

<Tabs>
  <Tab title="Console">
    To get the private endpoint URL for an index from the Pinecone console:

    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index.
    3. Select the index.
    4. Copy the **Private host** value.
  </Tab>

  <Tab title="API">
    To get the private endpoint URL for an index from the API, use the [Describe an index](/reference/api/latest/control-plane/describe_index) operation, which returns the private endpoint URL as the `private_host` value:

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
          -H "Api-Key: $PINECONE_API_KEY" \
          -H "X-Pinecone-Api-Version: 2026-07"
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

      ```json curl {4} theme={null}
      {
        "name": "docs-example",
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "deployment": {
          "deployment_type": "managed",
          "region": "us-east-1",
          "cloud": "aws",
          "environment": "aped-4627-b74a"
        },
        "read_capacity": {
          "mode": "OnDemand",
          "status": {
            "state": "Ready",
            "current_shards": null,
            "current_replicas": null
          }
        },
        "schema": {
          "fields": {
            "embedding": {
              "type": "dense_vector",
              "description": null,
              "dimension": 1536,
              "metric": "cosine"
            }
          }
        },
        "tags": {
          "environment": "production"
        },
        "deletion_protection": "disabled"
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  If you [restrict access to private endpoints](/guides/production/configure-private-endpoints#restrict-access-to-private-endpoints), requests that don't come through a private endpoint get an `Unauthorized` response. Requests through a private endpoint that isn't registered to the index's project also get `Unauthorized`.
</Note>

## Restrict access to private endpoints

After your private endpoint works, you can turn off internet access to the project. Then only requests that come through a private endpoint can read or write the project's indexes.

<Warning>
  This setting applies to the whole project. Any application that reaches an index in the project over the internet stops working.
</Warning>

1. In the [Pinecone console](https://app.pinecone.io/organizations/-/projects), select your project and go to **Settings > Network**.
2. On the **ACCESS** tab, turn on **Restrict access to only private endpoints**.
3. Click **Confirm and proceed**.

To turn internet access back on, turn the toggle off.

## Manage private endpoints

To view a project's private endpoints, open the [Pinecone console](https://app.pinecone.io/organizations/-/projects), select the project, and go to **Settings > Network**. The **PRIVATE ENDPOINTS** tab lists each endpoint's ID, cloud, and region.

To delete a private endpoint:

1. On the **PRIVATE ENDPOINTS** tab, open the **Actions** menu for the endpoint and click **Delete**.
2. Enter the endpoint ID to confirm, and then click **Delete Endpoint**.

Deleting a private endpoint in Pinecone doesn't delete the endpoint in your AWS or Azure account. Delete it there separately if you no longer need it.
