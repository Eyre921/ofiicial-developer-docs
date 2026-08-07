---
title: "Inference metrics: TTFT & TPS"
source: https://docs.together.ai/learn/ttft-and-tps
path: learn/ttft-and-tps
---

Two numbers that describe how fast an LLM feels.

**TL;DR:** There are two numbers that describe how fast an LLM feels in practice. The first is **TTFT** (time to first token), which is how long you wait between sending your request and seeing the first word of the response appear. The second is **TPS** (tokens per second), which is how fast each word appears after that. These two numbers are affected by different things, and you usually want to optimize them differently depending on the application.

## Why TTFT and TPS matter

The two most important metrics when it comes to LLM inference are time to first token (TTFT) and tokens per second (TPS). Other metrics such as tokens per minute (TPM) per GPU, time between tokens (TBT), and more can be understood as functions of these.

When you call an LLM, there is a pause before tokens stream back to you. This initial wait time is the TTFT: the pause between sending your request and the model showing you the first word of its reply.

Once the tokens start streaming, how fast they're generated is measured using TPS. This is the rate at which tokens stream in once the model has actually started generating.

You can have the same total time across two different combinations of TTFT and TPS and the experience will feel very different. A 5-second TTFT followed by 100 TPS feels sluggish to start and then snappy once it gets going. A 200ms TTFT followed by 20 TPS feels responsive at first and then laggy. Users perceive these two flavors of "slow" differently, which is why the system has to be tuned with both numbers in mind. Voice applications require a very low TTFT, while coding agent applications can have a slightly more relaxed TTFT but benefit from higher TPS.

<TimingDiagram />

## Two phases of inference: prefill and decode

Inference happens in two phases, and TTFT and TPS each correspond to one of them:

* **Prefill:** The model processes your entire prompt in one pass. The compute in this phase is parallel across positions, which means the prefill is essentially a single big matrix multiplication that the GPU is well-suited to handle. The cost of prefill scales with prompt length.
* **Decode:** The model generates output tokens one at a time, with each token depending on the previous one. The cost of decode scales with output length.

TTFT is mostly prefill latency plus a little overhead from the network and platform. TPS is mostly decode speed. The two phases share a model and a GPU, but the bottleneck for each is different:

* Prefill is **compute-bound**, meaning the GPU is multiplying matrices flat-out, and the limiting factor is how fast it can do the math.
* Decode is **memory-bound**, meaning the GPU spends most of its time reading model weights and the cached state from memory rather than actually multiplying.

For more on the forward-pass details that produce these two phases, see [How LLMs work](/learn/how-llms-work).

## What affects TTFT

A handful of things affect how long you wait for the first token:

* **Prompt length:** This is the single biggest factor. A 16K-token prompt takes meaningfully longer to prefill than a 1K-token prompt.
* **Model size:** A 70B-parameter model has more matmuls to do per token than an 8B-parameter model does. Larger models have higher TTFT on the same prompt, all other things being equal.
* **Prompt caching:** If you reuse the same system prompt or the same document across many calls, the platform can cache the prefill state and skip that work on a cache hit. When this happens, TTFT and compute cost drop to near-zero for the cached portion. On Together, prompt caching is enabled by default on [dedicated endpoints](/docs/dedicated-endpoints/settings).
* **Server load and queueing:** On shared serverless infrastructure, if the GPU is busy when your request arrives, you wait in the queue. Quiet times have lower TTFT than peak times for this reason.
* **Cold starts:** If a model has to be loaded fresh into GPU memory (rare on serverless, more common on dedicated endpoints that scale to zero), TTFT can be several seconds because the model has to be moved from disk into VRAM before any inference can happen. Consecutive calls thereafter should be much faster.

## What affects TPS

A different set of things affects how fast each token streams in:

* **Model size:** Bigger models have more weights to read per token. A 405B model has lower TPS than an 8B model, all other things being equal.
* **Quantization:** If you store the weights using fewer bits (fp8 instead of fp16, int4 instead of int8), the memory bandwidth needed to read them goes down. Lower memory bandwidth means higher TPS, sometimes by a meaningful amount. See [Quantization](/learn/quantization) for more on this.
* **Batching:** Servers run many requests at once to amortize the cost of reading model weights from memory. More requests in a batch means more total throughput across the GPU, but the per-request TPS can dip slightly because the GPU is doing more work per cycle.
* **Speculative decoding:** A small "draft" model guesses ahead and the big model verifies. When the guesses are right, you get 2 to 3 times the TPS for the same model. (This is mostly a server-side concern.)
* **Context length:** As the response grows, decoding gets a little bit slower per token, because the KV cache the model has to read from grows as well. The effect is usually small unless the output is very long.
* **Mixture-of-Experts (MoE):** MoE models split the feed-forward layers into many small "experts" and route each token through only a handful of them. That means the *active* parameters per token are a small fraction of the total. A 400B MoE with \~17B active params decodes closer to the speed of a 17B dense model than a 400B dense one. The total VRAM footprint still matches the full model (all experts have to be resident in memory in case they get routed to), but per-token TPS scales with active params rather than total params. Most modern frontier open models (DeepSeek-V3, Llama 4, Qwen3-Coder, Kimi K2) are MoE for exactly this reason.

## Next steps

<CardGroup>
  <Card title="Context windows" icon="layout-board" href="/learn/context-windows">
    Why long inputs get slow before they get expensive.
  </Card>

  <Card title="Quantization" icon="zoom-in" href="/learn/quantization">
    The most-bang-for-your-buck TPS lever.
  </Card>

  <Card title="Choosing a deployment option" icon="server" href="/learn/choosing-a-deployment-option">
    When serverless variance is hurting your latency budget.
  </Card>
</CardGroup>
