---
title: "Invoke a Deepgram SageMaker Endpoint"
source: https://developers.deepgram.com/docs/invoke-sagemaker-endpoint.md
path: docs/invoke-sagemaker-endpoint
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Invoke a Deepgram SageMaker Endpoint

Once your endpoint is deployed and in service, you invoke it to transcribe audio. The endpoint supports three invocation modes, depending on which endpoint type you deployed and how you need the response returned.

| Mode             | API                                     | Endpoint type | Input limit            | Response                              |
| ---------------- | --------------------------------------- | ------------- | ---------------------- | ------------------------------------- |
| **Streaming**    | `InvokeEndpointWithBidirectionalStream` | Real-time     | 30 min per connection  | Results streamed back live            |
| **Synchronous**  | `InvokeEndpoint`                        | Real-time     | 25 MB per request body | One immediate response                |
| **Asynchronous** | `InvokeEndpointAsync`                   | Asynchronous  | 1 GB per S3 object     | Written to Amazon S3 (near real-time) |

**Not sure which endpoint type you need?** See [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker) for a full comparison of real-time and asynchronous endpoints and guidance on choosing between them.

**Passing Deepgram parameters.** For synchronous and asynchronous invocations, the Deepgram model and feature parameters are passed in the `CustomAttributes` field (the `X-Amzn-SageMaker-Custom-Attributes` header) as `v1/listen?model=...&language=...`. For streaming, the same values are split across `ModelInvocationPath` (`v1/listen`) and `ModelQueryString`. In all cases an API path such as `v1/listen` is required — without it the container returns a 404. The examples on this page use `v1/listen` (speech-to-text), but other routes are available (for example, `v1/speak` for text-to-speech).

Complete, runnable examples for all three modes — in Python, TypeScript, and Java — are maintained in the [deepgram-devs/dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) repository. The sections below explain each mode and link to the corresponding example. See the repository's `README` for setup and prerequisites.

## Use the Deepgram SDKs with the SageMaker transport

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

## Streaming (real-time)

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

## Synchronous (real-time)

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

## Asynchronous

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

Asynchronous invocation requires an endpoint deployed with **Async invocation config** enabled (with an S3 output path), as described in [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker#deploy-with-the-aws-cli-or-boto3). To autoscale an asynchronous endpoint — including scaling to zero when idle — see [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async).

For the complete example — S3 upload, invocation, and polling for results — see [`python-stt/stt_wav_async.py`](https://github.com/deepgram-devs/dg-sagemaker/blob/main/python-stt/stt_wav_async.py) in the repository.

## Related resources

* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Troubleshooting](/docs/troubleshooting-sagemaker)
* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker)
* [deepgram-devs/dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) example repository
