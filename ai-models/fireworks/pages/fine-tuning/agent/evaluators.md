---
title: "Fireworks Agent: Evaluator Authoring"
source: https://docs.fireworks.ai/fine-tuning/agent/evaluators
path: fine-tuning/agent/evaluators
---

Have Fireworks Agent generate a reusable evaluator from your dataset — for scoring candidates in an SFT sweep, or for use with Managed RFT.

Fireworks Agent can write a task-specific evaluator from your dataset alone. Two flavors:

* **SFT evaluators** — a Python evaluator (`evaluator.py`) plus a spec (`eval_spec.md`) that Agent uses to score candidates during a subsequent SFT sweep in the same session.
* **RFT evaluators** — an Eval Protocol `@evaluation_test` evaluator ready to drive a Reinforcement Fine-Tuning job.

Use evaluator authoring when you have a dataset and a clear notion of what "correct" looks like, but no evaluator script yet.

## SFT evaluators

### What you get

Agent generates two artifacts in the session workspace:

* `outputs/eval_spec.md` — a human-readable spec describing what the evaluator checks (the contract: what counts as correct, how partial credit works, edge cases).
* `outputs/evaluator.py` — a Python evaluator that takes a model's outputs and the dataset's ground truth and returns scores.

After the artifacts are written, Agent surfaces the full `eval_spec.md` and `evaluator.py` contents in chat so you can review them before they're used downstream.

### Example session instructions

Author an evaluator only:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Generate an evaluator for accounts/myacct/datasets/customer-support. Outputs are short text answers; check whether the final assistant reply matches ground truth on key facts."
```

Author an evaluator and continue straight into SFT in the same session — Agent reuses the freshly-written evaluator without re-authoring:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Generate an evaluator for accounts/myacct/datasets/customer-support, then run SFT on Qwen3 8B and use that evaluator to pick the winning candidate."
```

