---
title: "GPT-OSS quickstart"
source: https://docs.together.ai/docs/gpt-oss
path: docs/gpt-oss
---

Get started with GPT-OSS, OpenAI's open-weight reasoning model.

GPT-OSS is a flexible open-weight reasoning model designed for developers, researchers, and enterprises who need transparency and customization while maintaining the advanced reasoning capabilities of chain-of-thought processing.

GPT-OSS has been trained to think step-by-step before responding with an answer, excelling at complex reasoning tasks such as coding, mathematics, planning, puzzles, and agent workflows.

It features adjustable reasoning effort levels, allowing you to balance performance with computational cost.

<Frame>
  <img />
</Frame>

## How to use GPT-OSS API

Since reasoning models produce longer responses with chain-of-thought processing, stream tokens for a better user experience:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # pass in API key to api_key or set an env variable

  stream = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[
          {
              "role": "user",
              "content": "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?",
          }
      ],
      temperature=1.0,
      top_p=1.0,
      reasoning_effort="medium",
      stream=True,
  )

  for chunk in stream:
      if chunk.choices:
          print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "openai/gpt-oss-120b",
    messages: [{ 
      role: "user", 
      content: "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?" 
    }],
    temperature: 1.0,
    top_p: 1.0,
    reasoning_effort: "medium",
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.together.ai/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "openai/gpt-oss-120b",
       	"messages": [
            {"role": "user", "content": "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?"}
       	],
          "temperature": 1.0,
          "top_p": 1.0,
          "reasoning_effort": "medium",
          "stream": true
       }'
  ```
</CodeGroup>

This will produce the response below:

```json theme={null}
{
  "id": "o669aLj-62bZhn-96b01dc00f33ab9a",
  "object": "chat.completion",
  "created": 1754499896,
  "model": "openai/gpt-oss-120b",
  "service_tier": null,
  "system_fingerprint": null,
  "kv_transfer_params": null,
  "prompt": [],
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "**Short answer:**  \nNo. From “All roses are flowers” and “Some flowers are red” ...",
        "tool_calls": [],
        "reasoning": "We need to answer the logic puzzle. Statement: All roses ..."
      },
      "logprobs": null,
      "finish_reason": "stop",
      "seed": null
    }
  ],
  "usage": {
    "prompt_tokens": 96,
    "total_tokens": 984,
    "completion_tokens": 888
  }
}
```

To access only the chain-of-thought reasoning you can look at the `reasoning` property:

```plain theme={null}
We need to answer the logic puzzle. The premise: "All roses are flowers" (i.e., every rose is a flower). "Some flowers are red" (there exists at least one flower that is red). Does this entail that some roses are red? In standard syllogistic logic, no; you cannot infer that. Because the red flower could be a different type. The conclusion "Some roses are red" is not guaranteed. It's a classic syllogism: All R are F, Some F are R (actually some F are red). The conclusion "Some R are red" is not valid (invalid). So answer: No, we cannot conclude; we need additional assumption like "All red flowers are roses" or "All red things are roses". Provide explanation.

Hence final answer: no, not necessarily; situation possible where all roses are yellow etc.

