---
title: "Cross-region inference routing"
source: https://developers.deepgram.com/docs/cross-region-routing-sagemaker.md
path: docs/cross-region-routing-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Cross-region inference routing

> Use Amazon SageMaker AI cross-Region inference routing with Deepgram: create an inference router over Deepgram endpoints in several AWS Regions or accounts, invoke it for pre-recorded (batch) and asynchronous requests, cap cross-Region traffic, and understand the limits, including no support for streaming.

Amazon SageMaker AI [cross-Region inference routing](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html) lets your application call one inference router instead of one Deepgram SageMaker Endpoint. The router sends each request to a healthy Deepgram Endpoint in its own AWS Region first. When that endpoint throttles or returns server errors, for example because it can't add GPU instances during a traffic spike, the router shifts new requests to your Deepgram Endpoints in other Regions or AWS accounts, then shifts them back gradually after the local endpoint recovers.

The router doesn't change your endpoints, models, containers, or auto-scaling. You still deploy and size a Deepgram Endpoint in each Region. Cross-Region inference routing costs nothing extra: you pay standard SageMaker AI and Deepgram license charges for the endpoints that serve requests, and standard Amazon CloudWatch rates for router metrics.

## Supported workloads

| Workload                   | Deepgram endpoint | Router API                   | Supported                                                                                                                  |
| -------------------------- | ----------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Pre-recorded (batch) audio | Real-time         | `InvokeInferenceRouter`      | Yes, up to 6 MB per request and 60 seconds of model time                                                                   |
| Asynchronous invocations   | Asynchronous      | `InvokeInferenceRouterAsync` | Yes, with input and output in Amazon S3                                                                                    |
| Streaming audio            | Real-time         | —                            | No. The router doesn't support streaming, so call `InvokeEndpointWithBidirectionalStream` on a Regional endpoint directly. |

