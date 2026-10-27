---
title: "Private Endpoints"
source: https://docs.turso.tech/cloud/private-endpoints
path: cloud/private-endpoints
---

Learn how to configure private endpoints for your Turso Database on AWS.

Set up an AWS VPC endpoint to securely access Turso databases through AWS PrivateLink, keeping all traffic within AWS's private network.

## Prerequisites

* Existing VPC in your target AWS region
* Subnets in supported availability zones (see region-specific requirements below)
* IAM permissions to create VPC endpoints and modify security groups
* Active Turso account with configured databases

## Quickstart

**us-east-1**

**1. Create VPC Endpoint**

Navigate to **VPC Dashboard** → **Endpoints** → **Create endpoint** and configure:

> **Basic Settings**
>
> * **Name**: Enter a descriptive name (e.g., `turso-database-endpoint`)
> * **Service category**: Select "Other endpoint services"
> * **Service name**: Enter `com.amazonaws.vpce.us-east-1.vpce-svc-0d9cc6f6a688ce8a5`
> * Click **Verify service**

> **Network Configuration**
>
> * Select your **VPC**
> * Enable **DNS name**
> * Choose **IPv4** for DNS record type
> * Select subnets in supported AZs (`use1-az4` and/or `use1-az6`)
> * Configure security groups and click **Create endpoint**

**2. Configure Security Groups**

Update security groups to allow proper communication:

**VPC Endpoint Security Group:**

* Inbound: Allow HTTPS (port 443) from your application security groups

**Application Security Groups:**

* Outbound: Allow HTTPS (port 443) to the VPC endpoint security group

**3. Update Application Connections**

Make sure you are using the regional Turso URL format:

```bash theme={null}
curl https://<database_name>-<organization_slug>.aws-us-east-1.turso.io
```

**4. Verify Setup**

Test your VPC endpoint configuration from within your VPC:

```bash theme={null}
# Test connectivity
curl -v https://<database_name>-<organization_slug>.aws-us-east-1.turso.io

# Verify private routing (should show traffic staying within AWS network)
traceroute -T <database_name>-<organization_slug>.aws-us-east-1.turso.io
```

**us-east-2**

**1. Create VPC Endpoint**

Navigate to **VPC Dashboard** → **Endpoints** → **Create endpoint** and configure:

> **Basic Settings**
>
> * **Name**: Enter a descriptive name (e.g., `turso-database-endpoint`)
> * **Service category**: Select "Other endpoint services"
> * **Service name**: Enter `com.amazonaws.vpce.us-east-2.vpce-svc-08cc04ea0962d5036`
> * Click **Verify service**

> **Network Configuration**
>
> * Select your **VPC**
> * Enable **DNS name**
> * Choose **IPv4** for DNS record type
> * Select subnets in supported AZs (`use2-az1` and/or `use2-az2`)
> * Configure security groups and click **Create endpoint**

**2. Configure Security Groups**

Update security groups to allow proper communication:

**VPC Endpoint Security Group:**

* Inbound: Allow HTTPS (port 443) from your application security groups

**Application Security Groups:**

* Outbound: Allow HTTPS (port 443) to the VPC endpoint security group

**3. Update Application Connections**

Make sure you are using the regional Turso URL format:

```bash theme={null}
curl https://<database_name>-<organization_slug>.aws-us-east-2.turso.io
```

**4. Verify Setup**

Test your VPC endpoint configuration from within your VPC:

```bash theme={null}
# Test connectivity
curl -v https://<database_name>-<organization_slug>.aws-us-east-2.turso.io

# Verify private routing (should show traffic staying within AWS network)
traceroute -T <database_name>-<organization_slug>.aws-us-east-2.turso.io
```

**us-west-2**

**1. Create VPC Endpoint**

Navigate to **VPC Dashboard** → **Endpoints** → **Create endpoint** and configure:

> **Basic Settings**
>
> * **Name**: Enter a descriptive name (e.g., `turso-database-endpoint`)
> * **Service category**: Select "Other endpoint services"
> * **Service name**: Enter `com.amazonaws.vpce.us-west-2.vpce-svc-0372e98cdacb325b7`
> * Click **Verify service**

> **Network Configuration**
>
> * Select your **VPC**
> * Enable **DNS name**
> * Choose **IPv4** for DNS record type
> * Select subnets in supported AZs (`usw2-az1` and/or `usw2-az3`)
> * Configure security groups and click **Create endpoint**

**2. Configure Security Groups**

Update security groups to allow proper communication:

**VPC Endpoint Security Group:**

* Inbound: Allow HTTPS (port 443) from your application security groups

**Application Security Groups:**

* Outbound: Allow HTTPS (port 443) to the VPC endpoint security group

**3. Update Application Connections**

Make sure you are using the regional Turso URL format:

```bash theme={null}
curl https://<database_name>-<organization_slug>.aws-us-west-2.turso.io
```

**4. Verify Setup**

Test your VPC endpoint configuration from within your VPC:

