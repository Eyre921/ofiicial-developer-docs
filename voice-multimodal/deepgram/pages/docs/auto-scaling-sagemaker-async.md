---
title: "Auto-Scaling Asynchronous SageMaker Endpoints"
source: https://developers.deepgram.com/docs/auto-scaling-sagemaker-async.md
path: docs/auto-scaling-sagemaker-async
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Auto-Scaling Asynchronous SageMaker Endpoints

Deepgram's speech-to-text models can be deployed on Amazon SageMaker as **asynchronous inference endpoints**, which queue incoming requests and process them from Amazon S3. Async endpoints handle **pre-recorded files only** (no streaming) — payloads up to **1 GB**, processing times up to **one hour**, and near real-time latency — and, unlike real-time endpoints, they can **autoscale to zero** when there are no requests to process, so you only pay while the endpoint is actively working.

This guide covers how to configure autoscaling — including scale-to-zero — for an asynchronous Deepgram endpoint. For a comparison of endpoint types and when to use each, see [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker).

**Need live streaming instead?** This page covers batch/non-streaming workloads on asynchronous endpoints. For live streaming speech-to-text on real-time endpoints, see [Auto-Scaling Real-Time Endpoints](/docs/auto-scaling-sagemaker-streaming). Real-time endpoints scale between a minimum and maximum instance count (both ≥ 1) and **cannot** scale to zero.

Asynchronous endpoints are the right choice when you process pre-recorded audio, work with large files (up to 1 GB), or have spiky or sporadic traffic — they can autoscale to zero when the queue is empty, so you only pay while requests are processing.

## How it works

SageMaker integrates with AWS Application Auto Scaling to adjust the number of instances behind your endpoint in response to load. For asynchronous endpoints, the relevant signal is the **request queue depth**, exposed through the `ApproximateBacklogSizePerInstance` CloudWatch metric (the number of queued requests divided by the current instance count).

A target-tracking scaling policy adds instances when the per-instance backlog rises above your target and removes them as the backlog drains. Because async endpoints allow a minimum capacity of zero, the fleet can scale all the way down to no instances during idle periods. Requests received while at zero instances are **queued**, and the endpoint scales back up to process them.

**Scaling up from zero requires an extra policy.** By default, a scaled-to-zero endpoint will not scale up until the backlog exceeds your target value — which can mean a long wait for the first request after an idle period. Add the optional [scale-up-from-zero policy](#scale-up-from-zero-for-new-requests) so the endpoint wakes on the first queued request.

## Prerequisites

* A Deepgram model deployed to a SageMaker asynchronous inference endpoint (an endpoint configuration with an `AsyncInferenceConfig` object). See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker).
* An Amazon S3 bucket for request and response payloads.
* IAM permissions to register scalable targets and manage scaling policies (for example, `AmazonSageMakerFullAccess` plus Application Auto Scaling permissions).
* The AWS CLI or AWS SDK for Python (Boto3) configured with credentials for your account.

## Use multiple instance types for resilience