Thus solve puzzle.
```

## Available models

GPT-OSS 120B is available on Together AI:

**GPT-OSS 120B:**

* **Model string:** `openai/gpt-oss-120b`.
* **Hardware requirements:** Fits on 80 GB GPU.
* **Architecture:** Mixture-of-Experts (MoE) with token-choice routing.
* **Context length:** 128K tokens with RoPE.
* **Best for:** Enterprise applications requiring maximum reasoning performance.

<Note>
  GPT-OSS 20B (`openai/gpt-oss-20b`) was removed from serverless inference on September 15, 2026, with `Qwen/Qwen3.5-9B` as its listed replacement. It remains available for [fine-tuning](/docs/fine-tuning/supported-models) and [dedicated endpoints](/docs/dedicated-endpoints/models). See the [deprecations page](/docs/deprecations) for details.
</Note>

## GPT-OSS best practices

Reasoning models like GPT-OSS should be used differently than standard instruct models to get optimal results:

**Recommended parameters:**

* **Reasoning effort:** Use the adjustable reasoning effort levels to control computational cost vs. accuracy.
* **Temperature:** Use 1.0 for maximum creativity and diverse reasoning approaches.
* **Top-p:** Use 1.0 to allow the full vocabulary distribution for optimal reasoning exploration.
* **System prompt:** The system prompt can be provided as a `developer` message which is used to provide information about the instructions for the model and available function tools.
* **System message:** It's recommended not to modify the `system` message which is used to specify reasoning effort, meta information like knowledge cutoff, and built-in tools.

**Prompting best practices:**
Think of GPT-OSS as a senior problem-solver – provide high-level objectives and let it determine the methodology:

* **Strengths:** Excels at open-ended reasoning, multi-step logic, and inferring unstated requirements.
* **Avoid over-prompting:** Micromanaging steps can limit its advanced reasoning capabilities.
* **Provide clear objectives:** Balance clarity with flexibility for optimal results.

## GPT-OSS use cases

* **Code review & analysis:** Comprehensive code analysis across large codebases with detailed improvement suggestions.
* **Strategic planning:** Multi-stage planning with reasoning about optimal approaches and resource allocation.
* **Complex document analysis:** Processing legal contracts, technical specifications, and regulatory documents.
* **Benchmarking AI systems:** Evaluates other LLM responses with contextual understanding, particularly useful in critical validation scenarios.
* **AI model evaluation:** Sophisticated evaluation of other AI systems with contextual understanding.
* **Scientific research:** Multi-step reasoning for hypothesis generation and experimental design.
* **Academic analysis:** Deep analysis of research papers and literature reviews.
* **Information extraction:** Efficiently extracts relevant data from large volumes of unstructured information, ideal for RAG systems.
* **Agent workflows:** Building sophisticated AI agents with complex reasoning capabilities.
* **RAG systems:** Enhanced information extraction and synthesis from large knowledge bases.
* **Problem solving:** Handling ambiguous requirements and inferring unstated assumptions.
* **Ambiguity resolution:** Interprets unclear instructions effectively and seeks clarification when needed.

## Managing context and costs

### Reasoning effort control

GPT-OSS features adjustable reasoning effort levels to optimize for your specific use case:

* **Low effort:** Faster responses for simpler tasks with reduced reasoning depth.
* **Medium effort:** Balanced performance for most use cases (recommended default).
* **High effort:** Maximum reasoning for complex problems requiring deep analysis. You should also specify `max_tokens` of \~30,000 with this setting.

### Token management

When working with reasoning models, it's crucial to maintain adequate space in the context window:

* Use `max_tokens` parameter to control response length and costs.
* Monitor reasoning token usage vs. output tokens - reasoning tokens can vary from hundreds to tens of thousands based on complexity.
* Consider reasoning effort level based on task complexity and budget constraints.
* Simpler problems may only require a few hundred reasoning tokens, while complex challenges could generate extensive reasoning.

### Cost/latency optimization

* Implement limits on total token generation using the `max_tokens` parameter.
* Balance thorough reasoning with resource utilization based on your specific requirements.
* Consider using lower reasoning effort for routine tasks and higher effort for critical decisions.

## Technical architecture

### Model architecture

* **MoE design:** Token-choice Mixture-of-Experts with SwiGLU activations for improved performance.
* **Expert selection:** Softmax-after-topk approach for calculating MoE weights, ensuring optimal expert utilization.
* **Attention mechanism:** RoPE (Rotary Position Embedding) with 128K context length.
* **Attention patterns:** Alternating between full context and sliding 128-token window for efficiency.
* **Attention sink:** Learned attention sink per-head with additional additive value in the softmax denominator.

### Tokenization

* **Standard compatibility:** Uses the same tokenizer as GPT-4o.
* **Broad support:** Ensures seamless integration with existing applications and tools.

### Context handling

* **128K context window:** Large context capacity for processing extensive documents.
* **Efficient patterns:** Optimized attention patterns for long-context scenarios.
* **Memory optimization:** GPT-OSS Large is designed to fit efficiently within 80 GB GPU memory.