> **Warning**
>
> **Asynchronous endpoints are temporarily unavailable for Marketplace-hosted Deepgram.** Asynchronous routing needs an asynchronous endpoint in every Region you route to. Until asynchronous endpoints are available again, use a real-time routing target for pre-recorded audio. Contact a [Deepgram representative](https://deepgram.com/contact-us) if your use case needs asynchronous processing.

Real-time routing is available in 32 commercial AWS Regions and asynchronous routing in 25. See [Tools and Regions](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html) in the AWS documentation for the current list.

## Before you begin

* **A Deepgram Endpoint in each Region.** Deploy the same Deepgram product and version in every Region you route to. Every destination must accept the same request and return the same response format; the router doesn't check this. The Model Package ARN is Region-specific, so copy the ARN for each Region. See [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker).
* **Quota in each Region.** Each standby endpoint needs instance quota in its own Region. See [Requesting SageMaker Quota](/docs/request-sagemaker-quota).
* **An AWS Marketplace subscription in each account.** Each AWS account that owns a destination endpoint subscribes to the Deepgram product and pays for its own endpoint. See [Subscribe on AWS Marketplace](/docs/subscribe-aws-marketplace).
* **An AWS CLI or SDK version that supports inference routers.** You manage routers with the `sagemaker` client and invoke them with the `sagemaker-inference-router-runtime` client, not `sagemaker-runtime`. The SageMaker AI console doesn't support inference routers.
* **IAM permissions.** Callers need `sagemaker:InvokeInferenceRouter` on the router and `sagemaker:InvokeEndpoint` on every destination endpoint. For asynchronous routing, they need `sagemaker:InvokeInferenceRouterAsync` and `sagemaker:InvokeEndpointAsync` instead.

## Route pre-recorded audio

A real-time routing target lists Deepgram real-time endpoints. Each routing target represents one model, so create one routing target per Deepgram product.

#### Create the router

Save the routing target as `routing-targets.json`. This example routes between Deepgram Endpoints in `us-west-2` and `us-east-1`:

```json
[
  {
    "Name": "nova-3",
    "Destinations": [
      { "ResourceArn": "arn:aws:sagemaker:us-west-2:111122223333:endpoint/deepgram-nova-3-usw2" },
      { "ResourceArn": "arn:aws:sagemaker:us-east-1:111122223333:endpoint/deepgram-nova-3-use1" }
    ]
  }
]
```

Create the router in the Region where most of your callers run. That Region is the router's local Region.

```bash
aws sagemaker create-inference-router \
  --region us-west-2 \
  --inference-router-name deepgram-router \
  --routing-targets file://routing-targets.json
```

Run `aws sagemaker describe-inference-router --region us-west-2 --inference-router-name deepgram-router` and wait until `Status` is `InService` and every destination's `RoutingStatus` is `Routable`.

#### Invoke the router

Call `InvokeInferenceRouter` with the router name and routing target name instead of `EndpointName`. The router passes the request body, `ContentType`, `Accept`, and `CustomAttributes` to the destination unchanged, so you pass Deepgram parameters in `CustomAttributes` as you do for [synchronous invocation](/docs/invoke-sagemaker-endpoint#synchronous-real-time).

```python
import json

import boto3
from botocore.config import Config

runtime = boto3.client(
    "sagemaker-inference-router-runtime",
    region_name="us-west-2",
    config=Config(read_timeout=170, retries={"total_max_attempts": 2, "mode": "standard"}),
)

with open("audio.wav", "rb") as f:
    response = runtime.invoke_inference_router(
        InferenceRouterName="deepgram-router",
        RoutingTargetName="nova-3",
        ContentType="audio/wav",
        Accept="application/json",
        CustomAttributes="v1/listen?model=nova-3&language=en&punctuate=true",
        Body=f.read(),
    )

print(response["InvokedRoutedResourceArn"], response["RoutingReason"])
result = json.loads(response["Body"].read())
transcript = result["results"]["channels"][0]["alternatives"][0]["transcript"]
```

The router can retry a request once on another destination, and each attempt has up to 60 seconds, so set the client read timeout to at least 170 seconds and allow at most 2 attempts.

Each response names the endpoint that served the request (`InvokedRoutedResourceArn`) and why the router chose it (`RoutingReason`): `local-preferred`, `failover`, `capacity-available`, or `only-healthy`.

> **Note**
>
> The router accepts request bodies up to 6 MB, compared with 25 MB for `InvokeEndpoint` on a Regional endpoint. Send larger pre-recorded files to a Regional endpoint directly.

## Route asynchronous invocations

An asynchronous routing target lists only Deepgram asynchronous endpoints, and sets the Amazon S3 output and failure locations on the routing target instead of on each endpoint. The input, output, and failure buckets must be in the router's Region and owned by the router's account.

```json
[
  {
    "Name": "nova-3-async",
    "Destinations": [
      { "ResourceArn": "arn:aws:sagemaker:us-west-2:111122223333:endpoint/deepgram-nova-3-async-usw2" },
      { "ResourceArn": "arn:aws:sagemaker:us-east-1:111122223333:endpoint/deepgram-nova-3-async-use1" }
    ],
    "AsyncInferenceConfig": {
      "OutputConfig": {
        "S3OutputPath": "s3://amzn-s3-demo-bucket/output/",
        "S3FailurePath": "s3://amzn-s3-demo-bucket/failure/"
      },
      "ClientConfig": { "MaxTimeInBacklogSeconds": 900 }
    }
  }
]
```

Upload the audio to Amazon S3 in the router's Region, then call `InvokeInferenceRouterAsync`:

```bash
aws sagemaker-inference-router-runtime invoke-inference-router-async \
  --region us-west-2 \
  --inference-router-name deepgram-router \
  --routing-target-name nova-3-async \
  --input-location s3://amzn-s3-demo-bucket/input/audio.wav \
  --content-type audio/wav \
  --custom-attributes "v1/listen?model=nova-3&language=en"
```

The response returns the `OutputLocation` and `FailureLocation` where the transcript or error lands. The router places each request on a local endpoint first, and moves it to another Region when the endpoint refuses it or doesn't start it within `MaxTimeInBacklogSeconds`. A request doesn't move after the Deepgram container starts processing it.

Each destination's execution role needs `s3:GetObject` on the input and `s3:PutObject` on the output path. See [Route asynchronous inference requests through an inference router](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html) for the full permissions and notification options.

## Plan standby capacity

The router moves traffic only to healthy destinations and doesn't add capacity, so size each standby endpoint for the traffic you expect it to absorb.

* Keep at least one instance in service in each real-time standby endpoint, and configure [auto-scaling](/docs/auto-scaling-sagemaker-streaming) so it adds instances before it throttles. Slow responses that succeed don't move traffic.
* To reserve a real-time endpoint's capacity for callers in its own Region, set `CrossRegionTrafficConfig` in its endpoint configuration. For example, `MaxInvocationsPerSecondPerInstance=50,MaxCrossRegionPercentPerEndpoint=25` limits routers in other Regions to 25% of 50 invocations per second per `InService` instance. Requests over the cap fail with `ThrottlingException`, and the router retries them on another destination. `CrossRegionTrafficConfig` doesn't apply to asynchronous endpoints.
* An asynchronous standby can scale to zero. Set `MaxTimeInBacklogSeconds` longer than the time the standby takes to scale out.
* Combine routing with [multiple instance types](/docs/auto-scaling-sagemaker#use-multiple-instance-types-for-resilience) on each endpoint. Instance pools fall back within a Region; the router falls back across Regions.

## Route to endpoints in other AWS accounts

A router can send requests to a Deepgram Endpoint that another AWS account owns. The endpoint owner attaches an endpoint policy with `aws sagemaker put-endpoint-policy` that allows the router's account to invoke the endpoint only through that router, using the `sagemaker:SourceInferenceRouterArn` condition key. The router owner grants its callers permission to invoke the router and the shared endpoint, then adds the endpoint's ARN as a destination. See [Route requests to endpoints in other AWS accounts](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-cross-account.html).

## Limitations

* The router doesn't support streaming, so live transcription and streaming text-to-speech can't fail over through it.
* The router runs in one Region. If that Region is impaired, calls to the router fail even when destinations in other Regions are healthy.
* You can't restrict a request to specific Regions. Add destinations only in Regions where your data may be processed.
* You can't set routing weights or health thresholds, or place another Region ahead of the router's Region.
* The router doesn't support `TargetVariant`, `TargetModel`, `InferenceComponentName`, or `SessionId`.
* Real-time requests have a 6 MB body limit and 60 seconds of model time per attempt. Model execution timeout increases for your account don't apply through the router.
* A router supports up to 20 routing targets with up to 10 destinations each.

## Related resources

* [Invoke a Deepgram SageMaker Endpoint](/docs/invoke-sagemaker-endpoint)
* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker)
* [Route requests across AWS Regions with cross-Region inference routing (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html)
* [Get started with inference routers (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-get-started.html)
* [Monitor inference routers (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-monitor.html)