For improved availability, configure your endpoint with multiple instance types so SageMaker can fall back to an alternative pool when your preferred instance type is constrained. This applies to both real-time and asynchronous endpoints. See [Use multiple instance types for resilience](/docs/auto-scaling-sagemaker#use-multiple-instance-types-for-resilience) in the parent guide for configuration details and code examples.

## Register the scalable target

Register your endpoint variant with Application Auto Scaling and set the instance bounds. The key difference from a real-time endpoint is `MinCapacity=0`, which allows the endpoint to scale down to zero instances.

```python
import boto3

client = boto3.client('application-autoscaling')

# Application Auto Scaling references the endpoint variant by resource ID
resource_id = 'endpoint/' + endpoint_name + '/variant/' + variant_name  # e.g. 'variant1'

client.register_scalable_target(
    ServiceNamespace='sagemaker',
    ResourceId=resource_id,
    ScalableDimension='sagemaker:variant:DesiredInstanceCount',
    MinCapacity=0,   # Allows scale-to-zero when the queue is empty
    MaxCapacity=5,   # Set to your peak instance count
)
```

## Create a target-tracking scaling policy

Apply a target-tracking policy on the `ApproximateBacklogSizePerInstance` custom metric. The `TargetValue` is the number of queued requests per instance you're willing to tolerate before adding capacity — start with a small value and tune against your latency requirements.

```python
client.put_scaling_policy(
    PolicyName='AsyncBacklogTargetTracking',
    ServiceNamespace='sagemaker',
    ResourceId=resource_id,
    ScalableDimension='sagemaker:variant:DesiredInstanceCount',
    PolicyType='TargetTrackingScaling',
    TargetTrackingScalingPolicyConfiguration={
        'TargetValue': 5.0,  # Target ApproximateBacklogSizePerInstance
        'CustomizedMetricSpecification': {
            'MetricName': 'ApproximateBacklogSizePerInstance',
            'Namespace': 'AWS/SageMaker',
            'Dimensions': [
                {'Name': 'EndpointName', 'Value': endpoint_name},
            ],
            'Statistic': 'Average',
        },
        # Optional: tune how quickly the endpoint scales in/out
        'ScaleInCooldown': 300,
        'ScaleOutCooldown': 300,
    },
)
```

### Choose a target value

Benchmark a single instance with representative audio files to find the per-instance backlog at which queue wait times stay within your latency budget. Set `TargetValue` to a level below that threshold so the policy adds capacity before the queue grows faster than one instance can drain it.

## Scale up from zero for new requests

When an endpoint has scaled down to zero, the target-tracking policy above won't bring it back until the backlog exceeds your target value — so a single request arriving after an idle period can sit in the queue for a long time. To wake the endpoint on the **first** queued request, add a step-scaling policy driven by the `HasBacklogWithoutCapacity` metric, which fires when there are queued requests but zero instances.

```python
cw_client = boto3.client('cloudwatch')

# 1. Step-scaling policy: add one instance when at zero capacity with a backlog
response = client.put_scaling_policy(
    PolicyName='HasBacklogWithoutCapacity-ScalingPolicy',
    ServiceNamespace='sagemaker',
    ResourceId=resource_id,
    ScalableDimension='sagemaker:variant:DesiredInstanceCount',
    PolicyType='StepScaling',
    StepScalingPolicyConfiguration={
        'AdjustmentType': 'ChangeInCapacity',
        'MetricAggregationType': 'Average',
        'Cooldown': 300,
        'StepAdjustments': [
            {'MetricIntervalLowerBound': 0, 'ScalingAdjustment': 1},
        ],
    },
)

# 2. Alarm on HasBacklogWithoutCapacity that triggers the policy above
cw_client.put_metric_alarm(
    AlarmName='HasBacklogWithoutCapacity-Alarm',
    MetricName='HasBacklogWithoutCapacity',
    Namespace='AWS/SageMaker',
    Statistic='Average',
    EvaluationPeriods=2,
    DatapointsToAlarm=2,
    Threshold=1,
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    TreatMissingData='missing',
    Dimensions=[
        {'Name': 'EndpointName', 'Value': endpoint_name},
    ],
    Period=60,
    AlarmActions=[response['PolicyARN']],
)
```

With both policies in place, the target-tracking policy handles scaling under sustained load, while the step-scaling policy ensures a scaled-to-zero endpoint wakes promptly on the first incoming request.

## Monitor scaling activity

Watch these CloudWatch metrics (namespace `AWS/SageMaker`, dimensioned by `EndpointName`) to confirm scaling behaves as expected:

* **`ApproximateBacklogSize`** — total requests in the queue.
* **`ApproximateBacklogSizePerInstance`** — the target-tracking signal.
* **`HasBacklogWithoutCapacity`** — non-zero when requests are queued but no instances are running (the scale-up-from-zero trigger).
* **Instance count** — confirm the endpoint scales to zero when idle and back up under load.

## FAQ

**Q: Does the asynchronous endpoint scale down to 0 during periods of no traffic?**

**A:** Yes. Set `MinCapacity=0` when registering the scalable target. Requests received while at zero instances are queued, and the endpoint scales back up to process them. Add the [`HasBacklogWithoutCapacity` scale-up policy](#scale-up-from-zero-for-new-requests) so the endpoint wakes on the first queued request instead of waiting for the backlog to exceed your target value.

**Q: How is this different from real-time endpoint autoscaling?**

**A:** Real-time endpoints serve streaming and synchronous pre-recorded requests, scale on concurrent in-flight requests (`ConcurrentRequestsPerModel`), and require a minimum of 1 instance. Asynchronous endpoints serve pre-recorded files only, scale on queue depth (`ApproximateBacklogSizePerInstance`), and can scale to zero. See [Auto-Scaling Real-Time Endpoints](/docs/auto-scaling-sagemaker-streaming) for the real-time guide.

**Q: What's the maximum input size and processing time?**

**A:** Asynchronous endpoints accept payloads up to 1 GB and processing times up to one hour per request. For the 25 MB real-time limit and streaming details, see [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker).

## Related resources

* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker)
* [Auto-Scaling Real-Time Endpoints](/docs/auto-scaling-sagemaker-streaming)
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Amazon SageMaker Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
* [Autoscale an asynchronous endpoint (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-autoscale.html)
