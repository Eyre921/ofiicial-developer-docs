---
title: "Which model should I use?"
source: https://docs.fireworks.ai/guides/recommended-models
path: guides/recommended-models
---

Find the best open models for your use case or migrate from closed source models like Claude, GPT, and Gemini

Looking for the right open source model? Whether you're exploring by use case or migrating from closed source models like Claude, GPT, or Gemini, this guide provides recommendations based on **Fireworks internal testing**, **customer deployments**, and **external benchmarks**. We update it regularly as new models emerge.

<Tip>
  Medium and small models typically offer faster responses and lower cost, with some tradeoff in capability for more complex tasks.
</Tip>

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
      <td><strong>Code & Development</strong></td>
      <td><strong>Code generation, reasoning & agentic tasks</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813">DeepSeek V4 Pro (0813)</a>, <a href="https://app.fireworks.ai/models/fireworks/kimi-k3">Kimi K3</a>, <a href="https://app.fireworks.ai/models/fireworks/glm-5p2">GLM 5.2</a>, <a href="https://app.fireworks.ai/models/fireworks/minimax-m3">MiniMax M3</a></td>
    </tr>

    <tr>
      <td><strong>AI Applications</strong></td>
      <td><strong>AI agents with tool use</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/kimi-k2p6">Kimi K2.6</a>, <a href="https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813">DeepSeek V4 Pro (0813)</a>, <a href="https://app.fireworks.ai/models/fireworks/glm-5p2">GLM 5.2</a>, <a href="https://app.fireworks.ai/models/fireworks/minimax-m3">MiniMax M3</a></td>
    </tr>

    <tr>
      <td />

      <td><strong>General reasoning & planning</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813">DeepSeek V4 Pro (0813)</a>, <a href="https://app.fireworks.ai/models/fireworks/kimi-k2p6">Kimi K2.6</a>, <a href="https://app.fireworks.ai/models/fireworks/glm-5p2">GLM 5.2</a>, <a href="https://app.fireworks.ai/models/fireworks/gpt-oss-120b">GPT-OSS 120B</a> <em>(medium)</em></td>
    </tr>

    <tr>
      <td />

      <td><strong>Long context & summarization</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813">DeepSeek V4 Pro (0813)</a>, <a href="https://app.fireworks.ai/models/fireworks/kimi-k2p6">Kimi K2.6</a>, <a href="https://app.fireworks.ai/models/fireworks/qwen3p7-plus">Qwen3.7 Plus</a>, <a href="https://app.fireworks.ai/models/fireworks/glm-5p2">GLM 5.2</a>, <a href="https://app.fireworks.ai/models/fireworks/deepseek-v4-flash-0731">DeepSeek V4 Flash (0731)</a></td>
    </tr>

    <tr>
      <td />

      <td><strong>Fast extraction, classification & search</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/deepseek-v4-flash-0731">DeepSeek V4 Flash (0731)</a>, <a href="https://app.fireworks.ai/models/fireworks/minimax-m3">MiniMax M3</a>, <a href="https://app.fireworks.ai/models/fireworks/kimi-k2p6">Kimi K2.6</a>, <a href="https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4">Step 3.7 Flash</a>, <a href="https://app.fireworks.ai/models/fireworks/qwen3-8b">Qwen3 8B</a> <em>(small)</em></td>
    </tr>

    <tr>
      <td><strong>Vision & Multimodal</strong></td>
      <td><strong>Vision & document understanding</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/kimi-k2p6">Kimi K2.6</a>, <a href="https://app.fireworks.ai/models/fireworks/qwen3p7-plus">Qwen3.7 Plus</a>, <a href="https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4">Step 3.7 Flash</a>, <a href="https://app.fireworks.ai/models/fireworks/gemma-4-31b-it">Gemma 4 31B</a> <em>(small)</em></td>
    </tr>

    <tr>
      <td />

      <td><strong>Audio & video understanding</strong></td>
      <td><a href="https://fireworks.ai/models/fireworks/qwen3-omni-30b-a3b-instruct">Qwen3 Omni 30B A3B Instruct</a>, <a href="https://fireworks.ai/models/fireworks/nvidia-nemotron-3-nano-omni-30b-a3b">NVIDIA Nemotron 3 Nano Omni 30B A3B</a></td>
    </tr>

    <tr>
      <td><strong>Search & Retrieval</strong></td>
      <td><strong>Embeddings & reranking</strong></td>
      <td><a href="https://app.fireworks.ai/models/fireworks/qwen3-embedding-8b">Qwen3 Embedding 8B</a>, <a href="https://app.fireworks.ai/models/fireworks/qwen3-reranker-8b">Qwen3 Reranker 8B</a></td>
    </tr>
  </tbody>
