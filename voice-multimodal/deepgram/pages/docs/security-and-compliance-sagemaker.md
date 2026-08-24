---
title: "Security and Compliance"
source: https://developers.deepgram.com/docs/security-and-compliance-sagemaker.md
path: docs/security-and-compliance-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Security and Compliance

> Security and compliance for Deepgram on Amazon SageMaker: TLS requirements for API access, FIPS 140-3 endpoints for the control plane and inference traffic, FedRAMP coverage, network isolation for AWS Marketplace containers, container vulnerability scanning with no Critical or High CVEs, and VPC endpoint options for restricting access to your endpoint.

As a managed service, Amazon SageMaker AI is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well-Architected Framework*.

For more information, review the AWS documentation [Infrastructure security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-security.html).

## API access requirements

You use AWS published API calls to access Amazon SageMaker AI through the network. Clients must support the following:

* Transport Layer Security (TLS). AWS requires TLS 1.2 and recommends TLS 1.3.
* Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

## FIPS 140-3 endpoints

Amazon SageMaker AI offers FIPS 140-3 endpoints in several regions. Unlike standard AWS endpoints, FIPS endpoints use a TLS software library that complies with FIPS 140. Compliance programs that require FIPS-validated cryptography for data in transit, such as FedRAMP, must use them.

A Deepgram deployment uses two of these endpoints:

| Purpose                                                                  | Standard endpoint                          | FIPS endpoint                                   |
| ------------------------------------------------------------------------ | ------------------------------------------ | ----------------------------------------------- |
| Control plane — create, update, and describe endpoints                   | `api.sagemaker.<region>.amazonaws.com`     | `api-fips.sagemaker.<region>.amazonaws.com`     |
| Inference — `InvokeEndpoint` and `InvokeEndpointWithBidirectionalStream` | `runtime.sagemaker.<region>.amazonaws.com` | `runtime-fips.sagemaker.<region>.amazonaws.com` |

Every Deepgram model and transport, including streaming, works over these endpoints. Switching to them changes only the hostname.

SageMaker FIPS endpoints are available in US East (N. Virginia and Ohio), US West (N. California and Oregon), Canada, and AWS GovCloud (US). For the authoritative list, see [FIPS endpoints by service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service). If a region has no FIPS endpoint, deploy in one that does. Deepgram is not available on AWS Marketplace in GovCloud — see [FedRAMP](#fedramp) below.

To configure your clients, see [Use FIPS Endpoints](/docs/fips-endpoints-sagemaker).

### What a FIPS endpoint covers

A FIPS endpoint covers the TLS session between your client and AWS. The Deepgram container itself performs no cryptographic operations:

* SageMaker terminates the client TLS session and forwards the request to the container over the instance's loopback interface.
* Network isolation is enabled, so the container opens no outbound connections.

## Network isolation for AWS Marketplace containers

Network isolation is required to run models using resources from AWS Marketplace. For additional security, AWS Marketplace images run within an Amazon VPC. They only have access to data within their local file systems. For details, see [No internet access for Marketplace algorithm and model package containers](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html#:~:text=Network%20isolation%20is%20required%20to%20run%20training%20jobs%20and%20models%20using%20resources%20from%20AWS%20Marketplace.%20For%20additional%20security%2C%20AWS%20Marketplace%20images%20run%20within%20an%20Amazon%20VPC.%20They%20only%20have%20access%20to%20data%20within%20their%20local%20file%20systems.).

With network isolation enabled, Deepgram Marketplace containers cannot make outbound network calls to any service, including Amazon S3 and Deepgram infrastructure. The container runtime environment receives no AWS credentials.

## Container vulnerability scanning

AWS Marketplace scans every SageMaker container image for Common Vulnerabilities and Exposures (CVE) before publishing, and rejects any image with a Critical or High severity finding until it is resolved. Deepgram containers listed on AWS Marketplace therefore carry no Critical or High CVEs.

For more information, see [SageMaker AI Scans AWS Marketplace Training and Inference Containers for Security Vulnerabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-security.html#mkt-container-scan) and [Scan your uploaded image](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-uploading-your-images.html#ml-scan-your-uploaded-image).

## Endpoint access: public internet or VPC

A SageMaker Endpoint can be accessible over the public internet or restricted to access only from within your Amazon VPC. To restrict access to your endpoint to a VPC, create an [interface VPC endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html) for SageMaker Runtime. Traffic between your VPC and SageMaker then travels over the AWS network and never traverses the public internet.

Use a VPC endpoint when you want to:

* Keep all inference traffic on the AWS network.
* Apply VPC security groups and route tables to control which clients reach the endpoint.
* Meet compliance requirements that prohibit public internet exposure of inference traffic.

VPC endpoints and FIPS endpoints address different layers: a VPC endpoint controls the network path your traffic takes, and a FIPS endpoint controls the cryptography that protects it. Use both when your compliance program requires both.

## Compliance

Deepgram models running on Amazon SageMaker AI real-time endpoints are eligible for most common compliance frameworks, including SOC 1/2/3, HIPAA, PCI DSS, FedRAMP, GDPR, and ISO 27001/27017/27018.

### FedRAMP

Two separate FedRAMP Certifications cover AWS environments:

| AWS environment   | Regions                                              | FedRAMP Certification                |
| ----------------- | ---------------------------------------------------- | ------------------------------------ |
| AWS US East-West  | Northern Virginia, Ohio, Oregon, Northern California | Class C (formerly Moderate baseline) |
| AWS GovCloud (US) | US-East, US-West                                     | Class D (formerly High baseline)     |

Deepgram is not listed on AWS Marketplace in AWS GovCloud (US), so a Marketplace subscription cannot reach the Class D (formerly High baseline) environment. For a GovCloud deployment, contact your [Deepgram representative](https://deepgram.com/contact-us).

For the services in scope of each certification boundary, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). For AWS's own answers on regional coverage, package availability, and how to request authorization artifacts, see the [AWS FedRAMP FAQ](https://aws.amazon.com/compliance/fedramp/).

FedRAMP requires FIPS-validated cryptography for data in transit, so pair a FedRAMP-covered region with the [FIPS 140-3 endpoints](#fips-140-3-endpoints) above.

## Related resources

* [Use FIPS Endpoints](/docs/fips-endpoints-sagemaker)
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)
* [Observability for Amazon SageMaker](/docs/observability-sagemaker)
