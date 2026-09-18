---
title: "Model Quality and Precision"
source: https://docs.fireworks.ai/models/model-quality
path: models/model-quality
---

How Fireworks tunes precision per model and validates every launch against the provider's official API before it serves production traffic.

Fireworks aims to serve the best possible version of each model across speed, quality, and latency. Even when our eval scores are on par with other open source providers, we take additional precautions before launch so that the model you call matches or exceeds the official API.

## Precision

Serverless models are served using a proprietary mixed-precision configuration (FP8, FP4, and BF16) that is custom-tuned per model. Every deployment is checked against the provider's official API and against an unquantized baseline before it serves production traffic.

* Attention, MoE experts, KV cache, and projections can each run at a different precision within the same deployment, rather than one blanket format across all models.
* The specific methods are refined on an ongoing basis. The validation methodology below is applied consistently across every model we serve, and is what we encourage you to evaluate directly.
* On standard serverless, this is what lets certain models from the Kimi family run at roughly 1/10th the cost and 2-3x the speed of comparable closed frontier models.

## How we validate quantization quality

We combine divergence testing with a suite of standard benchmarks.

| Metric               | What it measures                                                                                                      | Tolerance     |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------- |
| KL divergence (KLD)  | Change in output token distribution against the unquantized reference, measured separately for prefill and generation | Below \~0.007 |
| Token rejection rate | How often the top-p probability token changes against the reference precision                                         | Below \~3%    |

Divergence testing is supplemented with a suite of evolving benchmarks, checked against each model provider's own published or reproduced numbers, including side-by-side runs against the official API. These include AIME, GPQA, SWE-bench, Terminal-Bench, and DeepSWE, plus MMMU Pro and OCRBench for multimodal models.

<Note>
  Where our numbers diverge from a model card, we publish why. Deviations can occur when a benchmark harness assumes a decoding mode that differs from how the model is normally served.
</Note>

## What we test

Beyond precision itself, each model launch is validated across:

* **Prompt formatting**: chat template output checked against the model provider's own reference implementation.
* **Tool calling**: streaming, non-streaming, and grammar-constrained generation, across multi-turn workflows.
* **Numerical correctness**: precision matched against reference outputs via generations, logprobs, and KLD.
* **System behavior**: timeouts, disconnect handling, and correct error codes under load.
* **SDK compatibility**: common client SDKs and gateway or proxy services.

## Validation stages

Benchmarks describe model capability, but they do not capture whether a serving stack implements the model correctly. Because different failure classes surface at different stages, we run multiple layers of validation:

1. Deterministic unit tests for formatting, parsing, and tool-call edge cases.
2. Single-turn benchmark checks.
3. Multi-turn agentic evaluation.
4. Multimodal benchmarks for vision models.
5. Production monitoring and regression reruns.

This process has caught issues before they reached customers, including:

* Reasoning-trace instability in a newly released frontier model, identified pre-launch and resolved in coordination with the model provider and serving frameworks.
* A silent drift in reasoning that trapped the model in reasoning loops, which we found across all other providers.
* A tool-calling interruption under sustained load, resolved with an updated decoding safeguard.
* A load-handling edge case that could return an ambiguous response instead of a standard rate-limit signal, corrected so that normal retry behavior applies.

A single launch can involve hundreds of eval jobs across endpoints and configurations. We do not move on to performance tuning until quality meets our bar.

## Verify it yourself

We encourage you to verify these results independently. The serverless Chat Completions API exposes logprobs, so you can measure divergence against a reference implementation directly, using the same method described in our [quantization writeup](https://fireworks.ai/blog/fireworks-quantization).

```python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<FIREWORKS_API_KEY>",
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/gpt-oss-120b",
    messages=[{"role": "user", "content": "Explain KL divergence in one paragraph."}],
    logprobs=True,
    top_logprobs=5,
)

for entry in response.choices[0].logprobs.content:
    print(entry.token, entry.logprob, entry.top_logprobs)
```

<Tip>
  `top_logprobs` is capped by the deployment's `--max-logprobs` limit, which is 5 by default. See [Querying text models](/guides/querying-text-models) for the full response format.
</Tip>

## Custom and dedicated precision

On a [dedicated deployment](/guides/ondemand-deployments), a precision profile can be tailored to your workload instead of using the default serverless configuration. See [Quantization](/models/quantization) for the precisions you can select yourself, and contact your account team to scope a custom configuration.

## Related reading

<CardGroup>
  <Card title="Evaluating quantization" icon="chart-line" href="https://fireworks.ai/blog/fireworks-quantization">
    How Fireworks evaluates quantization precisely and interpretably.
  </Card>

  <Card title="GLM 5.3 Flash" icon="bolt" href="https://x.com/dzhulgakov/status/2093739346423947644">
    Benchmark scores are not the only indicator of performance.
  </Card>

  <Card title="DeepSeek V4 Pro" icon="microscope" href="https://fireworks.ai/blog/deepseek-v4-pro-validating-frontier-models-for-production">
    Validating frontier models for production.
  </Card>

  <Card title="Kimi K2.5" icon="ruler" href="https://fireworks.ai/blog/quality-first-with-kimi-k2p5">
    The benchmark gap: what it takes to ship Kimi K2.5.
  </Card>

  <Card title="gpt-oss" icon="shield-check" href="https://fireworks.ai/blog/gpt-oss-on-fireworks-ai">
    Quality first: how Fireworks is the go-to place for gpt-oss.
  </Card>
</CardGroup>