</table>

<Tip>
  For audio/video workloads, start with `Qwen3 Omni 30B A3B Instruct`. `NVIDIA Nemotron 3 Nano Omni 30B A3B` is a newer omni option, but its reasoning mode is currently limited to text+image inputs; use `enable_thinking: false` for video/audio requests.
</Tip>

<Tip>
  Looking for a smaller MiniLM, BGE, or nomic style embedder? Those legacy models are not shown in the Model Library but still serve on serverless. See [embeddings and reranking](/guides/querying-embeddings-models) for the supported ids.
</Tip>

***

## Migrating from Closed Models?

If you're currently using Claude, OpenAI / GPT, or Gemini models, here's a guide to the best open source alternatives on Fireworks by use case and latency requirements.

### Claude Alternatives

| **Closed Source**                | **Use Case**                                             | **Latency Budget** | **Open Source Alternative**                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------- | -------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Claude Opus 4.8 / Sonnet 4.6** | • Agentic use cases<br />• Coding<br />• Research agents | High               | • [DeepSeek V4 Pro (0813)](https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813)<br />• [Kimi K3](https://app.fireworks.ai/models/fireworks/kimi-k3)<br />• [GLM 5.2](https://app.fireworks.ai/models/fireworks/glm-5p2)<br />• [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)<br />• [Qwen3.7 Plus](https://app.fireworks.ai/models/fireworks/qwen3p7-plus) |
| **Claude Haiku 4.5**             | • Agentic use cases<br />• Coding<br />• Research agents | Low                | • [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4)<br />• [DeepSeek V4 Flash (0731)](https://app.fireworks.ai/models/fireworks/deepseek-v4-flash-0731)<br />• [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)<br />• [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) <em>(small)</em>                                    |

### OpenAI GPT Alternatives

| **Closed Source**         | **Use Case**                                          | **Latency Budget** | **Open Source Alternative**                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | ----------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPT-5.5 / GPT-5.5 Pro** | • Agentic use cases<br />• Research agents            | High               | • [DeepSeek V4 Pro (0813)](https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813)<br />• [Kimi K2.6](https://app.fireworks.ai/models/fireworks/kimi-k2p6)<br />• [GLM 5.2](https://app.fireworks.ai/models/fireworks/glm-5p2)<br />• [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)                                        |
| **GPT-5.4 mini & nano**   | • Chatbots<br />• Intent classification<br />• Search | Low                | • [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4)<br />• [DeepSeek V4 Flash (0731)](https://app.fireworks.ai/models/fireworks/deepseek-v4-flash-0731)<br />• [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)<br />• [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) <em>(small)</em> |

### Google Gemini Alternatives

| **Closed Source**                     | **Use Case**                                                 | **Latency Budget** | **Open Source Alternative**                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.1 Pro**                    | • Agentic use cases<br />• Research agents<br />• Multimodal | High               | • [DeepSeek V4 Pro (0813)](https://app.fireworks.ai/models/fireworks/deepseek-v4-pro-0813)<br />• [Kimi K2.6](https://app.fireworks.ai/models/fireworks/kimi-k2p6)<br />• [GLM 5.2](https://app.fireworks.ai/models/fireworks/glm-5p2)<br />• [Qwen3.7 Plus](https://app.fireworks.ai/models/fireworks/qwen3p7-plus)<br />• [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3) |
| **Gemini 3.5 Flash & 3.1 Flash-Lite** | • Chatbots<br />• Intent classification<br />• Search        | Low                | • [Step 3.7 Flash](https://app.fireworks.ai/models/fireworks/step-3p7-flash-nvfp4)<br />• [DeepSeek V4 Flash (0731)](https://app.fireworks.ai/models/fireworks/deepseek-v4-flash-0731)<br />• [MiniMax M3](https://app.fireworks.ai/models/fireworks/minimax-m3)<br />• [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) <em>(small)</em>                                        |

**Understanding Latency Budget:**

* **High latency budget**: Quality is priority. Best for complex reasoning, multi-step workflows, and research tasks where accuracy matters more than speed.
* **Low latency budget**: Speed is priority. Best for user-facing applications like chatbots, real-time search, and high-throughput classification.

***

<Tip>
  You can explore and filter every available model in the [Fireworks Model Library](https://app.fireworks.ai/models).
</Tip>

*Last updated: August 2026*
