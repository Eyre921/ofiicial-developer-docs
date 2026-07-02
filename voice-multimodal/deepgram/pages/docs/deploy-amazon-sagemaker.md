---
title: "Deploy Deepgram on Amazon SageMaker"
source: https://developers.deepgram.com/docs/deploy-amazon-sagemaker.md
path: docs/deploy-amazon-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deploy Deepgram on Amazon SageMaker

For an overview of running Deepgram on SageMaker, including benefits, tradeoffs, and pricing, see [Amazon SageMaker](/docs/amazon-sagemaker).

## Supported Products

Follow [this AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=deepgram\&CREATOR=6efa21f9-9a33-4cae-ba44-756436fa71dd\&FULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL\&filters=CREATOR%2CFULFILLMENT_OPTION_TYPE) link to see the Deepgram products that are supported on the SageMaker AI platform. No login to your AWS account is required to view this public AWS Marketplace website.

For Speech-to-Text (STT), Deepgram publishes a separate product listing for each combination of:

* **Model family** — such as Nova-3 or Flux
* **Language coverage** — monolingual or multilingual
* **Processing mode** — streaming or batch

For example, *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming* is one listing.

For Text-to-Speech (TTS), Deepgram publishes a single product listing per model family (such as Aura-2), with no separate listings for language coverage or processing mode. Subscribe to and deploy a SageMaker Endpoint for each product you wish to utilize. Your application code will need to route requests to the SageMaker Endpoint for the product you wish to run inference against.

Within a listing, individual languages are delivered as **versions** of the model package. A monolingual listing may offer one version covering English and French, and another covering Vietnamese and Thai. Read the version name and its release notes to understand the set of languages each version provides, and select the version that matches the languages you need when deploying.

