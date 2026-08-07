---
title: "Inference parameters & sampling"
source: https://docs.together.ai/learn/inference-parameters-and-sampling
path: learn/inference-parameters-and-sampling
---

Temperature, top-k, top-p, and the other knobs that shape how a model picks each next token.

**TL;DR:** At every step of generation, the model produces a probability for every possible next token in its vocabulary. Sampling is the process of picking one of those tokens to actually use. Temperature, top-k, top-p, and a few penalty controls are different ways of shaping that probability distribution before you pick from it. They do not change the model itself, they only change how you draw a token from the model's output distribution.

## Why sampling exists at all

Imagine the model is choosing the next word in this sentence: "The capital of France is \_\_\_". The model assigns very high probability to "Paris", lower probability to "France", "Lyon", "Marseille", and "Brussels", and very small slivers of probability to the rest of its \~200,000-token vocabulary.

You could pick "Paris" every single time. This works perfectly well for factual questions where there is one obvious correct answer. But if you try the same strategy on a prompt like "Write me a poem about loneliness \_\_\_", you will get the same stale rhymes that the model assigns the highest probability to, every single time. The "right" word in creative or open-ended writing is rarely the highest-probability word, because the highest-probability word is the most predictable one and predictable writing is usually boring.

Sampling lets you choose between two extremes. On one end is textbook mode, where you always pick the most probable word. On the other is a more creative mode, where you sometimes pick a less expected word to get more variety. The controls in this section move you between those two ends.

<SamplingDistributionDiagram />

## Greedy decoding

The most basic sampling strategy is to pick the highest-probability token every single time. This is called **greedy decoding** and on most APIs it is equivalent to setting `temperature = 0`. Greedy decoding can be repetitive or bland. Because you always pick the top option, the model never tries any of the moderately likely alternatives, and the output can read as generic.

Greedy decoding is the right default for tasks like information extraction, classification, and any task where there is clear single correct answer.

## Temperature

Temperature is the most commonly used sampling parameter. It works by dividing the logits by a temperature value before the softmax converts them into probabilities. The effect on the resulting distribution looks like this:

* `temperature = 0` is equivalent to greedy decoding. The model always picks the maximum value token.
* `temperature = 1.0` gives you the model's unaltered distribution. This is the distribution the model would naturally produce based on its training.
* `temperature < 1` sharpens the distribution. The most likely tokens become even more likely, and the long tail of unlikely tokens gets suppressed. The output becomes more focused and less surprising.
* `temperature > 1` flattens the distribution toward uniform. The output becomes more creative and more random, but also more likely to go off the rails.

As a rough starting point, you might use `0` for anything factual, `0.7` for general chat, and `0.9 to 1.2` for creative writing. Above about `1.5`, the model tends to produce strange outputs regardless of the prompt, so it is rarely worth going any higher. Model providers usually publish recommended defaults for temperature and the controls below—when they do, stick to those values for optimal results.

## Top-k and top-p

Even with a sensible temperature, a 200K-token vocabulary has a very long tail of very unlikely tokens. Sampling can occasionally land on one of those tail tokens, which might make the output go somewhere strange. Top-k and top-p are two different ways to ignore the tail before sampling, so that the model can only pick from a reasonable shortlist.

### Top-k

Top-k works by sorting all of the tokens by probability, keeping the top *k* of them, and throwing away the rest. After truncating to the top *k* tokens, the remaining probabilities are renormalized to sum to 1, and you sample from that shortened distribution. Setting `top_k = 20` means "only ever consider the 20 most likely next tokens".

Top-k is straightforward and reliable. The downside is that the "right" number of plausible tokens varies a lot from step to step. Sometimes there are only 3 obvious candidates and many noisy ones, in which case top-k is keeping more than you need. Other times there are 200 reasonable candidates and your top-k of 20 has thrown away 180 of them.

### Top-p (nucleus sampling)

Top-p works a little differently. You sort the tokens by probability, then keep the smallest set of tokens whose probabilities together add up to *p*. You sample from that set. Setting `top_p = 0.9` means "consider the smallest group of tokens that together hold 90% of the probability".

