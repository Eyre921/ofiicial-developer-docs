---
title: "Troubleshooting"
source: https://developers.deepgram.com/docs/troubleshooting-sagemaker.md
path: docs/troubleshooting-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Troubleshooting

If you're experiencing any issues with your Deepgram deployment on Amazon SageMaker AI, start with the Deepgram container logs in Amazon CloudWatch, then work through the common causes below.

## View container logs

If you open the SageMaker AI Endpoint resource details, there will be a link to open the Amazon CloudWatch Log Group for that endpoint.
Within the CloudWatch Log Group, there should be a Log Stream that contains the Deepgram logs for all components.
You can use the Amazon CloudWatch Logs [Live Tail feature](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) to watch logs in near-real-time
while you are sending requests to the Deepgram API, via the SageMaker AI APIs.

To use the CloudWatch Logs Live Tail feature locally, from the [AWS CLI tool](https://aws.amazon.com/cli/), you can use the following command.

```bash
aws logs tail --follow /aws/sagemaker/Endpoints/YOUR_SAGEMAKER_ENDPOINT_NAME --region YOUR_AWS_REGION
```

## Endpoint fails to start (CUDA / driver preflight)

Current Deepgram model packages run a CUDA 13 runtime and require NVIDIA driver 580 or later on the host. If the endpoint boots on an older default inference AMI — which is what happens when the Endpoint Configuration was created from the SageMaker AI console, or without `InferenceAmiVersion` set — the container fails its CUDA preflight check and the endpoint never reaches `InService`. The CloudWatch log stream for the endpoint contains a line similar to:

```
[cuda-preflight] To fix this, set InferenceAmiVersion to al2023-ami-sagemaker-inference-gpu-4-1 on your endpoint configuration's ProductionVariant. That AMI provides NVIDIA driver 580 with CUDA 13.
```

To fix this, create a new Endpoint Configuration with the AWS CLI, Boto3, or Terraform that sets `InferenceAmiVersion` to `al2023-ami-sagemaker-inference-gpu-4-1` on the production variant, then create or [update](/docs/update-amazon-sagemaker-endpoint) the endpoint with it. See [Inference AMI Versions](/docs/deploy-amazon-sagemaker#inference-ami-versions) for the available versions and Deepgram's recommendation.

## Endpoint is InService but every request returns 400

A `400` on every request usually means the request does not match the product you deployed, not that the endpoint is unhealthy.

* **Multilingual Nova-3 listings require `language=multi`.** Sending `language=en` (or any single language code) to a multilingual Nova-3 endpoint returns `400`, which looks like a dead endpoint. Pass `language=multi` in the query string.
* **Flux multilingual is selected by model name, not a language parameter.** Use `model=flux-general-multi`; there is no `language` parameter for Flux multilingual.
* **Streaming-mode bundles reject synchronous invocation.** A product listing published for streaming returns `400 No such model/language/tier` when called through the synchronous `/invocations` path (`InvokeEndpoint`). Use `InvokeEndpointWithBidirectionalStream` for streaming listings, or deploy the batch listing for synchronous and asynchronous invocation. See [Invoke a Deepgram SageMaker Endpoint](/docs/invoke-sagemaker-endpoint).

## Endpoint stuck in Creating

If the endpoint stays in `Creating` well beyond the usual several minutes, or moves to `Failed`, check `FailureReason`:

```bash
aws sagemaker describe-endpoint --endpoint-name YOUR_SAGEMAKER_ENDPOINT_NAME --query '{Status:EndpointStatus,FailureReason:FailureReason}'
```

Common causes:

* **`ModelDataDownloadTimeoutInSeconds` is too low.** Large multilingual bundles can take longer than the default download window. Recreate the Endpoint Configuration with a higher value on the production variant (Deepgram's CLI steps use `600`; large multilingual Nova-3 bundles may need more).
* **Capacity or quota.** The instance type is unavailable in the Availability Zone, or your account quota for it is `0`. A `ResourceLimitExceeded` failure reason points to quota — see [Requesting SageMaker Quota](/docs/request-sagemaker-quota).

## Checklist

If you experience any issues using Deepgram services running on the Amazon SageMaker AI platform, please review this checklist before contacting Deepgram support.

* Ensure that your application's AWS IAM User or IAM Role has permission to call the `InvokeEndpointWithBidirectionalStream` SageMaker AI action.
* Ensure your application is targeting the correct AWS account and region, where your SageMaker Endpoint exists.
* Ensure the Deepgram product you've deployed (eg. streaming Speech-to-Text), from the AWS Marketplace, corresponds to the Deepgram API you're calling.
* Ensure the Endpoint Configuration pins `InferenceAmiVersion` to `al2023-ami-sagemaker-inference-gpu-4-1`. The SageMaker AI console does not expose this setting; create the Endpoint Configuration with the AWS CLI or API, or with [Terraform](/docs/terraform-deploy-sagemaker#inference-ami-versions). See [Inference AMI Versions](/docs/deploy-amazon-sagemaker#inference-ami-versions).
* If you subscribed through a private offer in an AWS organization, ensure the linked account deploying the endpoint has accepted the offer or holds a License Manager entitlement. See [Private offers](/docs/subscribe-aws-marketplace#private-offers).

## Related resources

* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Health Checks & Automatic Recovery](/docs/health-checks-sagemaker)
* [Observability](/docs/observability-sagemaker)
