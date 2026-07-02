---
title: "Overview"
source: https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models
path: fine-tuning/reinforcement-fine-tuning-models
---

Train models using reinforcement learning in minutes

<Tip>
  **Reinforcement Fine-Tuning (RFT)** is free for models under 16B parameters. When creating an RFT job in the UI, filter for free tuning models in the model selection area on the [fine-tuning creation page](https://app.fireworks.ai/dashboard/fine-tuning/create). If kicking off jobs from the terminal, you can find the model ID from the [Model Library](https://app.fireworks.ai/models?filter=LLM\&tunable=true). Note: SFT and DPO jobs are billed per training token for all model sizes—see the [pricing page](https://fireworks.ai/pricing) for details.
</Tip>

Fireworks RFT helps you train frontier models like DeepSeek V3 and Kimi K2 to **outperform closed models for your product use case, using reinforcement learning.** Fireworks RFT is powerful and easy to use for developers and enterprises:

* **No infrastructure:** Train frontier models without managing GPUs or RL infra
* **Production-ready:** Built-in tracing, monitoring, security & one-click deploy
* **Fast iteration:** From evaluator setup to deployed model in hours, not weeks

<Tip>
  See how [Genspark](https://fireworks.ai/blog/genspark) and [Vercel](https://fireworks.ai/blog/vercel) used Fireworks RFT to train open models for agentic use cases, outperforming leading closed models.
</Tip>

## Quickstart: Pick Your Training Approach

<CardGroup>
  <Card title="Single-Turn Training" icon="laptop-code" href="/fine-tuning/quickstart-math">
    **⏱️ 15 minutes**

    **Best for:** Testing locally, simple task training

    **How it works:** Iterate on your evaluator and use it to train a small model on Fireworks.
  </Card>

  <Card title="Remote Agents" icon="server" href="/fine-tuning/quickstart-svg-agent">
    **⏱️ 1-2 hours**

    **Best for:** Agents, multi-turn workflows, existing services

    **How it works:** Rollouts happen in your environment. Connect via HTTP with tracing.
  </Card>

  <Card title="Secure Training (BYOB)" icon="shield-check" href="/fine-tuning/secure-fine-tuning">
    **⏱️ 2-4 hours**

    **Best for:** Sensitive data, compliance, enterprise

    **How it works:** Training data never leaves your GCS/S3 bucket. Full data isolation.
  </Card>
</CardGroup>

## Launch Training

<CardGroup>
  <Card title="Prerequisites & Validation" icon="list-check" href="/fine-tuning/training-prerequisites">
    Requirements, validation checks, and common errors before launching
  </Card>

  <Card title="CLI (eval-protocol)" icon="terminal" href="/fine-tuning/cli-reference">
    Fast, scriptable, reproducible. Perfect for automation and iteration
  </Card>

  <Card title="Web UI" icon="browser" href="/fine-tuning/web-ui-guide">
    Visual, guided, beginner-friendly. Great for exploring options
  </Card>
</CardGroup>

<Note>
  Already familiar with [firectl](/fine-tuning/cli-reference#using-firectl-cli-alternative)? You can create RFT jobs directly.
</Note>

## RFT Concepts

<CardGroup>
  <Card title="How RFT Works" href="/fine-tuning/how-rft-works" icon="brain">
    The RL training loop explained
  </Card>

  <Card title="Evaluators" href="/fine-tuning/evaluators" icon="check-circle">
    How reward functions guide training
  </Card>

  <Card title="Environments" href="/fine-tuning/environments" icon="server">
    Local vs remote evaluation environments
  </Card>

  <Card title="Parameter Tuning" href="/fine-tuning/parameter-tuning" icon="sliders">
    Optimize your training configuration
  </Card>

  <Card title="Cost Estimator" href="/fine-tuning/rft-cost-estimator" icon="calculator">
    Estimate and optimize your training costs
  </Card>
</CardGroup>
