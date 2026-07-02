---
title: "Weighted Training"
source: https://docs.fireworks.ai/fine-tuning/weighted-training
path: fine-tuning/weighted-training
---

Control which samples have greater influence during RFT training

Weighted training lets you assign different importance levels to samples in your dataset, giving you control over how your model learns. This is useful when some examples are higher quality, more representative, or more important to your use case than others.

## How it works

During training, each sample's loss is multiplied by its weight before being used to update model parameters. Higher weights mean stronger learning signals—the model pays more attention to these examples. Lower weights (including negative) reduce or reverse a sample's influence.

## Dataset format

Add a `weight` field at the root level of each JSON object in your JSONL dataset:

```json theme={null}
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is 2 + 2?"},
    {"role": "assistant", "content": "4"}
  ],
  "weight": 2.0
}
```

### Weight values

The `weight` field accepts any floating-point number:

| Weight      | Effect                                                  |
| ----------- | ------------------------------------------------------- |
| `> 1.0`     | Increased importance—model learns more from this sample |
| `1.0`       | Default behavior (same as omitting weight)              |
| `0.0 - 1.0` | Reduced importance—sample has less influence            |
| `0.0`       | Sample is effectively ignored during training           |
| `< 0.0`     | Negative weight—reverses the learning signal            |

<Warning>
  If you use weights, the `weight` field must be present in **all samples** in your dataset. Mixing weighted and unweighted samples is not supported.
</Warning>

## Use cases

### Upweight high-quality examples

When you have samples of varying quality, give more weight to your best examples:

```json theme={null}
{"messages": [...], "weight": 2.0}
{"messages": [...], "weight": 1.0}
{"messages": [...], "weight": 0.5}
```

### Balance dataset distribution

If certain prompt types are underrepresented, upweight them to ensure the model learns them well:

```json theme={null}
{"messages": [...], "weight": 3.0}
{"messages": [...], "weight": 1.0}
```

### De-emphasize noisy samples

If you have samples that may contain noise but can't easily be filtered, reduce their weight:

```json theme={null}
{"messages": [...], "weight": 0.3}
```

## Message filtering

For multi-turn conversations, you can also control which assistant messages to include in training by adding a `weight` field to individual messages. This uses a binary format following the [OpenAI fine-tuning specification](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input#fine_tuning-chat_input-messages-assistant_message-weight).

```json theme={null}
{
  "messages": [
    {"role": "user", "content": "What's the capital of France?"},
    {"role": "assistant", "content": "Paris.", "weight": 1},
    {"role": "user", "content": "What about Germany?"},
    {"role": "assistant", "content": "Berlin.", "weight": 0}
  ]
}
```

Message-level weights only accept `0` or `1`:

* `1`: Include this assistant message in training (default)
* `0`: Exclude this assistant message from training

<Note>
  Message-level weights are for **filtering** which turns to train on, not for adjusting training influence. Use sample-level weights (at the root of the JSON object) for weighted importance.
</Note>

## Example dataset

Here's a complete example of a weighted RFT dataset:

```jsonl dataset.jsonl theme={null}
{"messages": [{"role": "system", "content": "You are a math tutor."}, {"role": "user", "content": "What is 15 * 3?"}, {"role": "assistant", "content": "15 * 3 = 45"}], "weight": 1.0}
{"messages": [{"role": "system", "content": "You are a math tutor."}, {"role": "user", "content": "Solve: 2x + 5 = 15"}, {"role": "assistant", "content": "x = 5"}], "weight": 1.5}
{"messages": [{"role": "system", "content": "You are a math tutor."}, {"role": "user", "content": "Integrate x^2 dx"}, {"role": "assistant", "content": "(x^3)/3 + C"}], "weight": 2.0}
```

This dataset upweights more complex math problems, so the model focuses more on calculus than basic arithmetic.
