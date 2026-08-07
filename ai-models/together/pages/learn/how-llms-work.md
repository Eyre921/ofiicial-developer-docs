---
title: "How LLMs work"
source: https://docs.together.ai/learn/how-llms-work
path: learn/how-llms-work
---

How a large language model produces text from a prompt, one token at a time.

**TL;DR:** An LLM is a series of calculations that, when applied to input text, produce output text. You give it some text, it turns the text into numbers, runs the numbers through a big stack of matrix multiplications, and gives you back a probability for every possible next word. Then it picks one and adds it to the end of the output. To produce a longer reply, it repeats this in a loop.

That's the whole top-level picture. Everything else on this page is detail on what makes this interesting: how text becomes numbers, what the matrix multiplications actually are, how to think about what a transformer does to input text, and what "training" a model actually means.

## What an LLM is trying to do

An LLM is, at its core, trying to build a statistical model of the language data it was trained on. The cleanest way to imagine what this means is to picture yourself in a familiar place:

<img alt="A Wheel of Fortune puzzle board showing 'ANOTHER FEATHER _N YO_R _A_' under the category PHRASE." />

Almost everyone fills in the missing letters instantly, spelling out: "another feather **in your cap**". But let's play devil's advocate for a second—why not "another feather **on your cat**"? It's a perfectly grammatical English sentence. Why does that completion not even occur to us?

Because you've heard the first phrase countless times, and never the second; because you know feathers go in caps and not on cats; because one has a known meaning and the other is nonsense. All of these factors contribute to the former being much more probable than the latter.

An LLM has direct access only to the first of these factors: raw frequency. The LLM has seen "feather in your cap" repeated in its training data orders of magnitude more often than "feather on your cat", and the probabilities it assigns to the next token reflect that. It does not *know* that feathers don't go on cats, but it was trained on enormous quantities of text written by humans who did, and the statistics it absorbed into its weights inherit that knowledge by proxy. The model approximates understanding by reproducing the statistical patterns of writers who actually had it.

## Calling an LLM API

Here is about the simplest call you can make on Together AI. We hand a text model the start of a sentence and ask it to continue, capped at a single token of output:

```python theme={null}
from together import Together

client = Together()

# Call the model
response = client.completions.create(
    model="Qwen/Qwen3.5-9B",  # Model ID
    prompt="The largest city in France is",  # Input text
    max_tokens=1,  # Maximum number of tokens to generate
)

print(response.choices[0].text)  # Print the output text
```

On the way in, your input text becomes a list of integers. A module called the **tokenizer** chops the prompt into *tokens*, chunks of text about four characters long, and looks up a fixed integer ID for each one. So `"The largest city in France is"` turns into something like:

```text theme={null}
[ 791, 7928, 3363, 304, 9822, 374 ]
```

This is a deterministic table lookup, not something the model learns at inference time. The model itself only ever maps integers to probabilities. It takes that list of indices and returns a probability for every possible *next* index:

```text theme={null}
input:  a list of integer indices  [ 791, 7928, 3363, 304, 9822, 374 ]
output: a probability for every possible next index
```

The output is a vector with one slot per token in the model's vocabulary (typically between 50,000 and 200,000 tokens). Each number in that vector represents the model's guess for how likely that token is to come next.

Because we asked for `max_tokens=1`, the inference engine takes the single most likely index, decodes it back to text, and hands you `" Paris"`. (In practice, you might need more than one token to reliably finish the sentence.)

To produce a longer reply, the inference engine repeats these steps in a loop:

1. Convert the current input into a list of integer indices (token IDs).
2. Run the model on the current input.
3. Look at the probabilities for the next token.
4. Pick the next token.
5. Add it to the end of the input.
6. Repeat until the model produces a stop signal or you hit a length limit.

The model itself is stateless—it doesn't remember anything between two separate questions unless you repeat yourself. Whatever it appears to "remember" is only because the inference loop keeps feeding the previous outputs back into the next call. The "memory" lives in the repeated turns of back-and-forth conversation, not in the model itself.

Let's break down the steps in more detail:

## Text becomes tokens, tokens become vectors

