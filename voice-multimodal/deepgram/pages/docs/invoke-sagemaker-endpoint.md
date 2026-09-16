---
title: "Invoke a Deepgram SageMaker Endpoint"
source: https://developers.deepgram.com/docs/invoke-sagemaker-endpoint.md
path: docs/invoke-sagemaker-endpoint
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Invoke a Deepgram SageMaker Endpoint

Once your endpoint is deployed and in service, you invoke it to transcribe audio. A real-time endpoint supports two invocation modes, depending on how you need the response returned.

| Mode             | API                                     | Endpoint type | Input limit            | Response                                                                                                                       |
| ---------------- | --------------------------------------- | ------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Streaming**    | `InvokeEndpointWithBidirectionalStream` | Real-time     | 30 min per connection  | Results streamed back live                                                                                                     |
| **Synchronous**  | `InvokeEndpoint`                        | Real-time     | 25 MB per request body | One immediate response                                                                                                         |
| **Asynchronous** | `InvokeEndpointAsync`                   | Asynchronous  | —                      | Temporarily unsupported for Marketplace-hosted Deepgram. Contact a [Deepgram representative](https://deepgram.com/contact-us). |

**Passing Deepgram parameters.** For synchronous invocations, the Deepgram model and feature parameters are passed in the `CustomAttributes` field (the `X-Amzn-SageMaker-Custom-Attributes` header) as `v1/listen?model=...&language=...`. For streaming, the same values are split across `ModelInvocationPath` (`v1/listen`) and `ModelQueryString`. In all cases an API path such as `v1/listen` is required — without it the container returns a 404. The examples on this page use `v1/listen` (speech-to-text), but other routes are available (for example, `v1/speak` for text-to-speech).

Complete, runnable examples for both modes — in Python, TypeScript, and Java — are maintained in the [deepgram-devs/dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) repository. The sections below explain each mode and link to the corresponding example. See the repository's `README` for setup and prerequisites.

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

Streaming uses the HTTP/2 bidirectional streaming client (`@aws-sdk/client-sagemaker-runtime-http2` in TypeScript, `aws-sdk-sagemaker-runtime-http2` in Python) against the SageMaker bidirectional runtime endpoint (`https://runtime.sagemaker.<region>.amazonaws.com:8443`). The request `Body` is an async iterable of payload parts:

* **Binary audio** is sent as a `Bytes` payload with `DataType: "BINARY"`.
* **Control messages** (for example, `KeepAlive` and `CloseStream`) are sent as UTF-8 encoded JSON with `DataType: "UTF8"`.

**Always include `:8443` in the endpoint URL.** The bidirectional streaming runtime listens on port 8443, not 443. A streaming client that hangs with no error and never receives a response is almost always pointed at the endpoint without `:8443`.

#### Python

Requires `aws-sdk-sagemaker-runtime-http2` 0.11 or later with the `awscrt` extra (`pip install "aws-sdk-sagemaker-runtime-http2[awscrt]>=0.11"`). The client takes explicit credentials and an AWS CRT transport; payload events are typed.

```python
import asyncio
import json

import boto3
from aws_sdk_sagemaker_runtime_http2.client import AsyncSageMakerRuntimeHTTP2Client
from aws_sdk_sagemaker_runtime_http2.config import AsyncSageMakerRuntimeHTTP2Config
from aws_sdk_sagemaker_runtime_http2.models import (
    InvokeEndpointWithBidirectionalStreamInput,
    RequestPayloadPart,
    RequestStreamEventPayloadPart,
    ResponseStreamEventPayloadPart,
)
from smithy_http.aio.crt import AWSCRTHTTPClient

REGION = "us-east-2"


async def main():
    creds = boto3.Session().get_credentials().get_frozen_credentials()
    client = AsyncSageMakerRuntimeHTTP2Client(
        config=AsyncSageMakerRuntimeHTTP2Config(
            region=REGION,
            endpoint_uri=f"https://runtime.sagemaker.{REGION}.amazonaws.com:8443",
            aws_access_key_id=creds.access_key,
            aws_secret_access_key=creds.secret_key,
            aws_session_token=creds.token,
            transport=AWSCRTHTTPClient(),
        )
    )

    stream = await client.invoke_endpoint_with_bidirectional_stream(
        InvokeEndpointWithBidirectionalStreamInput(
            endpoint_name="<your-endpoint-name>",
            model_invocation_path="v1/listen",
            model_query_string="model=nova-3&language=en&encoding=linear16&sample_rate=16000",
        )
    )
    _, output = await stream.await_output()

    async def send(data: bytes, data_type: str):  # audio: "BINARY"; JSON control: "UTF8"
        await stream.input_stream.send(
            RequestStreamEventPayloadPart(
                value=RequestPayloadPart(bytes_=data, data_type=data_type)
            )
        )

    async def send_audio():
        with open("audio.raw", "rb") as f:
            while chunk := f.read(3200):  # 100 ms of 16 kHz linear16 audio
                await send(chunk, "BINARY")
                await asyncio.sleep(0.1)
        await send(json.dumps({"type": "CloseStream"}).encode(), "UTF8")

    async def receive_results():
        while (event := await output.receive()) is not None:
            if isinstance(event, ResponseStreamEventPayloadPart):
                print(event.value.bytes_.decode())  # Deepgram JSON transcript result
            else:  # ModelStreamError / InternalStreamFailure
                print("stream error:", event.value)

    await asyncio.gather(send_audio(), receive_results())
    await client.close()


asyncio.run(main())
```

#### TypeScript

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

Use synchronous invocation to transcribe a single pre-recorded file and receive the full transcript in one immediate response. This is Deepgram's "batch" transcription on a real-time endpoint — there is no streaming connection and no queue. The request body is capped at 25 MB; use streaming for larger audio.

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

Asynchronous invocation (`InvokeEndpointAsync`, files up to 1 GB) is temporarily not supported for Marketplace-hosted Deepgram. If your use case needs it, contact a [Deepgram representative](https://deepgram.com/contact-us).

## Related resources

* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Troubleshooting](/docs/troubleshooting-sagemaker)
* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker)
* [deepgram-devs/dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) example repository
