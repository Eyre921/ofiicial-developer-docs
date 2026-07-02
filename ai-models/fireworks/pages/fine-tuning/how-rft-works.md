---
title: "Basics"
source: https://docs.fireworks.ai/fine-tuning/how-rft-works
path: fine-tuning/how-rft-works
---

Understand the reinforcement learning fundamentals behind RFT

## What is reinforcement fine-tuning?

In traditional supervised fine-tuning, you provide a dataset with labeled examples showing exactly what the model should output. In reinforcement fine-tuning, you instead provide:

1. **A dataset**: Prompts, with input examples for the model to respond to
2. **An evaluator**: Code that scores the model's outputs from 0.0 (bad) to 1.0 (good), also known as a reward function
3. **An agent**: An LLM application, with access to tools, APIs, and data needed for your task

During training, the model generates responses to each prompt, receives scores from your reward function, and produces outputs that maximize the reward.

## Use cases

Reinforcement fine-tuning helps you train models to excel at:

* **Code generation and analysis** - Writing and debugging functions with verifiable execution results or test outcomes
* **Structured output generation** - JSON formatting, data extraction, classification, and schema compliance with programmatic validation
* **Domain-specific reasoning** - Legal analysis, financial modeling, or medical triage with verifiable criteria and compliance checks
* **Tool-using agents** - Multi-step workflows where agents call external APIs with measurable success criteria

## How it works

<Steps>
  <Step title="Design your evaluator">
    Define how you'll score model outputs from 0 to 1. For example, scoring outputs higher by checking if your agent called the right tools, or if your LLM-as-judge rates the output highly.
  </Step>

  <Step title="Prepare dataset">
    Create a JSONL file with prompts (system and user messages). These will be used to generate rollouts during training.
  </Step>

  <Step title="Connect your agent">
    Train locally, or connect your agent as a remote server to Fireworks with our /init and /status endpoints.
  </Step>

  <Step title="Launch training">
    Create an RFT job via the UI or CLI. Fireworks orchestrates rollouts, evaluates them, and trains the model to maximize reward.
  </Step>

  <Step title="Deploy model">
    Once training completes, deploy your fine-tuned LoRA model to production with an on-demand deployment.
  </Step>
</Steps>

### RFT works best when:

1. You can determine whether a model's output is "good" or "bad," even if only approximately
2. You have prompts but lack perfect "golden" completions to learn from
3. The task requires multi-step reasoning where evaluating intermediate steps is hard
4. You want the model to explore creative solutions beyond your training examples

## Next steps

<CardGroup>
  <Card title="Create an evaluator" icon="code" href="/fine-tuning/evaluators">
    Learn how to design effective reward functions
  </Card>

  <Card title="Kick off training" icon="rocket" href="/fine-tuning/cli-reference">
    Learn how to launch and configure RFT jobs
  </Card>
</CardGroup>
