---
title: "Fireworks Agent: Supervised Fine-Tuning"
source: https://docs.fireworks.ai/fine-tuning/agent/sft
path: fine-tuning/agent/sft
---

Run end-to-end SFT with Fireworks Agent — dataset inspection, hyperparameter sweep, evaluator-guided selection, and a deployed winner.

Fireworks Agent's SFT workflow takes a dataset and (optionally) a base model, runs a hyperparameter sweep with held-out evaluation, picks the winner, retrains on the full data, and deploys the result. You approve a single plan with a cost estimate up front; Agent handles everything from there and pauses only at meaningful decision points.

<Note>
  For the underlying SFT mechanics (job parameters, supported base models, dataset format), see [Managed Fine-Tuning → Supervised Fine-Tuning](/fine-tuning/fine-tuning-models). This page documents the Fireworks Agent workflow built on top of it.
</Note>

## What you give Agent

Agent needs enough to build an executable plan. The required inputs:

* **Dataset ID** — an existing Fireworks dataset in `READY` state, in OpenAI-compatible chat format. Optionally a separate evaluation dataset.
* **Base model(s)** — one or more base models. If you omit this, Agent will ask you to choose from the supported list.
* **Evaluation approach** — one of three strategies (see below). Default is validation loss only.

Everything else (epochs, LoRA rank, learning rate, batching) is resolved by Agent from defaults or your explicit overrides.

## Example session instruction

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Run supervised fine-tuning on accounts/myacct/datasets/customer-support-conv. Use Qwen3 32B as the base model. Use validation loss for evaluation."
```

For explicit candidates instead of the default tuning grid:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Run SFT on accounts/myacct/datasets/mydata across qwen3-8b and qwen3-32b with learning rates 1e-4 and 5e-5, LoRA ranks 16 and 32, and 3 epochs."
```

