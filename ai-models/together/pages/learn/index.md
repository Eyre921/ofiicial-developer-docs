---
title: "Introduction"
source: https://docs.together.ai/learn/index
path: learn/index
---

Explore the fundamental concepts of the Together AI platform: Tokens, context windows, when to use serverless vs. dedicated inference, and how the stack works in practice.

The [reference docs](/intro) cover *how* to use the platform. This section covers the *why* behind what you're calling. Each topic starts broad and then layers in details, so you can form an accurate high-level mental model of the complete system.

You can read everything in order or cherry-pick whatever's relevant to what you're building:

## Fundamentals

<CardGroup>
  <Card title="How LLMs work" icon="cpu" href="/learn/how-llms-work">
    Text in, probabilities out, repeat in a loop.
  </Card>

  <Card title="Tokens & tokenization" icon="scissors" href="/learn/tokens-and-tokenization">
    Subword chunks of input and output.
  </Card>

  <Card title="Context windows" icon="layout-board" href="/learn/context-windows">
    The model's working memory and hard limits.
  </Card>

  <Card title="Inference parameters & sampling" icon="adjustments" href="/learn/inference-parameters-and-sampling">
    How to produce predictable or creative outputs.
  </Card>

  <Card title="Context engineering" icon="messages" href="/learn/prompt-engineering">
    Structuring prompts for optimal results.
  </Card>

  <Card title="Inference metrics" icon="dashboard" href="/learn/ttft-and-tps">
    TTFT and TPS, how fast an LLM feels.
  </Card>
</CardGroup>

## Core capabilities

<CardGroup>
  <Card title="Function calling & tool use" icon="tools" href="/learn/function-calling-and-tool-use">
    Model plans, your code runs the tool.
  </Card>

  <Card title="Structured outputs & JSON mode" icon="braces" href="/learn/structured-outputs">
    Force schema-valid output via constrained decoding.
  </Card>
</CardGroup>

## Customization & deployment

<CardGroup>
  <Card title="Fine-tune vs. prompt" icon="git-branch" href="/learn/finetune-vs-prompt">
    Hone a model for a particular task.
  </Card>

  <Card title="Choosing a deployment option" icon="server" href="/learn/choosing-a-deployment-option">
    Serverless, dedicated endpoints, or containers.
  </Card>

  <Card title="Quantization" icon="zoom-in" href="/learn/quantization">
    The JPEG quality slider for a model.
  </Card>
</CardGroup>
