---
title: "Thinking history in fine-tuning"
source: https://docs.fireworks.ai/fine-tuning/thinking-history
path: fine-tuning/thinking-history
---

Choose how historical reasoning is rendered for managed fine-tuning and match training behavior to inference.

Thinking models can store an assistant turn's reasoning in `reasoning_content`. A thinking-history mode controls whether that existing reasoning remains visible in the context of later turns.

This setting does **not** enable or disable thinking generation. It only controls how reasoning already present in the dataset is rendered. Thinking enablement, context-length splitting, and truncation are separate concerns.

## Interleaved and Preserved

* **Interleaved** removes thinking across user-turn boundaries while retaining the complete assistant → tool → assistant trajectory for the current user turn.
* **Preserved** retains thinking across user turns.

These names align with the serving API's `reasoning_history="interleaved"` and `reasoning_history="preserved"` behaviors. Choose the mode that matches how you will replay reasoning history when serving the fine-tuned model.

<Warning>
  Do not interpret Interleaved as "keep only the final assistant's thinking." The boundary is the last real user query. If one user turn contains an assistant tool call, a tool result, and another assistant response, thinking from both assistant messages stays in that turn's trajectory.
</Warning>

## Model capabilities

Models expose one of four capability shapes:

* **Selectable:** the job can explicitly select Interleaved or Preserved.
* **Fixed Interleaved:** only Interleaved is supported.
* **Fixed Preserved:** only Preserved is supported.
* **Automatic:** neither explicit mode describes the model-native behavior; the renderer selects behavior from each dataset row's input shape.

| Base model                | Available modes                | Default                   | Interleaved boundary                                                       | Managed SFT datums                                                    |
| ------------------------- | ------------------------------ | ------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| GLM 5.1                   | Interleaved, Preserved         | Interleaved               | Last real user query; keeps the complete current assistant/tool trajectory | Both modes unroll per user turn                                       |
| GLM 5.2                   | Interleaved, Preserved         | Interleaved               | Same as GLM 5.1                                                            | Interleaved unrolls; Preserved keeps one complete datum               |
| Qwen 3.5                  | Interleaved only               | Interleaved               | Last real user query; tool results do not reset the boundary               | Unrolls per user turn                                                 |
| Qwen 3.6                  | Interleaved, Preserved         | Interleaved               | Same as Qwen 3.5                                                           | Interleaved unrolls; Preserved keeps one complete datum               |
| Kimi K2.5                 | Interleaved only               | Interleaved               | Keeps thinking in the trailing/current assistant-tool trajectory           | Unrolls per user turn                                                 |
| Kimi K2.6                 | Interleaved, Preserved         | Interleaved               | Same as Kimi K2.5                                                          | Interleaved unrolls; Preserved keeps one complete datum               |
| Kimi K2.7 Code            | Preserved only                 | Preserved                 | Not applicable                                                             | Keeps one complete datum                                              |
| DeepSeek V4 Flash and Pro | Automatic only; no mode toggle | Automatic (`UNSPECIFIED`) | Depends on whether the row declares tools                                  | Without tools, unrolls; with declared tools, keeps one complete datum |

Base models not listed above keep their existing model-default renderer behavior and do not expose an explicit thinking-history choice.

### GLM 5.1 compared with GLM 5.2

Both versions expose the upstream `clear_thinking` template control. Fireworks maps Interleaved to `clear_thinking=true` and Preserved to `clear_thinking=false`. Both default to Interleaved, and both use the last real user query as the clearing boundary.

The difference is in Preserved mode:

* **GLM 5.1 still unrolls.** Its official template can change an earlier assistant turn's rendered think wrapper after a later assistant message is appended. The previously rendered sequence is therefore not always a prefix of the longer conversation.
* **GLM 5.2 keeps one complete datum.** Its Preserved rendering is prefix-stable: appending a later turn does not rewrite tokens already rendered for earlier turns.

GLM 5.1 unrolling does not remove preserved reasoning. It creates one training datum per user turn so that every target is rendered with the correct template context.

### Qwen 3.5 compared with Qwen 3.6

Both versions use the same Interleaved boundary: the last real user query, not the last assistant response. In a user → assistant tool call → tool result → assistant response trajectory, thinking from both assistant messages is retained.

* **Qwen 3.5** has no supported history toggle and is fixed to Interleaved.
* **Qwen 3.6** adds the upstream `preserve_thinking` control. Fireworks maps Interleaved to `preserve_thinking=false` and Preserved to `preserve_thinking=true`. Preserved is prefix-stable and stays one complete datum.

For byte-level parity with the official Qwen 3.6 template, Preserved mode can emit an empty think wrapper for a historical assistant message that has no `reasoning_content`. This does not synthesize reasoning; it preserves the template's exact structure.

### Kimi K2.5 compared with Kimi K2.6 and K2.7 Code

