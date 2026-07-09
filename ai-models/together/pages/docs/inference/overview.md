---
title: "Overview"
source: https://docs.together.ai/docs/inference/overview
path: docs/inference/overview
---

Run inference on 100+ open-source models.

Together AI offers three ways to run inference:

**[Serverless models](/docs/serverless/models):** A shared fleet of popular open models you can call through a per-token API. No GPUs to provision or manage. Best for prototyping, or apps with variable traffic.

**[Provisioned throughput](/docs/inference/provisioned-throughput):** Reserved capacity for a selected stock model with a defined SLA covering committed throughput and reliability. Best for production workloads that need stronger guarantees than serverless.

**[Dedicated endpoints](/docs/dedicated-endpoints/overview):** A single model running on GPUs reserved for you, billed per minute by hardware. Best for serving fine-tuned models, or workloads that need direct control over hardware, latency, and throughput.

## Get started

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/quickstart">
    Set up an API key and make your first call in Python, TypeScript, or cURL.
  </Card>

  <Card title="Recommended models" icon="list" href="/docs/inference/recommended-models">
    Our picks for common inference use cases.
  </Card>

  <Card title="Pricing" icon="credit-card" href="/docs/inference/pricing">
    How Together AI bills for inference.
  </Card>
</CardGroup>

## Shared inference API

Serverless, provisioned throughput, and dedicated endpoint workloads all use the same inference APIs for generating and retrieving model outputs. Apps work on any deployment mode without code changes; just swap the `model` parameter:

<CodeGroup>
  ```python Python highlight={7,13} theme={null}
  from together import Together

  client = Together()

  # Serverless model request
  response = client.chat.completions.create(
      model="moonshotai/Kimi-K2.6",
      messages=[{"role": "user", "content": "Hello!"}],
  )

  # Dedicated endpoint request
  response = client.chat.completions.create(
      model="<ACCOUNT_NAME>/Qwen/Qwen3.5-9B-FP8-bb04c904",
      messages=[{"role": "user", "content": "Hello!"}],
  )
  ```

  ```typescript TypeScript highlight={6,12} theme={null}
  import Together from "together-ai";
  const client = new Together();

  // Serverless model request
  let response = await client.chat.completions.create({
      model: "moonshotai/Kimi-K2.6",
      messages: [{ role: "user", content: "Hello!" }],
  });

  // Dedicated endpoint request
  response = await client.chat.completions.create({
      model: "<ACCOUNT_NAME>/Qwen/Qwen3.5-9B-FP8-bb04c904",
      messages: [{ role: "user", content: "Hello!" }],
  });
  ```

  ```bash cURL highlight={6,15} theme={null}
  # Serverless model request
  curl -X POST "https://api.together.ai/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
            "model": "moonshotai/Kimi-K2.6",
            "messages": [{"role": "user", "content": "Hello!"}]
          }'

  # Dedicated endpoint request
  curl -X POST "https://api.together.ai/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
            "model": "<ACCOUNT_NAME>/Qwen/Qwen3.5-9B-FP8-bb04c904",
            "messages": [{"role": "user", "content": "Hello!"}]
          }'
  ```
</CodeGroup>

## Integrations

<CardGroup>
  <Card title="OpenAI compatibility" icon="plug" href="/docs/inference/openai-compatibility">
    Drop-in replacement for OpenAI clients.
  </Card>

  <Card title="SDK integrations" icon="code" href="/docs/inference/sdk-integrations">
    Together SDKs and framework wiring.
  </Card>
</CardGroup>

## Batch processing

<Card title="Batch processing" icon="hourglass-high" href="/docs/inference/batch/overview">
  If your workload doesn't need a real-time response, submit it as a batch job for up to 50% off serverless rates.
</Card>

## Model capabilities

<CardGroup>
  <Card title="Chat & text" icon="message-circle" href="/docs/inference/chat/overview">
    Chat completions, streaming, parameters.
  </Card>

  <Card title="Function calling" icon="tool" href="/docs/inference/function-calling/overview">
    Tool use and agentic loops.
  </Card>

  <Card title="Vision" icon="eye" href="/docs/inference/vision/overview">
    Pass images alongside text.
  </Card>

  <Card title="Image generation" icon="photo" href="/docs/inference/images/overview">
    FLUX, Kontext, and Google models.
  </Card>

  <Card title="Video generation" icon="movie" href="/docs/inference/videos/overview">
    Text-to-video and image-to-video.
  </Card>

  <Card title="Speech-to-text" icon="microphone" href="/docs/inference/transcription/overview">
    Batch and streaming transcription.
  </Card>

  <Card title="Text-to-speech" icon="volume" href="/docs/inference/text-to-speech/overview">
    HTTP and WebSocket audio output.
  </Card>

  <Card title="Embeddings & rerank" icon="vector-bezier-2" href="/docs/inference/embeddings/embeddings">
    Vectors, rerankers, and RAG.
  </Card>
</CardGroup>
