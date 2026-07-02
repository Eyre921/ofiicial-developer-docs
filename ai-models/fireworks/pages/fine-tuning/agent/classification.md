---
title: "Fireworks Agent: Classification"
source: https://docs.fireworks.ai/fine-tuning/agent/classification
path: fine-tuning/agent/classification
---

Benchmark base models, fine-tune on labeled data, and pick the best classifier — automatically.

Fireworks Agent's classification workflow is purpose-built for label-prediction tasks. It evaluates one or more base models against your labeled dataset, fine-tunes the strongest candidates, and reports a head-to-head comparison of base vs fine-tuned accuracy on a held-out test split.

Use this workflow for classification, content extraction, intent detection, routing, and other tasks with a discrete label set.

<Note>
  For the underlying SFT mechanics (job parameters, supported base models, dataset format), see [Managed Fine-Tuning → Supervised Fine-Tuning](/fine-tuning/fine-tuning-models). The classification workflow is built on top of SFT with classification-specific dataset handling and reporting.
</Note>

## What you give Agent

| Input                            | Required? | Notes                                                                                  |
| -------------------------------- | --------- | -------------------------------------------------------------------------------------- |
| Dataset ID(s)                    | **Yes**   | Single dataset (split 80/20 train/test) or two datasets (separate train + eval)        |
| Models to evaluate and fine-tune | **Yes**   | Agent does **not** default to "all models"; pick from the supported list when prompted |
| Candidate labels                 | No        | Agent infers labels from your data if you don't list them explicitly                   |
| Imbalance-ratio threshold        | No        | Defaults to `50.0` (ratio of most-frequent to least-frequent label)                    |

### Dataset requirements

* Each sample must contain `messages` in OpenAI chat-completion format.
* `ground_truth` is optional. If absent, Agent extracts the label from the final assistant message using task-specific logic in the plan.
* `ground_truth` may be a single string or a list of strings.

## Example session instructions

Single dataset with automatic split, two candidate models:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Benchmark and fine-tune classification on accounts/myacct/datasets/intent-labels. Compare Qwen3 8B and Qwen3 32B. Labels are: billing, technical, account, sales."
```

Separate train and eval datasets, model already chosen:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Run classification fine-tuning on accounts/myacct/datasets/train, eval on accounts/myacct/datasets/test, using Qwen3 8B."
```

<Note>
  **Where classification lives in the 7-phase pipeline:** Phase 1 is dataset inspection (with per-label sample counts and imbalance detection), phase 2 is plan + cost approval, **phase 3 is the base-model benchmark plus fine-tuning sweep**, phase 4 is the full-data run for each candidate, **phase 5 is the fine-tuned evaluation** with per-label and overall accuracy, phase 6 is deployment of the winner, phase 7 is the base-vs-fine-tuned comparison report. See [How Agent runs a training job](/fine-tuning/agent/introduction#how-agent-runs-a-training-job).
</Note>

## Workflow stages

<Steps>
  <Step title="Dataset inspection">
    Agent stages your dataset locally once, computes per-label sample counts, detects the imbalance ratio, and inspects message structure. If `ground_truth` is missing, Agent decides how to extract the label from the final assistant turn.
  </Step>

  <Step title="Label resolution">
    If you provided candidate labels in your instruction, Agent uses them. Otherwise, Agent infers them from the data and surfaces the inferred set in the plan for you to confirm.
  </Step>

  <Step title="Imbalance handling">
    Agent computes the ratio of most-frequent to least-frequent label. If it exceeds the threshold (default `50.0`), Agent flags the imbalance in the plan and proposes mitigations (rebalancing, weighted training, or a smaller candidate set).
  </Step>

  <Step title="Plan + cost approval">
    Agent writes a plan and presents it with a cost breakdown (base-model evaluation inference + fine-tuning + fine-tuned evaluation inference + total). Approve once to proceed.
  </Step>

  <Step title="Base-model benchmarking">
    Agent runs inference on the held-out eval split against each selected base model and reports per-label and overall accuracy. This becomes the baseline.
  </Step>

  <Step title="Fine-tuning sweep">
    Agent fine-tunes the strongest candidates with the default tuning grid (or your explicit grid), batched into waves of up to 6 active jobs.
  </Step>

  <Step title="Fine-tuned evaluation">
    Agent runs the same eval inference against each fine-tuned model and computes per-label accuracy, overall accuracy, and confusion-matrix style summaries.
  </Step>

  <Step title="Deployment and comparison report">
    Agent picks the winner, deploys it (phase 6), and writes the final comparison report (phase 7) showing base vs fine-tuned accuracy per candidate plus a `fireworks-ai` SDK snippet for inference.
  </Step>
</Steps>

## Output

When the session reports `succeeded`, Agent's response includes:

* Per-label and overall accuracy for every base model evaluated
* Per-label and overall accuracy for every fine-tuned candidate
* The winning model ID, deployment ID, and inference endpoint
* A `fireworks-ai` SDK snippet for label prediction
* `final_report.md` in the session workspace with the full base vs fine-tuned comparison and estimated-vs-actual cost

## Customizing the run

* **Explicit labels:** *"Labels are: positive, negative, neutral."*
* **Imbalance threshold override:** *"Use an imbalance threshold of 20."*
* **Inference-only mode:** *"Just benchmark — don't fine-tune."*
* **Single candidate:** *"Only fine-tune Qwen3 8B, skip the base-vs-base comparison."*
* **Custom split:** *"Use a 70/30 train/test split."*

<Note>
  **Agent crib notes**

  * Required inputs: dataset ID and at least one base model to evaluate. Agent will ask explicitly if either is missing.
  * Agent needs to know your labels eventually — either supply them in the instruction or confirm Agent's inferred set when prompted.
  * The default imbalance threshold is `50.0`; if your dataset is highly imbalanced, expect Agent to flag it in the plan.
  * For multi-label classification (a sample with multiple ground-truth labels), pass `ground_truth` as a list in your dataset.
  * Agent creates new resources only; your dataset, models, and deployments are never deleted or modified in place.
</Note>