* **Kimi K2.5** is fixed to Interleaved and unrolls per user turn.
* **Kimi K2.6** adds the upstream `preserve_thinking` control. Fireworks maps Interleaved to `preserve_thinking=false` and Preserved to `preserve_thinking=true`; Preserved stays one complete datum.
* **Kimi K2.7 Code** is fixed to Preserved and stays one complete datum.

### DeepSeek V4 automatic behavior

DeepSeek V4 Flash and Pro do not expose an Interleaved/Preserved toggle. Leave the job field omitted or `UNSPECIFIED`.

The model-native renderer makes a deterministic choice for each row:

* A row without declared tools removes thinking across user turns and unrolls per user turn.
* A row with declared tools preserves thinking and remains one complete datum.

This is determined by the row's input shape, not chosen autonomously or stochastically by the model. Render-preview clients should display one read-only automatic option.

## Why some modes unroll

Managed SFT trains all assistant messages. When a renderer removes historical thinking, Fireworks unrolls the conversation at **user boundaries** so every assistant response gets one opportunity to be the current target.

Consider this conversation:

```text theme={null}
U1
A1 (thinking 1, final answer)

U2
A2 (thinking 2, tool call)
Tool result
A3 (thinking 3, final answer)
```

For an Interleaved renderer that unrolls, Fireworks produces:

* Datum 0 trains A1.
* Datum 1 removes thinking 1 from the historical context and trains A2 and A3 together. Thinking 2 and thinking 3 both remain because they belong to the same user turn.

For a prefix-stable Preserved renderer, the row remains one datum and thinking 1, 2, and 3 all remain. GLM 5.1 is the exception: its Preserved renderer keeps the reasoning but still unrolls because of its template's prefix behavior.

Because unrolled datums duplicate conversation context, the tuned token count can exceed the raw dataset token count. Unrolling is independent of context-length truncation or splitting.

## Configure a training job

The optional, immutable REST field is `thinkingTraceHistoryMode`:

* `THINKING_TRACE_HISTORY_MODE_UNSPECIFIED`: use the registered model's default behavior. For an unregistered model, keep its existing renderer fallback.
* `THINKING_TRACE_HISTORY_MODE_INTERLEAVED`: explicitly request Interleaved when supported.
* `THINKING_TRACE_HISTORY_MODE_PRESERVED`: explicitly request Preserved when supported.

`UNSPECIFIED` is the default for clients that omit the field; it is not a third user-selectable history mode.

```json theme={null}
{
  "thinkingTraceHistoryMode": "THINKING_TRACE_HISTORY_MODE_PRESERVED"
}
```

An explicitly requested unsupported mode fails configuration validation before GPU training starts. Managed SFT, DPO, and ORPO use the same field and enum. The unrolling behavior described above applies to managed SFT; RFT does not expose this setting.

## Preview before training

A render-preview request does not select a thinking-history mode. It returns every available option for the base model in `thinkingTraceHistoryModeOptions` and one rendering per option for each example.

* Selectable models return two options for a toggle.
* Fixed and automatic models return one read-only option.
* A rendering can contain multiple `renderedDatums` when that dataset row unrolls.
* Within each datum, concatenate `segments[].text` in order. A `lossWeight` of `0` is masked context; a value greater than `0` is trained.

Select one of the returned modes when creating the training job. After the job starts, use [Render Samples](/fine-tuning/debug-sft-tokenization) to inspect the exact token IDs and loss mask seen by the trainer.

## How Fireworks verifies model behavior

Fireworks treats the official model chat template as the behavior baseline and manually onboards supported model families. Capability is not inferred dynamically from arbitrary template text.

Renderer tests pin upstream Hugging Face template revisions and verify token-for-token parity for single-turn, multi-turn, and tool-trajectory inputs. A shared regression fixture verifies all of the following:

* Interleaved clears thinking before the last real user query.
* Every assistant message after that query remains, including multiple assistants around a tool result.
* Preserved retains every thinking trace.
* Each renderer's prefix behavior produces the documented datum count.

The relevant upstream templates are [GLM 5.1](https://huggingface.co/zai-org/GLM-5.1/blob/main/chat_template.jinja), [GLM 5.2](https://huggingface.co/zai-org/GLM-5.2/blob/main/chat_template.jinja), [Qwen 3.5](https://huggingface.co/Qwen/Qwen3.5-35B-A3B/blob/main/tokenizer_config.json), [Qwen 3.6](https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/tokenizer_config.json), [Kimi K2.5](https://huggingface.co/moonshotai/Kimi-K2.5/blob/main/chat_template.jinja), [Kimi K2.6](https://huggingface.co/moonshotai/Kimi-K2.6/blob/main/chat_template.jinja), and [Kimi K2.7 Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/main/chat_template.jinja).

<Card title="Prepare an SFT dataset" icon="database" href="/fine-tuning/fine-tuning-models">
  Add `reasoning_content` to assistant messages in your JSONL dataset.
</Card>
