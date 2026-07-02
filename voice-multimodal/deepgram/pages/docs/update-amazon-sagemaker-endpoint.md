---
title: "Update an Amazon SageMaker Endpoint"
source: https://developers.deepgram.com/docs/update-amazon-sagemaker-endpoint.md
path: docs/update-amazon-sagemaker-endpoint
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Update an Amazon SageMaker Endpoint

When you ship a newer Deepgram model version, switch language models, or apply a new [environment variable configuration](/docs/configure-sagemaker-deployments), you need to update an Amazon SageMaker Endpoint that is already serving production traffic. Amazon SageMaker AI handles this through the [`UpdateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) API, which replaces the running fleet with a new fleet without taking the Endpoint offline.

Because Deepgram is distributed through the AWS Marketplace, SageMaker performs an **all-at-once** update: it provisions a new fleet, shifts 100% of the traffic to it in a single step, and terminates the old fleet. This is the only deployment strategy available to AWS Marketplace containers — see [Other deployment guardrails](#other-deployment-guardrails) below.

## When to update an endpoint

Common reasons to update a Deepgram SageMaker Endpoint include:

* Promoting a newer Deepgram Model Package version published to the AWS Marketplace.
* Switching the underlying instance type to scale capacity or reduce cost.
* Changing [Deepgram environment variables](/docs/configure-sagemaker-deployments) to tune `api.toml` or `engine.toml` settings (for example, `flux.max_streams` or `max_active_requests`).
* Migrating between Deepgram language models or product listings.

Each of these changes is applied by creating a new SageMaker **Model** and/or **Endpoint Configuration** and then calling `UpdateEndpoint` with the new Endpoint Configuration. If only the Endpoint Configuration changes — for example, a different instance type — you can reuse the existing Model.

## How updates work for Deepgram

When you call `UpdateEndpoint` against a Deepgram Endpoint, SageMaker:

1. Provisions a complete new fleet (the green fleet) using the new Endpoint Configuration, while the existing fleet (the blue fleet) continues to serve traffic.
2. Once the green fleet is healthy, shifts **all** traffic from the blue fleet to the green fleet in a single step.
3. Terminates the blue fleet.

Because the update is all-at-once, there is no incremental traffic shift, no baking period to evaluate the new fleet on a fraction of traffic before commitment, and no automatic rollback based on CloudWatch alarms. The Endpoint stays in service for the entire procedure — clients continue to be served by the blue fleet until SageMaker performs the cutover.

## Update an endpoint

If the underlying Model needs to change — for example, a new Marketplace Model Package version, a different ECR image, or new environment variables — create a new SageMaker **Model**. See the AWS CLI and Boto3 examples in [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments) for how to create a Model. If the Model can be reused, skip this step.

Create a new **Endpoint Configuration** that references the Model and uses the same variant name as the existing Endpoint Configuration. The variant name (typically `AllTraffic`) must match for SageMaker to update the Endpoint in place.

Call [`UpdateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) with the existing Endpoint name and the new Endpoint Configuration name.

```bash title="AWS CLI"
aws sagemaker update-endpoint \
  --endpoint-name my-deepgram-streaming-stt \
  --endpoint-config-name my-deepgram-streaming-stt-config-v2
```

```python title="Boto3"
import boto3

sagemaker = boto3.client("sagemaker")

sagemaker.update_endpoint(
    EndpointName="my-deepgram-streaming-stt",
    EndpointConfigName="my-deepgram-streaming-stt-config-v2",
)
```

After you initiate the update, monitor progress in the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/home) under **Endpoints** > your endpoint, or by polling the [`DescribeEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API. The Endpoint's `EndpointStatus` transitions through `Updating` and back to `InService` once the cutover completes.

## Considerations for Deepgram workloads

* **Variant name must match.** When you create the new Endpoint Configuration, use the same variant name (typically `AllTraffic`) as the existing configuration. SageMaker requires this for in-place updates.
* **Streaming connections are long-lived.** Deepgram streaming Speech-to-Text Endpoints hold bidirectional WebSocket connections for [up to 30 minutes](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html). Existing connections are not migrated to the green fleet — they continue on the original instances until they close. Plan updates to coincide with periods of lower streaming traffic if you want to minimize disruption.
* **GPU capacity.** During the cutover, SageMaker briefly runs both the blue and green fleets in parallel. Confirm that your AWS account has sufficient GPU instance quota in the target region to accommodate the full additional fleet before starting the update.
* **Monitor the rollout.** Because the Marketplace update path does not include automated alarm-based rollback, watch your application's error tracking and the [Amazon CloudWatch metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html) for the Endpoint after the cutover (for example, `ModelLatency` and any application-level error metrics you emit). If you observe regressions, roll back manually by calling `UpdateEndpoint` again with the previous Endpoint Configuration.

## Other deployment guardrails

Amazon SageMaker AI supports additional [deployment guardrails](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html) — including blue/green deployments with [canary](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-canary.html) and [linear](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-linear.html) traffic shifting, and [rolling deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-rolling.html) — that provide gradual traffic shifting, baking periods, and CloudWatch-based auto-rollback. These guardrails are not available for AWS Marketplace containers like Deepgram. Per the [deployment guardrails exclusions](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-exclusions.html), Endpoints that use Marketplace containers fall back to a blue/green deployment with all-at-once traffic shifting and no final baking period.

***

What's Next

* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)
* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker-streaming)
* [Observability for Amazon SageMaker](/docs/observability-sagemaker)
