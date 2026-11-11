---
title: "Thinking history in training"
source: https://docs.fireworks.ai/fine-tuning/thinking-history
path: fine-tuning/thinking-history
---

Choose how reasoning from earlier turns appears in Fireworks training data, with the thinking_trace_history_mode recipe setting, so a fine-tuned thinking model matches how you serve it.

Thinking models can store an assistant turn's reasoning in `reasoning_content`. A thinking-history mode controls whether that existing reasoning remains visible in the context of later turns.

This setting does **not** enable or disable thinking generation. It only controls how reasoning already present in the dataset is rendered. Thinking enablement, context-length splitting, and truncation are separate concerns.

## Interleaved and Preserved

* **Interleaved** removes thinking across user-turn boundaries while retaining the complete assistant → tool → assistant trajectory for the current user turn.
* **Preserved** retains thinking across user turns.

These names align with the serving API's `reasoning_history="interleaved"` and `reasoning_history="preserved"` behaviors. Choose the mode that matches how you will replay reasoning history when serving the trained model.

> [!WARNING]
>
> Do not interpret Interleaved as "keep only the final assistant's thinking." The boundary is the last real user query. If one user turn contains an assistant tool call, a tool result, and another assistant response, thinking from both assistant messages stays in that turn's trajectory.

## Model capabilities

Models expose one of four capability shapes:

* **Selectable:** you can choose Interleaved or Preserved.
* **Fixed Interleaved:** only Interleaved is supported.
* **Fixed Preserved:** only Preserved is supported.
* **Automatic:** neither explicit mode describes the model-native behavior; the renderer selects behavior from each dataset row's input shape.

| Base model | Available modes | Default | Interleaved boundary | SFT datums |
| - | - | - | - | - |
| GLM 5.1 | Interleaved, Preserved | Interleaved | Last real user query; keeps the complete current assistant/tool trajectory | Both modes unroll per user turn |
| GLM 5.2 | Interleaved, Preserved | Interleaved | Same as GLM 5.1 | Interleaved unrolls; Preserved keeps one complete datum |
| GLM 5.3 and GLM 5.3 Flash | Interleaved, Preserved | Preserved | Same as GLM 5.1 | Interleaved unrolls; Preserved keeps one complete datum |
| Qwen 3.5 | Interleaved only | Interleaved | Last real user query; tool results do not reset the boundary | Unrolls per user turn |
| Qwen 3.6 | Interleaved, Preserved | Interleaved | Same as Qwen 3.5 | Interleaved unrolls; Preserved keeps one complete datum |
| Qwen 3.8 27B | Interleaved, Preserved | Preserved | Same as Qwen 3.5 | Interleaved unrolls; Preserved keeps one complete datum |
| Kimi K2.5 | Interleaved only | Interleaved | Keeps thinking in the trailing/current assistant-tool trajectory | Unrolls per user turn |
| Kimi K2.6 | Interleaved, Preserved | Interleaved | Same as Kimi K2.5 | Interleaved unrolls; Preserved keeps one complete datum |
| Kimi K2.7 Code | Preserved only | Preserved | Not applicable | Keeps one complete datum |
| Nemotron 3 Nano, Super, and Ultra; Nemotron 3.5 Lightning | Interleaved, Preserved | Interleaved | Last real user query | Interleaved unrolls; Preserved keeps one complete datum |
| DeepSeek V4 Flash and Pro | Automatic only; no mode toggle | Automatic | Depends on whether the row declares tools | Without tools, unrolls; with declared tools, keeps one complete datum |

Base models not listed above keep their default renderer behavior and do not offer a thinking-history choice.

### GLM 5.1, 5.2, and 5.3

All three expose the upstream `clear_thinking` template control. Fireworks maps Interleaved to `clear_thinking=true` and Preserved to `clear_thinking=false`. GLM 5.1 and 5.2 default to Interleaved, GLM 5.3 defaults to Preserved (see below), and all three use the last real user query as the clearing boundary.

The difference is in Preserved mode:

* **GLM 5.1 still unrolls.** Its official template can change an earlier assistant turn's rendered think wrapper after a later assistant message is appended. The previously rendered sequence is therefore not always a prefix of the longer conversation.
* **GLM 5.2 keeps one complete datum.** Its Preserved rendering is prefix-stable: appending a later turn does not rewrite tokens already rendered for earlier turns.

GLM 5.1 unrolling does not remove preserved reasoning. It creates one training datum per user turn so that every target is rendered with the correct template context.

**GLM 5.3 and GLM 5.3 Flash** default to Preserved, because their template defaults to `clear_thinking=false`. Preserved keeps one complete datum, and Interleaved unrolls.

### Qwen 3.5, 3.6, and 3.8

All three use the same Interleaved boundary: the last real user query, not the last assistant response. In a user → assistant tool call → tool result → assistant response trajectory, thinking from both assistant messages is retained.

* **Qwen 3.5** has no supported history toggle and is fixed to Interleaved.
* **Qwen 3.6** adds the upstream `preserve_thinking` control. Fireworks maps Interleaved to `preserve_thinking=false` and Preserved to `preserve_thinking=true`. Preserved is prefix-stable and stays one complete datum.
* **Qwen 3.8 27B** offers both modes and defaults to Preserved, which stays one complete datum. Interleaved unrolls.

For byte-level parity with the official Qwen 3.6 template, Preserved mode can emit an empty think wrapper for a historical assistant message that has no `reasoning_content`. This does not synthesize reasoning; it preserves the template's exact structure.

