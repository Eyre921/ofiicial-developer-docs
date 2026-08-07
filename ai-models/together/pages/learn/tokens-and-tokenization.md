---
title: "Tokens & tokenization"
source: https://docs.together.ai/learn/tokens-and-tokenization
path: learn/tokens-and-tokenization
---

How tokenization works, what the model reads, and why tokens drive cost and context usage.

**TL;DR:** A model never reads actual words or characters. It reads tokens, subword chunks of about four characters each, where every chunk has a fixed integer ID. Tokenization is the deterministic step that turns your text into those IDs before the model ever sees it. Understanding this step matters because you pay per token, and filling your LLM's context window with the right tokens makes all the difference for generating useful outputs.

<a href="https://tiktokenizer.vercel.app/">
  <img alt="Tokenized example: &#x22;What are the top 3 things to do in NYC?&#x22; split into 12 tokens with integer IDs shown. Click to open tiktokenizer.vercel.app." />
</a>

<p>
  Try it yourself at <a href="https://tiktokenizer.vercel.app/">tiktokenizer.vercel.app</a>.
</p>

## How a model "reads"

When you read English fluently, you don't sound out every letter. You see "the" and "have" and "tokenization" as single shapes, and your brain pulls up the meaning in one go. The rare and unfamiliar parts, like "antidisestablishmentarianism" or "solidgoldmagickarp", you slow down and parse in chunks: *anti-dis-establish-ment-arian-ism* or *solid-gold-magic-karp*.

A tokenizer does roughly the same thing for an LLM. Common strings get a single ID, rare ones get broken into a handful of subword pieces, and anything weirder than that falls back to individual bytes. Every model's vocabulary is fixed and determined by the tokenizer—once the tokenizer is trained, nothing more about it is learned at inference time.

The trade-off between token length and vocabulary size is straightforward: Using characters as tokens give you a tiny vocabulary but absurdly long sequences, and the model has to re-derive "h-e-l-l-o means hello" every single time. Using whole words as tokens gives you short sequences but a vocabulary of millions, including separate tokens for typos, novel words, URLs, and rare names. Subwords strike a sweet spot between these two extremes: models typically have \~50,000 to 200,000 tokens in their vocabulary, so every possible input is representable, but common text stays short.

A rough rule of thumb for English is that one token ≈ 4 characters ≈ ¾ of a word. So 1,000 tokens is roughly 750 words, or one short page.

## What tokenization actually does

Tokenization is a two-step process: first, splitting the text into chunks, then looking each chunk up in a table to get an integer ID.

```text theme={null}
"Hello, world!"  →  ["Hello", ",", " world", "!"]  →  [9906, 11, 1917, 0]
```

Notice three things about this example:

* `Hello` and ` world` (with a leading space) are each one token. The space matters and travels with the word.
* `,` and `!` are their own tokens. Punctuation almost always is, because it's common enough to warrant its own token ID.
* The IDs are lookup indices into a fixed vocabulary. There's no math here, no learning. The same text always produces the same IDs, every time.

Different models use different tokenizers, so the same string can produce different IDs across model families like GPT-5.5, Claude Opus 4.8, and DeepSeek-V4. Within one model family, the tokenizer is typically fixed and baked in at pretraining time.

## Byte pair encoding (BPE)

Almost every modern tokenizer is built using an algorithm called **byte pair encoding (BPE)**. The training procedure is as follows:

1. Start with a vocabulary of every distinct byte (or character).
2. Across the training corpus, count every pair of adjacent tokens.
3. Take the most common pair, merge it into a new token, and add it to the vocabulary.
4. Re-tokenize the corpus using the new vocabulary.
5. Repeat until the vocabulary reaches the target size (typically anywhere between 50,000 and 200,000 unique tokens).

The list of merges is saved in order. At inference time, encoding a new piece of text means applying the same merges in the same order. Fast, deterministic, no model required.

<BpeDiagram />

## Special tokens

Beside the BPE-trained vocabulary, every model reserves a few IDs for special tokens. These tokens never come from user text. The model has been trained to treat them as boundaries:

* `<|bos|>`, `<|eos|>`: start and end of the stream.
* `<|user_start|>` & `<|user_end|>`: plus the assistant pair, turn boundaries.
* `<|tool_call|>`, `<|tool_response|>`: tool boundaries (different models name them differently).

A multi-turn chat ends up laid out for the model like this:

