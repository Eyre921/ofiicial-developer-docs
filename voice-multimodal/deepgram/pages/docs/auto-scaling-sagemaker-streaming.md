---
title: "Auto-Scaling Real-Time Endpoints"
source: https://developers.deepgram.com/docs/auto-scaling-sagemaker-streaming.md
path: docs/auto-scaling-sagemaker-streaming
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Auto-Scaling Real-Time Endpoints

A Deepgram **real-time** endpoint serves two kinds of requests: **streaming** over a bidirectional stream (`InvokeEndpointWithBidirectionalStream`, up to 30 minutes each) and **synchronous pre-recorded** requests (`InvokeEndpoint` — a single file up to 25 MB, returned in one immediate response, Deepgram's "batch" API). Both are in-flight invocations that load the instance, so concurrent requests is the right scaling signal — which is why the high-resolution `ConcurrentRequestsPerModel` metric is ideal here.

**Need scale-to-zero?** Real-time endpoints keep a minimum of one instance and cannot scale to zero. For batch workloads that can scale to zero during idle periods, see [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async).

Before configuring auto scaling, you must have a Deepgram SageMaker Endpoint deployed and running with status `InService`. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) for setup instructions.

## How it works

Amazon SageMaker integrates with [AWS Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) to add or remove instances backing your endpoint. When you create a target tracking scaling policy with the `ConcurrentRequestsPerModel` metric, SageMaker:

1. Monitors the number of concurrent in-flight requests (streaming connections and synchronous pre-recorded requests) per instance.
2. Triggers a scale-out when concurrency exceeds your target value.
3. Triggers a scale-in when concurrency drops below the target value.

Because `ConcurrentRequestsPerModel` is a high-resolution metric (10-second intervals), SageMaker detects the need to scale out up to 6x faster than standard one-minute metrics such as `InvocationsPerInstance`.

## Prerequisites

* A deployed Deepgram SageMaker Endpoint with status `InService`
* AWS IAM permissions for Application Auto Scaling:
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html): `AmazonSageMakerFullAccess`
  * [**IAM Policy**](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_id-based-policy-examples.html): Application Auto Scaling identity-based policies
