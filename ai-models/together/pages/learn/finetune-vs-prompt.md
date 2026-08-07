---
title: "When to fine-tune vs. prompt"
source: https://docs.together.ai/learn/finetune-vs-prompt
path: learn/finetune-vs-prompt
---

Prompting steers an existing model. Fine-tuning changes its weights. You should almost always try prompting first.

**TL;DR:** Prompting steers a model with the text you put in front of it. Fine-tuning continues training the model on your examples and actually changes its weights. You should almost always try prompting first, because it is faster, cheaper, and instantly reversible. Try reaching for fine-tuning only when you've hit a hard ceiling in your efforts to improve prompt quality, when you have enough data from prompts and outputs to train on, and when the behavior you need is a *pattern* the model can learn from examples rather than a *fact* it needs to look up.

## Try prompting first

Prompting has four huge advantages, which taken together should always make it your default starting point. First off, it's basically **free**, because you are already paying for inference and there is no extra training run or labeled dataset you need to build. Second, it's **fast**, because changing the prompt and running it again takes seconds, while fine-tuning a model takes hours, or even days. Third, it's **reversible**, because a bad prompt costs you only the tokens you wasted, while a bad fine-tune costs you the wasted time and compute of an entire training run. And lastly it **composes**, because each request can have a different prompt for a different task, while a fine-tuned model creates one new behavioral shape and applies it to every request.

For almost all cases in which a model is not doing what you want, the right tool is [better prompting](/learn/prompt-engineering)—better instructions, more examples, more structure, tighter constraints. If iterating on the prompt gets you to an acceptable quality threshold, you should stop there.

## Where fine-tuning wins

Fine-tuning is the right tool for a narrow set of problems. There are roughly four types of issues it can help you solve:

### Consistent style or format that prompts cannot lock in

If you've written three pages of system prompt trying to explain your brand voice, and the model still drifts into generic assistant-speak by turn four, you can either fine-tune or switch to a model with stronger instruction following out of the box. Style is something a model picks up from many examples more reliably than from explicit instructions.

### Smaller and cheaper inference

Suppose you can get frontier-model quality on your task using a 20-page prompt. That long prompt is expensive on every call. A fine-tuned smaller model (e.g. Qwen3.5 9B) can often hit the same quality with a one-line prompt—cheaper per call, faster TTFT, less context used per request. At high call volumes, fine-tuning quickly becomes worth the cost in these cases.

### A behavior the base model resists

Sometimes the base model has been trained against the behavior you want (also known as refusal training). The model might be too cautious about a particular domain and refuse to respond, too verbose, or too quick to add disclaimers. Prompting can soften these tendencies. Fine-tuning on examples of the behavior you actually want provides more direct leverage.

### Patterns, not facts

Fine-tuning is not the way to teach a model new facts. If the problem is "the model does not know our product catalog", the right answer is retrieval-augmented generation (RAG), not training. But if the gap is about *patterns* rather than *looked-up facts* (e.g. "the model does not know how our internal ticketing taxonomy works"), fine-tuning can help.

## The real costs of fine-tuning

The most visible downside of fine-tuning is the cost of the training run itself, which is often not actually all that expensive. But there are some less-visible costs that can be much more significant:

* **The dataset:** You need labeled examples to train a fine-tune, hundreds at minimum, usually thousands. Building a good dataset can take longer than the rest of your entire project, and a bad dataset will produce a model that confidently does the wrong thing.
* **The evaluation set:** Without a witheld dataset for evaluation, you have no way to know whether the fine-tune actually improved or degraded the model behavior. You need an eval set regardless of whether you fine-tune, but most teams discover this the hard way after their first run.
* **Iteration cycles:** Tweaking the prompt and re-running takes seconds. Tweaking the data/hyperparameters and re-training can take hours to days. Mistakes are more expensive for fine-tuning than context engineering.
* **Base model drift:** When the base model for your fine-tune gets upgraded to a new version, your fine-tune will still be stuck on the old base. You either re-train from the new base (more work) or stay on the old base and miss out on the improvements.
* **Hosting:** A fine-tuned model needs somewhere to run. On Together, you can [deploy a fine-tuned model](/docs/deploying-a-fine-tuned-model) to a [dedicated endpoint](/learn/choosing-a-deployment-option).

## Flavors of fine-tuning

Modern fine-tuning is not a single technique but a small family of them. Here are the ones you'll likely see in the wild:

* **Supervised fine-tuning (SFT):** The classic approach. You give the model input/output pairs and it learns to imitate the outputs. Good for style, format, and pattern-matching tasks.
* **LoRA / QLoRA:** Parameter-efficient fine-tuning. Instead of updating all of the model's weights, you train a small "adapter" alongside the base model. Much cheaper to train, much smaller artifact, and you can swap adapters for different behaviors without re-hosting the base. Most production fine-tuning today is actually LoRA.
* **Preference fine-tuning (DPO / RPO / KTO):** Trains on pairs of "better" and "worse" outputs instead of single targets. Useful for shaping tone, formatting, refusal behavior, anything where you can rank outputs more easily than write ideal ones from scratch.
* **Reinforcement fine-tuning (RFT) / RLVR:** Used for tasks where the answer can be checked automatically (math, code that passes tests, structured extraction). The model gets a reward signal based on whether it was right, not on whether it sounded right. This is the family of techniques behind modern reasoning models.

For most teams, LoRA SFT is the right starting point. You only need to reach for preference tuning or RFT if SFT does not give you what you want. To start a run on Together, see [fine-tuning](/docs/fine-tuning-overview).

## Before you train

Before you kick off a fine-tune, you should have:

1. **A specific failure mode:** "The model is worse than I'd like" is not enough. "It drifts off-brand after turn 3" or "it adds disclaimers we don't want" is specific enough to actually fix.
2. **A prompt-only baseline you have genuinely pushed on:** Spend a day on the prompt before spending a week on data.
3. **An eval set:** 50–200 examples with the expected behavior labeled. Without this, you cannot tell whether the fine-tune helped, hurt, or did nothing.
4. **A budget:** Dollars, plus willingness to maintain the fine-tune through base-model upgrades, dataset drift, and edge cases.
5. **Volume:** At 50 calls a day, the per-call savings from a fine-tune will not pay back the work. At 50,000 calls a day, they will.

<Info>
  A rough rule of thumb: If a clever person on your team can write a prompt that gets you 90% of the way in a week, fine-tuning will buy you the last 10% at roughly 10× the cost in time and ongoing maintenance—but that trade is sometimes worth it.
</Info>

## Next steps

<CardGroup>
  <Card title="Context engineering" icon="messages" href="/learn/prompt-engineering">
    Try this before fine-tuning.
  </Card>

  <Card title="Choosing a deployment option" icon="server" href="/learn/choosing-a-deployment-option">
    How to host a fine-tuned model.
  </Card>

  <Card title="Quantization" icon="zoom-in" href="/learn/quantization">
    How to make a fine-tuned model cheaper to serve.
  </Card>
</CardGroup>
