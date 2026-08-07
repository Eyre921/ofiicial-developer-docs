---
title: "Structured outputs & JSON mode"
source: https://docs.together.ai/learn/structured-outputs
path: learn/structured-outputs
---

Force the model to produce schema-valid output.

**TL;DR:** Structured outputs let you force a model to produce valid JSON as output (or any other schema you specify). The mechanism works at the [sampler level](/learn/inference-parameters-and-sampling): at every generation step, any token that would break the schema has its probability zeroed out, which means the model literally cannot pick those tokens. The output you get back is guaranteed to be parseable in the shape you asked for. This is the same constrained-decoding machinery that's used under the hood for tool/function calling.

## How it works

Structured decoding works by combining two mechanisms: prompting the model to produce a particular response shape, and making the inference engine enforce that shape one token at a time during generation. The model still has freedom for the parts that aren't constrained, but the *structure* of the output is no longer up for negotiation.

This distinction matters most when you're processing multiple responses programmatically. If your pipeline depends on the LLM always outputting JSON, the only scalable solution is to constrain the decoding space of tokens so that generating outputs with an incorrect structure is literally impossible. Prior to constrained decoding libraries like Outlines and XGrammar becoming popular, the common (and much less performant) approach was to prompt and retry until the model output matched the correct structure, or you hit your budget for retries.

## Constrained decoding

Language model generation happens one token at a time. At each step, the model produces a logit for every token in the vocabulary, softmax converts those logits into probabilities, and the sampler picks one of the tokens to add to the output (see [Inference parameters & sampling](/learn/inference-parameters-and-sampling) for the details).

Constrained decoding adds an extra step in between the logits and the sampler. The constraint engine looks at the output the model has produced so far, figures out which tokens would still produce valid JSON (or schema-valid JSON), and sets the logits for all the other tokens to `-∞`. A logit of `-∞` becomes a probability of zero after the softmax, which means the sampler cannot pick that token. Because the constraint is enforced at the sampler rather than asked for in the prompt, the invalid-output failure mode literally cannot happen.

See [Structured outputs](/docs/inference/chat/structured-outputs) for details on how to enable this for your requests on Together AI.

<LogitMaskDiagram />

## When constraints can hurt the result

Constraining the output can be extremely powerful and useful, but is not always ideal. There are two things worth watching for.

The first is **over-constraint**. If your schema only allows three enum values, but the correct answer for the input is actually a fourth value, the model has no choice but to give you a wrong answer. The constraint engine will produce *something* that is valid against the schema, because it cannot produce "none of these". You can avoid this by always including an escape hatch in your schemas, such as an `"other"` value, for classifications you might not have fully enumerated.

The second is **tunnel vision**. Forcing the model into JSON shape from the very first token can hurt the quality of its reasoning. For complex tasks, the best results often come from a structure where the model thinks in natural language first ("Let me consider the options...") and then produces the structured answer at the end. For this purpose, reasoning models have their reasoning tokens unconstrained and the structured outputs only apply to their output content tokens.

<Info>
  Structured output is not magic. It's a constraint at the sampler level, not a quality booster. If the underlying model does not know the answer to your question, no amount of schema enforcement will fix that. You'll get a confidently wrong answer that happens to come in a schema-valid shape.
</Info>

## When to use it

Structured outputs can be use in a number of common production patterns:

* **Extraction:** Tasks like "pull the name, email, and order total out of this support ticket". You define a schema for the fields you want, and the model fills it in. This pattern skips the parsing-regex hell that extraction usually entails.
* **Classification with confidence:** A schema like `{ category: enum, confidence: number }` gives you both a label and a way to threshold low-confidence predictions before acting on them.
* **Routing:** A question like "which of these 8 tools should handle this query?" is well-suited to enum-typed output, which is guaranteed to produce a valid option.
* **Form-filling agents:** You can step through a structured response in stages (intent → fields → action). Each step uses a schema appropriate for that turn of the conversation.
* **Function calling under the hood:** [Function calling](/learn/function-calling-and-tool-use) is actually built on the same constrained-decoding machinery. The schema in that case is the parameter spec for the function being called.

## Next steps

<CardGroup>
  <Card title="Function calling & tool use" icon="tools" href="/learn/function-calling-and-tool-use">
    Same constraint engine, different purpose.
  </Card>

  <Card title="Inference parameters & sampling" icon="adjustments" href="/learn/inference-parameters-and-sampling">
    What sampling looks like before constraints are applied.
  </Card>

  <Card title="Context engineering" icon="messages" href="/learn/prompt-engineering">
    When a schema isn't enough and the prompt is your real constraint. When a schema isn't enough, the prompt be w more. When a schema isn't enough, the prompt be w more.
  </Card>
</CardGroup>