* The [AWS CLI](https://aws.amazon.com/cli/) installed and configured, or the [AWS SDK for Python (boto3)](https://aws.amazon.com/sdk-for-python/) available in your environment

## Use multiple instance types for resilience

For improved availability, configure your endpoint with multiple instance types so SageMaker can fall back to an alternative pool when your preferred instance type is constrained. This applies to both real-time and asynchronous endpoints. See [Use multiple instance types for resilience](/docs/auto-scaling-sagemaker#use-multiple-instance-types-for-resilience) in the parent guide for configuration details and code examples.

## Register the scalable target

Before you can attach a scaling policy, register your SageMaker Endpoint variant as a scalable target with Application Auto Scaling. This defines the minimum and maximum instance count for horizontal scaling.

#### AWS CLI

```bash
aws application-autoscaling register-scalable-target \
  --service-namespace sagemaker \
  --resource-id endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount \
  --min-capacity 1 \
  --max-capacity 4
```

#### Python (boto3)

```python
import boto3

client = boto3.client("application-autoscaling")

client.register_scalable_target(
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    MinCapacity=1,
    MaxCapacity=4,
)
```

Replace `YOUR_ENDPOINT_NAME` with the name of your SageMaker Endpoint. `AllTraffic` is the default [SageMaker Endpoint Variant](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) name assigned when you create an endpoint with a single production variant. If you configured a custom variant name, replace `AllTraffic` with that name. Adjust `--min-capacity` and `--max-capacity` to match your expected traffic range.

## Create a target tracking scaling policy

Define a target tracking policy that uses the `ConcurrentRequestsPerModel` high-resolution metric. The `TargetValue` represents the desired number of concurrent streaming connections per instance. When the average concurrency across instances exceeds this value, SageMaker adds instances. When it drops below, SageMaker removes instances.

#### AWS CLI

Save the following policy configuration to a file named `scaling-policy.json`:

```json
{
  "TargetValue": 5.0,
  "PredefinedMetricSpecification": {
    "PredefinedMetricType": "SageMakerVariantConcurrentRequestsPerModelHighResolution"
  },
  "ScaleInCooldown": 300,
  "ScaleOutCooldown": 60
}
```

Apply the policy:

```bash
aws application-autoscaling put-scaling-policy \
  --policy-name deepgram-streaming-concurrency-policy \
  --service-namespace sagemaker \
  --resource-id endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration file://scaling-policy.json
```

#### Python (boto3)

```python
import boto3

client = boto3.client("application-autoscaling")

client.put_scaling_policy(
    PolicyName="deepgram-streaming-concurrency-policy",
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    PolicyType="TargetTrackingScaling",
    TargetTrackingScalingPolicyConfiguration={
        "TargetValue": 5.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "SageMakerVariantConcurrentRequestsPerModelHighResolution"
        },
        "ScaleInCooldown": 300,
        "ScaleOutCooldown": 60,
    },
)
```

### Configuration parameters

| Parameter              | Description                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TargetValue`          | The target number of concurrent requests per instance. Set this based on your benchmarking results.                                                                                   |
| `PredefinedMetricType` | Use `SageMakerVariantConcurrentRequestsPerModelHighResolution` for the high-resolution concurrency metric.                                                                            |
| `ScaleOutCooldown`     | (Optional) Seconds to wait after a scale-out before another scale-out can occur. A lower value (such as `60`) allows faster reaction to traffic spikes.                               |
| `ScaleInCooldown`      | (Optional) Seconds to wait after a scale-in before another scale-in can occur. A higher value (such as `300`) prevents premature removal of instances while streams are still active. |

## Choose a target value

The correct `TargetValue` depends on your instance type, Deepgram model, and feature configuration. Streaming connections hold GPU resources for the entire session, so each instance supports a finite number of concurrent streams at acceptable latency.

To determine the right target value:

1. Deploy a single instance and open concurrent streams incrementally.
2. Monitor response latency. The [Measuring streaming latency](/docs/measuring-streaming-latency) guide describes how to benchmark.
3. Identify the concurrency level at which average latency remains below 400 ms.
4. Set `TargetValue` to approximately 70-80% of that limit to give the auto scaler time to add capacity before latency degrades.

For example, if a `g5.2xlarge` instance handles 10 concurrent streams at acceptable latency, set `TargetValue` to `7` or `8`.

If your endpoint uses [heterogeneous instance pools](#use-multiple-instance-types-for-resilience), the predefined `ConcurrentRequestsPerModel` metric is not sufficient on its own because per-instance capacity varies across pools. Follow the AWS guidance on driving the scaling policy from a weighted custom metric for mixed fleets. See [Use heterogeneous instance type endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-heterogeneous.html) for details.

## Verify the scaling policy

After applying the policy, confirm it is active:

#### AWS CLI

```bash
aws application-autoscaling describe-scaling-policies \
  --service-namespace sagemaker \
  --resource-id endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic
```

#### Python (boto3)

```python
import boto3

client = boto3.client("application-autoscaling")

response = client.describe_scaling_policies(
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic",
)

for policy in response["ScalingPolicies"]:
    print(policy["PolicyName"], policy["PolicyType"])
```

You can also view the auto scaling configuration in the [Amazon SageMaker console](https://console.aws.amazon.com/sagemaker/home) under **Endpoints** > your endpoint > **Endpoint runtime settings**.

## Monitor scaling activity

Amazon CloudWatch automatically creates alarms when you apply a target tracking policy. You can monitor these alarms and the scaling activity in the CloudWatch console.

Key metrics to watch in the `AWS/SageMaker` namespace:

![CloudWatch Metrics console showing the ConcurrentRequestsPerModel metric for a SageMaker Endpoint Variant](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/511832b235f0bf021547acd94375c1bb907c5cf7cdbdb6e6b94756b7436af1b6/images/cloudwatch-concurrent-requests-per-model.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260817%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260817T113239Z&X-Amz-Expires=604800&X-Amz-Signature=588dc102e9a2c2923d3ef5075fe333dfe2655377c014c087fc6f831570e57927&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

| Metric                       | Description                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| `ConcurrentRequestsPerModel` | Number of in-flight requests per instance, including queued requests. Emitted every 10 seconds. |
| `InvocationsPerInstance`     | Number of invocations per instance per minute. Useful as a secondary metric.                    |

To view scaling events:

```bash
aws application-autoscaling describe-scaling-activities \
  --service-namespace sagemaker \
  --resource-id endpoint/YOUR_ENDPOINT_NAME/variant/AllTraffic
```

## FAQ

### Does auto-scaling scale down to 0 during periods of no traffic?

Not for real-time endpoints. SageMaker managed auto-scaling for real-time endpoints requires a minimum of 1 instance and scales between your configured minimum and maximum (both ≥ 1). To reduce costs during idle periods, you can delete and recreate endpoints via scheduled orchestration or workload-triggered provisioning — or use [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async), which **do** support scaling to zero.

---

What's Next

* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker)
* [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async)
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Measuring Streaming Latency](/docs/measuring-streaming-latency)
