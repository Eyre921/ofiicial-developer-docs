---
title: "Pricing"
source: https://docs.together.ai/docs/fine-tuning/pricing
path: docs/fine-tuning/pricing
---

Fine-tuning is billed per token processed, scaled by model size, training method, and training type.

Together AI bills fine-tuning by the total number of tokens processed across training and validation. The per-token rate depends on three factors: the model size bracket, the training method (supervised or DPO), and the training type (LoRA or full fine-tuning). For current rates, see the [together.ai/pricing](https://www.together.ai/pricing#fine-tuning).

After training, hosting on a [dedicated endpoint](/docs/fine-tuning/deployment) is billed separately by the minute.

## How tokens are counted

The total tokens processed in a job is equal to:

```text theme={null}
total_tokens = (n_epochs × tokens_per_training_dataset) + (n_evals × tokens_per_validation_dataset)
```

Tokenization occurs shortly after the job starts. Your final token count and price are calculated and recorded after tokenization completes, after which they appear on the [fine-tuning jobs dashboard](https://api.together.ai/jobs) and in `client.fine_tuning.retrieve(id=<JOB_ID>)`.

If you disable [packing](/reference/post-fine-tunes#body-packing), training tokens are computed as `dataset_length` × [`max_seq_length`](/reference/post-fine-tunes#body-max-seq-length) instead.

## Estimate job cost

There are three ways to estimate the cost of a fine-tuning job before launching it:

1. **CLI**: When you submit a job with [`tg fine-tuning create`](/reference/cli/finetune#create), the CLI prints the estimated price and asks for confirmation before the job is submitted.
2. **Web interface**: On the [new fine-tuning job page](https://api.together.ai/fine-tuning/new), the estimate appears once you select a model and dataset.
3. **API/SDK**: Call the [estimate price endpoint](/reference/post-fine-tunes-estimate-price) with the same parameters you plan to submit to the create job endpoint. The response includes the estimated total price, the estimated training and evaluation token counts, your credit limit, and whether you are allowed to proceed:

<CodeGroup>
  ```python Python theme={null}
  import os

  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  estimate = client.fine_tuning.estimate_price(
      training_file="file-abc123",
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      n_epochs=3,
      training_method={"method": "sft"},
      training_type={"type": "Lora", "lora_r": 8},
  )

  print(estimate)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together({ apiKey: process.env.TOGETHER_API_KEY });

  const estimate = await client.fineTuning.estimatePrice({
    training_file: "file-abc123",
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    n_epochs: 3,
    training_method: { method: "sft" },
    training_type: { type: "Lora", lora_r: 8 },
  });

  console.log(estimate);
  ```
</CodeGroup>

<Note>
  The cost estimate is only available after your input datasets pass [server-side validation](/docs/fine-tuning/data-preparation#wait-for-server-side-validation).
</Note>

## Cancelled and early-stopped jobs

When a running job is cancelled or [stopped early](/docs/fine-tuning/early-stopping), you pay for completed steps only. To check how many steps a job completed, retrieve it and read `steps_completed`:

```bash theme={null}
tg fine-tuning retrieve <job-id> --json | jq '.steps_completed'
```

## Failed jobs

If a job fails, for example due to an invalid input or an internal Together AI-side error, all charges are fully refunded, including any completed steps.

## Minimum spend

Fine-tuning jobs have a \$4.00 minimum charge. Some models are exempt. See [fine-tuning pricing](https://www.together.ai/pricing#fine-tuning) for the current rates and exceptions.

## Hosting charges

After training, your fine-tuned model can be served on a dedicated endpoint that bills per minute based on the hardware attached. These charges are separate from your fine-tuning job cost and continue until you stop or delete the endpoint. See [deployment](/docs/fine-tuning/deployment) for the full setup and teardown flow.
