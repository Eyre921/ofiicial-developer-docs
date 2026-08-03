---
title: "Recommended models"
source: https://docs.together.ai/docs/inference/recommended-models
path: docs/inference/recommended-models
---

Our picks for common inference use cases.

Together hosts 100+ open-source models across text, image, video, and audio.

Most of the models below are for instant [serverless inference](/docs/serverless/models), or reserved hardware deployments with [dedicated model inference](/docs/dedicated-endpoints/models). Both options use the same [inference API](/docs/inference/overview).

## Chat & text

| Use case                     | Recommended model          | Model string                | Alternatives                              | Learn more                                                    |
| :--------------------------- | :------------------------- | :-------------------------- | :---------------------------------------- | :------------------------------------------------------------ |
| **Chat**                     | Kimi K2.6 (instant mode)   | `moonshotai/Kimi-K2.6`      | `MiniMaxAI/MiniMax-M3`                    | [Chat completions](/docs/inference/chat/overview)             |
| **Reasoning**                | Kimi K2.6 (reasoning mode) | `moonshotai/Kimi-K2.6`      | `zai-org/GLM-5.2`                         | [Reasoning](/docs/inference/chat/reasoning)                   |
| **Coding agents**            | Kimi K2.7 Code             | `moonshotai/Kimi-K2.7-Code` | `zai-org/GLM-5.2`                         | [Build coding agents](/docs/how-to-build-coding-agents)       |
| **Small and fast**           | Gemma 4 31B IT             | `google/gemma-4-31B-it`     | `openai/gpt-oss-20b`, `Qwen/Qwen3.5-9B`   | -                                                             |
| **Mid-size general purpose** | MiniMax M3                 | `MiniMaxAI/MiniMax-M3`      | `meta-llama/Llama-3.3-70B-Instruct-Turbo` | -                                                             |
| **Function calling**         | GLM-5.2                    | `zai-org/GLM-5.2`           | `moonshotai/Kimi-K2.6`                    | [Function calling](/docs/inference/function-calling/overview) |

## Vision

| Use case   | Recommended model | Model string           | Alternatives                                    | Learn more                                                                                  |
| :--------- | :---------------- | :--------------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Vision** | Kimi K2.6         | `moonshotai/Kimi-K2.6` | `google/gemma-4-31B-it`, `MiniMaxAI/MiniMax-M3` | [Vision](/docs/inference/vision/overview), [OCR quickstart](/docs/quickstart-how-to-do-ocr) |

## Image generation

| Use case           | Recommended model | Model string             | Alternatives                                                        | Learn more                                                |
| :----------------- | :---------------- | :----------------------- | :------------------------------------------------------------------ | :-------------------------------------------------------- |
| **Text-to-image**  | Flash Image 2.5   | `google/flash-image-2.5` | `black-forest-labs/FLUX.2-pro`, `ByteDance-Seed/Seedream-4.0`       | [Text-to-image](/docs/inference/images/overview)          |
| **Image-to-image** | Flash Image 2.5   | `google/flash-image-2.5` | `black-forest-labs/FLUX.1-kontext-max`, `google/gemini-3-pro-image` | [Image-to-image](/docs/inference/images/reference-images) |

## Video generation

| Use case           | Recommended model | Model string        | Alternatives                                             | Learn more                                          |
| :----------------- | :---------------- | :------------------ | :------------------------------------------------------- | :-------------------------------------------------- |
| **Text-to-video**  | Sora 2 Pro        | `openai/sora-2-pro` | `google/veo-3.0`, `ByteDance/Seedance-1.0-pro`           | [Video generation](/docs/inference/videos/overview) |
| **Image-to-video** | Veo 3.0           | `google/veo-3.0`    | `ByteDance/Seedance-1.0-pro`, `kwaivgI/kling-2.1-master` | [Video generation](/docs/inference/videos/overview) |

## Audio

| Use case           | Recommended model | Model string              | Alternatives                                         | Learn more                                                |
| :----------------- | :---------------- | :------------------------ | :--------------------------------------------------- | :-------------------------------------------------------- |
| **Text-to-speech** | Cartesia Sonic 3  | `cartesia/sonic-3`        | `canopylabs/orpheus-3b-0.1-ft`, `hexgrad/Kokoro-82M` | [Text-to-speech](/docs/inference/text-to-speech/overview) |
| **Speech-to-text** | Whisper Large v3  | `openai/whisper-large-v3` | `nvidia/parakeet-tdt-0.6b-v3`, `deepgram/nova-3-en`  | [Speech-to-text](/docs/inference/transcription/overview)  |

## Embeddings, rerank, and moderation

| Use case       | Recommended model       | Model string                              | Notes                                                                   | Learn more                                                                                                               |
| :------------- | :---------------------- | :---------------------------------------- | :---------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Embeddings** | Multilingual E5 Large   | `intfloat/multilingual-e5-large-instruct` | -                                                                       | [Embeddings](/reference/embeddings-2)                                                                                    |
| **Rerank**     | MixedBread Rerank Large | `mixedbread-ai/Mxbai-Rerank-Large-V2`     | Only on [dedicated model inference](/docs/dedicated-endpoints/overview) | [Rerank](/docs/inference/embeddings/rerank), [Improve search with rerankers](/docs/how-to-improve-search-with-rerankers) |
| **Moderation** | Llama Guard 4 12B       | `meta-llama/Llama-Guard-4-12B`            | -                                                                       | -                                                                                                                        |

## Related resources

<CardGroup>
  <Card title="Serverless models" icon="list" href="/docs/serverless/models">
    Full catalog with context windows, pricing, and capabilities.
  </Card>

  <Card title="Dedicated model inference" icon="server" href="/docs/dedicated-endpoints/models">
    Models available on reserved hardware.
  </Card>

  <Card title="WhichLLM" icon="chart-bar" href="https://whichllm.together.ai/">
    Categorical benchmarks to compare models across use cases.
  </Card>

  <Card title="Pricing" icon="credit-card" href="https://together.ai/pricing">
    Per-token and per-output pricing for all models.
  </Card>
</CardGroup>
