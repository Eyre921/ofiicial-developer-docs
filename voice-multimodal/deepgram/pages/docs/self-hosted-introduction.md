---
title: "Introduction"
source: https://developers.deepgram.com/docs/self-hosted-introduction.md
path: docs/self-hosted-introduction
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Introduction

This introduction opens a series of guides that aim to:

* Outline the benefits and use cases of self-hosting
* Describe the architecture, requirements, and needed assets for an installation
* Tell you how to configure your environment and set up your server for the installation
* Show you how to install the actual Deepgram application
* Provide a starting point for how to connect your own applications with your self-hosted Deepgram instance
* Help you plan your server maintenance and security practices

## Why Self-Host

Using Deepgram as a service has a variety of benefits. First, it's extremely fast to start developing with. Signing up, getting an API key, and getting your first voice AI response can take as little as a minute. Using Deepgram as a service also enables you to avoid all hardware, installation, configuration, backup, and maintenance-related costs.

With that being said, there are situations a self-hosted deployment might make sense. The most common use cases we have seen are when you have stringent performance or security requirements.

### Performance

Certain use cases, like AI voicebots, have very sensitive latency and load requirements. If you need ultra-low latency with voice AI services colocated with your other services, self-hosting can meet these requirements.

### Security

One of the common use-cases for self-hosting Deepgram is to satisfy security or data privacy requirements. In a typical self-hosted deployment, no audio, transcripts, or other identifying markers of the request content are sent to Deepgram. Your Deepgram components will only contact the Deepgram license server in order to validate the Deepgram components and models, as well as report usage information. The usage information reported for each request includes metadata such as audio duration or character count, features requested, and success response codes.

Furthermore, self-hosted deployments do not offer a method to persist request or response data on your own servers. Request and response data are not stored beyond the duration of the original API request.

## Components

Before you deploy Deepgram, you’ll need to make effective design decisions about the components of your system, their relationships, and the interactions between components. Ideally, your architecture will meet your business needs, optimize both performance and security, and provide a strong technical foundation for future growth.

Deepgram provides a variety of components available for a self-hosted deployment. Many guides describe how to create a deployment using Deepgram’s required components, API and Engine. Some guides include details on additional components, such as the [License Proxy](/docs/license-proxy) in the diagram below. See [Self-Hosted Add Ons](/docs/self-hosted-add-ons) for more details.

If you aren't certain which components your contract includes, please consult your Deepgram Account Representative.

The components and architecture below describe Docker/Podman and Kubernetes deployments. [Amazon SageMaker](/docs/amazon-sagemaker) packages the API, Engine, and licensing into a single managed endpoint that scales horizontally as one unit — you don't provision or scale API, Engine, and the License Proxy separately. A SageMaker deployment also runs fully airgapped: the container is network-isolated and makes no connection to the Deepgram Cloud.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/9c8beab8a02fc149c898dcadcbabd1701dbd872d4c105d919164ffa401311f95/images/f551a1e5784007e643d90a54ce3f77ab55da484804240deeb1cf741ff6cdcddc-deepgram_architecture.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T113251Z&X-Amz-Expires=604800&X-Amz-Signature=9402c1ccff33c530bf96a824f16d7fcc2b48ee07dd6c7e1fb11b064939eedf1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Deepgram API

The Deepgram API interfaces with the Deepgram Engine to expose endpoints for your requests.

### Deepgram Engine

The Deepgram Engine performs the computationally intensive task of voice AI. It also manages GPU devices and responds to requests from the API layer. Because the Deepgram Engine is decoupled from the Deepgram API, you can scale it independently from the API.

### Licensing and Usage

Deepgram components register with the Deepgram License Server, represented above within the Deepgram Cloud, in order to verify licensing and report usage. API and Engine containers can be configured to connect directly to the licensing server, or to proxy their communication through the [Deepgram License Proxy](/docs/license-proxy).

## Prerequisites

