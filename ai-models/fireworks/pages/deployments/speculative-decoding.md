---
title: "Speculative Decoding"
source: https://docs.fireworks.ai/deployments/speculative-decoding
path: deployments/speculative-decoding
---

Speed up generation with draft models and n-gram speculation

Speed up text generation by using a smaller "draft" model to assist the main model, or using n-gram based speculation.

## Default drafters

<Tip>
  **For most deployments, a default drafter is already attached automatically**, so you don't need to configure a draft model yourself to benefit from speculative decoding.

  For further optimized throughput, [reach out to us](https://fireworks.ai/company/contact-us) about a custom speculative decoding model adapted to your traffic pattern.
</Tip>

<Note>
  Speculative decoding may slow down output generation if the draft model is not a good speculator, or if token count/speculation length is too high or too low. It may also reduce max throughput. Test different models and speculation lengths for your use case.
</Note>

## Configuration options

| Flag                         | Type   | Description                                                                                 |
| ---------------------------- | ------ | ------------------------------------------------------------------------------------------- |
| `--draft-model`              | string | Draft model name. Can be a Fireworks model or custom model. See recommendations below.      |
| `--draft-token-count`        | int32  | Tokens to generate per step. Required when using draft model or n-gram. Typically set to 4. |
| `--ngram-speculation-length` | int32  | Alternative to draft model: uses N-gram based speculation from previous input.              |

<Note>
  `--draft-model` and `--ngram-speculation-length` cannot be used together.
</Note>

## Custom draft models

While you can specify a custom draft model with `--draft-model`, we recommend only setting a **small base model** as the drafter when using this setting. Other speculative decoding methods such as DFlash, EAGLE, and Medusa require specific configurations. If you need to set one of those up, [reach out to us](https://fireworks.ai/company/contact-us) and we'll help you configure it.

### Fallback draft models

If a default drafter isn't attached and you'd like a starting point, these small base models can be used as fallback drafters. Note that using a base model as a drafter is generally not ideal.

| Draft model                                        | Use with              |
| -------------------------------------------------- | --------------------- |
| `accounts/fireworks/models/llama-v3p2-1b-instruct` | All Llama models > 3B |
| `accounts/fireworks/models/qwen2p5-0p5b-instruct`  | All Qwen models > 3B  |

## Examples

<Tabs>
  <Tab title="Draft model">
    Use a smaller model to speed up generation:

    ```bash theme={null}
    firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
      --draft-model="accounts/fireworks/models/llama-v3p2-1b-instruct" \
      --draft-token-count=4
    ```
  </Tab>

  <Tab title="N-gram speculation">
    Use input history for speculation (no draft model needed):

    ```bash theme={null}
    firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
      --ngram-speculation-length=3 \
      --draft-token-count=4
    ```
  </Tab>
</Tabs>

<Tip>
  Fireworks also supports [Predicted Outputs](/guides/predicted-outputs) which works in addition to model-based speculative decoding.
</Tip>