When the model receives your input text, it first converts it into a list of token IDs (integer indices). After that, it turns each ID into a **vector** or **embedding**: a list of floats, typically 1,024 to 16,384 long. The model has a learned lookup table that maps each token ID to a vector. That vector is the model's working representation of the token, or its "embedding".

Why is each token represented as a vector? Two reasons:

1. First, you can't do useful math on raw token IDs, ID 5279 and ID 5280 are arbitrary. With vectors, the model can express that "Paris" and "Lyon" are similar in some directions and different in others, literally by placing their vectors close together along the "city" axis and far apart along the "size" axis.
2. Second, the main operation throughout the model is a **matrix multiplication** (matmul): you multiply a vector by a **matrix** (a grid of numbers) to get a new, transformed vector, and that only works on vectors, not raw integer IDs. The numbers filling those matrices are the model's weights, so a "learned matrix" (a term that comes up later) just means one of these grids, with values found by training rather than set by hand.

## The transformer block

After the embedding step, every token is a vector, but that vector still only reflects the token in isolation. The embedding for "bank" is identical whether the sentence is "river bank" or "savings bank." The job of the transformer is to refine each vector until it captures what the token means *in this particular context*.

It does that by passing the vectors through *N* identical layers (blocks), where *N* is usually between 32 (small models) and 120+ (frontier models). Every block runs the same two steps:

1. **Attention:** Each token gathers information from the earlier tokens in the sequence and folds the relevant parts into its own vector. This is the only step where tokens exchange information.
2. **Feed-forward network (FFN/MLP):** Each token's vector is then processed on its own, with no reference to the others. This is where the model applies the knowledge stored in its weights to the now-contextualized vector.

A useful shorthand is "communicate, then compute": attention moves information *between* tokens, the feed-forward network does the heavy processing *within* each token. The next block repeats both steps on the result, and the next, and so on through all *N* layers.

The vector that flows down this stack is often called the **residual stream**, because each block doesn't overwrite it but *adds* a correction to it (a **residual connection**). So the representation of "bank" isn't rewritten from scratch at every layer; it accumulates. Early blocks tend to resolve local, surface-level structure (which word attaches to which, basic grammar), and later blocks build up the more abstract, meaning-level features the final prediction depends on. By the last block, the vector at each position is a context-aware summary of everything the model needs in order to predict what comes next.

## Attention

For each token, the attention step computes three things from the token's current vector by multiplying it with three different learned matrices:

* A **query (Q)**, "what am I looking for?"
* A **key (K)**, "what do I look like to others?"
* A **value (V)**, "what do I have to share?"

Then, for each token's query, the model measures how closely it matches every earlier token's key using a dot product. Those match scores are normalized into weights that sum to 1, so the closest matches get the most weight. The token then pulls in a weighted average of those tokens' values, and that blend is the update attention adds to its vector.

Three things to know about attention:

1. **Causal mask:** A token at position 5 can only look at positions 0-4. Never the future. That's what makes the model autoregressive: At training time, it can't peek at the next word it's supposed to predict, and at inference time, it can't look at tokens that haven't been generated yet.
2. **Multi-head:** This whole process runs in parallel many times (typically 32-96 "heads"), with different learned matrices each. Different heads end up specializing in different patterns—one might track the most recent noun, another might find matching brackets in code, another the subject of the current clause.
3. **Q, K, and V are learned matrices:** The interpretation of Q, K, and V above is a useful analogy for explaining what attention does, but in practice it's all matrix multiplication. The model figures out what to put in those matrices during training, purely from the process of trying to predict the next word.

Below is an example of what this might look like for the sentence "The cat sat on the mat." Each row represents one query position. Colored cells are the earlier tokens it pays the most attention to.

Click on any row to see the attention weights for that token:

<AttentionMatrixDiagram />

The pattern you see demonstrates what one head might learn during the attention step. A real model has many of these running in parallel per layer, each picking up something different.

## Feed forward network (FFN)

After attention has mixed information across tokens, the feed forward network (FFN) (AKA multilayer perceptron, or MLP) processes each token's vector on its own. It widens the vector (typically to 4× its size) by multiplying it with one matrix, applies a nonlinear function, then narrows it back down with another matrix.

