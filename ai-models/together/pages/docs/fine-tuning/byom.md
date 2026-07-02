---
title: "Bring your own model"
source: https://docs.together.ai/docs/fine-tuning/byom
path: docs/fine-tuning/byom
---

Fine-tune a Hugging Face model that isn't in the Together catalog.

Together's bring-your-own-model (BYOM) flow lets you fine-tune a model from a Hugging Face repository that isn't in the official catalog, by pairing a base model from Together (the training template) with your custom checkpoint from Hugging Face (the actual weights to tune).

## When to BYOM

Use the BYOM flow when:

* **You want to start from a community variant.** A specialized model on Hugging Face (medical, legal, code) sometimes makes a better starting point than a generic base.
* **You're continuing your own previous work.** Upload your last checkpoint to Hugging Face and resume training on Together.
* **A new model isn't in the catalog yet.** As long as it has a supported architecture under 100B parameters, you can fine-tune it.

## Prerequisites

Your model must meet these constraints:

* **Architecture:** CausalLM only (text generation).
* **Size:** Under 100 billion parameters.
* **Weights:** `.safetensors` format.
* **No custom code:** `trust_remote_code=True` is not allowed.
* **Access:** The Hugging Face repo is public, or you have an API token with read access.
* **Framework compatibility:** Transformers v4.55 or earlier.

You'll also need a Together base model whose architecture matches your custom checkpoint (Llama, Qwen, Mistral, Gemma, etc.) and whose `max_seq_length` is no larger than your checkpoint supports.

## Launch the job

Launch the job by pairing the base model (template) with `from_hf_model` (your checkpoint):

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.create(
      model="togethercomputer/llama-2-7b-chat",  # base template
      from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # your custom model
      training_file="<FILE_ID>",
      n_epochs=3,
      learning_rate=1e-5,
      suffix="custom-v1",
      # hf_api_token="hf_xxxxxxxxxxxx",  # for a private repo
      # hf_model_revision="abc123def456",  # to pin a specific commit
  )
  print(job.id)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.create({
    model: "togethercomputer/llama-2-7b-chat",
    from_hf_model: "HuggingFaceTB/SmolLM2-1.7B-Instruct",
    training_file: "<FILE_ID>",
    n_epochs: 3,
    learning_rate: 1e-5,
    suffix: "custom-v1",
  });
  console.log(job.id);
  ```

  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "togethercomputer/llama-2-7b-chat" \
    --from-hf-model "HuggingFaceTB/SmolLM2-1.7B-Instruct" \
    --n-epochs 3 \
    --learning-rate 1e-5 \
    --suffix "custom-v1"
  ```
</CodeGroup>

| Parameter           | Purpose                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| `model`             | A base model from Together's catalog. Its config provides the training template and inference setup. |
| `from_hf_model`     | The Hugging Face repo with your custom weights.                                                      |
| `hf_api_token`      | Only needed for private repos. Omit for public ones. Passing a dummy value can cause a 400 error.    |
| `hf_model_revision` | Optional. Pin to a specific commit hash instead of `main`.                                           |

## Pick the base template

Match these three variables to pick the base template:

* **Architecture:** Must match (treat Code Llama as Llama, etc.).
* **Size:** As close to your custom checkpoint as the catalog allows. If every option is larger, pick the smallest.
* **Max sequence length:** The base's max must be at least as large as your checkpoint's; ideally not much larger.

For example: `HuggingFaceTB/SmolLM2-135M-Instruct` has Llama architecture, 135M parameters, and an 8k context. The closest Llama in the catalog by parameter count is `meta-llama/Llama-3.2-1B-Instruct`, but its max context is 131k, much higher than the checkpoint supports. A better choice is `togethercomputer/llama-2-7b-chat`: larger than your checkpoint, but the max sequence length fits.

## Watch and deploy

BYOM jobs use the same lifecycle as catalog jobs:

* [Poll the job](/docs/fine-tuning/monitoring#poll-until-the-job-is-done) with the SDK or CLI.
* Deploy the result on a [dedicated endpoint](/docs/fine-tuning/deployment). Your fine-tuned model appears under **My Models** in the [dashboard](https://api.together.ai/models) once training completes.

The base model dictates which hardware can host the result. If `client.endpoints.list_hardware(model=<base>)` returns 404, the base can't be deployed; pick a different one before training.

## Troubleshooting

* **Training failed with CUDA OOM:** Reduce `batch_size` or use a smaller base template.
* **Training failed with a checkpoint validation error:** The architecture doesn't match the base template or a parameter is out of range. Confirm the checkpoint is CausalLM and verify its `config.json` against the base.
* **Training failed with a runtime error:** Likely a corrupted or incomplete checkpoint. Re-upload to Hugging Face.
* **Model uses `trust_remote_code`:** Not supported. Use a similar model that doesn't, or [contact support](https://www.together.ai/contact) to add it to the catalog.
* **Internal errors:** The platform notifies our team automatically. If the issue persists, contact support with the job ID.

## FAQ

**Can I fine-tune a LoRA adapter?**

Yes. The platform merges the adapter with the base during training, producing a full checkpoint rather than a separate adapter.

**Can I train a model I uploaded for dedicated inference?**

No. Models uploaded with [custom-models](/docs/dedicated-endpoints/custom-models) are not visible to the fine-tuning API. Upload to Hugging Face instead and reference the repo as `from_hf_model`.

**Will my fine-tuned model work for inference?**

Yes, when the base you specified is supported, the architecture matches, and training completes successfully. Models built on unsupported architectures may not run reliably; [contact support](https://www.together.ai/contact) if you need that.
