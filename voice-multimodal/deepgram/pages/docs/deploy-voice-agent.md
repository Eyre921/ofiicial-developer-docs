---
title: "Deploy Voice Agent"
source: https://developers.deepgram.com/docs/deploy-voice-agent.md
path: docs/deploy-voice-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deploy Voice Agent

> Deploy Deepgram's Voice Agent API for self-hosted conversational AI with real-time speech-to-speech interactions

This guide covers deploying Deepgram's Voice Agent API in a self-hosted Kubernetes environment using the Deepgram Helm chart. The Voice Agent API orchestrates Speech-to-Text (STT), a Large Language Model (LLM), and Text-to-Speech (TTS) into a single WebSocket-based conversational pipeline.

The Voice Agent API is served by the same `self-hosted-api` container used for STT and TTS. The `/v1/agent/converse` WebSocket endpoint becomes available when STT and TTS Engine services are running alongside the API.

## Prerequisites

### 1. Get Configuration Files

Voice Agent configuration files are available in the [self-hosted-resources repository](https://github.com/deepgram/self-hosted-resources/tree/main/charts/deepgram-self-hosted/samples).

Two files are provided for AWS deployments:

* `05-voice-agent-aws.cluster-config.yaml` — EKS cluster configuration with dedicated node groups for API, Engine (GPU), and License Proxy workloads.
* `05-voice-agent-aws.values.yaml` — Helm values file with Voice Agent enabled, including STT, TTS, and end-of-turn Engine replicas.

```shell Shell
BASE_URL="https://raw.githubusercontent.com/deepgram/self-hosted-resources/refs/heads/main"
curl -sSL "$BASE_URL/charts/deepgram-self-hosted/samples/05-voice-agent-aws.cluster-config.yaml" -o cluster-config.yaml
curl -sSL "$BASE_URL/charts/deepgram-self-hosted/samples/05-voice-agent-aws.values.yaml" -o values.yaml
```

### 2. Get Deepgram Models

Obtain your Voice Agent model links from your Deepgram Account Representative. The recommended models for Voice Agent deployments include:

#### STT

* If using Flux:
  * **Flux** model (e.g. `flux-general-en.*.dg`)
* If using Nova-3:
  * **Nova-3** model (e.g. `nova-3-general.en.streaming.*.dg`)
  * **End-of-turn** model (e.g. `end-of-turn.*.dg`)

#### TTS

* If using Aura-2:
  * **Voice** model (e.g., `aura-2.voice-pack.en.*.dg`)
  * **Generator** model (e.g., `aura-2.generator.en.*.dg`)
* If using Aura-1:
  * **Voice** model (e.g. `aura-asteria-en.*.dg`)
  * **Phonemizer** (e.g. `phonemizer.en.*.dg`)

### 3. Deploy Kubernetes Cluster

You need a running Kubernetes cluster with GPU-enabled nodes. Choose a platform option based on your infrastructure and follow the corresponding setup guide:

* [Amazon Web Services (EKS)](/docs/aws-k8s)
* [Google Cloud Platform (GKE)](/docs/gcp-k8s)
* [Self-Managed Kubernetes](/docs/self-managed-kubernetes)

The Voice Agent sample configuration (`05-voice-agent-aws`) provisions dedicated node groups for API, Engine, and License Proxy workloads. If you are starting from an existing cluster, ensure your node groups have the appropriate labels and GPU resources.

### Verify the Deployment

Check that all pods are running:

```shell Shell
kubectl get pods
# Confirm that api, engine (STT, TTS, EOT), and license-proxy pods are Running
kubectl logs <POD_NAME>
```

## Testing Your Deployment

To make sure your Deepgram self-hosted Voice Agent deployment is properly configured and running, you will want to verify the services and make sample requests.

### Port-Forward the API Service

Forward the API service to test locally:

```shell Shell
kubectl port-forward svc/deepgram-api 8080:8080
```

### Networking Considerations

Unless you have HTTPS or TLS running on your API instance, construct your Deepgram API endpoint with `http://`, not `https://`, and `ws://`, not `wss://` (for instance, `ws://localhost:8080/v1/agent/converse`).

### Test STT

Test the Speech-to-Text service with a sample audio file.

1. Download a sample file from Deepgram (or supply your own file).
   ```shell Shell
   wget https://dpgr.am/bueller.wav
   ```
2. Send your audio file to your local Deepgram setup for transcription.
   ```shell Shell
   curl -X POST --data-binary @bueller.wav "http://localhost:8080/v1/listen?model=nova-3"
   ```

If you're using your own file, make sure to replace `bueller.wav` with the name of your audio file.

You should receive a JSON response with the transcription and associated metadata.

### Test TTS

Test the Text-to-Speech service with a sample speak request.

```shell Shell
curl --request POST \
   --header "Content-Type: application/json" \
   --output tts-test.wav \
   --data '{"text":"This is a TTS self-hosted test."}' \
   --url "http://localhost:8080/v1/speak?model=aura-2-thalia-en"
```

You should receive a response with the audio output. You can play the file locally to evaluate the synthesized speech.

### Initializing the Voice Agent

The [Voice Agent Getting Started](/docs/voice-agent) guide walks through building a voice agent with Deepgram's hosted API. For self-hosted deployments, the only difference is how you initialize the `DeepgramClient` — you point it at your self-hosted endpoint instead of the default `api.deepgram.com`.

**Hosted (default):**

```python Python
api_key = os.getenv("DEEPGRAM_API_KEY")
client = DeepgramClient(api_key=api_key)

with client.agent.v1.connect() as connection:
    print("Created WebSocket connection...")
```

```javascript JavaScript
const deepgram = new DeepgramClient({ apiKey: process.env.DEEPGRAM_API_KEY });
const connection = await deepgram.agent.v1.connect();
```

```java Java
DeepgramClient client = DeepgramClient.builder()
    .apiKey(System.getenv("DEEPGRAM_API_KEY"))
    .build();
```

**Self-hosted** — set the `baseUrl` to your port-forwarded or load-balanced endpoint:

```python Python
import os

from deepgram import DeepgramClient
from deepgram.environment import DeepgramClientEnvironment

self_hosted_env = DeepgramClientEnvironment(
    base="http://localhost:8080",
    production="ws://localhost:8080",
    agent="ws://localhost:8080",
    agent_rest="http://localhost:8080"  # requires Python SDK v7.2.0+
)

api_key = os.getenv("DEEPGRAM_API_KEY")

client = DeepgramClient(
    api_key=api_key,
    environment=self_hosted_env
)

with client.agent.v1.connect() as connection:
    print("Created WebSocket connection...")
```

```javascript JavaScript
const deepgram = new DeepgramClient({
  apiKey: process.env.DEEPGRAM_API_KEY,
  baseUrl: "http://localhost:8080",
});

const connection = await deepgram.agent.v1.connect();
```

```java Java
Environment selfHostedEnv = Environment.custom()
    .base("http://localhost:8080")
    .agent("ws://localhost:8080")
    .production("ws://localhost:8080")
    .build();

DeepgramClient client = DeepgramClient.builder()
    .apiKey(System.getenv("DEEPGRAM_API_KEY"))
    .environment(selfHostedEnv)
    .build();
```

Once connected, follow the same steps as the [Voice Agent Getting Started](/docs/voice-agent) guide to configure and interact with your agent. For additional SDK configuration details, see [Using SDKs with Self-Hosted](/docs/using-sdks-with-self-hosted).

***

What's Next

Now that you have a Voice Agent deployment working, explore advanced configuration and integration options:

* [Configure the Voice Agent](/docs/configure-voice-agent)
* [Voice Agent Feature Overview](/docs/voice-agent-feature-overview)
* [Using SDKs with Self-Hosted](/docs/using-sdks-with-self-hosted)
* [Self-Hosted Add Ons](/docs/self-hosted-add-ons)
