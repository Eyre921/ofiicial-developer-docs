---
title: "Which model should I use?"
source: https://docs.fireworks.ai/guides/recommended-models
path: guides/recommended-models
---

Pick the best Fireworks open-weight model for chat, coding, vision, embeddings, and agents, or migrate off Claude, GPT, and Gemini to comparable open models.

Looking for the right open source model? Whether you're exploring by use case or migrating from closed source models like Claude, GPT, or Gemini, this guide provides recommendations based on **Fireworks internal testing**, **customer deployments**, and **external benchmarks**. We update it regularly as new models emerge.

> [!TIP]
>
> Medium and small models typically offer faster responses and lower cost, with some tradeoff in capability for more complex tasks.

## Choose by Use Case

<table>
  <colgroup>
    <col />

    <col />

    <col />
  </colgroup>

  <thead>
    <tr>
      <th>Category</th>
      <th>Use Case</th>
      <th>Recommended Models</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Code & Development**</td>
      <td>**Code generation, reasoning & agentic tasks**</td>
      <td>[DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017), [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3), [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3), [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)</td>
    </tr>

    <tr>
      <td>**AI Applications**</td>
      <td>**AI agents with tool use**</td>
      <td>[Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3), [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017), [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3), [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)</td>
    </tr>

    <tr>
      <td />

      <td>**General reasoning & planning**</td>
      <td>[DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017), [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3), [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3), [GPT-OSS 120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(medium)*</td>
    </tr>

    <tr>
      <td />

      <td>**Long context & summarization**</td>
      <td>[DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017), [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3), [Qwen3.7 Plus](https://app.fireworks.ai/models/fireworks/qwen3p7-plus), [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3)</td>
    </tr>

    <tr>
      <td />

      <td>**Fast extraction, classification & search**</td>
      <td>[DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017), [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3), [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3), [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(small)*</td>
    </tr>

    <tr>
      <td>**Vision & Multimodal**</td>
      <td>**Vision & document understanding**</td>
      <td>[DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017), [Qwen3.7 Plus](https://app.fireworks.ai/models/fireworks/qwen3p7-plus), [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4), [Gemma 4 31B](https://app.fireworks.ai/models/fireworks/gemma-4-31b-it) *(small)*</td>
    </tr>

    <tr>
      <td />

      <td>**Audio & video understanding**</td>
      <td>[Qwen3 Omni 30B A3B Instruct](https://fireworks.ai/models/fireworks/qwen3-omni-30b-a3b-instruct), [NVIDIA Nemotron 3 Nano Omni 30B A3B](https://fireworks.ai/models/fireworks/nvidia-nemotron-3-nano-omni-30b-a3b)</td>
    </tr>

    <tr>
      <td>**Search & Retrieval**</td>
      <td>**Embeddings & reranking**</td>
      <td>[Qwen3 Embedding 8B](https://app.fireworks.ai/models/fireworks/qwen3-embedding-8b), [Qwen3 Reranker 8B](https://app.fireworks.ai/models/fireworks/qwen3-reranker-8b)</td>
    </tr>
  </tbody>
</table>

> [!TIP]
>
> Looking for a smaller MiniLM, BGE, or nomic style embedder? Those legacy models are not shown in the Model Library but still serve on serverless. See [embeddings and reranking](/guides/querying-embeddings-models) for the supported ids.

***

## Migrating from Closed Models?

If you're currently using Claude, OpenAI / GPT, or Gemini models, here's a guide to the best open source alternatives on Fireworks by use case and latency requirements.

### Claude Alternatives

| **Closed Source** | **Use Case** | **Latency Budget** | **Open Source Alternative** |
| - | - | - | - |
| **Claude Opus 4.8 / Sonnet 4.6** | • Agentic use cases • Coding • Research agents | High | • [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017) • [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3) • [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3) • [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) • [Qwen3.7 Plus](https://app.fireworks.ai/models/fireworks/qwen3p7-plus) |
| **Claude Haiku 4.5** | • Agentic use cases • Coding • Research agents | Low | • [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4) • [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017) • [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) • [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(small)* |

### OpenAI GPT Alternatives

| **Closed Source** | **Use Case** | **Latency Budget** | **Open Source Alternative** |
| - | - | - | - |
| **GPT-5.5 / GPT-5.5 Pro** | • Agentic use cases • Research agents | High | • [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017) • [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3) • [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3) • [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) |
| **GPT-5.4 mini & nano** | • Chatbots • Intent classification • Search | Low | • [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4) • [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017) • [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) • [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(small)* |

### Google Gemini Alternatives

| **Closed Source** | **Use Case** | **Latency Budget** | **Open Source Alternative** |
| - | - | - | - |
| **Gemini 3.1 Pro** | • Agentic use cases • Research agents • Multimodal | High | • [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017) • [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3) • [GLM 5.3](https://app.fireworks.ai/models/fireworks/glm-5p3) • [Qwen3.7 Plus](https://app.fireworks.ai/models/fireworks/qwen3p7-plus) • [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) |
| **Gemini 3.5 Flash & 3.1 Flash-Lite** | • Chatbots • Intent classification • Search | Low | • [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4) • [DeepSeek V4.1 Flash 1017](https://app.fireworks.ai/models/fireworks/deepseek-v4p1-flash-1017) • [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) • [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(small)* |

**Understanding Latency Budget:**

* **High latency budget**: Quality is priority. Best for complex reasoning, multi-step workflows, and research tasks where accuracy matters more than speed.
* **Low latency budget**: Speed is priority. Best for user-facing applications like chatbots, real-time search, and high-throughput classification.

***

> [!TIP]
>
> You can explore and filter every available model in the [Fireworks Model Library](https://app.fireworks.ai/models).

*Last updated: October 2026*
