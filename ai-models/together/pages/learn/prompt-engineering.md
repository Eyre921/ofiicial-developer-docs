---
title: "Context engineering"
source: https://docs.together.ai/learn/prompt-engineering
path: learn/prompt-engineering
---

How to structure context for chat, RAG, and coding agents.

**TL;DR:** The prompt you submit to a model is all that can see for a given call. Besides its weights, the model does not have any outside memory, or any hidden context. What you put in the prompt is the entire context for that call. Structuring that context so it carries every relevant detail and instruction is the main lever you have to impact output quality. For chat applications this includes the system prompt, previous `user` and `assistant` turns, as well as retrieved chunks in the case of retrieval-augmented generation (RAG). For coding agents, this includes the system prompt, your `AGENTS.md`, tools, memory, skills, previous turns of reasoning, tool calls, and user and assistant responses.

## What a prompt actually is

For a chat model, a "prompt" is the full list of messages you send to the API:

```text theme={null}
messages = [
  { role: "system",    content: "You are a helpful assistant..." },
  { role: "user",      content: "How do I revert a Git commit?" },
  { role: "assistant", content: "..." },
  { role: "user",      content: "And what if I already pushed?" }
]
```

Internally, all of those messages get concatenated into one long stream of tokens using the chat template, with role boundaries marked by special tokens (see [Tokens & tokenization](/learn/tokens-and-tokenization) for what those special tokens are). The model sees a single stream, not three separate messages. There is no memory or state between API calls; if you want the model to remember something from an earlier conversation, you have to include that information in the messages list.

By default, the model also has no live access to anything outside the prompt. It can't browse the web, read your files, see your screen, or check the current date. Everything the model knows comes either from its training data or from the current prompt. If you need the model to access context outside the immediate prompt, you give it tools (see [Function calling & tool use](/learn/function-calling-and-tool-use)).

## Specificity

The model cannot read your mind. If your prompt is vague, the model fills the gaps with plausible defaults, and those defaults will probably not be the ones you wanted. This is a common failure people experience when they give coding agents unspecific instructions.

Consider the difference between these two prompts:

<VagueVsSpecificDiagram />

The vague version will give you a summary of some length, in some tone, with some level of detail. The model chooses all of those for itself, and you have no way of predicting which choice it will make. The specific version, on the other hand, has a much smaller failure surface. The format is specified, the audience, length, and style are all specified, and the model should stay within those guardrails.

## Showing examples

Telling the model exactly what you want is good, but *showing* the model what you want, by including example inputs and outputs in the prompt, is even better. This technique is called **few-shot prompting**.

```text theme={null}
Classify the sentiment of each review as POSITIVE, NEGATIVE, or NEUTRAL.

Review: "Took forever to ship and the box was crushed."
Sentiment: NEGATIVE

Review: "Does exactly what it says on the tin."
Sentiment: POSITIVE

Review: "I bought it last Tuesday."
Sentiment: NEUTRAL

Review: "Was hoping for more but it works fine."
Sentiment:
```

A few examples can be more effective than a lot of instructions. The model picks up on patterns in the examples (format, tone, edge cases) and replicates those patterns in its own response. Two to five examples is enough for most tasks; you rarely need more than ten unless you are dealing with a complex extraction task with many possible structures.

This type of prompting will often work better for instruct/non-reasoning models, while specificity works better for reasoning models.

## Adding structure

For long prompts, adding some structure to the prompt helps the model find the right piece of context at the right time. There are two patterns that tend to pay off in practice.

### Use headings and delimiters

```text theme={null}
### CONTEXT
The user has uploaded a CSV with 3 columns: name, age, city.

### TASK
Write a Python function that returns a dict mapping city to the
average age in that city.

### CONSTRAINTS
- Use only the standard library.
- Handle empty input by returning {}.
- No type hints.
```

Heading-style sections, or XML tags like `<context>...</context>`, help the model treat instructions, examples, and data as distinct sections rather than as one continuous block of text. Structured prompts are also easier for *you* to maintain over time, because you can find and update the right section without rereading the whole thing.

### Put critical context near the top and the bottom

Models tend to pay more attention to the beginning and end of a long input than to the middle (see [Context windows](/learn/context-windows) for more on this). If there's something that has to be true about every output, it's worth mentioning that constraint in the system prompt, and also restating it right before the user's question. This redundancy is annoying when you write the prompt, but it tends to produce more reliable outputs.

## Ordering content for cache hits

Coding agents like Claude Code live inside long-running sessions and rack up many prompts per task. Each of those prompts is mostly the same: the same system prompt, the same tools, the same `AGENTS.md`, the same project files. The only thing that really grows is the conversation. This is exactly the thing that **prompt caching** is built for. Providers cache the prefix of the prompt, and as long as the prefix is identical to a previous call, you skip recomputing it and pay a fraction of the cost. When done well, 90–95% of the context can be a cache hit and thus cost less time and money. On Together, prompt caching is enabled by default for [dedicated endpoints](/docs/dedicated-endpoints/settings).

The trick is putting everything in the right order: **static content first, dynamic content last**. For a coding agent this usually looks like:

1. **Static system prompt** and tool definitions
2. **`AGENTS.md` / `CLAUDE.md`**, project-level instructions
3. **Session context**, skills, open files, recent edits, current working directory
4. **Conversation**, messages, reasoning traces, and tool calls

Anything that almost never changes goes at the top, so it can be cached across every session in the workspace. Anything that changes every turn goes at the bottom. The further down the prompt a change happens, the more of the prefix survives in the cache, and the more sessions end up sharing a cache hit.

This ordering is easy to break. Common pitfalls include:

* **Timestamps in the static prompt:** Including the current date/time at the top makes every call unique, killing cache hits. Put timestamps near the bottom if needed.
* **Unordered tools:** If tools are not sorted, their order can vary and break the prefix. Always sort tools by name before serializing.
* **Changing tool definitions:** Modifying or reordering tools changes the prefix for everyone. Only append new tools; don't alter or insert into the static list.

<Info>
  The most important thing to keep in mind is that the *earliest change* to your prompt invalidates all cached tokens afterwards. You want to keep the prefix as stable as possible to maximize the cache hit ratio. Only put volatile info (time, user message, current file) in the dynamic tail, not the static, cached head/prefix.
</Info>

## Next steps

<CardGroup>
  <Card title="Structured outputs & JSON mode" icon="braces" href="/learn/structured-outputs">
    For when "output JSON" in the prompt is not enough.
  </Card>

  <Card title="Function calling & tool use" icon="tools" href="/learn/function-calling-and-tool-use">
    For letting the model access data beyond the prompt.
  </Card>

  <Card title="Fine-tune vs. prompt" icon="git-branch" href="/learn/finetune-vs-prompt">
    The next step when prompt engineering hits a ceiling in performance.
  </Card>
</CardGroup>
