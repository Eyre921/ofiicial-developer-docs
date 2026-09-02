---
title: "Recommended models"
source: https://docs.together.ai/docs/inference/recommended-models
path: docs/inference/recommended-models
---

Our picks for common inference use cases.

Together hosts 100+ open-source models across text, image, video, and audio.

Most of the models below are for instant [serverless inference](/docs/serverless/models), or reserved hardware deployments with [dedicated model inference](/docs/dedicated-endpoints/models). Both options use the same [inference API](/docs/inference/overview).

## Chat & text

| Use case                     | Recommended model | Model string                         | Alternatives                                                     | Learn more                                                    |
| :--------------------------- | :---------------- | :----------------------------------- | :--------------------------------------------------------------- | :------------------------------------------------------------ |
| **Chat**                     | Kimi K3           | `moonshotai/Kimi-K3`                 | `Qwen3.8-2.4T-A95B`                                              | [Chat completions](/docs/inference/chat/overview)             |
| **Reasoning**                | Kimi K3           | `moonshotai/Kimi-K3`                 | `deepseek-ai/DeepSeek-V4-Pro-0813`                               | [Reasoning](/docs/inference/chat/reasoning)                   |
| **Coding agents**            | Kimi K3           | `moonshotai/Kimi-K3`                 | `deepseek-ai/DeepSeek-V4-Flash-0731`, `zai-org/GLM-5.3`          | [Build coding agents](/docs/how-to-build-coding-agents)       |
| **Small and fast**           | Qwen3.8 27B       | `Qwen/Qwen3.8-27B`                   | `google/gemma-4-31B-it`, `openai/gpt-oss-20b`, `Qwen/Qwen3.5-9B` | -                                                             |
| **Mid-size general purpose** | DeepSeek V4 Flash | `deepseek-ai/DeepSeek-V4-Flash-0731` | `MiniMaxAI/MiniMax-M3`                                           | -                                                             |
| **Function calling**         | DeepSeek V4 Flash | `deepseek-ai/DeepSeek-V4-Flash-0731` | `zai-org/GLM-5.3`                                                | [Function calling](/docs/inference/function-calling/overview) |

## Vision

| Use case   | Recommended model | Model string        | Alternatives                                 | Learn more                                                                                  |
| :--------- | :---------------- | :------------------ | :------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Vision** | Qwen3.8 2.4T A95B | `Qwen3.8-2.4T-A95B` | `moonshotai/Kimi-K3`, `MiniMaxAI/MiniMax-M3` | [Vision](/docs/inference/vision/overview), [OCR quickstart](/docs/quickstart-how-to-do-ocr) |

## Image generation

| Use case           | Recommended model | Model string         | Alternatives             | Learn more                                                |
| :----------------- | :---------------- | :------------------- | :----------------------- | :-------------------------------------------------------- |
| **Text-to-image**  | GPT Image 2       | `openai/gpt-image-2` | `google/flash-image-2.5` | [Text-to-image](/docs/inference/images/overview)          |
| **Image-to-image** | GPT Image 2       | `openai/gpt-image-2` | `google/flash-image-2.5` | [Image-to-image](/docs/inference/images/reference-images) |

## Video generation

| Use case           | Recommended model      | Model string             | Alternatives               | Learn more                                          |
| :----------------- | :--------------------- | :----------------------- | :------------------------- | :-------------------------------------------------- |
| **Text-to-video**  | ByteDance Seedance 2.5 | `ByteDance/Seedance-2.5` | `black-forest-labs/FLUX-3` | [Video generation](/docs/inference/videos/overview) |
| **Image-to-video** | ByteDance Seedance 2.5 | `ByteDance/Seedance-2.5` | `black-forest-labs/FLUX-3` | [Video generation](/docs/inference/videos/overview) |

## Audio

| Use case           | Recommended model                      | Model string                             | Alternatives                                         | Learn more                                                |
| :----------------- | :------------------------------------- | :--------------------------------------- | :--------------------------------------------------- | :-------------------------------------------------------- |
| **Text-to-speech** | Cartesia Sonic 3                       | `cartesia/sonic-3`                       | `canopylabs/orpheus-3b-0.1-ft`, `hexgrad/Kokoro-82M` | [Text-to-speech](/docs/inference/text-to-speech/overview) |
| **Speech-to-text** | NVIDIA Nemotron 3.5 ASR Streaming 0.6B | `nvidia/nemotron-3.5-asr-streaming-0.6b` | `openai/whisper-large-v3`                            | [Speech-to-text](/docs/inference/transcription/overview)  |

## Embeddings and rerank

| Use case       | Recommended model       | Model string                              | Notes                                                                   | Learn more                                                                                                               |
| :------------- | :---------------------- | :---------------------------------------- | :---------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **Embeddings** | Multilingual E5 Large   | `intfloat/multilingual-e5-large-instruct` | -                                                                       | [Embeddings](/reference/embeddings-2)                                                                                    |
| **Rerank**     | MixedBread Rerank Large | `mixedbread-ai/Mxbai-Rerank-Large-V2`     | Only on [dedicated model inference](/docs/dedicated-endpoints/overview) | [Rerank](/docs/inference/embeddings/rerank), [Improve search with rerankers](/docs/how-to-improve-search-with-rerankers) |

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