<Note>
  **Where evaluator authoring lives in the 7-phase pipeline:** When evaluator authoring runs as a standalone session, phases 3–7 of the standard pipeline don't apply; the session writes `outputs/evaluator.py` + `outputs/eval_spec.md` and stops. When you chain authoring into SFT in the same session, those artifacts feed **phase 5 (Evaluation)** of the follow-on training pipeline — used to score candidates during phase 3 and again for direct evaluation of the final model. (RFT evaluators are saved to your Fireworks account and then used by [Managed Fine-Tuning's RFT path](/fine-tuning/reinforcement-fine-tuning-models), not by Agent.) See [How Agent runs a training job](/fine-tuning/agent/introduction#how-agent-runs-a-training-job).
</Note>

When you ask for both in one instruction, Agent writes the evaluator first, then automatically continues into SFT with **same-session evaluator reuse**: the SFT workflow picks up `outputs/evaluator.py` and `outputs/eval_spec.md` without re-authoring them, and reuses the staged dataset paths so the dataset is downloaded only once.

### Multi-turn handoff

If you want fine-grained control of the handoff, structure your two instructions like this:

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Generate an evaluator for accounts/myacct/datasets/mydata."
# Wait for evaluator artifacts to be written and presented in chat.
```

Then continue in the **same session**:

```bash theme={null}
source .env && firectl session update <session-id> \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Now run SFT on Qwen3 32B using the evaluator we just authored. Reuse outputs/evaluator.py and outputs/eval_spec.md — do not regenerate them."
```

Agent will inherit the staged dataset and the evaluator artifacts without re-downloading or rewriting them.

## RFT evaluators

<Note>
  **Agent authors RFT evaluators but does not run RFT training.** This workflow produces and validates the Eval Protocol evaluator file, then registers it with your Fireworks account. The actual RFT training job runs through [Managed Fine-Tuning's RFT path](/fine-tuning/reinforcement-fine-tuning-models) — not from an Agent session.
</Note>

### What you get

An Eval Protocol `@evaluation_test` evaluator file, validated end-to-end, ready to drop into a Reinforcement Fine-Tuning job. The plan includes the concrete evaluator code, validation commands, and the command to save the evaluator to Fireworks.

This is purpose-built for tasks where you can score model outputs against reference data — math problems, code generation, structured-output extraction, agentic workflows with verifiable side effects.

### Example session instruction

```bash theme={null}
source .env && firectl session create \
  --api-key $FIREWORKS_AGENT_API_KEY \
  --instruction "Build an RFT evaluator for accounts/myacct/datasets/math-problems. Score whether the final numeric answer matches ground truth."
```

Agent inspects samples, writes the evaluator, validates it on a few records, and presents the plan with the save command. You approve once and Agent executes the plan, registering the evaluator with your Fireworks account.

### Handing off to RFT training

Once the evaluator is saved, run the RFT job through Managed Fine-Tuning — see the [Reinforcement Fine-Tuning Overview](/fine-tuning/reinforcement-fine-tuning-models) and [Evaluators concepts](/fine-tuning/evaluators). For example:

```bash theme={null}
firectl rftj create \
  --base-model accounts/fireworks/models/qwen3-8b \
  --evaluator accounts/myacct/evaluators/<your-evaluator> \
  --dataset accounts/myacct/datasets/math-problems
```

Or use the [Web UI](/fine-tuning/web-ui-guide) to launch the RFT job interactively.

## Workflow summary

<Steps>
  <Step title="Dataset inspection">
    Agent stages the dataset locally, samples records, and infers the evaluator contract from data plus your scoring intent. Agent will not finalize an evaluator without successfully staging readable data.
  </Step>

  <Step title="Spec and code generation">
    For SFT, Agent writes both `eval_spec.md` (the contract) and `evaluator.py` (the implementation) and self-checks that both are non-empty before finishing. For RFT, Agent writes a single Eval Protocol `@evaluation_test` file and self-checks that it's non-empty and that validation succeeds.
  </Step>

  <Step title="Review and approval">
    Agent surfaces the artifacts inline in chat. For RFT, Agent also presents a plan with validation and save commands and asks for one approval.
  </Step>

  <Step title="Hand off (optional)">
    If your instruction asks for downstream SFT, Agent continues into the SFT workflow in the same session and reuses the just-authored evaluator — no re-downloading, no re-authoring. RFT training itself runs through [Managed Fine-Tuning](/fine-tuning/reinforcement-fine-tuning-models), not from an Agent session.
  </Step>
</Steps>

## When to use which

| Use case                                                                                                          | Workflow                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| You want an evaluator Agent can use to score candidates during an SFT sweep, with optional auto-continue into SFT | **SFT evaluator authoring** (run end-to-end by Agent)                                                                                                              |
| You want an Eval Protocol evaluator to drive an RFT job                                                           | **RFT evaluator authoring** (Agent writes and saves the evaluator; RFT training runs through [Managed Fine-Tuning](/fine-tuning/reinforcement-fine-tuning-models)) |
| You don't have a clear notion of "correct" yet                                                                    | Start with **validation-loss-only SFT** on [Agent SFT](/fine-tuning/agent/sft) and add an evaluator later                                                          |

<Note>
  **Agent crib notes**

  * Required input: dataset ID. Agent also wants your scoring intent in plain English — "check whether the answer matches ground truth", "verify the JSON has the right schema", etc.
  * For SFT evaluators, ask for both authoring and SFT in the same instruction to get same-session evaluator reuse for free.
  * For RFT evaluators, expect a plan + cost approval before the evaluator is saved to your Fireworks account. **The Agent session ends after the evaluator is saved.** Hand off to [Managed Fine-Tuning's RFT path](/fine-tuning/reinforcement-fine-tuning-models) to run the actual RFT training job.
  * Agent surfaces the generated `eval_spec.md` and `evaluator.py` inline in chat after authoring — relay them to the user.
  * All evaluator artifacts live under `outputs/` in the session workspace and can be inspected via `firectl session get <id>` if needed.
</Note>
