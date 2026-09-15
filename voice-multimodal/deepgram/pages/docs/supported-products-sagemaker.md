---
title: "Supported Products"
source: https://developers.deepgram.com/docs/supported-products-sagemaker.md
path: docs/supported-products-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Supported Products

Follow [this AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=deepgram\&CREATOR=6efa21f9-9a33-4cae-ba44-756436fa71dd\&FULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL\&filters=CREATOR%2CFULFILLMENT_OPTION_TYPE) link to see the Deepgram products that are supported on the SageMaker AI platform. No login to your AWS account is required to view this public AWS Marketplace website.

## Product listings

For Speech-to-Text (STT), Deepgram publishes a separate product listing for each combination of:

* **Model family** — such as Nova-3 or Flux
* **Language coverage** — monolingual or multilingual
* **Processing mode** — streaming or batch

For example, *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming* is one listing.

For Text-to-Speech (TTS), Deepgram publishes a single product listing per model family (such as Aura-2), with no separate listings for language coverage or processing mode. Subscribe to and deploy a SageMaker Endpoint for each product you wish to utilize. Your application code will need to route requests to the SageMaker Endpoint for the product you wish to run inference against.

Within a listing, individual languages are delivered as **versions** of the model package. A monolingual listing may offer one version covering English and French, and another covering Vietnamese and Thai. Read the version name and its release notes to understand the set of languages each version provides, and select the version that matches the languages you need when deploying.

*Language Requests*: If there is a transcription language that is not currently available on the AWS Marketplace, please work with your account manager to request additional language models to be added. For a full list of the Deepgram supported transcription languages, [check out this document](/docs/models-languages-overview). You can also view the [Changelog](https://developers.deepgram.com/changelog) to see recent product announcements.

## Instance types

Every Deepgram SageMaker product requires a GPU-accelerated instance. Choose an instance type from the table for the product you are deploying, and request [SageMaker quota](/docs/request-sagemaker-quota) for it before you create an endpoint.

| Product           | Recommended      | Also supported                                                                               | Not supported                           |
| ----------------- | ---------------- | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Nova-3 STT        | `ml.g6.2xlarge`  | `ml.g7.2xlarge`, `ml.g7e.2xlarge`, `ml.g6e.2xlarge`, `ml.g5.2xlarge`, `ml.g4dn.2xlarge`      | —                                       |
| Flux STT          | `ml.g6.2xlarge`  | `ml.g7.2xlarge`, `ml.g7e.2xlarge`, `ml.g6e.2xlarge`, `ml.g5.2xlarge`                         | `ml.g4dn.*` (no sm\_75 kernel)          |
| Aura-2 TTS        | `ml.g6.12xlarge` | `ml.g7.12xlarge`, `ml.g7e.12xlarge`, `ml.g5.12xlarge`, `ml.g6e.12xlarge`, `ml.g4dn.12xlarge` | Single-GPU types (Aura-2 needs 2+ GPUs) |
| Flux TTS (Aura-3) | `ml.g6e.2xlarge` | `ml.g7.2xlarge`, `ml.g7e.2xlarge`, `ml.g6.2xlarge`                                           | `ml.g5.*`, `ml.g4dn.*`                  |

SageMaker rejects an endpoint configuration whose instance type is not listed in the model package's `SupportedRealtimeInferenceInstanceTypes`. The `ml.g7.*` and `ml.g7e.*` families are available in model package versions published after the g7 rollout; if you deploy an older version, choose one of the other supported types. To check what a specific version supports, run `aws sagemaker describe-model-package --model-package-name <model-package-arn>`.

The host driver your instances boot with is set separately from the instance type. Current Deepgram model packages require a recent inference AMI version — see [Inference AMI Versions](/docs/deploy-amazon-sagemaker#inference-ami-versions).

## Related resources

* [Subscribe on AWS Marketplace](/docs/subscribe-aws-marketplace)
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Requesting SageMaker Quota](/docs/request-sagemaker-quota)
* [Deployment Environments](/docs/self-hosted-deployment-environments)
