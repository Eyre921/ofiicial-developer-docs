---
title: "Cost Estimator"
source: https://docs.fireworks.ai/fine-tuning/rft-cost-estimator
path: fine-tuning/rft-cost-estimator
---

Estimate and optimize the cost of your RFT training jobs

<Tip>
  **Reinforcement Fine-Tuning (RFT)** is free for models under 16B parameters. When creating an RFT job in the UI, filter for free tuning models in the model selection area on the [fine-tuning creation page](https://app.fireworks.ai/dashboard/fine-tuning/create). If kicking off jobs from the terminal, you can find the model ID from the [Model Library](https://app.fireworks.ai/models?filter=LLM\&tunable=true). Note: SFT and DPO jobs are billed per training token for all model sizes—see the [pricing page](https://fireworks.ai/pricing) for details.
</Tip>

## Interactive cost calculator

Select your model and training configuration to get an instant cost estimate. The calculator uses the following formulas:

1. **Total tokens**: Prompts × Epochs × Response candidates × (Max tokens × 0.6)
2. **GPU hours**: (Total tokens ÷ 1M) × (GPU hours per million tokens range, varies by model size)
3. **Cost**: GPU hours × GPU rate per hour

You can derive wall-clock training time from the estimate as: **Training time = GPU hours ÷ Number of GPUs**.

The GPU hours per million tokens range varies by model size and accounts for variability in model efficiency, system overhead, and actual response lengths. Ranges are based on actual RFT job data.

<Warning>
  **Order-of-magnitude estimates only.** This calculator provides estimates and is not intended for real forecasting or budgeting. Actual costs may vary significantly.
</Warning>

<RftCostCalculator />

## How RFT pricing works

Reinforcement fine-tuning jobs are billed based on **GPU-seconds** consumed during training. The total cost depends on three main factors:

1. **Model size** — Determines how many GPUs are needed and the per-GPU-hour rate
2. **Training dataset** — How much data is processed (dataset size × epochs × rollouts)
3. **Rollout generation** — Token generation during training (max tokens × rollouts per prompt)

## Cost formula

The approximate cost of an RFT job can be estimated as:

$$
\text{Cost} = \text{GPU-hours} \times \text{Price per GPU-hour}
$$

Where GPU-hours depend on:

$$
\text{GPU-hours} \approx \text{Num GPUs} \times \left(\frac{\text{Prompts} \times \text{Epochs} \times \text{Rollouts (n)} \times \text{Avg tokens per rollout}}{\text{Throughput (tokens/sec)}}\right) \div 3600
$$

The key variables are:

| Variable                    | Description                    | How to control                      |
| --------------------------- | ------------------------------ | ----------------------------------- |
| **Num GPUs**                | GPUs required for the model    | Determined by model size            |
| **Prompts**                 | Number of rows in your dataset | Your dataset size                   |
| **Epochs**                  | Passes through the dataset     | `--epochs` flag (default: 1)        |
| **Response candidates (n)** | Responses generated per prompt | `--n` flag (default: 4)             |
| **Avg tokens per rollout**  | Average response length        | `--max-tokens` flag (default: 2048) |
| **Throughput**              | Tokens generated per second    | Determined by model + hardware      |

<Note>
  Training time directly translates to cost: **Cost = Training time × Num GPUs × GPU-hour rate**. Check the [pricing page](https://fireworks.ai/pricing) for current GPU-hour rates.
</Note>

### How parameters affect cost

See how each parameter change impacts your total cost relative to a baseline configuration (500 prompts, 1 epoch, n=4, 2048 max tokens):

| Change                             | Cost impact    | Explanation                             |
| ---------------------------------- | -------------- | --------------------------------------- |
| Double dataset size (1000 prompts) | **\~2×**       | Linear scaling with dataset size        |
| Double rollouts (n=8)              | **\~2×**       | Linear scaling with rollout count       |
| Double max tokens (4096)           | **\~1.5–2×**   | More tokens per rollout                 |
| Add epoch (epochs=2)               | **\~2×**       | Full additional pass through data       |
| Double LoRA rank (16 → 32)         | **\~1.2–1.5×** | More trainable parameters               |
| Halve max tokens (1024)            | **\~0.5–0.7×** | Fewer tokens generated                  |
| Halve rollouts (n=2)               | **\~0.5×**     | Fewer rollouts but less learning signal |

## Cost optimization tips

<AccordionGroup>
  <Accordion title="Start with free models">
    Use models under 16B parameters for initial experimentation. Iterate on your evaluator and dataset with `qwen3-0p6b` or `llama-v3p1-8b-instruct` before moving to larger models.

    This lets you:

    * Validate your evaluator logic at zero cost
    * Test dataset quality and format
    * Tune rollout parameters
    * Establish baseline reward curves
  </Accordion>

  <Accordion title="Limit max tokens">
    Set `--max-tokens` to the minimum needed for your task:

    * **Short outputs** (classification, short answers): 256–512 tokens
    * **Medium outputs** (code generation, summaries): 1024–2048 tokens
    * **Long outputs** (detailed analysis, multi-step reasoning): 4096+ tokens

    Every token generated during rollouts costs compute. Don't use 16384 max tokens if your task only needs 512.
  </Accordion>

  <Accordion title="Use 1 epoch first">
    Start with 1 epoch (default). Most RFT jobs converge well within a single pass through the data. Add more epochs only if the reward curve is still climbing at the end of training.
  </Accordion>

  <Accordion title="Optimize evaluator speed">
    Slow evaluators increase wall-clock training time and therefore cost:

    * Keep evaluations under 5 seconds per rollout
    * Cache expensive computations
    * For remote evaluators, ensure your server can handle concurrent requests
    * Avoid unnecessary API calls in your evaluation logic

    **Evaluator complexity impact**: Simple evaluators (self-contained) have minimal overhead. Evaluators with calls to external services, such as LLM-as-judge use cases or company-specific endpoints, may have variable training time due to rate limits by model providers or other services.
  </Accordion>

  <Accordion title="Curate your dataset">
    A smaller, high-quality dataset often outperforms a larger, noisy one:

    * Remove duplicate or near-duplicate prompts
    * Ensure prompts are diverse and representative
    * Start with 200–500 well-chosen prompts
    * Quality over quantity reduces cost while maintaining performance
  </Accordion>
</AccordionGroup>

## Example cost scenarios

<AccordionGroup>
  <Accordion title="Scenario 1: Quick prototype (Free)">
    **Goal**: Test an evaluator on a small model

    | Parameter          | Value           |
    | ------------------ | --------------- |
    | Model              | Qwen3 0.6B      |
    | Dataset            | 100 prompts     |
    | Epochs             | 1               |
    | Rollouts (n)       | 4               |
    | Max tokens         | 2048            |
    | **Estimated cost** | **Free**        |
    | **Estimated time** | \~15–30 minutes |

    Best for: Initial evaluator development and testing.
  </Accordion>

  <Accordion title="Scenario 2: Production training (Free)">
    **Goal**: Train a capable model for production use

    | Parameter          | Value                 |
    | ------------------ | --------------------- |
    | Model              | Llama 3.1 8B Instruct |
    | Dataset            | 500 prompts           |
    | Epochs             | 1                     |
    | Rollouts (n)       | 4                     |
    | Max tokens         | 2048                  |
    | **Estimated cost** | **Free**              |
    | **Estimated time** | \~1–2 hours           |

    Best for: Production workloads that can use an 8B model.
  </Accordion>

  <Accordion title="Scenario 3: Large model training (Paid)">
    **Goal**: Train a large model for maximum quality

    | Parameter          | Value                          |
    | ------------------ | ------------------------------ |
    | Model              | Llama 3.3 70B Instruct         |
    | Dataset            | 500 prompts                    |
    | Epochs             | 1                              |
    | Rollouts (n)       | 4                              |
    | Max tokens         | 2048                           |
    | **Estimated cost** | Training hours × 8 GPUs × rate |
    | **Estimated time** | \~1–2 hours                    |

    Check the [Fireworks Pricing page](https://fireworks.ai/pricing) for the current GPU-hour rate. For a 2-hour job on 8 GPUs, multiply: 2 × 8 × (rate per GPU-hour).
  </Accordion>

  <Accordion title="Scenario 4: High-quality with more rollouts (Paid)">
    **Goal**: Maximum quality with large model and more rollouts

    | Parameter          | Value                          |
    | ------------------ | ------------------------------ |
    | Model              | DeepSeek V3                    |
    | Dataset            | 1000 prompts                   |
    | Epochs             | 2                              |
    | Rollouts (n)       | 8                              |
    | Max tokens         | 4096                           |
    | **Estimated cost** | Training hours × 8 GPUs × rate |
    | **Estimated time** | \~8–16 hours                   |

    This is a larger job. The cost scales with training time: more prompts, epochs, rollouts, and tokens all increase total GPU-hours.
  </Accordion>
</AccordionGroup>

## Monitoring costs during training

Cost information is only available after your job completes:

1. **Dashboard**: The [Fireworks Dashboard](https://app.fireworks.ai) displays the final cost on the RFT job page once training finishes
2. **Training progress**: While the job is running, you can monitor elapsed time and estimated completion in the job overview
3. **Early stopping**: You can cancel a job early if needed—the model checkpoint from the last completed step is still usable. The final cost will be calculated based on GPU-seconds consumed up to the cancellation point.

<Tip>
  If a job is running longer than expected, check your evaluator performance. Slow evaluators are the most common cause of unexpectedly long (and expensive) training runs.
</Tip>

## Next steps

<CardGroup>
  <Card title="Pricing Page" icon="dollar-sign" href="https://fireworks.ai/pricing">
    View current GPU-hour rates and pricing tiers
  </Card>

  <Card title="Parameter Tuning" icon="sliders" href="/fine-tuning/parameter-tuning">
    Learn how each parameter affects training quality and cost
  </Card>

  <Card title="Launch Training" icon="rocket" href="/fine-tuning/cli-reference">
    Create your first RFT job
  </Card>
</CardGroup>
