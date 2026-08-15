---
title: "Deploying Flux TTS"
source: https://developers.deepgram.com/docs/deploy-flux-tts.md
path: docs/deploy-flux-tts
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deploying Flux TTS

Flux TTS is an Early Access feature in self-hosted deployments, released in [self-hosted release 260812](/changelog). Its configuration surface and its voice set may both change before general availability. Contact your Deepgram Account Representative before you size or deploy Flux TTS in a production self-hosted environment.

Flux TTS is generally available in Deepgram's hosted API.

## Requirements

Please familiarize yourself with these general requirements before attempting to deploy Flux TTS to your self-hosted Deepgram instances.

* Flux TTS runs on the NVIDIA L4, L40S, A100, and H100 GPUs. The NVIDIA T4 and A10 are not supported. See [Model and GPU Compatibility](/docs/self-hosted-deployment-environments#model-and-gpu-compatibility) for how this compares to Deepgram's other models.
* Each host running a Flux TTS Engine needs at least 64 GB of system RAM. See [Memory Requirements](#memory-requirements) below.
* Flux TTS requires Deepgram container images from `release-260812` or later. It runs on both the standard and the FIPS-compliant images. On FIPS images, MP3 and FLAC output are a known issue: set `encoding` explicitly on batch `/v2/speak` requests, which return MP3 by default. Streaming output is unaffected. See [MP3 and FLAC Output](/docs/fips-compliant-deployment#mp3-and-flac-output).
* Flux TTS must be enabled explicitly in your Engine configuration file. It is off by default.
* Flux TTS requires a dedicated Engine. It cannot share an Engine with Aura models.
* The Flux TTS model file must be present in your Engine `models` directory. Request it from your Deepgram account representative.
* Your API configuration must enable the `/v2/speak` endpoint.

## Memory Requirements

A Flux TTS Engine needs considerably more system RAM than an Aura Engine. While it loads the Flux TTS model at startup, the Engine container allocates up to 60 GB of system RAM. Once the model is loaded, steady-state usage is much lower.

Provision at least 64 GB of system RAM on every host running a Flux TTS Engine. On AWS, the `g6.4xlarge` instance type (one L4 GPU, 64 GB RAM) meets this requirement.

Size the host against the 60 GB startup peak, not against steady-state usage. An Engine that cannot allocate this memory at startup will fail to load the model and exit.

This requirement applies to system RAM, not GPU memory.

## Enable Flux TTS in Deepgram Self-Hosted Deployment

Flux TTS requires a couple of configuration changes in your self-hosted Deepgram deployment.

### Engine

In your Deepgram Engine configuration, enable Flux TTS and select the model. Both `uuid` and `max_batch_size` are required when `enabled = true`.

```toml Deepgram Engine Configuration
[flux_tts]
enabled = true
uuid = "<model UUID provided by Deepgram>"
max_batch_size = 0 # Placeholder; not a working value. See the warning below.
```

`max_batch_size` has no safe default. The correct value differs substantially between GPUs, and a value tuned for one will underperform or exhaust memory on another. Engine will not start until you set it to a non-zero value. Contact your Deepgram account representative for a recommended value for the GPUs in your deployment.

### API

In your Deepgram API configuration, make sure that the `/v2/speak` endpoint is enabled. This endpoint is new for Flux TTS. Aura and Aura-2 are served via the `/v1/speak` endpoint.

```toml Deepgram API Configuration
[features]
speak_v2 = true
speak_v2_streaming = true
```

`speak_v2` exposes the batch REST transport, and `speak_v2_streaming` exposes the WebSocket transport.

### Helm

The Helm chart exposes `fluxTts.enabled`, `fluxTts.uuid`, and `fluxTts.maxBatchSize` for the Engine side, and `api.features.speakV2` and `api.features.speakV2Streaming` for the API side. Helm users do not edit the Engine configuration file directly; the chart renders it for them. See `charts/deepgram-self-hosted/samples/08-flux-tts-setup.values.yaml` in the [self-hosted-resources repository](https://github.com/deepgram/self-hosted-resources) for a complete example.

## Deployment Constraints

Flux TTS requires a dedicated Engine. Deploy it separately from Aura, and from your speech-to-text models, which contend for the same GPU memory.

Flux TTS and Aura cannot run on the same Engine. Engine refuses to start if both are configured, exiting before it loads any model. To serve both, run separate Engine instances.

Flux TTS synthesis workers bind to a single GPU. Exposing additional GPUs to a Flux TTS Engine does not increase its capacity. To use more GPUs, run one Engine per GPU.

## Making a Test Request

Once your containers are running, make a sample request to verify that Flux TTS is loaded and serving. Flux TTS model strings use the format `flux-{voice}-{language}`, for example `flux-haley-en`. See [Flux TTS Voices & Languages](/docs/flux-tts/voices) for the full catalog.

Unless you have HTTPS/TLS configured, use the `http://` and `ws://` protocols. Both `/v2/speak` transports are available on the same API port.

### Batch (REST)

```shell Shell
curl --request POST \
   --header "Content-Type: application/json" \
   --output flux-tts-test.mp3 \
   --data '{"text":"This is a Flux TTS self-hosted test."}' \
   --url "http://localhost:8080/v2/speak?model=flux-haley-en"
```

You should receive a response with the audio output. You can copy this file locally to manually evaluate the synthesized speech.

### Streaming (WebSocket)

```shell Shell
# Connect with wscat for testing.
wscat -c "ws://localhost:8080/v2/speak?model=flux-haley-en"

# Then send text frames, e.g.
# {"type": "Speak", "text": "This is a Flux TTS self-hosted test."}
# {"type": "Flush"}
```

Each turn follows a clean lifecycle: `SpeechStarted` → audio → `SpeechMetadata`. Congratulations - your self-hosted Flux TTS setup is working!

## What's Next

Flux TTS behaves the same way in a self-hosted deployment as it does on Deepgram's hosted platform. To learn about the API surface, voices, and transports, see:

* [Flux TTS Overview](/docs/flux-tts/overview)
* [Client Messages](/docs/flux-tts/client-messages)
* [Server Messages](/docs/flux-tts/server-messages)
* [Voices & Languages](/docs/flux-tts/voices)
* [Batch vs Streaming](/docs/flux-tts/batch-vs-streaming)
