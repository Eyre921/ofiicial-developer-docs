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

Amazon SageMaker is a managed cloud platform from Amazon Web Services (AWS) that enables deployment of Deepgram as a managed, container-based service. The endpoint is air-gapped and runs on compute inside your own AWS VPC. Once you deploy Deepgram as a SageMaker Model Endpoint, you can run inference against the service using the Amazon SageMaker AI Software Development Kit (SDK).

The [Deepgram SDKs](/home) can also target a SageMaker Endpoint through the SageMaker transport, so you can keep the same client-side request and response patterns whether you call the Deepgram-hosted API or your own SageMaker deployment.

## Benefits and Tradeoffs

Deepgram on SageMaker is the fastest path to running Deepgram inside your own AWS account. Compared to self-hosting Deepgram on Docker or Kubernetes, SageMaker trades some flexibility for a managed endpoint that AWS operates on your behalf.

### When SageMaker is the right fit

* **Ease of deployment.** A ready-to-use endpoint can be created in minutes from the AWS Console or with infrastructure-as-code. There are no container images to mirror, no GPU drivers to install, and no Helm charts to maintain.
* **Lower management overhead.** AWS manages the underlying instances, host OS, container runtime, and model package distribution. You do not need a dedicated platform team to keep the service patched and healthy.
* **Compliance for regulated workloads.** Deepgram runs entirely inside your AWS account and VPC. Audio never leaves your environment, and you inherit the compliance posture of SageMaker AI (HIPAA-eligible, SOC, ISO, PCI, FedRAMP, and others). This makes SageMaker a strong fit for regulated industries that need a private deployment without operating their own Kubernetes platform.
* **Native integration with AWS services.** SageMaker Endpoints integrate out of the box with Amazon CloudWatch (logs and metrics), AWS IAM (authentication and authorization), Amazon VPC (network isolation), AWS PrivateLink, AWS KMS, AWS CloudTrail (audit), and SageMaker auto-scaling. You get production-grade observability and access controls without building them yourself.
* **AWS Marketplace billing.** Deepgram license charges flow through your existing AWS bill, simplifying procurement for teams that already buy through AWS.

### When Docker or Kubernetes may be a better fit