Prerequisites depend on how you deploy. [Amazon SageMaker](/docs/amazon-sagemaker) is the fastest path and requires only an AWS account, while deploying with Docker/Podman or Kubernetes requires a Deepgram Enterprise Plan.

### Amazon SageMaker

To deploy through SageMaker, you only need:

* an AWS account
* AWS IAM permissions for SageMaker and the AWS Marketplace (the [AmazonSageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) and [AWSMarketplaceManageSubscriptions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html) managed policies)

You subscribe to a Deepgram product on the AWS Marketplace and are billed through your existing AWS account — see [Pricing](/docs/amazon-sagemaker#pricing) for details. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) to get started.

For larger or longer-term deployments, [AWS Marketplace Private Offers](/docs/amazon-sagemaker#private-offers) are available with negotiated unit economics and committed-use terms. Contact your [AWS account team](https://aws.amazon.com/contact-us/sales-support/) or [Deepgram representative](https://deepgram.com/contact-us) to start a Private Offer.

### Docker, Podman, and Kubernetes

To self-host Deepgram with Docker/Podman or Kubernetes, you will need to enroll in a [Deepgram Enterprise Plan](https://deepgram.com/pricing). If you're interested, please [contact us](https://deepgram.com/contact-us/)! You'll be promptly connected with a Deepgram Account Representative who will help you every step of the way, from proof-of-concept to a full production environment.

Your Deepgram Account Representative will guide you through the process of setting up:

* a Deepgram product contract
* a [Deepgram Console account](https://console.deepgram.com/). Your contract will be tied to a specific Deepgram project, and you can manage your usage, credentials, billing, and more in the Deepgram Console.

Ahead of your planned self-hosted deployment, your Deepgram Account Representative will need:

* your Deepgram Console account email address
* your Deepgram Console Project ID

Providing this information will allow Deepgram to authorize your project for self-hosted usage, including access to container images and download links for AI models.

Detailed troubleshooting and on-demand support require an on-going support contract with Deepgram.

## Initial Setup

To setup your deployment environment and successfully self-host Deepgram products for the first time, the guides in this "Self-Hosted Deployments" section will take you through step by step.

Starting with this guide, you can use the "What's Next" section at the bottom of each page to take you from one guide to another until you have a working environment. Unless specifically indicated, each step in a given guide is required - skipping steps will leave you with an incomplete or broken environment.

Start with the [Deployment Environments](/docs/self-hosted-deployment-environments) guide to get an overview of the architecture. In that guide, you can decide on a container orchestrator and cloud platform, and proceed from that point. Alternatively, if you use AWS, you can deploy Deepgram through [Amazon SageMaker](/docs/deploy-amazon-sagemaker) for a simplified, managed deployment experience.

## Common Setup Path

All deployments follow the same initial setup path through environment preparation:

1. [Deployment Environments](/docs/self-hosted-deployment-environments) - Choose your architecture and infrastructure
2. Container orchestration choice: [Docker/Podman](/docs/dockerpodman) or [Kubernetes](/docs/kubernetes), or deploy via [Amazon SageMaker](/docs/deploy-amazon-sagemaker)
3. Platform setup (e.g., [Amazon Web Services](/docs/aws-docker-podman), [Google Cloud Platform](/docs/gcp-docker-podman), etc.)
4. [Drivers and Container Orchestration Tools](/docs/drivers-and-containerization-platforms) - GPU drivers and container runtime
5. [Self Service Licensing & Credentials](/docs/self-hosted-self-service-tutorial) - Authentication and access setup

## Choose Your Service Path

After completing the common setup, you'll choose between two deployment paths:

* **Speech-to-Text (STT):** Traditional transcription and real-time speech recognition - [Deploy STT Services](/docs/deploy-stt-services)
* **Text-to-Speech (TTS):** Conversational AI voice synthesis - [Deploy TTS Services](/docs/deploy-tts-services)

At the end of these guides, you should be able to make an inference request, and your deployment is complete!

---

What’s Next

Our next step will be to start talking about your deployment environment.

* [Deployment Environments](/docs/self-hosted-deployment-environments)
