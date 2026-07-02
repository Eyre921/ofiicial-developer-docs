---
title: "Security and Compliance"
source: https://developers.deepgram.com/docs/security-and-compliance-sagemaker.md
path: docs/security-and-compliance-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Security and Compliance

> How Deepgram on Amazon SageMaker is protected by AWS infrastructure security, including TLS requirements for API access, network isolation for AWS Marketplace containers, container vulnerability scanning with no Critical or High CVEs, and VPC endpoint options for restricting access to your endpoint.

As a managed service, Amazon SageMaker AI is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well-Architected Framework*.

For more information, review the AWS documentation [Infrastructure security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-security.html).

## API access requirements

You use AWS published API calls to access Amazon SageMaker AI through the network. Clients must support the following:

* Transport Layer Security (TLS). AWS requires TLS 1.2 and recommends TLS 1.3.
* Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

## Network isolation for AWS Marketplace containers

Network isolation is required to run models using resources from AWS Marketplace. For additional security, AWS Marketplace images run within an Amazon VPC. They only have access to data within their local file systems. For details, see [No internet access for Marketplace algorithm and model package containers](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html#:~:text=Network%20isolation%20is%20required%20to%20run%20training%20jobs%20and%20models%20using%20resources%20from%20AWS%20Marketplace.%20For%20additional%20security%2C%20AWS%20Marketplace%20images%20run%20within%20an%20Amazon%20VPC.%20They%20only%20have%20access%20to%20data%20within%20their%20local%20file%20systems.).

Because network isolation is enabled, Deepgram Marketplace containers cannot make any outbound network calls to any service, including Amazon S3 or Deepgram infrastructure. No AWS credentials are made available to the container runtime environment.

## Container vulnerability scanning

AWS Marketplace scans all SageMaker container images for Common Vulnerabilities and Exposures (CVE) before publishing. Deepgram containers listed on AWS Marketplace are published without any CVEs of Critical or High severity — this is a requirement enforced by AWS Marketplace before any product can be listed. If a scan detects vulnerabilities at these severity levels, the container image cannot be published until they are resolved.

For more information, see [SageMaker AI Scans AWS Marketplace Training and Inference Containers for Security Vulnerabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-security.html#mkt-container-scan) and [Scan your uploaded image](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-uploading-your-images.html#ml-scan-your-uploaded-image).

## Endpoint access: public internet or VPC

A SageMaker Endpoint can be accessible over the public internet or restricted to access only from within your Amazon VPC. To restrict access to your endpoint to a VPC, create an [interface VPC endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html) for SageMaker Runtime. Traffic between your VPC and SageMaker then travels over the AWS network and never traverses the public internet.

Use a VPC endpoint when you want to:

* Keep all inference traffic on the AWS network.
* Apply VPC security groups and route tables to control which clients reach the endpoint.
* Meet compliance requirements that prohibit public internet exposure of inference traffic.

## Compliance

Deepgram models running on Amazon SageMaker AI real-time endpoints are eligible for most common compliance frameworks, including but not limited to SOC 1/2/3, HIPAA, PCI DSS, FedRAMP Moderate (US East/West), GDPR, and ISO 27001/27017/27018. For specific compliance details for Amazon SageMaker AI, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

## Related resources

* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)
* [Observability for Amazon SageMaker](/docs/observability-sagemaker)