```bash theme={null}
# Test connectivity
curl -v https://<database_name>-<organization_slug>.aws-us-west-2.turso.io

# Verify private routing (should show traffic staying within AWS network)
traceroute -T <database_name>-<organization_slug>.aws-us-west-2.turso.io
```

**eu-west-1**

**1. Create VPC Endpoint**

Navigate to **VPC Dashboard** → **Endpoints** → **Create endpoint** and configure:

> **Basic Settings**
>
> * **Name**: Enter a descriptive name (e.g., `turso-database-endpoint`)
> * **Service category**: Select "Other endpoint services"
> * **Service name**: Enter `com.amazonaws.vpce.eu-west-1.vpce-svc-09559a4fb467b07fd`
> * Click **Verify service**

> **Network Configuration**
>
> * Select your **VPC**
> * Enable **DNS name**
> * Choose **IPv4** for DNS record type
> * Select subnets in supported AZs (`euw1-az1` and/or `euw1-az3`)
> * Configure security groups and click **Create endpoint**

**2. Configure Security Groups**

Update security groups to allow proper communication:

**VPC Endpoint Security Group:**

* Inbound: Allow HTTPS (port 443) from your application security groups

**Application Security Groups:**

* Outbound: Allow HTTPS (port 443) to the VPC endpoint security group

**3. Update Application Connections**

Make sure you are using the regional Turso URL format:

```bash theme={null}
curl https://<database_name>-<organization_slug>.aws-eu-west-1.turso.io
```

**4. Verify Setup**

Test your VPC endpoint configuration from within your VPC:

```bash theme={null}
# Test connectivity
curl -v https://<database_name>-<organization_slug>.aws-eu-west-1.turso.io

# Verify private routing (should show traffic staying within AWS network)
traceroute -T <database_name>-<organization_slug>.aws-eu-west-1.turso.io
```

**ap-south-1**

**1. Create VPC Endpoint**

Navigate to **VPC Dashboard** → **Endpoints** → **Create endpoint** and configure:

> **Basic Settings**
>
> * **Name**: Enter a descriptive name (e.g., `turso-database-endpoint`)
> * **Service category**: Select "Other endpoint services"
> * **Service name**: Enter `com.amazonaws.vpce.ap-south-1.vpce-svc-0c1607d1026a49817`
> * Click **Verify service**

> **Network Configuration**
>
> * Select your **VPC**
> * Enable **DNS name**
> * Choose **IPv4** for DNS record type
> * Select subnets in supported AZs (`aps1-az1` and/or `aps1-az3`)
> * Configure security groups and click **Create endpoint**

**2. Configure Security Groups**

Update security groups to allow proper communication:

**VPC Endpoint Security Group:**

* Inbound: Allow HTTPS (port 443) from your application security groups

**Application Security Groups:**

* Outbound: Allow HTTPS (port 443) to the VPC endpoint security group

**3. Update Application Connections**

Make sure you are using the regional Turso URL format:

```bash theme={null}
curl https://<database_name>-<organization_slug>.aws-ap-south-1.turso.io
```

**4. Verify Setup**

Test your VPC endpoint configuration from within your VPC:

```bash theme={null}
# Test connectivity
curl -v https://<database_name>-<organization_slug>.aws-ap-south-1.turso.io

# Verify private routing (should show traffic staying within AWS network)
traceroute -T <database_name>-<organization_slug>.aws-ap-south-1.turso.io
```

**ap-northeast-1**

**1. Create VPC Endpoint**

Navigate to **VPC Dashboard** → **Endpoints** → **Create endpoint** and configure:

> **Basic Settings**
>
> * **Name**: Enter a descriptive name (e.g., `turso-database-endpoint`)
> * **Service category**: Select "Other endpoint services"
> * **Service name**: Enter `com.amazonaws.vpce.ap-northeast-1.vpce-svc-070f604683ada07db`
> * Click **Verify service**

> **Network Configuration**
>
> * Select your **VPC**
> * Enable **DNS name**
> * Choose **IPv4** for DNS record type
> * Select subnets in supported AZs (`apne1-az4` and/or `apne1-az1`)
> * Configure security groups and click **Create endpoint**

**2. Configure Security Groups**

Update security groups to allow proper communication:

**VPC Endpoint Security Group:**

* Inbound: Allow HTTPS (port 443) from your application security groups

**Application Security Groups:**

* Outbound: Allow HTTPS (port 443) to the VPC endpoint security group

**3. Update Application Connections**

Make sure you are using the regional Turso URL format:

```bash theme={null}
curl https://<database_name>-<organization_slug>.aws-ap-northeast-1.turso.io
```

**4. Verify Setup**

Test your VPC endpoint configuration from within your VPC:

```bash theme={null}
# Test connectivity
curl -v https://<database_name>-<organization_slug>.aws-ap-northeast-1.turso.io

# Verify private routing (should show traffic staying within AWS network)
traceroute -T <database_name>-<organization_slug>.aws-ap-northeast-1.turso.io
```

## Important Notes

* Traffic remains within AWS's private network
* Standard AWS VPC endpoint pricing applies
* Applications can access the endpoint from any AZ in your VPC
* Each region has specific service names and supported availability zones