This is where most of the parameters in the model actually live. By raw count, the feed forward network layers dwarf the attention layers. A useful way to think about it is that this is where the model stores all of its knowledge about the world. The widening step is like asking many questions about the token's current state in parallel, while the narrowing step writes back the answers.

Most of the model's "world knowledge"—what cities are capitals, which functions Python has, that one programming language uses curly braces and another uses indentation—is stored in the feed forward network weights. Nobody has a clean understanding of which weight stores what exactly, because the patterns are distributed across millions of neurons in ways no one fully understands. The entire field of **interpretability** is trying to answer exactly this question.

## Picking a token

After the last block, each position holds a vector that summarizes everything the model thinks up to that point. To turn this into a prediction for the next token, one final linear layer projects the vector back to the vocabulary, producing one number for each possible next token. These numbers are called **logits**.

Logits are raw scores, not probabilities, and they can be any real number, including negative ones. To turn them into probabilities, you apply a **softmax** operation: exponentiate each logit and normalize. This ensures that the probabilities are all positive and sum to 1 (which is a requirement for a valid probability distribution).

Then you pick / sample a token. The most basic choice is to pick the highest-probability token (greedy decoding), but several controls—temperature, top-k, and top-p—shape the distribution before sampling. See [inference parameters & sampling](/learn/inference-parameters-and-sampling) for more details.

## What training actually does

Everything covered above—the matmuls, the attention, the FFN / MLPs, the softmax—is fixed and constant. The model's behavior comes from the numbers inside those matrices. Those numbers are called **weights**. They start off random, and during the training process, the model searches for useful values for each weight. This process of taking the weights from random initializations to useful values is called **pretraining**, and it costs millions of dollars in compute, can take months to complete.

Pretraining works like this:

1. Take a document from the training data (anything from Wikipedia to GitHub to chat logs).
2. For every position in that document, ask the model what comes next.
3. Compare its prediction to the actual next token. The mismatch between the prediction and the actual next token is called the **loss**.
4. Compute how much each weight contributed to the loss.
5. Nudge each weight a tiny bit in the direction that would have reduced the loss. This is called **backpropagation**.

Repeat this process over trillions of token-positions (DeepSeek V4, for example, is trained on 32 trillion tokens) across most of the public internet. The model isn't memorizing the training set, it's adjusting its weights so the statistical patterns that show up across all those documents get reproduced when it generates.

Pretraining is usually followed by three more stages:

* **Instruction tuning:** Training the pretrained model on examples of "good behavior" (helpful answers, polite refusals, structured output) so it stops continuing text and starts responding to instructions.
* **Preference tuning:** Approaches like reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO) run a feedback loop where pairs of "good" and "bad" outputs nudge the model toward outputs people actually want.
* **Reinforcement learning with verifiable rewards (RLVR):** Training on tasks whose answers can be checked automatically (math problems, code that passes tests, puzzles with a known solution), so the model gets rewarded for actually being right rather than for sounding right. This is the trick behind modern "reasoning" models that think out loud before answering.

By the end, what you have is a few billion to a few trillion weights. The architecture is primarily the same for all models (with small modifications here or there) and the intelligence is in those numbers. This is what you can download from Hugging Face for open-weight models.

This is also what people mean when they say a model is "just" matrix multiplications. The compute all happens through matmuls, and the behavior is defined by the values inside those matrices. The architecture is compact enough to fit in a few hundred lines of Python. The behavior is rich because every weight has been tuned by hundreds of thousands of GPU-hours of next-token prediction.

## Next steps

<CardGroup>
  <Card title="Tokens & tokenization" icon="scissors" href="/learn/tokens-and-tokenization">
    What happens to the input text before the model sees it.
  </Card>

  <Card title="Context windows" icon="layout-board" href="/learn/context-windows">
    How much input the model can take in a single request (and why there's a hard limit).
  </Card>

  <Card title="Inference parameters & sampling" icon="adjustments" href="/learn/inference-parameters-and-sampling">
    Available controls for shaping the output.
  </Card>
</CardGroup>
