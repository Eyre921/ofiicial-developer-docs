---
title: "Context windows"
source: https://docs.together.ai/learn/context-windows
path: learn/context-windows
---

The model's working memory. A hard limit on the way in, a soft constraint inside it.

**TL;DR:** The context window is the maximum number of tokens the model can utilize in a single request. Both the input you send and the output the model generates must fit inside that this budget when combined. The context window is a hard limit, meaning that if you exceed it, the request will fail before completion.

## The model's working memory

It helps to think about the context window in terms of your own working memory. You can hold a phone number in your head for about a minute, maybe two. If you try to remember a grocery list and do some mental arithmetic at the same time, something starts to slip. Your brain has a fixed capacity for how much it can keep track of at once, and the more you try to hold, the harder it is to think clearly and attend to everything.

A model has a similar ceiling, except its size is published on the model's spec sheet. Every model has a number called the **max context length**, the maximum number of tokens it can take in a single request. The system prompt, every prior conversation turn, the each new user message, reasoning traces, prior tool calls, tool results, and the reply the model is about to generate all share the same budget, and must be smaller than the max context length. Once a request exceeds the limit, it fails unless you summarize the history down to fit (often called "compacting").

Context windows have been getting bigger and currently run anywhere between 250K and 1M tokens. Over the last few years, the practical implication of this number has shifted from "I can fit one document" to "I can fit an entire codebase or a whole book" in a single call. A bigger window opens up new use cases—but it's not free, as you'll see below.

## What different platforms do

Different platforms handle context window overflow in different ways:

* **Reject the request:** The API returns an error telling you that you exceeded the window. This is the most direct option and the easiest one to debug, because you immediately know that you have a problem to fix.
* **Truncate the input:** Some platforms silently drop the oldest messages until the input fits. This is fast to ship from the platform's side, but it can make the model act amnesic in long conversations because the model has no way to know that something was cut from earlier in the history.
* **Truncate the output:** If the input fits but the model runs out of room to reply, generation stops mid-token. You'll see a response with `finish_reason: "length"`, which tells you the response was cut off before the model decided it was finished.

On Together, the `max_tokens` parameter caps the output, and the input plus `max_tokens` must fit within the model's context window. See [inference parameters](/docs/inference/chat/parameters) for the full list of request parameters.

<WindowSliderDiagram />

## Why bigger windows are not free

There are two costs that grow with the size of your input:

### Prefill compute (scales roughly quadratically)

Before the model can generate anything, it has to process the entire input you gave it in a single forward pass. The attention step in that forward pass has every token look at every other token, which is roughly *N × N* work for an input of *N* tokens. If you double the size of your prompt, you more than double the amount of time the model spends before the first output token appears. This time-to-first-token effect is covered in detail in [TTFT & TPS](/learn/ttft-and-tps).

### KV cache memory (scales linearly with length)

While the model is generating output, it keeps a small per-layer state for every token it has already seen. That state is called the **key-value (KV) cache**, and its size grows linearly with the total number of tokens in the request. Long contexts eat GPU memory, and the amount of GPU memory available limits how many concurrent requests a server can run at once. That, in turn, affects throughput and price.

<Info>
  Modern long-context models use a number of attention variants (sliding window, sparse attention, grouped-query attention, compressed sparse attention, etc.) to bend that quadratic curve. Even with these optimizations, however, the fundamental rule still holds: long inputs cost more compute, and long histories cost more memory. A 100K-token prompt is genuinely about ten times more expensive than a 10K-token one, even when you are running it on the same model.
</Info>

## The "lost in the middle" effect

Having a 1M-token window does not mean the model uses every one of those tokens equally well. Models are known to pay more attention to the beginning and end of a long input than to the middle. [Liu et al. (2023)](https://arxiv.org/abs/2307.03172) named this the "lost in the middle" effect. If you put the most important context at the top of the prompt and again near the bottom, the quality of the model's response tends to hold up better than if you bury that information in the middle of 150K tokens of background. See [context engineering](/learn/prompt-engineering) for more details.

<img alt="A line chart from Liu et al. 2023 showing GPT-3.5-turbo accuracy on a 20-document QA task as a function of where the answer-containing document is placed. Accuracy is ~76% when the answer is in the 1st document, drops to a low of ~54% around the 10th position, then rises back to ~63% at the 20th. A horizontal dashed line shows the closed-book baseline of ~56%, which the in-context model dips below in the middle range." />

<p>
  Source: <a href="https://arxiv.org/abs/2307.03172">Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (2023)</a>. Accuracy is highest when the answer sits at the very start or very end of the context, and dips below the closed-book baseline when it's buried in the middle.
</p>

<Info>
  Newer "needle in a haystack" benchmarks measure whether a model can reliably retrieve a single fact placed at various depths in a long context. Frontier models in 2026 do well on simple needles, but they degrade significantly on multi-fact retrieval and reasoning that spans different parts of the context.
</Info>

## Long-context optimizations

Plain attention does work proportional to the square of the input length (the *N × N* cost from above). If a model claims a 1M context window and still runs efficiently (such as DeepSeek-V4), something else is going on under the hood. The main tricks that long-context models use are:

* **Sliding-window attention:** Each token only looks at the most recent *W* tokens (for example, *W* = 4K) instead of all previous tokens. This cuts the math from quadratic to linear at the cost of weaker long-range dependencies. To recover some of that range, sliding-window attention is often mixed with a few full-attention layers in the same model.
* **Grouped-query attention (GQA):** Multiple attention heads share the same keys and values, which shrinks the KV cache by a meaningful factor. GQA is cheap to implement and widely used.
* **Mixture-of-Experts (MoE):** Only a fraction of the model's parameters are run/active per token. This does not shrink the context, but it makes long-context calls dramatically cheaper to compute because the model is doing less work per token.
* **Position interpolation / RoPE scaling:** These are mathematical tricks that let a model trained on a 4K context generalize to 32K or more without retraining from scratch.

You usually do not need to think about which technique a given model is using, but it explains why two models with the same nominal window size can have very different latencies and qualities.

## Strategies for handling excess context

At some point you will have more relevant text than fits in the window. There are a few options for handling this:

* **Retrieval-augmented generation (RAG):** Index your data in a vector store. At query time, look up the chunks most relevant to the user's question, and only include those chunks in the prompt. Retrieval scales to arbitrary corpora because you are only ever putting a small relevant slice in front of the model.
* **Summarization and compaction:** As the conversation grows, you can compress old turns into a shorter summary that takes their place. You lose some fidelity to the exact wording of earlier turns, but the window stays manageable.
* **Caching:** If you keep sending the same system prompt or the same background document across many calls, prompt caching lets the model skip the prefill work for the cached portion. This does not shrink the context, but it makes long-prompt calls faster and cheaper. On Together, prompt caching is enabled by default on [dedicated endpoints](/docs/dedicated-endpoints/settings).
* **Bigger model:** When all else fails, switch to a model with a larger window. Windows keep growing, with models such as DeepSeek-V4 pushing toward 1M tokens.

## Next steps

<CardGroup>
  <Card title="Inference metrics: TTFT & TPS" icon="dashboard" href="/learn/ttft-and-tps">
    How the prefill / decode split shows up as latency.
  </Card>

  <Card title="Tokens & tokenization" icon="scissors" href="/learn/tokens-and-tokenization">
    How to estimate token counts before you call.
  </Card>

  <Card title="Context engineering" icon="messages" href="/learn/prompt-engineering">
    What to put in (and what to cut) when the window matters.
  </Card>
</CardGroup>