<Note>
  **Where SFT lives in the 7-phase pipeline:** Phase 1 is dataset inspection, phase 2 is plan + cost approval, **phase 3 is the candidate sweep** described below, phase 4 is the full-data final run, **phase 5 is held-out evaluation** (using the strategy you picked in phase 2), phase 6 is deployment, phase 7 is the final report. See [How Agent runs a training job](/fine-tuning/agent/introduction#how-agent-runs-a-training-job).
</Note>

## Workflow stages

<Steps>
  <Step title="Dataset inspection">
    Agent stages your dataset locally exactly once per session (`firectl dataset download ...`), inspects format and sample structure, estimates token counts for cost, and decides whether any conversion is needed (for example, mapping `ground_truth` fields onto an assistant message or rewriting `tool` roles).
  </Step>

  <Step title="Strategy and candidate selection">
    Agent picks an evaluation strategy (see [Evaluation paths](#evaluation-paths) below) and resolves your candidate grid. The default tuning grid is three HP configurations with the LoRA rank and learning rate shown below; epochs default to `min(5, ceil(2500 / total_samples))` unless you override them.

    | HP config | LoRA rank | Learning rate |
    | --------- | --------- | ------------- |
    | 1         | 8         | 1.5e-4        |
    | 2         | 16        | 1.0e-4        |
    | 3         | 32        | 5.0e-5        |

    For HP tuning on datasets larger than 1,000 samples, Agent subsamples to 1,000 (seed `42`) to keep candidate-search costs bounded.
  </Step>

  <Step title="Plan + cost approval">
    Agent writes a plan to the session workspace and presents it to you with a cost breakdown (Training + Inference + Total). A single approval covers both the plan and the estimate. Reply with `Approved, proceed.` or ask for revisions and Agent will re-cost and re-present.
  </Step>

  <Step title="Hyperparameter sweep">
    Agent launches the candidate training runs, capped at **6 active jobs at a time** by default. Each candidate trains on the (sub-sampled) train split and is evaluated against the held-out test split using the evaluation strategy you chose.
  </Step>

  <Step title="Promotion gate">
    Before the full-data final run, Agent pauses at a promotion gate. It surfaces the candidate scoreboard (validation loss and any evaluator metrics) and asks you to confirm the winner. Reply with `Proceed with the winning config.`
  </Step>

  <Step title="Full-data final run">
    Agent trains the winning configuration on the full dataset (epochs default to `min(5, ceil(2500 / total_samples))` for the final run). Agent then evaluates the final model directly and writes `final_report.md`.
  </Step>

  <Step title="Deployment">
    Agent deploys the final model and reports the deployed model ID, deployment ID, inference endpoint, and a copy-paste `fireworks-ai` SDK snippet you can use immediately.
  </Step>
</Steps>

## Evaluation paths

Agent supports three evaluation strategies. You can specify one in your instruction, or Agent will ask which to use in plain English (it does **not** say "Path A" / "Path B" / "Path C" to you — the labels below are docs shorthand for the three options).

### Path A — validation loss only

The default. Agent creates a held-out test split, trains each candidate, and picks the winner purely on validation loss. No task-level evaluator is run. Choose this when:

* You don't have an evaluator script for the task
* The dataset is small or evaluator design is not yet settled
* You want the fastest, lowest-cost sweep

Trigger phrase: *"Use validation loss for evaluation."* or simply *"validation loss is fine"* if Agent asks.

### Path B — bring your own evaluator

You provide a Python evaluator (uploaded to Fireworks, or generated in the same session via [evaluator authoring](/fine-tuning/agent/evaluators)). Agent runs the evaluator on each candidate's outputs and on the final model.

Trigger phrase: *"Use evaluator accounts/myacct/evaluators/my-eval."* or *"Use my own evaluator"* if Agent asks.

### Path C — Agent-generated evaluator

Agent inspects your data and writes a Python evaluator for structured or objectively checkable outputs (for example: numeric answers, JSON schemas, exact-match labels). It then uses that evaluator to score candidates and the final model.

Trigger phrase: *"Generate an evaluator for me."* or *"agent-generated evaluator"* if Agent asks.

## Output

When the session reports `succeeded`, Agent's final message includes:

* The deployed **model ID** and **deployment ID**
* The inference endpoint and a ready-to-run `fireworks-ai` SDK snippet
* Final training loss and evaluation loss (or evaluator score) for the winning model
* Provenance for any rollout/evaluation evidence carried forward from candidate search
* A link to `final_report.md` in the session workspace with the full plan, costs (estimated vs actual), and per-candidate metrics

## Supported base models

Agent's SFT workflow supports the same base models as Managed Fine-Tuning. For the canonical list and maximum context lengths, see [Managed Fine-Tuning Overview → Supported base models](/fine-tuning/managed-finetuning-intro#supported-base-models).

You can ask Agent for the current list inside any session: *"Which base models do you support for SFT?"*

## Customizing the run

Things you can put in your instruction:

* **Candidate grid:** *"Use LoRA ranks 8, 16, 32 with learning rates 1e-4 and 5e-5."*
* **Fixed epochs:** *"Train each candidate for 3 epochs."*
* **Subsampling override:** *"Use 500 samples for HP tuning."*
* **Batch limit:** *"Run up to 10 training jobs in parallel."*
* **Skip final retrain:** *"Skip the full-data final run."* (Agent will deploy the winning candidate directly.)
* **Eval set:** *"Use accounts/myacct/datasets/holdout as the eval dataset."* (Agent sets `evaluationDataset` and disables eval carveout.)

If anything in your instruction conflicts with Agent's defaults, your instruction wins.

<Note>
  **Agent crib notes**

  * Required inputs for an SFT session: dataset ID. Optional: base model, evaluation strategy, candidate grid, epochs.
  * Default tuning grid is 3 LoRA configs × selected base models. Default epochs = `min(5, ceil(2500 / total_samples))`.
  * Agent will pause twice for user input: plan + cost approval, and the promotion gate. Common responses: `Approved, proceed.` and `Proceed with the winning config.`
  * For validation-loss-only evaluation, answer `validation loss is fine` when Agent asks how to evaluate.
  * All training jobs and the deployed model are created in **your** account using the `FIREWORKS_AGENT_API_KEY` you authenticated with. Agent never destroys or modifies your existing resources.
</Note>
