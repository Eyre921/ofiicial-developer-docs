---
title: "Using Secrets"
source: https://docs.fireworks.ai/fine-tuning/using-secret-in-evaluator
path: fine-tuning/using-secret-in-evaluator
---

Learn how to create secrets that can be utilized within your reward function.

# Creating Secrets

<Steps>
  <Step title="Navigate to the secrets page on your dashboard">
    <img alt="new.png" />
  </Step>

  <Step title="Create a new secret">
    <img alt="test.png" />

    All secrets created here will be injected as environment variables for your Evaluator to access.
  </Step>

  <Step title="Update the Evaluator to access the new secret">
    <img alt="openai_secret.png" />
  </Step>
</Steps>

And that's it! If you want to learn more about creating evaluators, see:

1. Learn about [Evaluation](/fine-tuning/evaluators) and [Eval Protocol](https://evalprotocol.io/introduction) for evaluator authoring
