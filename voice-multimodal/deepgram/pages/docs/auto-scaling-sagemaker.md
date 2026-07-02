---
title: "Auto-Scaling SageMaker Endpoints"
source: https://developers.deepgram.com/docs/auto-scaling-sagemaker.md
path: docs/auto-scaling-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Auto-Scaling SageMaker Endpoints

Deepgram models deployed on Amazon SageMaker can automatically scale the number of instances behind an endpoint in response to load, using AWS Application Auto Scaling. How you configure autoscaling — and whether the endpoint can scale all the way down to zero — depends on which type of endpoint you deploy.

This page explains the two endpoint types and helps you choose between them. For step-by-step setup, follow the guide that matches your deployment:

* **[Auto-Scaling Real-Time Endpoints](/docs/auto-scaling-sagemaker-streaming)** — for streaming requests and synchronous pre-recorded requests that return an immediate response.
* **[Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async)** — for pre-recorded files processed from a queue, with scale-to-zero support.

## Real-time vs. asynchronous endpoints

Both endpoint types can transcribe pre-recorded audio — the difference is *how* the request is processed and returned, and that determines which signal each scales on.

A **real-time endpoint** serves two kinds of requests:

* **Streaming** — live audio over a bidirectional stream (`InvokeEndpointWithBidirectionalStream`), up to 30 minutes per connection, with results streamed back as the audio is processed.
* **Synchronous (pre-recorded)** — a single file up to 25 MB submitted with `InvokeEndpoint`, processed in real time and returned in one immediate, synchronous response (Deepgram's "batch" API).

An **asynchronous endpoint** serves one kind of request:

* **Pre-recorded files only** — a file up to 1 GB, submitted to a queue with `InvokeEndpointAsync` via an S3 pointer and processed asynchronously with near real-time latency. The result is written back to S3; there is no synchronous response and no streaming.

|                    | **Real-time endpoint**                                                                | **Asynchronous endpoint**                                                 |
| ------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Supported requests | Streaming **and** synchronous pre-recorded                                            | Pre-recorded files only                                                   |
| Invocation         | `InvokeEndpoint` (synchronous) or `InvokeEndpointWithBidirectionalStream` (streaming) | `InvokeEndpointAsync` with an S3 payload pointer                          |
| Max input size     | 25 MB per file                                                                        | 1 GB per file                                                             |
| Max duration       | 30 min per streaming connection                                                       | Up to 1 hour processing per request                                       |
| Response           | Immediate / synchronous (or streamed)                                                 | Asynchronous — written to S3 (near real-time)                             |
| Scales to zero     | No — minimum 1 instance                                                               | **Yes** — `MinCapacity=0`                                                 |
| Scaling metric     | `ConcurrentRequestsPerModel`                                                          | `ApproximateBacklogSizePerInstance`                                       |
| Setup guide        | [Auto-Scaling Real-Time Endpoints](/docs/auto-scaling-sagemaker-streaming)            | [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async) |

### Which should I use?

* **Choose a real-time endpoint** when you need live streaming transcription, or when you transcribe pre-recorded files of 25 MB or less and want an immediate synchronous response. These endpoints keep a minimum of one instance running at all times.
* **Choose an asynchronous endpoint** when you transcribe pre-recorded files — especially large ones (up to 1 GB) — or have spiky or sporadic traffic where paying for idle instances is wasteful. Asynchronous endpoints can autoscale to zero when the queue is empty, so you only pay while requests are processing. They do not support live streaming.

## How autoscaling works

Both endpoint types integrate with AWS Application Auto Scaling. At a high level, you:

1. **Register a scalable target** — tell Application Auto Scaling which endpoint variant to scale and the minimum and maximum instance counts.
2. **Define a scaling policy** — a target-tracking policy that adds or removes instances to keep a chosen CloudWatch metric near a target value.
3. **Apply the policy** and monitor scaling activity in CloudWatch.

The difference between the two is the **signal** they scale on:

* **Real-time endpoints** scale on concurrency — the `ConcurrentRequestsPerModel` metric — because each in-flight request, whether a streaming connection or a synchronous pre-recorded request, represents load on an instance.
* **Asynchronous endpoints** scale on queue depth — the `ApproximateBacklogSizePerInstance` metric — and allow a minimum capacity of zero, enabling scale-to-zero during idle periods.

For the exact metrics, policies, and code, follow the guide for your endpoint type below.

## Use multiple instance types for resilience

A single instance type can become temporarily unavailable in a given region or Availability Zone, which may prevent your endpoint from scaling out when traffic increases. To reduce this risk, configure your endpoint variant with multiple instance types in priority order using SageMaker's [heterogeneous instance pools](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-heterogeneous.html). SageMaker provisions instances from your highest-priority pool first and falls back to lower-priority pools when capacity in the preferred pool is constrained.

This applies to both real-time and asynchronous endpoints.

The following endpoint configuration lists `ml.g6.2xlarge` as the preferred instance type and falls back to `ml.g6e.2xlarge` if the first pool is unavailable:

```python title="Boto3"
import boto3

sagemaker = boto3.client("sagemaker")

sagemaker.create_endpoint_config(
    EndpointConfigName="my-deepgram-endpoint-config",
    ProductionVariants=[
        {
            "VariantName": "AllTraffic",
            "ModelName": "my-model",
            "InitialInstanceCount": 2,
            "InstancePools": [
                {
                    "InstanceType": "ml.g6.2xlarge",
                    "Priority": 1,
                },
                {
                    "InstanceType": "ml.g6e.2xlarge",
                    "Priority": 2,
                },
            ],
            "VariantInstanceProvisionTimeoutInSeconds": 600,
        }
    ],
)
```

When you use multiple instance types, give additional consideration to your scaling policy. The predefined scaling metrics (`ConcurrentRequestsPerModel` for real-time endpoints, `ApproximateBacklogSizePerInstance` for async endpoints) do not account for capacity differences between pools, so a target tracking policy that uses them directly may scale unevenly across instance types. For mixed fleets, AWS recommends driving the scaling policy from a weighted custom metric instead. See the [AWS heterogeneous endpoints documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-heterogeneous.html) for details on configuring weighted custom metrics for heterogeneous endpoints.

## Related resources

* [Auto-Scaling Real-Time Endpoints](/docs/auto-scaling-sagemaker-streaming)
* [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async)
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Amazon SageMaker Asynchronous Inference (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
* [Automatic scaling of Amazon SageMaker models (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