Top-p adapts to the shape of the distribution at each step. When the model is very sure about the next token, the set that adds up to 90% is small. When the model is uncertain, the set grows to include more candidates. This adaptive behavior often makes top-p a better default than top-k.

You can use both together. Most APIs let you set either parameter independently, and some platforms apply top-k first and then top-p.

## Repetition, presence, frequency penalties, and logit bias

Models sometimes get stuck repeating the same phrase or word over and over. There are several controls that let you influence the token distribution during generation, including penalties and direct logit biasing:

* **Frequency penalty:** Each occurrence of a token in the output so far reduces that token's logit a little. The more times you have used the word "however", the less likely "however" is to come up again on the next step.
* **Presence penalty:** Any token that has appeared at all gets its logit reduced by a fixed amount. Presence penalty does not care how many times the token appeared—it only checks whether it's appeared at all.
* **Repetition penalty:** This is the same idea applied multiplicatively to the logits rather than additively. Repetition penalty is more common in open-source models than in OpenAI-style APIs.
* **Logit bias:** This parameter lets you directly adjust the likelihood of specific tokens appearing in the generated output. For example, you can strongly encourage or almost entirely ban certain words or pieces of text from appearing by pushing their probabilities up or down before sampling. This can be done alongside penalties or on its own.

All of these controls should be used sparingly. If you apply too much penalty or bias, the model will strain to avoid common or important words, hurting fluency in ways worse than the original repetition. For logit bias, start with small adjustments unless you are intentionally trying to force or block a token entirely. If the output starts feeling forced or unnatural, dial the penalties and biases back.

## Seed and determinism

Sampling uses a random number generator under the hood. If you fix the seed, the same input produces the same output across runs. This is useful for testing, debugging, and reproducible evaluation runs.

An important caveat worth knowing is that even with a fixed seed, hardware and batching can introduce small amounts of non-determinism. Different concurrent requests can subtly affect floating-point order, which means "deterministic" in practice means "deterministic most of the time but not always". In practice, the same call repeated several times can return slightly different logits.

## What changes for reasoning models

Modern **reasoning/hybrid models** produce a long internal chain of thought before they give you a final answer. Most of these models ship with recommended sampling settings, which you should almost certainly use. Performance degrades noticeably when you override the provider's recommendations.

The exact behavior varies significantly across models, so it is worth checking the model card before you tune these controls on a hybrid or reasoning model.

## What to pick for what

Here are reasonable starting points by task. For the exact request fields, see [inference parameters](/docs/inference/chat/parameters).

* **Extraction, classification, structured output:** Use `temperature = 0`. You want one right answer and you want it to be reproducible.
* **General chat or assistant tasks:** Use `temperature = 0.7` and `top_p = 0.9`. This is a safe middle ground for most use cases.
* **Creative writing or brainstorming:** Use `temperature = 0.9 to 1.1` and `top_p = 0.95`. Let the model breathe a bit and explore less predictable options.
* **Code generation:** Use `temperature = 0.1 to 0.3`. Coding demands precision. A little randomness can help when the model is stuck, but most of the time you want the model's best guess rather than a creative one.
* **Reasoning/hybrid models:** Check to see if the model provider recommends a setting for the sampling parameters in reasoning and non-reasoning modes.

<Tip>
  If your output is bad, the first thing to check is the prompt, not the sampling. Sampling controls are a small intervention compared to the prompt itself. You should get the prompt right first, then tune sampling only if you have a specific complaint about the output (too repetitive, too random, too generic).
</Tip>

## Next steps

<CardGroup>
  <Card title="Context engineering" icon="messages" href="/learn/prompt-engineering">
    The biggest lever on output quality.
  </Card>

  <Card title="Structured outputs & JSON mode" icon="braces" href="/learn/structured-outputs">
    Constrain outputs to a schema.
  </Card>

  <Card title="How LLMs work" icon="cpu" href="/learn/how-llms-work">
    Where logits come from in the first place.
  </Card>
</CardGroup>