*Language Requests*: If there is a transcription language that is not currently available on the AWS Marketplace, please work with your account manager to request additional language models to be added. For a full list of the Deepgram supported transcription languages, [check out this document](https://developers.deepgram.com/docs/models-languages-overview). You can also view the [Changelog](https://developers.deepgram.com/changelog) to see recent product announcements.

## Limitations

When using Deepgram services in Amazon SageMaker, please be aware of the following limitations.

* Deepgram cannot call Large Langage Model (LLM) services
* Deepgram cannot invoke user-defined [callback URLs](/docs/callback)
* Passing a JSON payload for transcription (e.g., referencing a file stored in cloud storage via URL) is unsupported, as the SageMaker isolation model prevents the container from reaching out to external cloud storage
* Deepgram [custom metrics](/docs/metrics-guide) are not currently available through Amazon SageMaker Endpoints
* For streaming invocations, the connection remains open until you explicitly close the input stream or the endpoint closes the connection, supporting [up to 30 minutes of connection time](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-test-endpoints.html#realtime-endpoints-test-endpoints-sdk:~:text=The%20connection%20remains%20open%20until%20you%20explicitly%20close%20the%20input%20stream%20or%20the%20endpoint%20closes%20the%20connection%2C%20supporting%20up%20to%2030%20minutes%20of%20connection%20time).
* For non-streaming invocations, the [maximum size of the input data is 25 MB](https://docs.aws.amazon.com/marketplace/latest/userguide/ml-service-restrictions-and-limits.html#:~:text=For%20an%20endpoint%2C%20limit%20the%20maximum%20size%20of%20the%20input%20data%20per%20invocation%20to%2025%20MB.%20This%20value%20can%27t%20be%20adjusted) for real-time endpoints. For larger files, use [asynchronous endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html), which support payloads up to 1 GB with near real-time latency and can scale to zero when there are no requests to be processed.

## Prerequisites

* An AWS account
* AWS IAM permissions to SageMaker and Marketplace
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html): AWSMarketplaceManageSubscriptions
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html): AmazonSageMakerFullAccess

## Subscribe to Deepgram Products

Before you can deploy Deepgram on Amazon SageMaker AI, you'll need to subscribe to the product in the AWS Marketplace.
Keep in mind that you are not billed for the product until you deploy an [Amazon SageMaker AI Endpoint resource](https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-console.html).

Login to the [AWS Management Console](https://console.aws.amazon.com/) for the account you'd like to deploy in

Navigate to the [AWS Marketplace console, pre-filtered for Deepgram SageMaker Model products](https://us-east-1.console.aws.amazon.com/marketplace/search#!mpSearch/search?text=deepgram\&filter%3AFULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL)

Click on the Deepgram product you're interested in deploying (eg. *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming*)

Click on the **View Purchase Options** button

Ensure the **Offer Type** of **Public Offer** is selected (*if required*)

Scroll down and click the **Subscribe** button

## Create AWS IAM Role for SageMaker Execution

Follow [the AWS documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) to create an AWS Identity & Access Management (IAM) role that will be used to run SageMaker Model Endpoints.
You only need to create a single SageMaker execution role, and can reuse this IAM Role to deploy multiple SageMaker Endpoints.

## Deploy Deepgram Model Package for SageMaker AI

Once you've subscribed to the Deepgram product on AWS Marketplace, you can deploy a [SageMaker AI Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html).
The SageMaker "Endpoint" resource represents the compute instance that runs the Deepgram Voice AI services.
It will take several minutes to deploy a SageMaker Endpoint, once you initiate the resource creation.

**Which endpoint type should you deploy?** Deploy a **real-time** endpoint for live streaming and synchronous (single-file) transcription, or an **asynchronous** endpoint for large pre-recorded files (up to 1 GB) and scale-to-zero. See [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker) for a full comparison.

In the AWS Management Console, navigate to the [AWS Marketplace **Manage subscriptions** console](https://us-east-1.console.aws.amazon.com/marketplace/subscriptions)

On the **Active subscriptions** tab, find the subscription for the Deepgram product you want to deploy (eg. *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming*)

Click the **Configure** button in the **Actions** column on the right-hand side

In the **Setup** box, under **Service**, choose **Amazon SageMaker AI console**

Under the **Version** header, select the product version from the dropdown. If the listing has more than one version, read the version name and the release notes to understand the set of languages (or features) each version provides, and choose the version that matches your needs

Select the AWS **Region** you want to deploy to

Under **Amazon SageMaker options**, keep **Create real-time inference endpoint** selected

Click the **Create endpoint** button. You'll be redirected to the Amazon SageMaker AI console

Provide a name for the model (eg. `deepgram-streaming-stt`)

Under **IAM Role**, select the [SageMaker execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) that you created

Click the **Next** button

Provide an **Endpoint Name**, such as `my-deepgram-streaming-stt`

**(Asynchronous endpoints only) Configure async invocation.**

If you are deploying an **asynchronous** endpoint, expand the **Async invocation config** section and toggle it on, then set the **S3 output path** — the S3 location (for example, `s3://your-bucket/output/`) where transcription results are written. The remaining fields are optional.

For a **real-time** endpoint (streaming and synchronous invocation), leave **Async invocation config** turned **off** and continue to the next step unchanged.

To autoscale an asynchronous endpoint — including scaling to zero when idle — see [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async).

Under **Variants** ➡️ **Production**, scroll all the way to the right, and click **Edit**

If desired, select **Choose Other Instance Type** and select the instance type you want to deploy to (eg. `g5.2xlarge`), then click **Save**

Click the **Create Endpoint Configuration** button

Click the **Submit** button, to create the SageMaker AI Endpoint

After following these steps, you should see a new Endpoint in your AWS account.
If you don't see the Endpoint, ensure that you have selected the correct AWS region in the [AWS Management Console](https://console.aws.amazon.com/sagemaker/home?#/endpoints).
It may take several minutes for the Endpoint to change to status `InService`.
Once the Endpoint status has changed to `InService`, you can monitor the Amazon CloudWatch Logs for the Endpoint to ensure normal operation of the Deepgram services.

## Inference

Once your endpoint is deployed and in service, you invoke it to transcribe audio. The endpoint supports three invocation modes, depending on which endpoint type you deployed and how you need the response returned.

| Mode             | API                                     | Endpoint type | Input limit            | Response                              |
| ---------------- | --------------------------------------- | ------------- | ---------------------- | ------------------------------------- |
| **Streaming**    | `InvokeEndpointWithBidirectionalStream` | Real-time     | 30 min per connection  | Results streamed back live            |
| **Synchronous**  | `InvokeEndpoint`                        | Real-time     | 25 MB per request body | One immediate response                |
| **Asynchronous** | `InvokeEndpointAsync`                   | Asynchronous  | 1 GB per S3 object     | Written to Amazon S3 (near real-time) |

**Not sure which endpoint type you need?** See [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker) for a full comparison of real-time and asynchronous endpoints and guidance on choosing between them.

**Passing Deepgram parameters.** For synchronous and asynchronous invocations, the Deepgram model and feature parameters are passed in the `CustomAttributes` field (the `X-Amzn-SageMaker-Custom-Attributes` header) as `v1/listen?model=...&language=...`. For streaming, the same values are split across `ModelInvocationPath` (`v1/listen`) and `ModelQueryString`. In all cases an API path such as `v1/listen` is required — without it the container returns a 404. The examples on this page use `v1/listen` (speech-to-text), but other routes are available (for example, `v1/speak` for text-to-speech).

Complete, runnable examples for all three modes — in Python, TypeScript, and Java — are maintained in the [deepgram-devs/dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) repository. The sections below explain each mode and link to the corresponding example. See the repository's `README` for setup and prerequisites.

### Use the Deepgram SDKs with the SageMaker transport

You don't have to call the AWS APIs directly. The [Deepgram SDKs](https://developers.deepgram.com/home) can target a SageMaker endpoint through a **SageMaker transport**, so you keep the same client-side request and response patterns whether you call the Deepgram-hosted API or your own SageMaker deployment. You swap the transport; your `listen` request and result-handling code stays the same.

For example, the Deepgram Java SDK pairs with the [Deepgram SageMaker transport](https://github.com/deepgram/deepgram-java-sdk-transport-sagemaker) (`com.deepgram:deepgram-sagemaker`):

```java
import com.deepgram.DeepgramClient;
import com.deepgram.sagemaker.SageMakerConfig;
import com.deepgram.sagemaker.SageMakerTransportFactory;
import com.deepgram.resources.listen.v1.websocket.V1WebSocketClient;

SageMakerConfig smConfig = SageMakerConfig.builder()
        .endpointName("<your-endpoint-name>")
        .region("us-east-2")
        .build();

DeepgramClient client = DeepgramClient.builder()
        .apiKey("unused") // auth is AWS SigV4 via the transport, not a Deepgram API key
        .transportFactory(new SageMakerTransportFactory(smConfig))
        .build();

// Same SDK surface as the Deepgram-hosted API:
V1WebSocketClient ws = client.listen().v1().v1WebSocket();
ws.onResults(r -> { /* handle transcript */ });
ws.connect(connectOptions).get();
ws.sendMedia(ByteString.of(audioChunk));
// ... send a CloseStream message when finished
```

The remaining sections show the underlying AWS APIs directly, which apply to any language.

### Streaming (real-time)

Use streaming for live, interactive transcription over a persistent bidirectional connection. You send audio chunks and receive transcription results as the audio is processed, up to 30 minutes per connection.

Streaming uses the HTTP/2 bidirectional streaming client (`@aws-sdk/client-sagemaker-runtime-http2` in TypeScript, `aws_sdk_sagemaker_runtime_http2` in Python) against the SageMaker bidirectional runtime endpoint (`https://runtime.sagemaker.<region>.amazonaws.com:8443`). The request `Body` is an async iterable of payload parts:

* **Binary audio** is sent as a `Bytes` payload with `DataType: "BINARY"`.
* **Control messages** (for example, `KeepAlive` and `CloseStream`) are sent as UTF-8 encoded JSON with `DataType: "UTF8"`.

```typescript
import {
  SageMakerRuntimeHTTP2Client,
  InvokeEndpointWithBidirectionalStreamCommand,
} from "@aws-sdk/client-sagemaker-runtime-http2";

const region = "us-east-2";
const client = new SageMakerRuntimeHTTP2Client({
  region,
  endpoint: `https://runtime.sagemaker.${region}.amazonaws.com:8443`,
});

// Async generator yielding audio chunks (BINARY) and control messages (UTF8)
async function* requestStream() {
  // yield { PayloadPart: { Bytes: audioChunk, DataType: "BINARY" } };
  // yield { PayloadPart: { Bytes: new TextEncoder().encode(
  //           JSON.stringify({ type: "CloseStream" })), DataType: "UTF8" } };
}

const command = new InvokeEndpointWithBidirectionalStreamCommand({
  EndpointName: "<your-endpoint-name>",
  ModelInvocationPath: "v1/listen",
  ModelQueryString: "model=nova-3&language=en&smart_format=true",
  Body: requestStream(),
});

const response = await client.send(command);

for await (const event of response.Body) {
  if (event.PayloadPart?.Bytes) {
    const message = new TextDecoder().decode(event.PayloadPart.Bytes);
    // message is a Deepgram JSON transcript result
  }
}
```

For the complete examples — file and microphone capture, payload wrapping, keepalive handling, and stream processing — see:

* TypeScript: [`js-stt/stt.file.ts`](https://github.com/deepgram-devs/dg-sagemaker/blob/main/js-stt/stt.file.ts) and [`stt.microphone.ts`](https://github.com/deepgram-devs/dg-sagemaker/blob/main/js-stt/stt.microphone.ts)
* Python: [`python-stt/stt_wav_stress.py`](https://github.com/deepgram-devs/dg-sagemaker/blob/main/python-stt/stt_wav_stress.py) (`stream` subcommand)

### Synchronous (real-time)

Use synchronous invocation to transcribe a single pre-recorded file and receive the full transcript in one immediate response. This is Deepgram's "batch" transcription on a real-time endpoint — there is no streaming connection and no queue. The request body is capped at 25 MB; use streaming or asynchronous invocation for larger audio.

You send the audio as the request body to `InvokeEndpoint`, pass the Deepgram parameters via `CustomAttributes`, and parse the transcript from the JSON response.

```python
import json
import boto3

runtime = boto3.client("sagemaker-runtime", region_name="us-east-2")

with open("audio.wav", "rb") as f:
    response = runtime.invoke_endpoint(
        EndpointName="<your-endpoint-name>",
        ContentType="audio/wav",
        Accept="application/json",
        CustomAttributes="v1/listen?model=nova-3&language=en&punctuate=true",
        Body=f.read(),
    )

result = json.loads(response["Body"].read())
transcript = result["results"]["channels"][0]["alternatives"][0]["transcript"]
```

For the complete example, see [`python-stt/stt_wav_stress.py`](https://github.com/deepgram-devs/dg-sagemaker/blob/main/python-stt/stt_wav_stress.py) (`batch` subcommand) in the repository.

### Asynchronous

Use asynchronous invocation for large or long-form pre-recorded files — up to 1 GB, with up to one hour of processing time. Requests are queued and processed with near real-time latency, and the result is written back to Amazon S3.

The flow is:

1. Upload the audio file to an S3 bucket.
2. Call `InvokeEndpointAsync` with `InputLocation` pointing to the uploaded file and the Deepgram parameters in `CustomAttributes`.
3. SageMaker immediately returns an `OutputLocation` and a `FailureLocation` in S3, and processes the request from the queue.
4. Poll the `OutputLocation` (success) and `FailureLocation` (error) prefixes until one appears, then download and parse the result — or react to an Amazon SNS notification, if configured.

```python
import boto3

runtime = boto3.client("sagemaker-runtime", region_name="us-east-2")

response = runtime.invoke_endpoint_async(
    EndpointName="<your-async-endpoint-name>",
    InputLocation="s3://<your-bucket>/input/audio.wav",
    ContentType="audio/wav",
    Accept="application/json",
    CustomAttributes="v1/listen?model=nova-3&language=en",
    InvocationTimeoutSeconds=3600,
)

output_location = response["OutputLocation"]    # S3 URI for the transcript on success
failure_location = response["FailureLocation"]  # S3 URI for error details on failure
```

Asynchronous invocation requires an endpoint deployed with **Async invocation config** enabled (with an S3 output path), as described in the deployment steps above. To autoscale an asynchronous endpoint — including scaling to zero when idle — see [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async).

For the complete example — S3 upload, invocation, and polling for results — see [`python-stt/stt_wav_async.py`](https://github.com/deepgram-devs/dg-sagemaker/blob/main/python-stt/stt_wav_async.py) in the repository.

## Troubleshooting

If you're experiencing any issues with your Deepgram deployment on Amazon SageMaker AI, you can obtain the Deepgram container logs from the Amazon CloudWatch service.
If you open the SageMaker AI Endpoint resource details, there will be a link to open the Amazon CloudWatch Log Group for that endpoint.
Within the CloudWatch Log Group, there should be a Log Stream that contains the Deepgram logs for all components.
You can use the Amazon CloudWatch Logs [Live Tail feature](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) to watch logs in near-real-time
while you are sending requests to the Deepgram API, via the SageMaker AI APIs.

To use the CloudWatch Logs Live Tail feature locally, from the [AWS CLI tool](https://aws.amazon.com/cli/), you can use the following command.

```
aws logs tail --follow /aws/sagemaker/Endpoints/YOUR_SAGEMAKER_ENDPOINT_NAME --region YOUR_AWS_REGION
```

### Checklist

If you experience any issues using Deepgram services running on the Amazon SageMaker AI platform, please review this checklist before contacting Deepgram support.

* Ensure that your application's AWS IAM User or IAM Role has permission to call the `InvokeEndpointWithBidirectionalStream` SageMaker AI action.
* Ensure your application is targeting the correct AWS account and region, where your SageMaker Endpoint exists.
* Ensure the Deepgram product you've deployed (eg. streaming Speech-to-Text), from the AWS Marketplace, corresponds to the Deepgram API you're calling.
* There is a known compatibility issue using pre-Blackwell NVIDIA GPUs with the latest [SageMaker-provided AMI](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) named `al2023-ami-sagemaker-inference-gpu-4-1` which includes the NVIDIA 580 driver version. When creating your SageMaker Endpoint Configuration resource, using a g4dn, g5, g6, or g6e instance family, please be sure that you are using one of the AMIs before this version. You can also reference [this AWS supported configurations table](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-gpu-drivers.html#inference-gpu-drivers-versions).
* If you have received a SageMaker private offer for a management account of an AWS organization, you may use [AWS License Manager](https://aws.amazon.com/blogs/awsmarketplace/manage-your-aws-marketplace-license-entitlements-in-aws-license-manager/) to grant usage of the SageMaker private offer to member accounts within your AWS organization as a Marketplace license entitlement.
