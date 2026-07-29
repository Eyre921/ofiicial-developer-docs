---
title: "Preference fine-tuning"
source: https://docs.together.ai/docs/fine-tuning/preference-tuning
path: docs/fine-tuning/preference-tuning
---

Align a model with paired preferred and dispreferred responses using DPO.

Preference fine-tuning trains a model on paired examples that show which responses you want it to generate and which it should avoid. Together AI implements this with [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290). This is more effective than supervised fine-tuning when you have ranked outputs for the same prompt.

## When to use preference tuning

Consider using preference tuning when:

* **You have ranked pairs of responses for the same prompt.** Standard supervised fine-tuning (SFT) only learns from a single target completion per example. DPO learns from the gap between good and bad (preferred and dispreferred) responses.
* **You're polishing a model that already works.** DPO is most effective as a refinement step. If your data is far from the base model's pretraining distribution, run SFT first and continue with DPO from that checkpoint (see [Combine SFT and DPO](#combine-sft-and-dpo)).
* **You want to reduce specific failure modes.** Pair the failure as `non_preferred_output` against the desired behavior.

Skip DPO if your dataset is single-target. Use [supervised fine-tuning](/docs/fine-tuning/supervised) instead.

## Prepare your data

Each line in the JSONL file carries:

* `input.messages`: the context, in [conversational format](/docs/fine-tuning/data-preparation#conversational-data).
* `preferred_output`: a list containing exactly one assistant message representing the ideal response.
* `non_preferred_output`: a list containing exactly one assistant message representing the suboptimal response.

```json theme={null}
{
  "input": {
    "messages": [
      {"role": "assistant", "content": "Hello, how can I assist you today?"},
      {"role": "user", "content": "Can you tell me about the rise of the Roman Empire?"}
    ]
  },
  "preferred_output": [
    {"role": "assistant", "content": "The Roman Empire rose from a small city-state founded in 753 BCE. Through military conquests and strategic alliances, Rome expanded across the Italian peninsula. After the Punic Wars, it grew even stronger, and in 27 BCE, Augustus became the first emperor, marking the start of the Roman Empire."}
  ],
  "non_preferred_output": [
    {"role": "assistant", "content": "The Roman Empire rose due to military strength and strategic alliances."}
  ]
}
```

<Warning>
  Each output must contain exactly one assistant message. Preference tuning does not support pre-tokenized Parquet datasets. [Contact us](https://www.together.ai/contact) if you need this feature.
</Warning>

For tool-calling preference data, see [data preparation](/docs/fine-tuning/data-preparation#tool-calling-data). For reasoning preference data, see [reasoning preference format](/docs/fine-tuning/data-preparation#reasoning-data).

## Launch a DPO job

Set `training_method` to `"dpo"`. The full list of DPO parameters lives in the [API reference](/reference/post-fine-tunes).

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "meta-llama/Llama-3.2-3B-Instruct" \
    --lora \
    --training-method "dpo" \
    --dpo-beta 0.2
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="meta-llama/Llama-3.2-3B-Instruct",
      lora=True,
      training_method="dpo",
      dpo_beta=0.2,
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "meta-llama/Llama-3.2-3B-Instruct",
    lora: true,
    training_method: "dpo",
    dpo_beta: 0.2,
  });
  console.log(job.id);
  ```
</CodeGroup>

## DPO parameters

| Parameter                           | Type  | Default | Description                                                                                                                                                                                                                                   |
| ----------------------------------- | ----- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dpo_beta`                          | float | `0.1`   | How far the model is allowed to drift from the reference model. Lower values (around `0.1`) update more aggressively toward the preferred output; higher values (around `0.7`) stay closer to the reference. Useful range is `0.05` to `0.9`. |
| `dpo_normalize_logratios_by_length` | bool  | `false` | Normalize log ratios by sample length during loss calculation.                                                                                                                                                                                |
| `dpo_reference_free`                | bool  | `false` | Train without a reference model. When enabled, the loss skips the reference model's log probabilities instead of penalizing drift from it.                                                                                                    |
| `rpo_alpha`                         | float | `0.0`   | Incorporate the NLL loss on selected samples with this weight.                                                                                                                                                                                |
| `simpo_gamma`                       | float | `0.0`   | Add a margin to the loss, force-enable length normalization, and exclude reference logits. Matches the [SimPO](https://arxiv.org/pdf/2405.14734) loss.                                                                                        |

<Note>
  For [LoRA long-context fine-tuning](/docs/fine-tuning/supported-models), half the context length is used for the preferred response and half for the non-preferred response. On a 32k model, effective context per side is 16k. Preference tuning ignores the `train_on_inputs` flag because the loss is computed from the preferred and non-preferred outputs.
</Note>

To stop a DPO run automatically when validation loss plateaus, see [early stopping](/docs/fine-tuning/early-stopping).

## DPO metrics

Beyond standard training metrics, DPO jobs report:

* **Accuracy:** The share of examples where the reward for the preferred response exceeds the reward for the non-preferred response.
* **KL divergence:** How much the trained model's output distribution has diverged from the reference model's. Higher values mean the trained model has moved further from the reference.
* **Per-side log probabilities:** For both preferred and non-preferred outputs, useful for debugging stalled runs.

For how to retrieve these values during or after a run, see [monitoring a fine-tuning job](/docs/fine-tuning/monitoring#preference-tuning-jobs).

## Combine SFT and DPO

The recommended workflow when your training data differs substantially from the base model's pretraining distribution:

1. Run a [supervised fine-tune](/docs/fine-tuning/supervised) on the concatenation of context and preferred output, using one of the supported [SFT data formats](/docs/fine-tuning/data-preparation).
2. Continue training the resulting checkpoint with DPO. Pass the previous job's checkpoint to `from_checkpoint`:

```python Python theme={null}
job = client.fine_tuning.create(
    training_file="<DPO_FILE_ID>",
    from_checkpoint="<SFT_JOB_ID>",
    training_method="dpo",
    dpo_beta=0.2,
)
```

SFT first followed by DPO usually produces a noticeably better model than DPO alone for out-of-domain tasks.
