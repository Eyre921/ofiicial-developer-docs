---
title: "Speculative Decoding"
source: https://docs.fireworks.ai/deployments/speculative-decoding
path: deployments/speculative-decoding
---

Speed up generation with draft models and n-gram speculation

Speculative decoding reduces generation latency by proposing multiple tokens and
letting the target model verify them in parallel. The target model still verifies
every accepted token; the drafter does not replace the target model.

The benefit depends on both the cost of producing draft tokens and how often the
target model accepts them. A poorly matched drafter can make generation slower,
so benchmark with representative traffic before overriding Fireworks defaults.

<Note>
  The deployment flags on this page apply to [dedicated
  deployments](/guides/ondemand-deployments). Fireworks manages the serving
  configuration for Serverless models.
</Note>

## Start with the default

<Tip>
  **For most supported models, a default drafter and draft-token count are already
  configured.** A new deployment inherits those settings, so you usually do not
  need to pass any speculative-decoding flags.

  Create the deployment normally, then benchmark it before changing the drafter:

  ```bash theme={null}
  firectl deployment create accounts/fireworks/models/<MODEL_ID> --wait
  ```
</Tip>

If the base model does not define a default drafter, the deployment runs without
model-based speculative decoding. To explicitly disable an inherited default
when creating a comparison deployment, use:

```bash theme={null}
firectl deployment create accounts/fireworks/models/<MODEL_ID> \
  --disable-speculative-decoding \
  --wait
```

## Choose a method

| Method                                         | Best starting point                                                                                               | Configuration                                          |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Default model-based speculation                | General chat, reasoning, and coding traffic                                                                       | No flags; inherit the model's default                  |
| Custom draft model                             | A validated drafter for your model or traffic distribution                                                        | `--draft-model` and `--draft-token-count`              |
| N-gram speculation                             | Repetitive output, code editing, and structured generation where output often repeats the prompt or prior context | `--ngram-speculation-length` and `--draft-token-count` |
| [Predicted Outputs](/guides/predicted-outputs) | The caller already knows most of the expected response, such as regenerating a file with a small edit             | Request-level `prediction` or `speculation` input      |

Predicted Outputs can be used in addition to a deployment's model-based
speculative decoding.

## Configuration options

| Flag                             | Description                                                                                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--draft-model`                  | Resource name of a Fireworks or custom draft model. If omitted, the deployment inherits the base model's default drafter.                                                 |
| `--draft-token-count`            | Number of candidate tokens proposed per step. It is required with an explicitly selected draft model or N-gram speculation. Start with `4`, then benchmark nearby values. |
| `--ngram-speculation-length`     | Length of the previous input sequence used for N-gram matching. This does not require a separate draft model.                                                             |
| `--disable-speculative-decoding` | Disables inherited speculative-decoding settings when creating a deployment.                                                                                              |

<Note>
  `--draft-model` and `--ngram-speculation-length` are alternative deployment
  strategies and cannot be used together.
</Note>

## Custom draft models

For self-service configuration, use a small base model that is compatible with
the target model. In practice, this means using the same model family and
tokenizer. A model that is merely smaller is not necessarily a useful drafter;
its acceptance rate and execution cost both matter.

### Fallback draft models

If the target model has no default drafter, the following small base models are
reasonable starting points for an experiment. A purpose-built drafter generally
performs better.

| Draft model                                        | Use with              |
| -------------------------------------------------- | --------------------- |
| `accounts/fireworks/models/llama-v3p2-1b-instruct` | All Llama models > 3B |
| `accounts/fireworks/models/qwen2p5-0p5b-instruct`  | All Qwen models > 3B  |

Fireworks also supports compatible EAGLE, DFlash, DSpark, and Medusa draft
addons. These formats are architecture-specific and require a checkpoint and
configuration prepared for the exact target model; they are not drop-in
replacements for a small base-model drafter. [Contact
Fireworks](https://fireworks.ai/company/contact-us) to validate an existing
checkpoint or discuss a drafter adapted to your traffic.

## Examples

<Tabs>
  <Tab title="Draft model">
    Create a deployment with an explicit small base-model drafter:

    ```bash theme={null}
    firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
      --draft-model="accounts/fireworks/models/llama-v3p2-1b-instruct" \
      --draft-token-count=4
    ```
  </Tab>

  <Tab title="N-gram speculation">
    Use N-gram speculation without a separate draft model:

    ```bash theme={null}
    firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
      --ngram-speculation-length=3 \
      --draft-token-count=4
    ```
  </Tab>
</Tabs>

You can change the explicit drafter and draft-token count on an existing
deployment:

```bash theme={null}
firectl deployment update <DEPLOYMENT_ID> \
  --draft-model="accounts/<ACCOUNT_ID>/models/<DRAFT_MODEL_ID>" \
  --draft-token-count=4
```

## Benchmark and tune

Compare at least three configurations on the same target model and deployment
shape:

1. The inherited Fireworks default.
2. Your candidate drafter or N-gram settings.
3. A deployment created with `--disable-speculative-decoding`.

Use production-like prompts, output lengths, sampling parameters, and
concurrency. Measure time to first token, inter-token latency, p50/p95 request
latency, and maximum sustainable throughput. A high acceptance rate alone does
not guarantee a speedup because the drafter also consumes compute.

To inspect per-request metrics, set `perf_metrics_in_response` to `true` in the
completion request. For dedicated deployments, the final response or final
streaming chunk includes:

* `speculation-generated-tokens`: number of tokens generated through speculation
* `speculation-acceptance`: acceptance rate by proposed-token position

Acceptance normally falls at later positions. Increase `--draft-token-count`
only while the additional accepted tokens outweigh the extra drafting and
verification work. Re-run the benchmark when the traffic mix, prompt format,
model, quantization, or deployment shape changes.
