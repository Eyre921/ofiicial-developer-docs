---
title: "Choose a Training Path"
source: https://docs.fireworks.ai/fine-tuning/choose-training-path
path: fine-tuning/choose-training-path
---

Choose the Fireworks workflow, infrastructure, and interaction surface for your training task.

Pick a **method**, then a **surface** (managed or Training API, serverless or dedicated). The surface decides how much of the model you can update and which **interfaces** are available to you.

## Choose a method

All three run as standard workflows on [Managed Fine-Tuning](/fine-tuning/managed-finetuning-intro), or as custom loops you write yourself on the [Training API](/fine-tuning/training-api/introduction).

|                              | SFT                                                                                                                                   | DPO                                                                                                         | RL                                                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Data you supply**          | Verified input/output pairs, or successful trajectories                                                                               | Preference pairs, single-turn only: one prompt, a chosen and a rejected response                            | Prompts, plus an evaluator that can tell a good outcome from a bad one                                                                                 |
| **Dataset size**             | Hundreds of examples, or roughly 10M+ tokens                                                                                          | Hundreds to thousands of pairs                                                                              | Dozens to thousands of prompts, sometimes more. Often fewer than 100 is enough                                                                         |
| **Good for**                 | Classification, extraction, format and tone adherence, distillation                                                                   | Steering the model toward a goal you cannot measure objectively, such as style, helpfulness, or safety.     | Tasks where you have no verified outputs to learn from, but you can tell whether an outcome was good or bad. Pushing the model beyond state-of-the-art |
| **Consider alternatives if** | You have very few examples, or no high-quality verified outputs to learn from                                                         | Outputs can be judged objectively, or you already have high-quality verified pairs. Both point to SFT or RL | You have no way at all to judge an outcome, including an LLM judge. Simpler methods are untried, or you want a quick fine-tuning experiment            |
| **Guides**                   | [Text](/fine-tuning/fine-tuning-models) · [Vision](/fine-tuning/fine-tuning-vlm) · [Cookbook](/fine-tuning/training-api/cookbook/sft) | [Managed DPO / ORPO](/fine-tuning/dpo-fine-tuning) · [Cookbook](/fine-tuning/training-api/cookbook/dpo)     | [Managed RFT](/fine-tuning/reinforcement-fine-tuning-models) · [Cookbook](/fine-tuning/training-api/cookbook/rl)                                       |

## Choose a surface

Answer the question below and the flow takes you to your surface, which links to its guide. Click any answered question to change it, or show every path at once.

<TrainingDecisionFlow />

Compare the last branch in detail on [serverless versus dedicated](/fine-tuning/training-api/choose-infrastructure), and check per-model support on [Models](/fine-tuning/models).

## Choose how to interact

* **Skill** — the only interface that drives both surfaces. Your coding agent configures, runs, and troubleshoots training through the [Fireworks training skill](/fine-tuning/agent/use-with-coding-agents).
* **Fireworks UI, `firectl`, or the REST API** — managed jobs only. Guided creation and monitoring in the UI, reproducible job and resource automation from the CLI or API.
* **Python SDK** — Training API loops only, on serverless or dedicated. Start from a [cookbook recipe](/fine-tuning/training-api/cookbook/overview).

## Before launch

Verify current model support, shapes, access status, pricing, limits, and quota in the linked live pages. A coding agent asks for confirmation before any mutation — upload, registration, paid inference, job creation, promotion, or deployment — and again after material changes.