* You need to run Deepgram outside AWS or on bare metal.
* You require features that the SageMaker isolation model does not currently support, such as user-defined [callback URLs](/docs/callback) or JSON payloads that reference audio in cloud storage.
* You want to run the [Deepgram Voice Agent](/docs/voice-agent). SageMaker Endpoints cannot invoke Large Language Model (LLM) services, which the Voice Agent requires, so the Voice Agent cannot run inside SageMaker.
* You need streaming connections that stay open for longer than 30 minutes. SageMaker Real-Time Inference supports [up to 30 minutes of connection time](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html#realtime-endpoints-test-endpoints-sdk:~:text=The%20connection%20remains%20open%20until%20you%20explicitly%20close%20the%20input%20stream%20or%20the%20endpoint%20closes%20the%20connection%2C%20supporting%20up%20to%2030%20minutes%20of%20connection%20time) per bidirectional streaming connection.
* You need to send more than 25 MB of input data per non-streaming invocation on a real-time endpoint, or more than 1 GB on an asynchronous endpoint. SageMaker enforces a [25 MB maximum payload size](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-service-restrictions-and-limits.html#:~:text=For%20an%20endpoint%2C%20limit%20the%20maximum%20size%20of%20the%20input%20data%20per%20invocation%20to%2025%20MB.%20This%20value%20can%27t%20be%20adjusted) for real-time endpoints. For larger files, [asynchronous endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) support payloads up to 1 GB with near real-time latency and can scale to zero when there are no requests to be processed.
* You need fine-grained control over the container runtime, networking, or process supervision beyond what SageMaker exposes.

## Limitations

When using Deepgram services in Amazon SageMaker, please be aware of the following limitations.

* The SageMaker network isolation model prevents the container from making outbound calls to external LLM providers. As a result, the [Deepgram Voice Agent](/docs/voice-agent) cannot run inside SageMaker.
* Deepgram cannot invoke user-defined [callback URLs](/docs/callback)
* Passing a JSON payload for transcription (e.g., referencing a file stored in cloud storage via URL) is unsupported, as the SageMaker isolation model prevents the container from reaching out to external cloud storage
* Deepgram [custom metrics](/docs/metrics-guide) are not currently available through Amazon SageMaker Endpoints
* For streaming invocations, the connection remains open until you explicitly close the input stream or the endpoint closes the connection, supporting [up to 30 minutes of connection time](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html#realtime-endpoints-test-endpoints-sdk:~:text=The%20connection%20remains%20open%20until%20you%20explicitly%20close%20the%20input%20stream%20or%20the%20endpoint%20closes%20the%20connection%2C%20supporting%20up%20to%2030%20minutes%20of%20connection%20time).
* For non-streaming invocations, the [maximum size of the input data is 25 MB](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-service-restrictions-and-limits.html#:~:text=For%20an%20endpoint%2C%20limit%20the%20maximum%20size%20of%20the%20input%20data%20per%20invocation%20to%2025%20MB.%20This%20value%20can%27t%20be%20adjusted) for real-time endpoints. For larger files, use [asynchronous endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html), which support payloads up to 1 GB with near real-time latency and can scale to zero when there are no requests to be processed.

## Deployment options

Most customers can stand up a ready-to-use endpoint in minutes:

1. **Subscribe.** Subscribe to a Deepgram product on the AWS Marketplace and note its Model Package ARN. See [Subscribe on AWS Marketplace](/docs/subscribe-aws-marketplace).
2. **Deploy** with one of two paths:
   * **AWS CLI or SDK.** Create the SageMaker Model, Endpoint Configuration, and Endpoint with the AWS CLI or Boto3. This is the recommended path because it lets you pin the inference AMI version that current Deepgram model packages require. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker).
   * **Infrastructure-as-Code.** Deploy the same model package using Terraform for repeatable, version-controlled rollouts. See [Deploy with Terraform](/docs/terraform-deploy-sagemaker).

The SageMaker AI console cannot set the inference AMI version, so endpoints created through the console fail to start with current Deepgram model packages. Use the CLI, SDK, or Terraform paths above.

## Pricing

Deepgram on SageMaker is billed per request, at the same rates shown on [deepgram.com/pricing](https://deepgram.com/pricing). The AWS pricing page may list the dimension `inference.count.m.i.c Inference Pricing` at a cost of `$0.001/request`. When the cost of a request exceeds \$0.001, Deepgram automatically emits a charge for multiple units for that single request.

### Private offers

For larger or longer-term deployments, AWS Marketplace Private Offers are available with negotiated unit economics and committed-use terms. Contact your [AWS account team](https://aws.amazon.com/contact-us/sales-support/) or [Deepgram representative](https://deepgram.com/contact-us) to start a Private Offer.

### Try before you buy

A 14-day free trial is available with unlimited product usage and zero Deepgram license charges during the trial window. Each trial is available once per AWS account per product. Contact a [Deepgram representative](https://deepgram.com/contact-us) if you need additional time for testing.

### Infrastructure charges

Infrastructure charges are set by AWS and billed separately from Deepgram license charges. Public pricing for SageMaker Real-Time Inference is available at [aws.amazon.com/sagemaker/ai/pricing](https://aws.amazon.com/sagemaker/ai/pricing/). Self-service savings may be available on 1-year or 3-year committed usage by purchasing a [Machine Learning Savings Plan from AWS](https://aws.amazon.com/savingsplans/ml-pricing/). For more information or to discuss additional discounts, [contact your AWS sales representative](https://aws.amazon.com/contact-us/sales-support/).