### Kimi K2.5 compared with Kimi K2.6 and K2.7 Code

* **Kimi K2.5** is fixed to Interleaved and unrolls per user turn.
* **Kimi K2.6** adds the upstream `preserve_thinking` control. Fireworks maps Interleaved to `preserve_thinking=false` and Preserved to `preserve_thinking=true`; Preserved stays one complete datum.
* **Kimi K2.7 Code** is fixed to Preserved and stays one complete datum.

### DeepSeek V4 automatic behavior

DeepSeek V4 Flash and Pro do not expose an Interleaved/Preserved toggle. Leave `thinking_trace_history_mode` empty.

The model-native renderer makes a deterministic choice for each row:

* A row without declared tools removes thinking across user turns and unrolls per user turn.
* A row with declared tools preserves thinking and remains one complete datum.

This is determined by the row's input shape, not chosen autonomously or stochastically by the model.

## Why some modes unroll

The SFT recipe trains every assistant message by default. When a renderer removes historical thinking, the recipe unrolls the conversation at **user boundaries** so every assistant response gets one opportunity to be the current target. DPO and ORPO do not unroll: each side of a preference pair is rendered as one datum.

Consider this conversation:

```text theme={null}
U1
A1 (thinking 1, final answer)

U2
A2 (thinking 2, tool call)
Tool result
A3 (thinking 3, final answer)
```

For an Interleaved renderer that unrolls, the recipe produces:

* Datum 0 trains A1.
* Datum 1 removes thinking 1 from the historical context and trains A2 and A3 together. Thinking 2 and thinking 3 both remain because they belong to the same user turn.

For a prefix-stable Preserved renderer, the row remains one datum and thinking 1, 2, and 3 all remain. GLM 5.1 is the exception: its Preserved renderer keeps the reasoning but still unrolls because of its template's prefix behavior.

Because unrolled datums duplicate conversation context, the tuned token count can exceed the raw dataset token count. Unrolling is independent of context-length truncation or splitting.

## Set the mode

The SFT, DPO, and ORPO recipes take the mode as `thinking_trace_history_mode`:

```python theme={null}
cfg = Config(
    # ... other fields ...
    thinking_trace_history_mode="preserved",
)
```

* `""` (the default): load the model's original renderer. For Qwen 3.5, Qwen 3.6, Kimi K2.5, Kimi K2.6, Kimi K2.7 Code, GLM 5.1, and GLM 5.2, that renderer doesn't fully match the behavior on this page, so set the mode explicitly. For DeepSeek V4 and models not in the table, leave it empty.
* `"interleaved"`: request Interleaved.
* `"preserved"`: request Preserved.

A mode the model doesn't support fails when the recipe starts, before any training. Models not in the table accept only the empty value.

## Check what the trainer sees

In the SFT recipe, set `render_samples_file` to write rendered examples to a JSONL file, with one record per datum, so you can see where a conversation unrolls and which tokens are trained. See "Check tokenization" in [Cookbook: Supervised Fine-Tuning](/fine-tuning/training-api/cookbook/sft).

## Existing managed jobs

Managed SFT, DPO, and ORPO jobs, which no longer accept new jobs, store this setting in the `thinkingTraceHistoryMode` field: `THINKING_TRACE_HISTORY_MODE_UNSPECIFIED` (the model default), `THINKING_TRACE_HISTORY_MODE_INTERLEAVED`, or `THINKING_TRACE_HISTORY_MODE_PRESERVED`. To train the same way on the Training API, set `thinking_trace_history_mode` from that field: `"interleaved"` or `"preserved"` for an explicit mode. For `UNSPECIFIED`, managed training used the Default column in the table above, so set that mode explicitly. For DeepSeek V4 or a model not in the table, leave it empty. See [Migrate from Managed Training](/fine-tuning/migrate-from-managed-training).

## How Fireworks verifies model behavior

Fireworks treats the official model chat template as the behavior baseline and manually onboards supported model families. Capability is not inferred dynamically from arbitrary template text.

Renderer tests pin upstream Hugging Face template revisions and verify token-for-token parity for single-turn, multi-turn, and tool-trajectory inputs. A shared regression fixture verifies all of the following:

* Interleaved clears thinking before the last real user query.
* Every assistant message after that query remains, including multiple assistants around a tool result.
* Preserved retains every thinking trace.
* Each renderer's prefix behavior produces the documented datum count.

The relevant upstream templates are [GLM 5.1](https://huggingface.co/zai-org/GLM-5.1/blob/main/chat_template.jinja), [GLM 5.2](https://huggingface.co/zai-org/GLM-5.2/blob/main/chat_template.jinja), [Qwen 3.5](https://huggingface.co/Qwen/Qwen3.5-35B-A3B/blob/main/tokenizer_config.json), [Qwen 3.6](https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/tokenizer_config.json), [Kimi K2.5](https://huggingface.co/moonshotai/Kimi-K2.5/blob/main/chat_template.jinja), [Kimi K2.6](https://huggingface.co/moonshotai/Kimi-K2.6/blob/main/chat_template.jinja), and [Kimi K2.7 Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/main/chat_template.jinja).

> [card] [Prepare an SFT dataset](/fine-tuning/training-api/cookbook/sft#dataset-format)
>
> Add `reasoning_content` to assistant messages in your JSONL dataset.
