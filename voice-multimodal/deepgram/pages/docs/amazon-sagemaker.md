---
title: "Amazon SageMaker"
source: https://developers.deepgram.com/docs/amazon-sagemaker.md
path: docs/amazon-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Amazon SageMaker

> Overview of running Deepgram on Amazon SageMaker AI. Compare benefits and tradeoffs versus self-hosted Docker or Kubernetes, review deployment options, and understand SageMaker pricing for Deepgram models.

Amazon SageMaker is a managed cloud platform from Amazon Web Services (AWS) that enables deployment of Deepgram as a managed, container-based service. Once you deploy Deepgram as a SageMaker Model Endpoint, you can run inference against the service using the Amazon SageMaker AI Software Development Kit (SDK).

The [Deepgram SDKs](/home) can also target a SageMaker Endpoint through the SageMaker transport, so you can keep the same client-side request and response patterns whether you call the Deepgram-hosted API or your own SageMaker deployment.

## Benefits and Tradeoffs

Deepgram on SageMaker is the fastest path to running Deepgram inside your own AWS account. Compared to self-hosting Deepgram on Docker or Kubernetes, SageMaker trades some flexibility for a managed endpoint that AWS operates on your behalf.

### When SageMaker is the right fit

* **Ease of deployment.** A ready-to-use endpoint can be created in minutes from the AWS Console or with infrastructure-as-code. There are no container images to mirror, no GPU drivers to install, and no Helm charts to maintain.
* **Lower management overhead.** AWS manages the underlying instances, host OS, container runtime, and model package distribution. You do not need a dedicated platform team to keep the service patched and healthy.
* **Compliance for regulated workloads.** Deepgram runs entirely inside your AWS account and VPC. Audio never leaves your environment, and you inherit the compliance posture of SageMaker AI (HIPAA-eligible, SOC, ISO, PCI, FedRAMP, and others). This makes SageMaker a strong fit for regulated industries that need a private deployment without operating their own Kubernetes platform.
* **Native integration with AWS services.** SageMaker Endpoints integrate out of the box with Amazon CloudWatch (logs and metrics), AWS IAM (authentication and authorization), Amazon VPC (network isolation), AWS PrivateLink, AWS KMS, AWS CloudTrail (audit), and SageMaker auto-scaling. You get production-grade observability and access controls without building them yourself.
* **AWS Marketplace billing.** Deepgram license charges flow through your existing AWS bill, simplifying procurement for teams that already buy through AWS.

While SageMaker covers most production scenarios, AWS imposes a small number of platform-specific constraints — for example, callback URLs and external file URL ingestion are not supported. Review the full list in the [Limitations section of the deployment guide](/docs/deploy-amazon-sagemaker#limitations) before choosing SageMaker.

### When Docker or Kubernetes may be a better fit

* You need to run Deepgram outside AWS or on bare metal.
* You require features that the SageMaker isolation model does not currently support, such as user-defined [callback URLs](/docs/callback), JSON payloads that reference audio in cloud storage, or Deepgram [custom metrics](/docs/metrics-guide).
* You want to run the [Deepgram Voice Agent](/docs/voice-agent). SageMaker Endpoints cannot invoke Large Language Model (LLM) services, which the Voice Agent requires, so the Voice Agent cannot run inside SageMaker.
* You need streaming connections that stay open for longer than 30 minutes. SageMaker Real-Time Inference supports [up to 30 minutes of connection time](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html#realtime-endpoints-test-endpoints-sdk:~:text=The%20connection%20remains%20open%20until%20you%20explicitly%20close%20the%20input%20stream%20or%20the%20endpoint%20closes%20the%20connection%2C%20supporting%20up%20to%2030%20minutes%20of%20connection%20time) per bidirectional streaming connection.
* You need to send more than 25 MB of input data per non-streaming invocation on a real-time endpoint, or more than 1 GB on an asynchronous endpoint. SageMaker enforces a [25 MB maximum payload size](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-service-restrictions-and-limits.html#:~:text=For%20an%20endpoint%2C%20limit%20the%20maximum%20size%20of%20the%20input%20data%20per%20invocation%20to%2025%20MB.%20This%20value%20can%27t%20be%20adjusted) for real-time endpoints. For larger files, [asynchronous endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) support payloads up to 1 GB with near real-time latency and can scale to zero when there are no requests to be processed.
* You need fine-grained control over the container runtime, networking, or process supervision beyond what SageMaker exposes.

## Deployment options

Most customers can stand up a ready-to-use endpoint in minutes through one of two paths:

* **AWS Console.** Subscribe to a Deepgram product on the AWS Marketplace and click through the SageMaker Console to create the endpoint. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) for the step-by-step walkthrough.
* **Infrastructure-as-Code.** Deploy the same model package using Terraform for repeatable, version-controlled rollouts. See [Deploy with Terraform](/docs/terraform-deploy-sagemaker).

## Pricing

Deepgram on SageMaker is billed hourly per instance type. Current rates are listed on the [AWS Marketplace product pages for each Deepgram model](https://aws.amazon.com/marketplace/search/results?searchTerms=deepgram\&CREATOR=6efa21f9-9a33-4cae-ba44-756436fa71dd\&FULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL\&filters=CREATOR%2CFULFILLMENT_OPTION_TYPE).

### Private offers

For larger or longer-term deployments, AWS Marketplace Private Offers are available with negotiated unit economics and committed-use terms. Contact your [AWS account team](https://aws.amazon.com/contact-us/sales-support/) or [Deepgram representative](https://deepgram.com/contact-us) to start a Private Offer.

### Try before you buy

A 14-day free trial is available with unlimited product usage and zero Deepgram license charges during the trial window. Each trial is available once per AWS account per product. Contact a [Deepgram representative](https://deepgram.com/contact-us) if you need additional time for testing.

### Infrastructure charges

Infrastructure charges are set by AWS and billed separately from Deepgram license charges. Public pricing for SageMaker Real-Time Inference is available at [aws.amazon.com/sagemaker/ai/pricing](https://aws.amazon.com/sagemaker/ai/pricing/). For volume discounts or committed-use pricing on the underlying compute, [contact your AWS Sales Representative](https://aws.amazon.com/contact-us/sales-support/).
