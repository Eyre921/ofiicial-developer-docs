---
title: "Fireworks Agent: Preference Learning (DPO/ORPO)"
source: https://docs.fireworks.ai/fine-tuning/agent/dpo
path: fine-tuning/agent/dpo
---

Run preference fine-tuning end-to-end with optional base-model sweep, automatic pair generation, and pairwise evaluation.

Fireworks Agent's preference-learning workflow runs DPO or ORPO fine-tuning against pre-paired preference data, or generates pairs for you from a prompts-only dataset using delta learning. It can sweep multiple base models when you don't know which to pick, evaluates winners pairwise (or with your evaluator), and produces a final comparison report.

<Note>
  For the underlying DPO mechanics and dataset format details, see [Managed Fine-Tuning → DPO Fine-Tuning](/fine-tuning/dpo-fine-tuning). This page documents the Fireworks Agent workflow built on top of it.
</Note>

## What you give Agent

| Input              | Required? | Notes                                                                                                                   |
| ------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| Dataset ID(s)      | **Yes**   | A single dataset (split 80/20 train/test automatically) or two datasets (separate train + test)                         |
| Base model         | No        | If omitted, Agent runs a **model sweep** across supported base models to pick the best automatically                    |
| Evaluator          | No        | Evaluator ID, custom rubric text, or none (Agent builds a data-grounded pairwise judge rubric if you don't provide one) |
| Performance target | No        | Optional goal score, for example *"win rate above 70%"*                                                                 |

## Example session instructions

Pre-paired preference data with a specific base model:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Run DPO on accounts/myacct/datasets/customer-prefs using Qwen3 32B."
```

Prompts-only dataset with automatic pair generation and a base-model sweep:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Run preference learning on accounts/myacct/datasets/prompts-only. Generate preference pairs automatically and sweep base models to find the best one."
```

<Note>
  **Where DPO lives in the 7-phase pipeline:** Phase 1 is dataset inspection, phase 2 is plan + cost approval, **phase 3 is the preference sweep** (replacing the SFT HP sweep — includes pair generation up-front for Format B), phase 5 is the pairwise evaluation, phase 6 is deployment of the winner, phase 7 is the final report. DPO does **not** run a separate phase 4 full-data retrain — the sweep itself is the training run on the chosen base model + config. See [How Agent runs a training job](/fine-tuning/agent/introduction#how-agent-runs-a-training-job).
</Note>

## Dataset formats

Agent accepts two formats:

### Format A — DPO format (pre-paired preferences)

Each sample has `input`, `preferred_output`, and `non_preferred_output` fields. `input.messages` holds the conversation; `preferred_output` and `non_preferred_output` hold candidate assistant responses.

When this format is detected, Agent skips pair generation and goes straight to training.

### Format B — prompts-only

Each sample has a `messages` field with user messages only (no assistant completions). Agent generates preference pairs automatically using **delta learning**: it samples completions from a strong and a weak model, then constructs preferred/non-preferred pairs for training.

## Workflow stages

<Steps>
  <Step title="Dataset download and metrics">
    Agent stages the dataset locally exactly once per session, computes token statistics, and decides between Format A (skip pair generation) and Format B (generate pairs).
  </Step>

  <Step title="Inspect evaluator and gather inputs">
    Agent resolves your evaluator choice (evaluator ID / custom rubric / auto rubric) and asks for anything missing — usually the dataset and, if you omitted both base model and grid, confirmation that a base-model sweep is OK.
  </Step>

  <Step title="Plan + cost approval">
    Agent presents a plan plus a cost breakdown (training + any pair-generation inference + evaluator inference + total) and asks for a single approval covering both.
  </Step>

  <Step title="Pair generation (Format B only)">
    Agent generates preference pairs via delta learning and uploads the resulting dataset to Fireworks under a new, timestamped name. Your original dataset is left untouched.
  </Step>

  <Step title="Model sweep / HP sweep">
    If no base model was specified, Agent runs DPO/ORPO across a curated set of supported base models. If a base model was specified, Agent runs an HP sweep against that single base model. Training jobs are batched (default cap of 6 active at once).
  </Step>

  <Step title="Evaluation and pairwise comparison">
    For each trained model, Agent generates completions on the held-out test split and scores them. With your own evaluator, scores are reported independently. Without one, Agent uses a pairwise judge rubric grounded in actual training samples.
  </Step>

  <Step title="Deployment and final report">
    Agent deploys the winning fine-tuned model and writes a final report comparing base and fine-tuned models, with the deployment endpoint and (if you supplied a performance target) whether the target was met.
  </Step>
</Steps>

## Evaluator handling

Agent supports three evaluator paths, in priority order:

1. **Evaluator ID** — for example `accounts/myacct/evaluators/my-eval`. Agent fetches the evaluator code, installs dependencies, and runs it to score each model's completions independently. Agent reports average scores for the base model and every fine-tuned candidate.
2. **Custom rubric text** — provide a pairwise LLM judge rubric in your instruction. Agent uses it to compare two completions head-to-head.
3. **Neither** — Agent inspects training samples and writes a data-grounded pairwise judge rubric automatically.

## Output

When the session reports `succeeded`, Agent returns:

* The winning fine-tuned model ID and its deployment endpoint
* Base vs fine-tuned comparison: scores or win rate from the chosen evaluator
* A copy-paste `fireworks-ai` SDK snippet for the deployed model
* `final_report.md` in the session workspace with per-model scores, pair-generation provenance (if Format B), and estimated-vs-actual cost

## Supported base models

The model sweep selects from the supported preference-learning base models. For the canonical list, see [Managed Fine-Tuning Overview → Supported base models](/fine-tuning/managed-finetuning-intro#supported-base-models).

## Customizing the run

* **Pin a base model:** *"Use Qwen3 32B."* — skips the model sweep.
* **Explicit grid:** *"Sweep Qwen3 32B and Qwen3-30B-A3B with beta 0.1 and 0.3."*
* **Bring your own evaluator:** *"Use evaluator accounts/myacct/evaluators/my-rubric."*
* **Auto-generate pairs:** *"Generate preference pairs automatically."*
* **Set a target:** *"Stop early once we reach 75% win rate against the base."*

<Note>
  **Agent crib notes**

  * Required input: dataset ID. Everything else is optional.
  * Agent will pause for one approval (plan + cost) and again at the comparison report. The promotion gate appears only when a clear winner needs confirmation.
  * If the dataset is prompts-only, Agent will generate pairs by sampling strong and weak models — expect inference cost on top of training cost.
  * Agent always creates new datasets with timestamped names; your original dataset is never overwritten.
  * For deeper customization of the loss (custom beta schedules, hybrid objectives), use the [Training API](/fine-tuning/training-api/introduction) instead.
</Note>