```text theme={null}
<|bos|>
<|user_start|>What are the top 3 things to do in NYC?<|user_end|>
<|assistant_start|>Visit the Met, walk the High Line, and...<|assistant_end|>
<|user_start|>What about Brooklyn?<|user_end|>
<|assistant_start|>
```

Notice the last line. It opens an assistant turn and doesn't close it. That trailing special token is the cue that tells the model "it's your turn to generate tokens until you emit `<|assistant_end|>`." Almost the entire chat UX is two special tokens and a streaming loop.

<Warning>
  Special tokens are why you should never paste raw user input directly between role markers. If a user message literally contains the bytes `<|user_end|>`, a careless tokenizer might honor them and the user has impersonated the system role. Production tokenizers treat these as ordinary text unless you explicitly ask them to parse.
</Warning>

## The same word is not always the same token(s)

When converting text to tokens, details like casing, whitespace, and punctuation all matter. The tokenizer doesn't make semantic judgments. It does a greedy lookup against a fixed table, and that table was trained on whatever happened to appear in the corpus. So the strings below, which a human reads as variants of one word, become different sequences of token IDs:

```text theme={null}
"apple"   → [28202]
" apple"  → [24149]
"Apple"   → [27665]
" Apple"  → [8325]
"APPLE"   → [8193, 877]
" apples" → [24149, 82]
"apples." → [680, 645, 13]
```

The model usually handles this gracefully because these variants co-occur in training, but it's also why the model can respond slightly differently to different prompt phrasing. If you move a single space, the model is conditioning on a different token sequence, which can lead to different outputs.

<VariantsDiagram />

## Cost and context

Two of the most important numbers in any model specification are quoted in token counts, not words:

* **Context window:** The maximum number of tokens the model can see in one request (input + output combined). To give you an idea, \~8K tokens is a long email, 200K tokens is a small book, and 10M tokens is a small library. See [context windows](/learn/context-windows) to learn more.
* **Price:** This is usually quoted per million tokens, with separate rates for input, output, and cached tokens. Output is typically 3-4× more expensive than input because generating tokens one at a time is the slow phase of inference. See [TTFT & TPS](/learn/ttft-and-tps) and our [serverless model pricing](/docs/serverless/models) page to learn more.

Here's a rough guide for token counts:

```text theme={null}
1 token    ≈  ¾ of a word     ≈  4 characters
100 tokens ≈  75 words        ≈  half a paragraph
1K tokens  ≈  750 words       ≈  one page
8K tokens  ≈  6,000 words     ≈  a long article
128K       ≈  96,000 words    ≈  a short novel
1M         ≈  750,000 words   ≈  Lord of the Rings + appendices
```

<TokenBudgetDiagram />

## Where tokenization gets weird

Once you start counting tokens, you'll notice some quirks:

* **Numbers:** "1234" may be one token, "12345" two, and "9999999999" several. The model can't reliably see digit positions because they aren't single tokens. This is one of the reasons large arithmetic is unreliable without chain-of-thought or a tool call to a calculator function.
* **Code:** Common keywords (`def`, `return`) are single tokens, but unusual identifiers fragment. Indentation, brackets, and newlines each cost a token, which is why code prompts are surprisingly token-heavy.
* **Non-English text:** Most tokenizers were trained on corpora that are 70-90% English. A Korean or Hindi sentence can take 2-4× more tokens than its English translation, which means higher cost and smaller effective context. Newer tokenizers have improved this meaningfully, but the gap still exists.
* **Repeated whitespace:** JSON pretty-printed with indentation can be meaningfully more expensive than the same JSON minified.
* **Emoji and rare Unicode:** Most emoji are multi-byte. Less common ones can take 4-6 tokens for a single emoji.

<Tip>
  When a prompt feels too long or a reply stops mid-thought, paste the input into a [tokenizer playground](https://tiktokenizer.vercel.app/) and look at the actual count. It's almost always 1.3-2× what you expected, especially with system prompts, JSON, or non-English content.
</Tip>

## Next steps

<CardGroup>
  <Card title="How LLMs work" icon="cpu" href="/learn/how-llms-work">
    What the model does with these IDs once it has them.
  </Card>

  <Card title="Context windows" icon="layout-board" href="/learn/context-windows">
    The consequences of a finite token budget.
  </Card>

  <Card title="Inference metrics: TTFT & TPS" icon="dashboard" href="/learn/ttft-and-tps">
    Why long inputs are slow to start, and long outputs are slow overall.
  </Card>
</CardGroup>
